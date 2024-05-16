from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.gui.icon.Icon as _Icon
_Icon = _Icon
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.icon.ImageIcon as _ImageIcon
_ImageIcon = _ImageIcon
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ImageIcon():
    """dev.ultreon.quantum.client.gui.icon.ImageIcon"""
 
    @staticmethod
    def _wrap(java_value: _ImageIcon) -> 'ImageIcon':
        return ImageIcon(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ImageIcon):
        """
        Dynamic initializer for ImageIcon.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ImageIcon__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ImageIcon__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public default void dev.ultreon.quantum.client.gui.icon.Icon.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Icon, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def __init__(self, arg0: 'Identifier', arg1: int, arg2: int):
        """public dev.ultreon.quantum.client.gui.icon.ImageIcon(dev.ultreon.quantum.util.Identifier,int,int)"""
        val = _ImageIcon(arg0, _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def id(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.gui.icon.ImageIcon.id()"""
        return 'util.Identifier'._wrap(super(ImageIcon, self).id())

    @override
    @overload
    def v(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.v()"""
        return int._wrap(super(ImageIcon, self).v())

    @override
    @overload
    def texHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.texHeight()"""
        return int._wrap(super(ImageIcon, self).texHeight())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.icon.ImageIcon.equals(java.lang.Object)"""
        return bool._wrap(super(_ImageIcon, self).equals(arg0))

    @override
    @overload
    def u(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.u()"""
        return int._wrap(super(ImageIcon, self).u())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: float, arg2: float, arg3: int, arg4: int, arg5: float):
        """public default void dev.ultreon.quantum.client.gui.icon.Icon.render(dev.ultreon.quantum.client.gui.Renderer,float,float,int,int,float)"""
        super(_Icon, self).render(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Identifier'):
        """public dev.ultreon.quantum.client.gui.icon.ImageIcon(dev.ultreon.quantum.util.Identifier)"""
        val = _ImageIcon(arg0)
        self.__wrapper = val

    @override
    @overload
    def texWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.texWidth()"""
        return int._wrap(super(ImageIcon, self).texWidth())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.hashCode()"""
        return int._wrap(super(ImageIcon, self).hashCode())

    @override
    @overload
    def width(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.width()"""
        return int._wrap(super(ImageIcon, self).width())

    @override
    @overload
    def height(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.height()"""
        return int._wrap(super(ImageIcon, self).height())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.icon.ImageIcon.toString()"""
        return str._wrap(super(ImageIcon, self).toString())

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

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.icon.ImageIcon
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.gui.icon.Icon as _Icon
_Icon = _Icon
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.icon.ImageIcon as _ImageIcon
_ImageIcon = _ImageIcon
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ImageIcon():
    """dev.ultreon.quantum.client.gui.icon.ImageIcon"""
 
    @staticmethod
    def _wrap(java_value: _ImageIcon) -> 'ImageIcon':
        return ImageIcon(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ImageIcon):
        """
        Dynamic initializer for ImageIcon.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ImageIcon__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ImageIcon__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public default void dev.ultreon.quantum.client.gui.icon.Icon.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Icon, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def __init__(self, arg0: 'Identifier', arg1: int, arg2: int):
        """public dev.ultreon.quantum.client.gui.icon.ImageIcon(dev.ultreon.quantum.util.Identifier,int,int)"""
        val = _ImageIcon(arg0, _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def id(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.gui.icon.ImageIcon.id()"""
        return 'util.Identifier'._wrap(super(ImageIcon, self).id())

    @override
    @overload
    def v(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.v()"""
        return int._wrap(super(ImageIcon, self).v())

    @override
    @overload
    def texHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.texHeight()"""
        return int._wrap(super(ImageIcon, self).texHeight())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.icon.ImageIcon.equals(java.lang.Object)"""
        return bool._wrap(super(_ImageIcon, self).equals(arg0))

    @override
    @overload
    def u(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.u()"""
        return int._wrap(super(ImageIcon, self).u())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: float, arg2: float, arg3: int, arg4: int, arg5: float):
        """public default void dev.ultreon.quantum.client.gui.icon.Icon.render(dev.ultreon.quantum.client.gui.Renderer,float,float,int,int,float)"""
        super(_Icon, self).render(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Identifier'):
        """public dev.ultreon.quantum.client.gui.icon.ImageIcon(dev.ultreon.quantum.util.Identifier)"""
        val = _ImageIcon(arg0)
        self.__wrapper = val

    @override
    @overload
    def texWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.texWidth()"""
        return int._wrap(super(ImageIcon, self).texWidth())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.hashCode()"""
        return int._wrap(super(ImageIcon, self).hashCode())

    @override
    @overload
    def width(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.width()"""
        return int._wrap(super(ImageIcon, self).width())

    @override
    @overload
    def height(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.height()"""
        return int._wrap(super(ImageIcon, self).height())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.icon.ImageIcon.toString()"""
        return str._wrap(super(ImageIcon, self).toString())

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

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.icon.ImageIcon 
 
 
# CLASS: dev.ultreon.quantum.client.gui.icon.MessageIcon
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.gui.icon.Icon as _Icon
_Icon = _Icon
from builtins import str
import dev.ultreon.quantum.client.gui.icon.MessageIcon as _MessageIcon
_MessageIcon = _MessageIcon
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MessageIcon():
    """dev.ultreon.quantum.client.gui.icon.MessageIcon"""
 
    @staticmethod
    def _wrap(java_value: _MessageIcon) -> 'MessageIcon':
        return MessageIcon(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MessageIcon):
        """
        Dynamic initializer for MessageIcon.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MessageIcon__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MessageIcon__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def id(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.gui.icon.MessageIcon.id()"""
        return 'util.Identifier'._wrap(super(MessageIcon, self).id())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public default void dev.ultreon.quantum.client.gui.icon.Icon.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Icon, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public dev.ultreon.quantum.client.gui.icon.MessageIcon(int,int,int,int)"""
        val = _MessageIcon(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.icon.MessageIcon.toString()"""
        return str._wrap(super(MessageIcon, self).toString())

    @override
    @overload
    def u(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.MessageIcon.u()"""
        return int._wrap(super(MessageIcon, self).u())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: float, arg2: float, arg3: int, arg4: int, arg5: float):
        """public default void dev.ultreon.quantum.client.gui.icon.Icon.render(dev.ultreon.quantum.client.gui.Renderer,float,float,int,int,float)"""
        super(_Icon, self).render(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def v(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.MessageIcon.v()"""
        return int._wrap(super(MessageIcon, self).v())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.MessageIcon.hashCode()"""
        return int._wrap(super(MessageIcon, self).hashCode())

    @override
    @overload
    def height(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.MessageIcon.height()"""
        return int._wrap(super(MessageIcon, self).height())

    @override
    @overload
    def texHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.MessageIcon.texHeight()"""
        return int._wrap(super(MessageIcon, self).texHeight())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.icon.MessageIcon.equals(java.lang.Object)"""
        return bool._wrap(super(_MessageIcon, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def width(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.MessageIcon.width()"""
        return int._wrap(super(MessageIcon, self).width())

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
    def texWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.MessageIcon.texWidth()"""
        return int._wrap(super(MessageIcon, self).texWidth())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


MessageIcon.ERROR = MessageIcon._wrap(_ERROR.ERROR)

MessageIcon.DANGER = MessageIcon._wrap(_DANGER.DANGER)

MessageIcon.WARNING = MessageIcon._wrap(_WARNING.WARNING)

MessageIcon.INFO = MessageIcon._wrap(_INFO.INFO)

MessageIcon.QUESTION = MessageIcon._wrap(_QUESTION.QUESTION) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.icon.Icon
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.gui.icon.Icon as _Icon
_Icon = _Icon
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

from abc import abstractmethod, ABC
 
class Icon():
    """dev.ultreon.quantum.client.gui.icon.Icon"""
 
    @staticmethod
    def _wrap(java_value: _Icon) -> 'Icon':
        return Icon(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Icon):
        """
        Dynamic initializer for Icon.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Icon__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Icon__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def id(self, ):
        """public abstract dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.gui.icon.Icon.id()"""
        pass

    @overload
    def render(self, arg0: 'Renderer', arg1: float, arg2: float, arg3: int, arg4: int, arg5: float):
        """public default void dev.ultreon.quantum.client.gui.icon.Icon.render(dev.ultreon.quantum.client.gui.Renderer,float,float,int,int,float)"""
        super(_Icon, self).render(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5))

    @abstractmethod
    def v(self, ):
        """public abstract int dev.ultreon.quantum.client.gui.icon.Icon.v()"""
        pass

    @abstractmethod
    def width(self, ):
        """public abstract int dev.ultreon.quantum.client.gui.icon.Icon.width()"""
        pass

    @abstractmethod
    def height(self, ):
        """public abstract int dev.ultreon.quantum.client.gui.icon.Icon.height()"""
        pass

    @abstractmethod
    def texWidth(self, ):
        """public abstract int dev.ultreon.quantum.client.gui.icon.Icon.texWidth()"""
        pass

    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public default void dev.ultreon.quantum.client.gui.icon.Icon.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Icon, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @abstractmethod
    def u(self, ):
        """public abstract int dev.ultreon.quantum.client.gui.icon.Icon.u()"""
        pass

    @abstractmethod
    def texHeight(self, ):
        """public abstract int dev.ultreon.quantum.client.gui.icon.Icon.texHeight()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.gui.icon.GenericIcon
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.gui.icon.Icon as _Icon
_Icon = _Icon
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.client.gui.icon.GenericIcon as _GenericIcon
_GenericIcon = _GenericIcon
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GenericIcon():
    """dev.ultreon.quantum.client.gui.icon.GenericIcon"""
 
    @staticmethod
    def _wrap(java_value: _GenericIcon) -> 'GenericIcon':
        return GenericIcon(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GenericIcon):
        """
        Dynamic initializer for GenericIcon.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GenericIcon__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GenericIcon__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public default void dev.ultreon.quantum.client.gui.icon.Icon.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(_Icon, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.icon.GenericIcon.toString()"""
        return str._wrap(super(GenericIcon, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.icon.GenericIcon.equals(java.lang.Object)"""
        return bool._wrap(super(_GenericIcon, self).equals(arg0))

    @override
    @overload
    def texWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.GenericIcon.texWidth()"""
        return int._wrap(super(GenericIcon, self).texWidth())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def width(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.GenericIcon.width()"""
        return int._wrap(super(GenericIcon, self).width())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: float, arg2: float, arg3: int, arg4: int, arg5: float):
        """public default void dev.ultreon.quantum.client.gui.icon.Icon.render(dev.ultreon.quantum.client.gui.Renderer,float,float,int,int,float)"""
        super(_Icon, self).render(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5))

    @override
    @overload
    def texHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.GenericIcon.texHeight()"""
        return int._wrap(super(GenericIcon, self).texHeight())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.GenericIcon.hashCode()"""
        return int._wrap(super(GenericIcon, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def u(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.GenericIcon.u()"""
        return int._wrap(super(GenericIcon, self).u())

    @override
    @overload
    def height(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.GenericIcon.height()"""
        return int._wrap(super(GenericIcon, self).height())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public dev.ultreon.quantum.client.gui.icon.GenericIcon(int,int,int,int)"""
        val = _GenericIcon(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def id(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.gui.icon.GenericIcon.id()"""
        return 'util.Identifier'._wrap(super(GenericIcon, self).id())

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

    @override
    @overload
    def v(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.GenericIcon.v()"""
        return int._wrap(super(GenericIcon, self).v())


GenericIcon.UNLOCKED = GenericIcon._wrap(_UNLOCKED.UNLOCKED)

GenericIcon.RELOAD = GenericIcon._wrap(_RELOAD.RELOAD)

GenericIcon.LOCKED = GenericIcon._wrap(_LOCKED.LOCKED)