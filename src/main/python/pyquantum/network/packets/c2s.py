from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.network import server
except ImportError:
    server = _import_once("pyquantum.network.server")

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
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket as _C2SBlockBreakPacket
_C2SBlockBreakPacket = _C2SBlockBreakPacket
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
 
class C2SBlockBreakPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket"""
 
    @staticmethod
    def _wrap(java_value: _C2SBlockBreakPacket) -> 'C2SBlockBreakPacket':
        return C2SBlockBreakPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _C2SBlockBreakPacket):
        """
        Dynamic initializer for C2SBlockBreakPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_C2SBlockBreakPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_C2SBlockBreakPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _C2SBlockBreakPacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(_C2SBlockBreakPacket, self).handle(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_C2SBlockBreakPacket, self).toBytes(arg0)

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
    def __init__(self, arg0: 'BlockPos'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket(dev.ultreon.quantum.world.BlockPos)"""
        val = _C2SBlockBreakPacket(arg0)
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

 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.network import server
except ImportError:
    server = _import_once("pyquantum.network.server")

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
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket as _C2SBlockBreakPacket
_C2SBlockBreakPacket = _C2SBlockBreakPacket
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
 
class C2SBlockBreakPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket"""
 
    @staticmethod
    def _wrap(java_value: _C2SBlockBreakPacket) -> 'C2SBlockBreakPacket':
        return C2SBlockBreakPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _C2SBlockBreakPacket):
        """
        Dynamic initializer for C2SBlockBreakPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_C2SBlockBreakPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_C2SBlockBreakPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _C2SBlockBreakPacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(_C2SBlockBreakPacket, self).handle(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_C2SBlockBreakPacket, self).toBytes(arg0)

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
    def __init__(self, arg0: 'BlockPos'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket(dev.ultreon.quantum.world.BlockPos)"""
        val = _C2SBlockBreakPacket(arg0)
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

 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakPacket 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SCommandPacket
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.network.packets.c2s.C2SCommandPacket as _C2SCommandPacket
_C2SCommandPacket = _C2SCommandPacket
try:
    from pyquantum.network import server
