from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import dev.ultreon.quantum.client.font.Font as __Font
__Font = __Font
import java.lang.Object as __object
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import dev.ultreon.quantum.text.FormattedText as __FormattedText
__FormattedText = __FormattedText
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
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
import java.util.List as List
from builtins import int
 
class Font(pygdx.__Disposable, utils.Disposable):
    """dev.ultreon.quantum.client.font.Font"""
 
    @staticmethod
    def __wrap(java_value: __Font) -> 'Font':
        return Font(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Font):
        """
        Dynamic initializer for Font.
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
    def dispose(self):
        """public void dev.ultreon.quantum.client.font.Font.dispose()"""
        super(Font, self).dispose()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def drawText(self, arg0: 'Renderer', arg1: 'TextObject', arg2: float, arg3: float, arg4: 'Color', arg5: bool):
        """public void dev.ultreon.quantum.client.font.Font.drawText(dev.ultreon.quantum.client.gui.Renderer,dev.ultreon.quantum.text.TextObject,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        super(__Font, self).drawText(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3), arg4, __boolean.valueOf(arg5))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def drawText(self, arg0: 'Renderer', arg1: str, arg2: float, arg3: float, arg4: 'Color', arg5: bool):
        """public void dev.ultreon.quantum.client.font.Font.drawText(dev.ultreon.quantum.client.gui.Renderer,java.lang.String,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        super(__Font, self).drawText(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3), arg4, __boolean.valueOf(arg5))

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void dev.ultreon.quantum.client.font.Font.setColor(float,float,float,float)"""
        super(__Font, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def width(self, arg0: str) -> int:
        """public int dev.ultreon.quantum.client.font.Font.width(java.lang.String)"""
        return int.__wrap(super(__Font, self).width(arg0))

    @overload
    def width(self, arg0: 'List') -> int:
        """public int dev.ultreon.quantum.client.font.Font.width(java.util.List<dev.ultreon.quantum.text.FormattedText>)"""
        return int.__wrap(super(__Font, self).width(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def wordWrap(self, arg0: 'TextObject', arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.text.FormattedText> dev.ultreon.quantum.client.font.Font.wordWrap(dev.ultreon.quantum.text.TextObject,int)"""
        return 'List'.__wrap(super(__Font, self).wordWrap(arg0, __int.valueOf(arg1)))

    @overload
    def width(self, arg0: 'FormattedText') -> int:
        """public int dev.ultreon.quantum.client.font.Font.width(dev.ultreon.quantum.text.FormattedText)"""
        return int.__wrap(super(__Font, self).width(arg0))

    @overload
    def __init__(self, arg0: 'BitmapFont', arg1: bool):
        """public dev.ultreon.quantum.client.font.Font(com.badlogic.gdx.graphics.g2d.BitmapFont,boolean)"""
        val = __Font(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setColor(self, arg0: 'Color'):
        """public void dev.ultreon.quantum.client.font.Font.setColor(dev.ultreon.quantum.util.Color)"""
        super(__Font, self).setColor(arg0)

    @overload
    def getFormattedText(self, arg0: 'TextObject') -> 'text.FormattedText':
        """public dev.ultreon.quantum.text.FormattedText dev.ultreon.quantum.client.font.Font.getFormattedText(dev.ultreon.quantum.text.TextObject)"""
        return 'text.FormattedText'.__wrap(super(__Font, self).getFormattedText(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def isSpecial(self) -> bool:
        """public boolean dev.ultreon.quantum.client.font.Font.isSpecial()"""
        return bool.__wrap(super(Font, self).isSpecial())

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
    def drawText(self, arg0: 'Renderer', arg1: 'FormattedText', arg2: float, arg3: float, arg4: 'Color', arg5: bool):
        """public void dev.ultreon.quantum.client.font.Font.drawText(dev.ultreon.quantum.client.gui.Renderer,dev.ultreon.quantum.text.FormattedText,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        super(__Font, self).drawText(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3), arg4, __boolean.valueOf(arg5))

    @overload
    def drawText(self, arg0: 'Renderer', arg1: 'List', arg2: float, arg3: float, arg4: 'Color', arg5: bool):
        """public void dev.ultreon.quantum.client.font.Font.drawText(dev.ultreon.quantum.client.gui.Renderer,java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        super(__Font, self).drawText(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3), arg4, __boolean.valueOf(arg5))

    @overload
    def width(self, arg0: 'TextObject') -> int:
        """public int dev.ultreon.quantum.client.font.Font.width(dev.ultreon.quantum.text.TextObject)"""
        return int.__wrap(super(__Font, self).width(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'BitmapFont'):
        """public dev.ultreon.quantum.client.font.Font(com.badlogic.gdx.graphics.g2d.BitmapFont)"""
        val = __Font(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.quantum.client.font.Font
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import dev.ultreon.quantum.client.font.Font as __Font
__Font = __Font
import java.lang.Object as __object
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import dev.ultreon.quantum.text.FormattedText as __FormattedText
__FormattedText = __FormattedText
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
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
import java.util.List as List
from builtins import int
 
class Font(pygdx.__Disposable, utils.Disposable):
    """dev.ultreon.quantum.client.font.Font"""
 
    @staticmethod
    def __wrap(java_value: __Font) -> 'Font':
        return Font(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Font):
        """
        Dynamic initializer for Font.
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
    def dispose(self):
        """public void dev.ultreon.quantum.client.font.Font.dispose()"""
        super(Font, self).dispose()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def drawText(self, arg0: 'Renderer', arg1: 'TextObject', arg2: float, arg3: float, arg4: 'Color', arg5: bool):
        """public void dev.ultreon.quantum.client.font.Font.drawText(dev.ultreon.quantum.client.gui.Renderer,dev.ultreon.quantum.text.TextObject,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        super(__Font, self).drawText(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3), arg4, __boolean.valueOf(arg5))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def drawText(self, arg0: 'Renderer', arg1: str, arg2: float, arg3: float, arg4: 'Color', arg5: bool):
        """public void dev.ultreon.quantum.client.font.Font.drawText(dev.ultreon.quantum.client.gui.Renderer,java.lang.String,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        super(__Font, self).drawText(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3), arg4, __boolean.valueOf(arg5))

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void dev.ultreon.quantum.client.font.Font.setColor(float,float,float,float)"""
        super(__Font, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def width(self, arg0: str) -> int:
        """public int dev.ultreon.quantum.client.font.Font.width(java.lang.String)"""
        return int.__wrap(super(__Font, self).width(arg0))

    @overload
    def width(self, arg0: 'List') -> int:
        """public int dev.ultreon.quantum.client.font.Font.width(java.util.List<dev.ultreon.quantum.text.FormattedText>)"""
        return int.__wrap(super(__Font, self).width(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def wordWrap(self, arg0: 'TextObject', arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.text.FormattedText> dev.ultreon.quantum.client.font.Font.wordWrap(dev.ultreon.quantum.text.TextObject,int)"""
        return 'List'.__wrap(super(__Font, self).wordWrap(arg0, __int.valueOf(arg1)))

    @overload
    def width(self, arg0: 'FormattedText') -> int:
        """public int dev.ultreon.quantum.client.font.Font.width(dev.ultreon.quantum.text.FormattedText)"""
        return int.__wrap(super(__Font, self).width(arg0))

    @overload
    def __init__(self, arg0: 'BitmapFont', arg1: bool):
        """public dev.ultreon.quantum.client.font.Font(com.badlogic.gdx.graphics.g2d.BitmapFont,boolean)"""
        val = __Font(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setColor(self, arg0: 'Color'):
        """public void dev.ultreon.quantum.client.font.Font.setColor(dev.ultreon.quantum.util.Color)"""
        super(__Font, self).setColor(arg0)

    @overload
    def getFormattedText(self, arg0: 'TextObject') -> 'text.FormattedText':
        """public dev.ultreon.quantum.text.FormattedText dev.ultreon.quantum.client.font.Font.getFormattedText(dev.ultreon.quantum.text.TextObject)"""
        return 'text.FormattedText'.__wrap(super(__Font, self).getFormattedText(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def isSpecial(self) -> bool:
        """public boolean dev.ultreon.quantum.client.font.Font.isSpecial()"""
        return bool.__wrap(super(Font, self).isSpecial())

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
    def drawText(self, arg0: 'Renderer', arg1: 'FormattedText', arg2: float, arg3: float, arg4: 'Color', arg5: bool):
        """public void dev.ultreon.quantum.client.font.Font.drawText(dev.ultreon.quantum.client.gui.Renderer,dev.ultreon.quantum.text.FormattedText,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        super(__Font, self).drawText(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3), arg4, __boolean.valueOf(arg5))

    @overload
    def drawText(self, arg0: 'Renderer', arg1: 'List', arg2: float, arg3: float, arg4: 'Color', arg5: bool):
        """public void dev.ultreon.quantum.client.font.Font.drawText(dev.ultreon.quantum.client.gui.Renderer,java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        super(__Font, self).drawText(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3), arg4, __boolean.valueOf(arg5))

    @overload
    def width(self, arg0: 'TextObject') -> int:
        """public int dev.ultreon.quantum.client.font.Font.width(dev.ultreon.quantum.text.TextObject)"""
        return int.__wrap(super(__Font, self).width(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'BitmapFont'):
        """public dev.ultreon.quantum.client.font.Font(com.badlogic.gdx.graphics.g2d.BitmapFont)"""
        val = __Font(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.quantum.client.font.Font 
 
 
# CLASS: dev.ultreon.quantum.client.font.TextObjectRenderer
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.client.font.TextObjectRenderer as __TextObjectRenderer
__TextObjectRenderer = __TextObjectRenderer
try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TextObjectRenderer():
    """dev.ultreon.quantum.client.font.TextObjectRenderer"""
 
    @staticmethod
    def __wrap(java_value: __TextObjectRenderer) -> 'TextObjectRenderer':
        return TextObjectRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextObjectRenderer):
        """
        Dynamic initializer for TextObjectRenderer.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getText(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.font.TextObjectRenderer.getText()"""
        return str.__wrap(super(TextObjectRenderer, self).getText())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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

    @overload
    def __init__(self, arg0: 'Font', arg1: 'TextObject'):
        """public dev.ultreon.quantum.client.font.TextObjectRenderer(dev.ultreon.quantum.client.font.Font,dev.ultreon.quantum.text.TextObject)"""
        val = __TextObjectRenderer(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def render(self, arg0: 'Renderer', arg1: 'Color', arg2: float, arg3: float, arg4: bool):
        """public void dev.ultreon.quantum.client.font.TextObjectRenderer.render(dev.ultreon.quantum.client.gui.Renderer,dev.ultreon.quantum.util.Color,float,float,boolean)"""
        super(__TextObjectRenderer, self).render(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3), __boolean.valueOf(arg4))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.font.WordWrapper
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.client.font.WordWrapper as __WordWrapper
__WordWrapper = __WordWrapper
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class WordWrapper():
    """dev.ultreon.quantum.client.font.WordWrapper"""
 
    @staticmethod
    def __wrap(java_value: __WordWrapper) -> 'WordWrapper':
        return WordWrapper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WordWrapper):
        """
        Dynamic initializer for WordWrapper.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def wrap(self, arg0: 'FormattedText', arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.text.FormattedText> dev.ultreon.quantum.client.font.WordWrapper.wrap(dev.ultreon.quantum.text.FormattedText,int)"""
        return 'List'.__wrap(super(__WordWrapper, self).wrap(arg0, __int.valueOf(arg1)))

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

    @overload
    def __init__(self, arg0: 'BitmapFont', arg1: 'Font'):
        """public dev.ultreon.quantum.client.font.WordWrapper(com.badlogic.gdx.graphics.g2d.BitmapFont,dev.ultreon.quantum.client.font.Font)"""
        val = __WordWrapper(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))