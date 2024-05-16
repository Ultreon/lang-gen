from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = __import_once__("pyquantum.network.client")

import java.util.List as __List
__List = __List
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
import dev.ultreon.quantum.network.packets.InitialPermissionsPacket as __InitialPermissionsPacket
__InitialPermissionsPacket = __InitialPermissionsPacket
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class InitialPermissionsPacket():
    """dev.ultreon.quantum.network.packets.InitialPermissionsPacket"""
 
    @staticmethod
    def __wrap(java_value: __InitialPermissionsPacket) -> 'InitialPermissionsPacket':
        return InitialPermissionsPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InitialPermissionsPacket):
        """
        Dynamic initializer for InitialPermissionsPacket.
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
    def getPermissions(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.api.commands.perms.Permission> dev.ultreon.quantum.network.packets.InitialPermissionsPacket.getPermissions()"""
        return 'List'.__wrap(super(InitialPermissionsPacket, self).getPermissions())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.InitialPermissionsPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__InitialPermissionsPacket, self).toBytes(arg0)

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
        """public dev.ultreon.quantum.network.packets.InitialPermissionsPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __InitialPermissionsPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'List'):
        """public dev.ultreon.quantum.network.packets.InitialPermissionsPacket(java.util.List<dev.ultreon.quantum.api.commands.perms.Permission>)"""
        val = __InitialPermissionsPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.InitialPermissionsPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(__InitialPermissionsPacket, self).handle(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.network.packets.InitialPermissionsPacket
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = __import_once__("pyquantum.network.client")

import java.util.List as __List
__List = __List
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
import dev.ultreon.quantum.network.packets.InitialPermissionsPacket as __InitialPermissionsPacket
__InitialPermissionsPacket = __InitialPermissionsPacket
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class InitialPermissionsPacket():
    """dev.ultreon.quantum.network.packets.InitialPermissionsPacket"""
 
    @staticmethod
    def __wrap(java_value: __InitialPermissionsPacket) -> 'InitialPermissionsPacket':
        return InitialPermissionsPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InitialPermissionsPacket):
        """
        Dynamic initializer for InitialPermissionsPacket.
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
    def getPermissions(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.api.commands.perms.Permission> dev.ultreon.quantum.network.packets.InitialPermissionsPacket.getPermissions()"""
        return 'List'.__wrap(super(InitialPermissionsPacket, self).getPermissions())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.InitialPermissionsPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__InitialPermissionsPacket, self).toBytes(arg0)

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
        """public dev.ultreon.quantum.network.packets.InitialPermissionsPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __InitialPermissionsPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'List'):
        """public dev.ultreon.quantum.network.packets.InitialPermissionsPacket(java.util.List<dev.ultreon.quantum.api.commands.perms.Permission>)"""
        val = __InitialPermissionsPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.InitialPermissionsPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(__InitialPermissionsPacket, self).handle(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.network.packets.InitialPermissionsPacket 
 
 
# CLASS: dev.ultreon.quantum.network.packets.RemovePermissionPacket
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = __import_once__("pyquantum.network.client")

import dev.ultreon.quantum.api.commands.perms.Permission as __Permission
__Permission = __Permission
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

try:
    from pyquantum.api.commands import perms
except ImportError:
    perms = __import_once__("pyquantum.api.commands.perms")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.network.packets.RemovePermissionPacket as __RemovePermissionPacket
__RemovePermissionPacket = __RemovePermissionPacket
from builtins import int
 
class RemovePermissionPacket():
    """dev.ultreon.quantum.network.packets.RemovePermissionPacket"""
 
    @staticmethod
    def __wrap(java_value: __RemovePermissionPacket) -> 'RemovePermissionPacket':
        return RemovePermissionPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RemovePermissionPacket):
        """
        Dynamic initializer for RemovePermissionPacket.
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
        """public void dev.ultreon.quantum.network.packets.RemovePermissionPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__RemovePermissionPacket, self).toBytes(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.RemovePermissionPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(__RemovePermissionPacket, self).handle(arg0, arg1)

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
        """public dev.ultreon.quantum.network.packets.RemovePermissionPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __RemovePermissionPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getPermission(self) -> 'perms.Permission':
        """public dev.ultreon.quantum.api.commands.perms.Permission dev.ultreon.quantum.network.packets.RemovePermissionPacket.getPermission()"""
        return 'perms.Permission'.__wrap(super(RemovePermissionPacket, self).getPermission())

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
    def __init__(self, arg0: 'Permission'):
        """public dev.ultreon.quantum.network.packets.RemovePermissionPacket(dev.ultreon.quantum.api.commands.perms.Permission)"""
        val = __RemovePermissionPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.network.packets.C2SAttackPacket
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.network import server
except ImportError:
    server = __import_once__("pyquantum.network.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

from builtins import type
import dev.ultreon.quantum.network.packets.C2SAttackPacket as __C2SAttackPacket
__C2SAttackPacket = __C2SAttackPacket
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
 
class C2SAttackPacket():
    """dev.ultreon.quantum.network.packets.C2SAttackPacket"""
 
    @staticmethod
    def __wrap(java_value: __C2SAttackPacket) -> 'C2SAttackPacket':
        return C2SAttackPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __C2SAttackPacket):
        """
        Dynamic initializer for C2SAttackPacket.
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
        """public dev.ultreon.quantum.network.packets.C2SAttackPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __C2SAttackPacket(arg0)
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
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.C2SAttackPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(__C2SAttackPacket, self).handle(arg0, arg1)

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.C2SAttackPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__C2SAttackPacket, self).toBytes(arg0)

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
    def __init__(self, arg0: 'Entity'):
        """public dev.ultreon.quantum.network.packets.C2SAttackPacket(dev.ultreon.quantum.entity.Entity)"""
        val = __C2SAttackPacket(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.network.packets.AddPermissionPacket
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = __import_once__("pyquantum.network.client")

import dev.ultreon.quantum.api.commands.perms.Permission as __Permission
__Permission = __Permission
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

try:
    from pyquantum.api.commands import perms
except ImportError:
    perms = __import_once__("pyquantum.api.commands.perms")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.network.packets.AddPermissionPacket as __AddPermissionPacket
__AddPermissionPacket = __AddPermissionPacket
from builtins import int
 
class AddPermissionPacket():
    """dev.ultreon.quantum.network.packets.AddPermissionPacket"""
 
    @staticmethod
    def __wrap(java_value: __AddPermissionPacket) -> 'AddPermissionPacket':
        return AddPermissionPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AddPermissionPacket):
        """
        Dynamic initializer for AddPermissionPacket.
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
    def __init__(self, arg0: 'Permission'):
        """public dev.ultreon.quantum.network.packets.AddPermissionPacket(dev.ultreon.quantum.api.commands.perms.Permission)"""
        val = __AddPermissionPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getPermission(self) -> 'perms.Permission':
        """public dev.ultreon.quantum.api.commands.perms.Permission dev.ultreon.quantum.network.packets.AddPermissionPacket.getPermission()"""
        return 'perms.Permission'.__wrap(super(AddPermissionPacket, self).getPermission())

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
        """public dev.ultreon.quantum.network.packets.AddPermissionPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __AddPermissionPacket(arg0)
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
        """public void dev.ultreon.quantum.network.packets.AddPermissionPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__AddPermissionPacket, self).toBytes(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.AddPermissionPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(__AddPermissionPacket, self).handle(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.network.packets.Packet
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.packets.Packet as __Packet
__Packet = __Packet
from abc import abstractmethod, ABC
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
 
class Packet(ABC):
    """dev.ultreon.quantum.network.packets.Packet"""
 
    @staticmethod
    def __wrap(java_value: __Packet) -> 'Packet':
        return Packet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Packet):
        """
        Dynamic initializer for Packet.
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

    @abstractmethod
    def handle(self, arg0: 'PacketContext', arg1: 'PacketHandler'):
        """public abstract void dev.ultreon.quantum.network.packets.Packet.handle(dev.ultreon.quantum.network.PacketContext,T)"""
        pass

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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.packets.Packet()"""
        val = __Packet()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @abstractmethod
    def toBytes(self, arg0: 'PacketIO'):
        """public abstract void dev.ultreon.quantum.network.packets.Packet.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        pass

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.packets.Packet()"""
        val = __Packet()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.network.packets.AbilitiesPacket
import dev.ultreon.quantum.network.packets.AbilitiesPacket as __AbilitiesPacket
__AbilitiesPacket = __AbilitiesPacket
from abc import abstractmethod, ABC
 
class AbilitiesPacket(ABC):
    """dev.ultreon.quantum.network.packets.AbilitiesPacket"""
 
    @staticmethod
    def __wrap(java_value: __AbilitiesPacket) -> 'AbilitiesPacket':
        return AbilitiesPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbilitiesPacket):
        """
        Dynamic initializer for AbilitiesPacket.
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
    def isFlying(self, ):
        """public abstract boolean dev.ultreon.quantum.network.packets.AbilitiesPacket.isFlying()"""
        pass

    @abstractmethod
    def isInstaMine(self, ):
        """public abstract boolean dev.ultreon.quantum.network.packets.AbilitiesPacket.isInstaMine()"""
        pass

    @abstractmethod
    def allowFlight(self, ):
        """public abstract boolean dev.ultreon.quantum.network.packets.AbilitiesPacket.allowFlight()"""
        pass

    @abstractmethod
    def isInvincible(self, ):
        """public abstract boolean dev.ultreon.quantum.network.packets.AbilitiesPacket.isInvincible()"""
        pass