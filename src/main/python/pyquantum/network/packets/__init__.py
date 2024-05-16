from __future__ import annotations
from overload import overload


 
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

import dev.ultreon.quantum.network.packets.InitialPermissionsPacket as _InitialPermissionsPacket
_InitialPermissionsPacket = _InitialPermissionsPacket
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InitialPermissionsPacket():
    """dev.ultreon.quantum.network.packets.InitialPermissionsPacket"""
 
    @staticmethod
    def _wrap(java_value: _InitialPermissionsPacket) -> 'InitialPermissionsPacket':
        return InitialPermissionsPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InitialPermissionsPacket):
        """
        Dynamic initializer for InitialPermissionsPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InitialPermissionsPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InitialPermissionsPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getPermissions(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.api.commands.perms.Permission> dev.ultreon.quantum.network.packets.InitialPermissionsPacket.getPermissions()"""
        return 'List'._wrap(super(InitialPermissionsPacket, self).getPermissions())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.InitialPermissionsPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _InitialPermissionsPacket(arg0)
        self.__wrapper = val

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.InitialPermissionsPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_InitialPermissionsPacket, self).handle(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'List'):
        """public dev.ultreon.quantum.network.packets.InitialPermissionsPacket(java.util.List<dev.ultreon.quantum.api.commands.perms.Permission>)"""
        val = _InitialPermissionsPacket(arg0)
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
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.InitialPermissionsPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_InitialPermissionsPacket, self).toBytes(arg0)

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

 
 
 
# CLASS: dev.ultreon.quantum.network.packets.InitialPermissionsPacket
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

import dev.ultreon.quantum.network.packets.InitialPermissionsPacket as _InitialPermissionsPacket
_InitialPermissionsPacket = _InitialPermissionsPacket
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InitialPermissionsPacket():
    """dev.ultreon.quantum.network.packets.InitialPermissionsPacket"""
 
    @staticmethod
    def _wrap(java_value: _InitialPermissionsPacket) -> 'InitialPermissionsPacket':
        return InitialPermissionsPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InitialPermissionsPacket):
        """
        Dynamic initializer for InitialPermissionsPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InitialPermissionsPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InitialPermissionsPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getPermissions(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.api.commands.perms.Permission> dev.ultreon.quantum.network.packets.InitialPermissionsPacket.getPermissions()"""
        return 'List'._wrap(super(InitialPermissionsPacket, self).getPermissions())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.InitialPermissionsPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _InitialPermissionsPacket(arg0)
        self.__wrapper = val

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.InitialPermissionsPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_InitialPermissionsPacket, self).handle(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'List'):
        """public dev.ultreon.quantum.network.packets.InitialPermissionsPacket(java.util.List<dev.ultreon.quantum.api.commands.perms.Permission>)"""
        val = _InitialPermissionsPacket(arg0)
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
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.InitialPermissionsPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_InitialPermissionsPacket, self).toBytes(arg0)

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

 
 
 
# CLASS: dev.ultreon.quantum.network.packets.InitialPermissionsPacket 
 
 
# CLASS: dev.ultreon.quantum.network.packets.RemovePermissionPacket
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

try:
    from pyquantum.api.commands import perms
except ImportError:
    perms = _import_once("pyquantum.api.commands.perms")

