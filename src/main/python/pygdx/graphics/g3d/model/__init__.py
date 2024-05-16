from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import com.badlogic.gdx.graphics.g3d.model.NodeAnimation as __NodeAnimation
__NodeAnimation = __NodeAnimation
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NodeAnimation():
    """com.badlogic.gdx.graphics.g3d.model.NodeAnimation"""
 
    @staticmethod
    def __wrap(java_value: __NodeAnimation) -> 'NodeAnimation':
        return NodeAnimation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NodeAnimation):
        """
        Dynamic initializer for NodeAnimation.
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.model.NodeAnimation()"""
        val = __NodeAnimation()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.model.NodeAnimation()"""
        val = __NodeAnimation()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.model.NodeAnimation
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import com.badlogic.gdx.graphics.g3d.model.NodeAnimation as __NodeAnimation
__NodeAnimation = __NodeAnimation
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NodeAnimation():
    """com.badlogic.gdx.graphics.g3d.model.NodeAnimation"""
 
    @staticmethod
    def __wrap(java_value: __NodeAnimation) -> 'NodeAnimation':
        return NodeAnimation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NodeAnimation):
        """
        Dynamic initializer for NodeAnimation.
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.model.NodeAnimation()"""
        val = __NodeAnimation()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.model.NodeAnimation()"""
        val = __NodeAnimation()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.model.NodeAnimation 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.model.Node
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
import com.badlogic.gdx.graphics.g3d.model.Node as __Node
__Node = __Node
try:
    from pygdx.math import collision
except ImportError:
    collision = __import_once__("pygdx.math.collision")

