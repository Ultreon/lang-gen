from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent as __RangedValueComponent
__RangedValueComponent = __RangedValueComponent
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = __import_once__("pyquantum.client.gui.widget")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RangedValueComponent(__UIComponent, UIComponent):
    """dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent"""
 
    @staticmethod
    def __wrap(java_value: __RangedValueComponent) -> 'RangedValueComponent':
        return RangedValueComponent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RangedValueComponent):
        """
        Dynamic initializer for RangedValueComponent.
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
    def getHolder(self) -> 'type.Class':
        """public java.lang.Class<? extends T> dev.ultreon.quantum.component.GameComponent.getHolder()"""
        return 'type.Class'.__wrap(super(component.GameComponent, self).getHolder())

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
    def handleImGui(self, arg0: str, arg1: 'Identifier', arg2: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent.handleImGui(java.lang.String,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__RangedValueComponent, self).handleImGui(arg0, arg1, arg2)

    @overload
    def get(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent.get()"""
        return int.__wrap(super(RangedValueComponent, self).get())

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
    def __init__(self, arg0: int, arg1: int, arg2: int):
        """public dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent(int,int,int)"""
        val = __RangedValueComponent(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent.set(int)"""
        super(__RangedValueComponent, self).set(__int.valueOf(arg0))

    @overload
    def min(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent.min()"""
        return int.__wrap(super(RangedValueComponent, self).min())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def max(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent.max()"""
        return int.__wrap(super(RangedValueComponent, self).max())

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent as __RangedValueComponent
__RangedValueComponent = __RangedValueComponent
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = __import_once__("pyquantum.client.gui.widget")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RangedValueComponent(__UIComponent, UIComponent):
    """dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent"""
 
    @staticmethod
    def __wrap(java_value: __RangedValueComponent) -> 'RangedValueComponent':
        return RangedValueComponent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RangedValueComponent):
        """
        Dynamic initializer for RangedValueComponent.
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
    def getHolder(self) -> 'type.Class':
        """public java.lang.Class<? extends T> dev.ultreon.quantum.component.GameComponent.getHolder()"""
        return 'type.Class'.__wrap(super(component.GameComponent, self).getHolder())

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
    def handleImGui(self, arg0: str, arg1: 'Identifier', arg2: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent.handleImGui(java.lang.String,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__RangedValueComponent, self).handleImGui(arg0, arg1, arg2)

    @overload
    def get(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent.get()"""
        return int.__wrap(super(RangedValueComponent, self).get())

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
    def __init__(self, arg0: int, arg1: int, arg2: int):
        """public dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent(int,int,int)"""
        val = __RangedValueComponent(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent.set(int)"""
        super(__RangedValueComponent, self).set(__int.valueOf(arg0))

    @overload
    def min(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent.min()"""
        return int.__wrap(super(RangedValueComponent, self).min())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def max(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent.max()"""
        return int.__wrap(super(RangedValueComponent, self).max())

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.components.RangedValueComponent 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.components.TextComponent
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = __import_once__("pyquantum.client.gui.widget")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

from builtins import object
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.widget.components.TextComponent as __TextComponent
__TextComponent = __TextComponent
from builtins import bool
from builtins import int
 
class TextComponent(__UIComponent, UIComponent):
    """dev.ultreon.quantum.client.gui.widget.components.TextComponent"""
 
    @staticmethod
    def __wrap(java_value: __TextComponent) -> 'TextComponent':
        return TextComponent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextComponent):
        """
        Dynamic initializer for TextComponent.
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
    def get(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.widget.components.TextComponent.get()"""
        return 'text.TextObject'.__wrap(super(TextComponent, self).get())

    @overload
    def set(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.client.gui.widget.components.TextComponent.set(dev.ultreon.quantum.text.TextObject)"""
        super(__TextComponent, self).set(arg0)

    @overload
    def __init__(self, arg0: 'TextObject'):
        """public dev.ultreon.quantum.client.gui.widget.components.TextComponent(dev.ultreon.quantum.text.TextObject)"""
        val = __TextComponent(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getHolder(self) -> 'type.Class':
        """public java.lang.Class<? extends T> dev.ultreon.quantum.component.GameComponent.getHolder()"""
        return 'type.Class'.__wrap(super(component.GameComponent, self).getHolder())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.widget.components.TextComponent()"""
        val = __TextComponent()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def translate(self, arg0: str, *arg1: object):
        """public void dev.ultreon.quantum.client.gui.widget.components.TextComponent.translate(java.lang.String,java.lang.Object...)"""
        super(__TextComponent, self).translate(arg0, arg1)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.widget.components.TextComponent()"""
        val = __TextComponent()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setRaw(self, arg0: str):
        """public void dev.ultreon.quantum.client.gui.widget.components.TextComponent.setRaw(java.lang.String)"""
        super(__TextComponent, self).setRaw(arg0)

    @overload
    def getRaw(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.widget.components.TextComponent.getRaw()"""
        return str.__wrap(super(TextComponent, self).getRaw())

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

    @override
    @overload
    def handleImGui(self, arg0: str, arg1: 'Identifier', arg2: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.components.TextComponent.handleImGui(java.lang.String,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__TextComponent, self).handleImGui(arg0, arg1, arg2)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.components.ColorComponent
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = __import_once__("pyquantum.client.gui.widget")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import dev.ultreon.quantum.util.Color as __Color
__Color = __Color
import java.lang.Long as __long
import dev.ultreon.quantum.client.gui.widget.components.ColorComponent as __ColorComponent
__ColorComponent = __ColorComponent
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ColorComponent(__UIComponent, UIComponent):
    """dev.ultreon.quantum.client.gui.widget.components.ColorComponent"""
 
    @staticmethod
    def __wrap(java_value: __ColorComponent) -> 'ColorComponent':
        return ColorComponent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ColorComponent):
        """
        Dynamic initializer for ColorComponent.
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
    def rgb(self, arg0: int, arg1: int, arg2: int):
        """public void dev.ultreon.quantum.client.gui.widget.components.ColorComponent.rgb(int,int,int)"""
        super(__ColorComponent, self).rgb(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def rgb(self, arg0: float, arg1: float, arg2: float):
        """public void dev.ultreon.quantum.client.gui.widget.components.ColorComponent.rgb(float,float,float)"""
        super(__ColorComponent, self).rgb(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def rgb(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.components.ColorComponent.rgb(int)"""
        super(__ColorComponent, self).rgb(__int.valueOf(arg0))

    @override
    @overload
    def getHolder(self) -> 'type.Class':
        """public java.lang.Class<? extends T> dev.ultreon.quantum.component.GameComponent.getHolder()"""
        return 'type.Class'.__wrap(super(component.GameComponent, self).getHolder())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def get(self) -> 'util.Color':
        """public dev.ultreon.quantum.util.Color dev.ultreon.quantum.client.gui.widget.components.ColorComponent.get()"""
        return 'util.Color'.__wrap(super(ColorComponent, self).get())

    @overload
    def set(self, arg0: 'Color'):
        """public void dev.ultreon.quantum.client.gui.widget.components.ColorComponent.set(dev.ultreon.quantum.util.Color)"""
        super(__ColorComponent, self).set(arg0)

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
    def __init__(self, arg0: 'RgbColor'):
        """public dev.ultreon.quantum.client.gui.widget.components.ColorComponent(dev.ultreon.quantum.util.RgbColor)"""
        val = __ColorComponent(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def rgba(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void dev.ultreon.quantum.client.gui.widget.components.ColorComponent.rgba(int,int,int,int)"""
        super(__ColorComponent, self).rgba(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

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
    def hex(self, arg0: str):
        """public void dev.ultreon.quantum.client.gui.widget.components.ColorComponent.hex(java.lang.String)"""
        super(__ColorComponent, self).hex(arg0)

    @overload
    def argb(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.components.ColorComponent.argb(int)"""
        super(__ColorComponent, self).argb(__int.valueOf(arg0))

    @override
    @overload
    def handleImGui(self, arg0: str, arg1: 'Identifier', arg2: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.components.ColorComponent.handleImGui(java.lang.String,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__ColorComponent, self).handleImGui(arg0, arg1, arg2)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def rgba(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void dev.ultreon.quantum.client.gui.widget.components.ColorComponent.rgba(float,float,float,float)"""
        super(__ColorComponent, self).rgba(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.components.UIComponent
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = __import_once__("pyquantum.client.gui.widget")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.client.gui.widget.components.UIComponent as __UIComponent
__UIComponent = __UIComponent
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class UIComponent(pyquantum.__GameComponent, component.GameComponent):
    """dev.ultreon.quantum.client.gui.widget.components.UIComponent"""
 
    @staticmethod
    def __wrap(java_value: __UIComponent) -> 'UIComponent':
        return UIComponent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UIComponent):
        """
        Dynamic initializer for UIComponent.
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
    def getHolder(self) -> 'type.Class':
        """public java.lang.Class<? extends T> dev.ultreon.quantum.component.GameComponent.getHolder()"""
        return 'type.Class'.__wrap(super(component.GameComponent, self).getHolder())

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
    def handleImGui(self, arg0: str, arg1: 'Identifier', arg2: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.components.UIComponent.handleImGui(java.lang.String,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__UIComponent, self).handleImGui(arg0, arg1, arg2)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.gui.widget.components.UIComponent()"""
        val = __UIComponent()
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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.gui.widget.components.UIComponent()"""
        val = __UIComponent()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.components.AlignmentComponent
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = __import_once__("pyquantum.client.gui.widget")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __string
import java.lang.String as __String
__String = __String
try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.widget.components.AlignmentComponent as __AlignmentComponent
__AlignmentComponent = __AlignmentComponent
from builtins import bool
import dev.ultreon.quantum.client.gui.Alignment as __Alignment
__Alignment = __Alignment
from builtins import int
 
class AlignmentComponent(__UIComponent, UIComponent):
    """dev.ultreon.quantum.client.gui.widget.components.AlignmentComponent"""
 
    @staticmethod
    def __wrap(java_value: __AlignmentComponent) -> 'AlignmentComponent':
        return AlignmentComponent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AlignmentComponent):
        """
        Dynamic initializer for AlignmentComponent.
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
    def get(self) -> 'gui.Alignment':
        """public dev.ultreon.quantum.client.gui.Alignment dev.ultreon.quantum.client.gui.widget.components.AlignmentComponent.get()"""
        return 'gui.Alignment'.__wrap(super(AlignmentComponent, self).get())

    @override
    @overload
    def getHolder(self) -> 'type.Class':
        """public java.lang.Class<? extends T> dev.ultreon.quantum.component.GameComponent.getHolder()"""
        return 'type.Class'.__wrap(super(component.GameComponent, self).getHolder())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: 'Alignment'):
        """public void dev.ultreon.quantum.client.gui.widget.components.AlignmentComponent.set(dev.ultreon.quantum.client.gui.Alignment)"""
        super(__AlignmentComponent, self).set(arg0)

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
    def handleImGui(self, arg0: str, arg1: 'Identifier', arg2: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.components.AlignmentComponent.handleImGui(java.lang.String,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__AlignmentComponent, self).handleImGui(arg0, arg1, arg2)

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
    def __init__(self, arg0: 'Alignment'):
        """public dev.ultreon.quantum.client.gui.widget.components.AlignmentComponent(dev.ultreon.quantum.client.gui.Alignment)"""
        val = __AlignmentComponent(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.components.CallbackComponent
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = __import_once__("pyquantum.client.gui.widget")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.client.gui.widget.components.CallbackComponent as __CallbackComponent
__CallbackComponent = __CallbackComponent
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __string
import java.lang.String as __String
__String = __String
try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CallbackComponent(__UIComponent, UIComponent):
    """dev.ultreon.quantum.client.gui.widget.components.CallbackComponent"""
 
    @staticmethod
    def __wrap(java_value: __CallbackComponent) -> 'CallbackComponent':
        return CallbackComponent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CallbackComponent):
        """
        Dynamic initializer for CallbackComponent.
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
    def call(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.components.CallbackComponent.call(T)"""
        super(__CallbackComponent, self).call(arg0)

    @override
    @overload
    def handleImGui(self, arg0: str, arg1: 'Identifier', arg2: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.components.CallbackComponent.handleImGui(java.lang.String,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__CallbackComponent, self).handleImGui(arg0, arg1, arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def set(self, arg0: 'Callback'):
        """public void dev.ultreon.quantum.client.gui.widget.components.CallbackComponent.set(dev.ultreon.quantum.client.gui.Callback<T>)"""
        super(__CallbackComponent, self).set(arg0)

    @override
    @overload
    def getHolder(self) -> 'type.Class':
        """public java.lang.Class<? extends T> dev.ultreon.quantum.component.GameComponent.getHolder()"""
        return 'type.Class'.__wrap(super(component.GameComponent, self).getHolder())

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
    def call0(self, arg0: object):
        """public void dev.ultreon.quantum.client.gui.widget.components.CallbackComponent.call0(java.lang.Object)"""
        super(__CallbackComponent, self).call0(arg0)

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
    def __init__(self, arg0: 'Callback'):
        """public dev.ultreon.quantum.client.gui.widget.components.CallbackComponent(dev.ultreon.quantum.client.gui.Callback<T>)"""
        val = __CallbackComponent(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.gui.widget.components.ScaleComponent
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = __import_once__("pyquantum.client.gui.widget")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import dev.ultreon.quantum.client.gui.widget.components.ScaleComponent as __ScaleComponent
__ScaleComponent = __ScaleComponent
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ScaleComponent(__UIComponent, UIComponent):
    """dev.ultreon.quantum.client.gui.widget.components.ScaleComponent"""
 
    @staticmethod
    def __wrap(java_value: __ScaleComponent) -> 'ScaleComponent':
        return ScaleComponent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ScaleComponent):
        """
        Dynamic initializer for ScaleComponent.
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
    def handleImGui(self, arg0: str, arg1: 'Identifier', arg2: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.components.ScaleComponent.handleImGui(java.lang.String,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__ScaleComponent, self).handleImGui(arg0, arg1, arg2)

    @overload
    def get(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.components.ScaleComponent.get()"""
        return int.__wrap(super(ScaleComponent, self).get())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getHolder(self) -> 'type.Class':
        """public java.lang.Class<? extends T> dev.ultreon.quantum.component.GameComponent.getHolder()"""
        return 'type.Class'.__wrap(super(component.GameComponent, self).getHolder())

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
    def set(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.components.ScaleComponent.set(int)"""
        super(__ScaleComponent, self).set(__int.valueOf(arg0))

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
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.client.gui.widget.components.ScaleComponent(int)"""
        val = __ScaleComponent(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))