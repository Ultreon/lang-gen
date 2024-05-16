from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.quantum.client.sound.ClientSoundRegistry as __ClientSoundRegistry
__ClientSoundRegistry = __ClientSoundRegistry
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.audio.Sound as __Sound
__Sound = __Sound
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import audio
except ImportError:
    audio = __import_once__("pygdx.audio")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ClientSoundRegistry():
    """dev.ultreon.quantum.client.sound.ClientSoundRegistry"""
 
    @staticmethod
    def __wrap(java_value: __ClientSoundRegistry) -> 'ClientSoundRegistry':
        return ClientSoundRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientSoundRegistry):
        """
        Dynamic initializer for ClientSoundRegistry.
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
    def getSound(self, arg0: 'Identifier') -> 'audio.Sound':
        """public com.badlogic.gdx.audio.Sound dev.ultreon.quantum.client.sound.ClientSoundRegistry.getSound(dev.ultreon.quantum.util.Identifier)"""
        return 'audio.Sound'.__wrap(super(__ClientSoundRegistry, self).getSound(arg0))

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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.sound.ClientSoundRegistry()"""
        val = __ClientSoundRegistry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.sound.ClientSoundRegistry()"""
        val = __ClientSoundRegistry()
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
    def registerSounds(self):
        """public void dev.ultreon.quantum.client.sound.ClientSoundRegistry.registerSounds()"""
        super(ClientSoundRegistry, self).registerSounds()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.sound.ClientSoundRegistry
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.quantum.client.sound.ClientSoundRegistry as __ClientSoundRegistry
__ClientSoundRegistry = __ClientSoundRegistry
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.audio.Sound as __Sound
__Sound = __Sound
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import audio
except ImportError:
    audio = __import_once__("pygdx.audio")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ClientSoundRegistry():
    """dev.ultreon.quantum.client.sound.ClientSoundRegistry"""
 
    @staticmethod
    def __wrap(java_value: __ClientSoundRegistry) -> 'ClientSoundRegistry':
        return ClientSoundRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientSoundRegistry):
        """
        Dynamic initializer for ClientSoundRegistry.
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
    def getSound(self, arg0: 'Identifier') -> 'audio.Sound':
        """public com.badlogic.gdx.audio.Sound dev.ultreon.quantum.client.sound.ClientSoundRegistry.getSound(dev.ultreon.quantum.util.Identifier)"""
        return 'audio.Sound'.__wrap(super(__ClientSoundRegistry, self).getSound(arg0))

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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.sound.ClientSoundRegistry()"""
        val = __ClientSoundRegistry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.sound.ClientSoundRegistry()"""
        val = __ClientSoundRegistry()
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
    def registerSounds(self):
        """public void dev.ultreon.quantum.client.sound.ClientSoundRegistry.registerSounds()"""
        super(ClientSoundRegistry, self).registerSounds()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.sound.ClientSoundRegistry