from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.network.packets.s2c.S2CAddEntityPacket as _S2CAddEntityPacket
_S2CAddEntityPacket = _S2CAddEntityPacket
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CAddEntityPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CAddEntityPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CAddEntityPacket) -> 'S2CAddEntityPacket':
        return S2CAddEntityPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CAddEntityPacket):
        """
        Dynamic initializer for S2CAddEntityPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CAddEntityPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CAddEntityPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CAddEntityPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CAddEntityPacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CAddEntityPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CAddEntityPacket, self).toBytes(arg0)

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Entity'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CAddEntityPacket(dev.ultreon.quantum.entity.Entity)"""
        val = _S2CAddEntityPacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CAddEntityPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CAddEntityPacket, self).handle(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CAddEntityPacket
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.network.packets.s2c.S2CAddEntityPacket as _S2CAddEntityPacket
_S2CAddEntityPacket = _S2CAddEntityPacket
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CAddEntityPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CAddEntityPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CAddEntityPacket) -> 'S2CAddEntityPacket':
        return S2CAddEntityPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CAddEntityPacket):
        """
        Dynamic initializer for S2CAddEntityPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CAddEntityPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CAddEntityPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CAddEntityPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CAddEntityPacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CAddEntityPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CAddEntityPacket, self).toBytes(arg0)

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Entity'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CAddEntityPacket(dev.ultreon.quantum.entity.Entity)"""
        val = _S2CAddEntityPacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CAddEntityPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CAddEntityPacket, self).handle(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CAddEntityPacket 
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CBlockEntitySetPacket
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.network.packets.s2c.S2CBlockEntitySetPacket as _S2CBlockEntitySetPacket
_S2CBlockEntitySetPacket = _S2CBlockEntitySetPacket
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CBlockEntitySetPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CBlockEntitySetPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CBlockEntitySetPacket) -> 'S2CBlockEntitySetPacket':
        return S2CBlockEntitySetPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CBlockEntitySetPacket):
        """
        Dynamic initializer for S2CBlockEntitySetPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CBlockEntitySetPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CBlockEntitySetPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'BlockPos', arg1: int):
        """public dev.ultreon.quantum.network.packets.s2c.S2CBlockEntitySetPacket(dev.ultreon.quantum.world.BlockPos,int)"""
        val = _S2CBlockEntitySetPacket(arg0, _int.valueOf(arg1))
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
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CBlockEntitySetPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CBlockEntitySetPacket, self).toBytes(arg0)

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
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CBlockEntitySetPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CBlockEntitySetPacket, self).handle(arg0, arg1)

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CBlockEntitySetPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CBlockEntitySetPacket(arg0)
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CSpawnParticlesPacket
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.lang.String as _String
_String = _String
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
try:
    from pyquantum.world import particles
except ImportError:
    particles = _import_once("pyquantum.world.particles")

import dev.ultreon.quantum.network.packets.s2c.S2CSpawnParticlesPacket as _S2CSpawnParticlesPacket
_S2CSpawnParticlesPacket = _S2CSpawnParticlesPacket
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CSpawnParticlesPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CSpawnParticlesPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CSpawnParticlesPacket) -> 'S2CSpawnParticlesPacket':
        return S2CSpawnParticlesPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CSpawnParticlesPacket):
        """
        Dynamic initializer for S2CSpawnParticlesPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CSpawnParticlesPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CSpawnParticlesPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CSpawnParticlesPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CSpawnParticlesPacket, self).handle(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CSpawnParticlesPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CSpawnParticlesPacket, self).toBytes(arg0)

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
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CSpawnParticlesPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CSpawnParticlesPacket(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'ParticleType', arg1: 'Vec3d', arg2: 'Vec3d', arg3: int):
        """public dev.ultreon.quantum.network.packets.s2c.S2CSpawnParticlesPacket(dev.ultreon.quantum.world.particles.ParticleType,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d,int)"""
        val = _S2CSpawnParticlesPacket(arg0, arg1, arg2, _int.valueOf(arg3))
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CPlayerHurtPacket
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.entity.damagesource.DamageSource as _DamageSource
_DamageSource = _DamageSource
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.lang.String as _String
_String = _String
import java.lang.Float as _float
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
try:
    from pyquantum.entity import damagesource
except ImportError:
    damagesource = _import_once("pyquantum.entity.damagesource")

