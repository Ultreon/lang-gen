from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

from builtins import type
try:
    from pyquantum.world.gen import noise
except ImportError:
    noise = __import_once__("pyquantum.world.gen.noise")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.world.gen.feature.PatchFeature as __PatchFeature
__PatchFeature = __PatchFeature
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PatchFeature():
    """dev.ultreon.quantum.world.gen.feature.PatchFeature"""
 
    @staticmethod
    def __wrap(java_value: __PatchFeature) -> 'PatchFeature':
        return PatchFeature(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PatchFeature):
        """
        Dynamic initializer for PatchFeature.
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
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.feature.PatchFeature.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(__PatchFeature, self).create(arg0)

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
    def __init__(self, arg0: 'NoiseConfig', arg1: 'Block', arg2: float, arg3: int):
        """public dev.ultreon.quantum.world.gen.feature.PatchFeature(dev.ultreon.quantum.world.gen.noise.NoiseConfig,dev.ultreon.quantum.block.Block,float,int)"""
        val = __PatchFeature(arg0, arg1, __float.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def handle(self, arg0: 'World', arg1: 'ChunkAccess', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.PatchFeature.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.ChunkAccess,int,int,int)"""
        return bool.__wrap(super(__PatchFeature, self).handle(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

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
    def __init__(self, arg0: 'NoiseConfig', arg1: 'Block', arg2: float):
        """public dev.ultreon.quantum.world.gen.feature.PatchFeature(dev.ultreon.quantum.world.gen.noise.NoiseConfig,dev.ultreon.quantum.block.Block,float)"""
        val = __PatchFeature(arg0, arg1, __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.feature.PatchFeature.dispose()"""
        super(PatchFeature, self).dispose()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.world.gen.feature.PatchFeature
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

from builtins import type
try:
    from pyquantum.world.gen import noise
except ImportError:
    noise = __import_once__("pyquantum.world.gen.noise")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.world.gen.feature.PatchFeature as __PatchFeature
__PatchFeature = __PatchFeature
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PatchFeature():
    """dev.ultreon.quantum.world.gen.feature.PatchFeature"""
 
    @staticmethod
    def __wrap(java_value: __PatchFeature) -> 'PatchFeature':
        return PatchFeature(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PatchFeature):
        """
        Dynamic initializer for PatchFeature.
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
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.feature.PatchFeature.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(__PatchFeature, self).create(arg0)

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
    def __init__(self, arg0: 'NoiseConfig', arg1: 'Block', arg2: float, arg3: int):
        """public dev.ultreon.quantum.world.gen.feature.PatchFeature(dev.ultreon.quantum.world.gen.noise.NoiseConfig,dev.ultreon.quantum.block.Block,float,int)"""
        val = __PatchFeature(arg0, arg1, __float.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def handle(self, arg0: 'World', arg1: 'ChunkAccess', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.PatchFeature.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.ChunkAccess,int,int,int)"""
        return bool.__wrap(super(__PatchFeature, self).handle(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

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
    def __init__(self, arg0: 'NoiseConfig', arg1: 'Block', arg2: float):
        """public dev.ultreon.quantum.world.gen.feature.PatchFeature(dev.ultreon.quantum.world.gen.noise.NoiseConfig,dev.ultreon.quantum.block.Block,float)"""
        val = __PatchFeature(arg0, arg1, __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.feature.PatchFeature.dispose()"""
        super(PatchFeature, self).dispose()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.world.gen.feature.PatchFeature 
 
 
# CLASS: dev.ultreon.quantum.world.gen.feature.CactiFeature
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

import dev.ultreon.quantum.world.gen.feature.CactiFeature as __CactiFeature
__CactiFeature = __CactiFeature
from builtins import type
try:
    from pyquantum.world.gen import noise
except ImportError:
    noise = __import_once__("pyquantum.world.gen.noise")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.world.gen.WorldGenFeature as __WorldGenFeature
__WorldGenFeature = __WorldGenFeature
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CactiFeature():
    """dev.ultreon.quantum.world.gen.feature.CactiFeature"""
 
    @staticmethod
    def __wrap(java_value: __CactiFeature) -> 'CactiFeature':
        return CactiFeature(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CactiFeature):
        """
        Dynamic initializer for CactiFeature.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def handle(self, arg0: 'World', arg1: 'ChunkAccess', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.CactiFeature.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.ChunkAccess,int,int,int)"""
        return bool.__wrap(super(__CactiFeature, self).handle(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

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
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.feature.CactiFeature.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(__CactiFeature, self).create(arg0)

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.WorldGenFeature.dispose()"""
        super(gen.WorldGenFeature, self).dispose()

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
    def __init__(self, arg0: 'NoiseConfig', arg1: 'Block', arg2: float, arg3: int, arg4: int):
        """public dev.ultreon.quantum.world.gen.feature.CactiFeature(dev.ultreon.quantum.world.gen.noise.NoiseConfig,dev.ultreon.quantum.block.Block,float,int,int)"""
        val = __CactiFeature(arg0, arg1, __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.feature.TreeFeature
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

from builtins import type
try:
    from pyquantum.world.gen import noise
except ImportError:
    noise = __import_once__("pyquantum.world.gen.noise")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import dev.ultreon.quantum.world.gen.feature.TreeFeature as __TreeFeature
__TreeFeature = __TreeFeature
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.world.gen.WorldGenFeature as __WorldGenFeature
__WorldGenFeature = __WorldGenFeature
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TreeFeature():
    """dev.ultreon.quantum.world.gen.feature.TreeFeature"""
 
    @staticmethod
    def __wrap(java_value: __TreeFeature) -> 'TreeFeature':
        return TreeFeature(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TreeFeature):
        """
        Dynamic initializer for TreeFeature.
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
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.feature.TreeFeature.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(__TreeFeature, self).create(arg0)

    @overload
    def handle(self, arg0: 'World', arg1: 'ChunkAccess', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.TreeFeature.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.ChunkAccess,int,int,int)"""
        return bool.__wrap(super(__TreeFeature, self).handle(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

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

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.WorldGenFeature.dispose()"""
        super(gen.WorldGenFeature, self).dispose()

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
    def __init__(self, arg0: 'NoiseConfig', arg1: 'Block', arg2: 'Block', arg3: float, arg4: int, arg5: int):
        """public dev.ultreon.quantum.world.gen.feature.TreeFeature(dev.ultreon.quantum.world.gen.noise.NoiseConfig,dev.ultreon.quantum.block.Block,dev.ultreon.quantum.block.Block,float,int,int)"""
        val = __TreeFeature(arg0, arg1, arg2, __float.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.feature.OreFeature
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

from builtins import type
import dev.ultreon.quantum.world.gen.feature.OreFeature as __OreFeature
__OreFeature = __OreFeature
import kotlin.ranges.IntRange as IntRange
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.world.gen.WorldGenFeature as __WorldGenFeature
__WorldGenFeature = __WorldGenFeature
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class OreFeature():
    """dev.ultreon.quantum.world.gen.feature.OreFeature"""
 
    @staticmethod
    def __wrap(java_value: __OreFeature) -> 'OreFeature':
        return OreFeature(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OreFeature):
        """
        Dynamic initializer for OreFeature.
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
    def handle(self, arg0: 'World', arg1: 'ChunkAccess', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.OreFeature.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.ChunkAccess,int,int,int)"""
        return bool.__wrap(super(__OreFeature, self).handle(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int, arg1: 'Block', arg2: int, arg3: 'IntRange', arg4: 'IntRange'):
        """public dev.ultreon.quantum.world.gen.feature.OreFeature(long,dev.ultreon.quantum.block.Block,int,kotlin.ranges.IntRange,kotlin.ranges.IntRange)"""
        val = __OreFeature(__long.valueOf(arg0), arg1, __int.valueOf(arg2), arg3, arg4)
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

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.WorldGenFeature.dispose()"""
        super(gen.WorldGenFeature, self).dispose()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.feature.OreFeature.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(__OreFeature, self).create(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.world.gen.feature.DefaultedArray
import java.util.ListIterator as __ListIterator
__ListIterator = __ListIterator
import java.util.function.Predicate as Predicate
import java.util.function.Supplier as Supplier
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import dev.ultreon.quantum.world.gen.feature.DefaultedArray as __DefaultedArray
__DefaultedArray = __DefaultedArray
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.util.List as __List
__List = __List
import java.util.ListIterator as ListIterator
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.util.List as List
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class DefaultedArray():
    """dev.ultreon.quantum.world.gen.feature.DefaultedArray"""
 
    @staticmethod
    def __wrap(java_value: __DefaultedArray) -> 'DefaultedArray':
        return DefaultedArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefaultedArray):
        """
        Dynamic initializer for DefaultedArray.
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
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.DefaultedArray.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__DefaultedArray, self).containsAll(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.DefaultedArray.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__DefaultedArray, self).retainAll(arg0))

    @overload
    def remove(self, arg0: int) -> object:
        """public T dev.ultreon.quantum.world.gen.feature.DefaultedArray.remove(int)"""
        return object.__wrap(super(__DefaultedArray, self).remove(__int.valueOf(arg0)))

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(__List, self).sort(arg0)

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(__List, self).addFirst(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(__List, self).replaceAll(arg0)

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int dev.ultreon.quantum.world.gen.feature.DefaultedArray.lastIndexOf(java.lang.Object)"""
        return int.__wrap(super(__DefaultedArray, self).lastIndexOf(arg0))

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<T> dev.ultreon.quantum.world.gen.feature.DefaultedArray.listIterator(int)"""
        return 'ListIterator'.__wrap(super(__DefaultedArray, self).listIterator(__int.valueOf(arg0)))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'.__wrap(super(List, self).spliterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object.__wrap(super(List, self).removeLast())

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(__List, self).addLast(arg0)

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.DefaultedArray.contains(java.lang.Object)"""
        return bool.__wrap(super(__DefaultedArray, self).contains(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.DefaultedArray.addAll(java.util.Collection<? extends T>)"""
        return bool.__wrap(super(__DefaultedArray, self).addAll(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int dev.ultreon.quantum.world.gen.feature.DefaultedArray.size()"""
        return int.__wrap(super(DefaultedArray, self).size())

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T1> T1[] dev.ultreon.quantum.world.gen.feature.DefaultedArray.toArray(T1[])"""
        return List[object].__wrap(super(__DefaultedArray, self).toArray(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.DefaultedArray.isEmpty()"""
        return bool.__wrap(super(DefaultedArray, self).isEmpty())

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<T> dev.ultreon.quantum.world.gen.feature.DefaultedArray.listIterator()"""
        return 'ListIterator'.__wrap(super(DefaultedArray, self).listIterator())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0))

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
    def subList(self, arg0: int, arg1: int) -> 'DefaultedArray':
        """public dev.ultreon.quantum.world.gen.feature.DefaultedArray<T> dev.ultreon.quantum.world.gen.feature.DefaultedArray.subList(int,int)"""
        return 'DefaultedArray'.__wrap(super(__DefaultedArray, self).subList(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def get(self, arg0: int) -> object:
        """public T dev.ultreon.quantum.world.gen.feature.DefaultedArray.get(int)"""
        return object.__wrap(super(__DefaultedArray, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> dev.ultreon.quantum.world.gen.feature.DefaultedArray.iterator()"""
        return 'Iterator'.__wrap(super(DefaultedArray, self).iterator())

    @overload
    def __init__(self, arg0: object, arg1: int):
        """public dev.ultreon.quantum.world.gen.feature.DefaultedArray(T,int)"""
        val = __DefaultedArray(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object.__wrap(super(List, self).getFirst())

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void dev.ultreon.quantum.world.gen.feature.DefaultedArray.add(int,T)"""
        super(__DefaultedArray, self).add(__int.valueOf(arg0), arg1)

    @overload
    def __init__(self, arg0: 'Supplier', arg1: int):
        """public dev.ultreon.quantum.world.gen.feature.DefaultedArray(java.util.function.Supplier<T>,int)"""
        val = __DefaultedArray(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object.__wrap(super(List, self).getLast())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.DefaultedArray.remove(java.lang.Object)"""
        return bool.__wrap(super(__DefaultedArray, self).remove(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.DefaultedArray.add(T)"""
        return bool.__wrap(super(__DefaultedArray, self).add(arg0))

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object.__wrap(super(List, self).removeFirst())

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int dev.ultreon.quantum.world.gen.feature.DefaultedArray.indexOf(java.lang.Object)"""
        return int.__wrap(super(__DefaultedArray, self).indexOf(arg0))

    @override
    @overload
    def clear(self):
        """public void dev.ultreon.quantum.world.gen.feature.DefaultedArray.clear()"""
        super(DefaultedArray, self).clear()

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.DefaultedArray.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__DefaultedArray, self).removeAll(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] dev.ultreon.quantum.world.gen.feature.DefaultedArray.toArray()"""
        return List[object].__wrap(super(DefaultedArray, self).toArray())

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
    def set(self, arg0: int, arg1: object) -> object:
        """public T dev.ultreon.quantum.world.gen.feature.DefaultedArray.set(int,T)"""
        return object.__wrap(super(__DefaultedArray, self).set(__int.valueOf(arg0), arg1))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'.__wrap(super(List, self).reversed())

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.DefaultedArray.addAll(int,java.util.Collection<? extends T>)"""
        return bool.__wrap(super(__DefaultedArray, self).addAll(__int.valueOf(arg0), arg1)) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.feature.RockFeature
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

from builtins import type
import dev.ultreon.quantum.world.gen.feature.RockFeature as __RockFeature
__RockFeature = __RockFeature
try:
    from pyquantum.world.gen import noise
except ImportError:
    noise = __import_once__("pyquantum.world.gen.noise")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.world.gen.WorldGenFeature as __WorldGenFeature
__WorldGenFeature = __WorldGenFeature
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RockFeature():
    """dev.ultreon.quantum.world.gen.feature.RockFeature"""
 
    @staticmethod
    def __wrap(java_value: __RockFeature) -> 'RockFeature':
        return RockFeature(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RockFeature):
        """
        Dynamic initializer for RockFeature.
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

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.WorldGenFeature.dispose()"""
        super(gen.WorldGenFeature, self).dispose()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def handle(self, arg0: 'World', arg1: 'ChunkAccess', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.RockFeature.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.ChunkAccess,int,int,int)"""
        return bool.__wrap(super(__RockFeature, self).handle(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @overload
    def __init__(self, arg0: 'NoiseConfig', arg1: 'Block', arg2: float):
        """public dev.ultreon.quantum.world.gen.feature.RockFeature(dev.ultreon.quantum.world.gen.noise.NoiseConfig,dev.ultreon.quantum.block.Block,float)"""
        val = __RockFeature(arg0, arg1, __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.feature.RockFeature.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(__RockFeature, self).create(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.feature.FoliageFeature
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

from builtins import type
import dev.ultreon.quantum.world.gen.feature.FoliageFeature as __FoliageFeature
__FoliageFeature = __FoliageFeature
try:
    from pyquantum.world.gen import noise
except ImportError:
    noise = __import_once__("pyquantum.world.gen.noise")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.world.gen.WorldGenFeature as __WorldGenFeature
__WorldGenFeature = __WorldGenFeature
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FoliageFeature():
    """dev.ultreon.quantum.world.gen.feature.FoliageFeature"""
 
    @staticmethod
    def __wrap(java_value: __FoliageFeature) -> 'FoliageFeature':
        return FoliageFeature(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FoliageFeature):
        """
        Dynamic initializer for FoliageFeature.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def handle(self, arg0: 'World', arg1: 'ChunkAccess', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.FoliageFeature.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.ChunkAccess,int,int,int)"""
        return bool.__wrap(super(__FoliageFeature, self).handle(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

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
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.feature.FoliageFeature.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(__FoliageFeature, self).create(arg0)

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.WorldGenFeature.dispose()"""
        super(gen.WorldGenFeature, self).dispose()

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
    def __init__(self, arg0: 'NoiseConfig', arg1: 'Block', arg2: float):
        """public dev.ultreon.quantum.world.gen.feature.FoliageFeature(dev.ultreon.quantum.world.gen.noise.NoiseConfig,dev.ultreon.quantum.block.Block,float)"""
        val = __FoliageFeature(arg0, arg1, __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val