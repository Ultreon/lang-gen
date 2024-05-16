from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.input import util
except ImportError:
    util = _import_once("pyquantum.client.input.util")

try:
    import pygson
except ImportError:
    pygson = _import_once("pygson")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.input.util.ControllerButton as _ControllerButton
_ControllerButton = _ControllerButton
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = _import_once("pycorelibs.commons.v0")

from builtins import bool
import dev.ultreon.quantum.client.input.controller.ButtonBinding as _ButtonBinding
_ButtonBinding = _ButtonBinding
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ButtonBinding():
    """dev.ultreon.quantum.client.input.controller.ButtonBinding"""
 
    @staticmethod
    def _wrap(java_value: _ButtonBinding) -> 'ButtonBinding':
        return ButtonBinding(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ButtonBinding):
        """
        Dynamic initializer for ButtonBinding.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ButtonBinding__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ButtonBinding__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'Identifier', arg1: 'ControllerButton'):
        """public dev.ultreon.quantum.client.input.controller.ButtonBinding(dev.ultreon.libs.commons.v0.Identifier,dev.ultreon.quantum.client.input.util.ControllerButton)"""
        val = _ButtonBinding(arg0, arg1)
        self.__wrapper = val

    @overload
    def save(self, arg0: 'JsonObject'):
        """public final void dev.ultreon.quantum.client.input.controller.ButtonBinding.save(com.google.gson.JsonObject)"""
        super(_ButtonBinding, self).save(arg0)

    @overload
    def isReleased(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.controller.ButtonBinding.isReleased()"""
        return bool._wrap(super(ButtonBinding, self).isReleased())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setButton(self, arg0: 'ControllerButton'):
        """public void dev.ultreon.quantum.client.input.controller.ButtonBinding.setButton(dev.ultreon.quantum.client.input.util.ControllerButton)"""
        super(_ButtonBinding, self).setButton(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.controller.ButtonBinding.isPressed()"""
        return bool._wrap(super(ButtonBinding, self).isPressed())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def isJustPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.controller.ButtonBinding.isJustPressed()"""
        return bool._wrap(super(ButtonBinding, self).isJustPressed())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getButton(self) -> 'util.ControllerButton':
        """public dev.ultreon.quantum.client.input.util.ControllerButton dev.ultreon.quantum.client.input.controller.ButtonBinding.getButton()"""
        return 'util.ControllerButton'._wrap(super(ButtonBinding, self).getButton())

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

 
 
 
# CLASS: dev.ultreon.quantum.client.input.controller.ButtonBinding
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.input import util
except ImportError:
    util = _import_once("pyquantum.client.input.util")

try:
    import pygson
except ImportError:
    pygson = _import_once("pygson")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.input.util.ControllerButton as _ControllerButton
_ControllerButton = _ControllerButton
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = _import_once("pycorelibs.commons.v0")

from builtins import bool
import dev.ultreon.quantum.client.input.controller.ButtonBinding as _ButtonBinding
_ButtonBinding = _ButtonBinding
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ButtonBinding():
    """dev.ultreon.quantum.client.input.controller.ButtonBinding"""
 
    @staticmethod
    def _wrap(java_value: _ButtonBinding) -> 'ButtonBinding':
        return ButtonBinding(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ButtonBinding):
        """
        Dynamic initializer for ButtonBinding.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ButtonBinding__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ButtonBinding__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'Identifier', arg1: 'ControllerButton'):
        """public dev.ultreon.quantum.client.input.controller.ButtonBinding(dev.ultreon.libs.commons.v0.Identifier,dev.ultreon.quantum.client.input.util.ControllerButton)"""
        val = _ButtonBinding(arg0, arg1)
        self.__wrapper = val

    @overload
    def save(self, arg0: 'JsonObject'):
        """public final void dev.ultreon.quantum.client.input.controller.ButtonBinding.save(com.google.gson.JsonObject)"""
        super(_ButtonBinding, self).save(arg0)

    @overload
    def isReleased(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.controller.ButtonBinding.isReleased()"""
        return bool._wrap(super(ButtonBinding, self).isReleased())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setButton(self, arg0: 'ControllerButton'):
        """public void dev.ultreon.quantum.client.input.controller.ButtonBinding.setButton(dev.ultreon.quantum.client.input.util.ControllerButton)"""
        super(_ButtonBinding, self).setButton(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.controller.ButtonBinding.isPressed()"""
        return bool._wrap(super(ButtonBinding, self).isPressed())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def isJustPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.controller.ButtonBinding.isJustPressed()"""
        return bool._wrap(super(ButtonBinding, self).isJustPressed())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getButton(self) -> 'util.ControllerButton':
        """public dev.ultreon.quantum.client.input.util.ControllerButton dev.ultreon.quantum.client.input.controller.ButtonBinding.getButton()"""
        return 'util.ControllerButton'._wrap(super(ButtonBinding, self).getButton())

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

 
 
 
# CLASS: dev.ultreon.quantum.client.input.controller.ButtonBinding