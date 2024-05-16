from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client.input import util
except ImportError:
    util = __import_once__("pyquantum.client.input.util")

try:
    import pygson
except ImportError:
    pygson = __import_once__("pygson")

from builtins import str
import dev.ultreon.quantum.client.input.controller.ButtonBinding as __ButtonBinding
__ButtonBinding = __ButtonBinding
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.input.util.ControllerButton as __ControllerButton
__ControllerButton = __ControllerButton
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = __import_once__("pycorelibs.commons.v0")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ButtonBinding():
    """dev.ultreon.quantum.client.input.controller.ButtonBinding"""
 
    @staticmethod
    def __wrap(java_value: __ButtonBinding) -> 'ButtonBinding':
        return ButtonBinding(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ButtonBinding):
        """
        Dynamic initializer for ButtonBinding.
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
    def isJustPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.controller.ButtonBinding.isJustPressed()"""
        return bool.__wrap(super(ButtonBinding, self).isJustPressed())

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
    def isReleased(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.controller.ButtonBinding.isReleased()"""
        return bool.__wrap(super(ButtonBinding, self).isReleased())

    @overload
    def setButton(self, arg0: 'ControllerButton'):
        """public void dev.ultreon.quantum.client.input.controller.ButtonBinding.setButton(dev.ultreon.quantum.client.input.util.ControllerButton)"""
        super(__ButtonBinding, self).setButton(arg0)

    @overload
    def getButton(self) -> 'util.ControllerButton':
        """public dev.ultreon.quantum.client.input.util.ControllerButton dev.ultreon.quantum.client.input.controller.ButtonBinding.getButton()"""
        return 'util.ControllerButton'.__wrap(super(ButtonBinding, self).getButton())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Identifier', arg1: 'ControllerButton'):
        """public dev.ultreon.quantum.client.input.controller.ButtonBinding(dev.ultreon.libs.commons.v0.Identifier,dev.ultreon.quantum.client.input.util.ControllerButton)"""
        val = __ButtonBinding(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.controller.ButtonBinding.isPressed()"""
        return bool.__wrap(super(ButtonBinding, self).isPressed())

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
    def save(self, arg0: 'JsonObject'):
        """public final void dev.ultreon.quantum.client.input.controller.ButtonBinding.save(com.google.gson.JsonObject)"""
        super(__ButtonBinding, self).save(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.input.controller.ButtonBinding
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client.input import util
except ImportError:
    util = __import_once__("pyquantum.client.input.util")

try:
    import pygson
except ImportError:
    pygson = __import_once__("pygson")

from builtins import str
import dev.ultreon.quantum.client.input.controller.ButtonBinding as __ButtonBinding
__ButtonBinding = __ButtonBinding
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.input.util.ControllerButton as __ControllerButton
__ControllerButton = __ControllerButton
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = __import_once__("pycorelibs.commons.v0")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ButtonBinding():
    """dev.ultreon.quantum.client.input.controller.ButtonBinding"""
 
    @staticmethod
    def __wrap(java_value: __ButtonBinding) -> 'ButtonBinding':
        return ButtonBinding(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ButtonBinding):
        """
        Dynamic initializer for ButtonBinding.
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
    def isJustPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.controller.ButtonBinding.isJustPressed()"""
        return bool.__wrap(super(ButtonBinding, self).isJustPressed())

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
    def isReleased(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.controller.ButtonBinding.isReleased()"""
        return bool.__wrap(super(ButtonBinding, self).isReleased())

    @overload
    def setButton(self, arg0: 'ControllerButton'):
        """public void dev.ultreon.quantum.client.input.controller.ButtonBinding.setButton(dev.ultreon.quantum.client.input.util.ControllerButton)"""
        super(__ButtonBinding, self).setButton(arg0)

    @overload
    def getButton(self) -> 'util.ControllerButton':
        """public dev.ultreon.quantum.client.input.util.ControllerButton dev.ultreon.quantum.client.input.controller.ButtonBinding.getButton()"""
        return 'util.ControllerButton'.__wrap(super(ButtonBinding, self).getButton())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Identifier', arg1: 'ControllerButton'):
        """public dev.ultreon.quantum.client.input.controller.ButtonBinding(dev.ultreon.libs.commons.v0.Identifier,dev.ultreon.quantum.client.input.util.ControllerButton)"""
        val = __ButtonBinding(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.controller.ButtonBinding.isPressed()"""
        return bool.__wrap(super(ButtonBinding, self).isPressed())

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
    def save(self, arg0: 'JsonObject'):
        """public final void dev.ultreon.quantum.client.input.controller.ButtonBinding.save(com.google.gson.JsonObject)"""
        super(__ButtonBinding, self).save(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.input.controller.ButtonBinding