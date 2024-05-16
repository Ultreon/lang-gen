from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
import dev.ultreon.quantum.sound.event.SoundEvents as _SoundEvents
_SoundEvents = _SoundEvents
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SoundEvents():
    """dev.ultreon.quantum.sound.event.SoundEvents"""
 
    @staticmethod
    def _wrap(java_value: _SoundEvents) -> 'SoundEvents':
        return SoundEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SoundEvents):
        """
        Dynamic initializer for SoundEvents.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SoundEvents__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SoundEvents__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.world.SoundEvent dev.ultreon.quantum.sound.event.SoundEvents.BUTTON_RELEASE
    BUTTON_RELEASE: 'world.SoundEvent' = _wrap(_world.SoundEvent.BUTTON_RELEASE)

    # public static final dev.ultreon.quantum.world.SoundEvent dev.ultreon.quantum.sound.event.SoundEvents.BUTTON_PRESS
    BUTTON_PRESS: 'world.SoundEvent' = _wrap(_world.SoundEvent.BUTTON_PRESS)

    # public static final dev.ultreon.quantum.world.SoundEvent dev.ultreon.quantum.sound.event.SoundEvents.SCREENSHOT
    SCREENSHOT: 'world.SoundEvent' = _wrap(_world.SoundEvent.SCREENSHOT)

    # public static final dev.ultreon.quantum.world.SoundEvent dev.ultreon.quantum.sound.event.SoundEvents.PLAYER_HURT
    PLAYER_HURT: 'world.SoundEvent' = _wrap(_world.SoundEvent.PLAYER_HURT)


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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.sound.event.SoundEvents()"""
        val = _SoundEvents()
        self.__wrapper = val

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.sound.event.SoundEvents.init()"""
            _SoundEvents.init()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

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
    def __init__(self, ):
        """public dev.ultreon.quantum.sound.event.SoundEvents()"""
        val = _SoundEvents()
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.quantum.sound.event.SoundEvents
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
import dev.ultreon.quantum.sound.event.SoundEvents as _SoundEvents
_SoundEvents = _SoundEvents
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SoundEvents():
    """dev.ultreon.quantum.sound.event.SoundEvents"""
 
    @staticmethod
    def _wrap(java_value: _SoundEvents) -> 'SoundEvents':
        return SoundEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SoundEvents):
        """
        Dynamic initializer for SoundEvents.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SoundEvents__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SoundEvents__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.world.SoundEvent dev.ultreon.quantum.sound.event.SoundEvents.BUTTON_RELEASE
    BUTTON_RELEASE: 'world.SoundEvent' = _wrap(_world.SoundEvent.BUTTON_RELEASE)

    # public static final dev.ultreon.quantum.world.SoundEvent dev.ultreon.quantum.sound.event.SoundEvents.BUTTON_PRESS
    BUTTON_PRESS: 'world.SoundEvent' = _wrap(_world.SoundEvent.BUTTON_PRESS)

    # public static final dev.ultreon.quantum.world.SoundEvent dev.ultreon.quantum.sound.event.SoundEvents.SCREENSHOT
    SCREENSHOT: 'world.SoundEvent' = _wrap(_world.SoundEvent.SCREENSHOT)

    # public static final dev.ultreon.quantum.world.SoundEvent dev.ultreon.quantum.sound.event.SoundEvents.PLAYER_HURT
    PLAYER_HURT: 'world.SoundEvent' = _wrap(_world.SoundEvent.PLAYER_HURT)


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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.sound.event.SoundEvents()"""
        val = _SoundEvents()
        self.__wrapper = val

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.sound.event.SoundEvents.init()"""
            _SoundEvents.init()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

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
    def __init__(self, ):
        """public dev.ultreon.quantum.sound.event.SoundEvents()"""
        val = _SoundEvents()
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.quantum.sound.event.SoundEvents