from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.network.packets.s2c.S2CPlayerHurtPacket as _S2CPlayerHurtPacket
_S2CPlayerHurtPacket = _S2CPlayerHurtPacket
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CPlayerHurtPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CPlayerHurtPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CPlayerHurtPacket) -> 'S2CPlayerHurtPacket':
        return S2CPlayerHurtPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CPlayerHurtPacket):
        """
        Dynamic initializer for S2CPlayerHurtPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CPlayerHurtPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CPlayerHurtPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getDamage(self) -> float:
        """public float dev.ultreon.quantum.network.packets.s2c.S2CPlayerHurtPacket.getDamage()"""
        return float._wrap(super(S2CPlayerHurtPacket, self).getDamage())

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
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CPlayerHurtPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CPlayerHurtPacket, self).handle(arg0, arg1)

    @overload
    def getSource(self) -> 'damagesource.DamageSource':
        """public dev.ultreon.quantum.entity.damagesource.DamageSource dev.ultreon.quantum.network.packets.s2c.S2CPlayerHurtPacket.getSource()"""
        return 'damagesource.DamageSource'._wrap(super(S2CPlayerHurtPacket, self).getSource())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: float, arg1: 'DamageSource'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CPlayerHurtPacket(float,dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        val = _S2CPlayerHurtPacket(_float.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CPlayerHurtPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CPlayerHurtPacket, self).toBytes(arg0)

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
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CPlayerHurtPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CPlayerHurtPacket(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CPlayerHealthPacket
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.network.packets.s2c.S2CPlayerHealthPacket as _S2CPlayerHealthPacket
_S2CPlayerHealthPacket = _S2CPlayerHealthPacket
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.lang.String as _String
_String = _String
import java.lang.Float as _float
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CPlayerHealthPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CPlayerHealthPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CPlayerHealthPacket) -> 'S2CPlayerHealthPacket':
        return S2CPlayerHealthPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CPlayerHealthPacket):
        """
        Dynamic initializer for S2CPlayerHealthPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CPlayerHealthPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CPlayerHealthPacket__wrapper":
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
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CPlayerHealthPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CPlayerHealthPacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CPlayerHealthPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CPlayerHealthPacket, self).toBytes(arg0)

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
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CPlayerHealthPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CPlayerHealthPacket, self).handle(arg0, arg1)

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

    @overload
    def __init__(self, arg0: float):
        """public dev.ultreon.quantum.network.packets.s2c.S2CPlayerHealthPacket(float)"""
        val = _S2CPlayerHealthPacket(_float.valueOf(arg0))
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CCloseMenuPacket
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.network.packets.s2c.S2CCloseMenuPacket as _S2CCloseMenuPacket
_S2CCloseMenuPacket = _S2CCloseMenuPacket
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CCloseMenuPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CCloseMenuPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CCloseMenuPacket) -> 'S2CCloseMenuPacket':
        return S2CCloseMenuPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CCloseMenuPacket):
        """
        Dynamic initializer for S2CCloseMenuPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CCloseMenuPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CCloseMenuPacket__wrapper":
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
    def __init__(self, ):
        """public dev.ultreon.quantum.network.packets.s2c.S2CCloseMenuPacket()"""
        val = _S2CCloseMenuPacket()
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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CCloseMenuPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CCloseMenuPacket, self).toBytes(arg0)

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CCloseMenuPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CCloseMenuPacket, self).handle(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.packets.s2c.S2CCloseMenuPacket()"""
        val = _S2CCloseMenuPacket()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CCloseMenuPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CCloseMenuPacket(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.C2SAbilitiesPacket
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.network.packets.s2c.C2SAbilitiesPacket as _C2SAbilitiesPacket
_C2SAbilitiesPacket = _C2SAbilitiesPacket
try:
    from pyquantum.network import server
except ImportError:
    server = _import_once("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class C2SAbilitiesPacket():
    """dev.ultreon.quantum.network.packets.s2c.C2SAbilitiesPacket"""
 
    @staticmethod
    def _wrap(java_value: _C2SAbilitiesPacket) -> 'C2SAbilitiesPacket':
        return C2SAbilitiesPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _C2SAbilitiesPacket):
        """
        Dynamic initializer for C2SAbilitiesPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_C2SAbilitiesPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_C2SAbilitiesPacket__wrapper":
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
    def isFlying(self) -> bool:
        """public boolean dev.ultreon.quantum.network.packets.s2c.C2SAbilitiesPacket.isFlying()"""
        return bool._wrap(super(C2SAbilitiesPacket, self).isFlying())

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
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.C2SAbilitiesPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_C2SAbilitiesPacket, self).toBytes(arg0)

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
    def isInstaMine(self) -> bool:
        """public boolean dev.ultreon.quantum.network.packets.s2c.C2SAbilitiesPacket.isInstaMine()"""
        return bool._wrap(super(C2SAbilitiesPacket, self).isInstaMine())

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.C2SAbilitiesPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(_C2SAbilitiesPacket, self).handle(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def allowFlight(self) -> bool:
        """public boolean dev.ultreon.quantum.network.packets.s2c.C2SAbilitiesPacket.allowFlight()"""
        return bool._wrap(super(C2SAbilitiesPacket, self).allowFlight())

    @overload
    def __init__(self, arg0: 'PlayerAbilities'):
        """public dev.ultreon.quantum.network.packets.s2c.C2SAbilitiesPacket(dev.ultreon.quantum.entity.player.PlayerAbilities)"""
        val = _C2SAbilitiesPacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isInvincible(self) -> bool:
        """public boolean dev.ultreon.quantum.network.packets.s2c.C2SAbilitiesPacket.isInvincible()"""
        return bool._wrap(super(C2SAbilitiesPacket, self).isInvincible())

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.C2SAbilitiesPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _C2SAbilitiesPacket(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CMenuItemChanged
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.network.packets.s2c.S2CMenuItemChanged as _S2CMenuItemChanged
_S2CMenuItemChanged = _S2CMenuItemChanged
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CMenuItemChanged():
    """dev.ultreon.quantum.network.packets.s2c.S2CMenuItemChanged"""
 
    @staticmethod
    def _wrap(java_value: _S2CMenuItemChanged) -> 'S2CMenuItemChanged':
        return S2CMenuItemChanged(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CMenuItemChanged):
        """
        Dynamic initializer for S2CMenuItemChanged.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CMenuItemChanged__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CMenuItemChanged__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: int, arg1: 'ItemStack'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CMenuItemChanged(int,dev.ultreon.quantum.item.ItemStack)"""
        val = _S2CMenuItemChanged(_int.valueOf(arg0), arg1)
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
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CMenuItemChanged.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CMenuItemChanged, self).toBytes(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CMenuItemChanged.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CMenuItemChanged, self).handle(arg0, arg1)

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CMenuItemChanged(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CMenuItemChanged(arg0)
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CTabCompletePacket
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import dev.ultreon.quantum.network.packets.s2c.S2CTabCompletePacket as _S2CTabCompletePacket
_S2CTabCompletePacket = _S2CTabCompletePacket
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.util.List as List
 
class S2CTabCompletePacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CTabCompletePacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CTabCompletePacket) -> 'S2CTabCompletePacket':
        return S2CTabCompletePacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CTabCompletePacket):
        """
        Dynamic initializer for S2CTabCompletePacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CTabCompletePacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CTabCompletePacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'List'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CTabCompletePacket(java.util.List<java.lang.String>)"""
        val = _S2CTabCompletePacket(arg0)
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
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CTabCompletePacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CTabCompletePacket, self).handle(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CTabCompletePacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CTabCompletePacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CTabCompletePacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CTabCompletePacket, self).toBytes(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CPlayerPositionPacket
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.util.UUID as UUID
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.lang.String as _String
_String = _String
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import dev.ultreon.quantum.network.packets.s2c.S2CPlayerPositionPacket as _S2CPlayerPositionPacket
_S2CPlayerPositionPacket = _S2CPlayerPositionPacket
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CPlayerPositionPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CPlayerPositionPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CPlayerPositionPacket) -> 'S2CPlayerPositionPacket':
        return S2CPlayerPositionPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CPlayerPositionPacket):
        """
        Dynamic initializer for S2CPlayerPositionPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CPlayerPositionPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CPlayerPositionPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'UUID', arg1: 'Vec3d'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CPlayerPositionPacket(java.util.UUID,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        val = _S2CPlayerPositionPacket(arg0, arg1)
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

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CPlayerPositionPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CPlayerPositionPacket, self).handle(arg0, arg1)

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CPlayerPositionPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CPlayerPositionPacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CPlayerPositionPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CPlayerPositionPacket, self).toBytes(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CPlayerSetPosPacket
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.lang.String as _String
_String = _String
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import dev.ultreon.quantum.network.packets.s2c.S2CPlayerSetPosPacket as _S2CPlayerSetPosPacket
_S2CPlayerSetPosPacket = _S2CPlayerSetPosPacket
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CPlayerSetPosPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CPlayerSetPosPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CPlayerSetPosPacket) -> 'S2CPlayerSetPosPacket':
        return S2CPlayerSetPosPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CPlayerSetPosPacket):
        """
        Dynamic initializer for S2CPlayerSetPosPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CPlayerSetPosPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CPlayerSetPosPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CPlayerSetPosPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CPlayerSetPosPacket, self).handle(arg0, arg1)

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
    def __init__(self, arg0: 'Vec3d'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CPlayerSetPosPacket(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        val = _S2CPlayerSetPosPacket(arg0)
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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CPlayerSetPosPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CPlayerSetPosPacket, self).toBytes(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public dev.ultreon.quantum.network.packets.s2c.S2CPlayerSetPosPacket(double,double,double)"""
        val = _S2CPlayerSetPosPacket(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CPlayerSetPosPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CPlayerSetPosPacket(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CTimePacket$Operation
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.network.packets.s2c.S2CTimePacket as _S2CTimePacket_Operation
_Operation = _S2CTimePacket_Operation.Operation
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
 
class Operation():
    """dev.ultreon.quantum.network.packets.s2c.S2CTimePacket.Operation"""
 
    @staticmethod
    def _wrap(java_value: _Operation) -> 'Operation':
        return Operation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Operation):
        """
        Dynamic initializer for Operation.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Operation__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Operation__wrapper":
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
    def values() -> List['Operation']:
        """public static dev.ultreon.quantum.network.packets.s2c.S2CTimePacket$Operation[] dev.ultreon.quantum.network.packets.s2c.S2CTimePacket$Operation.values()"""
        return List[Operation]._wrap(_Operation.values())

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
    def valueOf(arg0: str) -> 'Operation':
        """public static dev.ultreon.quantum.network.packets.s2c.S2CTimePacket$Operation dev.ultreon.quantum.network.packets.s2c.S2CTimePacket$Operation.valueOf(java.lang.String)"""
        return Operation._wrap(_Operation.valueOf(arg0))


Operation.SET = Operation._wrap(_SET.SET)

Operation.SUB = Operation._wrap(_SUB.SUB)

Operation.ADD = Operation._wrap(_ADD.ADD) 
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CMenuCursorPacket
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import dev.ultreon.quantum.network.packets.s2c.S2CMenuCursorPacket as _S2CMenuCursorPacket
_S2CMenuCursorPacket = _S2CMenuCursorPacket
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CMenuCursorPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CMenuCursorPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CMenuCursorPacket) -> 'S2CMenuCursorPacket':
        return S2CMenuCursorPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CMenuCursorPacket):
        """
        Dynamic initializer for S2CMenuCursorPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CMenuCursorPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CMenuCursorPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CMenuCursorPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CMenuCursorPacket, self).toBytes(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'ItemStack'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CMenuCursorPacket(dev.ultreon.quantum.item.ItemStack)"""
        val = _S2CMenuCursorPacket(arg0)
        self.__wrapper = val

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CMenuCursorPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CMenuCursorPacket, self).handle(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CMenuCursorPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CMenuCursorPacket(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CCommandSyncPacket
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import dev.ultreon.quantum.network.packets.s2c.S2CCommandSyncPacket as _S2CCommandSyncPacket
_S2CCommandSyncPacket = _S2CCommandSyncPacket
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.util.List as List
 
class S2CCommandSyncPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CCommandSyncPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CCommandSyncPacket) -> 'S2CCommandSyncPacket':
        return S2CCommandSyncPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CCommandSyncPacket):
        """
        Dynamic initializer for S2CCommandSyncPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CCommandSyncPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CCommandSyncPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CCommandSyncPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CCommandSyncPacket, self).handle(arg0, arg1)

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
    def __init__(self, arg0: 'List'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CCommandSyncPacket(java.util.List<java.lang.String>)"""
        val = _S2CCommandSyncPacket(arg0)
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

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CCommandSyncPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CCommandSyncPacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CCommandSyncPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CCommandSyncPacket, self).toBytes(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CLoginAcceptedPacket
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.util.UUID as UUID
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.network.packets.s2c.S2CLoginAcceptedPacket as _S2CLoginAcceptedPacket
_S2CLoginAcceptedPacket = _S2CLoginAcceptedPacket
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CLoginAcceptedPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CLoginAcceptedPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CLoginAcceptedPacket) -> 'S2CLoginAcceptedPacket':
        return S2CLoginAcceptedPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CLoginAcceptedPacket):
        """
        Dynamic initializer for S2CLoginAcceptedPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CLoginAcceptedPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CLoginAcceptedPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'LoginClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CLoginAcceptedPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.LoginClientPacketHandler)"""
        super(_S2CLoginAcceptedPacket, self).handle(arg0, arg1)

    @overload
    def __init__(self, arg0: 'UUID'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CLoginAcceptedPacket(java.util.UUID)"""
        val = _S2CLoginAcceptedPacket(arg0)
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CLoginAcceptedPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CLoginAcceptedPacket, self).toBytes(arg0)

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
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CLoginAcceptedPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CLoginAcceptedPacket(arg0)
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CRespawnPacket
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.network.packets.s2c.S2CRespawnPacket as _S2CRespawnPacket
_S2CRespawnPacket = _S2CRespawnPacket
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.lang.String as _String
_String = _String
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CRespawnPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CRespawnPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CRespawnPacket) -> 'S2CRespawnPacket':
        return S2CRespawnPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CRespawnPacket):
        """
        Dynamic initializer for S2CRespawnPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CRespawnPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CRespawnPacket__wrapper":
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
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CRespawnPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CRespawnPacket, self).toBytes(arg0)

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CRespawnPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CRespawnPacket, self).handle(arg0, arg1)

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Vec3d'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CRespawnPacket(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        val = _S2CRespawnPacket(arg0)
        self.__wrapper = val

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

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CRespawnPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CRespawnPacket(arg0)
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CDisconnectPacket
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import dev.ultreon.quantum.network.packets.s2c.S2CDisconnectPacket as _S2CDisconnectPacket
_S2CDisconnectPacket = _S2CDisconnectPacket
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CDisconnectPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CDisconnectPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CDisconnectPacket) -> 'S2CDisconnectPacket':
        return S2CDisconnectPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CDisconnectPacket):
        """
        Dynamic initializer for S2CDisconnectPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CDisconnectPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CDisconnectPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CDisconnectPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CDisconnectPacket(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.network.packets.s2c.S2CDisconnectPacket(java.lang.String)"""
        val = _S2CDisconnectPacket(arg0)
        self.__wrapper = val

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'ClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CDisconnectPacket.handle(dev.ultreon.quantum.network.PacketContext,T)"""
        super(_S2CDisconnectPacket, self).handle(arg0, arg1)

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CDisconnectPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CDisconnectPacket, self).toBytes(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CChunkCancelPacket
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import dev.ultreon.quantum.network.packets.s2c.S2CChunkCancelPacket as _S2CChunkCancelPacket
_S2CChunkCancelPacket = _S2CChunkCancelPacket
import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CChunkCancelPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CChunkCancelPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CChunkCancelPacket) -> 'S2CChunkCancelPacket':
        return S2CChunkCancelPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CChunkCancelPacket):
        """
        Dynamic initializer for S2CChunkCancelPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CChunkCancelPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CChunkCancelPacket__wrapper":
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

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CChunkCancelPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CChunkCancelPacket, self).toBytes(arg0)

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
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CChunkCancelPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CChunkCancelPacket, self).handle(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'ChunkPos'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CChunkCancelPacket(dev.ultreon.quantum.world.ChunkPos)"""
        val = _S2CChunkCancelPacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CChunkCancelPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CChunkCancelPacket(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CRemoveEntityPacket
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.network.packets.s2c.S2CRemoveEntityPacket as _S2CRemoveEntityPacket
_S2CRemoveEntityPacket = _S2CRemoveEntityPacket
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CRemoveEntityPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CRemoveEntityPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CRemoveEntityPacket) -> 'S2CRemoveEntityPacket':
        return S2CRemoveEntityPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CRemoveEntityPacket):
        """
        Dynamic initializer for S2CRemoveEntityPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CRemoveEntityPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CRemoveEntityPacket__wrapper":
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
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CRemoveEntityPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CRemoveEntityPacket, self).toBytes(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.network.packets.s2c.S2CRemoveEntityPacket(int)"""
        val = _S2CRemoveEntityPacket(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CRemoveEntityPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CRemoveEntityPacket, self).handle(arg0, arg1)

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CRemoveEntityPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CRemoveEntityPacket(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CPingPacket
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import dev.ultreon.quantum.network.packets.s2c.S2CPingPacket as _S2CPingPacket
_S2CPingPacket = _S2CPingPacket
import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CPingPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CPingPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CPingPacket) -> 'S2CPingPacket':
        return S2CPingPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CPingPacket):
        """
        Dynamic initializer for S2CPingPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CPingPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CPingPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.network.packets.s2c.S2CPingPacket(long)"""
        val = _S2CPingPacket(_long.valueOf(arg0))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CPingPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CPingPacket(arg0)
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'ClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CPingPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.ClientPacketHandler)"""
        super(_S2CPingPacket, self).handle(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CPingPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CPingPacket, self).toBytes(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2COpenMenuPacket
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.network.packets.s2c.S2COpenMenuPacket as _S2COpenMenuPacket
_S2COpenMenuPacket = _S2COpenMenuPacket
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2COpenMenuPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2COpenMenuPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2COpenMenuPacket) -> 'S2COpenMenuPacket':
        return S2COpenMenuPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2COpenMenuPacket):
        """
        Dynamic initializer for S2COpenMenuPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2COpenMenuPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2COpenMenuPacket__wrapper":
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

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2COpenMenuPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2COpenMenuPacket, self).toBytes(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2COpenMenuPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2COpenMenuPacket(arg0)
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Identifier', arg1: 'Collection'):
        """public dev.ultreon.quantum.network.packets.s2c.S2COpenMenuPacket(dev.ultreon.quantum.util.Identifier,java.util.Collection<dev.ultreon.quantum.menu.ItemSlot>)"""
        val = _S2COpenMenuPacket(arg0, arg1)
        self.__wrapper = val

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2COpenMenuPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2COpenMenuPacket, self).handle(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CAddPlayerPacket
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.util.UUID as UUID
from pyquantum_helper import override
import dev.ultreon.quantum.network.packets.s2c.S2CAddPlayerPacket as _S2CAddPlayerPacket
_S2CAddPlayerPacket = _S2CAddPlayerPacket
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.lang.String as _String
_String = _String
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import java.lang.String as _string
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CAddPlayerPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CAddPlayerPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CAddPlayerPacket) -> 'S2CAddPlayerPacket':
        return S2CAddPlayerPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CAddPlayerPacket):
        """
        Dynamic initializer for S2CAddPlayerPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CAddPlayerPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CAddPlayerPacket__wrapper":
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
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CAddPlayerPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CAddPlayerPacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CAddPlayerPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CAddPlayerPacket, self).toBytes(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'UUID', arg1: str, arg2: 'Vec3d'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CAddPlayerPacket(java.util.UUID,java.lang.String,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        val = _S2CAddPlayerPacket(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CAddPlayerPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CAddPlayerPacket, self).handle(arg0, arg1)

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CInventoryItemChangedPacket
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import dev.ultreon.quantum.network.packets.s2c.S2CInventoryItemChangedPacket as _S2CInventoryItemChangedPacket
_S2CInventoryItemChangedPacket = _S2CInventoryItemChangedPacket
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CInventoryItemChangedPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CInventoryItemChangedPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CInventoryItemChangedPacket) -> 'S2CInventoryItemChangedPacket':
        return S2CInventoryItemChangedPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CInventoryItemChangedPacket):
        """
        Dynamic initializer for S2CInventoryItemChangedPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CInventoryItemChangedPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CInventoryItemChangedPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CInventoryItemChangedPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CInventoryItemChangedPacket, self).toBytes(arg0)

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CInventoryItemChangedPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CInventoryItemChangedPacket(arg0)
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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CInventoryItemChangedPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CInventoryItemChangedPacket, self).handle(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int, arg1: 'ItemStack'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CInventoryItemChangedPacket(int,dev.ultreon.quantum.item.ItemStack)"""
        val = _S2CInventoryItemChangedPacket(_int.valueOf(arg0), arg1)
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
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CModPacket
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network.api import packet
except ImportError:
    packet = _import_once("pyquantum.network.api.packet")

