from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
from typing import List
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.physics.box2d.WorldManifold as __WorldManifold
__WorldManifold = __WorldManifold
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class WorldManifold():
    """com.badlogic.gdx.physics.box2d.WorldManifold"""
 
    @staticmethod
    def __wrap(java_value: __WorldManifold) -> 'WorldManifold':
        return WorldManifold(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WorldManifold):
        """
        Dynamic initializer for WorldManifold.
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
    def getSeparations(self) -> List[float]:
        """public float[] com.badlogic.gdx.physics.box2d.WorldManifold.getSeparations()"""
        return List[float].__wrap(super(WorldManifold, self).getSeparations())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

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
    def getNumberOfContactPoints(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.WorldManifold.getNumberOfContactPoints()"""
        return int.__wrap(super(WorldManifold, self).getNumberOfContactPoints())

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
    def getPoints(self) -> List['math.Vector2']:
        """public com.badlogic.gdx.math.Vector2[] com.badlogic.gdx.physics.box2d.WorldManifold.getPoints()"""
        return List['math.Vector2'].__wrap(super(WorldManifold, self).getPoints())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getNormal(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.WorldManifold.getNormal()"""
        return 'math.Vector2'.__wrap(super(WorldManifold, self).getNormal())

 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.WorldManifold
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
from typing import List
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.physics.box2d.WorldManifold as __WorldManifold
__WorldManifold = __WorldManifold
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class WorldManifold():
    """com.badlogic.gdx.physics.box2d.WorldManifold"""
 
    @staticmethod
    def __wrap(java_value: __WorldManifold) -> 'WorldManifold':
        return WorldManifold(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WorldManifold):
        """
        Dynamic initializer for WorldManifold.
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
    def getSeparations(self) -> List[float]:
        """public float[] com.badlogic.gdx.physics.box2d.WorldManifold.getSeparations()"""
        return List[float].__wrap(super(WorldManifold, self).getSeparations())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

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
    def getNumberOfContactPoints(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.WorldManifold.getNumberOfContactPoints()"""
        return int.__wrap(super(WorldManifold, self).getNumberOfContactPoints())

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
    def getPoints(self) -> List['math.Vector2']:
        """public com.badlogic.gdx.math.Vector2[] com.badlogic.gdx.physics.box2d.WorldManifold.getPoints()"""
        return List['math.Vector2'].__wrap(super(WorldManifold, self).getPoints())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getNormal(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.WorldManifold.getNormal()"""
        return 'math.Vector2'.__wrap(super(WorldManifold, self).getNormal())

 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.WorldManifold 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.FixtureDef
import com.badlogic.gdx.physics.box2d.FixtureDef as __FixtureDef
__FixtureDef = __FixtureDef
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
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FixtureDef():
    """com.badlogic.gdx.physics.box2d.FixtureDef"""
 
    @staticmethod
    def __wrap(java_value: __FixtureDef) -> 'FixtureDef':
        return FixtureDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FixtureDef):
        """
        Dynamic initializer for FixtureDef.
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
        """public com.badlogic.gdx.physics.box2d.FixtureDef()"""
        val = __FixtureDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.FixtureDef()"""
        val = __FixtureDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.DestructionListener
import com.badlogic.gdx.physics.box2d.DestructionListener as __DestructionListener
__DestructionListener = __DestructionListener
 
class DestructionListener(ABC):
    """com.badlogic.gdx.physics.box2d.DestructionListener"""
 
    @staticmethod
    def __wrap(java_value: __DestructionListener) -> 'DestructionListener':
        return DestructionListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DestructionListener):
        """
        Dynamic initializer for DestructionListener.
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
 
 
# CLASS: com.badlogic.gdx.physics.box2d.Box2DDebugRenderer
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.physics.box2d.Box2DDebugRenderer as __Box2DDebugRenderer
__Box2DDebugRenderer = __Box2DDebugRenderer
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Box2DDebugRenderer():
    """com.badlogic.gdx.physics.box2d.Box2DDebugRenderer"""
 
    @staticmethod
    def __wrap(java_value: __Box2DDebugRenderer) -> 'Box2DDebugRenderer':
        return Box2DDebugRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Box2DDebugRenderer):
        """
        Dynamic initializer for Box2DDebugRenderer.
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
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.Box2DDebugRenderer()"""
        val = __Box2DDebugRenderer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.dispose()"""
        super(Box2DDebugRenderer, self).dispose()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setDrawContacts(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.setDrawContacts(boolean)"""
        super(__Box2DDebugRenderer, self).setDrawContacts(__boolean.valueOf(arg0))

    @overload
    def isDrawAABBs(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.isDrawAABBs()"""
        return bool.__wrap(super(Box2DDebugRenderer, self).isDrawAABBs())

    @overload
    def setDrawJoints(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.setDrawJoints(boolean)"""
        super(__Box2DDebugRenderer, self).setDrawJoints(__boolean.valueOf(arg0))

    @overload
    def isDrawBodies(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.isDrawBodies()"""
        return bool.__wrap(super(Box2DDebugRenderer, self).isDrawBodies())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.Box2DDebugRenderer()"""
        val = __Box2DDebugRenderer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isDrawInactiveBodies(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.isDrawInactiveBodies()"""
        return bool.__wrap(super(Box2DDebugRenderer, self).isDrawInactiveBodies())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def isDrawContacts(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.isDrawContacts()"""
        return bool.__wrap(super(Box2DDebugRenderer, self).isDrawContacts())

    @overload
    def __init__(self, arg0: bool, arg1: bool, arg2: bool, arg3: bool, arg4: bool, arg5: bool):
        """public com.badlogic.gdx.physics.box2d.Box2DDebugRenderer(boolean,boolean,boolean,boolean,boolean,boolean)"""
        val = __Box2DDebugRenderer(__boolean.valueOf(arg0), __boolean.valueOf(arg1), __boolean.valueOf(arg2), __boolean.valueOf(arg3), __boolean.valueOf(arg4), __boolean.valueOf(arg5))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def setAxis(arg0: 'Vector2'):
        """public static void com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.setAxis(com.badlogic.gdx.math.Vector2)"""
        __Box2DDebugRenderer.setAxis(arg0)

    @overload
    def isDrawVelocities(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.isDrawVelocities()"""
        return bool.__wrap(super(Box2DDebugRenderer, self).isDrawVelocities())

    @overload
    def setDrawInactiveBodies(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.setDrawInactiveBodies(boolean)"""
        super(__Box2DDebugRenderer, self).setDrawInactiveBodies(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setDrawAABBs(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.setDrawAABBs(boolean)"""
        super(__Box2DDebugRenderer, self).setDrawAABBs(__boolean.valueOf(arg0))

    @staticmethod
    @overload
    def getAxis() -> 'math.Vector2':
        """public static com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.getAxis()"""
        return math.Vector2.__wrap(__Box2DDebugRenderer.getAxis())

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
    def isDrawJoints(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.isDrawJoints()"""
        return bool.__wrap(super(Box2DDebugRenderer, self).isDrawJoints())

    @overload
    def render(self, arg0: 'World', arg1: 'Matrix4'):
        """public void com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.render(com.badlogic.gdx.physics.box2d.World,com.badlogic.gdx.math.Matrix4)"""
        super(__Box2DDebugRenderer, self).render(arg0, arg1)

    @overload
    def setDrawVelocities(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.setDrawVelocities(boolean)"""
        super(__Box2DDebugRenderer, self).setDrawVelocities(__boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setDrawBodies(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.setDrawBodies(boolean)"""
        super(__Box2DDebugRenderer, self).setDrawBodies(__boolean.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.Transform
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.physics.box2d.Transform as __Transform
__Transform = __Transform
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Transform():
    """com.badlogic.gdx.physics.box2d.Transform"""
 
    @staticmethod
    def __wrap(java_value: __Transform) -> 'Transform':
        return Transform(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Transform):
        """
        Dynamic initializer for Transform.
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
    def getOrientation(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Transform.getOrientation()"""
        return 'math.Vector2'.__wrap(super(Transform, self).getOrientation())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.Transform()"""
        val = __Transform()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Vector2', arg1: 'Vector2'):
        """public com.badlogic.gdx.physics.box2d.Transform(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        val = __Transform(arg0, arg1)
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
    def __init__(self, arg0: 'Vector2', arg1: float):
        """public com.badlogic.gdx.physics.box2d.Transform(com.badlogic.gdx.math.Vector2,float)"""
        val = __Transform(arg0, __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Transform.getRotation()"""
        return float.__wrap(super(Transform, self).getRotation())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getPosition(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Transform.getPosition()"""
        return 'math.Vector2'.__wrap(super(Transform, self).getPosition())

    @overload
    def mul(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Transform.mul(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Transform, self).mul(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.Transform()"""
        val = __Transform()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setRotation(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Transform.setRotation(float)"""
        super(__Transform, self).setRotation(__float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setOrientation(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.Transform.setOrientation(com.badlogic.gdx.math.Vector2)"""
        super(__Transform, self).setOrientation(arg0)

    @overload
    def setPosition(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.Transform.setPosition(com.badlogic.gdx.math.Vector2)"""
        super(__Transform, self).setPosition(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.Manifold$ManifoldPoint
import com.badlogic.gdx.physics.box2d.Manifold as __Manifold_ManifoldPoint
__ManifoldPoint = __Manifold_ManifoldPoint.ManifoldPoint
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
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ManifoldPoint():
    """com.badlogic.gdx.physics.box2d.Manifold.ManifoldPoint"""
 
    @staticmethod
    def __wrap(java_value: __ManifoldPoint) -> 'ManifoldPoint':
        return ManifoldPoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ManifoldPoint):
        """
        Dynamic initializer for ManifoldPoint.
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
    def __init__(self, arg0: 'Manifold'):
        """public com.badlogic.gdx.physics.box2d.Manifold$ManifoldPoint(com.badlogic.gdx.physics.box2d.Manifold)"""
        val = __ManifoldPoint(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.physics.box2d.Manifold$ManifoldPoint.toString()"""
        return str.__wrap(super(ManifoldPoint, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.EdgeShape
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.physics.box2d.EdgeShape as __EdgeShape
__EdgeShape = __EdgeShape
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.physics.box2d.Shape as __Shape_Type
__Type = __Shape_Type.Type
import com.badlogic.gdx.physics.box2d.Shape as __Shape
__Shape = __Shape
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EdgeShape():
    """com.badlogic.gdx.physics.box2d.EdgeShape"""
 
    @staticmethod
    def __wrap(java_value: __EdgeShape) -> 'EdgeShape':
        return EdgeShape(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EdgeShape):
        """
        Dynamic initializer for EdgeShape.
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
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.physics.box2d.EdgeShape.set(float,float,float,float)"""
        super(__EdgeShape, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setRadius(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Shape.setRadius(float)"""
        super(__Shape, self).setRadius(__float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getVertex0(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.EdgeShape.getVertex0(com.badlogic.gdx.math.Vector2)"""
        super(__EdgeShape, self).getVertex0(arg0)

    @overload
    def set(self, arg0: 'Vector2', arg1: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.EdgeShape.set(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(__EdgeShape, self).set(arg0, arg1)

    @overload
    def setVertex0(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.physics.box2d.EdgeShape.setVertex0(float,float)"""
        super(__EdgeShape, self).setVertex0(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def hasVertex3(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.EdgeShape.hasVertex3()"""
        return bool.__wrap(super(EdgeShape, self).hasVertex3())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.EdgeShape()"""
        val = __EdgeShape()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def hasVertex0(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.EdgeShape.hasVertex0()"""
        return bool.__wrap(super(EdgeShape, self).hasVertex0())

    @overload
    def setVertex3(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.physics.box2d.EdgeShape.setVertex3(float,float)"""
        super(__EdgeShape, self).setVertex3(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def setVertex0(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.EdgeShape.setVertex0(com.badlogic.gdx.math.Vector2)"""
        super(__EdgeShape, self).setVertex0(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setHasVertex0(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.EdgeShape.setHasVertex0(boolean)"""
        super(__EdgeShape, self).setHasVertex0(__boolean.valueOf(arg0))

    @override
    @overload
    def getRadius(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Shape.getRadius()"""
        return float.__wrap(super(Shape, self).getRadius())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getType(self) -> 'Type':
        """public com.badlogic.gdx.physics.box2d.Shape$Type com.badlogic.gdx.physics.box2d.EdgeShape.getType()"""
        return 'Type'.__wrap(super(EdgeShape, self).getType())

    @overload
    def setHasVertex3(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.EdgeShape.setHasVertex3(boolean)"""
        super(__EdgeShape, self).setHasVertex3(__boolean.valueOf(arg0))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.physics.box2d.Shape.dispose()"""
        super(Shape, self).dispose()

    @overload
    def setVertex3(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.EdgeShape.setVertex3(com.badlogic.gdx.math.Vector2)"""
        super(__EdgeShape, self).setVertex3(arg0)

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

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.Shape.getChildCount()"""
        return int.__wrap(super(Shape, self).getChildCount())

    @overload
    def getVertex3(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.EdgeShape.getVertex3(com.badlogic.gdx.math.Vector2)"""
        super(__EdgeShape, self).getVertex3(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.EdgeShape()"""
        val = __EdgeShape()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getVertex1(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.EdgeShape.getVertex1(com.badlogic.gdx.math.Vector2)"""
        super(__EdgeShape, self).getVertex1(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getVertex2(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.EdgeShape.getVertex2(com.badlogic.gdx.math.Vector2)"""
        super(__EdgeShape, self).getVertex2(arg0) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.Contact
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import com.badlogic.gdx.physics.box2d.Contact as __Contact
__Contact = __Contact
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.physics.box2d.WorldManifold as __WorldManifold
__WorldManifold = __WorldManifold
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.physics.box2d.Fixture as __Fixture
__Fixture = __Fixture
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Contact():
    """com.badlogic.gdx.physics.box2d.Contact"""
 
    @staticmethod
    def __wrap(java_value: __Contact) -> 'Contact':
        return Contact(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Contact):
        """
        Dynamic initializer for Contact.
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
    def ResetRestitution(self):
        """public void com.badlogic.gdx.physics.box2d.Contact.ResetRestitution()"""
        super(Contact, self).ResetRestitution()

    @overload
    def getChildIndexA(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.Contact.getChildIndexA()"""
        return int.__wrap(super(Contact, self).getChildIndexA())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isTouching(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Contact.isTouching()"""
        return bool.__wrap(super(Contact, self).isTouching())

    @overload
    def getChildIndexB(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.Contact.getChildIndexB()"""
        return int.__wrap(super(Contact, self).getChildIndexB())

    @overload
    def getFixtureB(self) -> 'Fixture':
        """public com.badlogic.gdx.physics.box2d.Fixture com.badlogic.gdx.physics.box2d.Contact.getFixtureB()"""
        return 'Fixture'.__wrap(super(Contact, self).getFixtureB())

    @overload
    def setRestitution(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Contact.setRestitution(float)"""
        super(__Contact, self).setRestitution(__float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getRestitution(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Contact.getRestitution()"""
        return float.__wrap(super(Contact, self).getRestitution())

    @overload
    def getFixtureA(self) -> 'Fixture':
        """public com.badlogic.gdx.physics.box2d.Fixture com.badlogic.gdx.physics.box2d.Contact.getFixtureA()"""
        return 'Fixture'.__wrap(super(Contact, self).getFixtureA())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getFriction(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Contact.getFriction()"""
        return float.__wrap(super(Contact, self).getFriction())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setTangentSpeed(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Contact.setTangentSpeed(float)"""
        super(__Contact, self).setTangentSpeed(__float.valueOf(arg0))

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
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Contact.isEnabled()"""
        return bool.__wrap(super(Contact, self).isEnabled())

    @overload
    def getTangentSpeed(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Contact.getTangentSpeed()"""
        return float.__wrap(super(Contact, self).getTangentSpeed())

    @overload
    def resetFriction(self):
        """public void com.badlogic.gdx.physics.box2d.Contact.resetFriction()"""
        super(Contact, self).resetFriction()

    @overload
    def setEnabled(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.Contact.setEnabled(boolean)"""
        super(__Contact, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def getWorldManifold(self) -> 'WorldManifold':
        """public com.badlogic.gdx.physics.box2d.WorldManifold com.badlogic.gdx.physics.box2d.Contact.getWorldManifold()"""
        return 'WorldManifold'.__wrap(super(Contact, self).getWorldManifold())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setFriction(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Contact.setFriction(float)"""
        super(__Contact, self).setFriction(__float.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.ChainShape
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.physics.box2d.Shape as __Shape_Type
__Type = __Shape_Type.Type
import com.badlogic.gdx.physics.box2d.Shape as __Shape
__Shape = __Shape
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.physics.box2d.ChainShape as __ChainShape
__ChainShape = __ChainShape
from builtins import int
 
class ChainShape():
    """com.badlogic.gdx.physics.box2d.ChainShape"""
 
    @staticmethod
    def __wrap(java_value: __ChainShape) -> 'ChainShape':
        return ChainShape(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ChainShape):
        """
        Dynamic initializer for ChainShape.
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

    @override
    @overload
    def setRadius(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Shape.setRadius(float)"""
        super(__Shape, self).setRadius(__float.valueOf(arg0))

    @overload
    def createLoop(self, arg0: 'float', arg1: int, arg2: int):
        """public void com.badlogic.gdx.physics.box2d.ChainShape.createLoop(float[],int,int)"""
        super(__ChainShape, self).createLoop(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def setNextVertex(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.ChainShape.setNextVertex(com.badlogic.gdx.math.Vector2)"""
        super(__ChainShape, self).setNextVertex(arg0)

    @overload
    def createLoop(self, arg0: 'float'):
        """public void com.badlogic.gdx.physics.box2d.ChainShape.createLoop(float[])"""
        super(__ChainShape, self).createLoop(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def clear(self):
        """public void com.badlogic.gdx.physics.box2d.ChainShape.clear()"""
        super(ChainShape, self).clear()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def createChain(self, arg0: 'float'):
        """public void com.badlogic.gdx.physics.box2d.ChainShape.createChain(float[])"""
        super(__ChainShape, self).createChain(arg0)

    @overload
    def createChain(self, arg0: 'float', arg1: int, arg2: int):
        """public void com.badlogic.gdx.physics.box2d.ChainShape.createChain(float[],int,int)"""
        super(__ChainShape, self).createChain(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.ChainShape()"""
        val = __ChainShape()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setNextVertex(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.physics.box2d.ChainShape.setNextVertex(float,float)"""
        super(__ChainShape, self).setNextVertex(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def getVertexCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.ChainShape.getVertexCount()"""
        return int.__wrap(super(ChainShape, self).getVertexCount())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def createLoop(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.ChainShape.createLoop(com.badlogic.gdx.math.Vector2[])"""
        super(__ChainShape, self).createLoop(arg0)

    @overload
    def setPrevVertex(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.ChainShape.setPrevVertex(com.badlogic.gdx.math.Vector2)"""
        super(__ChainShape, self).setPrevVertex(arg0)

    @override
    @overload
    def getRadius(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Shape.getRadius()"""
        return float.__wrap(super(Shape, self).getRadius())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setPrevVertex(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.physics.box2d.ChainShape.setPrevVertex(float,float)"""
        super(__ChainShape, self).setPrevVertex(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def createChain(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.ChainShape.createChain(com.badlogic.gdx.math.Vector2[])"""
        super(__ChainShape, self).createChain(arg0)

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.physics.box2d.Shape.dispose()"""
        super(Shape, self).dispose()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isLooped(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.ChainShape.isLooped()"""
        return bool.__wrap(super(ChainShape, self).isLooped())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.ChainShape()"""
        val = __ChainShape()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.Shape.getChildCount()"""
        return int.__wrap(super(Shape, self).getChildCount())

    @override
    @overload
    def getType(self) -> 'Type':
        """public com.badlogic.gdx.physics.box2d.Shape$Type com.badlogic.gdx.physics.box2d.ChainShape.getType()"""
        return 'Type'.__wrap(super(ChainShape, self).getType())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getVertex(self, arg0: int, arg1: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.ChainShape.getVertex(int,com.badlogic.gdx.math.Vector2)"""
        super(__ChainShape, self).getVertex(__int.valueOf(arg0), arg1) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.QueryCallback
from abc import abstractmethod, ABC
import com.badlogic.gdx.physics.box2d.QueryCallback as __QueryCallback
__QueryCallback = __QueryCallback
 
class QueryCallback(ABC):
    """com.badlogic.gdx.physics.box2d.QueryCallback"""
 
    @staticmethod
    def __wrap(java_value: __QueryCallback) -> 'QueryCallback':
        return QueryCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __QueryCallback):
        """
        Dynamic initializer for QueryCallback.
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
    def reportFixture(self, arg0: 'Fixture'):
        """public abstract boolean com.badlogic.gdx.physics.box2d.QueryCallback.reportFixture(com.badlogic.gdx.physics.box2d.Fixture)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.World
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.physics.box2d.Body as __Body
__Body = __Body
import com.badlogic.gdx.physics.box2d.Joint as __Joint
__Joint = __Joint
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.physics.box2d.World as __World
__World = __World
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import int
 
class World():
    """com.badlogic.gdx.physics.box2d.World"""
 
    @staticmethod
    def __wrap(java_value: __World) -> 'World':
        return World(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __World):
        """
        Dynamic initializer for World.
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
    def getJoints(self, arg0: 'Array'):
        """public void com.badlogic.gdx.physics.box2d.World.getJoints(com.badlogic.gdx.utils.Array<com.badlogic.gdx.physics.box2d.Joint>)"""
        super(__World, self).getJoints(arg0)

    @overload
    def setContactListener(self, arg0: 'ContactListener'):
        """public void com.badlogic.gdx.physics.box2d.World.setContactListener(com.badlogic.gdx.physics.box2d.ContactListener)"""
        super(__World, self).setContactListener(arg0)

    @staticmethod
    @overload
    def getVelocityThreshold() -> float:
        """public static native float com.badlogic.gdx.physics.box2d.World.getVelocityThreshold()"""
        return float.__wrap(__World.getVelocityThreshold())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isLocked(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.World.isLocked()"""
        return bool.__wrap(super(World, self).isLocked())

    @overload
    def setDestructionListener(self, arg0: 'DestructionListener'):
        """public void com.badlogic.gdx.physics.box2d.World.setDestructionListener(com.badlogic.gdx.physics.box2d.DestructionListener)"""
        super(__World, self).setDestructionListener(arg0)

    @overload
    def setContactFilter(self, arg0: 'ContactFilter'):
        """public void com.badlogic.gdx.physics.box2d.World.setContactFilter(com.badlogic.gdx.physics.box2d.ContactFilter)"""
        super(__World, self).setContactFilter(arg0)

    @overload
    def getContactCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.World.getContactCount()"""
        return int.__wrap(super(World, self).getContactCount())

    @overload
    def QueryAABB(self, arg0: 'QueryCallback', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.physics.box2d.World.QueryAABB(com.badlogic.gdx.physics.box2d.QueryCallback,float,float,float,float)"""
        super(__World, self).QueryAABB(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def clearForces(self):
        """public void com.badlogic.gdx.physics.box2d.World.clearForces()"""
        super(World, self).clearForces()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def step(self, arg0: float, arg1: int, arg2: int):
        """public void com.badlogic.gdx.physics.box2d.World.step(float,int,int)"""
        super(__World, self).step(__float.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def rayCast(self, arg0: 'RayCastCallback', arg1: 'Vector2', arg2: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.World.rayCast(com.badlogic.gdx.physics.box2d.RayCastCallback,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(__World, self).rayCast(arg0, arg1, arg2)

    @overload
    def getFixtures(self, arg0: 'Array'):
        """public void com.badlogic.gdx.physics.box2d.World.getFixtures(com.badlogic.gdx.utils.Array<com.badlogic.gdx.physics.box2d.Fixture>)"""
        super(__World, self).getFixtures(arg0)

    @overload
    def getProxyCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.World.getProxyCount()"""
        return int.__wrap(super(World, self).getProxyCount())

    @overload
    def getContactList(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.physics.box2d.Contact> com.badlogic.gdx.physics.box2d.World.getContactList()"""
        return 'utils.Array'.__wrap(super(World, self).getContactList())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def setVelocityThreshold(arg0: float):
        """public static native void com.badlogic.gdx.physics.box2d.World.setVelocityThreshold(float)"""
        __World.setVelocityThreshold(__float.valueOf(arg0))

    @overload
    def rayCast(self, arg0: 'RayCastCallback', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.physics.box2d.World.rayCast(com.badlogic.gdx.physics.box2d.RayCastCallback,float,float,float,float)"""
        super(__World, self).rayCast(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.physics.box2d.World.dispose()"""
        super(World, self).dispose()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setWarmStarting(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.World.setWarmStarting(boolean)"""
        super(__World, self).setWarmStarting(__boolean.valueOf(arg0))

    @overload
    def getAutoClearForces(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.World.getAutoClearForces()"""
        return bool.__wrap(super(World, self).getAutoClearForces())

    @overload
    def __init__(self, arg0: 'Vector2', arg1: bool):
        """public com.badlogic.gdx.physics.box2d.World(com.badlogic.gdx.math.Vector2,boolean)"""
        val = __World(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setContinuousPhysics(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.World.setContinuousPhysics(boolean)"""
        super(__World, self).setContinuousPhysics(__boolean.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setGravity(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.World.setGravity(com.badlogic.gdx.math.Vector2)"""
        super(__World, self).setGravity(arg0)

    @overload
    def destroyBody(self, arg0: 'Body'):
        """public void com.badlogic.gdx.physics.box2d.World.destroyBody(com.badlogic.gdx.physics.box2d.Body)"""
        super(__World, self).destroyBody(arg0)

    @overload
    def getBodyCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.World.getBodyCount()"""
        return int.__wrap(super(World, self).getBodyCount())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getGravity(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.World.getGravity()"""
        return 'math.Vector2'.__wrap(super(World, self).getGravity())

    @overload
    def createJoint(self, arg0: 'JointDef') -> 'Joint':
        """public com.badlogic.gdx.physics.box2d.Joint com.badlogic.gdx.physics.box2d.World.createJoint(com.badlogic.gdx.physics.box2d.JointDef)"""
        return 'Joint'.__wrap(super(__World, self).createJoint(arg0))

    @overload
    def destroyJoint(self, arg0: 'Joint'):
        """public void com.badlogic.gdx.physics.box2d.World.destroyJoint(com.badlogic.gdx.physics.box2d.Joint)"""
        super(__World, self).destroyJoint(arg0)

    @overload
    def getBodies(self, arg0: 'Array'):
        """public void com.badlogic.gdx.physics.box2d.World.getBodies(com.badlogic.gdx.utils.Array<com.badlogic.gdx.physics.box2d.Body>)"""
        super(__World, self).getBodies(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def createBody(self, arg0: 'BodyDef') -> 'Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.World.createBody(com.badlogic.gdx.physics.box2d.BodyDef)"""
        return 'Body'.__wrap(super(__World, self).createBody(arg0))

    @overload
    def getJointCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.World.getJointCount()"""
        return int.__wrap(super(World, self).getJointCount())

    @overload
    def setAutoClearForces(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.World.setAutoClearForces(boolean)"""
        super(__World, self).setAutoClearForces(__boolean.valueOf(arg0))

    @overload
    def getFixtureCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.World.getFixtureCount()"""
        return int.__wrap(super(World, self).getFixtureCount()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.BodyDef$BodyType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.physics.box2d.BodyDef as __BodyDef_BodyType
__BodyType = __BodyDef_BodyType.BodyType
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class BodyType():
    """com.badlogic.gdx.physics.box2d.BodyDef.BodyType"""
 
    @staticmethod
    def __wrap(java_value: __BodyType) -> 'BodyType':
        return BodyType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BodyType):
        """
        Dynamic initializer for BodyType.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def values() -> List['BodyType']:
        """public static com.badlogic.gdx.physics.box2d.BodyDef$BodyType[] com.badlogic.gdx.physics.box2d.BodyDef$BodyType.values()"""
        return List[BodyType].__wrap(__BodyType.values())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'BodyType':
        """public static com.badlogic.gdx.physics.box2d.BodyDef$BodyType com.badlogic.gdx.physics.box2d.BodyDef$BodyType.valueOf(java.lang.String)"""
        return BodyType.__wrap(__BodyType.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())

    @overload
    def getValue(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.BodyDef$BodyType.getValue()"""
        return int.__wrap(super(BodyType, self).getValue()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.Body
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
import com.badlogic.gdx.physics.box2d.Transform as __Transform
__Transform = __Transform
from builtins import type
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.physics.box2d.World as __World
__World = __World
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import com.badlogic.gdx.physics.box2d.Fixture as __Fixture
__Fixture = __Fixture
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
import com.badlogic.gdx.physics.box2d.Body as __Body
__Body = __Body
from builtins import object
import com.badlogic.gdx.physics.box2d.MassData as __MassData
__MassData = __MassData
import java.lang.Long as __long
import java.lang.Float as __float
import com.badlogic.gdx.physics.box2d.BodyDef as __BodyDef_BodyType
__BodyType = __BodyDef_BodyType.BodyType
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import int
 
class Body():
    """com.badlogic.gdx.physics.box2d.Body"""
 
    @staticmethod
    def __wrap(java_value: __Body) -> 'Body':
        return Body(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Body):
        """
        Dynamic initializer for Body.
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
    def isBullet(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Body.isBullet()"""
        return bool.__wrap(super(Body, self).isBullet())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getLocalPoint(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Body.getLocalPoint(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Body, self).getLocalPoint(arg0))

    @overload
    def getFixtureList(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.physics.box2d.Fixture> com.badlogic.gdx.physics.box2d.Body.getFixtureList()"""
        return 'utils.Array'.__wrap(super(Body, self).getFixtureList())

    @overload
    def getAngularDamping(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Body.getAngularDamping()"""
        return float.__wrap(super(Body, self).getAngularDamping())

    @overload
    def getWorldPoint(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Body.getWorldPoint(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Body, self).getWorldPoint(arg0))

    @overload
    def setTransform(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.physics.box2d.Body.setTransform(float,float,float)"""
        super(__Body, self).setTransform(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def resetMassData(self):
        """public void com.badlogic.gdx.physics.box2d.Body.resetMassData()"""
        super(Body, self).resetMassData()

    @overload
    def getLocalCenter(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Body.getLocalCenter()"""
        return 'math.Vector2'.__wrap(super(Body, self).getLocalCenter())

    @overload
    def getAngle(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Body.getAngle()"""
        return float.__wrap(super(Body, self).getAngle())

    @overload
    def setAngularDamping(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Body.setAngularDamping(float)"""
        super(__Body, self).setAngularDamping(__float.valueOf(arg0))

    @overload
    def applyLinearImpulse(self, arg0: 'Vector2', arg1: 'Vector2', arg2: bool):
        """public void com.badlogic.gdx.physics.box2d.Body.applyLinearImpulse(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,boolean)"""
        super(__Body, self).applyLinearImpulse(arg0, arg1, __boolean.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def applyTorque(self, arg0: float, arg1: bool):
        """public void com.badlogic.gdx.physics.box2d.Body.applyTorque(float,boolean)"""
        super(__Body, self).applyTorque(__float.valueOf(arg0), __boolean.valueOf(arg1))

    @overload
    def getInertia(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Body.getInertia()"""
        return float.__wrap(super(Body, self).getInertia())

    @overload
    def getType(self) -> 'BodyType':
        """public com.badlogic.gdx.physics.box2d.BodyDef$BodyType com.badlogic.gdx.physics.box2d.Body.getType()"""
        return 'BodyType'.__wrap(super(Body, self).getType())

    @overload
    def setLinearDamping(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Body.setLinearDamping(float)"""
        super(__Body, self).setLinearDamping(__float.valueOf(arg0))

    @overload
    def setAwake(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.Body.setAwake(boolean)"""
        super(__Body, self).setAwake(__boolean.valueOf(arg0))

    @overload
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Body.setUserData(java.lang.Object)"""
        super(__Body, self).setUserData(arg0)

    @overload
    def setType(self, arg0: 'BodyType'):
        """public void com.badlogic.gdx.physics.box2d.Body.setType(com.badlogic.gdx.physics.box2d.BodyDef$BodyType)"""
        super(__Body, self).setType(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def isAwake(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Body.isAwake()"""
        return bool.__wrap(super(Body, self).isAwake())

    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Body.getUserData()"""
        return object.__wrap(super(Body, self).getUserData())

    @overload
    def destroyFixture(self, arg0: 'Fixture'):
        """public void com.badlogic.gdx.physics.box2d.Body.destroyFixture(com.badlogic.gdx.physics.box2d.Fixture)"""
        super(__Body, self).destroyFixture(arg0)

    @overload
    def getLocalVector(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Body.getLocalVector(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Body, self).getLocalVector(arg0))

    @overload
    def getLinearVelocity(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Body.getLinearVelocity()"""
        return 'math.Vector2'.__wrap(super(Body, self).getLinearVelocity())

    @overload
    def getLinearVelocityFromLocalPoint(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Body.getLinearVelocityFromLocalPoint(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Body, self).getLinearVelocityFromLocalPoint(arg0))

    @overload
    def getLinearVelocityFromWorldPoint(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Body.getLinearVelocityFromWorldPoint(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Body, self).getLinearVelocityFromWorldPoint(arg0))

    @overload
    def applyAngularImpulse(self, arg0: float, arg1: bool):
        """public void com.badlogic.gdx.physics.box2d.Body.applyAngularImpulse(float,boolean)"""
        super(__Body, self).applyAngularImpulse(__float.valueOf(arg0), __boolean.valueOf(arg1))

    @overload
    def isFixedRotation(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Body.isFixedRotation()"""
        return bool.__wrap(super(Body, self).isFixedRotation())

    @overload
    def isSleepingAllowed(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Body.isSleepingAllowed()"""
        return bool.__wrap(super(Body, self).isSleepingAllowed())

    @overload
    def createFixture(self, arg0: 'Shape', arg1: float) -> 'Fixture':
        """public com.badlogic.gdx.physics.box2d.Fixture com.badlogic.gdx.physics.box2d.Body.createFixture(com.badlogic.gdx.physics.box2d.Shape,float)"""
        return 'Fixture'.__wrap(super(__Body, self).createFixture(arg0, __float.valueOf(arg1)))

    @overload
    def applyLinearImpulse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: bool):
        """public void com.badlogic.gdx.physics.box2d.Body.applyLinearImpulse(float,float,float,float,boolean)"""
        super(__Body, self).applyLinearImpulse(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __boolean.valueOf(arg4))

    @overload
    def applyForceToCenter(self, arg0: float, arg1: float, arg2: bool):
        """public void com.badlogic.gdx.physics.box2d.Body.applyForceToCenter(float,float,boolean)"""
        super(__Body, self).applyForceToCenter(__float.valueOf(arg0), __float.valueOf(arg1), __boolean.valueOf(arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setMassData(self, arg0: 'MassData'):
        """public void com.badlogic.gdx.physics.box2d.Body.setMassData(com.badlogic.gdx.physics.box2d.MassData)"""
        super(__Body, self).setMassData(arg0)

    @overload
    def getWorldVector(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Body.getWorldVector(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Body, self).getWorldVector(arg0))

    @overload
    def setGravityScale(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Body.setGravityScale(float)"""
        super(__Body, self).setGravityScale(__float.valueOf(arg0))

    @overload
    def getMass(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Body.getMass()"""
        return float.__wrap(super(Body, self).getMass())

    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Body.isActive()"""
        return bool.__wrap(super(Body, self).isActive())

    @overload
    def setLinearVelocity(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.Body.setLinearVelocity(com.badlogic.gdx.math.Vector2)"""
        super(__Body, self).setLinearVelocity(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getWorldCenter(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Body.getWorldCenter()"""
        return 'math.Vector2'.__wrap(super(Body, self).getWorldCenter())

    @overload
    def setLinearVelocity(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.physics.box2d.Body.setLinearVelocity(float,float)"""
        super(__Body, self).setLinearVelocity(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def setBullet(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.Body.setBullet(boolean)"""
        super(__Body, self).setBullet(__boolean.valueOf(arg0))

    @overload
    def applyForceToCenter(self, arg0: 'Vector2', arg1: bool):
        """public void com.badlogic.gdx.physics.box2d.Body.applyForceToCenter(com.badlogic.gdx.math.Vector2,boolean)"""
        super(__Body, self).applyForceToCenter(arg0, __boolean.valueOf(arg1))

    @overload
    def getTransform(self) -> 'Transform':
        """public com.badlogic.gdx.physics.box2d.Transform com.badlogic.gdx.physics.box2d.Body.getTransform()"""
        return 'Transform'.__wrap(super(Body, self).getTransform())

    @overload
    def getJointList(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.physics.box2d.JointEdge> com.badlogic.gdx.physics.box2d.Body.getJointList()"""
        return 'utils.Array'.__wrap(super(Body, self).getJointList())

    @overload
    def getGravityScale(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Body.getGravityScale()"""
        return float.__wrap(super(Body, self).getGravityScale())

    @overload
    def setAngularVelocity(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Body.setAngularVelocity(float)"""
        super(__Body, self).setAngularVelocity(__float.valueOf(arg0))

    @overload
    def getWorld(self) -> 'World':
        """public com.badlogic.gdx.physics.box2d.World com.badlogic.gdx.physics.box2d.Body.getWorld()"""
        return 'World'.__wrap(super(Body, self).getWorld())

    @overload
    def setSleepingAllowed(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.Body.setSleepingAllowed(boolean)"""
        super(__Body, self).setSleepingAllowed(__boolean.valueOf(arg0))

    @overload
    def applyForce(self, arg0: 'Vector2', arg1: 'Vector2', arg2: bool):
        """public void com.badlogic.gdx.physics.box2d.Body.applyForce(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,boolean)"""
        super(__Body, self).applyForce(arg0, arg1, __boolean.valueOf(arg2))

    @overload
    def getMassData(self) -> 'MassData':
        """public com.badlogic.gdx.physics.box2d.MassData com.badlogic.gdx.physics.box2d.Body.getMassData()"""
        return 'MassData'.__wrap(super(Body, self).getMassData())

    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.Body.setActive(boolean)"""
        super(__Body, self).setActive(__boolean.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def createFixture(self, arg0: 'FixtureDef') -> 'Fixture':
        """public com.badlogic.gdx.physics.box2d.Fixture com.badlogic.gdx.physics.box2d.Body.createFixture(com.badlogic.gdx.physics.box2d.FixtureDef)"""
        return 'Fixture'.__wrap(super(__Body, self).createFixture(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def applyForce(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: bool):
        """public void com.badlogic.gdx.physics.box2d.Body.applyForce(float,float,float,float,boolean)"""
        super(__Body, self).applyForce(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __boolean.valueOf(arg4))

    @overload
    def getLinearDamping(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Body.getLinearDamping()"""
        return float.__wrap(super(Body, self).getLinearDamping())

    @overload
    def getPosition(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Body.getPosition()"""
        return 'math.Vector2'.__wrap(super(Body, self).getPosition())

    @overload
    def setTransform(self, arg0: 'Vector2', arg1: float):
        """public void com.badlogic.gdx.physics.box2d.Body.setTransform(com.badlogic.gdx.math.Vector2,float)"""
        super(__Body, self).setTransform(arg0, __float.valueOf(arg1))

    @overload
    def setFixedRotation(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.Body.setFixedRotation(boolean)"""
        super(__Body, self).setFixedRotation(__boolean.valueOf(arg0))

    @overload
    def getAngularVelocity(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Body.getAngularVelocity()"""
        return float.__wrap(super(Body, self).getAngularVelocity()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.PolygonShape
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.physics.box2d.PolygonShape as __PolygonShape
__PolygonShape = __PolygonShape
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.physics.box2d.Shape as __Shape_Type
__Type = __Shape_Type.Type
import com.badlogic.gdx.physics.box2d.Shape as __Shape
__Shape = __Shape
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PolygonShape():
    """com.badlogic.gdx.physics.box2d.PolygonShape"""
 
    @staticmethod
    def __wrap(java_value: __PolygonShape) -> 'PolygonShape':
        return PolygonShape(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PolygonShape):
        """
        Dynamic initializer for PolygonShape.
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
    def set(self, arg0: 'float'):
        """public void com.badlogic.gdx.physics.box2d.PolygonShape.set(float[])"""
        super(__PolygonShape, self).set(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.PolygonShape()"""
        val = __PolygonShape()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setRadius(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Shape.setRadius(float)"""
        super(__Shape, self).setRadius(__float.valueOf(arg0))

    @override
    @overload
    def getRadius(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Shape.getRadius()"""
        return float.__wrap(super(Shape, self).getRadius())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def set(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.PolygonShape.set(com.badlogic.gdx.math.Vector2[])"""
        super(__PolygonShape, self).set(arg0)

    @overload
    def getVertex(self, arg0: int, arg1: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.PolygonShape.getVertex(int,com.badlogic.gdx.math.Vector2)"""
        super(__PolygonShape, self).getVertex(__int.valueOf(arg0), arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.physics.box2d.Shape.dispose()"""
        super(Shape, self).dispose()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def set(self, arg0: 'float', arg1: int, arg2: int):
        """public void com.badlogic.gdx.physics.box2d.PolygonShape.set(float[],int,int)"""
        super(__PolygonShape, self).set(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getVertexCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.PolygonShape.getVertexCount()"""
        return int.__wrap(super(PolygonShape, self).getVertexCount())

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.Shape.getChildCount()"""
        return int.__wrap(super(Shape, self).getChildCount())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setAsBox(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.physics.box2d.PolygonShape.setAsBox(float,float)"""
        super(__PolygonShape, self).setAsBox(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getType(self) -> 'Type':
        """public com.badlogic.gdx.physics.box2d.Shape$Type com.badlogic.gdx.physics.box2d.PolygonShape.getType()"""
        return 'Type'.__wrap(super(PolygonShape, self).getType())

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
    def setAsBox(self, arg0: float, arg1: float, arg2: 'Vector2', arg3: float):
        """public void com.badlogic.gdx.physics.box2d.PolygonShape.setAsBox(float,float,com.badlogic.gdx.math.Vector2,float)"""
        super(__PolygonShape, self).setAsBox(__float.valueOf(arg0), __float.valueOf(arg1), arg2, __float.valueOf(arg3))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.PolygonShape()"""
        val = __PolygonShape()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.RayCastCallback
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from abc import abstractmethod, ABC
import com.badlogic.gdx.physics.box2d.RayCastCallback as __RayCastCallback
__RayCastCallback = __RayCastCallback
 
class RayCastCallback(ABC):
    """com.badlogic.gdx.physics.box2d.RayCastCallback"""
 
    @staticmethod
    def __wrap(java_value: __RayCastCallback) -> 'RayCastCallback':
        return RayCastCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RayCastCallback):
        """
        Dynamic initializer for RayCastCallback.
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
    def reportRayFixture(self, arg0: 'Fixture', arg1: 'Vector2', arg2: 'Vector2', arg3: float):
        """public abstract float com.badlogic.gdx.physics.box2d.RayCastCallback.reportRayFixture(com.badlogic.gdx.physics.box2d.Fixture,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,float)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.JointEdge
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
import com.badlogic.gdx.physics.box2d.JointEdge as __JointEdge
__JointEdge = __JointEdge
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class JointEdge():
    """com.badlogic.gdx.physics.box2d.JointEdge"""
 
    @staticmethod
    def __wrap(java_value: __JointEdge) -> 'JointEdge':
        return JointEdge(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JointEdge):
        """
        Dynamic initializer for JointEdge.
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
 
 
# CLASS: com.badlogic.gdx.physics.box2d.Box2D
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
import com.badlogic.gdx.physics.box2d.Box2D as __Box2D
__Box2D = __Box2D
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Box2D():
    """com.badlogic.gdx.physics.box2d.Box2D"""
 
    @staticmethod
    def __wrap(java_value: __Box2D) -> 'Box2D':
        return Box2D(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Box2D):
        """
        Dynamic initializer for Box2D.
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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

        @staticmethod
        @overload
        def init():
            """public static void com.badlogic.gdx.physics.box2d.Box2D.init()"""
            __Box2D.init()

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
 
 
# CLASS: com.badlogic.gdx.physics.box2d.ContactListener
import com.badlogic.gdx.physics.box2d.ContactListener as __ContactListener
__ContactListener = __ContactListener
from abc import abstractmethod, ABC
 
class ContactListener(ABC):
    """com.badlogic.gdx.physics.box2d.ContactListener"""
 
    @staticmethod
    def __wrap(java_value: __ContactListener) -> 'ContactListener':
        return ContactListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ContactListener):
        """
        Dynamic initializer for ContactListener.
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
    def preSolve(self, arg0: 'Contact', arg1: 'Manifold'):
        """public abstract void com.badlogic.gdx.physics.box2d.ContactListener.preSolve(com.badlogic.gdx.physics.box2d.Contact,com.badlogic.gdx.physics.box2d.Manifold)"""
        pass

    @abstractmethod
    def postSolve(self, arg0: 'Contact', arg1: 'ContactImpulse'):
        """public abstract void com.badlogic.gdx.physics.box2d.ContactListener.postSolve(com.badlogic.gdx.physics.box2d.Contact,com.badlogic.gdx.physics.box2d.ContactImpulse)"""
        pass

    @abstractmethod
    def beginContact(self, arg0: 'Contact'):
        """public abstract void com.badlogic.gdx.physics.box2d.ContactListener.beginContact(com.badlogic.gdx.physics.box2d.Contact)"""
        pass

    @abstractmethod
    def endContact(self, arg0: 'Contact'):
        """public abstract void com.badlogic.gdx.physics.box2d.ContactListener.endContact(com.badlogic.gdx.physics.box2d.Contact)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.ContactImpulse
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.physics.box2d.ContactImpulse as __ContactImpulse
__ContactImpulse = __ContactImpulse
from builtins import float
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ContactImpulse():
    """com.badlogic.gdx.physics.box2d.ContactImpulse"""
 
    @staticmethod
    def __wrap(java_value: __ContactImpulse) -> 'ContactImpulse':
        return ContactImpulse(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ContactImpulse):
        """
        Dynamic initializer for ContactImpulse.
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
    def getCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.ContactImpulse.getCount()"""
        return int.__wrap(super(ContactImpulse, self).getCount())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getTangentImpulses(self) -> List[float]:
        """public float[] com.badlogic.gdx.physics.box2d.ContactImpulse.getTangentImpulses()"""
        return List[float].__wrap(super(ContactImpulse, self).getTangentImpulses())

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
    def getNormalImpulses(self) -> List[float]:
        """public float[] com.badlogic.gdx.physics.box2d.ContactImpulse.getNormalImpulses()"""
        return List[float].__wrap(super(ContactImpulse, self).getNormalImpulses()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.Filter
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
import com.badlogic.gdx.physics.box2d.Filter as __Filter
__Filter = __Filter
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Filter():
    """com.badlogic.gdx.physics.box2d.Filter"""
 
    @staticmethod
    def __wrap(java_value: __Filter) -> 'Filter':
        return Filter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Filter):
        """
        Dynamic initializer for Filter.
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
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.Filter()"""
        val = __Filter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.Filter()"""
        val = __Filter()
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

    @overload
    def set(self, arg0: 'Filter'):
        """public void com.badlogic.gdx.physics.box2d.Filter.set(com.badlogic.gdx.physics.box2d.Filter)"""
        super(__Filter, self).set(arg0)

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
 
 
# CLASS: com.badlogic.gdx.physics.box2d.JointDef$JointType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import com.badlogic.gdx.physics.box2d.JointDef as __JointDef_JointType
__JointType = __JointDef_JointType.JointType
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class JointType():
    """com.badlogic.gdx.physics.box2d.JointDef.JointType"""
 
    @staticmethod
    def __wrap(java_value: __JointType) -> 'JointType':
        return JointType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JointType):
        """
        Dynamic initializer for JointType.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def values() -> List['JointType']:
        """public static com.badlogic.gdx.physics.box2d.JointDef$JointType[] com.badlogic.gdx.physics.box2d.JointDef$JointType.values()"""
        return List[JointType].__wrap(__JointType.values())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'JointType':
        """public static com.badlogic.gdx.physics.box2d.JointDef$JointType com.badlogic.gdx.physics.box2d.JointDef$JointType.valueOf(java.lang.String)"""
        return JointType.__wrap(__JointType.valueOf(arg0))

    @overload
    def getValue(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.JointDef$JointType.getValue()"""
        return int.__wrap(super(JointType, self).getValue())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.Manifold$ManifoldType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import com.badlogic.gdx.physics.box2d.Manifold as __Manifold_ManifoldType
__ManifoldType = __Manifold_ManifoldType.ManifoldType
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class ManifoldType():
    """com.badlogic.gdx.physics.box2d.Manifold.ManifoldType"""
 
    @staticmethod
    def __wrap(java_value: __ManifoldType) -> 'ManifoldType':
        return ManifoldType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ManifoldType):
        """
        Dynamic initializer for ManifoldType.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ManifoldType':
        """public static com.badlogic.gdx.physics.box2d.Manifold$ManifoldType com.badlogic.gdx.physics.box2d.Manifold$ManifoldType.valueOf(java.lang.String)"""
        return ManifoldType.__wrap(__ManifoldType.valueOf(arg0))

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())

    @staticmethod
    @overload
    def values() -> List['ManifoldType']:
        """public static com.badlogic.gdx.physics.box2d.Manifold$ManifoldType[] com.badlogic.gdx.physics.box2d.Manifold$ManifoldType.values()"""
        return List[ManifoldType].__wrap(__ManifoldType.values()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.Fixture
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.physics.box2d.Body as __Body
__Body = __Body
import com.badlogic.gdx.physics.box2d.Filter as __Filter
__Filter = __Filter
from builtins import object
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.physics.box2d.Fixture as __Fixture
__Fixture = __Fixture
import com.badlogic.gdx.physics.box2d.Shape as __Shape_Type
__Type = __Shape_Type.Type
import com.badlogic.gdx.physics.box2d.Shape as __Shape
__Shape = __Shape
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Fixture():
    """com.badlogic.gdx.physics.box2d.Fixture"""
 
    @staticmethod
    def __wrap(java_value: __Fixture) -> 'Fixture':
        return Fixture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Fixture):
        """
        Dynamic initializer for Fixture.
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
    def setSensor(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.Fixture.setSensor(boolean)"""
        super(__Fixture, self).setSensor(__boolean.valueOf(arg0))

    @overload
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Fixture.setUserData(java.lang.Object)"""
        super(__Fixture, self).setUserData(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isSensor(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Fixture.isSensor()"""
        return bool.__wrap(super(Fixture, self).isSensor())

    @overload
    def testPoint(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Fixture.testPoint(float,float)"""
        return bool.__wrap(super(__Fixture, self).testPoint(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def setRestitution(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Fixture.setRestitution(float)"""
        super(__Fixture, self).setRestitution(__float.valueOf(arg0))

    @overload
    def setFilterData(self, arg0: 'Filter'):
        """public void com.badlogic.gdx.physics.box2d.Fixture.setFilterData(com.badlogic.gdx.physics.box2d.Filter)"""
        super(__Fixture, self).setFilterData(arg0)

    @overload
    def getShape(self) -> 'Shape':
        """public com.badlogic.gdx.physics.box2d.Shape com.badlogic.gdx.physics.box2d.Fixture.getShape()"""
        return 'Shape'.__wrap(super(Fixture, self).getShape())

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

    @overload
    def getType(self) -> 'Type':
        """public com.badlogic.gdx.physics.box2d.Shape$Type com.badlogic.gdx.physics.box2d.Fixture.getType()"""
        return 'Type'.__wrap(super(Fixture, self).getType())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setDensity(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Fixture.setDensity(float)"""
        super(__Fixture, self).setDensity(__float.valueOf(arg0))

    @overload
    def getDensity(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Fixture.getDensity()"""
        return float.__wrap(super(Fixture, self).getDensity())

    @overload
    def getBody(self) -> 'Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Fixture.getBody()"""
        return 'Body'.__wrap(super(Fixture, self).getBody())

    @overload
    def getRestitution(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Fixture.getRestitution()"""
        return float.__wrap(super(Fixture, self).getRestitution())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def testPoint(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Fixture.testPoint(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__Fixture, self).testPoint(arg0))

    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Fixture.getUserData()"""
        return object.__wrap(super(Fixture, self).getUserData())

    @overload
    def setFriction(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Fixture.setFriction(float)"""
        super(__Fixture, self).setFriction(__float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getFilterData(self) -> 'Filter':
        """public com.badlogic.gdx.physics.box2d.Filter com.badlogic.gdx.physics.box2d.Fixture.getFilterData()"""
        return 'Filter'.__wrap(super(Fixture, self).getFilterData())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def refilter(self):
        """public void com.badlogic.gdx.physics.box2d.Fixture.refilter()"""
        super(Fixture, self).refilter()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getFriction(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Fixture.getFriction()"""
        return float.__wrap(super(Fixture, self).getFriction()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.Shape
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.physics.box2d.Shape as __Shape
__Shape = __Shape
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Shape(ABC):
    """com.badlogic.gdx.physics.box2d.Shape"""
 
    @staticmethod
    def __wrap(java_value: __Shape) -> 'Shape':
        return Shape(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Shape):
        """
        Dynamic initializer for Shape.
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.Shape()"""
        val = __Shape()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getRadius(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Shape.getRadius()"""
        return float.__wrap(super(Shape, self).getRadius())

    @abstractmethod
    def getType(self, ):
        """public abstract com.badlogic.gdx.physics.box2d.Shape$Type com.badlogic.gdx.physics.box2d.Shape.getType()"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.physics.box2d.Shape.dispose()"""
        super(Shape, self).dispose()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setRadius(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Shape.setRadius(float)"""
        super(__Shape, self).setRadius(__float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.Shape.getChildCount()"""
        return int.__wrap(super(Shape, self).getChildCount())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.Shape()"""
        val = __Shape()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.physics.box2d.BodyDef
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import com.badlogic.gdx.physics.box2d.BodyDef as __BodyDef
__BodyDef = __BodyDef
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BodyDef():
    """com.badlogic.gdx.physics.box2d.BodyDef"""
 
    @staticmethod
    def __wrap(java_value: __BodyDef) -> 'BodyDef':
        return BodyDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BodyDef):
        """
        Dynamic initializer for BodyDef.
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
        """public com.badlogic.gdx.physics.box2d.BodyDef()"""
        val = __BodyDef()
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
        """public com.badlogic.gdx.physics.box2d.BodyDef()"""
        val = __BodyDef()
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
 
 
# CLASS: com.badlogic.gdx.physics.box2d.JointDef
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import com.badlogic.gdx.physics.box2d.JointDef as __JointDef
__JointDef = __JointDef
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class JointDef():
    """com.badlogic.gdx.physics.box2d.JointDef"""
 
    @staticmethod
    def __wrap(java_value: __JointDef) -> 'JointDef':
        return JointDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JointDef):
        """
        Dynamic initializer for JointDef.
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
        """public com.badlogic.gdx.physics.box2d.JointDef()"""
        val = __JointDef()
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.JointDef()"""
        val = __JointDef()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.Shape$Type
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.physics.box2d.Shape as __Shape_Type
__Type = __Shape_Type.Type
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Type():
    """com.badlogic.gdx.physics.box2d.Shape.Type"""
 
    @staticmethod
    def __wrap(java_value: __Type) -> 'Type':
        return Type(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Type):
        """
        Dynamic initializer for Type.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def values() -> List['Type']:
        """public static com.badlogic.gdx.physics.box2d.Shape$Type[] com.badlogic.gdx.physics.box2d.Shape$Type.values()"""
        return List[Type].__wrap(__Type.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Type':
        """public static com.badlogic.gdx.physics.box2d.Shape$Type com.badlogic.gdx.physics.box2d.Shape$Type.valueOf(java.lang.String)"""
        return Type.__wrap(__Type.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.CircleShape
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.physics.box2d.CircleShape as __CircleShape
__CircleShape = __CircleShape
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.physics.box2d.Shape as __Shape_Type
__Type = __Shape_Type.Type
import com.badlogic.gdx.physics.box2d.Shape as __Shape
__Shape = __Shape
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CircleShape():
    """com.badlogic.gdx.physics.box2d.CircleShape"""
 
    @staticmethod
    def __wrap(java_value: __CircleShape) -> 'CircleShape':
        return CircleShape(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CircleShape):
        """
        Dynamic initializer for CircleShape.
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

    @override
    @overload
    def setRadius(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Shape.setRadius(float)"""
        super(__Shape, self).setRadius(__float.valueOf(arg0))

    @override
    @overload
    def getRadius(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Shape.getRadius()"""
        return float.__wrap(super(Shape, self).getRadius())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getType(self) -> 'Type':
        """public com.badlogic.gdx.physics.box2d.Shape$Type com.badlogic.gdx.physics.box2d.CircleShape.getType()"""
        return 'Type'.__wrap(super(CircleShape, self).getType())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.CircleShape()"""
        val = __CircleShape()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.CircleShape()"""
        val = __CircleShape()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setPosition(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.CircleShape.setPosition(com.badlogic.gdx.math.Vector2)"""
        super(__CircleShape, self).setPosition(arg0)

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.physics.box2d.Shape.dispose()"""
        super(Shape, self).dispose()

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

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.Shape.getChildCount()"""
        return int.__wrap(super(Shape, self).getChildCount())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getPosition(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.CircleShape.getPosition()"""
        return 'math.Vector2'.__wrap(super(CircleShape, self).getPosition())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.Manifold
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from typing import List
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import com.badlogic.gdx.physics.box2d.Manifold as __Manifold_ManifoldPoint
__ManifoldPoint = __Manifold_ManifoldPoint.ManifoldPoint
import java.lang.Long as __long
import com.badlogic.gdx.physics.box2d.Manifold as __Manifold_ManifoldType
__ManifoldType = __Manifold_ManifoldType.ManifoldType
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.physics.box2d.Manifold as __Manifold
__Manifold = __Manifold
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Manifold():
    """com.badlogic.gdx.physics.box2d.Manifold"""
 
    @staticmethod
    def __wrap(java_value: __Manifold) -> 'Manifold':
        return Manifold(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Manifold):
        """
        Dynamic initializer for Manifold.
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getType(self) -> 'ManifoldType':
        """public com.badlogic.gdx.physics.box2d.Manifold$ManifoldType com.badlogic.gdx.physics.box2d.Manifold.getType()"""
        return 'ManifoldType'.__wrap(super(Manifold, self).getType())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getPointCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.Manifold.getPointCount()"""
        return int.__wrap(super(Manifold, self).getPointCount())

    @overload
    def getLocalPoint(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Manifold.getLocalPoint()"""
        return 'math.Vector2'.__wrap(super(Manifold, self).getLocalPoint())

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
    def getPoints(self) -> List['ManifoldPoint']:
        """public com.badlogic.gdx.physics.box2d.Manifold$ManifoldPoint[] com.badlogic.gdx.physics.box2d.Manifold.getPoints()"""
        return List['ManifoldPoint'].__wrap(super(Manifold, self).getPoints())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getLocalNormal(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Manifold.getLocalNormal()"""
        return 'math.Vector2'.__wrap(super(Manifold, self).getLocalNormal())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.Joint
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.physics.box2d.JointDef as __JointDef_JointType
__JointType = __JointDef_JointType.JointType
import com.badlogic.gdx.physics.box2d.Body as __Body
__Body = __Body
from builtins import object
import com.badlogic.gdx.physics.box2d.Joint as __Joint
__Joint = __Joint
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Joint(ABC):
    """com.badlogic.gdx.physics.box2d.Joint"""
 
    @staticmethod
    def __wrap(java_value: __Joint) -> 'Joint':
        return Joint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Joint):
        """
        Dynamic initializer for Joint.
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
    def getType(self) -> 'JointType':
        """public com.badlogic.gdx.physics.box2d.JointDef$JointType com.badlogic.gdx.physics.box2d.Joint.getType()"""
        return 'JointType'.__wrap(super(Joint, self).getType())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.isActive()"""
        return bool.__wrap(super(Joint, self).isActive())

    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Joint.getUserData()"""
        return object.__wrap(super(Joint, self).getUserData())

    @overload
    def getBodyA(self) -> 'Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyA()"""
        return 'Body'.__wrap(super(Joint, self).getBodyA())

    @overload
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Joint.setUserData(java.lang.Object)"""
        super(__Joint, self).setUserData(arg0)

    @overload
    def getReactionTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.Joint.getReactionTorque(float)"""
        return float.__wrap(super(__Joint, self).getReactionTorque(__float.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getReactionForce(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getReactionForce(float)"""
        return 'math.Vector2'.__wrap(super(__Joint, self).getReactionForce(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorB()"""
        return 'math.Vector2'.__wrap(super(Joint, self).getAnchorB())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorA()"""
        return 'math.Vector2'.__wrap(super(Joint, self).getAnchorA())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getBodyB(self) -> 'Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyB()"""
        return 'Body'.__wrap(super(Joint, self).getBodyB())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getCollideConnected(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.getCollideConnected()"""
        return bool.__wrap(super(Joint, self).getCollideConnected())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.ContactFilter
from abc import abstractmethod, ABC
import com.badlogic.gdx.physics.box2d.ContactFilter as __ContactFilter
__ContactFilter = __ContactFilter
 
class ContactFilter(ABC):
    """com.badlogic.gdx.physics.box2d.ContactFilter"""
 
    @staticmethod
    def __wrap(java_value: __ContactFilter) -> 'ContactFilter':
        return ContactFilter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ContactFilter):
        """
        Dynamic initializer for ContactFilter.
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
    def shouldCollide(self, arg0: 'Fixture', arg1: 'Fixture'):
        """public abstract boolean com.badlogic.gdx.physics.box2d.ContactFilter.shouldCollide(com.badlogic.gdx.physics.box2d.Fixture,com.badlogic.gdx.physics.box2d.Fixture)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.MassData
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
import com.badlogic.gdx.physics.box2d.MassData as __MassData
__MassData = __MassData
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MassData():
    """com.badlogic.gdx.physics.box2d.MassData"""
 
    @staticmethod
    def __wrap(java_value: __MassData) -> 'MassData':
        return MassData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MassData):
        """
        Dynamic initializer for MassData.
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
        """public com.badlogic.gdx.physics.box2d.MassData()"""
        val = __MassData()
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
        """public com.badlogic.gdx.physics.box2d.MassData()"""
        val = __MassData()
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