import java.lang.Integer as _int
import dev.ultreon.quantum.network.packets.RemovePermissionPacket as _RemovePermissionPacket
_RemovePermissionPacket = _RemovePermissionPacket
import dev.ultreon.quantum.api.commands.perms.Permission as _Permission
_Permission = _Permission
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RemovePermissionPacket():
    """dev.ultreon.quantum.network.packets.RemovePermissionPacket"""
 
    @staticmethod
    def _wrap(java_value: _RemovePermissionPacket) -> 'RemovePermissionPacket':
        return RemovePermissionPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RemovePermissionPacket):
        """
        Dynamic initializer for RemovePermissionPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RemovePermissionPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RemovePermissionPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.RemovePermissionPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_RemovePermissionPacket, self).handle(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getPermission(self) -> 'perms.Permission':
        """public dev.ultreon.quantum.api.commands.perms.Permission dev.ultreon.quantum.network.packets.RemovePermissionPacket.getPermission()"""
        return 'perms.Permission'._wrap(super(RemovePermissionPacket, self).getPermission())

    @overload
    def __init__(self, arg0: 'Permission'):
        """public dev.ultreon.quantum.network.packets.RemovePermissionPacket(dev.ultreon.quantum.api.commands.perms.Permission)"""
        val = _RemovePermissionPacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.RemovePermissionPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _RemovePermissionPacket(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.RemovePermissionPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_RemovePermissionPacket, self).toBytes(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.network.packets.C2SAttackPacket
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.network import server
except ImportError:
    server = _import_once("pyquantum.network.server")

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
import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import dev.ultreon.quantum.network.packets.C2SAttackPacket as _C2SAttackPacket
_C2SAttackPacket = _C2SAttackPacket
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class C2SAttackPacket():
    """dev.ultreon.quantum.network.packets.C2SAttackPacket"""
 
    @staticmethod
    def _wrap(java_value: _C2SAttackPacket) -> 'C2SAttackPacket':
        return C2SAttackPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _C2SAttackPacket):
        """
        Dynamic initializer for C2SAttackPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_C2SAttackPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_C2SAttackPacket__wrapper":
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
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.packets.C2SAttackPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_C2SAttackPacket, self).toBytes(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameServerPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.C2SAttackPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.server.InGameServerPacketHandler)"""
        super(_C2SAttackPacket, self).handle(arg0, arg1)

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
        """public dev.ultreon.quantum.network.packets.C2SAttackPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _C2SAttackPacket(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Entity'):
        """public dev.ultreon.quantum.network.packets.C2SAttackPacket(dev.ultreon.quantum.entity.Entity)"""
        val = _C2SAttackPacket(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.network.packets.AddPermissionPacket
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
import dev.ultreon.quantum.network.packets.AddPermissionPacket as _AddPermissionPacket
_AddPermissionPacket = _AddPermissionPacket
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

try:
    from pyquantum.api.commands import perms
except ImportError:
    perms = _import_once("pyquantum.api.commands.perms")

import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.perms.Permission as _Permission
_Permission = _Permission
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AddPermissionPacket():
    """dev.ultreon.quantum.network.packets.AddPermissionPacket"""
 
    @staticmethod
    def _wrap(java_value: _AddPermissionPacket) -> 'AddPermissionPacket':
        return AddPermissionPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AddPermissionPacket):
        """
        Dynamic initializer for AddPermissionPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AddPermissionPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AddPermissionPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'InGameClientPacketHandler'):
        """public void dev.ultreon.quantum.network.packets.AddPermissionPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.InGameClientPacketHandler)"""
        super(_AddPermissionPacket, self).handle(arg0, arg1)

    @overload
    def getPermission(self) -> 'perms.Permission':
        """public dev.ultreon.quantum.api.commands.perms.Permission dev.ultreon.quantum.network.packets.AddPermissionPacket.getPermission()"""
        return 'perms.Permission'._wrap(super(AddPermissionPacket, self).getPermission())

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
    def __init__(self, arg0: 'Permission'):
        """public dev.ultreon.quantum.network.packets.AddPermissionPacket(dev.ultreon.quantum.api.commands.perms.Permission)"""
        val = _AddPermissionPacket(arg0)
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
        """public void dev.ultreon.quantum.network.packets.AddPermissionPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(_AddPermissionPacket, self).toBytes(arg0)

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.packets.AddPermissionPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = _AddPermissionPacket(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.network.packets.Packet
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.network.packets.Packet as _Packet
_Packet = _Packet
from abc import abstractmethod, ABC
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
 
class Packet():
    """dev.ultreon.quantum.network.packets.Packet"""
 
    @staticmethod
    def _wrap(java_value: _Packet) -> 'Packet':
        return Packet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Packet):
        """
        Dynamic initializer for Packet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Packet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Packet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def handle(self, arg0: 'PacketContext', arg1: 'PacketHandler'):
        """public abstract void dev.ultreon.quantum.network.packets.Packet.handle(dev.ultreon.quantum.network.PacketContext,T)"""
        pass

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.packets.Packet()"""
        val = _Packet()
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
    def __init__(self, ):
        """public dev.ultreon.quantum.network.packets.Packet()"""
        val = _Packet()
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

    @abstractmethod
    def toBytes(self, arg0: 'PacketIO'):
        """public abstract void dev.ultreon.quantum.network.packets.Packet.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.packets.AbilitiesPacket
import dev.ultreon.quantum.network.packets.AbilitiesPacket as _AbilitiesPacket
_AbilitiesPacket = _AbilitiesPacket
from abc import abstractmethod, ABC
 
class AbilitiesPacket():
    """dev.ultreon.quantum.network.packets.AbilitiesPacket"""
 
    @staticmethod
    def _wrap(java_value: _AbilitiesPacket) -> 'AbilitiesPacket':
        return AbilitiesPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbilitiesPacket):
        """
        Dynamic initializer for AbilitiesPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbilitiesPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbilitiesPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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