from __future__ import annotations
from overload import overload


 
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
import dev.ultreon.quantum.world.gen.noise.FastNoiseLite as _FastNoiseLite_DomainWarpType
_DomainWarpType = _FastNoiseLite_DomainWarpType.DomainWarpType
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
 
class DomainWarpType():
    """dev.ultreon.quantum.world.gen.noise.FastNoiseLite.DomainWarpType"""
 
    @staticmethod
    def _wrap(java_value: _DomainWarpType) -> 'DomainWarpType':
        return DomainWarpType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DomainWarpType):
        """
        Dynamic initializer for DomainWarpType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DomainWarpType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DomainWarpType__wrapper":
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
    def valueOf(arg0: str) -> 'DomainWarpType':
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType.valueOf(java.lang.String)"""
        return DomainWarpType._wrap(_DomainWarpType.valueOf(arg0))

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
    def values() -> List['DomainWarpType']:
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType[] dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType.values()"""
        return List[DomainWarpType]._wrap(_DomainWarpType.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


DomainWarpType.BasicGrid = DomainWarpType._wrap(_BasicGrid.BasicGrid)

DomainWarpType.OpenSimplex2 = DomainWarpType._wrap(_OpenSimplex2.OpenSimplex2)

DomainWarpType.OpenSimplex2Reduced = DomainWarpType._wrap(_OpenSimplex2Reduced.OpenSimplex2Reduced)

 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType
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
import dev.ultreon.quantum.world.gen.noise.FastNoiseLite as _FastNoiseLite_DomainWarpType
_DomainWarpType = _FastNoiseLite_DomainWarpType.DomainWarpType
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
 
class DomainWarpType():
    """dev.ultreon.quantum.world.gen.noise.FastNoiseLite.DomainWarpType"""
 
    @staticmethod
    def _wrap(java_value: _DomainWarpType) -> 'DomainWarpType':
        return DomainWarpType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DomainWarpType):
        """
        Dynamic initializer for DomainWarpType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DomainWarpType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DomainWarpType__wrapper":
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
    def valueOf(arg0: str) -> 'DomainWarpType':
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType.valueOf(java.lang.String)"""
        return DomainWarpType._wrap(_DomainWarpType.valueOf(arg0))

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
    def values() -> List['DomainWarpType']:
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType[] dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType.values()"""
        return List[DomainWarpType]._wrap(_DomainWarpType.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


DomainWarpType.BasicGrid = DomainWarpType._wrap(_BasicGrid.BasicGrid)

DomainWarpType.OpenSimplex2 = DomainWarpType._wrap(_OpenSimplex2.OpenSimplex2)

DomainWarpType.OpenSimplex2Reduced = DomainWarpType._wrap(_OpenSimplex2Reduced.OpenSimplex2Reduced)

 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.FastNoiseLite$NoiseType
import dev.ultreon.quantum.world.gen.noise.FastNoiseLite as _FastNoiseLite_NoiseType
_NoiseType = _FastNoiseLite_NoiseType.NoiseType
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
 
class NoiseType():
    """dev.ultreon.quantum.world.gen.noise.FastNoiseLite.NoiseType"""
 
    @staticmethod
    def _wrap(java_value: _NoiseType) -> 'NoiseType':
        return NoiseType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NoiseType):
        """
        Dynamic initializer for NoiseType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NoiseType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NoiseType__wrapper":
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
    def valueOf(arg0: str) -> 'NoiseType':
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$NoiseType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$NoiseType.valueOf(java.lang.String)"""
        return NoiseType._wrap(_NoiseType.valueOf(arg0))

    @staticmethod
    @overload
    def values() -> List['NoiseType']:
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$NoiseType[] dev.ultreon.quantum.world.gen.noise.FastNoiseLite$NoiseType.values()"""
        return List[NoiseType]._wrap(_NoiseType.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


NoiseType.Perlin = NoiseType._wrap(_Perlin.Perlin)

NoiseType.Value = NoiseType._wrap(_Value.Value)

NoiseType.ValueCubic = NoiseType._wrap(_ValueCubic.ValueCubic)

NoiseType.OpenSimplex2 = NoiseType._wrap(_OpenSimplex2.OpenSimplex2)

NoiseType.Cellular = NoiseType._wrap(_Cellular.Cellular)

NoiseType.OpenSimplex2S = NoiseType._wrap(_OpenSimplex2S.OpenSimplex2S) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.JNoiseType
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import dev.ultreon.quantum.world.gen.noise.JNoiseType as _JNoiseType
_JNoiseType = _JNoiseType
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import de.articdive.jnoise.core.api.pipeline.NoiseSource as _NoiseSource
_NoiseSource = _NoiseSource
from builtins import float
import de.articdive.jnoise.core.api.pipeline.NoiseSource as NoiseSource
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JNoiseType():
    """dev.ultreon.quantum.world.gen.noise.JNoiseType"""
 
    @staticmethod
    def _wrap(java_value: _JNoiseType) -> 'JNoiseType':
        return JNoiseType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JNoiseType):
        """
        Dynamic initializer for JNoiseType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JNoiseType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JNoiseType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.noise.JNoiseType.equals(java.lang.Object)"""
        return bool._wrap(super(_JNoiseType, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def source(self) -> 'NoiseSource':
        """public de.articdive.jnoise.core.api.pipeline.NoiseSource dev.ultreon.quantum.world.gen.noise.JNoiseType.source()"""
        return 'NoiseSource'._wrap(super(JNoiseType, self).source())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.gen.noise.JNoiseType.toString()"""
        return str._wrap(super(JNoiseType, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.gen.noise.JNoiseType.hashCode()"""
        return int._wrap(super(JNoiseType, self).hashCode())

    @overload
    def eval(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.JNoiseType.eval(double,double,double)"""
        return float._wrap(super(_JNoiseType, self).eval(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.noise.JNoiseType.dispose()"""
        super(JNoiseType, self).dispose()

    @overload
    def __init__(self, arg0: 'NoiseSource'):
        """public dev.ultreon.quantum.world.gen.noise.JNoiseType(de.articdive.jnoise.core.api.pipeline.NoiseSource)"""
        val = _JNoiseType(arg0)
        self.__wrapper = val

    @overload
    def eval(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.JNoiseType.eval(double,double)"""
        return float._wrap(super(_JNoiseType, self).eval(_double.valueOf(arg0), _double.valueOf(arg1))) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.NoiseConfigs
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.world.gen.noise.NoiseConfigs as _NoiseConfigs
_NoiseConfigs = _NoiseConfigs
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NoiseConfigs():
    """dev.ultreon.quantum.world.gen.noise.NoiseConfigs"""
 
    @staticmethod
    def _wrap(java_value: _NoiseConfigs) -> 'NoiseConfigs':
        return NoiseConfigs(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NoiseConfigs):
        """
        Dynamic initializer for NoiseConfigs.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NoiseConfigs__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NoiseConfigs__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.LAYER_X
    LAYER_X: 'NoiseConfig' = _wrap(_NoiseConfig.LAYER_X)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.FIOLAGE
    FIOLAGE: 'NoiseConfig' = _wrap(_NoiseConfig.FIOLAGE)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.ROCK
    ROCK: 'NoiseConfig' = _wrap(_NoiseConfig.ROCK)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.OCEAN
    OCEAN: 'NoiseConfig' = _wrap(_NoiseConfig.OCEAN)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.PATCH
    PATCH: 'NoiseConfig' = _wrap(_NoiseConfig.PATCH)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.WATER_PATCH_1
    WATER_PATCH_1: 'NoiseConfig' = _wrap(_NoiseConfig.WATER_PATCH_1)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.BIOME_MAP
    BIOME_MAP: 'NoiseConfig' = _wrap(_NoiseConfig.BIOME_MAP)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.CACTI
    CACTI: 'NoiseConfig' = _wrap(_NoiseConfig.CACTI)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.LAYER_Y
    LAYER_Y: 'NoiseConfig' = _wrap(_NoiseConfig.LAYER_Y)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.ORE
    ORE: 'NoiseConfig' = _wrap(_NoiseConfig.ORE)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.BIOME_X
    BIOME_X: 'NoiseConfig' = _wrap(_NoiseConfig.BIOME_X)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.BIOME_Y
    BIOME_Y: 'NoiseConfig' = _wrap(_NoiseConfig.BIOME_Y)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.EMPTY
    EMPTY: 'NoiseConfig' = _wrap(_NoiseConfig.EMPTY)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.WATER_PATCH_2
    WATER_PATCH_2: 'NoiseConfig' = _wrap(_NoiseConfig.WATER_PATCH_2)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.DEFAULT
    DEFAULT: 'NoiseConfig' = _wrap(_NoiseConfig.DEFAULT)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.TREE
    TREE: 'NoiseConfig' = _wrap(_NoiseConfig.TREE)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.GENERIC_NOISE
    GENERIC_NOISE: 'NoiseConfig' = _wrap(_NoiseConfig.GENERIC_NOISE)


        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.world.gen.noise.NoiseConfigs.init()"""
            _NoiseConfigs.init()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.noise.NoiseConfigs()"""
        val = _NoiseConfigs()
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
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.noise.NoiseConfigs()"""
        val = _NoiseConfigs()
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
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.DomainWarping
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.libs.commons.v0.vector.Vec2d as _Vec2d
_Vec2d = _Vec2d
import java.lang.Object as _object
from builtins import type
from builtins import float
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.world.gen.noise.DomainWarping as _DomainWarping
_DomainWarping = _DomainWarping
import dev.ultreon.libs.commons.v0.vector.Vec2i as _Vec2i
_Vec2i = _Vec2i
import java.lang.Integer as _int
import dev.ultreon.quantum.world.gen.noise.NoiseInstance as _NoiseInstance
_NoiseInstance = _NoiseInstance
from builtins import bool
import java.lang.Long as _long
import reactor.core.Disposable as _Disposable
_Disposable = _Disposable
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DomainWarping():
    """dev.ultreon.quantum.world.gen.noise.DomainWarping"""
 
    @staticmethod
    def _wrap(java_value: _DomainWarping) -> 'DomainWarping':
        return DomainWarping(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DomainWarping):
        """
        Dynamic initializer for DomainWarping.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DomainWarping__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DomainWarping__wrapper":
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
    def __init__(self, arg0: 'NoiseInstance', arg1: 'NoiseInstance'):
        """public dev.ultreon.quantum.world.gen.noise.DomainWarping(dev.ultreon.quantum.world.gen.noise.NoiseInstance,dev.ultreon.quantum.world.gen.noise.NoiseInstance)"""
        val = _DomainWarping(arg0, arg1)
        self.__wrapper = val

    @property
    def domainX(self) -> NoiseInstance:
        return NoiseInstance._wrap(super(_DomainWarping).domainX())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @property
    def domainY(self) -> NoiseInstance:
        return NoiseInstance._wrap(super(_DomainWarping).domainY())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: 'NoiseConfig', arg2: 'NoiseConfig'):
        """public dev.ultreon.quantum.world.gen.noise.DomainWarping(long,dev.ultreon.quantum.world.gen.noise.NoiseConfig,dev.ultreon.quantum.world.gen.noise.NoiseConfig)"""
        val = _DomainWarping(_long.valueOf(arg0), arg1, arg2)
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

    @overload
    def generateDomainNoise(self, arg0: int, arg1: int, arg2: 'NoiseInstance') -> float:
        """public double dev.ultreon.quantum.world.gen.noise.DomainWarping.generateDomainNoise(int,int,dev.ultreon.quantum.world.gen.noise.NoiseInstance)"""
        return float._wrap(super(_DomainWarping, self).generateDomainNoise(_int.valueOf(arg0), _int.valueOf(arg1), arg2))

    @overload
    def generateDomainOffset(self, arg0: int, arg1: int) -> 'vector.Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.quantum.world.gen.noise.DomainWarping.generateDomainOffset(int,int)"""
        return 'vector.Vec2d'._wrap(super(_DomainWarping, self).generateDomainOffset(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def isDisposed(self) -> bool:
        """public default boolean reactor.core.Disposable.isDisposed()"""
        return bool._wrap(super(Disposable, self).isDisposed())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.noise.DomainWarping.dispose()"""
        super(DomainWarping, self).dispose()

    @overload
    def generateDomainOffsetInt(self, arg0: int, arg1: int) -> 'vector.Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.quantum.world.gen.noise.DomainWarping.generateDomainOffsetInt(int,int)"""
        return 'vector.Vec2i'._wrap(super(_DomainWarping, self).generateDomainOffsetInt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.PerlinNoise
from builtins import str
import dev.ultreon.quantum.world.gen.noise.PerlinNoise as _PerlinNoise
_PerlinNoise = _PerlinNoise
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PerlinNoise():
    """dev.ultreon.quantum.world.gen.noise.PerlinNoise"""
 
    @staticmethod
    def _wrap(java_value: _PerlinNoise) -> 'PerlinNoise':
        return PerlinNoise(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PerlinNoise):
        """
        Dynamic initializer for PerlinNoise.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PerlinNoise__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PerlinNoise__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def smoothNoise(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.PerlinNoise.smoothNoise(double,double,double)"""
        return float._wrap(super(_PerlinNoise, self).smoothNoise(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.noise.PerlinNoise()"""
        val = _PerlinNoise()
        self.__wrapper = val

    @overload
    def eval(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.PerlinNoise.eval(double,double)"""
        return float._wrap(super(_PerlinNoise, self).eval(_double.valueOf(arg0), _double.valueOf(arg1)))

    @overload
    def getSeed(self) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.PerlinNoise.getSeed()"""
        return float._wrap(super(PerlinNoise, self).getSeed())

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.noise.PerlinNoise.dispose()"""
        super(PerlinNoise, self).dispose()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def eval(self, arg0: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.PerlinNoise.eval(double)"""
        return float._wrap(super(_PerlinNoise, self).eval(_double.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def eval(self, arg0: float, arg1: float, arg2: float, arg3: int) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.PerlinNoise.eval(double,double,double,int)"""
        return float._wrap(super(_PerlinNoise, self).eval(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _int.valueOf(arg3)))

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
    def __init__(self, arg0: float):
        """public dev.ultreon.quantum.world.gen.noise.PerlinNoise(double)"""
        val = _PerlinNoise(_double.valueOf(arg0))
        self.__wrapper = val

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
        """public dev.ultreon.quantum.world.gen.noise.PerlinNoise()"""
        val = _PerlinNoise()
        self.__wrapper = val

    @overload
    def setSeed(self, arg0: float):
        """public void dev.ultreon.quantum.world.gen.noise.PerlinNoise.setSeed(double)"""
        super(_PerlinNoise, self).setSeed(_double.valueOf(arg0))

    @overload
    def eval(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.PerlinNoise.eval(double,double,double)"""
        return float._wrap(super(_PerlinNoise, self).eval(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.FastNoiseLite$RotationType3D
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.world.gen.noise.FastNoiseLite as _FastNoiseLite_RotationType3D
_RotationType3D = _FastNoiseLite_RotationType3D.RotationType3D
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
 
class RotationType3D():
    """dev.ultreon.quantum.world.gen.noise.FastNoiseLite.RotationType3D"""
 
    @staticmethod
    def _wrap(java_value: _RotationType3D) -> 'RotationType3D':
        return RotationType3D(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RotationType3D):
        """
        Dynamic initializer for RotationType3D.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RotationType3D__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RotationType3D__wrapper":
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
    def valueOf(arg0: str) -> 'RotationType3D':
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$RotationType3D dev.ultreon.quantum.world.gen.noise.FastNoiseLite$RotationType3D.valueOf(java.lang.String)"""
        return RotationType3D._wrap(_RotationType3D.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['RotationType3D']:
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$RotationType3D[] dev.ultreon.quantum.world.gen.noise.FastNoiseLite$RotationType3D.values()"""
        return List[RotationType3D]._wrap(_RotationType3D.values())


RotationType3D.None = RotationType3D._wrap(_None.None)

RotationType3D.ImproveXYPlanes = RotationType3D._wrap(_ImproveXYPlanes.ImproveXYPlanes)

RotationType3D.ImproveXZPlanes = RotationType3D._wrap(_ImproveXZPlanes.ImproveXZPlanes) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.FastNoiseLite$Vector3
from builtins import str
import dev.ultreon.quantum.world.gen.noise.FastNoiseLite as _FastNoiseLite_Vector3
_Vector3 = _FastNoiseLite_Vector3.Vector3
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Vector3():
    """dev.ultreon.quantum.world.gen.noise.FastNoiseLite.Vector3"""
 
    @staticmethod
    def _wrap(java_value: _Vector3) -> 'Vector3':
        return Vector3(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Vector3):
        """
        Dynamic initializer for Vector3.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Vector3__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Vector3__wrapper":
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
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public dev.ultreon.quantum.world.gen.noise.FastNoiseLite$Vector3(double,double,double)"""
        val = _Vector3(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))
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
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.FastNoiseLite
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.world.gen.noise.FastNoiseLite as _FastNoiseLite
_FastNoiseLite = _FastNoiseLite
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FastNoiseLite():
    """dev.ultreon.quantum.world.gen.noise.FastNoiseLite"""
 
    @staticmethod
    def _wrap(java_value: _FastNoiseLite) -> 'FastNoiseLite':
        return FastNoiseLite(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FastNoiseLite):
        """
        Dynamic initializer for FastNoiseLite.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FastNoiseLite__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FastNoiseLite__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def GetNoise(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.FastNoiseLite.GetNoise(double,double)"""
        return float._wrap(super(_FastNoiseLite, self).GetNoise(_double.valueOf(arg0), _double.valueOf(arg1)))

    @overload
    def SetRotationType3D(self, arg0: 'RotationType3D'):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetRotationType3D(dev.ultreon.quantum.world.gen.noise.FastNoiseLite$RotationType3D)"""
        super(_FastNoiseLite, self).SetRotationType3D(arg0)

    @overload
    def SetSeed(self, arg0: int):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetSeed(long)"""
        super(_FastNoiseLite, self).SetSeed(_long.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.noise.FastNoiseLite()"""
        val = _FastNoiseLite()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def SetCellularJitter(self, arg0: float):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetCellularJitter(double)"""
        super(_FastNoiseLite, self).SetCellularJitter(_double.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def SetFractalType(self, arg0: 'FractalType'):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetFractalType(dev.ultreon.quantum.world.gen.noise.FastNoiseLite$FractalType)"""
        super(_FastNoiseLite, self).SetFractalType(arg0)

    @overload
    def SetCellularDistanceFunction(self, arg0: 'CellularDistanceFunction'):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetCellularDistanceFunction(dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularDistanceFunction)"""
        super(_FastNoiseLite, self).SetCellularDistanceFunction(arg0)

    @overload
    def SetNoiseType(self, arg0: 'NoiseType'):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetNoiseType(dev.ultreon.quantum.world.gen.noise.FastNoiseLite$NoiseType)"""
        super(_FastNoiseLite, self).SetNoiseType(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def SetCellularReturnType(self, arg0: 'CellularReturnType'):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetCellularReturnType(dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularReturnType)"""
        super(_FastNoiseLite, self).SetCellularReturnType(arg0)

    @overload
    def SetDomainWarpAmp(self, arg0: float):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetDomainWarpAmp(double)"""
        super(_FastNoiseLite, self).SetDomainWarpAmp(_double.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def SetFractalOctaves(self, arg0: int):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetFractalOctaves(long)"""
        super(_FastNoiseLite, self).SetFractalOctaves(_long.valueOf(arg0))

    @overload
    def SetDomainWarpType(self, arg0: 'DomainWarpType'):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetDomainWarpType(dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType)"""
        super(_FastNoiseLite, self).SetDomainWarpType(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.noise.FastNoiseLite()"""
        val = _FastNoiseLite()
        self.__wrapper = val

    @overload
    def SetFrequency(self, arg0: float):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetFrequency(double)"""
        super(_FastNoiseLite, self).SetFrequency(_double.valueOf(arg0))

    @overload
    def GetNoise(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.FastNoiseLite.GetNoise(double,double,double)"""
        return float._wrap(super(_FastNoiseLite, self).GetNoise(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def SetFractalGain(self, arg0: float):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetFractalGain(double)"""
        super(_FastNoiseLite, self).SetFractalGain(_double.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def SetFractalWeightedStrength(self, arg0: float):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetFractalWeightedStrength(double)"""
        super(_FastNoiseLite, self).SetFractalWeightedStrength(_double.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.world.gen.noise.FastNoiseLite(long)"""
        val = _FastNoiseLite(_long.valueOf(arg0))
        self.__wrapper = val

    @overload
    def SetFractalPingPongStrength(self, arg0: float):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetFractalPingPongStrength(double)"""
        super(_FastNoiseLite, self).SetFractalPingPongStrength(_double.valueOf(arg0))

    @overload
    def DomainWarp(self, arg0: 'Vector3'):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.DomainWarp(dev.ultreon.quantum.world.gen.noise.FastNoiseLite$Vector3)"""
        super(_FastNoiseLite, self).DomainWarp(arg0)

    @overload
    def SetFractalLacunarity(self, arg0: float):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetFractalLacunarity(double)"""
        super(_FastNoiseLite, self).SetFractalLacunarity(_double.valueOf(arg0))

    @overload
    def DomainWarp(self, arg0: 'Vector2'):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.DomainWarp(dev.ultreon.quantum.world.gen.noise.FastNoiseLite$Vector2)"""
        super(_FastNoiseLite, self).DomainWarp(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.NoiseUtils
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.world.gen.noise.NoiseUtils as _NoiseUtils
_NoiseUtils = _NoiseUtils
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NoiseUtils():
    """dev.ultreon.quantum.world.gen.noise.NoiseUtils"""
 
    @staticmethod
    def _wrap(java_value: _NoiseUtils) -> 'NoiseUtils':
        return NoiseUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NoiseUtils):
        """
        Dynamic initializer for NoiseUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NoiseUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NoiseUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def remapValue01ToInt(arg0: float, arg1: float, arg2: float) -> int:
        """public static int dev.ultreon.quantum.world.gen.noise.NoiseUtils.remapValue01ToInt(double,double,double)"""
        return int._wrap(_NoiseUtils.remapValue01ToInt(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

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

    @staticmethod
    @overload
    def octavePerlin(arg0: float, arg1: float, arg2: 'NoiseInstance') -> float:
        """public static double dev.ultreon.quantum.world.gen.noise.NoiseUtils.octavePerlin(double,double,dev.ultreon.quantum.world.gen.noise.NoiseInstance)"""
        return float._wrap(_NoiseUtils.octavePerlin(_double.valueOf(arg0), _double.valueOf(arg1), arg2))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def redistribution(arg0: float, arg1: 'NoiseInstance') -> float:
        """public static double dev.ultreon.quantum.world.gen.noise.NoiseUtils.redistribution(double,dev.ultreon.quantum.world.gen.noise.NoiseInstance)"""
        return float._wrap(_NoiseUtils.redistribution(_double.valueOf(arg0), arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def remapValue01(arg0: float, arg1: float, arg2: float) -> float:
        """public static double dev.ultreon.quantum.world.gen.noise.NoiseUtils.remapValue01(double,double,double)"""
        return float._wrap(_NoiseUtils.remapValue01(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def remapValue(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float) -> float:
        """public static double dev.ultreon.quantum.world.gen.noise.NoiseUtils.remapValue(double,double,double,double,double)"""
        return float._wrap(_NoiseUtils.remapValue(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3), _double.valueOf(arg4)))

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
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.FastNoiseLite$FractalType
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
import dev.ultreon.quantum.world.gen.noise.FastNoiseLite as _FastNoiseLite_FractalType
_FractalType = _FastNoiseLite_FractalType.FractalType
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
 
class FractalType():
    """dev.ultreon.quantum.world.gen.noise.FastNoiseLite.FractalType"""
 
    @staticmethod
    def _wrap(java_value: _FractalType) -> 'FractalType':
        return FractalType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FractalType):
        """
        Dynamic initializer for FractalType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FractalType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FractalType__wrapper":
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
    def valueOf(arg0: str) -> 'FractalType':
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$FractalType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$FractalType.valueOf(java.lang.String)"""
        return FractalType._wrap(_FractalType.valueOf(arg0))

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
    def values() -> List['FractalType']:
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$FractalType[] dev.ultreon.quantum.world.gen.noise.FastNoiseLite$FractalType.values()"""
        return List[FractalType]._wrap(_FractalType.values())

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


FractalType.DomainWarpProgressive = FractalType._wrap(_DomainWarpProgressive.DomainWarpProgressive)

FractalType.None = FractalType._wrap(_None.None)

FractalType.Ridged = FractalType._wrap(_Ridged.Ridged)

FractalType.FBm = FractalType._wrap(_FBm.FBm)

FractalType.DomainWarpIndependent = FractalType._wrap(_DomainWarpIndependent.DomainWarpIndependent)

FractalType.PingPong = FractalType._wrap(_PingPong.PingPong) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularDistanceFunction
from builtins import str
import dev.ultreon.quantum.world.gen.noise.FastNoiseLite as _FastNoiseLite_CellularDistanceFunction
_CellularDistanceFunction = _FastNoiseLite_CellularDistanceFunction.CellularDistanceFunction
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
 
class CellularDistanceFunction():
    """dev.ultreon.quantum.world.gen.noise.FastNoiseLite.CellularDistanceFunction"""
 
    @staticmethod
    def _wrap(java_value: _CellularDistanceFunction) -> 'CellularDistanceFunction':
        return CellularDistanceFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CellularDistanceFunction):
        """
        Dynamic initializer for CellularDistanceFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CellularDistanceFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CellularDistanceFunction__wrapper":
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
    def values() -> List['CellularDistanceFunction']:
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularDistanceFunction[] dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularDistanceFunction.values()"""
        return List[CellularDistanceFunction]._wrap(_CellularDistanceFunction.values())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'CellularDistanceFunction':
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularDistanceFunction dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularDistanceFunction.valueOf(java.lang.String)"""
        return CellularDistanceFunction._wrap(_CellularDistanceFunction.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


CellularDistanceFunction.EuclideanSq = CellularDistanceFunction._wrap(_EuclideanSq.EuclideanSq)

CellularDistanceFunction.Euclidean = CellularDistanceFunction._wrap(_Euclidean.Euclidean)

CellularDistanceFunction.Manhattan = CellularDistanceFunction._wrap(_Manhattan.Manhattan)

CellularDistanceFunction.Hybrid = CellularDistanceFunction._wrap(_Hybrid.Hybrid) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.SimplexNoise$Octave
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.world.gen.noise.SimplexNoise as _SimplexNoise_Octave
_Octave = _SimplexNoise_Octave.Octave
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Octave():
    """dev.ultreon.quantum.world.gen.noise.SimplexNoise.Octave"""
 
    @staticmethod
    def _wrap(java_value: _Octave) -> 'Octave':
        return Octave(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Octave):
        """
        Dynamic initializer for Octave.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Octave__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Octave__wrapper":
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
    def noise(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.SimplexNoise$Octave.noise(double,double)"""
        return float._wrap(super(_Octave, self).noise(_double.valueOf(arg0), _double.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.world.gen.noise.SimplexNoise$Octave(int)"""
        val = _Octave(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def noise(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.SimplexNoise$Octave.noise(double,double,double)"""
        return float._wrap(super(_Octave, self).noise(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def noise(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.SimplexNoise$Octave.noise(double,double,double,double)"""
        return float._wrap(super(_Octave, self).noise(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3)))

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
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.noise.SimplexNoise$Octave.dispose()"""
        super(Octave, self).dispose()

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.SimplexNoise
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.world.gen.noise.SimplexNoise as _SimplexNoise
_SimplexNoise = _SimplexNoise
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SimplexNoise():
    """dev.ultreon.quantum.world.gen.noise.SimplexNoise"""
 
    @staticmethod
    def _wrap(java_value: _SimplexNoise) -> 'SimplexNoise':
        return SimplexNoise(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SimplexNoise):
        """
        Dynamic initializer for SimplexNoise.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SimplexNoise__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SimplexNoise__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.noise.SimplexNoise.dispose()"""
        super(SimplexNoise, self).dispose()

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
    def eval(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.SimplexNoise.eval(double,double)"""
        return float._wrap(super(_SimplexNoise, self).eval(_double.valueOf(arg0), _double.valueOf(arg1)))

    @overload
    def __init__(self, arg0: int, arg1: float, arg2: int):
        """public dev.ultreon.quantum.world.gen.noise.SimplexNoise(int,double,long)"""
        val = _SimplexNoise(_int.valueOf(arg0), _double.valueOf(arg1), _long.valueOf(arg2))
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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def eval(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.SimplexNoise.eval(double,double,double)"""
        return float._wrap(super(_SimplexNoise, self).eval(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.NoiseConfig
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.world.gen.noise.NoiseConfig as _NoiseConfig
_NoiseConfig = _NoiseConfig
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import java.lang.Float as _float
import java.lang.Integer as _int
import dev.ultreon.libs.commons.v0.vector.Vec2f as _Vec2f
_Vec2f = _Vec2f
import dev.ultreon.quantum.world.gen.noise.NoiseInstance as _NoiseInstance
_NoiseInstance = _NoiseInstance
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NoiseConfig():
    """dev.ultreon.quantum.world.gen.noise.NoiseConfig"""
 
    @staticmethod
    def _wrap(java_value: _NoiseConfig) -> 'NoiseConfig':
        return NoiseConfig(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NoiseConfig):
        """
        Dynamic initializer for NoiseConfig.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NoiseConfig__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NoiseConfig__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def persistence(self) -> float:
        """public float dev.ultreon.quantum.world.gen.noise.NoiseConfig.persistence()"""
        return float._wrap(super(NoiseConfig, self).persistence())

    @overload
    def redistributionModifier(self) -> float:
        """public float dev.ultreon.quantum.world.gen.noise.NoiseConfig.redistributionModifier()"""
        return float._wrap(super(NoiseConfig, self).redistributionModifier())

    @overload
    def noiseZoom(self) -> float:
        """public float dev.ultreon.quantum.world.gen.noise.NoiseConfig.noiseZoom()"""
        return float._wrap(super(NoiseConfig, self).noiseZoom())

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.noise.NoiseConfig.equals(java.lang.Object)"""
        return bool._wrap(super(_NoiseConfig, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.gen.noise.NoiseConfig.toString()"""
        return str._wrap(super(NoiseConfig, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.gen.noise.NoiseConfig.hashCode()"""
        return int._wrap(super(NoiseConfig, self).hashCode())

    @overload
    def create(self, arg0: int) -> 'NoiseInstance':
        """public dev.ultreon.quantum.world.gen.noise.NoiseInstance dev.ultreon.quantum.world.gen.noise.NoiseConfig.create(long)"""
        return 'NoiseInstance'._wrap(super(_NoiseConfig, self).create(_long.valueOf(arg0)))

    @overload
    def octaves(self) -> float:
        """public float dev.ultreon.quantum.world.gen.noise.NoiseConfig.octaves()"""
        return float._wrap(super(NoiseConfig, self).octaves())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: 'Vec2f', arg3: int, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public dev.ultreon.quantum.world.gen.noise.NoiseConfig(float,float,dev.ultreon.libs.commons.v0.vector.Vec2f,long,float,float,float,float,float)"""
        val = _NoiseConfig(_float.valueOf(arg0), _float.valueOf(arg1), arg2, _long.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8))
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def seed(self) -> int:
        """public long dev.ultreon.quantum.world.gen.noise.NoiseConfig.seed()"""
        return int._wrap(super(NoiseConfig, self).seed())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def exponent(self) -> float:
        """public float dev.ultreon.quantum.world.gen.noise.NoiseConfig.exponent()"""
        return float._wrap(super(NoiseConfig, self).exponent())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def offset(self) -> 'vector.Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.quantum.world.gen.noise.NoiseConfig.offset()"""
        return 'vector.Vec2f'._wrap(super(NoiseConfig, self).offset()) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.NoiseType
import dev.ultreon.quantum.server.ServerDisposable as _ServerDisposable
_ServerDisposable = _ServerDisposable
from abc import abstractmethod, ABC
import dev.ultreon.quantum.world.gen.noise.NoiseType as _NoiseType
_NoiseType = _NoiseType
 
class NoiseType():
    """dev.ultreon.quantum.world.gen.noise.NoiseType"""
 
    @staticmethod
    def _wrap(java_value: _NoiseType) -> 'NoiseType':
        return NoiseType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NoiseType):
        """
        Dynamic initializer for NoiseType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NoiseType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NoiseType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def eval(self, arg0: float, arg1: float, arg2: float):
        """public abstract double dev.ultreon.quantum.world.gen.noise.NoiseType.eval(double,double,double)"""
        pass

    @abstractmethod
    def dispose(self, ):
        """public abstract void dev.ultreon.quantum.server.ServerDisposable.dispose()"""
        pass

    @abstractmethod
    def eval(self, arg0: float, arg1: float):
        """public abstract double dev.ultreon.quantum.world.gen.noise.NoiseType.eval(double,double)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.NoiseInstance
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.libs.commons.v0.vector.Vec2f as _Vec2f
_Vec2f = _Vec2f
import dev.ultreon.quantum.world.gen.noise.NoiseInstance as _NoiseInstance
_NoiseInstance = _NoiseInstance
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NoiseInstance():
    """dev.ultreon.quantum.world.gen.noise.NoiseInstance"""
 
    @staticmethod
    def _wrap(java_value: _NoiseInstance) -> 'NoiseInstance':
        return NoiseInstance(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NoiseInstance):
        """
        Dynamic initializer for NoiseInstance.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NoiseInstance__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NoiseInstance__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def noiseZoom(self) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.NoiseInstance.noiseZoom()"""
        return float._wrap(super(NoiseInstance, self).noiseZoom())

    @overload
    def offset(self) -> 'vector.Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.quantum.world.gen.noise.NoiseInstance.offset()"""
        return 'vector.Vec2f'._wrap(super(NoiseInstance, self).offset())

    @overload
    def redistributionModifier(self) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.NoiseInstance.redistributionModifier()"""
        return float._wrap(super(NoiseInstance, self).redistributionModifier())

    @overload
    def seed(self) -> int:
        """public long dev.ultreon.quantum.world.gen.noise.NoiseInstance.seed()"""
        return int._wrap(super(NoiseInstance, self).seed())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.noise.NoiseInstance.dispose()"""
        super(NoiseInstance, self).dispose()

    @overload
    def eval(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.NoiseInstance.eval(double,double)"""
        return float._wrap(super(_NoiseInstance, self).eval(_double.valueOf(arg0), _double.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'NoiseType', arg1: int):
        """public dev.ultreon.quantum.world.gen.noise.NoiseInstance(dev.ultreon.quantum.world.gen.noise.NoiseType,long)"""
        val = _NoiseInstance(arg0, _long.valueOf(arg1))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'NoiseType', arg1: int, arg2: float, arg3: float, arg4: 'Vec2f', arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public dev.ultreon.quantum.world.gen.noise.NoiseInstance(dev.ultreon.quantum.world.gen.noise.NoiseType,long,double,double,dev.ultreon.libs.commons.v0.vector.Vec2f,double,double,double,double,double)"""
        val = _NoiseInstance(arg0, _long.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3), arg4, _double.valueOf(arg5), _double.valueOf(arg6), _double.valueOf(arg7), _double.valueOf(arg8), _double.valueOf(arg9))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def base(self) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.NoiseInstance.base()"""
        return float._wrap(super(NoiseInstance, self).base())

    @overload
    def octaves(self) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.NoiseInstance.octaves()"""
        return float._wrap(super(NoiseInstance, self).octaves())

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
    def exponent(self) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.NoiseInstance.exponent()"""
        return float._wrap(super(NoiseInstance, self).exponent())

    @overload
    def persistence(self) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.NoiseInstance.persistence()"""
        return float._wrap(super(NoiseInstance, self).persistence())

    @overload
    def amplitude(self) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.NoiseInstance.amplitude()"""
        return float._wrap(super(NoiseInstance, self).amplitude())

    @overload
    def eval(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.NoiseInstance.eval(double,double,double)"""
        return float._wrap(super(_NoiseInstance, self).eval(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

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
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularReturnType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.world.gen.noise.FastNoiseLite as _FastNoiseLite_CellularReturnType
_CellularReturnType = _FastNoiseLite_CellularReturnType.CellularReturnType
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
 
class CellularReturnType():
    """dev.ultreon.quantum.world.gen.noise.FastNoiseLite.CellularReturnType"""
 
    @staticmethod
    def _wrap(java_value: _CellularReturnType) -> 'CellularReturnType':
        return CellularReturnType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CellularReturnType):
        """
        Dynamic initializer for CellularReturnType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CellularReturnType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CellularReturnType__wrapper":
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
    def valueOf(arg0: str) -> 'CellularReturnType':
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularReturnType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularReturnType.valueOf(java.lang.String)"""
        return CellularReturnType._wrap(_CellularReturnType.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def values() -> List['CellularReturnType']:
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularReturnType[] dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularReturnType.values()"""
        return List[CellularReturnType]._wrap(_CellularReturnType.values())

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


CellularReturnType.CellValue = CellularReturnType._wrap(_CellValue.CellValue)

CellularReturnType.Distance2Mul = CellularReturnType._wrap(_Distance2Mul.Distance2Mul)

CellularReturnType.Distance2Add = CellularReturnType._wrap(_Distance2Add.Distance2Add)

CellularReturnType.Distance2Div = CellularReturnType._wrap(_Distance2Div.Distance2Div)

CellularReturnType.Distance2Sub = CellularReturnType._wrap(_Distance2Sub.Distance2Sub)

CellularReturnType.Distance = CellularReturnType._wrap(_Distance.Distance)

CellularReturnType.Distance2 = CellularReturnType._wrap(_Distance2.Distance2) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.FastNoiseLite$Vector2
from builtins import str
import java.lang.Double as _double
import dev.ultreon.quantum.world.gen.noise.FastNoiseLite as _FastNoiseLite_Vector2
_Vector2 = _FastNoiseLite_Vector2.Vector2
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Vector2():
    """dev.ultreon.quantum.world.gen.noise.FastNoiseLite.Vector2"""
 
    @staticmethod
    def _wrap(java_value: _Vector2) -> 'Vector2':
        return Vector2(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Vector2):
        """
        Dynamic initializer for Vector2.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Vector2__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Vector2__wrapper":
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
    def __init__(self, arg0: float, arg1: float):
        """public dev.ultreon.quantum.world.gen.noise.FastNoiseLite$Vector2(double,double)"""
        val = _Vector2(_double.valueOf(arg0), _double.valueOf(arg1))
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