try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.network.packets.s2c.S2CModPacket as _S2CModPacket
_S2CModPacket = _S2CModPacket
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CModPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CModPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CModPacket) -> 'S2CModPacket':
        return S2CModPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CModPacket):
        """
        Dynamic initializer for S2CModPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CModPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CModPacket__wrapper":
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
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CModPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CModPacket, self).toBytes(arg0)

    @overload
    def __init__(self, arg0: 'NetworkChannel', arg1: 'ModPacket'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CModPacket(dev.ultreon.quantum.network.NetworkChannel,dev.ultreon.quantum.network.api.packet.ModPacket<?>)"""
        val = _S2CModPacket(arg0, arg1)
        self.__wrapper = val

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CModPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CModPacket, self).handle(arg0, arg1)

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
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CModPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CModPacket(arg0)
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CPlaySoundPacket
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Float as _float
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import dev.ultreon.quantum.network.packets.s2c.S2CPlaySoundPacket as _S2CPlaySoundPacket
_S2CPlaySoundPacket = _S2CPlaySoundPacket
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CPlaySoundPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CPlaySoundPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CPlaySoundPacket) -> 'S2CPlaySoundPacket':
        return S2CPlaySoundPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CPlaySoundPacket):
        """
        Dynamic initializer for S2CPlaySoundPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CPlaySoundPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CPlaySoundPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'Identifier', arg1: float):
        """public dev.ultreon.quantum.network.packets.s2c.S2CPlaySoundPacket(dev.ultreon.quantum.util.Identifier,float)"""
        val = _S2CPlaySoundPacket(arg0, _float.valueOf(arg1))
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CPlaySoundPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CPlaySoundPacket, self).toBytes(arg0)

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
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CPlaySoundPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CPlaySoundPacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CPlaySoundPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CPlaySoundPacket, self).handle(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CRemovePlayerPacket
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.util.UUID as UUID
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.network.packets.s2c.S2CRemovePlayerPacket as _S2CRemovePlayerPacket
_S2CRemovePlayerPacket = _S2CRemovePlayerPacket
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CRemovePlayerPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CRemovePlayerPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CRemovePlayerPacket) -> 'S2CRemovePlayerPacket':
        return S2CRemovePlayerPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CRemovePlayerPacket):
        """
        Dynamic initializer for S2CRemovePlayerPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CRemovePlayerPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CRemovePlayerPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'UUID'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CRemovePlayerPacket(java.util.UUID)"""
        val = _S2CRemovePlayerPacket(arg0)
        self.__wrapper = val

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CRemovePlayerPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CRemovePlayerPacket, self).handle(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CRemovePlayerPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CRemovePlayerPacket, self).toBytes(arg0)

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CRemovePlayerPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CRemovePlayerPacket(arg0)
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CChunkDataPacket
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
try:
    from pyquantum import collection
except ImportError:
    collection = _import_once("pyquantum.collection")

import dev.ultreon.quantum.network.packets.s2c.S2CChunkDataPacket as _S2CChunkDataPacket
_S2CChunkDataPacket = _S2CChunkDataPacket
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CChunkDataPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CChunkDataPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CChunkDataPacket) -> 'S2CChunkDataPacket':
        return S2CChunkDataPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CChunkDataPacket):
        """
        Dynamic initializer for S2CChunkDataPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CChunkDataPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CChunkDataPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CChunkDataPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CChunkDataPacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CChunkDataPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CChunkDataPacket, self).handle(arg0, arg1)

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
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CChunkDataPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CChunkDataPacket, self).toBytes(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'ChunkPos', arg1: 'Storage', arg2: 'Storage', arg3: 'Collection'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CChunkDataPacket(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.collection.Storage<dev.ultreon.quantum.block.state.BlockProperties>,dev.ultreon.quantum.collection.Storage<dev.ultreon.quantum.world.Biome>,java.util.Collection<dev.ultreon.quantum.block.entity.BlockEntity>)"""
        val = _S2CChunkDataPacket(arg0, arg1, arg2, arg3)
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CBlockSetPacket
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.network.packets.s2c.S2CBlockSetPacket as _S2CBlockSetPacket
_S2CBlockSetPacket = _S2CBlockSetPacket
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CBlockSetPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CBlockSetPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CBlockSetPacket) -> 'S2CBlockSetPacket':
        return S2CBlockSetPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CBlockSetPacket):
        """
        Dynamic initializer for S2CBlockSetPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CBlockSetPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CBlockSetPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CBlockSetPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CBlockSetPacket, self).handle(arg0, arg1)

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

    @overload
    def __init__(self, arg0: 'BlockPos', arg1: 'BlockProperties'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CBlockSetPacket(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        val = _S2CBlockSetPacket(arg0, arg1)
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
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CBlockSetPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CBlockSetPacket, self).toBytes(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CBlockSetPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CBlockSetPacket(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CChatPacket
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.network.packets.s2c.S2CChatPacket as _S2CChatPacket
_S2CChatPacket = _S2CChatPacket
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.lang.String as _String
_String = _String
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CChatPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CChatPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CChatPacket) -> 'S2CChatPacket':
        return S2CChatPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CChatPacket):
        """
        Dynamic initializer for S2CChatPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CChatPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CChatPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CChatPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CChatPacket, self).toBytes(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'TextObject'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CChatPacket(dev.ultreon.quantum.text.TextObject)"""
        val = _S2CChatPacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CChatPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CChatPacket, self).handle(arg0, arg1)

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

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CChatPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CChatPacket(arg0)
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CAbilitiesPacket
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import dev.ultreon.quantum.network.packets.s2c.S2CAbilitiesPacket as _S2CAbilitiesPacket
_S2CAbilitiesPacket = _S2CAbilitiesPacket
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CAbilitiesPacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CAbilitiesPacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CAbilitiesPacket) -> 'S2CAbilitiesPacket':
        return S2CAbilitiesPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CAbilitiesPacket):
        """
        Dynamic initializer for S2CAbilitiesPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CAbilitiesPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CAbilitiesPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CAbilitiesPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CAbilitiesPacket, self).handle(arg0, arg1)

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CAbilitiesPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CAbilitiesPacket, self).toBytes(arg0)

    @override
    @overload
    def allowFlight(self) -> bool:
        """public boolean dev.ultreon.quantum.network.packets.s2c.S2CAbilitiesPacket.allowFlight()"""
        return bool._wrap(super(S2CAbilitiesPacket, self).allowFlight())

    @override
    @overload
    def isFlying(self) -> bool:
        """public boolean dev.ultreon.quantum.network.packets.s2c.S2CAbilitiesPacket.isFlying()"""
        return bool._wrap(super(S2CAbilitiesPacket, self).isFlying())

    @overload
    def __init__(self, arg0: 'PlayerAbilities'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CAbilitiesPacket(dev.ultreon.quantum.entity.player.PlayerAbilities)"""
        val = _S2CAbilitiesPacket(arg0)
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CAbilitiesPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CAbilitiesPacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def isInvincible(self) -> bool:
        """public boolean dev.ultreon.quantum.network.packets.s2c.S2CAbilitiesPacket.isInvincible()"""
        return bool._wrap(super(S2CAbilitiesPacket, self).isInvincible())

    @override
    @overload
    def isInstaMine(self) -> bool:
        """public boolean dev.ultreon.quantum.network.packets.s2c.S2CAbilitiesPacket.isInstaMine()"""
        return bool._wrap(super(S2CAbilitiesPacket, self).isInstaMine())

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
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CKeepAlivePacket
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import dev.ultreon.quantum.network.packets.s2c.S2CKeepAlivePacket as _S2CKeepAlivePacket
_S2CKeepAlivePacket = _S2CKeepAlivePacket
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CKeepAlivePacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CKeepAlivePacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CKeepAlivePacket) -> 'S2CKeepAlivePacket':
        return S2CKeepAlivePacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CKeepAlivePacket):
        """
        Dynamic initializer for S2CKeepAlivePacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CKeepAlivePacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CKeepAlivePacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.packets.s2c.S2CKeepAlivePacket()"""
        val = _S2CKeepAlivePacket()
        self.__wrapper = val

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CKeepAlivePacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CKeepAlivePacket, self).handle(arg0, arg1)

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
    def __init__(self, ):
        """public dev.ultreon.quantum.network.packets.s2c.S2CKeepAlivePacket()"""
        val = _S2CKeepAlivePacket()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CKeepAlivePacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CKeepAlivePacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CKeepAlivePacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CKeepAlivePacket, self).toBytes(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CGamemodePacket
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import dev.ultreon.quantum.network.packets.s2c.S2CGamemodePacket as _S2CGamemodePacket
_S2CGamemodePacket = _S2CGamemodePacket
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CGamemodePacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CGamemodePacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CGamemodePacket) -> 'S2CGamemodePacket':
        return S2CGamemodePacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CGamemodePacket):
        """
        Dynamic initializer for S2CGamemodePacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CGamemodePacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CGamemodePacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CGamemodePacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CGamemodePacket, self).handle(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CGamemodePacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CGamemodePacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'GameMode'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CGamemodePacket(dev.ultreon.quantum.util.GameMode)"""
        val = _S2CGamemodePacket(arg0)
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
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CGamemodePacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CGamemodePacket, self).toBytes(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.network.packets.s2c.S2CTimePacket
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = _import_once("pyquantum.network.client")

import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import dev.ultreon.quantum.network.packets.s2c.S2CTimePacket as _S2CTimePacket
_S2CTimePacket = _S2CTimePacket
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class S2CTimePacket():
    """dev.ultreon.quantum.network.packets.s2c.S2CTimePacket"""
 
    @staticmethod
    def _wrap(java_value: _S2CTimePacket) -> 'S2CTimePacket':
        return S2CTimePacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _S2CTimePacket):
        """
        Dynamic initializer for S2CTimePacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_S2CTimePacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_S2CTimePacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CTimePacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_S2CTimePacket, self).handle(arg0, arg1)

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

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.s2c.S2CTimePacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _S2CTimePacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.s2c.S2CTimePacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_S2CTimePacket, self).toBytes(arg0)

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
    def __init__(self, arg0: 'Operation', arg1: int):
        """public dev.ultreon.quantum.network.packets.s2c.S2CTimePacket(dev.ultreon.quantum.network.packets.s2c.S2CTimePacket$Operation,int)"""
        val = _S2CTimePacket(arg0, _int.valueOf(arg1))
        self.__wrapper = val

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