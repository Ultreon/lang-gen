from __future__ import annotations
from overload import overload


 
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
import dev.ultreon.quantum.world.gen.noise.FastNoiseLite as __FastNoiseLite_DomainWarpType
__DomainWarpType = __FastNoiseLite_DomainWarpType.DomainWarpType
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class DomainWarpType():
    """dev.ultreon.quantum.world.gen.noise.FastNoiseLite.DomainWarpType"""
 
    @staticmethod
    def __wrap(java_value: __DomainWarpType) -> 'DomainWarpType':
        return DomainWarpType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DomainWarpType):
        """
        Dynamic initializer for DomainWarpType.
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
 
    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType.OpenSimplex2
    OpenSimplex2: 'DomainWarpType' = __wrap(__DomainWarpType.OpenSimplex2)

    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType.BasicGrid
    BasicGrid: 'DomainWarpType' = __wrap(__DomainWarpType.BasicGrid)

    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType.OpenSimplex2Reduced
    OpenSimplex2Reduced: 'DomainWarpType' = __wrap(__DomainWarpType.OpenSimplex2Reduced)


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
    def valueOf(arg0: str) -> 'DomainWarpType':
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType.valueOf(java.lang.String)"""
        return DomainWarpType.__wrap(__DomainWarpType.valueOf(arg0))

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
    def values() -> List['DomainWarpType']:
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType[] dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType.values()"""
        return List[DomainWarpType].__wrap(__DomainWarpType.values())

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

 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType
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
import dev.ultreon.quantum.world.gen.noise.FastNoiseLite as __FastNoiseLite_DomainWarpType
__DomainWarpType = __FastNoiseLite_DomainWarpType.DomainWarpType
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class DomainWarpType():
    """dev.ultreon.quantum.world.gen.noise.FastNoiseLite.DomainWarpType"""
 
    @staticmethod
    def __wrap(java_value: __DomainWarpType) -> 'DomainWarpType':
        return DomainWarpType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DomainWarpType):
        """
        Dynamic initializer for DomainWarpType.
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
 
    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType.OpenSimplex2
    OpenSimplex2: 'DomainWarpType' = __wrap(__DomainWarpType.OpenSimplex2)

    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType.BasicGrid
    BasicGrid: 'DomainWarpType' = __wrap(__DomainWarpType.BasicGrid)

    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType.OpenSimplex2Reduced
    OpenSimplex2Reduced: 'DomainWarpType' = __wrap(__DomainWarpType.OpenSimplex2Reduced)


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
    def valueOf(arg0: str) -> 'DomainWarpType':
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType.valueOf(java.lang.String)"""
        return DomainWarpType.__wrap(__DomainWarpType.valueOf(arg0))

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
    def values() -> List['DomainWarpType']:
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType[] dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType.values()"""
        return List[DomainWarpType].__wrap(__DomainWarpType.values())

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

 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.FastNoiseLite$NoiseType
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
import java.lang.Integer as __int
import dev.ultreon.quantum.world.gen.noise.FastNoiseLite as __FastNoiseLite_NoiseType
__NoiseType = __FastNoiseLite_NoiseType.NoiseType
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class NoiseType():
    """dev.ultreon.quantum.world.gen.noise.FastNoiseLite.NoiseType"""
 
    @staticmethod
    def __wrap(java_value: __NoiseType) -> 'NoiseType':
        return NoiseType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NoiseType):
        """
        Dynamic initializer for NoiseType.
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
 
    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$NoiseType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$NoiseType.Cellular
    Cellular: 'NoiseType' = __wrap(__NoiseType.Cellular)

    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$NoiseType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$NoiseType.Value
    Value: 'NoiseType' = __wrap(__NoiseType.Value)

    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$NoiseType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$NoiseType.ValueCubic
    ValueCubic: 'NoiseType' = __wrap(__NoiseType.ValueCubic)

    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$NoiseType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$NoiseType.OpenSimplex2
    OpenSimplex2: 'NoiseType' = __wrap(__NoiseType.OpenSimplex2)

    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$NoiseType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$NoiseType.OpenSimplex2S
    OpenSimplex2S: 'NoiseType' = __wrap(__NoiseType.OpenSimplex2S)

    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$NoiseType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$NoiseType.Perlin
    Perlin: 'NoiseType' = __wrap(__NoiseType.Perlin)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'NoiseType':
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$NoiseType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$NoiseType.valueOf(java.lang.String)"""
        return NoiseType.__wrap(__NoiseType.valueOf(arg0))

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
    def values() -> List['NoiseType']:
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$NoiseType[] dev.ultreon.quantum.world.gen.noise.FastNoiseLite$NoiseType.values()"""
        return List[NoiseType].__wrap(__NoiseType.values())

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
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.JNoiseType
from builtins import str
import dev.ultreon.quantum.world.gen.noise.JNoiseType as __JNoiseType
__JNoiseType = __JNoiseType
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import de.articdive.jnoise.core.api.pipeline.NoiseSource as NoiseSource
import de.articdive.jnoise.core.api.pipeline.NoiseSource as __NoiseSource
__NoiseSource = __NoiseSource
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class JNoiseType():
    """dev.ultreon.quantum.world.gen.noise.JNoiseType"""
 
    @staticmethod
    def __wrap(java_value: __JNoiseType) -> 'JNoiseType':
        return JNoiseType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JNoiseType):
        """
        Dynamic initializer for JNoiseType.
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
    def __init__(self, arg0: 'NoiseSource'):
        """public dev.ultreon.quantum.world.gen.noise.JNoiseType(de.articdive.jnoise.core.api.pipeline.NoiseSource)"""
        val = __JNoiseType(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.gen.noise.JNoiseType.hashCode()"""
        return int.__wrap(super(JNoiseType, self).hashCode())

    @overload
    def eval(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.JNoiseType.eval(double,double,double)"""
        return float.__wrap(super(__JNoiseType, self).eval(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.noise.JNoiseType.equals(java.lang.Object)"""
        return bool.__wrap(super(__JNoiseType, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.gen.noise.JNoiseType.toString()"""
        return str.__wrap(super(JNoiseType, self).toString())

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
    def source(self) -> 'NoiseSource':
        """public de.articdive.jnoise.core.api.pipeline.NoiseSource dev.ultreon.quantum.world.gen.noise.JNoiseType.source()"""
        return 'NoiseSource'.__wrap(super(JNoiseType, self).source())

    @overload
    def eval(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.JNoiseType.eval(double,double)"""
        return float.__wrap(super(__JNoiseType, self).eval(__double.valueOf(arg0), __double.valueOf(arg1)))

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
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.NoiseConfigs
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
import dev.ultreon.quantum.world.gen.noise.NoiseConfigs as __NoiseConfigs
__NoiseConfigs = __NoiseConfigs
from builtins import bool
from builtins import int
 
class NoiseConfigs():
    """dev.ultreon.quantum.world.gen.noise.NoiseConfigs"""
 
    @staticmethod
    def __wrap(java_value: __NoiseConfigs) -> 'NoiseConfigs':
        return NoiseConfigs(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NoiseConfigs):
        """
        Dynamic initializer for NoiseConfigs.
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
 
    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.TREE
    TREE: 'NoiseConfig' = __wrap(__NoiseConfig.TREE)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.ROCK
    ROCK: 'NoiseConfig' = __wrap(__NoiseConfig.ROCK)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.WATER_PATCH_1
    WATER_PATCH_1: 'NoiseConfig' = __wrap(__NoiseConfig.WATER_PATCH_1)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.BIOME_Y
    BIOME_Y: 'NoiseConfig' = __wrap(__NoiseConfig.BIOME_Y)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.DEFAULT
    DEFAULT: 'NoiseConfig' = __wrap(__NoiseConfig.DEFAULT)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.ORE
    ORE: 'NoiseConfig' = __wrap(__NoiseConfig.ORE)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.OCEAN
    OCEAN: 'NoiseConfig' = __wrap(__NoiseConfig.OCEAN)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.CACTI
    CACTI: 'NoiseConfig' = __wrap(__NoiseConfig.CACTI)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.EMPTY
    EMPTY: 'NoiseConfig' = __wrap(__NoiseConfig.EMPTY)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.WATER_PATCH_2
    WATER_PATCH_2: 'NoiseConfig' = __wrap(__NoiseConfig.WATER_PATCH_2)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.FIOLAGE
    FIOLAGE: 'NoiseConfig' = __wrap(__NoiseConfig.FIOLAGE)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.PATCH
    PATCH: 'NoiseConfig' = __wrap(__NoiseConfig.PATCH)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.GENERIC_NOISE
    GENERIC_NOISE: 'NoiseConfig' = __wrap(__NoiseConfig.GENERIC_NOISE)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.BIOME_X
    BIOME_X: 'NoiseConfig' = __wrap(__NoiseConfig.BIOME_X)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.LAYER_X
    LAYER_X: 'NoiseConfig' = __wrap(__NoiseConfig.LAYER_X)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.LAYER_Y
    LAYER_Y: 'NoiseConfig' = __wrap(__NoiseConfig.LAYER_Y)

    # public static final dev.ultreon.quantum.world.gen.noise.NoiseConfig dev.ultreon.quantum.world.gen.noise.NoiseConfigs.BIOME_MAP
    BIOME_MAP: 'NoiseConfig' = __wrap(__NoiseConfig.BIOME_MAP)


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
        """public dev.ultreon.quantum.world.gen.noise.NoiseConfigs()"""
        val = __NoiseConfigs()
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.noise.NoiseConfigs()"""
        val = __NoiseConfigs()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.world.gen.noise.NoiseConfigs.init()"""
            __NoiseConfigs.init()

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
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.DomainWarping
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.world.gen.noise.DomainWarping as __DomainWarping
__DomainWarping = __DomainWarping
from builtins import float
import dev.ultreon.libs.commons.v0.vector.Vec2i as __Vec2i
__Vec2i = __Vec2i
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import dev.ultreon.quantum.world.gen.noise.NoiseInstance as __NoiseInstance
__NoiseInstance = __NoiseInstance
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import reactor.core.Disposable as __Disposable
__Disposable = __Disposable
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.libs.commons.v0.vector.Vec2d as __Vec2d
__Vec2d = __Vec2d
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DomainWarping():
    """dev.ultreon.quantum.world.gen.noise.DomainWarping"""
 
    @staticmethod
    def __wrap(java_value: __DomainWarping) -> 'DomainWarping':
        return DomainWarping(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DomainWarping):
        """
        Dynamic initializer for DomainWarping.
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
    def generateDomainOffsetInt(self, arg0: int, arg1: int) -> 'vector.Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.quantum.world.gen.noise.DomainWarping.generateDomainOffsetInt(int,int)"""
        return 'vector.Vec2i'.__wrap(super(__DomainWarping, self).generateDomainOffsetInt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @property
    def domainX(self) -> NoiseInstance:
        return NoiseInstance.__wrap(super(__DomainWarping).domainX())

    @override
    @overload
    def isDisposed(self) -> bool:
        """public default boolean reactor.core.Disposable.isDisposed()"""
        return bool.__wrap(super(Disposable, self).isDisposed())

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
    def __init__(self, arg0: int, arg1: 'NoiseConfig', arg2: 'NoiseConfig'):
        """public dev.ultreon.quantum.world.gen.noise.DomainWarping(long,dev.ultreon.quantum.world.gen.noise.NoiseConfig,dev.ultreon.quantum.world.gen.noise.NoiseConfig)"""
        val = __DomainWarping(__long.valueOf(arg0), arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'NoiseInstance', arg1: 'NoiseInstance'):
        """public dev.ultreon.quantum.world.gen.noise.DomainWarping(dev.ultreon.quantum.world.gen.noise.NoiseInstance,dev.ultreon.quantum.world.gen.noise.NoiseInstance)"""
        val = __DomainWarping(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @property
    def domainY(self) -> NoiseInstance:
        return NoiseInstance.__wrap(super(__DomainWarping).domainY())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def generateDomainOffset(self, arg0: int, arg1: int) -> 'vector.Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.quantum.world.gen.noise.DomainWarping.generateDomainOffset(int,int)"""
        return 'vector.Vec2d'.__wrap(super(__DomainWarping, self).generateDomainOffset(__int.valueOf(arg0), __int.valueOf(arg1)))

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
    def generateDomainNoise(self, arg0: int, arg1: int, arg2: 'NoiseInstance') -> float:
        """public double dev.ultreon.quantum.world.gen.noise.DomainWarping.generateDomainNoise(int,int,dev.ultreon.quantum.world.gen.noise.NoiseInstance)"""
        return float.__wrap(super(__DomainWarping, self).generateDomainNoise(__int.valueOf(arg0), __int.valueOf(arg1), arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.PerlinNoise
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.world.gen.noise.PerlinNoise as __PerlinNoise
__PerlinNoise = __PerlinNoise
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PerlinNoise():
    """dev.ultreon.quantum.world.gen.noise.PerlinNoise"""
 
    @staticmethod
    def __wrap(java_value: __PerlinNoise) -> 'PerlinNoise':
        return PerlinNoise(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PerlinNoise):
        """
        Dynamic initializer for PerlinNoise.
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

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.noise.PerlinNoise.dispose()"""
        super(PerlinNoise, self).dispose()

    @overload
    def eval(self, arg0: float, arg1: float, arg2: float, arg3: int) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.PerlinNoise.eval(double,double,double,int)"""
        return float.__wrap(super(__PerlinNoise, self).eval(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def getSeed(self) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.PerlinNoise.getSeed()"""
        return float.__wrap(super(PerlinNoise, self).getSeed())

    @overload
    def __init__(self, arg0: float):
        """public dev.ultreon.quantum.world.gen.noise.PerlinNoise(double)"""
        val = __PerlinNoise(__double.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setSeed(self, arg0: float):
        """public void dev.ultreon.quantum.world.gen.noise.PerlinNoise.setSeed(double)"""
        super(__PerlinNoise, self).setSeed(__double.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def eval(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.PerlinNoise.eval(double,double)"""
        return float.__wrap(super(__PerlinNoise, self).eval(__double.valueOf(arg0), __double.valueOf(arg1)))

    @overload
    def eval(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.PerlinNoise.eval(double,double,double)"""
        return float.__wrap(super(__PerlinNoise, self).eval(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def eval(self, arg0: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.PerlinNoise.eval(double)"""
        return float.__wrap(super(__PerlinNoise, self).eval(__double.valueOf(arg0)))

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.noise.PerlinNoise()"""
        val = __PerlinNoise()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def smoothNoise(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.PerlinNoise.smoothNoise(double,double,double)"""
        return float.__wrap(super(__PerlinNoise, self).smoothNoise(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.noise.PerlinNoise()"""
        val = __PerlinNoise()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.FastNoiseLite$RotationType3D
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
import dev.ultreon.quantum.world.gen.noise.FastNoiseLite as __FastNoiseLite_RotationType3D
__RotationType3D = __FastNoiseLite_RotationType3D.RotationType3D
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class RotationType3D():
    """dev.ultreon.quantum.world.gen.noise.FastNoiseLite.RotationType3D"""
 
    @staticmethod
    def __wrap(java_value: __RotationType3D) -> 'RotationType3D':
        return RotationType3D(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RotationType3D):
        """
        Dynamic initializer for RotationType3D.
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
 
    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$RotationType3D dev.ultreon.quantum.world.gen.noise.FastNoiseLite$RotationType3D.ImproveXYPlanes
    ImproveXYPlanes: 'RotationType3D' = __wrap(__RotationType3D.ImproveXYPlanes)

    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$RotationType3D dev.ultreon.quantum.world.gen.noise.FastNoiseLite$RotationType3D.ImproveXZPlanes
    ImproveXZPlanes: 'RotationType3D' = __wrap(__RotationType3D.ImproveXZPlanes)

    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$RotationType3D dev.ultreon.quantum.world.gen.noise.FastNoiseLite$RotationType3D.None
    None: 'RotationType3D' = __wrap(__RotationType3D.None)


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

    @staticmethod
    @overload
    def values() -> List['RotationType3D']:
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$RotationType3D[] dev.ultreon.quantum.world.gen.noise.FastNoiseLite$RotationType3D.values()"""
        return List[RotationType3D].__wrap(__RotationType3D.values())

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
    def valueOf(arg0: str) -> 'RotationType3D':
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$RotationType3D dev.ultreon.quantum.world.gen.noise.FastNoiseLite$RotationType3D.valueOf(java.lang.String)"""
        return RotationType3D.__wrap(__RotationType3D.valueOf(arg0))

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
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.FastNoiseLite$Vector3
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.world.gen.noise.FastNoiseLite as __FastNoiseLite_Vector3
__Vector3 = __FastNoiseLite_Vector3.Vector3
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
from builtins import int
 
class Vector3():
    """dev.ultreon.quantum.world.gen.noise.FastNoiseLite.Vector3"""
 
    @staticmethod
    def __wrap(java_value: __Vector3) -> 'Vector3':
        return Vector3(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Vector3):
        """
        Dynamic initializer for Vector3.
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
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public dev.ultreon.quantum.world.gen.noise.FastNoiseLite$Vector3(double,double,double)"""
        val = __Vector3(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))
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
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.FastNoiseLite
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import dev.ultreon.quantum.world.gen.noise.FastNoiseLite as __FastNoiseLite
__FastNoiseLite = __FastNoiseLite
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FastNoiseLite():
    """dev.ultreon.quantum.world.gen.noise.FastNoiseLite"""
 
    @staticmethod
    def __wrap(java_value: __FastNoiseLite) -> 'FastNoiseLite':
        return FastNoiseLite(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FastNoiseLite):
        """
        Dynamic initializer for FastNoiseLite.
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
    def SetCellularReturnType(self, arg0: 'CellularReturnType'):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetCellularReturnType(dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularReturnType)"""
        super(__FastNoiseLite, self).SetCellularReturnType(arg0)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.gen.noise.FastNoiseLite()"""
        val = __FastNoiseLite()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def SetFractalWeightedStrength(self, arg0: float):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetFractalWeightedStrength(double)"""
        super(__FastNoiseLite, self).SetFractalWeightedStrength(__double.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.world.gen.noise.FastNoiseLite(long)"""
        val = __FastNoiseLite(__long.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def SetFrequency(self, arg0: float):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetFrequency(double)"""
        super(__FastNoiseLite, self).SetFrequency(__double.valueOf(arg0))

    @overload
    def GetNoise(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.FastNoiseLite.GetNoise(double,double)"""
        return float.__wrap(super(__FastNoiseLite, self).GetNoise(__double.valueOf(arg0), __double.valueOf(arg1)))

    @overload
    def SetNoiseType(self, arg0: 'NoiseType'):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetNoiseType(dev.ultreon.quantum.world.gen.noise.FastNoiseLite$NoiseType)"""
        super(__FastNoiseLite, self).SetNoiseType(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.gen.noise.FastNoiseLite()"""
        val = __FastNoiseLite()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def SetFractalPingPongStrength(self, arg0: float):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetFractalPingPongStrength(double)"""
        super(__FastNoiseLite, self).SetFractalPingPongStrength(__double.valueOf(arg0))

    @overload
    def SetDomainWarpType(self, arg0: 'DomainWarpType'):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetDomainWarpType(dev.ultreon.quantum.world.gen.noise.FastNoiseLite$DomainWarpType)"""
        super(__FastNoiseLite, self).SetDomainWarpType(arg0)

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
    def SetFractalLacunarity(self, arg0: float):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetFractalLacunarity(double)"""
        super(__FastNoiseLite, self).SetFractalLacunarity(__double.valueOf(arg0))

    @overload
    def DomainWarp(self, arg0: 'Vector2'):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.DomainWarp(dev.ultreon.quantum.world.gen.noise.FastNoiseLite$Vector2)"""
        super(__FastNoiseLite, self).DomainWarp(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def GetNoise(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.FastNoiseLite.GetNoise(double,double,double)"""
        return float.__wrap(super(__FastNoiseLite, self).GetNoise(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def SetCellularJitter(self, arg0: float):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetCellularJitter(double)"""
        super(__FastNoiseLite, self).SetCellularJitter(__double.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def SetDomainWarpAmp(self, arg0: float):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetDomainWarpAmp(double)"""
        super(__FastNoiseLite, self).SetDomainWarpAmp(__double.valueOf(arg0))

    @overload
    def SetFractalType(self, arg0: 'FractalType'):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetFractalType(dev.ultreon.quantum.world.gen.noise.FastNoiseLite$FractalType)"""
        super(__FastNoiseLite, self).SetFractalType(arg0)

    @overload
    def SetFractalOctaves(self, arg0: int):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetFractalOctaves(long)"""
        super(__FastNoiseLite, self).SetFractalOctaves(__long.valueOf(arg0))

    @overload
    def DomainWarp(self, arg0: 'Vector3'):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.DomainWarp(dev.ultreon.quantum.world.gen.noise.FastNoiseLite$Vector3)"""
        super(__FastNoiseLite, self).DomainWarp(arg0)

    @overload
    def SetSeed(self, arg0: int):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetSeed(long)"""
        super(__FastNoiseLite, self).SetSeed(__long.valueOf(arg0))

    @overload
    def SetCellularDistanceFunction(self, arg0: 'CellularDistanceFunction'):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetCellularDistanceFunction(dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularDistanceFunction)"""
        super(__FastNoiseLite, self).SetCellularDistanceFunction(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def SetFractalGain(self, arg0: float):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetFractalGain(double)"""
        super(__FastNoiseLite, self).SetFractalGain(__double.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def SetRotationType3D(self, arg0: 'RotationType3D'):
        """public void dev.ultreon.quantum.world.gen.noise.FastNoiseLite.SetRotationType3D(dev.ultreon.quantum.world.gen.noise.FastNoiseLite$RotationType3D)"""
        super(__FastNoiseLite, self).SetRotationType3D(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.NoiseUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.world.gen.noise.NoiseUtils as __NoiseUtils
__NoiseUtils = __NoiseUtils
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NoiseUtils():
    """dev.ultreon.quantum.world.gen.noise.NoiseUtils"""
 
    @staticmethod
    def __wrap(java_value: __NoiseUtils) -> 'NoiseUtils':
        return NoiseUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NoiseUtils):
        """
        Dynamic initializer for NoiseUtils.
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

    @staticmethod
    @overload
    def remapValue(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float) -> float:
        """public static double dev.ultreon.quantum.world.gen.noise.NoiseUtils.remapValue(double,double,double,double,double)"""
        return float.__wrap(__NoiseUtils.remapValue(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3), __double.valueOf(arg4)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def redistribution(arg0: float, arg1: 'NoiseInstance') -> float:
        """public static double dev.ultreon.quantum.world.gen.noise.NoiseUtils.redistribution(double,dev.ultreon.quantum.world.gen.noise.NoiseInstance)"""
        return float.__wrap(__NoiseUtils.redistribution(__double.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def remapValue01(arg0: float, arg1: float, arg2: float) -> float:
        """public static double dev.ultreon.quantum.world.gen.noise.NoiseUtils.remapValue01(double,double,double)"""
        return float.__wrap(__NoiseUtils.remapValue01(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

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

    @staticmethod
    @overload
    def octavePerlin(arg0: float, arg1: float, arg2: 'NoiseInstance') -> float:
        """public static double dev.ultreon.quantum.world.gen.noise.NoiseUtils.octavePerlin(double,double,dev.ultreon.quantum.world.gen.noise.NoiseInstance)"""
        return float.__wrap(__NoiseUtils.octavePerlin(__double.valueOf(arg0), __double.valueOf(arg1), arg2))

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

    @staticmethod
    @overload
    def remapValue01ToInt(arg0: float, arg1: float, arg2: float) -> int:
        """public static int dev.ultreon.quantum.world.gen.noise.NoiseUtils.remapValue01ToInt(double,double,double)"""
        return int.__wrap(__NoiseUtils.remapValue01ToInt(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.FastNoiseLite$FractalType
from builtins import str
import dev.ultreon.quantum.world.gen.noise.FastNoiseLite as __FastNoiseLite_FractalType
__FractalType = __FastNoiseLite_FractalType.FractalType
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
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class FractalType():
    """dev.ultreon.quantum.world.gen.noise.FastNoiseLite.FractalType"""
 
    @staticmethod
    def __wrap(java_value: __FractalType) -> 'FractalType':
        return FractalType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FractalType):
        """
        Dynamic initializer for FractalType.
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
 
    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$FractalType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$FractalType.DomainWarpProgressive
    DomainWarpProgressive: 'FractalType' = __wrap(__FractalType.DomainWarpProgressive)

    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$FractalType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$FractalType.PingPong
    PingPong: 'FractalType' = __wrap(__FractalType.PingPong)

    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$FractalType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$FractalType.DomainWarpIndependent
    DomainWarpIndependent: 'FractalType' = __wrap(__FractalType.DomainWarpIndependent)

    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$FractalType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$FractalType.None
    None: 'FractalType' = __wrap(__FractalType.None)

    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$FractalType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$FractalType.FBm
    FBm: 'FractalType' = __wrap(__FractalType.FBm)

    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$FractalType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$FractalType.Ridged
    Ridged: 'FractalType' = __wrap(__FractalType.Ridged)


    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'FractalType':
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$FractalType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$FractalType.valueOf(java.lang.String)"""
        return FractalType.__wrap(__FractalType.valueOf(arg0))

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
    def values() -> List['FractalType']:
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$FractalType[] dev.ultreon.quantum.world.gen.noise.FastNoiseLite$FractalType.values()"""
        return List[FractalType].__wrap(__FractalType.values()) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularDistanceFunction
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import dev.ultreon.quantum.world.gen.noise.FastNoiseLite as __FastNoiseLite_CellularDistanceFunction
__CellularDistanceFunction = __FastNoiseLite_CellularDistanceFunction.CellularDistanceFunction
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
 
class CellularDistanceFunction():
    """dev.ultreon.quantum.world.gen.noise.FastNoiseLite.CellularDistanceFunction"""
 
    @staticmethod
    def __wrap(java_value: __CellularDistanceFunction) -> 'CellularDistanceFunction':
        return CellularDistanceFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CellularDistanceFunction):
        """
        Dynamic initializer for CellularDistanceFunction.
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
 
    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularDistanceFunction dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularDistanceFunction.Euclidean
    Euclidean: 'CellularDistanceFunction' = __wrap(__CellularDistanceFunction.Euclidean)

    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularDistanceFunction dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularDistanceFunction.Hybrid
    Hybrid: 'CellularDistanceFunction' = __wrap(__CellularDistanceFunction.Hybrid)

    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularDistanceFunction dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularDistanceFunction.EuclideanSq
    EuclideanSq: 'CellularDistanceFunction' = __wrap(__CellularDistanceFunction.EuclideanSq)

    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularDistanceFunction dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularDistanceFunction.Manhattan
    Manhattan: 'CellularDistanceFunction' = __wrap(__CellularDistanceFunction.Manhattan)


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
    def values() -> List['CellularDistanceFunction']:
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularDistanceFunction[] dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularDistanceFunction.values()"""
        return List[CellularDistanceFunction].__wrap(__CellularDistanceFunction.values())

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
    def valueOf(arg0: str) -> 'CellularDistanceFunction':
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularDistanceFunction dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularDistanceFunction.valueOf(java.lang.String)"""
        return CellularDistanceFunction.__wrap(__CellularDistanceFunction.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.SimplexNoise$Octave
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import dev.ultreon.quantum.world.gen.noise.SimplexNoise as __SimplexNoise_Octave
__Octave = __SimplexNoise_Octave.Octave
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Octave():
    """dev.ultreon.quantum.world.gen.noise.SimplexNoise.Octave"""
 
    @staticmethod
    def __wrap(java_value: __Octave) -> 'Octave':
        return Octave(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Octave):
        """
        Dynamic initializer for Octave.
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
    def noise(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.SimplexNoise$Octave.noise(double,double)"""
        return float.__wrap(super(__Octave, self).noise(__double.valueOf(arg0), __double.valueOf(arg1)))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.world.gen.noise.SimplexNoise$Octave(int)"""
        val = __Octave(__int.valueOf(arg0))
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
    def noise(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.SimplexNoise$Octave.noise(double,double,double,double)"""
        return float.__wrap(super(__Octave, self).noise(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3)))

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
    def noise(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.SimplexNoise$Octave.noise(double,double,double)"""
        return float.__wrap(super(__Octave, self).noise(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

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
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.SimplexNoise
from builtins import str
import dev.ultreon.quantum.world.gen.noise.SimplexNoise as __SimplexNoise
__SimplexNoise = __SimplexNoise
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SimplexNoise():
    """dev.ultreon.quantum.world.gen.noise.SimplexNoise"""
 
    @staticmethod
    def __wrap(java_value: __SimplexNoise) -> 'SimplexNoise':
        return SimplexNoise(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SimplexNoise):
        """
        Dynamic initializer for SimplexNoise.
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
    def eval(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.SimplexNoise.eval(double,double,double)"""
        return float.__wrap(super(__SimplexNoise, self).eval(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.noise.SimplexNoise.dispose()"""
        super(SimplexNoise, self).dispose()

    @overload
    def __init__(self, arg0: int, arg1: float, arg2: int):
        """public dev.ultreon.quantum.world.gen.noise.SimplexNoise(int,double,long)"""
        val = __SimplexNoise(__int.valueOf(arg0), __double.valueOf(arg1), __long.valueOf(arg2))
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
    def eval(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.SimplexNoise.eval(double,double)"""
        return float.__wrap(super(__SimplexNoise, self).eval(__double.valueOf(arg0), __double.valueOf(arg1)))

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
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.NoiseConfig
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.libs.commons.v0.vector.Vec2f as __Vec2f
__Vec2f = __Vec2f
from builtins import type
from builtins import float
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import dev.ultreon.quantum.world.gen.noise.NoiseConfig as __NoiseConfig
__NoiseConfig = __NoiseConfig
import dev.ultreon.quantum.world.gen.noise.NoiseInstance as __NoiseInstance
__NoiseInstance = __NoiseInstance
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
 
class NoiseConfig():
    """dev.ultreon.quantum.world.gen.noise.NoiseConfig"""
 
    @staticmethod
    def __wrap(java_value: __NoiseConfig) -> 'NoiseConfig':
        return NoiseConfig(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NoiseConfig):
        """
        Dynamic initializer for NoiseConfig.
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
    def octaves(self) -> float:
        """public float dev.ultreon.quantum.world.gen.noise.NoiseConfig.octaves()"""
        return float.__wrap(super(NoiseConfig, self).octaves())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.noise.NoiseConfig.equals(java.lang.Object)"""
        return bool.__wrap(super(__NoiseConfig, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.world.gen.noise.NoiseConfig.hashCode()"""
        return int.__wrap(super(NoiseConfig, self).hashCode())

    @overload
    def exponent(self) -> float:
        """public float dev.ultreon.quantum.world.gen.noise.NoiseConfig.exponent()"""
        return float.__wrap(super(NoiseConfig, self).exponent())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def create(self, arg0: int) -> 'NoiseInstance':
        """public dev.ultreon.quantum.world.gen.noise.NoiseInstance dev.ultreon.quantum.world.gen.noise.NoiseConfig.create(long)"""
        return 'NoiseInstance'.__wrap(super(__NoiseConfig, self).create(__long.valueOf(arg0)))

    @overload
    def offset(self) -> 'vector.Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.quantum.world.gen.noise.NoiseConfig.offset()"""
        return 'vector.Vec2f'.__wrap(super(NoiseConfig, self).offset())

    @overload
    def persistence(self) -> float:
        """public float dev.ultreon.quantum.world.gen.noise.NoiseConfig.persistence()"""
        return float.__wrap(super(NoiseConfig, self).persistence())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def redistributionModifier(self) -> float:
        """public float dev.ultreon.quantum.world.gen.noise.NoiseConfig.redistributionModifier()"""
        return float.__wrap(super(NoiseConfig, self).redistributionModifier())

    @overload
    def seed(self) -> int:
        """public long dev.ultreon.quantum.world.gen.noise.NoiseConfig.seed()"""
        return int.__wrap(super(NoiseConfig, self).seed())

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
    def __init__(self, arg0: float, arg1: float, arg2: 'Vec2f', arg3: int, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public dev.ultreon.quantum.world.gen.noise.NoiseConfig(float,float,dev.ultreon.libs.commons.v0.vector.Vec2f,long,float,float,float,float,float)"""
        val = __NoiseConfig(__float.valueOf(arg0), __float.valueOf(arg1), arg2, __long.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def noiseZoom(self) -> float:
        """public float dev.ultreon.quantum.world.gen.noise.NoiseConfig.noiseZoom()"""
        return float.__wrap(super(NoiseConfig, self).noiseZoom())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.world.gen.noise.NoiseConfig.toString()"""
        return str.__wrap(super(NoiseConfig, self).toString()) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.NoiseType
import dev.ultreon.quantum.server.ServerDisposable as __ServerDisposable
__ServerDisposable = __ServerDisposable
import dev.ultreon.quantum.world.gen.noise.NoiseType as __NoiseType
__NoiseType = __NoiseType
from abc import abstractmethod, ABC
 
class NoiseType(ABC):
    """dev.ultreon.quantum.world.gen.noise.NoiseType"""
 
    @staticmethod
    def __wrap(java_value: __NoiseType) -> 'NoiseType':
        return NoiseType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NoiseType):
        """
        Dynamic initializer for NoiseType.
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
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.libs.commons.v0.vector.Vec2f as __Vec2f
__Vec2f = __Vec2f
from builtins import type
from builtins import float
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import dev.ultreon.quantum.world.gen.noise.NoiseInstance as __NoiseInstance
__NoiseInstance = __NoiseInstance
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NoiseInstance():
    """dev.ultreon.quantum.world.gen.noise.NoiseInstance"""
 
    @staticmethod
    def __wrap(java_value: __NoiseInstance) -> 'NoiseInstance':
        return NoiseInstance(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NoiseInstance):
        """
        Dynamic initializer for NoiseInstance.
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
    def eval(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.NoiseInstance.eval(double,double,double)"""
        return float.__wrap(super(__NoiseInstance, self).eval(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def octaves(self) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.NoiseInstance.octaves()"""
        return float.__wrap(super(NoiseInstance, self).octaves())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.noise.NoiseInstance.dispose()"""
        super(NoiseInstance, self).dispose()

    @overload
    def noiseZoom(self) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.NoiseInstance.noiseZoom()"""
        return float.__wrap(super(NoiseInstance, self).noiseZoom())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def exponent(self) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.NoiseInstance.exponent()"""
        return float.__wrap(super(NoiseInstance, self).exponent())

    @overload
    def eval(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.NoiseInstance.eval(double,double)"""
        return float.__wrap(super(__NoiseInstance, self).eval(__double.valueOf(arg0), __double.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def redistributionModifier(self) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.NoiseInstance.redistributionModifier()"""
        return float.__wrap(super(NoiseInstance, self).redistributionModifier())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def persistence(self) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.NoiseInstance.persistence()"""
        return float.__wrap(super(NoiseInstance, self).persistence())

    @overload
    def seed(self) -> int:
        """public long dev.ultreon.quantum.world.gen.noise.NoiseInstance.seed()"""
        return int.__wrap(super(NoiseInstance, self).seed())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'NoiseType', arg1: int, arg2: float, arg3: float, arg4: 'Vec2f', arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public dev.ultreon.quantum.world.gen.noise.NoiseInstance(dev.ultreon.quantum.world.gen.noise.NoiseType,long,double,double,dev.ultreon.libs.commons.v0.vector.Vec2f,double,double,double,double,double)"""
        val = __NoiseInstance(arg0, __long.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3), arg4, __double.valueOf(arg5), __double.valueOf(arg6), __double.valueOf(arg7), __double.valueOf(arg8), __double.valueOf(arg9))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'NoiseType', arg1: int):
        """public dev.ultreon.quantum.world.gen.noise.NoiseInstance(dev.ultreon.quantum.world.gen.noise.NoiseType,long)"""
        val = __NoiseInstance(arg0, __long.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def amplitude(self) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.NoiseInstance.amplitude()"""
        return float.__wrap(super(NoiseInstance, self).amplitude())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def offset(self) -> 'vector.Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.quantum.world.gen.noise.NoiseInstance.offset()"""
        return 'vector.Vec2f'.__wrap(super(NoiseInstance, self).offset())

    @overload
    def base(self) -> float:
        """public double dev.ultreon.quantum.world.gen.noise.NoiseInstance.base()"""
        return float.__wrap(super(NoiseInstance, self).base())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularReturnType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import dev.ultreon.quantum.world.gen.noise.FastNoiseLite as __FastNoiseLite_CellularReturnType
__CellularReturnType = __FastNoiseLite_CellularReturnType.CellularReturnType
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
 
class CellularReturnType():
    """dev.ultreon.quantum.world.gen.noise.FastNoiseLite.CellularReturnType"""
 
    @staticmethod
    def __wrap(java_value: __CellularReturnType) -> 'CellularReturnType':
        return CellularReturnType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CellularReturnType):
        """
        Dynamic initializer for CellularReturnType.
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
 
    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularReturnType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularReturnType.Distance2Add
    Distance2Add: 'CellularReturnType' = __wrap(__CellularReturnType.Distance2Add)

    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularReturnType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularReturnType.Distance2Sub
    Distance2Sub: 'CellularReturnType' = __wrap(__CellularReturnType.Distance2Sub)

    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularReturnType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularReturnType.Distance2Mul
    Distance2Mul: 'CellularReturnType' = __wrap(__CellularReturnType.Distance2Mul)

    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularReturnType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularReturnType.Distance2
    Distance2: 'CellularReturnType' = __wrap(__CellularReturnType.Distance2)

    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularReturnType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularReturnType.CellValue
    CellValue: 'CellularReturnType' = __wrap(__CellularReturnType.CellValue)

    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularReturnType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularReturnType.Distance
    Distance: 'CellularReturnType' = __wrap(__CellularReturnType.Distance)

    # public static final dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularReturnType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularReturnType.Distance2Div
    Distance2Div: 'CellularReturnType' = __wrap(__CellularReturnType.Distance2Div)


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
    def values() -> List['CellularReturnType']:
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularReturnType[] dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularReturnType.values()"""
        return List[CellularReturnType].__wrap(__CellularReturnType.values())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'CellularReturnType':
        """public static dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularReturnType dev.ultreon.quantum.world.gen.noise.FastNoiseLite$CellularReturnType.valueOf(java.lang.String)"""
        return CellularReturnType.__wrap(__CellularReturnType.valueOf(arg0))

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
 
 
# CLASS: dev.ultreon.quantum.world.gen.noise.FastNoiseLite$Vector2
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.world.gen.noise.FastNoiseLite as __FastNoiseLite_Vector2
__Vector2 = __FastNoiseLite_Vector2.Vector2
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
from builtins import int
 
class Vector2():
    """dev.ultreon.quantum.world.gen.noise.FastNoiseLite.Vector2"""
 
    @staticmethod
    def __wrap(java_value: __Vector2) -> 'Vector2':
        return Vector2(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Vector2):
        """
        Dynamic initializer for Vector2.
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

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public dev.ultreon.quantum.world.gen.noise.FastNoiseLite$Vector2(double,double)"""
        val = __Vector2(__double.valueOf(arg0), __double.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val