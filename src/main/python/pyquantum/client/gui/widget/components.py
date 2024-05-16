from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent as _RangedValueComponent
_RangedValueComponent = _RangedValueComponent
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.component.GameComponent as _GameComponent
_GameComponent = _GameComponent
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RangedValueComponent():
    """dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent"""
 
    @staticmethod
    def _wrap(java_value: _RangedValueComponent) -> 'RangedValueComponent':
        return RangedValueComponent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RangedValueComponent):
        """
        Dynamic initializer for RangedValueComponent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RangedValueComponent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RangedValueComponent__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def get(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent.get()"""
        return int._wrap(super(RangedValueComponent, self).get())

    @overload
    def max(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent.max()"""
        return int._wrap(super(RangedValueComponent, self).max())

    @override
    @overload
    def handleImGui(self, arg0: str, arg1: 'Identifier', arg2: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent.handleImGui(java.lang.String,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_RangedValueComponent, self).handleImGui(arg0, arg1, arg2)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int):
        """public dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent(int,int,int)"""
        val = _RangedValueComponent(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent.set(int)"""
        super(_RangedValueComponent, self).set(_int.valueOf(arg0))

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
    def getHolder(self) -> 'type.Class':
        """public java.lang.Class<? extends T> dev.ultreon.quantum.component.GameComponent.getHolder()"""
        return 'type.Class'._wrap(super(component.GameComponent, self).getHolder())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def min(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent.min()"""
        return int._wrap(super(RangedValueComponent, self).min())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent as _RangedValueComponent
_RangedValueComponent = _RangedValueComponent
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.component.GameComponent as _GameComponent
_GameComponent = _GameComponent
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RangedValueComponent():
    """dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent"""
 
    @staticmethod
    def _wrap(java_value: _RangedValueComponent) -> 'RangedValueComponent':
        return RangedValueComponent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RangedValueComponent):
        """
        Dynamic initializer for RangedValueComponent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RangedValueComponent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RangedValueComponent__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def get(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent.get()"""
        return int._wrap(super(RangedValueComponent, self).get())

    @overload
    def max(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent.max()"""
        return int._wrap(super(RangedValueComponent, self).max())

    @override
    @overload
    def handleImGui(self, arg0: str, arg1: 'Identifier', arg2: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent.handleImGui(java.lang.String,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_RangedValueComponent, self).handleImGui(arg0, arg1, arg2)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int):
        """public dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent(int,int,int)"""
        val = _RangedValueComponent(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent.set(int)"""
        super(_RangedValueComponent, self).set(_int.valueOf(arg0))

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
    def getHolder(self) -> 'type.Class':
        """public java.lang.Class<? extends T> dev.ultreon.quantum.component.GameComponent.getHolder()"""
        return 'type.Class'._wrap(super(component.GameComponent, self).getHolder())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def min(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent.min()"""
        return int._wrap(super(RangedValueComponent, self).min())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.components.TextComponent
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import dev.ultreon.quantum.client.gui.widget.components.TextComponent as _TextComponent
_TextComponent = _TextComponent
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.String as _string
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.lang.Integer as _int
import dev.ultreon.quantum.component.GameComponent as _GameComponent
_GameComponent = _GameComponent
from builtins import bool
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class TextComponent():
    """dev.ultreon.quantum.client.gui.widget.components.TextComponent"""
 
    @staticmethod
    def _wrap(java_value: _TextComponent) -> 'TextComponent':
        return TextComponent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextComponent):
        """
        Dynamic initializer for TextComponent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextComponent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextComponent__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def translate(self, arg0: str, *arg1: object):
        """public void dev.ultreon.quantum.client.gui.widget.components.TextComponent.translate(java.lang.String,java.lang.Object...)"""
        super(_TextComponent, self).translate(arg0, arg1)

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
        """public dev.ultreon.quantum.client.gui.widget.components.TextComponent()"""
        val = _TextComponent()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'TextObject'):
        """public dev.ultreon.quantum.client.gui.widget.components.TextComponent(dev.ultreon.quantum.text.TextObject)"""
        val = _TextComponent(arg0)
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
    def get(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.widget.components.TextComponent.get()"""
        return 'text.TextObject'._wrap(super(TextComponent, self).get())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.widget.components.TextComponent()"""
        val = _TextComponent()
        self.__wrapper = val

    @overload
    def set(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.client.gui.widget.components.TextComponent.set(dev.ultreon.quantum.text.TextObject)"""
        super(_TextComponent, self).set(arg0)

    @overload
    def getRaw(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.components.TextComponent.getRaw()"""
        return str._wrap(super(TextComponent, self).getRaw())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def handleImGui(self, arg0: str, arg1: 'Identifier', arg2: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.components.TextComponent.handleImGui(java.lang.String,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_TextComponent, self).handleImGui(arg0, arg1, arg2)

    @override
    @overload
    def getHolder(self) -> 'type.Class':
        """public java.lang.Class<? extends T> dev.ultreon.quantum.component.GameComponent.getHolder()"""
        return 'type.Class'._wrap(super(component.GameComponent, self).getHolder())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setRaw(self, arg0: str):
        """public void dev.ultreon.quantum.client.gui.widget.components.TextComponent.setRaw(java.lang.String)"""
        super(_TextComponent, self).setRaw(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.components.ColorComponent
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.gui.widget.components.ColorComponent as _ColorComponent
_ColorComponent = _ColorComponent
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Float as _float
import java.lang.String as _string
import dev.ultreon.quantum.util.Color as _Color
_Color = _Color
import java.lang.Integer as _int
import dev.ultreon.quantum.component.GameComponent as _GameComponent
_GameComponent = _GameComponent
from builtins import bool
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class ColorComponent():
    """dev.ultreon.quantum.client.gui.widget.components.ColorComponent"""
 
    @staticmethod
    def _wrap(java_value: _ColorComponent) -> 'ColorComponent':
        return ColorComponent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ColorComponent):
        """
        Dynamic initializer for ColorComponent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ColorComponent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ColorComponent__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def rgb(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.components.ColorComponent.rgb(int)"""
        super(_ColorComponent, self).rgb(_int.valueOf(arg0))

    @overload
    def hex(self, arg0: str):
        """public void dev.ultreon.quantum.client.gui.widget.components.ColorComponent.hex(java.lang.String)"""
        super(_ColorComponent, self).hex(arg0)

    @overload
    def set(self, arg0: 'Color'):
        """public void dev.ultreon.quantum.client.gui.widget.components.ColorComponent.set(dev.ultreon.quantum.util.Color)"""
        super(_ColorComponent, self).set(arg0)

    @overload
    def rgb(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.client.gui.widget.components.ColorComponent.rgb(float,float,float)"""
        super(_ColorComponent, self).rgb(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def rgba(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void dev.ultreon.quantum.client.gui.widget.components.ColorComponent.rgba(int,int,int,int)"""
        super(_ColorComponent, self).rgba(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def handleImGui(self, arg0: str, arg1: 'Identifier', arg2: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.components.ColorComponent.handleImGui(java.lang.String,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_ColorComponent, self).handleImGui(arg0, arg1, arg2)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def get(self) -> 'util.Color':
        """public dev.ultreon.quantum.util.Color dev.ultreon.quantum.client.gui.widget.components.ColorComponent.get()"""
        return 'util.Color'._wrap(super(ColorComponent, self).get())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'RgbColor'):
        """public dev.ultreon.quantum.client.gui.widget.components.ColorComponent(dev.ultreon.quantum.util.RgbColor)"""
        val = _ColorComponent(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def rgb(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.client.gui.widget.components.ColorComponent.rgb(int,int,int)"""
        super(_ColorComponent, self).rgb(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def rgba(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.components.ColorComponent.rgba(float,float,float,float)"""
        super(_ColorComponent, self).rgba(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def argb(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.components.ColorComponent.argb(int)"""
        super(_ColorComponent, self).argb(_int.valueOf(arg0))

    @override
    @overload
    def getHolder(self) -> 'type.Class':
        """public java.lang.Class<? extends T> dev.ultreon.quantum.component.GameComponent.getHolder()"""
        return 'type.Class'._wrap(super(component.GameComponent, self).getHolder())

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
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.components.UIComponent
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.component.GameComponent as _GameComponent
_GameComponent = _GameComponent
import dev.ultreon.quantum.client.gui.widget.components.UIComponent as _UIComponent
_UIComponent = _UIComponent
from builtins import bool
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class UIComponent():
    """dev.ultreon.quantum.client.gui.widget.components.UIComponent"""
 
    @staticmethod
    def _wrap(java_value: _UIComponent) -> 'UIComponent':
        return UIComponent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UIComponent):
        """
        Dynamic initializer for UIComponent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UIComponent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UIComponent__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.widget.components.UIComponent()"""
        val = _UIComponent()
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
        """public dev.ultreon.quantum.client.gui.widget.components.UIComponent()"""
        val = _UIComponent()
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

    @overload
    def handleImGui(self, arg0: str, arg1: 'Identifier', arg2: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.components.UIComponent.handleImGui(java.lang.String,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_UIComponent, self).handleImGui(arg0, arg1, arg2)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getHolder(self) -> 'type.Class':
        """public java.lang.Class<? extends T> dev.ultreon.quantum.component.GameComponent.getHolder()"""
        return 'type.Class'._wrap(super(component.GameComponent, self).getHolder())

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
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.components.AlignmentComponent
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.gui.Alignment as _Alignment
_Alignment = _Alignment
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.component.GameComponent as _GameComponent
_GameComponent = _GameComponent
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.widget.components.AlignmentComponent as _AlignmentComponent
_AlignmentComponent = _AlignmentComponent
from builtins import bool
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class AlignmentComponent():
    """dev.ultreon.quantum.client.gui.widget.components.AlignmentComponent"""
 
    @staticmethod
    def _wrap(java_value: _AlignmentComponent) -> 'AlignmentComponent':
        return AlignmentComponent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AlignmentComponent):
        """
        Dynamic initializer for AlignmentComponent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AlignmentComponent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AlignmentComponent__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Alignment'):
        """public dev.ultreon.quantum.client.gui.widget.components.AlignmentComponent(dev.ultreon.quantum.client.gui.Alignment)"""
        val = _AlignmentComponent(arg0)
        self.__wrapper = val

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
    def set(self, arg0: 'Alignment'):
        """public void dev.ultreon.quantum.client.gui.widget.components.AlignmentComponent.set(dev.ultreon.quantum.client.gui.Alignment)"""
        super(_AlignmentComponent, self).set(arg0)

    @override
    @overload
    def handleImGui(self, arg0: str, arg1: 'Identifier', arg2: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.components.AlignmentComponent.handleImGui(java.lang.String,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_AlignmentComponent, self).handleImGui(arg0, arg1, arg2)

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
    def getHolder(self) -> 'type.Class':
        """public java.lang.Class<? extends T> dev.ultreon.quantum.component.GameComponent.getHolder()"""
        return 'type.Class'._wrap(super(component.GameComponent, self).getHolder())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def get(self) -> 'gui.Alignment':
        """public dev.ultreon.quantum.client.gui.Alignment dev.ultreon.quantum.client.gui.widget.components.AlignmentComponent.get()"""
        return 'gui.Alignment'._wrap(super(AlignmentComponent, self).get())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.components.CallbackComponent
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.gui.widget.components.CallbackComponent as _CallbackComponent
_CallbackComponent = _CallbackComponent
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.component.GameComponent as _GameComponent
_GameComponent = _GameComponent
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

from builtins import bool
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class CallbackComponent():
    """dev.ultreon.quantum.client.gui.widget.components.CallbackComponent"""
 
    @staticmethod
    def _wrap(java_value: _CallbackComponent) -> 'CallbackComponent':
        return CallbackComponent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CallbackComponent):
        """
        Dynamic initializer for CallbackComponent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CallbackComponent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CallbackComponent__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'Callback'):
        """public dev.ultreon.quantum.client.gui.widget.components.CallbackComponent(dev.ultreon.quantum.client.gui.Callback<T>)"""
        val = _CallbackComponent(arg0)
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

    @overload
    def call0(self, arg0: object):
        """public void dev.ultreon.quantum.client.gui.widget.components.CallbackComponent.call0(java.lang.Object)"""
        super(_CallbackComponent, self).call0(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def handleImGui(self, arg0: str, arg1: 'Identifier', arg2: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.components.CallbackComponent.handleImGui(java.lang.String,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_CallbackComponent, self).handleImGui(arg0, arg1, arg2)

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
    def getHolder(self) -> 'type.Class':
        """public java.lang.Class<? extends T> dev.ultreon.quantum.component.GameComponent.getHolder()"""
        return 'type.Class'._wrap(super(component.GameComponent, self).getHolder())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def call(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.components.CallbackComponent.call(T)"""
        super(_CallbackComponent, self).call(arg0)

    @overload
    def set(self, arg0: 'Callback'):
        """public void dev.ultreon.quantum.client.gui.widget.components.CallbackComponent.set(dev.ultreon.quantum.client.gui.Callback<T>)"""
        super(_CallbackComponent, self).set(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.components.ScaleComponent
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = _import_once("pyquantum.client.gui.widget")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.gui.widget.components.ScaleComponent as _ScaleComponent
_ScaleComponent = _ScaleComponent
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.component.GameComponent as _GameComponent
_GameComponent = _GameComponent
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ScaleComponent():
    """dev.ultreon.quantum.client.gui.widget.components.ScaleComponent"""
 
    @staticmethod
    def _wrap(java_value: _ScaleComponent) -> 'ScaleComponent':
        return ScaleComponent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ScaleComponent):
        """
        Dynamic initializer for ScaleComponent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ScaleComponent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ScaleComponent__wrapper":
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
    def handleImGui(self, arg0: str, arg1: 'Identifier', arg2: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.components.ScaleComponent.handleImGui(java.lang.String,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(_ScaleComponent, self).handleImGui(arg0, arg1, arg2)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def get(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.components.ScaleComponent.get()"""
        return int._wrap(super(ScaleComponent, self).get())

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
    def set(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.components.ScaleComponent.set(int)"""
        super(_ScaleComponent, self).set(_int.valueOf(arg0))

    @override
    @overload
    def getHolder(self) -> 'type.Class':
        """public java.lang.Class<? extends T> dev.ultreon.quantum.component.GameComponent.getHolder()"""
        return 'type.Class'._wrap(super(component.GameComponent, self).getHolder())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.client.gui.widget.components.ScaleComponent(int)"""
        val = _ScaleComponent(_int.valueOf(arg0))
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