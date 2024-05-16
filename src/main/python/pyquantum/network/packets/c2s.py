from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import server
except ImportError:
    server = __import_once__("pyquantum.network.server")

try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket as __C2SBlockBreakPacket
__C2SBlockBreakPacket = __C2SBlockBreakPacket
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class C2SBlockBreakPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket"""
 
    @staticmethod
    def __wrap(java_value: __C2SBlockBreakPacket) -> 'C2SBlockBreakPacket':
        return C2SBlockBreakPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __C2SBlockBreakPacket):
        """
        Dynamic initializer for C2SBlockBreakPacket.
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
    def __init__(self, arg0: 'BlockPos'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket(dev.ultreon.quantum.world.BlockPos)"""
        val = __C2SBlockBreakPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(__C2SBlockBreakPacket, self).handle(arg0, arg1)

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
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __C2SBlockBreakPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__C2SBlockBreakPacket, self).toBytes(arg0)

 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import server
except ImportError:
    server = __import_once__("pyquantum.network.server")

try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket as __C2SBlockBreakPacket
__C2SBlockBreakPacket = __C2SBlockBreakPacket
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class C2SBlockBreakPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket"""
 
    @staticmethod
    def __wrap(java_value: __C2SBlockBreakPacket) -> 'C2SBlockBreakPacket':
        return C2SBlockBreakPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __C2SBlockBreakPacket):
        """
        Dynamic initializer for C2SBlockBreakPacket.
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
    def __init__(self, arg0: 'BlockPos'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket(dev.ultreon.quantum.world.BlockPos)"""
        val = __C2SBlockBreakPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(__C2SBlockBreakPacket, self).handle(arg0, arg1)

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
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __C2SBlockBreakPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__C2SBlockBreakPacket, self).toBytes(arg0)

 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SCommandPacket
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import server
except ImportError:
    server = __import_once__("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import dev.ultreon.quantum.network.packets.c2s.C2SCommandPacket as __C2SCommandPacket
__C2SCommandPacket = __C2SCommandPacket
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class C2SCommandPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SCommandPacket"""
 
    @staticmethod
    def __wrap(java_value: __C2SCommandPacket) -> 'C2SCommandPacket':
        return C2SCommandPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __C2SCommandPacket):
        """
        Dynamic initializer for C2SCommandPacket.
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
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SCommandPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __C2SCommandPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SCommandPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(__C2SCommandPacket, self).handle(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SCommandPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__C2SCommandPacket, self).toBytes(arg0)

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
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.network.packets.c2s.C2SCommandPacket(java.lang.String)"""
        val = __C2SCommandPacket(arg0)
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SRespawnPacket
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import server
except ImportError:
    server = __import_once__("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.network.packets.c2s.C2SRespawnPacket as __C2SRespawnPacket
__C2SRespawnPacket = __C2SRespawnPacket
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class C2SRespawnPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SRespawnPacket"""
 
    @staticmethod
    def __wrap(java_value: __C2SRespawnPacket) -> 'C2SRespawnPacket':
        return C2SRespawnPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __C2SRespawnPacket):
        """
        Dynamic initializer for C2SRespawnPacket.
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
        """public dev.ultreon.quantum.network.packets.c2s.C2SRespawnPacket()"""
        val = __C2SRespawnPacket()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SRespawnPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(__C2SRespawnPacket, self).handle(arg0, arg1)

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
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SRespawnPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__C2SRespawnPacket, self).toBytes(arg0)

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SRespawnPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __C2SRespawnPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.packets.c2s.C2SRespawnPacket()"""
        val = __C2SRespawnPacket()
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SMenuTakeItemPacket
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import server
except ImportError:
    server = __import_once__("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.network.packets.c2s.C2SMenuTakeItemPacket as __C2SMenuTakeItemPacket
__C2SMenuTakeItemPacket = __C2SMenuTakeItemPacket
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class C2SMenuTakeItemPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SMenuTakeItemPacket"""
 
    @staticmethod
    def __wrap(java_value: __C2SMenuTakeItemPacket) -> 'C2SMenuTakeItemPacket':
        return C2SMenuTakeItemPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __C2SMenuTakeItemPacket):
        """
        Dynamic initializer for C2SMenuTakeItemPacket.
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
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SMenuTakeItemPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __C2SMenuTakeItemPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SMenuTakeItemPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__C2SMenuTakeItemPacket, self).toBytes(arg0)

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

    @overload
    def __init__(self, arg0: int, arg1: bool):
        """public dev.ultreon.quantum.network.packets.c2s.C2SMenuTakeItemPacket(int,boolean)"""
        val = __C2SMenuTakeItemPacket(__int.valueOf(arg0), __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SMenuTakeItemPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(__C2SMenuTakeItemPacket, self).handle(arg0, arg1)

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
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SDropItemPacket
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import server
except ImportError:
    server = __import_once__("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.network.packets.c2s.C2SDropItemPacket as __C2SDropItemPacket
__C2SDropItemPacket = __C2SDropItemPacket
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class C2SDropItemPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SDropItemPacket"""
 
    @staticmethod
    def __wrap(java_value: __C2SDropItemPacket) -> 'C2SDropItemPacket':
        return C2SDropItemPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __C2SDropItemPacket):
        """
        Dynamic initializer for C2SDropItemPacket.
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
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SDropItemPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(__C2SDropItemPacket, self).handle(arg0, arg1)

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SDropItemPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __C2SDropItemPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SDropItemPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__C2SDropItemPacket, self).toBytes(arg0)

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.packets.c2s.C2SDropItemPacket()"""
        val = __C2SDropItemPacket()
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
    def __init__(self):
        """public dev.ultreon.quantum.network.packets.c2s.C2SDropItemPacket()"""
        val = __C2SDropItemPacket()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SPingPacket
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import server
except ImportError:
    server = __import_once__("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.network.packets.c2s.C2SPingPacket as __C2SPingPacket
__C2SPingPacket = __C2SPingPacket
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class C2SPingPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SPingPacket"""
 
    @staticmethod
    def __wrap(java_value: __C2SPingPacket) -> 'C2SPingPacket':
        return C2SPingPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __C2SPingPacket):
        """
        Dynamic initializer for C2SPingPacket.
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
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SPingPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __C2SPingPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SPingPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__C2SPingPacket, self).toBytes(arg0)

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
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SPingPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(__C2SPingPacket, self).handle(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.packets.c2s.C2SPingPacket()"""
        val = __C2SPingPacket()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.packets.c2s.C2SPingPacket()"""
        val = __C2SPingPacket()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SCraftRecipePacket
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import server
except ImportError:
    server = __import_once__("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import recipe
except ImportError:
    recipe = __import_once__("pyquantum.recipe")

import dev.ultreon.quantum.network.packets.c2s.C2SCraftRecipePacket as __C2SCraftRecipePacket
__C2SCraftRecipePacket = __C2SCraftRecipePacket
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class C2SCraftRecipePacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SCraftRecipePacket"""
 
    @staticmethod
    def __wrap(java_value: __C2SCraftRecipePacket) -> 'C2SCraftRecipePacket':
        return C2SCraftRecipePacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __C2SCraftRecipePacket):
        """
        Dynamic initializer for C2SCraftRecipePacket.
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
    def __init__(self, arg0: 'RecipeType', arg1: 'Recipe'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SCraftRecipePacket(dev.ultreon.quantum.recipe.RecipeType,dev.ultreon.quantum.recipe.Recipe)"""
        val = __C2SCraftRecipePacket(arg0, arg1)
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

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SCraftRecipePacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__C2SCraftRecipePacket, self).toBytes(arg0)

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
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SCraftRecipePacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(__C2SCraftRecipePacket, self).handle(arg0, arg1)

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
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SCraftRecipePacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __C2SCraftRecipePacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SItemUsePacket
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import server
except ImportError:
    server = __import_once__("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.network.packets.c2s.C2SItemUsePacket as __C2SItemUsePacket
__C2SItemUsePacket = __C2SItemUsePacket
from builtins import bool
from builtins import int
 
class C2SItemUsePacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SItemUsePacket"""
 
    @staticmethod
    def __wrap(java_value: __C2SItemUsePacket) -> 'C2SItemUsePacket':
        return C2SItemUsePacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __C2SItemUsePacket):
        """
        Dynamic initializer for C2SItemUsePacket.
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
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SItemUsePacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(__C2SItemUsePacket, self).handle(arg0, arg1)

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SItemUsePacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __C2SItemUsePacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SItemUsePacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__C2SItemUsePacket, self).toBytes(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'BlockHitResult'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SItemUsePacket(dev.ultreon.quantum.util.BlockHitResult)"""
        val = __C2SItemUsePacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SChatPacket
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import server
except ImportError:
    server = __import_once__("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.packets.c2s.C2SChatPacket as __C2SChatPacket
__C2SChatPacket = __C2SChatPacket
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class C2SChatPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SChatPacket"""
 
    @staticmethod
    def __wrap(java_value: __C2SChatPacket) -> 'C2SChatPacket':
        return C2SChatPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __C2SChatPacket):
        """
        Dynamic initializer for C2SChatPacket.
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
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SChatPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__C2SChatPacket, self).toBytes(arg0)

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SChatPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(__C2SChatPacket, self).handle(arg0, arg1)

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
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SChatPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __C2SChatPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.network.packets.c2s.C2SChatPacket(java.lang.String)"""
        val = __C2SChatPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import server
