from __future__ import annotations
from overload import overload


 
from builtins import str
import java.util.function.Supplier as Supplier
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.debug.inspect.InspectionNode as __InspectionNode
__InspectionNode = __InspectionNode
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.quantum.debug.inspect.InspectionRoot as __InspectionRoot
__InspectionRoot = __InspectionRoot
from builtins import object
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class InspectionNode():
    """dev.ultreon.quantum.debug.inspect.InspectionNode"""
 
    @staticmethod
    def __wrap(java_value: __InspectionNode) -> 'InspectionNode':
        return InspectionNode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InspectionNode):
        """
        Dynamic initializer for InspectionNode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def removeNode(self, arg0: str) -> 'InspectionNode':
        """public dev.ultreon.quantum.debug.inspect.InspectionNode<?> dev.ultreon.quantum.debug.inspect.InspectionNode.removeNode(java.lang.String)"""
        return 'InspectionNode'.__wrap(super(__InspectionNode, self).removeNode(arg0))

    @overload
    def getNodes(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.quantum.debug.inspect.InspectionNode<?>> dev.ultreon.quantum.debug.inspect.InspectionNode.getNodes()"""
        return 'Map'.__wrap(super(InspectionNode, self).getNodes())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getParent(self) -> 'InspectionNode':
        """public dev.ultreon.quantum.debug.inspect.InspectionNode<?> dev.ultreon.quantum.debug.inspect.InspectionNode.getParent()"""
        return 'InspectionNode'.__wrap(super(InspectionNode, self).getParent())

    @overload
    def getRoot(self) -> 'InspectionRoot':
        """public dev.ultreon.quantum.debug.inspect.InspectionRoot<?> dev.ultreon.quantum.debug.inspect.InspectionNode.getRoot()"""
        return 'InspectionRoot'.__wrap(super(InspectionNode, self).getRoot())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def createNode(self, arg0: str, arg1: 'Supplier', *arg2: object) -> 'InspectionNode':
        """public final <C> dev.ultreon.quantum.debug.inspect.InspectionNode<C> dev.ultreon.quantum.debug.inspect.InspectionNode.createNode(java.lang.String,java.util.function.Supplier<C>,C...)"""
        return 'InspectionNode'.__wrap(super(__InspectionNode, self).createNode(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def create(self, arg0: str, arg1: 'Supplier'):
        """public void dev.ultreon.quantum.debug.inspect.InspectionNode.create(java.lang.String,java.util.function.Supplier<java.lang.Object>)"""
        super(__InspectionNode, self).create(arg0, arg1)

    @overload
    def remove(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.debug.inspect.InspectionNode.remove(java.lang.String)"""
        return bool.__wrap(super(__InspectionNode, self).remove(arg0))

    @overload
    def create(self, arg0: str, arg1: 'NodeMapping'):
        """public <C> void dev.ultreon.quantum.debug.inspect.InspectionNode.create(java.lang.String,dev.ultreon.quantum.debug.inspect.InspectionNode$NodeMapping<T, C>)"""
        super(__InspectionNode, self).create(arg0, arg1)

    @overload
    def createNode(self, arg0: str, arg1: 'NodeMapping', *arg2: object) -> 'InspectionNode':
        """public final <C> dev.ultreon.quantum.debug.inspect.InspectionNode<C> dev.ultreon.quantum.debug.inspect.InspectionNode.createNode(java.lang.String,dev.ultreon.quantum.debug.inspect.InspectionNode$NodeMapping<T, C>,C...)"""
        return 'InspectionNode'.__wrap(super(__InspectionNode, self).createNode(arg0, arg1, arg2))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: str, arg1: 'InspectionNode', arg2: 'InspectionRoot', arg3: 'Function', arg4: 'Consumer'):
        """public dev.ultreon.quantum.debug.inspect.InspectionNode(java.lang.String,dev.ultreon.quantum.debug.inspect.InspectionNode<?>,dev.ultreon.quantum.debug.inspect.InspectionRoot<?>,java.util.function.Function<dev.ultreon.quantum.debug.inspect.InspectionNode<T>, T>,java.util.function.Consumer<dev.ultreon.quantum.debug.inspect.InspectionNode<T>>)"""
        val = __InspectionNode(arg0, arg1, arg2, arg3, arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: str, arg1: 'InspectionNode', arg2: 'InspectionRoot', arg3: 'Function'):
        """public dev.ultreon.quantum.debug.inspect.InspectionNode(java.lang.String,dev.ultreon.quantum.debug.inspect.InspectionNode<?>,dev.ultreon.quantum.debug.inspect.InspectionRoot<?>,java.util.function.Function<dev.ultreon.quantum.debug.inspect.InspectionNode<T>, T>)"""
        val = __InspectionNode(arg0, arg1, arg2, arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getElements(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.util.function.Supplier<java.lang.String>> dev.ultreon.quantum.debug.inspect.InspectionNode.getElements()"""
        return 'Map'.__wrap(super(InspectionNode, self).getElements())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.debug.inspect.InspectionNode.getName()"""
        return str.__wrap(super(InspectionNode, self).getName())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.debug.inspect.InspectionNode.getValue()"""
        return object.__wrap(super(InspectionNode, self).getValue())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.debug.inspect.InspectionNode
from builtins import str
import java.util.function.Supplier as Supplier
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.debug.inspect.InspectionNode as __InspectionNode
__InspectionNode = __InspectionNode
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.quantum.debug.inspect.InspectionRoot as __InspectionRoot
__InspectionRoot = __InspectionRoot
from builtins import object
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class InspectionNode():
    """dev.ultreon.quantum.debug.inspect.InspectionNode"""
 
    @staticmethod
    def __wrap(java_value: __InspectionNode) -> 'InspectionNode':
        return InspectionNode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InspectionNode):
        """
        Dynamic initializer for InspectionNode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def removeNode(self, arg0: str) -> 'InspectionNode':
        """public dev.ultreon.quantum.debug.inspect.InspectionNode<?> dev.ultreon.quantum.debug.inspect.InspectionNode.removeNode(java.lang.String)"""
        return 'InspectionNode'.__wrap(super(__InspectionNode, self).removeNode(arg0))

    @overload
    def getNodes(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.quantum.debug.inspect.InspectionNode<?>> dev.ultreon.quantum.debug.inspect.InspectionNode.getNodes()"""
        return 'Map'.__wrap(super(InspectionNode, self).getNodes())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getParent(self) -> 'InspectionNode':
        """public dev.ultreon.quantum.debug.inspect.InspectionNode<?> dev.ultreon.quantum.debug.inspect.InspectionNode.getParent()"""
        return 'InspectionNode'.__wrap(super(InspectionNode, self).getParent())

    @overload
    def getRoot(self) -> 'InspectionRoot':
        """public dev.ultreon.quantum.debug.inspect.InspectionRoot<?> dev.ultreon.quantum.debug.inspect.InspectionNode.getRoot()"""
        return 'InspectionRoot'.__wrap(super(InspectionNode, self).getRoot())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def createNode(self, arg0: str, arg1: 'Supplier', *arg2: object) -> 'InspectionNode':
        """public final <C> dev.ultreon.quantum.debug.inspect.InspectionNode<C> dev.ultreon.quantum.debug.inspect.InspectionNode.createNode(java.lang.String,java.util.function.Supplier<C>,C...)"""
        return 'InspectionNode'.__wrap(super(__InspectionNode, self).createNode(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def create(self, arg0: str, arg1: 'Supplier'):
        """public void dev.ultreon.quantum.debug.inspect.InspectionNode.create(java.lang.String,java.util.function.Supplier<java.lang.Object>)"""
        super(__InspectionNode, self).create(arg0, arg1)

    @overload
    def remove(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.debug.inspect.InspectionNode.remove(java.lang.String)"""
        return bool.__wrap(super(__InspectionNode, self).remove(arg0))

    @overload
    def create(self, arg0: str, arg1: 'NodeMapping'):
        """public <C> void dev.ultreon.quantum.debug.inspect.InspectionNode.create(java.lang.String,dev.ultreon.quantum.debug.inspect.InspectionNode$NodeMapping<T, C>)"""
        super(__InspectionNode, self).create(arg0, arg1)

    @overload
    def createNode(self, arg0: str, arg1: 'NodeMapping', *arg2: object) -> 'InspectionNode':
        """public final <C> dev.ultreon.quantum.debug.inspect.InspectionNode<C> dev.ultreon.quantum.debug.inspect.InspectionNode.createNode(java.lang.String,dev.ultreon.quantum.debug.inspect.InspectionNode$NodeMapping<T, C>,C...)"""
        return 'InspectionNode'.__wrap(super(__InspectionNode, self).createNode(arg0, arg1, arg2))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: str, arg1: 'InspectionNode', arg2: 'InspectionRoot', arg3: 'Function', arg4: 'Consumer'):
        """public dev.ultreon.quantum.debug.inspect.InspectionNode(java.lang.String,dev.ultreon.quantum.debug.inspect.InspectionNode<?>,dev.ultreon.quantum.debug.inspect.InspectionRoot<?>,java.util.function.Function<dev.ultreon.quantum.debug.inspect.InspectionNode<T>, T>,java.util.function.Consumer<dev.ultreon.quantum.debug.inspect.InspectionNode<T>>)"""
        val = __InspectionNode(arg0, arg1, arg2, arg3, arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: str, arg1: 'InspectionNode', arg2: 'InspectionRoot', arg3: 'Function'):
        """public dev.ultreon.quantum.debug.inspect.InspectionNode(java.lang.String,dev.ultreon.quantum.debug.inspect.InspectionNode<?>,dev.ultreon.quantum.debug.inspect.InspectionRoot<?>,java.util.function.Function<dev.ultreon.quantum.debug.inspect.InspectionNode<T>, T>)"""
        val = __InspectionNode(arg0, arg1, arg2, arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getElements(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.util.function.Supplier<java.lang.String>> dev.ultreon.quantum.debug.inspect.InspectionNode.getElements()"""
        return 'Map'.__wrap(super(InspectionNode, self).getElements())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.debug.inspect.InspectionNode.getName()"""
        return str.__wrap(super(InspectionNode, self).getName())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.debug.inspect.InspectionNode.getValue()"""
        return object.__wrap(super(InspectionNode, self).getValue())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.debug.inspect.InspectionNode 
 
 
# CLASS: dev.ultreon.quantum.debug.inspect.InspectionRoot
from builtins import str
import java.util.function.Supplier as Supplier
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.debug.inspect.InspectionNode as __InspectionNode
__InspectionNode = __InspectionNode
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.quantum.debug.inspect.InspectionRoot as __InspectionRoot
__InspectionRoot = __InspectionRoot
from builtins import object
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.util.function.Function as Function
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class InspectionRoot():
    """dev.ultreon.quantum.debug.inspect.InspectionRoot"""
 
    @staticmethod
    def __wrap(java_value: __InspectionRoot) -> 'InspectionRoot':
        return InspectionRoot(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InspectionRoot):
        """
        Dynamic initializer for InspectionRoot.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def removeNode(self, arg0: str) -> 'InspectionNode':
        """public dev.ultreon.quantum.debug.inspect.InspectionNode<?> dev.ultreon.quantum.debug.inspect.InspectionNode.removeNode(java.lang.String)"""
        return 'InspectionNode'.__wrap(super(__InspectionNode, self).removeNode(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def registerFormatter(arg0: 'Class', arg1: 'Function'):
        """public static <E> void dev.ultreon.quantum.debug.inspect.InspectionRoot.registerFormatter(java.lang.Class<E>,java.util.function.Function<E, java.lang.String>)"""
        __InspectionRoot.registerFormatter(arg0, arg1)

    @override
    @overload
    def getParent(self) -> 'InspectionNode':
        """public dev.ultreon.quantum.debug.inspect.InspectionNode<?> dev.ultreon.quantum.debug.inspect.InspectionNode.getParent()"""
        return 'InspectionNode'.__wrap(super(InspectionNode, self).getParent())

    @override
    @overload
    def getRoot(self) -> 'InspectionRoot':
        """public dev.ultreon.quantum.debug.inspect.InspectionRoot<T> dev.ultreon.quantum.debug.inspect.InspectionRoot.getRoot()"""
        return 'InspectionRoot'.__wrap(super(InspectionRoot, self).getRoot())

    @override
    @overload
    def create(self, arg0: str, arg1: 'Supplier'):
        """public void dev.ultreon.quantum.debug.inspect.InspectionNode.create(java.lang.String,java.util.function.Supplier<java.lang.Object>)"""
        super(__InspectionNode, self).create(arg0, arg1)

    @overload
    def createNode(self, arg0: str, arg1: 'Supplier', *arg2: object) -> 'InspectionNode':
        """public final <C> dev.ultreon.quantum.debug.inspect.InspectionNode<C> dev.ultreon.quantum.debug.inspect.InspectionNode.createNode(java.lang.String,java.util.function.Supplier<C>,C...)"""
        return 'InspectionNode'.__wrap(super(__InspectionNode, self).createNode(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def createNode(self, arg0: str, arg1: 'NodeMapping', *arg2: object) -> 'InspectionNode':
        """public final <C> dev.ultreon.quantum.debug.inspect.InspectionNode<C> dev.ultreon.quantum.debug.inspect.InspectionNode.createNode(java.lang.String,dev.ultreon.quantum.debug.inspect.InspectionNode$NodeMapping<T, C>,C...)"""
        return 'InspectionNode'.__wrap(super(__InspectionNode, self).createNode(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getNodes(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.quantum.debug.inspect.InspectionNode<?>> dev.ultreon.quantum.debug.inspect.InspectionNode.getNodes()"""
        return 'Map'.__wrap(super(InspectionNode, self).getNodes())

    @overload
    def __init__(self, arg0: object):
        """public dev.ultreon.quantum.debug.inspect.InspectionRoot(T)"""
        val = __InspectionRoot(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.debug.inspect.InspectionRoot.dispose()"""
        super(InspectionRoot, self).dispose()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setInspecting(self, arg0: bool):
        """public void dev.ultreon.quantum.debug.inspect.InspectionRoot.setInspecting(boolean)"""
        super(__InspectionRoot, self).setInspecting(__boolean.valueOf(arg0))

    @overload
    def isInspecting(self) -> bool:
        """public boolean dev.ultreon.quantum.debug.inspect.InspectionRoot.isInspecting()"""
        return bool.__wrap(super(InspectionRoot, self).isInspecting())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.debug.inspect.InspectionNode.getName()"""
        return str.__wrap(super(InspectionNode, self).getName())

    @overload
    def remove(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.debug.inspect.InspectionNode.remove(java.lang.String)"""
        return bool.__wrap(super(__InspectionNode, self).remove(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def create(self, arg0: str, arg1: 'NodeMapping'):
        """public <C> void dev.ultreon.quantum.debug.inspect.InspectionNode.create(java.lang.String,dev.ultreon.quantum.debug.inspect.InspectionNode$NodeMapping<T, C>)"""
        super(__InspectionNode, self).create(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def format(arg0: object) -> str:
        """public static java.lang.String dev.ultreon.quantum.debug.inspect.InspectionRoot.format(java.lang.Object)"""
        return str.__wrap(__InspectionRoot.format(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getNode(self, arg0: str) -> 'InspectionNode':
        """public dev.ultreon.quantum.debug.inspect.InspectionNode<?> dev.ultreon.quantum.debug.inspect.InspectionRoot.getNode(java.lang.String)"""
        return 'InspectionNode'.__wrap(super(__InspectionRoot, self).getNode(arg0))

    @override
    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.debug.inspect.InspectionNode.getValue()"""
        return object.__wrap(super(InspectionNode, self).getValue())

    @override
    @overload
    def getElements(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.util.function.Supplier<java.lang.String>> dev.ultreon.quantum.debug.inspect.InspectionNode.getElements()"""
        return 'Map'.__wrap(super(InspectionNode, self).getElements())

    @staticmethod
    @overload
    def registerAutoFill(arg0: 'Class', arg1: 'Consumer'):
        """public static <N> void dev.ultreon.quantum.debug.inspect.InspectionRoot.registerAutoFill(java.lang.Class<N>,java.util.function.Consumer<dev.ultreon.quantum.debug.inspect.InspectionNode<N>>)"""
        __InspectionRoot.registerAutoFill(arg0, arg1) 
 
 
# CLASS: dev.ultreon.quantum.debug.inspect.DefaultInspections
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.debug.inspect.DefaultInspections as __DefaultInspections
__DefaultInspections = __DefaultInspections
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DefaultInspections():
    """dev.ultreon.quantum.debug.inspect.DefaultInspections"""
 
    @staticmethod
    def __wrap(java_value: __DefaultInspections) -> 'DefaultInspections':
        return DefaultInspections(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefaultInspections):
        """
        Dynamic initializer for DefaultInspections.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

        @staticmethod
        @overload
        def register():
            """public static void dev.ultreon.quantum.debug.inspect.DefaultInspections.register()"""
            __DefaultInspections.register()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.debug.inspect.DefaultInspections()"""
        val = __DefaultInspections()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.debug.inspect.DefaultInspections()"""
        val = __DefaultInspections()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.debug.inspect.InspectionNode$NodeMapping
import dev.ultreon.quantum.debug.inspect.InspectionNode as __InspectionNode_NodeMapping
__NodeMapping = __InspectionNode_NodeMapping.NodeMapping
from abc import abstractmethod, ABC
 
class NodeMapping(ABC):
    """dev.ultreon.quantum.debug.inspect.InspectionNode.NodeMapping"""
 
    @staticmethod
    def __wrap(java_value: __NodeMapping) -> 'NodeMapping':
        return NodeMapping(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NodeMapping):
        """
        Dynamic initializer for NodeMapping.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def map(self, arg0: object):
        """public abstract C dev.ultreon.quantum.debug.inspect.InspectionNode$NodeMapping.map(T)"""
        pass