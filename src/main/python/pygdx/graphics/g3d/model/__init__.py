from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.Renderable as _Renderable
_Renderable = _Renderable
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.model.NodePart as _NodePart
_NodePart = _NodePart
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NodePart():
    """com.badlogic.gdx.graphics.g3d.model.NodePart"""
 
    @staticmethod
    def _wrap(java_value: _NodePart) -> 'NodePart':
        return NodePart(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NodePart):
        """
        Dynamic initializer for NodePart.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NodePart__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NodePart__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def copy(self) -> 'NodePart':
        """public com.badlogic.gdx.graphics.g3d.model.NodePart com.badlogic.gdx.graphics.g3d.model.NodePart.copy()"""
        return 'NodePart'._wrap(super(NodePart, self).copy())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setRenderable(self, arg0: 'Renderable') -> 'g3d.Renderable':
        """public com.badlogic.gdx.graphics.g3d.Renderable com.badlogic.gdx.graphics.g3d.model.NodePart.setRenderable(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Renderable'._wrap(super(_NodePart, self).setRenderable(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.model.NodePart()"""
        val = _NodePart()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'MeshPart', arg1: 'Material'):
        """public com.badlogic.gdx.graphics.g3d.model.NodePart(com.badlogic.gdx.graphics.g3d.model.MeshPart,com.badlogic.gdx.graphics.g3d.Material)"""
        val = _NodePart(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.model.NodePart()"""
        val = _NodePart()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.model.NodePart
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.Renderable as _Renderable
_Renderable = _Renderable
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.model.NodePart as _NodePart
_NodePart = _NodePart
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NodePart():
    """com.badlogic.gdx.graphics.g3d.model.NodePart"""
 
    @staticmethod
    def _wrap(java_value: _NodePart) -> 'NodePart':
        return NodePart(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NodePart):
        """
        Dynamic initializer for NodePart.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NodePart__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NodePart__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def copy(self) -> 'NodePart':
        """public com.badlogic.gdx.graphics.g3d.model.NodePart com.badlogic.gdx.graphics.g3d.model.NodePart.copy()"""
        return 'NodePart'._wrap(super(NodePart, self).copy())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setRenderable(self, arg0: 'Renderable') -> 'g3d.Renderable':
        """public com.badlogic.gdx.graphics.g3d.Renderable com.badlogic.gdx.graphics.g3d.model.NodePart.setRenderable(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Renderable'._wrap(super(_NodePart, self).setRenderable(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.model.NodePart()"""
        val = _NodePart()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'MeshPart', arg1: 'Material'):
        """public com.badlogic.gdx.graphics.g3d.model.NodePart(com.badlogic.gdx.graphics.g3d.model.MeshPart,com.badlogic.gdx.graphics.g3d.Material)"""
        val = _NodePart(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.model.NodePart()"""
        val = _NodePart()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.model.NodePart 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.model.Node
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Iterable as Iterable
import com.badlogic.gdx.math.Matrix4 as _Matrix4
_Matrix4 = _Matrix4
import java.lang.String as _String
_String = _String
import java.lang.String as _string
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

import java.lang.Boolean as _boolean
import com.badlogic.gdx.graphics.g3d.model.Node as _Node
_Node = _Node
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.math.collision.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Node():
    """com.badlogic.gdx.graphics.g3d.model.Node"""
 
    @staticmethod
    def _wrap(java_value: _Node) -> 'Node':
        return Node(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Node):
        """
        Dynamic initializer for Node.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Node__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Node__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def extendBoundingBox(self, arg0: 'BoundingBox') -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g3d.model.Node.extendBoundingBox(com.badlogic.gdx.math.collision.BoundingBox)"""
        return 'collision.BoundingBox'._wrap(super(_Node, self).extendBoundingBox(arg0))

    @overload
    def addChildren(self, arg0: 'Iterable') -> int:
        """public <T extends com.badlogic.gdx.graphics.g3d.model.Node> int com.badlogic.gdx.graphics.g3d.model.Node.addChildren(java.lang.Iterable<T>)"""
        return int._wrap(super(_Node, self).addChildren(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def calculateWorldTransform(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g3d.model.Node.calculateWorldTransform()"""
        return 'math.Matrix4'._wrap(super(Node, self).calculateWorldTransform())

    @overload
    def calculateBoneTransforms(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.model.Node.calculateBoneTransforms(boolean)"""
        super(_Node, self).calculateBoneTransforms(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def hasChildren(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.model.Node.hasChildren()"""
        return bool._wrap(super(Node, self).hasChildren())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getParent(self) -> 'Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node com.badlogic.gdx.graphics.g3d.model.Node.getParent()"""
        return 'Node'._wrap(super(Node, self).getParent())

    @overload
    def getChildren(self) -> 'Iterable':
        """public java.lang.Iterable<com.badlogic.gdx.graphics.g3d.model.Node> com.badlogic.gdx.graphics.g3d.model.Node.getChildren()"""
        return 'Iterable'._wrap(super(Node, self).getChildren())

    @overload
    def removeChild(self, arg0: 'Node') -> bool:
        """public <T extends com.badlogic.gdx.graphics.g3d.model.Node> boolean com.badlogic.gdx.graphics.g3d.model.Node.removeChild(T)"""
        return bool._wrap(super(_Node, self).removeChild(arg0))

    @overload
    def getChild(self, arg0: int) -> 'Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node com.badlogic.gdx.graphics.g3d.model.Node.getChild(int)"""
        return 'Node'._wrap(super(_Node, self).getChild(_int.valueOf(arg0)))

    @overload
    def getChild(self, arg0: str, arg1: bool, arg2: bool) -> 'Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node com.badlogic.gdx.graphics.g3d.model.Node.getChild(java.lang.String,boolean,boolean)"""
        return 'Node'._wrap(super(_Node, self).getChild(arg0, _boolean.valueOf(arg1), _boolean.valueOf(arg2)))

    @overload
    def extendBoundingBox(self, arg0: 'BoundingBox', arg1: bool) -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g3d.model.Node.extendBoundingBox(com.badlogic.gdx.math.collision.BoundingBox,boolean)"""
        return 'collision.BoundingBox'._wrap(super(_Node, self).extendBoundingBox(arg0, _boolean.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def detach(self):
        """public void com.badlogic.gdx.graphics.g3d.model.Node.detach()"""
        super(Node, self).detach()

    @overload
    def calculateTransforms(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.model.Node.calculateTransforms(boolean)"""
        super(_Node, self).calculateTransforms(_boolean.valueOf(arg0))

    @overload
    def addChild(self, arg0: 'Node') -> int:
        """public <T extends com.badlogic.gdx.graphics.g3d.model.Node> int com.badlogic.gdx.graphics.g3d.model.Node.addChild(T)"""
        return int._wrap(super(_Node, self).addChild(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.model.Node()"""
        val = _Node()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.model.Node()"""
        val = _Node()
        self.__wrapper = val

    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.model.Node.getChildCount()"""
        return int._wrap(super(Node, self).getChildCount())

    @overload
    def insertChild(self, arg0: int, arg1: 'Node') -> int:
        """public <T extends com.badlogic.gdx.graphics.g3d.model.Node> int com.badlogic.gdx.graphics.g3d.model.Node.insertChild(int,T)"""
        return int._wrap(super(_Node, self).insertChild(_int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getNode(arg0: 'Array', arg1: str, arg2: bool, arg3: bool) -> 'Node':
        """public static com.badlogic.gdx.graphics.g3d.model.Node com.badlogic.gdx.graphics.g3d.model.Node.getNode(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.model.Node>,java.lang.String,boolean,boolean)"""
        return Node._wrap(_Node.getNode(arg0, arg1, _boolean.valueOf(arg2), _boolean.valueOf(arg3)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def insertChildren(self, arg0: int, arg1: 'Iterable') -> int:
        """public <T extends com.badlogic.gdx.graphics.g3d.model.Node> int com.badlogic.gdx.graphics.g3d.model.Node.insertChildren(int,java.lang.Iterable<T>)"""
        return int._wrap(super(_Node, self).insertChildren(_int.valueOf(arg0), arg1))

    @overload
    def calculateBoundingBox(self, arg0: 'BoundingBox') -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g3d.model.Node.calculateBoundingBox(com.badlogic.gdx.math.collision.BoundingBox)"""
        return 'collision.BoundingBox'._wrap(super(_Node, self).calculateBoundingBox(arg0))

    @overload
    def calculateBoundingBox(self, arg0: 'BoundingBox', arg1: bool) -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g3d.model.Node.calculateBoundingBox(com.badlogic.gdx.math.collision.BoundingBox,boolean)"""
        return 'collision.BoundingBox'._wrap(super(_Node, self).calculateBoundingBox(arg0, _boolean.valueOf(arg1)))

    @overload
    def calculateLocalTransform(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g3d.model.Node.calculateLocalTransform()"""
        return 'math.Matrix4'._wrap(super(Node, self).calculateLocalTransform())

    @overload
    def attachTo(self, arg0: 'Node'):
        """public <T extends com.badlogic.gdx.graphics.g3d.model.Node> void com.badlogic.gdx.graphics.g3d.model.Node.attachTo(T)"""
        super(_Node, self).attachTo(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def copy(self) -> 'Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node com.badlogic.gdx.graphics.g3d.model.Node.copy()"""
        return 'Node'._wrap(super(Node, self).copy())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def hasParent(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.model.Node.hasParent()"""
        return bool._wrap(super(Node, self).hasParent())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.model.Animation
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.model.Animation as _Animation
_Animation = _Animation
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Animation():
    """com.badlogic.gdx.graphics.g3d.model.Animation"""
 
    @staticmethod
    def _wrap(java_value: _Animation) -> 'Animation':
        return Animation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Animation):
        """
        Dynamic initializer for Animation.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Animation__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Animation__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.model.Animation()"""
        val = _Animation()
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.model.Animation()"""
        val = _Animation()
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.model.MeshPart
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.model.MeshPart as _MeshPart
_MeshPart = _MeshPart
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MeshPart():
    """com.badlogic.gdx.graphics.g3d.model.MeshPart"""
 
    @staticmethod
    def _wrap(java_value: _MeshPart) -> 'MeshPart':
        return MeshPart(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MeshPart):
        """
        Dynamic initializer for MeshPart.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MeshPart__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MeshPart__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def render(self, arg0: 'ShaderProgram', arg1: bool):
        """public void com.badlogic.gdx.graphics.g3d.model.MeshPart.render(com.badlogic.gdx.graphics.glutils.ShaderProgram,boolean)"""
        super(_MeshPart, self).render(arg0, _boolean.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'MeshPart'):
        """public com.badlogic.gdx.graphics.g3d.model.MeshPart(com.badlogic.gdx.graphics.g3d.model.MeshPart)"""
        val = _MeshPart(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.model.MeshPart()"""
        val = _MeshPart()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.model.MeshPart.update()"""
        super(MeshPart, self).update()

    @overload
    def set(self, arg0: 'MeshPart') -> 'MeshPart':
        """public com.badlogic.gdx.graphics.g3d.model.MeshPart com.badlogic.gdx.graphics.g3d.model.MeshPart.set(com.badlogic.gdx.graphics.g3d.model.MeshPart)"""
        return 'MeshPart'._wrap(super(_MeshPart, self).set(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def set(self, arg0: str, arg1: 'Mesh', arg2: int, arg3: int, arg4: int) -> 'MeshPart':
        """public com.badlogic.gdx.graphics.g3d.model.MeshPart com.badlogic.gdx.graphics.g3d.model.MeshPart.set(java.lang.String,com.badlogic.gdx.graphics.Mesh,int,int,int)"""
        return 'MeshPart'._wrap(super(_MeshPart, self).set(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def __init__(self, arg0: str, arg1: 'Mesh', arg2: int, arg3: int, arg4: int):
        """public com.badlogic.gdx.graphics.g3d.model.MeshPart(java.lang.String,com.badlogic.gdx.graphics.Mesh,int,int,int)"""
        val = _MeshPart(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def render(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.g3d.model.MeshPart.render(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(_MeshPart, self).render(arg0)

    @overload
    def equals(self, arg0: 'MeshPart') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.model.MeshPart.equals(com.badlogic.gdx.graphics.g3d.model.MeshPart)"""
        return bool._wrap(super(_MeshPart, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.model.MeshPart.equals(java.lang.Object)"""
        return bool._wrap(super(_MeshPart, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.model.MeshPart()"""
        val = _MeshPart()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.model.NodeAnimation
import com.badlogic.gdx.graphics.g3d.model.NodeAnimation as _NodeAnimation
_NodeAnimation = _NodeAnimation
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NodeAnimation():
    """com.badlogic.gdx.graphics.g3d.model.NodeAnimation"""
 
    @staticmethod
    def _wrap(java_value: _NodeAnimation) -> 'NodeAnimation':
        return NodeAnimation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NodeAnimation):
        """
        Dynamic initializer for NodeAnimation.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NodeAnimation__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NodeAnimation__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.model.NodeAnimation()"""
        val = _NodeAnimation()
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.model.NodeAnimation()"""
        val = _NodeAnimation()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.model.NodeKeyframe
import com.badlogic.gdx.graphics.g3d.model.NodeKeyframe as _NodeKeyframe
_NodeKeyframe = _NodeKeyframe
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NodeKeyframe():
    """com.badlogic.gdx.graphics.g3d.model.NodeKeyframe"""
 
    @staticmethod
    def _wrap(java_value: _NodeKeyframe) -> 'NodeKeyframe':
        return NodeKeyframe(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NodeKeyframe):
        """
        Dynamic initializer for NodeKeyframe.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NodeKeyframe__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NodeKeyframe__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: float, arg1: object):
        """public com.badlogic.gdx.graphics.g3d.model.NodeKeyframe(float,T)"""
        val = _NodeKeyframe(_float.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())