except ImportError:
    server = _import_once("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
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
 
class C2SCommandPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SCommandPacket"""
 
    @staticmethod
    def _wrap(java_value: _C2SCommandPacket) -> 'C2SCommandPacket':
        return C2SCommandPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _C2SCommandPacket):
        """
        Dynamic initializer for C2SCommandPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_C2SCommandPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_C2SCommandPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.network.packets.c2s.C2SCommandPacket(java.lang.String)"""
        val = _C2SCommandPacket(arg0)
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
        """public void dev.ultreon.quantum.network.packets.c2s.C2SCommandPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_C2SCommandPacket, self).toBytes(arg0)

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SCommandPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(_C2SCommandPacket, self).handle(arg0, arg1)

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
        """public dev.ultreon.quantum.network.packets.c2s.C2SCommandPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _C2SCommandPacket(arg0)
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SRespawnPacket
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.network import server
except ImportError:
    server = _import_once("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
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
import dev.ultreon.quantum.network.packets.c2s.C2SRespawnPacket as _C2SRespawnPacket
_C2SRespawnPacket = _C2SRespawnPacket
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class C2SRespawnPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SRespawnPacket"""
 
    @staticmethod
    def _wrap(java_value: _C2SRespawnPacket) -> 'C2SRespawnPacket':
        return C2SRespawnPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _C2SRespawnPacket):
        """
        Dynamic initializer for C2SRespawnPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_C2SRespawnPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_C2SRespawnPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SRespawnPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _C2SRespawnPacket(arg0)
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
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SRespawnPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(_C2SRespawnPacket, self).handle(arg0, arg1)

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
        """public void dev.ultreon.quantum.network.packets.c2s.C2SRespawnPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_C2SRespawnPacket, self).toBytes(arg0)

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
    def __init__(self):
        """public dev.ultreon.quantum.network.packets.c2s.C2SRespawnPacket()"""
        val = _C2SRespawnPacket()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.packets.c2s.C2SRespawnPacket()"""
        val = _C2SRespawnPacket()
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
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SMenuTakeItemPacket
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.network import server
except ImportError:
    server = _import_once("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.network.packets.c2s.C2SMenuTakeItemPacket as _C2SMenuTakeItemPacket
_C2SMenuTakeItemPacket = _C2SMenuTakeItemPacket
import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class C2SMenuTakeItemPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SMenuTakeItemPacket"""
 
    @staticmethod
    def _wrap(java_value: _C2SMenuTakeItemPacket) -> 'C2SMenuTakeItemPacket':
        return C2SMenuTakeItemPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _C2SMenuTakeItemPacket):
        """
        Dynamic initializer for C2SMenuTakeItemPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_C2SMenuTakeItemPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_C2SMenuTakeItemPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: int, arg1: bool):
        """public dev.ultreon.quantum.network.packets.c2s.C2SMenuTakeItemPacket(int,boolean)"""
        val = _C2SMenuTakeItemPacket(_int.valueOf(arg0), _boolean.valueOf(arg1))
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
        """public void dev.ultreon.quantum.network.packets.c2s.C2SMenuTakeItemPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_C2SMenuTakeItemPacket, self).toBytes(arg0)

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
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SMenuTakeItemPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(_C2SMenuTakeItemPacket, self).handle(arg0, arg1)

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
        """public dev.ultreon.quantum.network.packets.c2s.C2SMenuTakeItemPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _C2SMenuTakeItemPacket(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SDropItemPacket
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.network import server
except ImportError:
    server = _import_once("pyquantum.network.server")

import dev.ultreon.quantum.network.packets.c2s.C2SDropItemPacket as _C2SDropItemPacket
_C2SDropItemPacket = _C2SDropItemPacket
from builtins import str
from pyquantum_helper import override
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
 
class C2SDropItemPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SDropItemPacket"""
 
    @staticmethod
    def _wrap(java_value: _C2SDropItemPacket) -> 'C2SDropItemPacket':
        return C2SDropItemPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _C2SDropItemPacket):
        """
        Dynamic initializer for C2SDropItemPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_C2SDropItemPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_C2SDropItemPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.packets.c2s.C2SDropItemPacket()"""
        val = _C2SDropItemPacket()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SDropItemPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _C2SDropItemPacket(arg0)
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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.packets.c2s.C2SDropItemPacket()"""
        val = _C2SDropItemPacket()
        self.__wrapper = val

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SDropItemPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_C2SDropItemPacket, self).toBytes(arg0)

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SDropItemPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(_C2SDropItemPacket, self).handle(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SPingPacket
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.network import server
except ImportError:
    server = _import_once("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
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
import dev.ultreon.quantum.network.packets.c2s.C2SPingPacket as _C2SPingPacket
_C2SPingPacket = _C2SPingPacket
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class C2SPingPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SPingPacket"""
 
    @staticmethod
    def _wrap(java_value: _C2SPingPacket) -> 'C2SPingPacket':
        return C2SPingPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _C2SPingPacket):
        """
        Dynamic initializer for C2SPingPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_C2SPingPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_C2SPingPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SPingPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _C2SPingPacket(arg0)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.packets.c2s.C2SPingPacket()"""
        val = _C2SPingPacket()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SPingPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_C2SPingPacket, self).toBytes(arg0)

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
        """public dev.ultreon.quantum.network.packets.c2s.C2SPingPacket()"""
        val = _C2SPingPacket()
        self.__wrapper = val

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SPingPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(_C2SPingPacket, self).handle(arg0, arg1)

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
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SCraftRecipePacket
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.network import server
except ImportError:
    server = _import_once("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import recipe
except ImportError:
    recipe = _import_once("pyquantum.recipe")

import dev.ultreon.quantum.network.packets.c2s.C2SCraftRecipePacket as _C2SCraftRecipePacket
_C2SCraftRecipePacket = _C2SCraftRecipePacket
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
 
class C2SCraftRecipePacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SCraftRecipePacket"""
 
    @staticmethod
    def _wrap(java_value: _C2SCraftRecipePacket) -> 'C2SCraftRecipePacket':
        return C2SCraftRecipePacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _C2SCraftRecipePacket):
        """
        Dynamic initializer for C2SCraftRecipePacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_C2SCraftRecipePacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_C2SCraftRecipePacket__wrapper":
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

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SCraftRecipePacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(_C2SCraftRecipePacket, self).handle(arg0, arg1)

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
        """public void dev.ultreon.quantum.network.packets.c2s.C2SCraftRecipePacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_C2SCraftRecipePacket, self).toBytes(arg0)

    @overload
    def __init__(self, arg0: 'RecipeType', arg1: 'Recipe'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SCraftRecipePacket(dev.ultreon.quantum.recipe.RecipeType,dev.ultreon.quantum.recipe.Recipe)"""
        val = _C2SCraftRecipePacket(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SCraftRecipePacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _C2SCraftRecipePacket(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SItemUsePacket
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.network import server
except ImportError:
    server = _import_once("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.network.packets.c2s.C2SItemUsePacket as _C2SItemUsePacket
_C2SItemUsePacket = _C2SItemUsePacket
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
 
class C2SItemUsePacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SItemUsePacket"""
 
    @staticmethod
    def _wrap(java_value: _C2SItemUsePacket) -> 'C2SItemUsePacket':
        return C2SItemUsePacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _C2SItemUsePacket):
        """
        Dynamic initializer for C2SItemUsePacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_C2SItemUsePacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_C2SItemUsePacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'BlockHitResult'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SItemUsePacket(dev.ultreon.quantum.util.BlockHitResult)"""
        val = _C2SItemUsePacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SItemUsePacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(_C2SItemUsePacket, self).handle(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SItemUsePacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _C2SItemUsePacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SItemUsePacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_C2SItemUsePacket, self).toBytes(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SChatPacket
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.network import server
except ImportError:
    server = _import_once("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import dev.ultreon.quantum.network.packets.c2s.C2SChatPacket as _C2SChatPacket
_C2SChatPacket = _C2SChatPacket
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class C2SChatPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SChatPacket"""
 
    @staticmethod
    def _wrap(java_value: _C2SChatPacket) -> 'C2SChatPacket':
        return C2SChatPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _C2SChatPacket):
        """
        Dynamic initializer for C2SChatPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_C2SChatPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_C2SChatPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SChatPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_C2SChatPacket, self).toBytes(arg0)

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SChatPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _C2SChatPacket(arg0)
        self.__wrapper = val

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SChatPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(_C2SChatPacket, self).handle(arg0, arg1)

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
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.network.packets.c2s.C2SChatPacket(java.lang.String)"""
        val = _C2SChatPacket(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.network import server
except ImportError:
    server = _import_once("pyquantum.network.server")

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
import dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket as _C2SBlockBreakingPacket
_C2SBlockBreakingPacket = _C2SBlockBreakingPacket
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
 
class C2SBlockBreakingPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket"""
 
    @staticmethod
    def _wrap(java_value: _C2SBlockBreakingPacket) -> 'C2SBlockBreakingPacket':
        return C2SBlockBreakingPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _C2SBlockBreakingPacket):
        """
        Dynamic initializer for C2SBlockBreakingPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_C2SBlockBreakingPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_C2SBlockBreakingPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(_C2SBlockBreakingPacket, self).handle(arg0, arg1)

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
    def __init__(self, arg0: 'BlockPos', arg1: 'BlockStatus'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket$BlockStatus)"""
        val = _C2SBlockBreakingPacket(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _C2SBlockBreakingPacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_C2SBlockBreakingPacket, self).toBytes(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SModPacket
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.network import server
except ImportError:
    server = _import_once("pyquantum.network.server")

from builtins import str
import dev.ultreon.quantum.network.NetworkChannel as _NetworkChannel
_NetworkChannel = _NetworkChannel
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.network.api import packet
except ImportError:
    packet = _import_once("pyquantum.network.api.packet")

import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import dev.ultreon.quantum.network.packets.c2s.C2SModPacket as _C2SModPacket
_C2SModPacket = _C2SModPacket
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class C2SModPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SModPacket"""
 
    @staticmethod
    def _wrap(java_value: _C2SModPacket) -> 'C2SModPacket':
        return C2SModPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _C2SModPacket):
        """
        Dynamic initializer for C2SModPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_C2SModPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_C2SModPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'NetworkChannel', arg1: 'ModPacket'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SModPacket(dev.ultreon.quantum.network.NetworkChannel,dev.ultreon.quantum.network.api.packet.ModPacket<?>)"""
        val = _C2SModPacket(arg0, arg1)
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
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SModPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(_C2SModPacket, self).handle(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SModPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_C2SModPacket, self).toBytes(arg0)

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SModPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _C2SModPacket(arg0)
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

    @overload
    def getChannel(self) -> 'network.NetworkChannel':
        """public dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.network.packets.c2s.C2SModPacket.getChannel()"""
        return 'network.NetworkChannel'._wrap(super(C2SModPacket, self).getChannel())

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
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SOpenMenuPacket
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.network import server
except ImportError:
    server = _import_once("pyquantum.network.server")

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
import dev.ultreon.quantum.network.packets.c2s.C2SOpenMenuPacket as _C2SOpenMenuPacket
_C2SOpenMenuPacket = _C2SOpenMenuPacket
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
 
class C2SOpenMenuPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SOpenMenuPacket"""
 
    @staticmethod
    def _wrap(java_value: _C2SOpenMenuPacket) -> 'C2SOpenMenuPacket':
        return C2SOpenMenuPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _C2SOpenMenuPacket):
        """
        Dynamic initializer for C2SOpenMenuPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_C2SOpenMenuPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_C2SOpenMenuPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SOpenMenuPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _C2SOpenMenuPacket(arg0)
        self.__wrapper = val

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SOpenMenuPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(_C2SOpenMenuPacket, self).handle(arg0, arg1)

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
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SOpenMenuPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_C2SOpenMenuPacket, self).toBytes(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Identifier', arg1: 'BlockPos'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SOpenMenuPacket(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.world.BlockPos)"""
        val = _C2SOpenMenuPacket(arg0, arg1)
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
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SOpenInventoryPacket
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.network import server
except ImportError:
    server = _import_once("pyquantum.network.server")

from builtins import str
import dev.ultreon.quantum.network.packets.c2s.C2SOpenInventoryPacket as _C2SOpenInventoryPacket
_C2SOpenInventoryPacket = _C2SOpenInventoryPacket
from pyquantum_helper import override
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
 
class C2SOpenInventoryPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SOpenInventoryPacket"""
 
    @staticmethod
    def _wrap(java_value: _C2SOpenInventoryPacket) -> 'C2SOpenInventoryPacket':
        return C2SOpenInventoryPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _C2SOpenInventoryPacket):
        """
        Dynamic initializer for C2SOpenInventoryPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_C2SOpenInventoryPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_C2SOpenInventoryPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SOpenInventoryPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(_C2SOpenInventoryPacket, self).handle(arg0, arg1)

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
        """public dev.ultreon.quantum.network.packets.c2s.C2SOpenInventoryPacket()"""
        val = _C2SOpenInventoryPacket()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.packets.c2s.C2SOpenInventoryPacket()"""
        val = _C2SOpenInventoryPacket()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SOpenInventoryPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _C2SOpenInventoryPacket(arg0)
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

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SOpenInventoryPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_C2SOpenInventoryPacket, self).toBytes(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket$BlockStatus
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
import dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket as _C2SBlockBreakingPacket_BlockStatus
_BlockStatus = _C2SBlockBreakingPacket_BlockStatus.BlockStatus
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
 
class BlockStatus():
    """dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket.BlockStatus"""
 
    @staticmethod
    def _wrap(java_value: _BlockStatus) -> 'BlockStatus':
        return BlockStatus(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockStatus):
        """
        Dynamic initializer for BlockStatus.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockStatus__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockStatus__wrapper":
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
    def valueOf(arg0: str) -> 'BlockStatus':
        """public static dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket$BlockStatus dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket$BlockStatus.valueOf(java.lang.String)"""
        return BlockStatus._wrap(_BlockStatus.valueOf(arg0))

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def values() -> List['BlockStatus']:
        """public static dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket$BlockStatus[] dev.ultreon.quantum.network.packets.c2s.C2SBlockBreakingPacket$BlockStatus.values()"""
        return List[BlockStatus]._wrap(_BlockStatus.values())

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


BlockStatus.START = BlockStatus._wrap(_START.START)

BlockStatus.STOP = BlockStatus._wrap(_STOP.STOP)

BlockStatus.CONTINUE = BlockStatus._wrap(_CONTINUE.CONTINUE)

BlockStatus.BROKEN = BlockStatus._wrap(_BROKEN.BROKEN) 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SPlaceBlockPacket
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.network import server
except ImportError:
    server = _import_once("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
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

import dev.ultreon.quantum.network.packets.c2s.C2SPlaceBlockPacket as _C2SPlaceBlockPacket
_C2SPlaceBlockPacket = _C2SPlaceBlockPacket
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
 
class C2SPlaceBlockPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SPlaceBlockPacket"""
 
    @staticmethod
    def _wrap(java_value: _C2SPlaceBlockPacket) -> 'C2SPlaceBlockPacket':
        return C2SPlaceBlockPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _C2SPlaceBlockPacket):
        """
        Dynamic initializer for C2SPlaceBlockPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_C2SPlaceBlockPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_C2SPlaceBlockPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SPlaceBlockPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_C2SPlaceBlockPacket, self).toBytes(arg0)

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
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SPlaceBlockPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(_C2SPlaceBlockPacket, self).handle(arg0, arg1)

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
        """public dev.ultreon.quantum.network.packets.c2s.C2SPlaceBlockPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _C2SPlaceBlockPacket(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SPlaceBlockPacket(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        val = _C2SPlaceBlockPacket(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)
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
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SPlayerMovePacket
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.network import server
except ImportError:
    server = _import_once("pyquantum.network.server")

from builtins import str
import dev.ultreon.quantum.network.packets.c2s.C2SPlayerMovePacket as _C2SPlayerMovePacket
_C2SPlayerMovePacket = _C2SPlayerMovePacket
import java.lang.Double as _double
from pyquantum_helper import override
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
 
class C2SPlayerMovePacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SPlayerMovePacket"""
 
    @staticmethod
    def _wrap(java_value: _C2SPlayerMovePacket) -> 'C2SPlayerMovePacket':
        return C2SPlayerMovePacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _C2SPlayerMovePacket):
        """
        Dynamic initializer for C2SPlayerMovePacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_C2SPlayerMovePacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_C2SPlayerMovePacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SPlayerMovePacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_C2SPlayerMovePacket, self).toBytes(arg0)

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public dev.ultreon.quantum.network.packets.c2s.C2SPlayerMovePacket(double,double,double)"""
        val = _C2SPlayerMovePacket(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))
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
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SPlayerMovePacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _C2SPlayerMovePacket(arg0)
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SPlayerMovePacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(_C2SPlayerMovePacket, self).handle(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SDisconnectPacket
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.network import server
except ImportError:
    server = _import_once("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.network.packets.c2s.C2SDisconnectPacket as _C2SDisconnectPacket
_C2SDisconnectPacket = _C2SDisconnectPacket
import java.lang.String as _String
_String = _String
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
 
class C2SDisconnectPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SDisconnectPacket"""
 
    @staticmethod
    def _wrap(java_value: _C2SDisconnectPacket) -> 'C2SDisconnectPacket':
        return C2SDisconnectPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _C2SDisconnectPacket):
        """
        Dynamic initializer for C2SDisconnectPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_C2SDisconnectPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_C2SDisconnectPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'ServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SDisconnectPacket.handle(dev.ultreon.quantum.network.PacketContext,T)"""
        super(_C2SDisconnectPacket, self).handle(arg0, arg1)

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
        """public void dev.ultreon.quantum.network.packets.c2s.C2SDisconnectPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_C2SDisconnectPacket, self).toBytes(arg0)

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
        """public dev.ultreon.quantum.network.packets.c2s.C2SDisconnectPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _C2SDisconnectPacket(arg0)
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
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.network.packets.c2s.C2SDisconnectPacket(java.lang.String)"""
        val = _C2SDisconnectPacket(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SLoginPacket
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.network import server
except ImportError:
    server = _import_once("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import dev.ultreon.quantum.network.packets.c2s.C2SLoginPacket as _C2SLoginPacket
_C2SLoginPacket = _C2SLoginPacket
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class C2SLoginPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SLoginPacket"""
 
    @staticmethod
    def _wrap(java_value: _C2SLoginPacket) -> 'C2SLoginPacket':
        return C2SLoginPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _C2SLoginPacket):
        """
        Dynamic initializer for C2SLoginPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_C2SLoginPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_C2SLoginPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.network.packets.c2s.C2SLoginPacket(java.lang.String)"""
        val = _C2SLoginPacket(arg0)
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
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SLoginPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _C2SLoginPacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'LoginServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SLoginPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.LoginServerPacketHandler)"""
        super(_C2SLoginPacket, self).handle(arg0, arg1)

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
        """public void dev.ultreon.quantum.network.packets.c2s.C2SLoginPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_C2SLoginPacket, self).toBytes(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SKeepAlivePacket
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.network import server
except ImportError:
    server = _import_once("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.network.packets.c2s.C2SKeepAlivePacket as _C2SKeepAlivePacket
_C2SKeepAlivePacket = _C2SKeepAlivePacket
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
 
class C2SKeepAlivePacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SKeepAlivePacket"""
 
    @staticmethod
    def _wrap(java_value: _C2SKeepAlivePacket) -> 'C2SKeepAlivePacket':
        return C2SKeepAlivePacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _C2SKeepAlivePacket):
        """
        Dynamic initializer for C2SKeepAlivePacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_C2SKeepAlivePacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_C2SKeepAlivePacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SKeepAlivePacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_C2SKeepAlivePacket, self).toBytes(arg0)

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
        """public dev.ultreon.quantum.network.packets.c2s.C2SKeepAlivePacket()"""
        val = _C2SKeepAlivePacket()
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.packets.c2s.C2SKeepAlivePacket()"""
        val = _C2SKeepAlivePacket()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SKeepAlivePacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _C2SKeepAlivePacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SKeepAlivePacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(_C2SKeepAlivePacket, self).handle(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SChunkStatusPacket
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.network.packets.c2s.C2SChunkStatusPacket as _C2SChunkStatusPacket
_C2SChunkStatusPacket = _C2SChunkStatusPacket
try:
    from pyquantum.network import server
except ImportError:
    server = _import_once("pyquantum.network.server")

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
 
class C2SChunkStatusPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SChunkStatusPacket"""
 
    @staticmethod
    def _wrap(java_value: _C2SChunkStatusPacket) -> 'C2SChunkStatusPacket':
        return C2SChunkStatusPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _C2SChunkStatusPacket):
        """
        Dynamic initializer for C2SChunkStatusPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_C2SChunkStatusPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_C2SChunkStatusPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'ChunkPos', arg1: 'Status'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SChunkStatusPacket(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.Chunk$Status)"""
        val = _C2SChunkStatusPacket(arg0, arg1)
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
        """public void dev.ultreon.quantum.network.packets.c2s.C2SChunkStatusPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_C2SChunkStatusPacket, self).toBytes(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SChunkStatusPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _C2SChunkStatusPacket(arg0)
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
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SChunkStatusPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(_C2SChunkStatusPacket, self).handle(arg0, arg1)

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
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SRequestTabComplete
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.network import server
except ImportError:
    server = _import_once("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import dev.ultreon.quantum.network.packets.c2s.C2SRequestTabComplete as _C2SRequestTabComplete
_C2SRequestTabComplete = _C2SRequestTabComplete
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class C2SRequestTabComplete():
    """dev.ultreon.quantum.network.packets.c2s.C2SRequestTabComplete"""
 
    @staticmethod
    def _wrap(java_value: _C2SRequestTabComplete) -> 'C2SRequestTabComplete':
        return C2SRequestTabComplete(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _C2SRequestTabComplete):
        """
        Dynamic initializer for C2SRequestTabComplete.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_C2SRequestTabComplete__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_C2SRequestTabComplete__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.network.packets.c2s.C2SRequestTabComplete(java.lang.String)"""
        val = _C2SRequestTabComplete(arg0)
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
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SRequestTabComplete(dev.ultreon.quantum.network.PacketIO)"""
        val = _C2SRequestTabComplete(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SRequestTabComplete.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(_C2SRequestTabComplete, self).handle(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SRequestTabComplete.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_C2SRequestTabComplete, self).toBytes(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SCloseMenuPacket
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.network import server
except ImportError:
    server = _import_once("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
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
import dev.ultreon.quantum.network.packets.c2s.C2SCloseMenuPacket as _C2SCloseMenuPacket
_C2SCloseMenuPacket = _C2SCloseMenuPacket
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class C2SCloseMenuPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SCloseMenuPacket"""
 
    @staticmethod
    def _wrap(java_value: _C2SCloseMenuPacket) -> 'C2SCloseMenuPacket':
        return C2SCloseMenuPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _C2SCloseMenuPacket):
        """
        Dynamic initializer for C2SCloseMenuPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_C2SCloseMenuPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_C2SCloseMenuPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SCloseMenuPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_C2SCloseMenuPacket, self).toBytes(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.packets.c2s.C2SCloseMenuPacket()"""
        val = _C2SCloseMenuPacket()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.c2s.C2SCloseMenuPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _C2SCloseMenuPacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SCloseMenuPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(_C2SCloseMenuPacket, self).handle(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.packets.c2s.C2SCloseMenuPacket()"""
        val = _C2SCloseMenuPacket()
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
 
 
# CLASS: dev.ultreon.quantum.network.packets.c2s.C2SHotbarIndexPacket
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.network import server
except ImportError:
    server = _import_once("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
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
import dev.ultreon.quantum.network.packets.c2s.C2SHotbarIndexPacket as _C2SHotbarIndexPacket
_C2SHotbarIndexPacket = _C2SHotbarIndexPacket
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class C2SHotbarIndexPacket():
    """dev.ultreon.quantum.network.packets.c2s.C2SHotbarIndexPacket"""
 
    @staticmethod
    def _wrap(java_value: _C2SHotbarIndexPacket) -> 'C2SHotbarIndexPacket':
        return C2SHotbarIndexPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _C2SHotbarIndexPacket):
        """
        Dynamic initializer for C2SHotbarIndexPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_C2SHotbarIndexPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_C2SHotbarIndexPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SHotbarIndexPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_C2SHotbarIndexPacket, self).toBytes(arg0)

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
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.network.packets.c2s.C2SHotbarIndexPacket(int)"""
        val = _C2SHotbarIndexPacket(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.c2s.C2SHotbarIndexPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(_C2SHotbarIndexPacket, self).handle(arg0, arg1)

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
        """public dev.ultreon.quantum.network.packets.c2s.C2SHotbarIndexPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _C2SHotbarIndexPacket(arg0)
        self.__wrapper = val