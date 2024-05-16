from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import java.util.UUID as UUID
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.client import player
except ImportError:
    player = _import_once("pyquantum.client.player")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

import java.util.Collection as Collection
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import dev.ultreon.quantum.client.multiplayer.MultiplayerData as _MultiplayerData
_MultiplayerData = _MultiplayerData
from builtins import bool
import dev.ultreon.quantum.client.player.RemotePlayer as _RemotePlayer
_RemotePlayer = _RemotePlayer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MultiplayerData():
    """dev.ultreon.quantum.client.multiplayer.MultiplayerData"""
 
    @staticmethod
    def _wrap(java_value: _MultiplayerData) -> 'MultiplayerData':
        return MultiplayerData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MultiplayerData):
        """
        Dynamic initializer for MultiplayerData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MultiplayerData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MultiplayerData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def removePlayer(self, arg0: 'UUID'):
        """public void dev.ultreon.quantum.client.multiplayer.MultiplayerData.removePlayer(java.util.UUID)"""
        super(_MultiplayerData, self).removePlayer(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.multiplayer.MultiplayerData(dev.ultreon.quantum.client.QuantumClient)"""
        val = _MultiplayerData(arg0)
        self.__wrapper = val

    @overload
    def clear(self):
        """public void dev.ultreon.quantum.client.multiplayer.MultiplayerData.clear()"""
        super(MultiplayerData, self).clear()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def addPlayer(self, arg0: 'UUID', arg1: str, arg2: 'Vec3d') -> 'player.RemotePlayer':
        """public dev.ultreon.quantum.client.player.RemotePlayer dev.ultreon.quantum.client.multiplayer.MultiplayerData.addPlayer(java.util.UUID,java.lang.String,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'player.RemotePlayer'._wrap(super(_MultiplayerData, self).addPlayer(arg0, arg1, arg2))

    @overload
    def getRemotePlayerByUuid(self, arg0: 'UUID') -> 'player.RemotePlayer':
        """public dev.ultreon.quantum.client.player.RemotePlayer dev.ultreon.quantum.client.multiplayer.MultiplayerData.getRemotePlayerByUuid(java.util.UUID)"""
        return 'player.RemotePlayer'._wrap(super(_MultiplayerData, self).getRemotePlayerByUuid(arg0))

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
    def getRemotePlayers(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.client.player.RemotePlayer> dev.ultreon.quantum.client.multiplayer.MultiplayerData.getRemotePlayers()"""
        return 'Collection'._wrap(super(MultiplayerData, self).getRemotePlayers())

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
    def getRemotePlayerByName(self, arg0: str) -> 'player.RemotePlayer':
        """public dev.ultreon.quantum.client.player.RemotePlayer dev.ultreon.quantum.client.multiplayer.MultiplayerData.getRemotePlayerByName(java.lang.String)"""
        return 'player.RemotePlayer'._wrap(super(_MultiplayerData, self).getRemotePlayerByName(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.multiplayer.MultiplayerData
from pyquantum_helper import import_once as _import_once
import java.util.UUID as UUID
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.client import player
except ImportError:
    player = _import_once("pyquantum.client.player")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

import java.util.Collection as Collection
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import dev.ultreon.quantum.client.multiplayer.MultiplayerData as _MultiplayerData
_MultiplayerData = _MultiplayerData
from builtins import bool
import dev.ultreon.quantum.client.player.RemotePlayer as _RemotePlayer
_RemotePlayer = _RemotePlayer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MultiplayerData():
    """dev.ultreon.quantum.client.multiplayer.MultiplayerData"""
 
    @staticmethod
    def _wrap(java_value: _MultiplayerData) -> 'MultiplayerData':
        return MultiplayerData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MultiplayerData):
        """
        Dynamic initializer for MultiplayerData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MultiplayerData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MultiplayerData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def removePlayer(self, arg0: 'UUID'):
        """public void dev.ultreon.quantum.client.multiplayer.MultiplayerData.removePlayer(java.util.UUID)"""
        super(_MultiplayerData, self).removePlayer(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'QuantumClient'):
        """public dev.ultreon.quantum.client.multiplayer.MultiplayerData(dev.ultreon.quantum.client.QuantumClient)"""
        val = _MultiplayerData(arg0)
        self.__wrapper = val

    @overload
    def clear(self):
        """public void dev.ultreon.quantum.client.multiplayer.MultiplayerData.clear()"""
        super(MultiplayerData, self).clear()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def addPlayer(self, arg0: 'UUID', arg1: str, arg2: 'Vec3d') -> 'player.RemotePlayer':
        """public dev.ultreon.quantum.client.player.RemotePlayer dev.ultreon.quantum.client.multiplayer.MultiplayerData.addPlayer(java.util.UUID,java.lang.String,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'player.RemotePlayer'._wrap(super(_MultiplayerData, self).addPlayer(arg0, arg1, arg2))

    @overload
    def getRemotePlayerByUuid(self, arg0: 'UUID') -> 'player.RemotePlayer':
        """public dev.ultreon.quantum.client.player.RemotePlayer dev.ultreon.quantum.client.multiplayer.MultiplayerData.getRemotePlayerByUuid(java.util.UUID)"""
        return 'player.RemotePlayer'._wrap(super(_MultiplayerData, self).getRemotePlayerByUuid(arg0))

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
    def getRemotePlayers(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.client.player.RemotePlayer> dev.ultreon.quantum.client.multiplayer.MultiplayerData.getRemotePlayers()"""
        return 'Collection'._wrap(super(MultiplayerData, self).getRemotePlayers())

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
    def getRemotePlayerByName(self, arg0: str) -> 'player.RemotePlayer':
        """public dev.ultreon.quantum.client.player.RemotePlayer dev.ultreon.quantum.client.multiplayer.MultiplayerData.getRemotePlayerByName(java.lang.String)"""
        return 'player.RemotePlayer'._wrap(super(_MultiplayerData, self).getRemotePlayerByName(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.multiplayer.MultiplayerData