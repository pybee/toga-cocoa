from rubicon.objc import *

from toga.interface import Container as ContainerInterface

from ..libs import *
from .base import WidgetMixin


class TogaContainer(NSView):
    @objc_method
    def isFlipped(self) -> bool:
        # Default Cocoa coordinate frame is around the wrong way.
        return True

    @objc_method
    def display(self) -> None:
        self.layer.setNeedsDisplay_(True)
        self.layer.displayIfNeeded()


class Container(ContainerInterface, WidgetMixin):
    def __init__(self, id=id, style=None, children=None):
        super().__init__(id=id, style=style, children=children)
        self._create()

    def create(self):
        self._impl = TogaContainer.alloc().init()
        self._impl._interface = self

        # self._impl.setWantsLayer_(True)
        # self._impl.setBackgroundColor_(NSColor.blueColor())

        self._add_constraints()