import com.badlogic.gdx.math.Matrix4 as __Matrix4
__Matrix4 = __Matrix4
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.math.collision.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
import java.lang.Integer as __int
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Node():
    """com.badlogic.gdx.graphics.g3d.model.Node"""
 
    @staticmethod
    def __wrap(java_value: __Node) -> 'Node':
        return Node(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Node):
        """
        Dynamic initializer for Node.
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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.model.Node()"""
        val = __Node()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getChild(self, arg0: int) -> 'Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node com.badlogic.gdx.graphics.g3d.model.Node.getChild(int)"""
        return 'Node'.__wrap(super(__Node, self).getChild(__int.valueOf(arg0)))

    @overload
    def calculateBoundingBox(self, arg0: 'BoundingBox') -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g3d.model.Node.calculateBoundingBox(com.badlogic.gdx.math.collision.BoundingBox)"""
        return 'collision.BoundingBox'.__wrap(super(__Node, self).calculateBoundingBox(arg0))

    @overload
    def calculateBoneTransforms(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.model.Node.calculateBoneTransforms(boolean)"""
        super(__Node, self).calculateBoneTransforms(__boolean.valueOf(arg0))

    @overload
    def addChildren(self, arg0: 'Iterable') -> int:
        """public <T extends com.badlogic.gdx.graphics.g3d.model.Node> int com.badlogic.gdx.graphics.g3d.model.Node.addChildren(java.lang.Iterable<T>)"""
        return int.__wrap(super(__Node, self).addChildren(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def calculateBoundingBox(self, arg0: 'BoundingBox', arg1: bool) -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g3d.model.Node.calculateBoundingBox(com.badlogic.gdx.math.collision.BoundingBox,boolean)"""
        return 'collision.BoundingBox'.__wrap(super(__Node, self).calculateBoundingBox(arg0, __boolean.valueOf(arg1)))

    @overload
    def copy(self) -> 'Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node com.badlogic.gdx.graphics.g3d.model.Node.copy()"""
        return 'Node'.__wrap(super(Node, self).copy())

    @overload
    def addChild(self, arg0: 'Node') -> int:
        """public <T extends com.badlogic.gdx.graphics.g3d.model.Node> int com.badlogic.gdx.graphics.g3d.model.Node.addChild(T)"""
        return int.__wrap(super(__Node, self).addChild(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def attachTo(self, arg0: 'Node'):
        """public <T extends com.badlogic.gdx.graphics.g3d.model.Node> void com.badlogic.gdx.graphics.g3d.model.Node.attachTo(T)"""
        super(__Node, self).attachTo(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def calculateLocalTransform(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g3d.model.Node.calculateLocalTransform()"""
        return 'math.Matrix4'.__wrap(super(Node, self).calculateLocalTransform())

    @overload
    def extendBoundingBox(self, arg0: 'BoundingBox', arg1: bool) -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g3d.model.Node.extendBoundingBox(com.badlogic.gdx.math.collision.BoundingBox,boolean)"""
        return 'collision.BoundingBox'.__wrap(super(__Node, self).extendBoundingBox(arg0, __boolean.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def insertChildren(self, arg0: int, arg1: 'Iterable') -> int:
        """public <T extends com.badlogic.gdx.graphics.g3d.model.Node> int com.badlogic.gdx.graphics.g3d.model.Node.insertChildren(int,java.lang.Iterable<T>)"""
        return int.__wrap(super(__Node, self).insertChildren(__int.valueOf(arg0), arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.model.Node()"""
        val = __Node()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getChildren(self) -> 'Iterable':
        """public java.lang.Iterable<com.badlogic.gdx.graphics.g3d.model.Node> com.badlogic.gdx.graphics.g3d.model.Node.getChildren()"""
        return 'Iterable'.__wrap(super(Node, self).getChildren())

    @staticmethod
    @overload
    def getNode(arg0: 'Array', arg1: str, arg2: bool, arg3: bool) -> 'Node':
        """public static com.badlogic.gdx.graphics.g3d.model.Node com.badlogic.gdx.graphics.g3d.model.Node.getNode(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.model.Node>,java.lang.String,boolean,boolean)"""
        return Node.__wrap(__Node.getNode(arg0, arg1, __boolean.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def detach(self):
        """public void com.badlogic.gdx.graphics.g3d.model.Node.detach()"""
        super(Node, self).detach()

    @overload
    def insertChild(self, arg0: int, arg1: 'Node') -> int:
        """public <T extends com.badlogic.gdx.graphics.g3d.model.Node> int com.badlogic.gdx.graphics.g3d.model.Node.insertChild(int,T)"""
        return int.__wrap(super(__Node, self).insertChild(__int.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def calculateWorldTransform(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g3d.model.Node.calculateWorldTransform()"""
        return 'math.Matrix4'.__wrap(super(Node, self).calculateWorldTransform())

    @overload
    def hasChildren(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.model.Node.hasChildren()"""
        return bool.__wrap(super(Node, self).hasChildren())

    @overload
    def hasParent(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.model.Node.hasParent()"""
        return bool.__wrap(super(Node, self).hasParent())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def removeChild(self, arg0: 'Node') -> bool:
        """public <T extends com.badlogic.gdx.graphics.g3d.model.Node> boolean com.badlogic.gdx.graphics.g3d.model.Node.removeChild(T)"""
        return bool.__wrap(super(__Node, self).removeChild(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.model.Node.getChildCount()"""
        return int.__wrap(super(Node, self).getChildCount())

    @overload
    def getChild(self, arg0: str, arg1: bool, arg2: bool) -> 'Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node com.badlogic.gdx.graphics.g3d.model.Node.getChild(java.lang.String,boolean,boolean)"""
        return 'Node'.__wrap(super(__Node, self).getChild(arg0, __boolean.valueOf(arg1), __boolean.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getParent(self) -> 'Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node com.badlogic.gdx.graphics.g3d.model.Node.getParent()"""
        return 'Node'.__wrap(super(Node, self).getParent())

    @overload
    def calculateTransforms(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.model.Node.calculateTransforms(boolean)"""
        super(__Node, self).calculateTransforms(__boolean.valueOf(arg0))

    @overload
    def extendBoundingBox(self, arg0: 'BoundingBox') -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g3d.model.Node.extendBoundingBox(com.badlogic.gdx.math.collision.BoundingBox)"""
        return 'collision.BoundingBox'.__wrap(super(__Node, self).extendBoundingBox(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.model.Animation
from builtins import str
import com.badlogic.gdx.graphics.g3d.model.Animation as __Animation
__Animation = __Animation
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
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Animation():
    """com.badlogic.gdx.graphics.g3d.model.Animation"""
 
    @staticmethod
    def __wrap(java_value: __Animation) -> 'Animation':
        return Animation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Animation):
        """
        Dynamic initializer for Animation.
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.model.Animation()"""
        val = __Animation()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.model.Animation()"""
        val = __Animation()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.model.MeshPart
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.g3d.model.MeshPart as __MeshPart
__MeshPart = __MeshPart
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class MeshPart():
    """com.badlogic.gdx.graphics.g3d.model.MeshPart"""
 
    @staticmethod
    def __wrap(java_value: __MeshPart) -> 'MeshPart':
        return MeshPart(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MeshPart):
        """
        Dynamic initializer for MeshPart.
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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.model.MeshPart()"""
        val = __MeshPart()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'MeshPart'):
        """public com.badlogic.gdx.graphics.g3d.model.MeshPart(com.badlogic.gdx.graphics.g3d.model.MeshPart)"""
        val = __MeshPart(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.model.MeshPart.update()"""
        super(MeshPart, self).update()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.model.MeshPart.equals(java.lang.Object)"""
        return bool.__wrap(super(__MeshPart, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.model.MeshPart()"""
        val = __MeshPart()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: 'MeshPart') -> 'MeshPart':
        """public com.badlogic.gdx.graphics.g3d.model.MeshPart com.badlogic.gdx.graphics.g3d.model.MeshPart.set(com.badlogic.gdx.graphics.g3d.model.MeshPart)"""
        return 'MeshPart'.__wrap(super(__MeshPart, self).set(arg0))

    @overload
    def render(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.g3d.model.MeshPart.render(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(__MeshPart, self).render(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: 'MeshPart') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.model.MeshPart.equals(com.badlogic.gdx.graphics.g3d.model.MeshPart)"""
        return bool.__wrap(super(__MeshPart, self).equals(arg0))

    @overload
    def render(self, arg0: 'ShaderProgram', arg1: bool):
        """public void com.badlogic.gdx.graphics.g3d.model.MeshPart.render(com.badlogic.gdx.graphics.glutils.ShaderProgram,boolean)"""
        super(__MeshPart, self).render(arg0, __boolean.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: str, arg1: 'Mesh', arg2: int, arg3: int, arg4: int) -> 'MeshPart':
        """public com.badlogic.gdx.graphics.g3d.model.MeshPart com.badlogic.gdx.graphics.g3d.model.MeshPart.set(java.lang.String,com.badlogic.gdx.graphics.Mesh,int,int,int)"""
        return 'MeshPart'.__wrap(super(__MeshPart, self).set(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @overload
    def __init__(self, arg0: str, arg1: 'Mesh', arg2: int, arg3: int, arg4: int):
        """public com.badlogic.gdx.graphics.g3d.model.MeshPart(java.lang.String,com.badlogic.gdx.graphics.Mesh,int,int,int)"""
        val = __MeshPart(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.model.NodeKeyframe
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.model.NodeKeyframe as __NodeKeyframe
__NodeKeyframe = __NodeKeyframe
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NodeKeyframe():
    """com.badlogic.gdx.graphics.g3d.model.NodeKeyframe"""
 
    @staticmethod
    def __wrap(java_value: __NodeKeyframe) -> 'NodeKeyframe':
        return NodeKeyframe(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NodeKeyframe):
        """
        Dynamic initializer for NodeKeyframe.
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
    def __init__(self, arg0: float, arg1: object):
        """public com.badlogic.gdx.graphics.g3d.model.NodeKeyframe(float,T)"""
        val = __NodeKeyframe(__float.valueOf(arg0), arg1)
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.model.NodePart
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import com.badlogic.gdx.graphics.g3d.Renderable as __Renderable
__Renderable = __Renderable
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g3d.model.NodePart as __NodePart
__NodePart = __NodePart
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NodePart():
    """com.badlogic.gdx.graphics.g3d.model.NodePart"""
 
    @staticmethod
    def __wrap(java_value: __NodePart) -> 'NodePart':
        return NodePart(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NodePart):
        """
        Dynamic initializer for NodePart.
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
    def setRenderable(self, arg0: 'Renderable') -> 'g3d.Renderable':
        """public com.badlogic.gdx.graphics.g3d.Renderable com.badlogic.gdx.graphics.g3d.model.NodePart.setRenderable(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'g3d.Renderable'.__wrap(super(__NodePart, self).setRenderable(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.model.NodePart()"""
        val = __NodePart()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.model.NodePart()"""
        val = __NodePart()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'MeshPart', arg1: 'Material'):
        """public com.badlogic.gdx.graphics.g3d.model.NodePart(com.badlogic.gdx.graphics.g3d.model.MeshPart,com.badlogic.gdx.graphics.g3d.Material)"""
        val = __NodePart(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def copy(self) -> 'NodePart':
        """public com.badlogic.gdx.graphics.g3d.model.NodePart com.badlogic.gdx.graphics.g3d.model.NodePart.copy()"""
        return 'NodePart'.__wrap(super(NodePart, self).copy())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))