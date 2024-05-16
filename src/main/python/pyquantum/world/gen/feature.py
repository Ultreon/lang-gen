from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.world.gen import noise
except ImportError:
    noise = _import_once("pyquantum.world.gen.noise")

import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import dev.ultreon.quantum.world.gen.feature.PatchFeature as _PatchFeature
_PatchFeature = _PatchFeature
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PatchFeature():
    """dev.ultreon.quantum.world.gen.feature.PatchFeature"""
 
    @staticmethod
    def _wrap(java_value: _PatchFeature) -> 'PatchFeature':
        return PatchFeature(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PatchFeature):
        """
        Dynamic initializer for PatchFeature.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PatchFeature__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PatchFeature__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def handle(self, arg0: 'World', arg1: 'ChunkAccess', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.PatchFeature.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.ChunkAccess,int,int,int)"""
        return bool._wrap(super(_PatchFeature, self).handle(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.feature.PatchFeature.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(_PatchFeature, self).create(arg0)

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
    def __init__(self, arg0: 'NoiseConfig', arg1: 'Block', arg2: float, arg3: int):
        """public dev.ultreon.quantum.world.gen.feature.PatchFeature(dev.ultreon.quantum.world.gen.noise.NoiseConfig,dev.ultreon.quantum.block.Block,float,int)"""
        val = _PatchFeature(arg0, arg1, _float.valueOf(arg2), _int.valueOf(arg3))
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
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.feature.PatchFeature.dispose()"""
        super(PatchFeature, self).dispose()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'NoiseConfig', arg1: 'Block', arg2: float):
        """public dev.ultreon.quantum.world.gen.feature.PatchFeature(dev.ultreon.quantum.world.gen.noise.NoiseConfig,dev.ultreon.quantum.block.Block,float)"""
        val = _PatchFeature(arg0, arg1, _float.valueOf(arg2))
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

 
 
 
# CLASS: dev.ultreon.quantum.world.gen.feature.PatchFeature
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.world.gen import noise
except ImportError:
    noise = _import_once("pyquantum.world.gen.noise")

import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import dev.ultreon.quantum.world.gen.feature.PatchFeature as _PatchFeature
_PatchFeature = _PatchFeature
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PatchFeature():
    """dev.ultreon.quantum.world.gen.feature.PatchFeature"""
 
    @staticmethod
    def _wrap(java_value: _PatchFeature) -> 'PatchFeature':
        return PatchFeature(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PatchFeature):
        """
        Dynamic initializer for PatchFeature.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PatchFeature__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PatchFeature__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def handle(self, arg0: 'World', arg1: 'ChunkAccess', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.PatchFeature.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.ChunkAccess,int,int,int)"""
        return bool._wrap(super(_PatchFeature, self).handle(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.feature.PatchFeature.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(_PatchFeature, self).create(arg0)

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
    def __init__(self, arg0: 'NoiseConfig', arg1: 'Block', arg2: float, arg3: int):
        """public dev.ultreon.quantum.world.gen.feature.PatchFeature(dev.ultreon.quantum.world.gen.noise.NoiseConfig,dev.ultreon.quantum.block.Block,float,int)"""
        val = _PatchFeature(arg0, arg1, _float.valueOf(arg2), _int.valueOf(arg3))
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
    def dispose(self):
        """public void dev.ultreon.quantum.world.gen.feature.PatchFeature.dispose()"""
        super(PatchFeature, self).dispose()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'NoiseConfig', arg1: 'Block', arg2: float):
        """public dev.ultreon.quantum.world.gen.feature.PatchFeature(dev.ultreon.quantum.world.gen.noise.NoiseConfig,dev.ultreon.quantum.block.Block,float)"""
        val = _PatchFeature(arg0, arg1, _float.valueOf(arg2))
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

 
 
 
# CLASS: dev.ultreon.quantum.world.gen.feature.PatchFeature 
 
 
# CLASS: dev.ultreon.quantum.world.gen.feature.CactiFeature
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.world.gen.feature.CactiFeature as _CactiFeature
_CactiFeature = _CactiFeature
try:
    from pyquantum.world.gen import noise
except ImportError:
    noise = _import_once("pyquantum.world.gen.noise")

import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.world.gen.WorldGenFeature as _WorldGenFeature
_WorldGenFeature = _WorldGenFeature
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CactiFeature():
    """dev.ultreon.quantum.world.gen.feature.CactiFeature"""
 
    @staticmethod
    def _wrap(java_value: _CactiFeature) -> 'CactiFeature':
        return CactiFeature(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CactiFeature):
        """
        Dynamic initializer for CactiFeature.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CactiFeature__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CactiFeature__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.feature.CactiFeature.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(_CactiFeature, self).create(arg0)

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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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
        """public boolean dev.ultreon.quantum.world.gen.feature.CactiFeature.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.ChunkAccess,int,int,int)"""
        return bool._wrap(super(_CactiFeature, self).handle(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

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
    def __init__(self, arg0: 'NoiseConfig', arg1: 'Block', arg2: float, arg3: int, arg4: int):
        """public dev.ultreon.quantum.world.gen.feature.CactiFeature(dev.ultreon.quantum.world.gen.noise.NoiseConfig,dev.ultreon.quantum.block.Block,float,int,int)"""
        val = _CactiFeature(arg0, arg1, _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))
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
 
 
# CLASS: dev.ultreon.quantum.world.gen.feature.TreeFeature
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.world.gen import noise
except ImportError:
    noise = _import_once("pyquantum.world.gen.noise")

import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import dev.ultreon.quantum.world.gen.feature.TreeFeature as _TreeFeature
_TreeFeature = _TreeFeature
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.world.gen.WorldGenFeature as _WorldGenFeature
_WorldGenFeature = _WorldGenFeature
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TreeFeature():
    """dev.ultreon.quantum.world.gen.feature.TreeFeature"""
 
    @staticmethod
    def _wrap(java_value: _TreeFeature) -> 'TreeFeature':
        return TreeFeature(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TreeFeature):
        """
        Dynamic initializer for TreeFeature.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TreeFeature__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TreeFeature__wrapper":
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
    def __init__(self, arg0: 'NoiseConfig', arg1: 'Block', arg2: 'Block', arg3: float, arg4: int, arg5: int):
        """public dev.ultreon.quantum.world.gen.feature.TreeFeature(dev.ultreon.quantum.world.gen.noise.NoiseConfig,dev.ultreon.quantum.block.Block,dev.ultreon.quantum.block.Block,float,int,int)"""
        val = _TreeFeature(arg0, arg1, arg2, _float.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))
        self.__wrapper = val

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
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.feature.TreeFeature.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(_TreeFeature, self).create(arg0)

    @overload
    def handle(self, arg0: 'World', arg1: 'ChunkAccess', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.TreeFeature.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.ChunkAccess,int,int,int)"""
        return bool._wrap(super(_TreeFeature, self).handle(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.feature.OreFeature
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
import dev.ultreon.quantum.world.gen.feature.OreFeature as _OreFeature
_OreFeature = _OreFeature
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import kotlin.ranges.IntRange as IntRange
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.world.gen.WorldGenFeature as _WorldGenFeature
_WorldGenFeature = _WorldGenFeature
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class OreFeature():
    """dev.ultreon.quantum.world.gen.feature.OreFeature"""
 
    @staticmethod
    def _wrap(java_value: _OreFeature) -> 'OreFeature':
        return OreFeature(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OreFeature):
        """
        Dynamic initializer for OreFeature.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OreFeature__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OreFeature__wrapper":
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
    def handle(self, arg0: 'World', arg1: 'ChunkAccess', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.OreFeature.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.ChunkAccess,int,int,int)"""
        return bool._wrap(super(_OreFeature, self).handle(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: int, arg1: 'Block', arg2: int, arg3: 'IntRange', arg4: 'IntRange'):
        """public dev.ultreon.quantum.world.gen.feature.OreFeature(long,dev.ultreon.quantum.block.Block,int,kotlin.ranges.IntRange,kotlin.ranges.IntRange)"""
        val = _OreFeature(_long.valueOf(arg0), arg1, _int.valueOf(arg2), arg3, arg4)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.feature.OreFeature.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(_OreFeature, self).create(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.feature.DefaultedArray
import java.util.function.Predicate as Predicate
import java.util.function.Supplier as Supplier
import java.lang.Object as _Object
_Object = _Object
import java.util.ListIterator as _ListIterator
_ListIterator = _ListIterator
from builtins import type
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.Iterator as Iterator
from typing import List
import dev.ultreon.quantum.world.gen.feature.DefaultedArray as _DefaultedArray
_DefaultedArray = _DefaultedArray
import java.util.Comparator as Comparator
import java.util.ListIterator as ListIterator
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.util.List as List
 
class DefaultedArray():
    """dev.ultreon.quantum.world.gen.feature.DefaultedArray"""
 
    @staticmethod
    def _wrap(java_value: _DefaultedArray) -> 'DefaultedArray':
        return DefaultedArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DefaultedArray):
        """
        Dynamic initializer for DefaultedArray.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DefaultedArray__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DefaultedArray__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public default void java.util.List.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(_List, self).replaceAll(arg0)

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.List.getFirst()"""
        return object._wrap(super(List, self).getFirst())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.DefaultedArray.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_DefaultedArray, self).retainAll(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.List.removeLast()"""
        return object._wrap(super(List, self).removeLast())

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<T> dev.ultreon.quantum.world.gen.feature.DefaultedArray.listIterator(int)"""
        return 'ListIterator'._wrap(super(_DefaultedArray, self).listIterator(_int.valueOf(arg0)))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.DefaultedArray.add(T)"""
        return bool._wrap(super(_DefaultedArray, self).add(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T1> T1[] dev.ultreon.quantum.world.gen.feature.DefaultedArray.toArray(T1[])"""
        return List[object]._wrap(super(_DefaultedArray, self).toArray(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.DefaultedArray.contains(java.lang.Object)"""
        return bool._wrap(super(_DefaultedArray, self).contains(arg0))

    @overload
    def __init__(self, arg0: object, arg1: int):
        """public dev.ultreon.quantum.world.gen.feature.DefaultedArray(T,int)"""
        val = _DefaultedArray(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int dev.ultreon.quantum.world.gen.feature.DefaultedArray.indexOf(java.lang.Object)"""
        return int._wrap(super(_DefaultedArray, self).indexOf(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.DefaultedArray.isEmpty()"""
        return bool._wrap(super(DefaultedArray, self).isEmpty())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> dev.ultreon.quantum.world.gen.feature.DefaultedArray.iterator()"""
        return 'Iterator'._wrap(super(DefaultedArray, self).iterator())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.List.removeFirst()"""
        return object._wrap(super(List, self).removeFirst())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def remove(self, arg0: int) -> object:
        """public T dev.ultreon.quantum.world.gen.feature.DefaultedArray.remove(int)"""
        return object._wrap(super(_DefaultedArray, self).remove(_int.valueOf(arg0)))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.List.spliterator()"""
        return 'Spliterator'._wrap(super(List, self).spliterator())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] dev.ultreon.quantum.world.gen.feature.DefaultedArray.toArray()"""
        return List[object]._wrap(super(DefaultedArray, self).toArray())

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public T dev.ultreon.quantum.world.gen.feature.DefaultedArray.set(int,T)"""
        return object._wrap(super(_DefaultedArray, self).set(_int.valueOf(arg0), arg1))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.DefaultedArray.remove(java.lang.Object)"""
        return bool._wrap(super(_DefaultedArray, self).remove(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def get(self, arg0: int) -> object:
        """public T dev.ultreon.quantum.world.gen.feature.DefaultedArray.get(int)"""
        return object._wrap(super(_DefaultedArray, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public default void java.util.List.sort(java.util.Comparator<? super E>)"""
        super(_List, self).sort(arg0)

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int dev.ultreon.quantum.world.gen.feature.DefaultedArray.lastIndexOf(java.lang.Object)"""
        return int._wrap(super(_DefaultedArray, self).lastIndexOf(arg0))

    @overload
    def __init__(self, arg0: 'Supplier', arg1: int):
        """public dev.ultreon.quantum.world.gen.feature.DefaultedArray(java.util.function.Supplier<T>,int)"""
        val = _DefaultedArray(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.List.getLast()"""
        return object._wrap(super(List, self).getLast())

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.List.addFirst(E)"""
        super(_List, self).addFirst(arg0)

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.DefaultedArray.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_DefaultedArray, self).removeAll(arg0))

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void dev.ultreon.quantum.world.gen.feature.DefaultedArray.add(int,T)"""
        super(_DefaultedArray, self).add(_int.valueOf(arg0), arg1)

    @override
    @overload
    def size(self) -> int:
        """public int dev.ultreon.quantum.world.gen.feature.DefaultedArray.size()"""
        return int._wrap(super(DefaultedArray, self).size())

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<T> dev.ultreon.quantum.world.gen.feature.DefaultedArray.listIterator()"""
        return 'ListIterator'._wrap(super(DefaultedArray, self).listIterator())

    @override
    @overload
    def clear(self):
        """public void dev.ultreon.quantum.world.gen.feature.DefaultedArray.clear()"""
        super(DefaultedArray, self).clear()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.DefaultedArray.addAll(int,java.util.Collection<? extends T>)"""
        return bool._wrap(super(_DefaultedArray, self).addAll(_int.valueOf(arg0), arg1))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'._wrap(super(List, self).reversed())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.DefaultedArray.addAll(java.util.Collection<? extends T>)"""
        return bool._wrap(super(_DefaultedArray, self).addAll(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.DefaultedArray.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_DefaultedArray, self).containsAll(arg0))

    @overload
    def subList(self, arg0: int, arg1: int) -> 'DefaultedArray':
        """public dev.ultreon.quantum.world.gen.feature.DefaultedArray<T> dev.ultreon.quantum.world.gen.feature.DefaultedArray.subList(int,int)"""
        return 'DefaultedArray'._wrap(super(_DefaultedArray, self).subList(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.List.addLast(E)"""
        super(_List, self).addLast(arg0) 
 
 
# CLASS: dev.ultreon.quantum.world.gen.feature.RockFeature
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.world.gen import noise
except ImportError:
    noise = _import_once("pyquantum.world.gen.noise")

import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import dev.ultreon.quantum.world.gen.feature.RockFeature as _RockFeature
_RockFeature = _RockFeature
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.world.gen.WorldGenFeature as _WorldGenFeature
_WorldGenFeature = _WorldGenFeature
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RockFeature():
    """dev.ultreon.quantum.world.gen.feature.RockFeature"""
 
    @staticmethod
    def _wrap(java_value: _RockFeature) -> 'RockFeature':
        return RockFeature(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RockFeature):
        """
        Dynamic initializer for RockFeature.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RockFeature__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RockFeature__wrapper":
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'NoiseConfig', arg1: 'Block', arg2: float):
        """public dev.ultreon.quantum.world.gen.feature.RockFeature(dev.ultreon.quantum.world.gen.noise.NoiseConfig,dev.ultreon.quantum.block.Block,float)"""
        val = _RockFeature(arg0, arg1, _float.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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
        return bool._wrap(super(_RockFeature, self).handle(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.feature.RockFeature.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(_RockFeature, self).create(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.world.gen.feature.FoliageFeature
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.world.gen import noise
except ImportError:
    noise = _import_once("pyquantum.world.gen.noise")

import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import dev.ultreon.quantum.world.gen.feature.FoliageFeature as _FoliageFeature
_FoliageFeature = _FoliageFeature
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.world.gen.WorldGenFeature as _WorldGenFeature
_WorldGenFeature = _WorldGenFeature
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FoliageFeature():
    """dev.ultreon.quantum.world.gen.feature.FoliageFeature"""
 
    @staticmethod
    def _wrap(java_value: _FoliageFeature) -> 'FoliageFeature':
        return FoliageFeature(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FoliageFeature):
        """
        Dynamic initializer for FoliageFeature.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FoliageFeature__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FoliageFeature__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'NoiseConfig', arg1: 'Block', arg2: float):
        """public dev.ultreon.quantum.world.gen.feature.FoliageFeature(dev.ultreon.quantum.world.gen.noise.NoiseConfig,dev.ultreon.quantum.block.Block,float)"""
        val = _FoliageFeature(arg0, arg1, _float.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def create(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.world.gen.feature.FoliageFeature.create(dev.ultreon.quantum.world.ServerWorld)"""
        super(_FoliageFeature, self).create(arg0)

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
    def handle(self, arg0: 'World', arg1: 'ChunkAccess', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.world.gen.feature.FoliageFeature.handle(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.ChunkAccess,int,int,int)"""
        return bool._wrap(super(_FoliageFeature, self).handle(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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