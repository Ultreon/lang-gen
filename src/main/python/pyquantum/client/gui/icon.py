from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.quantum.client.gui.icon.Icon as __Icon
__Icon = __Icon
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.gui.icon.ImageIcon as __ImageIcon
__ImageIcon = __ImageIcon
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ImageIcon(__Icon, Icon):
    """dev.ultreon.quantum.client.gui.icon.ImageIcon"""
 
    @staticmethod
    def __wrap(java_value: __ImageIcon) -> 'ImageIcon':
        return ImageIcon(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ImageIcon):
        """
        Dynamic initializer for ImageIcon.
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
    def texHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.texHeight()"""
        return int.__wrap(super(ImageIcon, self).texHeight())

    @override
    @overload
    def v(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.v()"""
        return int.__wrap(super(ImageIcon, self).v())

    @override
    @overload
    def texWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.texWidth()"""
        return int.__wrap(super(ImageIcon, self).texWidth())

    @overload
    def __init__(self, arg0: 'Identifier', arg1: int, arg2: int):
        """public dev.ultreon.quantum.client.gui.icon.ImageIcon(dev.ultreon.quantum.util.Identifier,int,int)"""
        val = __ImageIcon(arg0, __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.icon.ImageIcon.toString()"""
        return str.__wrap(super(ImageIcon, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.hashCode()"""
        return int.__wrap(super(ImageIcon, self).hashCode())

    @override
    @overload
    def height(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.height()"""
        return int.__wrap(super(ImageIcon, self).height())

    @override
    @overload
    def width(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.width()"""
        return int.__wrap(super(ImageIcon, self).width())

    @override
    @overload
    def id(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.gui.icon.ImageIcon.id()"""
        return 'util.Identifier'.__wrap(super(ImageIcon, self).id())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Identifier'):
        """public dev.ultreon.quantum.client.gui.icon.ImageIcon(dev.ultreon.quantum.util.Identifier)"""
        val = __ImageIcon(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.icon.ImageIcon.equals(java.lang.Object)"""
        return bool.__wrap(super(__ImageIcon, self).equals(arg0))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public default void dev.ultreon.quantum.client.gui.icon.Icon.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Icon, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def u(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.u()"""
        return int.__wrap(super(ImageIcon, self).u())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: float, arg2: float, arg3: int, arg4: int, arg5: float):
        """public default void dev.ultreon.quantum.client.gui.icon.Icon.render(dev.ultreon.quantum.client.gui.Renderer,float,float,int,int,float)"""
        super(__Icon, self).render(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.icon.ImageIcon
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.quantum.client.gui.icon.Icon as __Icon
__Icon = __Icon
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.gui.icon.ImageIcon as __ImageIcon
__ImageIcon = __ImageIcon
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ImageIcon(__Icon, Icon):
    """dev.ultreon.quantum.client.gui.icon.ImageIcon"""
 
    @staticmethod
    def __wrap(java_value: __ImageIcon) -> 'ImageIcon':
        return ImageIcon(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ImageIcon):
        """
        Dynamic initializer for ImageIcon.
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
    def texHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.texHeight()"""
        return int.__wrap(super(ImageIcon, self).texHeight())

    @override
    @overload
    def v(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.v()"""
        return int.__wrap(super(ImageIcon, self).v())

    @override
    @overload
    def texWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.texWidth()"""
        return int.__wrap(super(ImageIcon, self).texWidth())

    @overload
    def __init__(self, arg0: 'Identifier', arg1: int, arg2: int):
        """public dev.ultreon.quantum.client.gui.icon.ImageIcon(dev.ultreon.quantum.util.Identifier,int,int)"""
        val = __ImageIcon(arg0, __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.icon.ImageIcon.toString()"""
        return str.__wrap(super(ImageIcon, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.hashCode()"""
        return int.__wrap(super(ImageIcon, self).hashCode())

    @override
    @overload
    def height(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.height()"""
        return int.__wrap(super(ImageIcon, self).height())

    @override
    @overload
    def width(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.width()"""
        return int.__wrap(super(ImageIcon, self).width())

    @override
    @overload
    def id(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.gui.icon.ImageIcon.id()"""
        return 'util.Identifier'.__wrap(super(ImageIcon, self).id())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Identifier'):
        """public dev.ultreon.quantum.client.gui.icon.ImageIcon(dev.ultreon.quantum.util.Identifier)"""
        val = __ImageIcon(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.icon.ImageIcon.equals(java.lang.Object)"""
        return bool.__wrap(super(__ImageIcon, self).equals(arg0))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public default void dev.ultreon.quantum.client.gui.icon.Icon.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Icon, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def u(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.ImageIcon.u()"""
        return int.__wrap(super(ImageIcon, self).u())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: float, arg2: float, arg3: int, arg4: int, arg5: float):
        """public default void dev.ultreon.quantum.client.gui.icon.Icon.render(dev.ultreon.quantum.client.gui.Renderer,float,float,int,int,float)"""
        super(__Icon, self).render(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.icon.ImageIcon 
 
 
# CLASS: dev.ultreon.quantum.client.gui.icon.MessageIcon
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.quantum.client.gui.icon.Icon as __Icon
__Icon = __Icon
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.gui.icon.MessageIcon as __MessageIcon
__MessageIcon = __MessageIcon
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MessageIcon(__Icon, Icon):
    """dev.ultreon.quantum.client.gui.icon.MessageIcon"""
 
    @staticmethod
    def __wrap(java_value: __MessageIcon) -> 'MessageIcon':
        return MessageIcon(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MessageIcon):
        """
        Dynamic initializer for MessageIcon.
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
 
    # public static final dev.ultreon.quantum.client.gui.icon.MessageIcon dev.ultreon.quantum.client.gui.icon.MessageIcon.ERROR
    ERROR: 'MessageIcon' = __wrap(__MessageIcon.ERROR)

    # public static final dev.ultreon.quantum.client.gui.icon.MessageIcon dev.ultreon.quantum.client.gui.icon.MessageIcon.DANGER
    DANGER: 'MessageIcon' = __wrap(__MessageIcon.DANGER)

    # public static final dev.ultreon.quantum.client.gui.icon.MessageIcon dev.ultreon.quantum.client.gui.icon.MessageIcon.QUESTION
    QUESTION: 'MessageIcon' = __wrap(__MessageIcon.QUESTION)

    # public static final dev.ultreon.quantum.client.gui.icon.MessageIcon dev.ultreon.quantum.client.gui.icon.MessageIcon.INFO
    INFO: 'MessageIcon' = __wrap(__MessageIcon.INFO)

    # public static final dev.ultreon.quantum.client.gui.icon.MessageIcon dev.ultreon.quantum.client.gui.icon.MessageIcon.WARNING
    WARNING: 'MessageIcon' = __wrap(__MessageIcon.WARNING)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def texHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.MessageIcon.texHeight()"""
        return int.__wrap(super(MessageIcon, self).texHeight())

    @override
    @overload
    def u(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.MessageIcon.u()"""
        return int.__wrap(super(MessageIcon, self).u())

    @override
    @overload
    def width(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.MessageIcon.width()"""
        return int.__wrap(super(MessageIcon, self).width())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.MessageIcon.hashCode()"""
        return int.__wrap(super(MessageIcon, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def height(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.MessageIcon.height()"""
        return int.__wrap(super(MessageIcon, self).height())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public dev.ultreon.quantum.client.gui.icon.MessageIcon(int,int,int,int)"""
        val = __MessageIcon(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.icon.MessageIcon.equals(java.lang.Object)"""
        return bool.__wrap(super(__MessageIcon, self).equals(arg0))

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public default void dev.ultreon.quantum.client.gui.icon.Icon.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Icon, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.icon.MessageIcon.toString()"""
        return str.__wrap(super(MessageIcon, self).toString())

    @override
    @overload
    def texWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.MessageIcon.texWidth()"""
        return int.__wrap(super(MessageIcon, self).texWidth())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: float, arg2: float, arg3: int, arg4: int, arg5: float):
        """public default void dev.ultreon.quantum.client.gui.icon.Icon.render(dev.ultreon.quantum.client.gui.Renderer,float,float,int,int,float)"""
        super(__Icon, self).render(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5))

    @override
    @overload
    def v(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.MessageIcon.v()"""
        return int.__wrap(super(MessageIcon, self).v())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def id(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.gui.icon.MessageIcon.id()"""
        return 'util.Identifier'.__wrap(super(MessageIcon, self).id()) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.icon.Icon
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.gui.icon.Icon as __Icon
__Icon = __Icon
import java.lang.Float as __float
try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

from abc import abstractmethod, ABC
import java.lang.Integer as __int
 
class Icon(ABC):
    """dev.ultreon.quantum.client.gui.icon.Icon"""
 
    @staticmethod
    def __wrap(java_value: __Icon) -> 'Icon':
        return Icon(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Icon):
        """
        Dynamic initializer for Icon.
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
 
    @abstractmethod
    def id(self, ):
        """public abstract dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.gui.icon.Icon.id()"""
        pass

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

    @abstractmethod
    def u(self, ):
        """public abstract int dev.ultreon.quantum.client.gui.icon.Icon.u()"""
        pass

    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public default void dev.ultreon.quantum.client.gui.icon.Icon.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Icon, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def render(self, arg0: 'Renderer', arg1: float, arg2: float, arg3: int, arg4: int, arg5: float):
        """public default void dev.ultreon.quantum.client.gui.icon.Icon.render(dev.ultreon.quantum.client.gui.Renderer,float,float,int,int,float)"""
        super(__Icon, self).render(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5))

    @abstractmethod
    def texHeight(self, ):
        """public abstract int dev.ultreon.quantum.client.gui.icon.Icon.texHeight()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.gui.icon.GenericIcon
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.quantum.client.gui.icon.Icon as __Icon
__Icon = __Icon
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
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.gui.icon.GenericIcon as __GenericIcon
__GenericIcon = __GenericIcon
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GenericIcon(__Icon, Icon):
    """dev.ultreon.quantum.client.gui.icon.GenericIcon"""
 
    @staticmethod
    def __wrap(java_value: __GenericIcon) -> 'GenericIcon':
        return GenericIcon(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GenericIcon):
        """
        Dynamic initializer for GenericIcon.
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
 
    # public static final dev.ultreon.quantum.client.gui.icon.GenericIcon dev.ultreon.quantum.client.gui.icon.GenericIcon.UNLOCKED
    UNLOCKED: 'GenericIcon' = __wrap(__GenericIcon.UNLOCKED)

    # public static final dev.ultreon.quantum.client.gui.icon.GenericIcon dev.ultreon.quantum.client.gui.icon.GenericIcon.RELOAD
    RELOAD: 'GenericIcon' = __wrap(__GenericIcon.RELOAD)

    # public static final dev.ultreon.quantum.client.gui.icon.GenericIcon dev.ultreon.quantum.client.gui.icon.GenericIcon.LOCKED
    LOCKED: 'GenericIcon' = __wrap(__GenericIcon.LOCKED)


    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.icon.GenericIcon.equals(java.lang.Object)"""
        return bool.__wrap(super(__GenericIcon, self).equals(arg0))

    @override
    @overload
    def u(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.GenericIcon.u()"""
        return int.__wrap(super(GenericIcon, self).u())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def texHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.GenericIcon.texHeight()"""
        return int.__wrap(super(GenericIcon, self).texHeight())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def width(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.GenericIcon.width()"""
        return int.__wrap(super(GenericIcon, self).width())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.GenericIcon.hashCode()"""
        return int.__wrap(super(GenericIcon, self).hashCode())

    @override
    @overload
    def texWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.GenericIcon.texWidth()"""
        return int.__wrap(super(GenericIcon, self).texWidth())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.icon.GenericIcon.toString()"""
        return str.__wrap(super(GenericIcon, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public default void dev.ultreon.quantum.client.gui.icon.Icon.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__Icon, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def id(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.gui.icon.GenericIcon.id()"""
        return 'util.Identifier'.__wrap(super(GenericIcon, self).id())

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: float, arg2: float, arg3: int, arg4: int, arg5: float):
        """public default void dev.ultreon.quantum.client.gui.icon.Icon.render(dev.ultreon.quantum.client.gui.Renderer,float,float,int,int,float)"""
        super(__Icon, self).render(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public dev.ultreon.quantum.client.gui.icon.GenericIcon(int,int,int,int)"""
        val = __GenericIcon(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def v(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.GenericIcon.v()"""
        return int.__wrap(super(GenericIcon, self).v())

    @override
    @overload
    def height(self) -> int:
        """public int dev.ultreon.quantum.client.gui.icon.GenericIcon.height()"""
        return int.__wrap(super(GenericIcon, self).height())