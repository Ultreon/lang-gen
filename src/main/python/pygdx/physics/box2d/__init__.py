from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
from typing import List
import com.badlogic.gdx.physics.box2d.WorldManifold as _WorldManifold
_WorldManifold = _WorldManifold
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WorldManifold():
    """com.badlogic.gdx.physics.box2d.WorldManifold"""
 
    @staticmethod
    def _wrap(java_value: _WorldManifold) -> 'WorldManifold':
        return WorldManifold(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldManifold):
        """
        Dynamic initializer for WorldManifold.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldManifold__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldManifold__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getPoints(self) -> List['math.Vector2']:
        """public com.badlogic.gdx.math.Vector2[] com.badlogic.gdx.physics.box2d.WorldManifold.getPoints()"""
        return List['math.Vector2']._wrap(super(WorldManifold, self).getPoints())

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
    def getSeparations(self) -> List[float]:
        """public float[] com.badlogic.gdx.physics.box2d.WorldManifold.getSeparations()"""
        return List[float]._wrap(super(WorldManifold, self).getSeparations())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getNumberOfContactPoints(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.WorldManifold.getNumberOfContactPoints()"""
        return int._wrap(super(WorldManifold, self).getNumberOfContactPoints())

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
    def getNormal(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.WorldManifold.getNormal()"""
        return 'math.Vector2'._wrap(super(WorldManifold, self).getNormal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.WorldManifold
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
from typing import List
import com.badlogic.gdx.physics.box2d.WorldManifold as _WorldManifold
_WorldManifold = _WorldManifold
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WorldManifold():
    """com.badlogic.gdx.physics.box2d.WorldManifold"""
 
    @staticmethod
    def _wrap(java_value: _WorldManifold) -> 'WorldManifold':
        return WorldManifold(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldManifold):
        """
        Dynamic initializer for WorldManifold.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldManifold__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldManifold__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getPoints(self) -> List['math.Vector2']:
        """public com.badlogic.gdx.math.Vector2[] com.badlogic.gdx.physics.box2d.WorldManifold.getPoints()"""
        return List['math.Vector2']._wrap(super(WorldManifold, self).getPoints())

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
    def getSeparations(self) -> List[float]:
        """public float[] com.badlogic.gdx.physics.box2d.WorldManifold.getSeparations()"""
        return List[float]._wrap(super(WorldManifold, self).getSeparations())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getNumberOfContactPoints(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.WorldManifold.getNumberOfContactPoints()"""
        return int._wrap(super(WorldManifold, self).getNumberOfContactPoints())

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
    def getNormal(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.WorldManifold.getNormal()"""
        return 'math.Vector2'._wrap(super(WorldManifold, self).getNormal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.WorldManifold 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.MassData
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import com.badlogic.gdx.physics.box2d.MassData as _MassData
_MassData = _MassData
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MassData():
    """com.badlogic.gdx.physics.box2d.MassData"""
 
    @staticmethod
    def _wrap(java_value: _MassData) -> 'MassData':
        return MassData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MassData):
        """
        Dynamic initializer for MassData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MassData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MassData__wrapper":
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
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.MassData()"""
        val = _MassData()
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
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.MassData()"""
        val = _MassData()
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.BodyDef$BodyType
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.physics.box2d.BodyDef as _BodyDef_BodyType
_BodyType = _BodyDef_BodyType.BodyType
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BodyType():
    """com.badlogic.gdx.physics.box2d.BodyDef.BodyType"""
 
    @staticmethod
    def _wrap(java_value: _BodyType) -> 'BodyType':
        return BodyType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BodyType):
        """
        Dynamic initializer for BodyType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BodyType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BodyType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'BodyType':
        """public static com.badlogic.gdx.physics.box2d.BodyDef$BodyType com.badlogic.gdx.physics.box2d.BodyDef$BodyType.valueOf(java.lang.String)"""
        return BodyType._wrap(_BodyType.valueOf(arg0))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @overload
    def getValue(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.BodyDef$BodyType.getValue()"""
        return int._wrap(super(BodyType, self).getValue())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @staticmethod
    @overload
    def values() -> List['BodyType']:
        """public static com.badlogic.gdx.physics.box2d.BodyDef$BodyType[] com.badlogic.gdx.physics.box2d.BodyDef$BodyType.values()"""
        return List[BodyType]._wrap(_BodyType.values())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.RayCastCallback
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.physics.box2d.RayCastCallback as _RayCastCallback
_RayCastCallback = _RayCastCallback
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from abc import abstractmethod, ABC
 
class RayCastCallback():
    """com.badlogic.gdx.physics.box2d.RayCastCallback"""
 
    @staticmethod
    def _wrap(java_value: _RayCastCallback) -> 'RayCastCallback':
        return RayCastCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RayCastCallback):
        """
        Dynamic initializer for RayCastCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RayCastCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RayCastCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def reportRayFixture(self, arg0: 'Fixture', arg1: 'Vector2', arg2: 'Vector2', arg3: float):
        """public abstract float com.badlogic.gdx.physics.box2d.RayCastCallback.reportRayFixture(com.badlogic.gdx.physics.box2d.Fixture,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,float)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.Transform
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.physics.box2d.Transform as _Transform
_Transform = _Transform
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Transform():
    """com.badlogic.gdx.physics.box2d.Transform"""
 
    @staticmethod
    def _wrap(java_value: _Transform) -> 'Transform':
        return Transform(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Transform):
        """
        Dynamic initializer for Transform.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Transform__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Transform__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.Transform()"""
        val = _Transform()
        self.__wrapper = val

    @overload
    def mul(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Transform.mul(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Transform, self).mul(arg0))

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.Transform()"""
        val = _Transform()
        self.__wrapper = val

    @overload
    def getOrientation(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Transform.getOrientation()"""
        return 'math.Vector2'._wrap(super(Transform, self).getOrientation())

    @overload
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Transform.getRotation()"""
        return float._wrap(super(Transform, self).getRotation())

    @overload
    def setOrientation(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.Transform.setOrientation(com.badlogic.gdx.math.Vector2)"""
        super(_Transform, self).setOrientation(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setRotation(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Transform.setRotation(float)"""
        super(_Transform, self).setRotation(_float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Vector2', arg1: 'Vector2'):
        """public com.badlogic.gdx.physics.box2d.Transform(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        val = _Transform(arg0, arg1)
        self.__wrapper = val

    @overload
    def getPosition(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Transform.getPosition()"""
        return 'math.Vector2'._wrap(super(Transform, self).getPosition())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setPosition(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.Transform.setPosition(com.badlogic.gdx.math.Vector2)"""
        super(_Transform, self).setPosition(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Vector2', arg1: float):
        """public com.badlogic.gdx.physics.box2d.Transform(com.badlogic.gdx.math.Vector2,float)"""
        val = _Transform(arg0, _float.valueOf(arg1))
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
 
 
# CLASS: com.badlogic.gdx.physics.box2d.Filter
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
import com.badlogic.gdx.physics.box2d.Filter as _Filter
_Filter = _Filter
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Filter():
    """com.badlogic.gdx.physics.box2d.Filter"""
 
    @staticmethod
    def _wrap(java_value: _Filter) -> 'Filter':
        return Filter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Filter):
        """
        Dynamic initializer for Filter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Filter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Filter__wrapper":
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
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.Filter()"""
        val = _Filter()
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

    @overload
    def set(self, arg0: 'Filter'):
        """public void com.badlogic.gdx.physics.box2d.Filter.set(com.badlogic.gdx.physics.box2d.Filter)"""
        super(_Filter, self).set(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.Filter()"""
        val = _Filter()
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.physics.box2d.Joint
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
import com.badlogic.gdx.physics.box2d.Joint as _Joint
_Joint = _Joint
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.physics.box2d.Body as _Body
_Body = _Body
import java.lang.Float as _float
import com.badlogic.gdx.physics.box2d.JointDef as _JointDef_JointType
_JointType = _JointDef_JointType.JointType
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Joint():
    """com.badlogic.gdx.physics.box2d.Joint"""
 
    @staticmethod
    def _wrap(java_value: _Joint) -> 'Joint':
        return Joint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Joint):
        """
        Dynamic initializer for Joint.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Joint__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Joint__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Joint.getUserData()"""
        return object._wrap(super(Joint, self).getUserData())

    @overload
    def getAnchorA(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorA()"""
        return 'math.Vector2'._wrap(super(Joint, self).getAnchorA())

    @overload
    def getCollideConnected(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.getCollideConnected()"""
        return bool._wrap(super(Joint, self).getCollideConnected())

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getBodyA(self) -> 'Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyA()"""
        return 'Body'._wrap(super(Joint, self).getBodyA())

    @overload
    def getBodyB(self) -> 'Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Joint.getBodyB()"""
        return 'Body'._wrap(super(Joint, self).getBodyB())

    @overload
    def getReactionForce(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getReactionForce(float)"""
        return 'math.Vector2'._wrap(super(_Joint, self).getReactionForce(_float.valueOf(arg0)))

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
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Joint.setUserData(java.lang.Object)"""
        super(_Joint, self).setUserData(arg0)

    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Joint.isActive()"""
        return bool._wrap(super(Joint, self).isActive())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getAnchorB(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Joint.getAnchorB()"""
        return 'math.Vector2'._wrap(super(Joint, self).getAnchorB())

    @overload
    def getReactionTorque(self, arg0: float) -> float:
        """public float com.badlogic.gdx.physics.box2d.Joint.getReactionTorque(float)"""
        return float._wrap(super(_Joint, self).getReactionTorque(_float.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getType(self) -> 'JointType':
        """public com.badlogic.gdx.physics.box2d.JointDef$JointType com.badlogic.gdx.physics.box2d.Joint.getType()"""
        return 'JointType'._wrap(super(Joint, self).getType())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.ContactImpulse
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.physics.box2d.ContactImpulse as _ContactImpulse
_ContactImpulse = _ContactImpulse
from typing import List
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ContactImpulse():
    """com.badlogic.gdx.physics.box2d.ContactImpulse"""
 
    @staticmethod
    def _wrap(java_value: _ContactImpulse) -> 'ContactImpulse':
        return ContactImpulse(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ContactImpulse):
        """
        Dynamic initializer for ContactImpulse.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ContactImpulse__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ContactImpulse__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getNormalImpulses(self) -> List[float]:
        """public float[] com.badlogic.gdx.physics.box2d.ContactImpulse.getNormalImpulses()"""
        return List[float]._wrap(super(ContactImpulse, self).getNormalImpulses())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.ContactImpulse.getCount()"""
        return int._wrap(super(ContactImpulse, self).getCount())

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
    def getTangentImpulses(self) -> List[float]:
        """public float[] com.badlogic.gdx.physics.box2d.ContactImpulse.getTangentImpulses()"""
        return List[float]._wrap(super(ContactImpulse, self).getTangentImpulses())

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
 
 
# CLASS: com.badlogic.gdx.physics.box2d.EdgeShape
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.physics.box2d.Shape as _Shape_Type
_Type = _Shape_Type.Type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.physics.box2d.EdgeShape as _EdgeShape
_EdgeShape = _EdgeShape
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import com.badlogic.gdx.physics.box2d.Shape as _Shape
_Shape = _Shape
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EdgeShape():
    """com.badlogic.gdx.physics.box2d.EdgeShape"""
 
    @staticmethod
    def _wrap(java_value: _EdgeShape) -> 'EdgeShape':
        return EdgeShape(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EdgeShape):
        """
        Dynamic initializer for EdgeShape.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EdgeShape__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EdgeShape__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.physics.box2d.EdgeShape.set(float,float,float,float)"""
        super(_EdgeShape, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def getVertex1(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.EdgeShape.getVertex1(com.badlogic.gdx.math.Vector2)"""
        super(_EdgeShape, self).getVertex1(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.Shape.getChildCount()"""
        return int._wrap(super(Shape, self).getChildCount())

    @override
    @overload
    def setRadius(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Shape.setRadius(float)"""
        super(_Shape, self).setRadius(_float.valueOf(arg0))

    @override
    @overload
    def getRadius(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Shape.getRadius()"""
        return float._wrap(super(Shape, self).getRadius())

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
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.EdgeShape()"""
        val = _EdgeShape()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.EdgeShape()"""
        val = _EdgeShape()
        self.__wrapper = val

    @overload
    def getVertex2(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.EdgeShape.getVertex2(com.badlogic.gdx.math.Vector2)"""
        super(_EdgeShape, self).getVertex2(arg0)

    @overload
    def setVertex0(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.physics.box2d.EdgeShape.setVertex0(float,float)"""
        super(_EdgeShape, self).setVertex0(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setHasVertex0(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.EdgeShape.setHasVertex0(boolean)"""
        super(_EdgeShape, self).setHasVertex0(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setVertex3(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.EdgeShape.setVertex3(com.badlogic.gdx.math.Vector2)"""
        super(_EdgeShape, self).setVertex3(arg0)

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.physics.box2d.Shape.dispose()"""
        super(Shape, self).dispose()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getVertex0(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.EdgeShape.getVertex0(com.badlogic.gdx.math.Vector2)"""
        super(_EdgeShape, self).getVertex0(arg0)

    @overload
    def getVertex3(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.EdgeShape.getVertex3(com.badlogic.gdx.math.Vector2)"""
        super(_EdgeShape, self).getVertex3(arg0)

    @overload
    def hasVertex0(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.EdgeShape.hasVertex0()"""
        return bool._wrap(super(EdgeShape, self).hasVertex0())

    @overload
    def hasVertex3(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.EdgeShape.hasVertex3()"""
        return bool._wrap(super(EdgeShape, self).hasVertex3())

    @override
    @overload
    def getType(self) -> 'Type':
        """public com.badlogic.gdx.physics.box2d.Shape$Type com.badlogic.gdx.physics.box2d.EdgeShape.getType()"""
        return 'Type'._wrap(super(EdgeShape, self).getType())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def set(self, arg0: 'Vector2', arg1: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.EdgeShape.set(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(_EdgeShape, self).set(arg0, arg1)

    @overload
    def setHasVertex3(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.EdgeShape.setHasVertex3(boolean)"""
        super(_EdgeShape, self).setHasVertex3(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setVertex3(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.physics.box2d.EdgeShape.setVertex3(float,float)"""
        super(_EdgeShape, self).setVertex3(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def setVertex0(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.EdgeShape.setVertex0(com.badlogic.gdx.math.Vector2)"""
        super(_EdgeShape, self).setVertex0(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.Manifold
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.physics.box2d.Manifold as _Manifold
_Manifold = _Manifold
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.physics.box2d.Manifold as _Manifold_ManifoldType
_ManifoldType = _Manifold_ManifoldType.ManifoldType
from typing import List
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import com.badlogic.gdx.physics.box2d.Manifold as _Manifold_ManifoldPoint
_ManifoldPoint = _Manifold_ManifoldPoint.ManifoldPoint
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Manifold():
    """com.badlogic.gdx.physics.box2d.Manifold"""
 
    @staticmethod
    def _wrap(java_value: _Manifold) -> 'Manifold':
        return Manifold(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Manifold):
        """
        Dynamic initializer for Manifold.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Manifold__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Manifold__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getType(self) -> 'ManifoldType':
        """public com.badlogic.gdx.physics.box2d.Manifold$ManifoldType com.badlogic.gdx.physics.box2d.Manifold.getType()"""
        return 'ManifoldType'._wrap(super(Manifold, self).getType())

    @overload
    def getLocalPoint(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Manifold.getLocalPoint()"""
        return 'math.Vector2'._wrap(super(Manifold, self).getLocalPoint())

    @overload
    def getPointCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.Manifold.getPointCount()"""
        return int._wrap(super(Manifold, self).getPointCount())

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getLocalNormal(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Manifold.getLocalNormal()"""
        return 'math.Vector2'._wrap(super(Manifold, self).getLocalNormal())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getPoints(self) -> List['ManifoldPoint']:
        """public com.badlogic.gdx.physics.box2d.Manifold$ManifoldPoint[] com.badlogic.gdx.physics.box2d.Manifold.getPoints()"""
        return List['ManifoldPoint']._wrap(super(Manifold, self).getPoints())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.ContactListener
from abc import abstractmethod, ABC
import com.badlogic.gdx.physics.box2d.ContactListener as _ContactListener
_ContactListener = _ContactListener
 
class ContactListener():
    """com.badlogic.gdx.physics.box2d.ContactListener"""
 
    @staticmethod
    def _wrap(java_value: _ContactListener) -> 'ContactListener':
        return ContactListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ContactListener):
        """
        Dynamic initializer for ContactListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ContactListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ContactListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.badlogic.gdx.physics.box2d.ContactFilter
import com.badlogic.gdx.physics.box2d.ContactFilter as _ContactFilter
_ContactFilter = _ContactFilter
from abc import abstractmethod, ABC
 
class ContactFilter():
    """com.badlogic.gdx.physics.box2d.ContactFilter"""
 
    @staticmethod
    def _wrap(java_value: _ContactFilter) -> 'ContactFilter':
        return ContactFilter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ContactFilter):
        """
        Dynamic initializer for ContactFilter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ContactFilter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ContactFilter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def shouldCollide(self, arg0: 'Fixture', arg1: 'Fixture'):
        """public abstract boolean com.badlogic.gdx.physics.box2d.ContactFilter.shouldCollide(com.badlogic.gdx.physics.box2d.Fixture,com.badlogic.gdx.physics.box2d.Fixture)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.DestructionListener
import com.badlogic.gdx.physics.box2d.DestructionListener as _DestructionListener
_DestructionListener = _DestructionListener
 
class DestructionListener():
    """com.badlogic.gdx.physics.box2d.DestructionListener"""
 
    @staticmethod
    def _wrap(java_value: _DestructionListener) -> 'DestructionListener':
        return DestructionListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DestructionListener):
        """
        Dynamic initializer for DestructionListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DestructionListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DestructionListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__)) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.Box2D
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.physics.box2d.Box2D as _Box2D
_Box2D = _Box2D
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Box2D():
    """com.badlogic.gdx.physics.box2d.Box2D"""
 
    @staticmethod
    def _wrap(java_value: _Box2D) -> 'Box2D':
        return Box2D(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Box2D):
        """
        Dynamic initializer for Box2D.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Box2D__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Box2D__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
        @staticmethod
        @overload
        def init():
            """public static void com.badlogic.gdx.physics.box2d.Box2D.init()"""
            _Box2D.init()

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
 
 
# CLASS: com.badlogic.gdx.physics.box2d.JointEdge
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.physics.box2d.JointEdge as _JointEdge
_JointEdge = _JointEdge
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JointEdge():
    """com.badlogic.gdx.physics.box2d.JointEdge"""
 
    @staticmethod
    def _wrap(java_value: _JointEdge) -> 'JointEdge':
        return JointEdge(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JointEdge):
        """
        Dynamic initializer for JointEdge.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JointEdge__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JointEdge__wrapper":
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
 
 
# CLASS: com.badlogic.gdx.physics.box2d.CircleShape
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.physics.box2d.CircleShape as _CircleShape
_CircleShape = _CircleShape
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.physics.box2d.Shape as _Shape_Type
_Type = _Shape_Type.Type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.physics.box2d.Shape as _Shape
_Shape = _Shape
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CircleShape():
    """com.badlogic.gdx.physics.box2d.CircleShape"""
 
    @staticmethod
    def _wrap(java_value: _CircleShape) -> 'CircleShape':
        return CircleShape(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CircleShape):
        """
        Dynamic initializer for CircleShape.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CircleShape__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CircleShape__wrapper":
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
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.CircleShape()"""
        val = _CircleShape()
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.physics.box2d.Shape.dispose()"""
        super(Shape, self).dispose()

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.Shape.getChildCount()"""
        return int._wrap(super(Shape, self).getChildCount())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def setRadius(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Shape.setRadius(float)"""
        super(_Shape, self).setRadius(_float.valueOf(arg0))

    @overload
    def getPosition(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.CircleShape.getPosition()"""
        return 'math.Vector2'._wrap(super(CircleShape, self).getPosition())

    @override
    @overload
    def getRadius(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Shape.getRadius()"""
        return float._wrap(super(Shape, self).getRadius())

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
    def getType(self) -> 'Type':
        """public com.badlogic.gdx.physics.box2d.Shape$Type com.badlogic.gdx.physics.box2d.CircleShape.getType()"""
        return 'Type'._wrap(super(CircleShape, self).getType())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setPosition(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.CircleShape.setPosition(com.badlogic.gdx.math.Vector2)"""
        super(_CircleShape, self).setPosition(arg0)

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
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.CircleShape()"""
        val = _CircleShape()
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.BodyDef
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.physics.box2d.BodyDef as _BodyDef
_BodyDef = _BodyDef
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BodyDef():
    """com.badlogic.gdx.physics.box2d.BodyDef"""
 
    @staticmethod
    def _wrap(java_value: _BodyDef) -> 'BodyDef':
        return BodyDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BodyDef):
        """
        Dynamic initializer for BodyDef.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BodyDef__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BodyDef__wrapper":
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
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.BodyDef()"""
        val = _BodyDef()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.BodyDef()"""
        val = _BodyDef()
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.physics.box2d.QueryCallback
import com.badlogic.gdx.physics.box2d.QueryCallback as _QueryCallback
_QueryCallback = _QueryCallback
from abc import abstractmethod, ABC
 
class QueryCallback():
    """com.badlogic.gdx.physics.box2d.QueryCallback"""
 
    @staticmethod
    def _wrap(java_value: _QueryCallback) -> 'QueryCallback':
        return QueryCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _QueryCallback):
        """
        Dynamic initializer for QueryCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_QueryCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_QueryCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def reportFixture(self, arg0: 'Fixture'):
        """public abstract boolean com.badlogic.gdx.physics.box2d.QueryCallback.reportFixture(com.badlogic.gdx.physics.box2d.Fixture)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.FixtureDef
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.physics.box2d.FixtureDef as _FixtureDef
_FixtureDef = _FixtureDef
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FixtureDef():
    """com.badlogic.gdx.physics.box2d.FixtureDef"""
 
    @staticmethod
    def _wrap(java_value: _FixtureDef) -> 'FixtureDef':
        return FixtureDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FixtureDef):
        """
        Dynamic initializer for FixtureDef.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FixtureDef__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FixtureDef__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.FixtureDef()"""
        val = _FixtureDef()
        self.__wrapper = val

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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.FixtureDef()"""
        val = _FixtureDef()
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.physics.box2d.World
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
import com.badlogic.gdx.physics.box2d.Joint as _Joint
_Joint = _Joint
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
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.physics.box2d.Body as _Body
_Body = _Body
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.physics.box2d.World as _World
_World = _World
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class World():
    """com.badlogic.gdx.physics.box2d.World"""
 
    @staticmethod
    def _wrap(java_value: _World) -> 'World':
        return World(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _World):
        """
        Dynamic initializer for World.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_World__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_World__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getBodyCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.World.getBodyCount()"""
        return int._wrap(super(World, self).getBodyCount())

    @overload
    def setWarmStarting(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.World.setWarmStarting(boolean)"""
        super(_World, self).setWarmStarting(_boolean.valueOf(arg0))

    @overload
    def getAutoClearForces(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.World.getAutoClearForces()"""
        return bool._wrap(super(World, self).getAutoClearForces())

    @overload
    def getFixtures(self, arg0: 'Array'):
        """public void com.badlogic.gdx.physics.box2d.World.getFixtures(com.badlogic.gdx.utils.Array<com.badlogic.gdx.physics.box2d.Fixture>)"""
        super(_World, self).getFixtures(arg0)

    @overload
    def getBodies(self, arg0: 'Array'):
        """public void com.badlogic.gdx.physics.box2d.World.getBodies(com.badlogic.gdx.utils.Array<com.badlogic.gdx.physics.box2d.Body>)"""
        super(_World, self).getBodies(arg0)

    @overload
    def getGravity(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.World.getGravity()"""
        return 'math.Vector2'._wrap(super(World, self).getGravity())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setGravity(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.World.setGravity(com.badlogic.gdx.math.Vector2)"""
        super(_World, self).setGravity(arg0)

    @overload
    def __init__(self, arg0: 'Vector2', arg1: bool):
        """public com.badlogic.gdx.physics.box2d.World(com.badlogic.gdx.math.Vector2,boolean)"""
        val = _World(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

    @overload
    def isLocked(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.World.isLocked()"""
        return bool._wrap(super(World, self).isLocked())

    @overload
    def setAutoClearForces(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.World.setAutoClearForces(boolean)"""
        super(_World, self).setAutoClearForces(_boolean.valueOf(arg0))

    @overload
    def clearForces(self):
        """public void com.badlogic.gdx.physics.box2d.World.clearForces()"""
        super(World, self).clearForces()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def createJoint(self, arg0: 'JointDef') -> 'Joint':
        """public com.badlogic.gdx.physics.box2d.Joint com.badlogic.gdx.physics.box2d.World.createJoint(com.badlogic.gdx.physics.box2d.JointDef)"""
        return 'Joint'._wrap(super(_World, self).createJoint(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def destroyJoint(self, arg0: 'Joint'):
        """public void com.badlogic.gdx.physics.box2d.World.destroyJoint(com.badlogic.gdx.physics.box2d.Joint)"""
        super(_World, self).destroyJoint(arg0)

    @staticmethod
    @overload
    def getVelocityThreshold() -> float:
        """public static native float com.badlogic.gdx.physics.box2d.World.getVelocityThreshold()"""
        return float._wrap(_World.getVelocityThreshold())

    @overload
    def createBody(self, arg0: 'BodyDef') -> 'Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.World.createBody(com.badlogic.gdx.physics.box2d.BodyDef)"""
        return 'Body'._wrap(super(_World, self).createBody(arg0))

    @overload
    def setDestructionListener(self, arg0: 'DestructionListener'):
        """public void com.badlogic.gdx.physics.box2d.World.setDestructionListener(com.badlogic.gdx.physics.box2d.DestructionListener)"""
        super(_World, self).setDestructionListener(arg0)

    @overload
    def getFixtureCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.World.getFixtureCount()"""
        return int._wrap(super(World, self).getFixtureCount())

    @overload
    def getContactList(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.physics.box2d.Contact> com.badlogic.gdx.physics.box2d.World.getContactList()"""
        return 'utils.Array'._wrap(super(World, self).getContactList())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.physics.box2d.World.dispose()"""
        super(World, self).dispose()

    @overload
    def setContactListener(self, arg0: 'ContactListener'):
        """public void com.badlogic.gdx.physics.box2d.World.setContactListener(com.badlogic.gdx.physics.box2d.ContactListener)"""
        super(_World, self).setContactListener(arg0)

    @overload
    def destroyBody(self, arg0: 'Body'):
        """public void com.badlogic.gdx.physics.box2d.World.destroyBody(com.badlogic.gdx.physics.box2d.Body)"""
        super(_World, self).destroyBody(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def setVelocityThreshold(arg0: float):
        """public static native void com.badlogic.gdx.physics.box2d.World.setVelocityThreshold(float)"""
        _World.setVelocityThreshold(_float.valueOf(arg0))

    @overload
    def getProxyCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.World.getProxyCount()"""
        return int._wrap(super(World, self).getProxyCount())

    @overload
    def rayCast(self, arg0: 'RayCastCallback', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.physics.box2d.World.rayCast(com.badlogic.gdx.physics.box2d.RayCastCallback,float,float,float,float)"""
        super(_World, self).rayCast(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getJointCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.World.getJointCount()"""
        return int._wrap(super(World, self).getJointCount())

    @overload
    def step(self, arg0: float, arg1: int, arg2: int):
        """public void com.badlogic.gdx.physics.box2d.World.step(float,int,int)"""
        super(_World, self).step(_float.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def setContinuousPhysics(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.World.setContinuousPhysics(boolean)"""
        super(_World, self).setContinuousPhysics(_boolean.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setContactFilter(self, arg0: 'ContactFilter'):
        """public void com.badlogic.gdx.physics.box2d.World.setContactFilter(com.badlogic.gdx.physics.box2d.ContactFilter)"""
        super(_World, self).setContactFilter(arg0)

    @overload
    def getContactCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.World.getContactCount()"""
        return int._wrap(super(World, self).getContactCount())

    @overload
    def getJoints(self, arg0: 'Array'):
        """public void com.badlogic.gdx.physics.box2d.World.getJoints(com.badlogic.gdx.utils.Array<com.badlogic.gdx.physics.box2d.Joint>)"""
        super(_World, self).getJoints(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def rayCast(self, arg0: 'RayCastCallback', arg1: 'Vector2', arg2: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.World.rayCast(com.badlogic.gdx.physics.box2d.RayCastCallback,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(_World, self).rayCast(arg0, arg1, arg2)

    @overload
    def QueryAABB(self, arg0: 'QueryCallback', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.physics.box2d.World.QueryAABB(com.badlogic.gdx.physics.box2d.QueryCallback,float,float,float,float)"""
        super(_World, self).QueryAABB(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.Body
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.physics.box2d.BodyDef as _BodyDef_BodyType
_BodyType = _BodyDef_BodyType.BodyType
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.physics.box2d.Transform as _Transform
_Transform = _Transform
import com.badlogic.gdx.physics.box2d.Body as _Body
_Body = _Body
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import java.lang.Boolean as _boolean
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.physics.box2d.MassData as _MassData
_MassData = _MassData
import com.badlogic.gdx.physics.box2d.Fixture as _Fixture
_Fixture = _Fixture
import com.badlogic.gdx.physics.box2d.World as _World
_World = _World
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Body():
    """com.badlogic.gdx.physics.box2d.Body"""
 
    @staticmethod
    def _wrap(java_value: _Body) -> 'Body':
        return Body(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Body):
        """
        Dynamic initializer for Body.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Body__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Body__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Body.setUserData(java.lang.Object)"""
        super(_Body, self).setUserData(arg0)

    @overload
    def applyForce(self, arg0: 'Vector2', arg1: 'Vector2', arg2: bool):
        """public void com.badlogic.gdx.physics.box2d.Body.applyForce(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,boolean)"""
        super(_Body, self).applyForce(arg0, arg1, _boolean.valueOf(arg2))

    @overload
    def getWorldVector(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Body.getWorldVector(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Body, self).getWorldVector(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getInertia(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Body.getInertia()"""
        return float._wrap(super(Body, self).getInertia())

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
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.Body.setActive(boolean)"""
        super(_Body, self).setActive(_boolean.valueOf(arg0))

    @overload
    def getLocalVector(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Body.getLocalVector(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Body, self).getLocalVector(arg0))

    @overload
    def setLinearVelocity(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.Body.setLinearVelocity(com.badlogic.gdx.math.Vector2)"""
        super(_Body, self).setLinearVelocity(arg0)

    @overload
    def resetMassData(self):
        """public void com.badlogic.gdx.physics.box2d.Body.resetMassData()"""
        super(Body, self).resetMassData()

    @overload
    def createFixture(self, arg0: 'Shape', arg1: float) -> 'Fixture':
        """public com.badlogic.gdx.physics.box2d.Fixture com.badlogic.gdx.physics.box2d.Body.createFixture(com.badlogic.gdx.physics.box2d.Shape,float)"""
        return 'Fixture'._wrap(super(_Body, self).createFixture(arg0, _float.valueOf(arg1)))

    @overload
    def setLinearDamping(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Body.setLinearDamping(float)"""
        super(_Body, self).setLinearDamping(_float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getLinearVelocityFromLocalPoint(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Body.getLinearVelocityFromLocalPoint(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Body, self).getLinearVelocityFromLocalPoint(arg0))

    @overload
    def setSleepingAllowed(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.Body.setSleepingAllowed(boolean)"""
        super(_Body, self).setSleepingAllowed(_boolean.valueOf(arg0))

    @overload
    def isAwake(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Body.isAwake()"""
        return bool._wrap(super(Body, self).isAwake())

    @overload
    def setTransform(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.physics.box2d.Body.setTransform(float,float,float)"""
        super(_Body, self).setTransform(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def getLocalCenter(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Body.getLocalCenter()"""
        return 'math.Vector2'._wrap(super(Body, self).getLocalCenter())

    @overload
    def applyLinearImpulse(self, arg0: 'Vector2', arg1: 'Vector2', arg2: bool):
        """public void com.badlogic.gdx.physics.box2d.Body.applyLinearImpulse(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,boolean)"""
        super(_Body, self).applyLinearImpulse(arg0, arg1, _boolean.valueOf(arg2))

    @overload
    def getMass(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Body.getMass()"""
        return float._wrap(super(Body, self).getMass())

    @overload
    def setAngularDamping(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Body.setAngularDamping(float)"""
        super(_Body, self).setAngularDamping(_float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def applyForceToCenter(self, arg0: float, arg1: float, arg2: bool):
        """public void com.badlogic.gdx.physics.box2d.Body.applyForceToCenter(float,float,boolean)"""
        super(_Body, self).applyForceToCenter(_float.valueOf(arg0), _float.valueOf(arg1), _boolean.valueOf(arg2))

    @overload
    def applyAngularImpulse(self, arg0: float, arg1: bool):
        """public void com.badlogic.gdx.physics.box2d.Body.applyAngularImpulse(float,boolean)"""
        super(_Body, self).applyAngularImpulse(_float.valueOf(arg0), _boolean.valueOf(arg1))

    @overload
    def destroyFixture(self, arg0: 'Fixture'):
        """public void com.badlogic.gdx.physics.box2d.Body.destroyFixture(com.badlogic.gdx.physics.box2d.Fixture)"""
        super(_Body, self).destroyFixture(arg0)

    @overload
    def getGravityScale(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Body.getGravityScale()"""
        return float._wrap(super(Body, self).getGravityScale())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getJointList(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.physics.box2d.JointEdge> com.badlogic.gdx.physics.box2d.Body.getJointList()"""
        return 'utils.Array'._wrap(super(Body, self).getJointList())

    @overload
    def getWorld(self) -> 'World':
        """public com.badlogic.gdx.physics.box2d.World com.badlogic.gdx.physics.box2d.Body.getWorld()"""
        return 'World'._wrap(super(Body, self).getWorld())

    @overload
    def getAngle(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Body.getAngle()"""
        return float._wrap(super(Body, self).getAngle())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Body.getUserData()"""
        return object._wrap(super(Body, self).getUserData())

    @overload
    def setFixedRotation(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.Body.setFixedRotation(boolean)"""
        super(_Body, self).setFixedRotation(_boolean.valueOf(arg0))

    @overload
    def setBullet(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.Body.setBullet(boolean)"""
        super(_Body, self).setBullet(_boolean.valueOf(arg0))

    @overload
    def setGravityScale(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Body.setGravityScale(float)"""
        super(_Body, self).setGravityScale(_float.valueOf(arg0))

    @overload
    def setAngularVelocity(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Body.setAngularVelocity(float)"""
        super(_Body, self).setAngularVelocity(_float.valueOf(arg0))

    @overload
    def setMassData(self, arg0: 'MassData'):
        """public void com.badlogic.gdx.physics.box2d.Body.setMassData(com.badlogic.gdx.physics.box2d.MassData)"""
        super(_Body, self).setMassData(arg0)

    @overload
    def getFixtureList(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.physics.box2d.Fixture> com.badlogic.gdx.physics.box2d.Body.getFixtureList()"""
        return 'utils.Array'._wrap(super(Body, self).getFixtureList())

    @overload
    def getPosition(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Body.getPosition()"""
        return 'math.Vector2'._wrap(super(Body, self).getPosition())

    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Body.isActive()"""
        return bool._wrap(super(Body, self).isActive())

    @overload
    def setAwake(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.Body.setAwake(boolean)"""
        super(_Body, self).setAwake(_boolean.valueOf(arg0))

    @overload
    def getMassData(self) -> 'MassData':
        """public com.badlogic.gdx.physics.box2d.MassData com.badlogic.gdx.physics.box2d.Body.getMassData()"""
        return 'MassData'._wrap(super(Body, self).getMassData())

    @overload
    def applyLinearImpulse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: bool):
        """public void com.badlogic.gdx.physics.box2d.Body.applyLinearImpulse(float,float,float,float,boolean)"""
        super(_Body, self).applyLinearImpulse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _boolean.valueOf(arg4))

    @overload
    def applyForce(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: bool):
        """public void com.badlogic.gdx.physics.box2d.Body.applyForce(float,float,float,float,boolean)"""
        super(_Body, self).applyForce(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _boolean.valueOf(arg4))

    @overload
    def getTransform(self) -> 'Transform':
        """public com.badlogic.gdx.physics.box2d.Transform com.badlogic.gdx.physics.box2d.Body.getTransform()"""
        return 'Transform'._wrap(super(Body, self).getTransform())

    @overload
    def getLocalPoint(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Body.getLocalPoint(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Body, self).getLocalPoint(arg0))

    @overload
    def getWorldCenter(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Body.getWorldCenter()"""
        return 'math.Vector2'._wrap(super(Body, self).getWorldCenter())

    @overload
    def getType(self) -> 'BodyType':
        """public com.badlogic.gdx.physics.box2d.BodyDef$BodyType com.badlogic.gdx.physics.box2d.Body.getType()"""
        return 'BodyType'._wrap(super(Body, self).getType())

    @overload
    def setLinearVelocity(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.physics.box2d.Body.setLinearVelocity(float,float)"""
        super(_Body, self).setLinearVelocity(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def isBullet(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Body.isBullet()"""
        return bool._wrap(super(Body, self).isBullet())

    @overload
    def getAngularVelocity(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Body.getAngularVelocity()"""
        return float._wrap(super(Body, self).getAngularVelocity())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def isFixedRotation(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Body.isFixedRotation()"""
        return bool._wrap(super(Body, self).isFixedRotation())

    @overload
    def setTransform(self, arg0: 'Vector2', arg1: float):
        """public void com.badlogic.gdx.physics.box2d.Body.setTransform(com.badlogic.gdx.math.Vector2,float)"""
        super(_Body, self).setTransform(arg0, _float.valueOf(arg1))

    @overload
    def getAngularDamping(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Body.getAngularDamping()"""
        return float._wrap(super(Body, self).getAngularDamping())

    @overload
    def createFixture(self, arg0: 'FixtureDef') -> 'Fixture':
        """public com.badlogic.gdx.physics.box2d.Fixture com.badlogic.gdx.physics.box2d.Body.createFixture(com.badlogic.gdx.physics.box2d.FixtureDef)"""
        return 'Fixture'._wrap(super(_Body, self).createFixture(arg0))

    @overload
    def getLinearDamping(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Body.getLinearDamping()"""
        return float._wrap(super(Body, self).getLinearDamping())

    @overload
    def getLinearVelocityFromWorldPoint(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Body.getLinearVelocityFromWorldPoint(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Body, self).getLinearVelocityFromWorldPoint(arg0))

    @overload
    def applyTorque(self, arg0: float, arg1: bool):
        """public void com.badlogic.gdx.physics.box2d.Body.applyTorque(float,boolean)"""
        super(_Body, self).applyTorque(_float.valueOf(arg0), _boolean.valueOf(arg1))

    @overload
    def getWorldPoint(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Body.getWorldPoint(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Body, self).getWorldPoint(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setType(self, arg0: 'BodyType'):
        """public void com.badlogic.gdx.physics.box2d.Body.setType(com.badlogic.gdx.physics.box2d.BodyDef$BodyType)"""
        super(_Body, self).setType(arg0)

    @overload
    def getLinearVelocity(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Body.getLinearVelocity()"""
        return 'math.Vector2'._wrap(super(Body, self).getLinearVelocity())

    @overload
    def isSleepingAllowed(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Body.isSleepingAllowed()"""
        return bool._wrap(super(Body, self).isSleepingAllowed())

    @overload
    def applyForceToCenter(self, arg0: 'Vector2', arg1: bool):
        """public void com.badlogic.gdx.physics.box2d.Body.applyForceToCenter(com.badlogic.gdx.math.Vector2,boolean)"""
        super(_Body, self).applyForceToCenter(arg0, _boolean.valueOf(arg1)) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.Shape
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.physics.box2d.Shape as _Shape
_Shape = _Shape
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Shape():
    """com.badlogic.gdx.physics.box2d.Shape"""
 
    @staticmethod
    def _wrap(java_value: _Shape) -> 'Shape':
        return Shape(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Shape):
        """
        Dynamic initializer for Shape.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Shape__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Shape__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.Shape()"""
        val = _Shape()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @abstractmethod
    def getType(self, ):
        """public abstract com.badlogic.gdx.physics.box2d.Shape$Type com.badlogic.gdx.physics.box2d.Shape.getType()"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.Shape.getChildCount()"""
        return int._wrap(super(Shape, self).getChildCount())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.Shape()"""
        val = _Shape()
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.physics.box2d.Shape.dispose()"""
        super(Shape, self).dispose()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

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
    def getRadius(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Shape.getRadius()"""
        return float._wrap(super(Shape, self).getRadius())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setRadius(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Shape.setRadius(float)"""
        super(_Shape, self).setRadius(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.Contact
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import com.badlogic.gdx.physics.box2d.WorldManifold as _WorldManifold
_WorldManifold = _WorldManifold
import java.lang.Integer as _int
import com.badlogic.gdx.physics.box2d.Contact as _Contact
_Contact = _Contact
import com.badlogic.gdx.physics.box2d.Fixture as _Fixture
_Fixture = _Fixture
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Contact():
    """com.badlogic.gdx.physics.box2d.Contact"""
 
    @staticmethod
    def _wrap(java_value: _Contact) -> 'Contact':
        return Contact(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Contact):
        """
        Dynamic initializer for Contact.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Contact__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Contact__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def ResetRestitution(self):
        """public void com.badlogic.gdx.physics.box2d.Contact.ResetRestitution()"""
        super(Contact, self).ResetRestitution()

    @overload
    def getWorldManifold(self) -> 'WorldManifold':
        """public com.badlogic.gdx.physics.box2d.WorldManifold com.badlogic.gdx.physics.box2d.Contact.getWorldManifold()"""
        return 'WorldManifold'._wrap(super(Contact, self).getWorldManifold())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Contact.isEnabled()"""
        return bool._wrap(super(Contact, self).isEnabled())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getChildIndexA(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.Contact.getChildIndexA()"""
        return int._wrap(super(Contact, self).getChildIndexA())

    @overload
    def setTangentSpeed(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Contact.setTangentSpeed(float)"""
        super(_Contact, self).setTangentSpeed(_float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getTangentSpeed(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Contact.getTangentSpeed()"""
        return float._wrap(super(Contact, self).getTangentSpeed())

    @overload
    def getChildIndexB(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.Contact.getChildIndexB()"""
        return int._wrap(super(Contact, self).getChildIndexB())

    @overload
    def setFriction(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Contact.setFriction(float)"""
        super(_Contact, self).setFriction(_float.valueOf(arg0))

    @overload
    def setRestitution(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Contact.setRestitution(float)"""
        super(_Contact, self).setRestitution(_float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def isTouching(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Contact.isTouching()"""
        return bool._wrap(super(Contact, self).isTouching())

    @overload
    def getRestitution(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Contact.getRestitution()"""
        return float._wrap(super(Contact, self).getRestitution())

    @overload
    def getFriction(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Contact.getFriction()"""
        return float._wrap(super(Contact, self).getFriction())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getFixtureB(self) -> 'Fixture':
        """public com.badlogic.gdx.physics.box2d.Fixture com.badlogic.gdx.physics.box2d.Contact.getFixtureB()"""
        return 'Fixture'._wrap(super(Contact, self).getFixtureB())

    @overload
    def getFixtureA(self) -> 'Fixture':
        """public com.badlogic.gdx.physics.box2d.Fixture com.badlogic.gdx.physics.box2d.Contact.getFixtureA()"""
        return 'Fixture'._wrap(super(Contact, self).getFixtureA())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setEnabled(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.Contact.setEnabled(boolean)"""
        super(_Contact, self).setEnabled(_boolean.valueOf(arg0))

    @overload
    def resetFriction(self):
        """public void com.badlogic.gdx.physics.box2d.Contact.resetFriction()"""
        super(Contact, self).resetFriction()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.Fixture
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.physics.box2d.Shape as _Shape_Type
_Type = _Shape_Type.Type
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.physics.box2d.Body as _Body
_Body = _Body
import com.badlogic.gdx.physics.box2d.Filter as _Filter
_Filter = _Filter
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.physics.box2d.Fixture as _Fixture
_Fixture = _Fixture
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.physics.box2d.Shape as _Shape
_Shape = _Shape
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Fixture():
    """com.badlogic.gdx.physics.box2d.Fixture"""
 
    @staticmethod
    def _wrap(java_value: _Fixture) -> 'Fixture':
        return Fixture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Fixture):
        """
        Dynamic initializer for Fixture.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Fixture__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Fixture__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setFilterData(self, arg0: 'Filter'):
        """public void com.badlogic.gdx.physics.box2d.Fixture.setFilterData(com.badlogic.gdx.physics.box2d.Filter)"""
        super(_Fixture, self).setFilterData(arg0)

    @overload
    def getType(self) -> 'Type':
        """public com.badlogic.gdx.physics.box2d.Shape$Type com.badlogic.gdx.physics.box2d.Fixture.getType()"""
        return 'Type'._wrap(super(Fixture, self).getType())

    @overload
    def getDensity(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Fixture.getDensity()"""
        return float._wrap(super(Fixture, self).getDensity())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setDensity(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Fixture.setDensity(float)"""
        super(_Fixture, self).setDensity(_float.valueOf(arg0))

    @overload
    def testPoint(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Fixture.testPoint(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_Fixture, self).testPoint(arg0))

    @overload
    def isSensor(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Fixture.isSensor()"""
        return bool._wrap(super(Fixture, self).isSensor())

    @overload
    def setFriction(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Fixture.setFriction(float)"""
        super(_Fixture, self).setFriction(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getUserData(self) -> object:
        """public java.lang.Object com.badlogic.gdx.physics.box2d.Fixture.getUserData()"""
        return object._wrap(super(Fixture, self).getUserData())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setUserData(self, arg0: object):
        """public void com.badlogic.gdx.physics.box2d.Fixture.setUserData(java.lang.Object)"""
        super(_Fixture, self).setUserData(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getFilterData(self) -> 'Filter':
        """public com.badlogic.gdx.physics.box2d.Filter com.badlogic.gdx.physics.box2d.Fixture.getFilterData()"""
        return 'Filter'._wrap(super(Fixture, self).getFilterData())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setSensor(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.Fixture.setSensor(boolean)"""
        super(_Fixture, self).setSensor(_boolean.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def testPoint(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Fixture.testPoint(float,float)"""
        return bool._wrap(super(_Fixture, self).testPoint(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def getFriction(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Fixture.getFriction()"""
        return float._wrap(super(Fixture, self).getFriction())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def refilter(self):
        """public void com.badlogic.gdx.physics.box2d.Fixture.refilter()"""
        super(Fixture, self).refilter()

    @overload
    def setRestitution(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Fixture.setRestitution(float)"""
        super(_Fixture, self).setRestitution(_float.valueOf(arg0))

    @overload
    def getShape(self) -> 'Shape':
        """public com.badlogic.gdx.physics.box2d.Shape com.badlogic.gdx.physics.box2d.Fixture.getShape()"""
        return 'Shape'._wrap(super(Fixture, self).getShape())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getBody(self) -> 'Body':
        """public com.badlogic.gdx.physics.box2d.Body com.badlogic.gdx.physics.box2d.Fixture.getBody()"""
        return 'Body'._wrap(super(Fixture, self).getBody())

    @overload
    def getRestitution(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Fixture.getRestitution()"""
        return float._wrap(super(Fixture, self).getRestitution())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.JointDef
from builtins import str
import com.badlogic.gdx.physics.box2d.JointDef as _JointDef
_JointDef = _JointDef
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
 
class JointDef():
    """com.badlogic.gdx.physics.box2d.JointDef"""
 
    @staticmethod
    def _wrap(java_value: _JointDef) -> 'JointDef':
        return JointDef(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JointDef):
        """
        Dynamic initializer for JointDef.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JointDef__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JointDef__wrapper":
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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.JointDef()"""
        val = _JointDef()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.JointDef()"""
        val = _JointDef()
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.physics.box2d.Manifold$ManifoldType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.physics.box2d.Manifold as _Manifold_ManifoldType
_ManifoldType = _Manifold_ManifoldType.ManifoldType
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ManifoldType():
    """com.badlogic.gdx.physics.box2d.Manifold.ManifoldType"""
 
    @staticmethod
    def _wrap(java_value: _ManifoldType) -> 'ManifoldType':
        return ManifoldType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ManifoldType):
        """
        Dynamic initializer for ManifoldType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ManifoldType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ManifoldType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ManifoldType':
        """public static com.badlogic.gdx.physics.box2d.Manifold$ManifoldType com.badlogic.gdx.physics.box2d.Manifold$ManifoldType.valueOf(java.lang.String)"""
        return ManifoldType._wrap(_ManifoldType.valueOf(arg0))

    @staticmethod
    @overload
    def values() -> List['ManifoldType']:
        """public static com.badlogic.gdx.physics.box2d.Manifold$ManifoldType[] com.badlogic.gdx.physics.box2d.Manifold$ManifoldType.values()"""
        return List[ManifoldType]._wrap(_ManifoldType.values())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.Shape$Type
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.physics.box2d.Shape as _Shape_Type
_Type = _Shape_Type.Type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Type():
    """com.badlogic.gdx.physics.box2d.Shape.Type"""
 
    @staticmethod
    def _wrap(java_value: _Type) -> 'Type':
        return Type(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Type):
        """
        Dynamic initializer for Type.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Type__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Type__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Type':
        """public static com.badlogic.gdx.physics.box2d.Shape$Type com.badlogic.gdx.physics.box2d.Shape$Type.valueOf(java.lang.String)"""
        return Type._wrap(_Type.valueOf(arg0))

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def values() -> List['Type']:
        """public static com.badlogic.gdx.physics.box2d.Shape$Type[] com.badlogic.gdx.physics.box2d.Shape$Type.values()"""
        return List[Type]._wrap(_Type.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.ChainShape
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.physics.box2d.ChainShape as _ChainShape
_ChainShape = _ChainShape
import com.badlogic.gdx.physics.box2d.Shape as _Shape_Type
_Type = _Shape_Type.Type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import com.badlogic.gdx.physics.box2d.Shape as _Shape
_Shape = _Shape
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ChainShape():
    """com.badlogic.gdx.physics.box2d.ChainShape"""
 
    @staticmethod
    def _wrap(java_value: _ChainShape) -> 'ChainShape':
        return ChainShape(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ChainShape):
        """
        Dynamic initializer for ChainShape.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ChainShape__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ChainShape__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def isLooped(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.ChainShape.isLooped()"""
        return bool._wrap(super(ChainShape, self).isLooped())

    @overload
    def setPrevVertex(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.ChainShape.setPrevVertex(com.badlogic.gdx.math.Vector2)"""
        super(_ChainShape, self).setPrevVertex(arg0)

    @overload
    def createLoop(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.ChainShape.createLoop(com.badlogic.gdx.math.Vector2[])"""
        super(_ChainShape, self).createLoop(arg0)

    @overload
    def createChain(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.ChainShape.createChain(com.badlogic.gdx.math.Vector2[])"""
        super(_ChainShape, self).createChain(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.Shape.getChildCount()"""
        return int._wrap(super(Shape, self).getChildCount())

    @override
    @overload
    def setRadius(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Shape.setRadius(float)"""
        super(_Shape, self).setRadius(_float.valueOf(arg0))

    @override
    @overload
    def getRadius(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Shape.getRadius()"""
        return float._wrap(super(Shape, self).getRadius())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.physics.box2d.ChainShape.clear()"""
        super(ChainShape, self).clear()

    @overload
    def createChain(self, arg0: 'float', arg1: int, arg2: int):
        """public void com.badlogic.gdx.physics.box2d.ChainShape.createChain(float[],int,int)"""
        super(_ChainShape, self).createChain(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def createChain(self, arg0: 'float'):
        """public void com.badlogic.gdx.physics.box2d.ChainShape.createChain(float[])"""
        super(_ChainShape, self).createChain(arg0)

    @overload
    def setPrevVertex(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.physics.box2d.ChainShape.setPrevVertex(float,float)"""
        super(_ChainShape, self).setPrevVertex(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def getType(self) -> 'Type':
        """public com.badlogic.gdx.physics.box2d.Shape$Type com.badlogic.gdx.physics.box2d.ChainShape.getType()"""
        return 'Type'._wrap(super(ChainShape, self).getType())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.ChainShape()"""
        val = _ChainShape()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def createLoop(self, arg0: 'float', arg1: int, arg2: int):
        """public void com.badlogic.gdx.physics.box2d.ChainShape.createLoop(float[],int,int)"""
        super(_ChainShape, self).createLoop(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def setNextVertex(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.physics.box2d.ChainShape.setNextVertex(float,float)"""
        super(_ChainShape, self).setNextVertex(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def createLoop(self, arg0: 'float'):
        """public void com.badlogic.gdx.physics.box2d.ChainShape.createLoop(float[])"""
        super(_ChainShape, self).createLoop(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.physics.box2d.Shape.dispose()"""
        super(Shape, self).dispose()

    @overload
    def getVertexCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.ChainShape.getVertexCount()"""
        return int._wrap(super(ChainShape, self).getVertexCount())

    @overload
    def getVertex(self, arg0: int, arg1: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.ChainShape.getVertex(int,com.badlogic.gdx.math.Vector2)"""
        super(_ChainShape, self).getVertex(_int.valueOf(arg0), arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setNextVertex(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.ChainShape.setNextVertex(com.badlogic.gdx.math.Vector2)"""
        super(_ChainShape, self).setNextVertex(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.ChainShape()"""
        val = _ChainShape()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.PolygonShape
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.physics.box2d.Shape as _Shape_Type
_Type = _Shape_Type.Type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.physics.box2d.PolygonShape as _PolygonShape
_PolygonShape = _PolygonShape
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.physics.box2d.Shape as _Shape
_Shape = _Shape
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PolygonShape():
    """com.badlogic.gdx.physics.box2d.PolygonShape"""
 
    @staticmethod
    def _wrap(java_value: _PolygonShape) -> 'PolygonShape':
        return PolygonShape(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PolygonShape):
        """
        Dynamic initializer for PolygonShape.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PolygonShape__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PolygonShape__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.PolygonShape()"""
        val = _PolygonShape()
        self.__wrapper = val

    @overload
    def set(self, arg0: 'float'):
        """public void com.badlogic.gdx.physics.box2d.PolygonShape.set(float[])"""
        super(_PolygonShape, self).set(arg0)

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
    def setAsBox(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.physics.box2d.PolygonShape.setAsBox(float,float)"""
        super(_PolygonShape, self).setAsBox(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.physics.box2d.Shape.dispose()"""
        super(Shape, self).dispose()

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.Shape.getChildCount()"""
        return int._wrap(super(Shape, self).getChildCount())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def setRadius(self, arg0: float):
        """public void com.badlogic.gdx.physics.box2d.Shape.setRadius(float)"""
        super(_Shape, self).setRadius(_float.valueOf(arg0))

    @override
    @overload
    def getRadius(self) -> float:
        """public float com.badlogic.gdx.physics.box2d.Shape.getRadius()"""
        return float._wrap(super(Shape, self).getRadius())

    @overload
    def set(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.PolygonShape.set(com.badlogic.gdx.math.Vector2[])"""
        super(_PolygonShape, self).set(arg0)

    @overload
    def setAsBox(self, arg0: float, arg1: float, arg2: 'Vector2', arg3: float):
        """public void com.badlogic.gdx.physics.box2d.PolygonShape.setAsBox(float,float,com.badlogic.gdx.math.Vector2,float)"""
        super(_PolygonShape, self).setAsBox(_float.valueOf(arg0), _float.valueOf(arg1), arg2, _float.valueOf(arg3))

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
    def set(self, arg0: 'float', arg1: int, arg2: int):
        """public void com.badlogic.gdx.physics.box2d.PolygonShape.set(float[],int,int)"""
        super(_PolygonShape, self).set(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.PolygonShape()"""
        val = _PolygonShape()
        self.__wrapper = val

    @overload
    def getVertexCount(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.PolygonShape.getVertexCount()"""
        return int._wrap(super(PolygonShape, self).getVertexCount())

    @override
    @overload
    def getType(self) -> 'Type':
        """public com.badlogic.gdx.physics.box2d.Shape$Type com.badlogic.gdx.physics.box2d.PolygonShape.getType()"""
        return 'Type'._wrap(super(PolygonShape, self).getType())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getVertex(self, arg0: int, arg1: 'Vector2'):
        """public void com.badlogic.gdx.physics.box2d.PolygonShape.getVertex(int,com.badlogic.gdx.math.Vector2)"""
        super(_PolygonShape, self).getVertex(_int.valueOf(arg0), arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.Box2DDebugRenderer
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.physics.box2d.Box2DDebugRenderer as _Box2DDebugRenderer
_Box2DDebugRenderer = _Box2DDebugRenderer
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Box2DDebugRenderer():
    """com.badlogic.gdx.physics.box2d.Box2DDebugRenderer"""
 
    @staticmethod
    def _wrap(java_value: _Box2DDebugRenderer) -> 'Box2DDebugRenderer':
        return Box2DDebugRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Box2DDebugRenderer):
        """
        Dynamic initializer for Box2DDebugRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Box2DDebugRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Box2DDebugRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getAxis() -> 'math.Vector2':
        """public static com.badlogic.gdx.math.Vector2 com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.getAxis()"""
        return math.Vector2._wrap(_Box2DDebugRenderer.getAxis())

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
    def isDrawBodies(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.isDrawBodies()"""
        return bool._wrap(super(Box2DDebugRenderer, self).isDrawBodies())

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
    def isDrawJoints(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.isDrawJoints()"""
        return bool._wrap(super(Box2DDebugRenderer, self).isDrawJoints())

    @overload
    def isDrawInactiveBodies(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.isDrawInactiveBodies()"""
        return bool._wrap(super(Box2DDebugRenderer, self).isDrawInactiveBodies())

    @overload
    def render(self, arg0: 'World', arg1: 'Matrix4'):
        """public void com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.render(com.badlogic.gdx.physics.box2d.World,com.badlogic.gdx.math.Matrix4)"""
        super(_Box2DDebugRenderer, self).render(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.physics.box2d.Box2DDebugRenderer()"""
        val = _Box2DDebugRenderer()
        self.__wrapper = val

    @overload
    def isDrawContacts(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.isDrawContacts()"""
        return bool._wrap(super(Box2DDebugRenderer, self).isDrawContacts())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setDrawVelocities(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.setDrawVelocities(boolean)"""
        super(_Box2DDebugRenderer, self).setDrawVelocities(_boolean.valueOf(arg0))

    @overload
    def setDrawJoints(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.setDrawJoints(boolean)"""
        super(_Box2DDebugRenderer, self).setDrawJoints(_boolean.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def setAxis(arg0: 'Vector2'):
        """public static void com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.setAxis(com.badlogic.gdx.math.Vector2)"""
        _Box2DDebugRenderer.setAxis(arg0)

    @overload
    def __init__(self, arg0: bool, arg1: bool, arg2: bool, arg3: bool, arg4: bool, arg5: bool):
        """public com.badlogic.gdx.physics.box2d.Box2DDebugRenderer(boolean,boolean,boolean,boolean,boolean,boolean)"""
        val = _Box2DDebugRenderer(_boolean.valueOf(arg0), _boolean.valueOf(arg1), _boolean.valueOf(arg2), _boolean.valueOf(arg3), _boolean.valueOf(arg4), _boolean.valueOf(arg5))
        self.__wrapper = val

    @overload
    def isDrawAABBs(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.isDrawAABBs()"""
        return bool._wrap(super(Box2DDebugRenderer, self).isDrawAABBs())

    @overload
    def setDrawInactiveBodies(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.setDrawInactiveBodies(boolean)"""
        super(_Box2DDebugRenderer, self).setDrawInactiveBodies(_boolean.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setDrawBodies(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.setDrawBodies(boolean)"""
        super(_Box2DDebugRenderer, self).setDrawBodies(_boolean.valueOf(arg0))

    @overload
    def isDrawVelocities(self) -> bool:
        """public boolean com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.isDrawVelocities()"""
        return bool._wrap(super(Box2DDebugRenderer, self).isDrawVelocities())

    @overload
    def setDrawAABBs(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.setDrawAABBs(boolean)"""
        super(_Box2DDebugRenderer, self).setDrawAABBs(_boolean.valueOf(arg0))

    @overload
    def setDrawContacts(self, arg0: bool):
        """public void com.badlogic.gdx.physics.box2d.Box2DDebugRenderer.setDrawContacts(boolean)"""
        super(_Box2DDebugRenderer, self).setDrawContacts(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.physics.box2d.Box2DDebugRenderer()"""
        val = _Box2DDebugRenderer()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.JointDef$JointType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import com.badlogic.gdx.physics.box2d.JointDef as _JointDef_JointType
_JointType = _JointDef_JointType.JointType
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JointType():
    """com.badlogic.gdx.physics.box2d.JointDef.JointType"""
 
    @staticmethod
    def _wrap(java_value: _JointType) -> 'JointType':
        return JointType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JointType):
        """
        Dynamic initializer for JointType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JointType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JointType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def values() -> List['JointType']:
        """public static com.badlogic.gdx.physics.box2d.JointDef$JointType[] com.badlogic.gdx.physics.box2d.JointDef$JointType.values()"""
        return List[JointType]._wrap(_JointType.values())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'JointType':
        """public static com.badlogic.gdx.physics.box2d.JointDef$JointType com.badlogic.gdx.physics.box2d.JointDef$JointType.valueOf(java.lang.String)"""
        return JointType._wrap(_JointType.valueOf(arg0))

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @overload
    def getValue(self) -> int:
        """public int com.badlogic.gdx.physics.box2d.JointDef$JointType.getValue()"""
        return int._wrap(super(JointType, self).getValue())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.Manifold$ManifoldPoint
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
import com.badlogic.gdx.physics.box2d.Manifold as _Manifold_ManifoldPoint
_ManifoldPoint = _Manifold_ManifoldPoint.ManifoldPoint
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ManifoldPoint():
    """com.badlogic.gdx.physics.box2d.Manifold.ManifoldPoint"""
 
    @staticmethod
    def _wrap(java_value: _ManifoldPoint) -> 'ManifoldPoint':
        return ManifoldPoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ManifoldPoint):
        """
        Dynamic initializer for ManifoldPoint.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ManifoldPoint__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ManifoldPoint__wrapper":
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
        return str._wrap(super(ManifoldPoint, self).toString())

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
    def __init__(self, arg0: 'Manifold'):
        """public com.badlogic.gdx.physics.box2d.Manifold$ManifoldPoint(com.badlogic.gdx.physics.box2d.Manifold)"""
        val = _ManifoldPoint(arg0)
        self.__wrapper = val