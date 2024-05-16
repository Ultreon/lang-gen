from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.Float as _float
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.client.font.Font as _Font
_Font = _Font
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

import dev.ultreon.quantum.text.FormattedText as _FormattedText
_FormattedText = _FormattedText
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Font():
    """dev.ultreon.quantum.client.font.Font"""
 
    @staticmethod
    def _wrap(java_value: _Font) -> 'Font':
        return Font(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Font):
        """
        Dynamic initializer for Font.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Font__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Font__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setColor(self, arg0: 'Color'):
        """public void dev.ultreon.quantum.client.font.Font.setColor(dev.ultreon.quantum.util.Color)"""
        super(_Font, self).setColor(arg0)

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.font.Font.dispose()"""
        super(Font, self).dispose()

    @overload
    def width(self, arg0: str) -> int:
        """public int dev.ultreon.quantum.client.font.Font.width(java.lang.String)"""
        return int._wrap(super(_Font, self).width(arg0))

    @overload
    def drawText(self, arg0: 'Renderer', arg1: 'FormattedText', arg2: float, arg3: float, arg4: 'Color', arg5: bool):
        """public void dev.ultreon.quantum.client.font.Font.drawText(dev.ultreon.quantum.client.gui.Renderer,dev.ultreon.quantum.text.FormattedText,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        super(_Font, self).drawText(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3), arg4, _boolean.valueOf(arg5))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'BitmapFont', arg1: bool):
        """public dev.ultreon.quantum.client.font.Font(com.badlogic.gdx.graphics.g2d.BitmapFont,boolean)"""
        val = _Font(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

    @overload
    def drawText(self, arg0: 'Renderer', arg1: str, arg2: float, arg3: float, arg4: 'Color', arg5: bool):
        """public void dev.ultreon.quantum.client.font.Font.drawText(dev.ultreon.quantum.client.gui.Renderer,java.lang.String,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        super(_Font, self).drawText(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3), arg4, _boolean.valueOf(arg5))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def width(self, arg0: 'FormattedText') -> int:
        """public int dev.ultreon.quantum.client.font.Font.width(dev.ultreon.quantum.text.FormattedText)"""
        return int._wrap(super(_Font, self).width(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def drawText(self, arg0: 'Renderer', arg1: 'List', arg2: float, arg3: float, arg4: 'Color', arg5: bool):
        """public void dev.ultreon.quantum.client.font.Font.drawText(dev.ultreon.quantum.client.gui.Renderer,java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        super(_Font, self).drawText(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3), arg4, _boolean.valueOf(arg5))

    @overload
    def isSpecial(self) -> bool:
        """public boolean dev.ultreon.quantum.client.font.Font.isSpecial()"""
        return bool._wrap(super(Font, self).isSpecial())

    @overload
    def __init__(self, arg0: 'BitmapFont'):
        """public dev.ultreon.quantum.client.font.Font(com.badlogic.gdx.graphics.g2d.BitmapFont)"""
        val = _Font(arg0)
        self.__wrapper = val

    @overload
    def drawText(self, arg0: 'Renderer', arg1: 'TextObject', arg2: float, arg3: float, arg4: 'Color', arg5: bool):
        """public void dev.ultreon.quantum.client.font.Font.drawText(dev.ultreon.quantum.client.gui.Renderer,dev.ultreon.quantum.text.TextObject,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        super(_Font, self).drawText(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3), arg4, _boolean.valueOf(arg5))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def width(self, arg0: 'TextObject') -> int:
        """public int dev.ultreon.quantum.client.font.Font.width(dev.ultreon.quantum.text.TextObject)"""
        return int._wrap(super(_Font, self).width(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def wordWrap(self, arg0: 'TextObject', arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.text.FormattedText> dev.ultreon.quantum.client.font.Font.wordWrap(dev.ultreon.quantum.text.TextObject,int)"""
        return 'List'._wrap(super(_Font, self).wordWrap(arg0, _int.valueOf(arg1)))

    @overload
    def width(self, arg0: 'List') -> int:
        """public int dev.ultreon.quantum.client.font.Font.width(java.util.List<dev.ultreon.quantum.text.FormattedText>)"""
        return int._wrap(super(_Font, self).width(arg0))

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void dev.ultreon.quantum.client.font.Font.setColor(float,float,float,float)"""
        super(_Font, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

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
    def getFormattedText(self, arg0: 'TextObject') -> 'text.FormattedText':
        """public dev.ultreon.quantum.text.FormattedText dev.ultreon.quantum.client.font.Font.getFormattedText(dev.ultreon.quantum.text.TextObject)"""
        return 'text.FormattedText'._wrap(super(_Font, self).getFormattedText(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.font.Font
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.Float as _float
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.client.font.Font as _Font
_Font = _Font
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

import dev.ultreon.quantum.text.FormattedText as _FormattedText
_FormattedText = _FormattedText
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Font():
    """dev.ultreon.quantum.client.font.Font"""
 
    @staticmethod
    def _wrap(java_value: _Font) -> 'Font':
        return Font(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Font):
        """
        Dynamic initializer for Font.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Font__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Font__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setColor(self, arg0: 'Color'):
        """public void dev.ultreon.quantum.client.font.Font.setColor(dev.ultreon.quantum.util.Color)"""
        super(_Font, self).setColor(arg0)

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.font.Font.dispose()"""
        super(Font, self).dispose()

    @overload
    def width(self, arg0: str) -> int:
        """public int dev.ultreon.quantum.client.font.Font.width(java.lang.String)"""
        return int._wrap(super(_Font, self).width(arg0))

    @overload
    def drawText(self, arg0: 'Renderer', arg1: 'FormattedText', arg2: float, arg3: float, arg4: 'Color', arg5: bool):
        """public void dev.ultreon.quantum.client.font.Font.drawText(dev.ultreon.quantum.client.gui.Renderer,dev.ultreon.quantum.text.FormattedText,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        super(_Font, self).drawText(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3), arg4, _boolean.valueOf(arg5))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'BitmapFont', arg1: bool):
        """public dev.ultreon.quantum.client.font.Font(com.badlogic.gdx.graphics.g2d.BitmapFont,boolean)"""
        val = _Font(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

    @overload
    def drawText(self, arg0: 'Renderer', arg1: str, arg2: float, arg3: float, arg4: 'Color', arg5: bool):
        """public void dev.ultreon.quantum.client.font.Font.drawText(dev.ultreon.quantum.client.gui.Renderer,java.lang.String,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        super(_Font, self).drawText(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3), arg4, _boolean.valueOf(arg5))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def width(self, arg0: 'FormattedText') -> int:
        """public int dev.ultreon.quantum.client.font.Font.width(dev.ultreon.quantum.text.FormattedText)"""
        return int._wrap(super(_Font, self).width(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def drawText(self, arg0: 'Renderer', arg1: 'List', arg2: float, arg3: float, arg4: 'Color', arg5: bool):
        """public void dev.ultreon.quantum.client.font.Font.drawText(dev.ultreon.quantum.client.gui.Renderer,java.util.List<dev.ultreon.quantum.text.FormattedText>,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        super(_Font, self).drawText(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3), arg4, _boolean.valueOf(arg5))

    @overload
    def isSpecial(self) -> bool:
        """public boolean dev.ultreon.quantum.client.font.Font.isSpecial()"""
        return bool._wrap(super(Font, self).isSpecial())

    @overload
    def __init__(self, arg0: 'BitmapFont'):
        """public dev.ultreon.quantum.client.font.Font(com.badlogic.gdx.graphics.g2d.BitmapFont)"""
        val = _Font(arg0)
        self.__wrapper = val

    @overload
    def drawText(self, arg0: 'Renderer', arg1: 'TextObject', arg2: float, arg3: float, arg4: 'Color', arg5: bool):
        """public void dev.ultreon.quantum.client.font.Font.drawText(dev.ultreon.quantum.client.gui.Renderer,dev.ultreon.quantum.text.TextObject,float,float,dev.ultreon.quantum.util.Color,boolean)"""
        super(_Font, self).drawText(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3), arg4, _boolean.valueOf(arg5))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def width(self, arg0: 'TextObject') -> int:
        """public int dev.ultreon.quantum.client.font.Font.width(dev.ultreon.quantum.text.TextObject)"""
        return int._wrap(super(_Font, self).width(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def wordWrap(self, arg0: 'TextObject', arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.text.FormattedText> dev.ultreon.quantum.client.font.Font.wordWrap(dev.ultreon.quantum.text.TextObject,int)"""
        return 'List'._wrap(super(_Font, self).wordWrap(arg0, _int.valueOf(arg1)))

    @overload
    def width(self, arg0: 'List') -> int:
        """public int dev.ultreon.quantum.client.font.Font.width(java.util.List<dev.ultreon.quantum.text.FormattedText>)"""
        return int._wrap(super(_Font, self).width(arg0))

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void dev.ultreon.quantum.client.font.Font.setColor(float,float,float,float)"""
        super(_Font, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

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
    def getFormattedText(self, arg0: 'TextObject') -> 'text.FormattedText':
        """public dev.ultreon.quantum.text.FormattedText dev.ultreon.quantum.client.font.Font.getFormattedText(dev.ultreon.quantum.text.TextObject)"""
        return 'text.FormattedText'._wrap(super(_Font, self).getFormattedText(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.font.Font 
 
 
# CLASS: dev.ultreon.quantum.client.font.TextObjectRenderer
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.client.font.TextObjectRenderer as _TextObjectRenderer
_TextObjectRenderer = _TextObjectRenderer
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextObjectRenderer():
    """dev.ultreon.quantum.client.font.TextObjectRenderer"""
 
    @staticmethod
    def _wrap(java_value: _TextObjectRenderer) -> 'TextObjectRenderer':
        return TextObjectRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextObjectRenderer):
        """
        Dynamic initializer for TextObjectRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextObjectRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextObjectRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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

    @overload
    def __init__(self, arg0: 'Font', arg1: 'TextObject'):
        """public dev.ultreon.quantum.client.font.TextObjectRenderer(dev.ultreon.quantum.client.font.Font,dev.ultreon.quantum.text.TextObject)"""
        val = _TextObjectRenderer(arg0, arg1)
        self.__wrapper = val

    @overload
    def getText(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.font.TextObjectRenderer.getText()"""
        return str._wrap(super(TextObjectRenderer, self).getText())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def render(self, arg0: 'Renderer', arg1: 'Color', arg2: float, arg3: float, arg4: bool):
        """public void dev.ultreon.quantum.client.font.TextObjectRenderer.render(dev.ultreon.quantum.client.gui.Renderer,dev.ultreon.quantum.util.Color,float,float,boolean)"""
        super(_TextObjectRenderer, self).render(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3), _boolean.valueOf(arg4))

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
 
 
# CLASS: dev.ultreon.quantum.client.font.WordWrapper
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.font.WordWrapper as _WordWrapper
_WordWrapper = _WordWrapper
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WordWrapper():
    """dev.ultreon.quantum.client.font.WordWrapper"""
 
    @staticmethod
    def _wrap(java_value: _WordWrapper) -> 'WordWrapper':
        return WordWrapper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WordWrapper):
        """
        Dynamic initializer for WordWrapper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WordWrapper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WordWrapper__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'BitmapFont', arg1: 'Font'):
        """public dev.ultreon.quantum.client.font.WordWrapper(com.badlogic.gdx.graphics.g2d.BitmapFont,dev.ultreon.quantum.client.font.Font)"""
        val = _WordWrapper(arg0, arg1)
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def wrap(self, arg0: 'FormattedText', arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.text.FormattedText> dev.ultreon.quantum.client.font.WordWrapper.wrap(dev.ultreon.quantum.text.FormattedText,int)"""
        return 'List'._wrap(super(_WordWrapper, self).wrap(arg0, _int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())