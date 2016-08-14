from abc import ABCMeta, abstractmethod


class Visitor(metaclass=ABCMeta):
    """
    Abstract Visitor class as part of the Visitor Design Pattern.
    """
    def visit(self, node, *args, **kwargs):
        """
        Visit the visitor with some object.

        @param node: An object to call a visitor method with.
        @param args: Arguments to go with the visitor method call.
        @param kwargs: Keyword arguments to go with the visitor method call.
        @return: The return value of the method that was called for visiting object.
        """
        method = None
        for cls in node.__class__.__mro__:
            method_name = 'visit_'+cls.__name__.lower()
            method = getattr(self, method_name, None)
            if method:
                break

        if not method:
            method = self.generic_visit
        return method(node, *args, **kwargs)

    @abstractmethod
    def generic_visit(self, node, *args, **kwargs):
        """
        The method to call if no methods were found for a visiting object.

        @param node: An object to call a visitor method with.
        @param args: Arguments to go with the visitor method call.
        @param kwargs: Keyword arguments to go with the visitor method call.
        """


class Visitee(object):
    """
    A base class for objects that wish to be able to visit a Visitor class.
    """
    def accept(self, visitor):
        """
        Visit a visitor with this class instance.

        @param visitor: The visitor to visit.
        @type visitor: Visitor
        """
        return visitor.visit(self)