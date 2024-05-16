from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import java.util.UUID as UUID
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.client import player
except ImportError:
    player = __import_once__("pyquantum.client.player")

import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

import java.util.Collection as Collection
import dev.ultreon.quantum.client.multiplayer.MultiplayerData as __MultiplayerData
__MultiplayerData = __MultiplayerData
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.player.RemotePlayer as __RemotePlayer
__RemotePlayer = __RemotePlayer
from builtins import bool
from builtins import int
 
class MultiplayerData():
    """dev.ultreon.quantum.client.multiplayer.MultiplayerData"""
 
    @staticmethod
    def __wrap(java_value: __MultiplayerData) -> 'MultiplayerData':
        return MultiplayerData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MultiplayerData):
        """
        Dynamic initializer for MultiplayerData.
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
    def clear(self):
        """public void dev.ultreon.quantum.client.multiplayer.MultiplayerData.clear()"""
        super(MultiplayerData, self).clear()

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
    def getRemotePlayers(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.client.player.RemotePlayer> dev.ultreon.quantum.client.multiplayer.MultiplayerData.getRemotePlayers()"""
        return 'Collection'.__wrap(super(MultiplayerData, self).getRemotePlayers())

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
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.multiplayer.MultiplayerData(dev.ultreon.quantum.client.QuantumClient)"""
        val = __MultiplayerData(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addPlayer(self, arg0: 'UUID', arg1: str, arg2: 'Vec3d') -> 'player.RemotePlayer':
        """public dev.ultreon.quantum.client.player.RemotePlayer dev.ultreon.quantum.client.multiplayer.MultiplayerData.addPlayer(java.util.UUID,java.lang.String,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'player.RemotePlayer'.__wrap(super(__MultiplayerData, self).addPlayer(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def removePlayer(self, arg0: 'UUID'):
        """public void dev.ultreon.quantum.client.multiplayer.MultiplayerData.removePlayer(java.util.UUID)"""
        super(__MultiplayerData, self).removePlayer(arg0)

    @overload
    def getRemotePlayerByUuid(self, arg0: 'UUID') -> 'player.RemotePlayer':
        """public dev.ultreon.quantum.client.player.RemotePlayer dev.ultreon.quantum.client.multiplayer.MultiplayerData.getRemotePlayerByUuid(java.util.UUID)"""
        return 'player.RemotePlayer'.__wrap(super(__MultiplayerData, self).getRemotePlayerByUuid(arg0))

    @overload
    def getRemotePlayerByName(self, arg0: str) -> 'player.RemotePlayer':
        """public dev.ultreon.quantum.client.player.RemotePlayer dev.ultreon.quantum.client.multiplayer.MultiplayerData.getRemotePlayerByName(java.lang.String)"""
        return 'player.RemotePlayer'.__wrap(super(__MultiplayerData, self).getRemotePlayerByName(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.multiplayer.MultiplayerData
from pyquantum_helper import import_once as __import_once__
import java.util.UUID as UUID
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.client import player
except ImportError:
    player = __import_once__("pyquantum.client.player")

import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

import java.util.Collection as Collection
import dev.ultreon.quantum.client.multiplayer.MultiplayerData as __MultiplayerData
__MultiplayerData = __MultiplayerData
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.player.RemotePlayer as __RemotePlayer
__RemotePlayer = __RemotePlayer
from builtins import bool
from builtins import int
 
class MultiplayerData():
    """dev.ultreon.quantum.client.multiplayer.MultiplayerData"""
 
    @staticmethod
    def __wrap(java_value: __MultiplayerData) -> 'MultiplayerData':
        return MultiplayerData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MultiplayerData):
        """
        Dynamic initializer for MultiplayerData.
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
    def clear(self):
        """public void dev.ultreon.quantum.client.multiplayer.MultiplayerData.clear()"""
        super(MultiplayerData, self).clear()

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
    def getRemotePlayers(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.client.player.RemotePlayer> dev.ultreon.quantum.client.multiplayer.MultiplayerData.getRemotePlayers()"""
        return 'Collection'.__wrap(super(MultiplayerData, self).getRemotePlayers())

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
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.multiplayer.MultiplayerData(dev.ultreon.quantum.client.QuantumClient)"""
        val = __MultiplayerData(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addPlayer(self, arg0: 'UUID', arg1: str, arg2: 'Vec3d') -> 'player.RemotePlayer':
        """public dev.ultreon.quantum.client.player.RemotePlayer dev.ultreon.quantum.client.multiplayer.MultiplayerData.addPlayer(java.util.UUID,java.lang.String,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'player.RemotePlayer'.__wrap(super(__MultiplayerData, self).addPlayer(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def removePlayer(self, arg0: 'UUID'):
        """public void dev.ultreon.quantum.client.multiplayer.MultiplayerData.removePlayer(java.util.UUID)"""
        super(__MultiplayerData, self).removePlayer(arg0)

    @overload
    def getRemotePlayerByUuid(self, arg0: 'UUID') -> 'player.RemotePlayer':
        """public dev.ultreon.quantum.client.player.RemotePlayer dev.ultreon.quantum.client.multiplayer.MultiplayerData.getRemotePlayerByUuid(java.util.UUID)"""
        return 'player.RemotePlayer'.__wrap(super(__MultiplayerData, self).getRemotePlayerByUuid(arg0))

    @overload
    def getRemotePlayerByName(self, arg0: str) -> 'player.RemotePlayer':
        """public dev.ultreon.quantum.client.player.RemotePlayer dev.ultreon.quantum.client.multiplayer.MultiplayerData.getRemotePlayerByName(java.lang.String)"""
        return 'player.RemotePlayer'.__wrap(super(__MultiplayerData, self).getRemotePlayerByName(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.multiplayer.MultiplayerData