import collections
import sys
from typing import Tuple

from pywinauto.application import WindowSpecification
from pywinauto import findbestmatch

from autoinsight.ident.AutomationTyping import ElementsInfo


# TODO set the default value base on configuration
def _get_elements_info(self, depth=50, max_width=30) -> ElementsInfo:
    """
    Get all the UI elements

    The elements in the control and for its descendants to
    a depth of **depth** (the whole subtree if **None**).

    :param self: The instance of the WindowSpecification.

    :param depth: Max depth level of an element tree to dump (None: unlimited).

    :param max_width: Max number of children of each element to dump (None: unlimited).

    .. note:: The identifiers dumped by this method have been made
           unique. So if you have 2 edit boxes, they won't both have "Edit"
           listed in their identifiers. In fact the first one can be
           referred to as "Edit", "Edit0", "Edit1" and the 2nd should be
           referred to as "Edit2".
    """
    if depth is None:
        depth = sys.maxsize
    if max_width is None:
        max_width = sys.maxsize
    # Wrap this control
    this_ctrl = self._WindowSpecification__resolve_control(self.criteria)[-1]

    ElementTreeNode = collections.namedtuple('ElementTreeNode', ['elem', 'id', 'children'])

    def create_element_tree(element_list) -> Tuple[ElementTreeNode, bool, bool]:
        """Build elements tree and create list with pre-order tree traversal"""
        depth_limit_reached = False
        width_limit_reached = False
        current_id = 0
        elem_stack = collections.deque([(this_ctrl, None, 0)])
        root_node = ElementTreeNode(elem=this_ctrl, id=current_id, children=[])
        while elem_stack:
            current_elem, current_elem_parent_children, current_node_depth = elem_stack.pop()
            if current_elem is None:
                elem_node = ElementTreeNode(None, current_id, [])
                current_elem_parent_children.append(elem_node)
            else:
                if current_node_depth <= depth:
                    if current_elem_parent_children is not None:
                        current_id += 1
                        elem_node = ElementTreeNode(current_elem, current_id, [])
                        current_elem_parent_children.append(elem_node)
                        element_list.append(current_elem)
                    else:
                        elem_node = root_node
                    child_elements = current_elem.children()
                    if len(child_elements) > max_width and current_node_depth < depth:
                        elem_stack.append((None, elem_node.children, current_node_depth + 1))
                        width_limit_reached = True
                    for i in range(min(len(child_elements) - 1, max_width - 1), -1, -1):
                        elem_stack.append((child_elements[i], elem_node.children, current_node_depth + 1))
                else:
                    depth_limit_reached = True
        return root_node, depth_limit_reached, width_limit_reached

    # Create a list of this control, all its descendants
    all_ctrls = [this_ctrl]

    # Build element tree
    elements_tree, depth_limit_reached, width_limit_reached = create_element_tree(all_ctrls)
    txt_ctrls = None
    all_ctrl_index_names_map = None

    if self.allow_magic_lookup:
        # Create a list of all visible text controls
        txt_ctrls = [ctrl for ctrl in all_ctrls if ctrl.can_be_label and ctrl.is_visible() and ctrl.window_text()]

        # Build a dictionary of disambiguated list of control names
        name_ctrl_id_map = findbestmatch.UniqueDict()
        for index, ctrl in enumerate(all_ctrls):
            ctrl_names = findbestmatch.get_control_names(ctrl, all_ctrls, txt_ctrls)
            for name in ctrl_names:
                name_ctrl_id_map[name] = index

        # Swap it around so that we are mapped off the control indices
        all_ctrl_index_names_map = {}
        for name, index in name_ctrl_id_map.items():
            all_ctrl_index_names_map.setdefault(index, []).append(name)

    return ElementsInfo(ctrlTreeRoot=elements_tree,
                        textCtrls=txt_ctrls,
                        allCtrlIndexNameMaps=all_ctrl_index_names_map,
                        allCtrl=all_ctrls)


WindowSpecification.get_elements_info = _get_elements_info