except ImportError:
    server = __import_once__("pyquantum.network.server")

try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket as __C2SBlockBreakingPacket
__C2SBlockBreakingPacket = __C2SBlockBreakingPacket
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class C2SBlockBreakingPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket"""
 
    @staticmethod
    def __wrap(java_value: __C2SBlockBreakingPacket) -> 'C2SBlockBreakingPacket':
        return C2SBlockBreakingPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __C2SBlockBreakingPacket):
        """
        Dynamic initializer for C2SBlockBreakingPacket.
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
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(__C2SBlockBreakingPacket, self).handle(arg0, arg1)

    @overload
    def __init__(self, arg0: 'BlockPos', arg1: 'BlockStatus'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket$BlockStatus)"""
        val = __C2SBlockBreakingPacket(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __C2SBlockBreakingPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__C2SBlockBreakingPacket, self).toBytes(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SModPacket
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import server
except ImportError:
    server = __import_once__("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.network.api import packet
except ImportError:
    packet = __import_once__("pyquantum.network.api.packet")

import dev.ultreon.quantum.network.NetworkChannel as __NetworkChannel
__NetworkChannel = __NetworkChannel
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.network.packets.c2s.C2SModPacket as __C2SModPacket
__C2SModPacket = __C2SModPacket
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class C2SModPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SModPacket"""
 
    @staticmethod
    def __wrap(java_value: __C2SModPacket) -> 'C2SModPacket':
        return C2SModPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __C2SModPacket):
        """
        Dynamic initializer for C2SModPacket.
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
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SModPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__C2SModPacket, self).toBytes(arg0)

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SModPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __C2SModPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'NetworkChannel', arg1: 'ModPacket'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SModPacket(dev.ultreon.quantum.network.NetworkChannel,dev.ultreon.quantum.network.api.packet.ModPacket<?>)"""
        val = __C2SModPacket(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SModPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(__C2SModPacket, self).handle(arg0, arg1)

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
    def getChannel(self) -> 'network.NetworkChannel':
        """public dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.network.packets.c2s.C2SModPacket.getChannel()"""
        return 'network.NetworkChannel'.__wrap(super(C2SModPacket, self).getChannel())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SOpenMenuPacket
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import server
except ImportError:
    server = __import_once__("pyquantum.network.server")

try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.packets.c2s.C2SOpenMenuPacket as __C2SOpenMenuPacket
__C2SOpenMenuPacket = __C2SOpenMenuPacket
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class C2SOpenMenuPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SOpenMenuPacket"""
 
    @staticmethod
    def __wrap(java_value: __C2SOpenMenuPacket) -> 'C2SOpenMenuPacket':
        return C2SOpenMenuPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __C2SOpenMenuPacket):
        """
        Dynamic initializer for C2SOpenMenuPacket.
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
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SOpenMenuPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__C2SOpenMenuPacket, self).toBytes(arg0)

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SOpenMenuPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(__C2SOpenMenuPacket, self).handle(arg0, arg1)

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Identifier', arg1: 'BlockPos'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SOpenMenuPacket(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.world.BlockPos)"""
        val = __C2SOpenMenuPacket(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SOpenMenuPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __C2SOpenMenuPacket(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SOpenInventoryPacket
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import server
except ImportError:
    server = __import_once__("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.network.packets.c2s.C2SOpenInventoryPacket as __C2SOpenInventoryPacket
__C2SOpenInventoryPacket = __C2SOpenInventoryPacket
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class C2SOpenInventoryPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SOpenInventoryPacket"""
 
    @staticmethod
    def __wrap(java_value: __C2SOpenInventoryPacket) -> 'C2SOpenInventoryPacket':
        return C2SOpenInventoryPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __C2SOpenInventoryPacket):
        """
        Dynamic initializer for C2SOpenInventoryPacket.
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
        """public dev.ultreon.quantum.network.packets.c2s.C2SOpenInventoryPacket()"""
        val = __C2SOpenInventoryPacket()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SOpenInventoryPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__C2SOpenInventoryPacket, self).toBytes(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.packets.c2s.C2SOpenInventoryPacket()"""
        val = __C2SOpenInventoryPacket()
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
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SOpenInventoryPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(__C2SOpenInventoryPacket, self).handle(arg0, arg1)

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
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SOpenInventoryPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __C2SOpenInventoryPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket$BlockStatus
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket as __C2SBlockBreakingPacket_BlockStatus
__BlockStatus = __C2SBlockBreakingPacket_BlockStatus.BlockStatus
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
 
class BlockStatus():
    """dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket.BlockStatus"""
 
    @staticmethod
    def __wrap(java_value: __BlockStatus) -> 'BlockStatus':
        return BlockStatus(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockStatus):
        """
        Dynamic initializer for BlockStatus.
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
 
    # public static final dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket$BlockStatus dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket$BlockStatus.CONTINUE
    CONTINUE: 'BlockStatus' = __wrap(__BlockStatus.CONTINUE)

    # public static final dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket$BlockStatus dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket$BlockStatus.START
    START: 'BlockStatus' = __wrap(__BlockStatus.START)

    # public static final dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket$BlockStatus dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket$BlockStatus.STOP
    STOP: 'BlockStatus' = __wrap(__BlockStatus.STOP)

    # public static final dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket$BlockStatus dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket$BlockStatus.BROKEN
    BROKEN: 'BlockStatus' = __wrap(__BlockStatus.BROKEN)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'BlockStatus':
        """public static dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket$BlockStatus dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket$BlockStatus.valueOf(java.lang.String)"""
        return BlockStatus.__wrap(__BlockStatus.valueOf(arg0))

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
    def values() -> List['BlockStatus']:
        """public static dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket$BlockStatus[] dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket$BlockStatus.values()"""
        return List[BlockStatus].__wrap(__BlockStatus.values()) 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SPlaceBlockPacket
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import server
except ImportError:
    server = __import_once__("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.network.packets.c2s.C2SPlaceBlockPacket as __C2SPlaceBlockPacket
__C2SPlaceBlockPacket = __C2SPlaceBlockPacket
import java.lang.String as __String
__String = __String
try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class C2SPlaceBlockPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SPlaceBlockPacket"""
 
    @staticmethod
    def __wrap(java_value: __C2SPlaceBlockPacket) -> 'C2SPlaceBlockPacket':
        return C2SPlaceBlockPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __C2SPlaceBlockPacket):
        """
        Dynamic initializer for C2SPlaceBlockPacket.
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
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SPlaceBlockPacket(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        val = __C2SPlaceBlockPacket(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SPlaceBlockPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __C2SPlaceBlockPacket(arg0)
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
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SPlaceBlockPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__C2SPlaceBlockPacket, self).toBytes(arg0)

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SPlaceBlockPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(__C2SPlaceBlockPacket, self).handle(arg0, arg1)

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
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SPlayerMovePacket
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import server
except ImportError:
    server = __import_once__("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.network.packets.c2s.C2SPlayerMovePacket as __C2SPlayerMovePacket
__C2SPlayerMovePacket = __C2SPlayerMovePacket
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
from builtins import int
 
class C2SPlayerMovePacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SPlayerMovePacket"""
 
    @staticmethod
    def __wrap(java_value: __C2SPlayerMovePacket) -> 'C2SPlayerMovePacket':
        return C2SPlayerMovePacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __C2SPlayerMovePacket):
        """
        Dynamic initializer for C2SPlayerMovePacket.
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
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SPlayerMovePacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __C2SPlayerMovePacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SPlayerMovePacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(__C2SPlayerMovePacket, self).handle(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public dev.ultreon.quantum.network.packets.c2s.C2SPlayerMovePacket(double,double,double)"""
        val = __C2SPlayerMovePacket(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SPlayerMovePacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__C2SPlayerMovePacket, self).toBytes(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SDisconnectPacket
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import server
except ImportError:
    server = __import_once__("pyquantum.network.server")

import dev.ultreon.quantum.network.packets.c2s.C2SDisconnectPacket as __C2SDisconnectPacket
__C2SDisconnectPacket = __C2SDisconnectPacket
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class C2SDisconnectPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SDisconnectPacket"""
 
    @staticmethod
    def __wrap(java_value: __C2SDisconnectPacket) -> 'C2SDisconnectPacket':
        return C2SDisconnectPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __C2SDisconnectPacket):
        """
        Dynamic initializer for C2SDisconnectPacket.
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
    def handle(self, arg0: 'PacketContext', arg1: 'ServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SDisconnectPacket.handle(dev.ultreon.quantum.network.PacketContext,T)"""
        super(__C2SDisconnectPacket, self).handle(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.network.packets.c2s.C2SDisconnectPacket(java.lang.String)"""
        val = __C2SDisconnectPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SDisconnectPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__C2SDisconnectPacket, self).toBytes(arg0)

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

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SDisconnectPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __C2SDisconnectPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SLoginPacket
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import server
except ImportError:
    server = __import_once__("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.network.packets.c2s.C2SLoginPacket as __C2SLoginPacket
__C2SLoginPacket = __C2SLoginPacket
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class C2SLoginPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SLoginPacket"""
 
    @staticmethod
    def __wrap(java_value: __C2SLoginPacket) -> 'C2SLoginPacket':
        return C2SLoginPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __C2SLoginPacket):
        """
        Dynamic initializer for C2SLoginPacket.
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
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SLoginPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__C2SLoginPacket, self).toBytes(arg0)

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
    def handle(self, arg0: 'PacketContext', arg1: 'LoginServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SLoginPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.LoginServerPacketHandler)"""
        super(__C2SLoginPacket, self).handle(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.network.packets.c2s.C2SLoginPacket(java.lang.String)"""
        val = __C2SLoginPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SLoginPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __C2SLoginPacket(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SKeepAlivePacket
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import server
except ImportError:
    server = __import_once__("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.network.packets.c2s.C2SKeepAlivePacket as __C2SKeepAlivePacket
__C2SKeepAlivePacket = __C2SKeepAlivePacket
from builtins import bool
from builtins import int
 
class C2SKeepAlivePacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SKeepAlivePacket"""
 
    @staticmethod
    def __wrap(java_value: __C2SKeepAlivePacket) -> 'C2SKeepAlivePacket':
        return C2SKeepAlivePacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __C2SKeepAlivePacket):
        """
        Dynamic initializer for C2SKeepAlivePacket.
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
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SKeepAlivePacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__C2SKeepAlivePacket, self).toBytes(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SKeepAlivePacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __C2SKeepAlivePacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.packets.c2s.C2SKeepAlivePacket()"""
        val = __C2SKeepAlivePacket()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.packets.c2s.C2SKeepAlivePacket()"""
        val = __C2SKeepAlivePacket()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SKeepAlivePacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(__C2SKeepAlivePacket, self).handle(arg0, arg1)

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
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SChunkStatusPacket
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import server
except ImportError:
    server = __import_once__("pyquantum.network.server")

try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.packets.c2s.C2SChunkStatusPacket as __C2SChunkStatusPacket
__C2SChunkStatusPacket = __C2SChunkStatusPacket
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class C2SChunkStatusPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SChunkStatusPacket"""
 
    @staticmethod
    def __wrap(java_value: __C2SChunkStatusPacket) -> 'C2SChunkStatusPacket':
        return C2SChunkStatusPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __C2SChunkStatusPacket):
        """
        Dynamic initializer for C2SChunkStatusPacket.
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
    def __init__(self, arg0: 'ChunkPos', arg1: 'Status'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SChunkStatusPacket(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.Chunk$Status)"""
        val = __C2SChunkStatusPacket(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SChunkStatusPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __C2SChunkStatusPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SChunkStatusPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(__C2SChunkStatusPacket, self).handle(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SChunkStatusPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__C2SChunkStatusPacket, self).toBytes(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SRequestTabComplete
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import server
except ImportError:
    server = __import_once__("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.packets.c2s.C2SRequestTabComplete as __C2SRequestTabComplete
__C2SRequestTabComplete = __C2SRequestTabComplete
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class C2SRequestTabComplete():
    """dev.ultreon.quantum.network.packets.c2s.C2SRequestTabComplete"""
 
    @staticmethod
    def __wrap(java_value: __C2SRequestTabComplete) -> 'C2SRequestTabComplete':
        return C2SRequestTabComplete(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __C2SRequestTabComplete):
        """
        Dynamic initializer for C2SRequestTabComplete.
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
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SRequestTabComplete(dev.ultreon.quantum.network.PacketIO)"""
        val = __C2SRequestTabComplete(arg0)
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
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SRequestTabComplete.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__C2SRequestTabComplete, self).toBytes(arg0)

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
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SRequestTabComplete.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(__C2SRequestTabComplete, self).handle(arg0, arg1)

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.network.packets.c2s.C2SRequestTabComplete(java.lang.String)"""
        val = __C2SRequestTabComplete(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SCloseMenuPacket
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import server
except ImportError:
    server = __import_once__("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.packets.c2s.C2SCloseMenuPacket as __C2SCloseMenuPacket
__C2SCloseMenuPacket = __C2SCloseMenuPacket
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class C2SCloseMenuPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SCloseMenuPacket"""
 
    @staticmethod
    def __wrap(java_value: __C2SCloseMenuPacket) -> 'C2SCloseMenuPacket':
        return C2SCloseMenuPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __C2SCloseMenuPacket):
        """
        Dynamic initializer for C2SCloseMenuPacket.
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
        """public dev.ultreon.quantum.network.packets.c2s.C2SCloseMenuPacket()"""
        val = __C2SCloseMenuPacket()
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.packets.c2s.C2SCloseMenuPacket()"""
        val = __C2SCloseMenuPacket()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SCloseMenuPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __C2SCloseMenuPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SCloseMenuPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__C2SCloseMenuPacket, self).toBytes(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SCloseMenuPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(__C2SCloseMenuPacket, self).handle(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SHotbarIndexPacket
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import server
except ImportError:
    server = __import_once__("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.packets.c2s.C2SHotbarIndexPacket as __C2SHotbarIndexPacket
__C2SHotbarIndexPacket = __C2SHotbarIndexPacket
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class C2SHotbarIndexPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SHotbarIndexPacket"""
 
    @staticmethod
    def __wrap(java_value: __C2SHotbarIndexPacket) -> 'C2SHotbarIndexPacket':
        return C2SHotbarIndexPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __C2SHotbarIndexPacket):
        """
        Dynamic initializer for C2SHotbarIndexPacket.
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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.network.packets.c2s.C2SHotbarIndexPacket(int)"""
        val = __C2SHotbarIndexPacket(__int.valueOf(arg0))
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
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SHotbarIndexPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __C2SHotbarIndexPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SHotbarIndexPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(__C2SHotbarIndexPacket, self).handle(arg0, arg1)

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SHotbarIndexPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__C2SHotbarIndexPacket, self).toBytes(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))