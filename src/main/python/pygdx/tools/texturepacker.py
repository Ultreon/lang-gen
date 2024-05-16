from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import com.badlogic.gdx.tools.texturepacker.TexturePacker as _TexturePacker_Page
_Page = _TexturePacker_Page.Page
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Page():
    """com.badlogic.gdx.tools.texturepacker.TexturePacker.Page"""
 
    @staticmethod
    def _wrap(java_value: _Page) -> 'Page':
        return Page(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Page):
        """
        Dynamic initializer for Page.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Page__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Page__wrapper":
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$Page()"""
        val = _Page()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$Page()"""
        val = _Page()
        self.__wrapper = val

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.TexturePacker$Page
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import com.badlogic.gdx.tools.texturepacker.TexturePacker as _TexturePacker_Page
_Page = _TexturePacker_Page.Page
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Page():
    """com.badlogic.gdx.tools.texturepacker.TexturePacker.Page"""
 
    @staticmethod
    def _wrap(java_value: _Page) -> 'Page':
        return Page(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Page):
        """
        Dynamic initializer for Page.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Page__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Page__wrapper":
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$Page()"""
        val = _Page()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$Page()"""
        val = _Page()
        self.__wrapper = val

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.TexturePacker$Page 
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.TexturePacker$Packer
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.tools.texturepacker.TexturePacker as _TexturePacker_Packer
_Packer = _TexturePacker_Packer.Packer
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from abc import abstractmethod, ABC
 
class Packer():
    """com.badlogic.gdx.tools.texturepacker.TexturePacker.Packer"""
 
    @staticmethod
    def _wrap(java_value: _Packer) -> 'Packer':
        return Packer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Packer):
        """
        Dynamic initializer for Packer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Packer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Packer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def pack(self, arg0: 'Array'):
        """public abstract com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Page> com.badlogic.gdx.tools.texturepacker.TexturePacker$Packer.pack(com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect>)"""
        pass

    @abstractmethod
    def pack(self, arg0: 'ProgressListener', arg1: 'Array'):
        """public abstract com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Page> com.badlogic.gdx.tools.texturepacker.TexturePacker$Packer.pack(com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener,com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect>)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener
import com.badlogic.gdx.tools.texturepacker.TexturePacker as _TexturePacker_ProgressListener
_ProgressListener = _TexturePacker_ProgressListener.ProgressListener
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ProgressListener():
    """com.badlogic.gdx.tools.texturepacker.TexturePacker.ProgressListener"""
 
    @staticmethod
    def _wrap(java_value: _ProgressListener) -> 'ProgressListener':
        return ProgressListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ProgressListener):
        """
        Dynamic initializer for ProgressListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ProgressListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ProgressListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def start(self, arg0: float):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.start(float)"""
        super(_ProgressListener, self).start(_float.valueOf(arg0))

    @overload
    def end(self):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.end()"""
        super(ProgressListener, self).end()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setCount(self, arg0: int):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.setCount(int)"""
        super(_ProgressListener, self).setCount(_int.valueOf(arg0))

    @overload
    def setTotal(self, arg0: int):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.setTotal(int)"""
        super(_ProgressListener, self).setTotal(_int.valueOf(arg0))

    @overload
    def isCancelled(self) -> bool:
        """public boolean com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.isCancelled()"""
        return bool._wrap(super(ProgressListener, self).isCancelled())

    @overload
    def getMessage(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.getMessage()"""
        return str._wrap(super(ProgressListener, self).getMessage())

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
    def getTotal(self) -> int:
        """public int com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.getTotal()"""
        return int._wrap(super(ProgressListener, self).getTotal())

    @overload
    def update(self, arg0: float):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.update(float)"""
        super(_ProgressListener, self).update(_float.valueOf(arg0))

    @overload
    def reset(self):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.reset()"""
        super(ProgressListener, self).reset()

    @overload
    def getCount(self) -> int:
        """public int com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.getCount()"""
        return int._wrap(super(ProgressListener, self).getCount())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener()"""
        val = _ProgressListener()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def cancel(self):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.cancel()"""
        super(ProgressListener, self).cancel()

    @overload
    def setMessage(self, arg0: str):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.setMessage(java.lang.String)"""
        super(_ProgressListener, self).setMessage(arg0)

    @overload
    def set(self, arg0: str):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.set(java.lang.String)"""
        super(_ProgressListener, self).set(arg0)

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
    def __init__(self, ):
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener()"""
        val = _ProgressListener()
        self.__wrapper = val

    @abstractmethod
    def progress(self, arg0: float):
        """public abstract void com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.progress(float)"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def update(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.update(int,int)"""
        return bool._wrap(super(_ProgressListener, self).update(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.MaxRectsPacker
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.tools.texturepacker.MaxRectsPacker as _MaxRectsPacker
_MaxRectsPacker = _MaxRectsPacker
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MaxRectsPacker():
    """com.badlogic.gdx.tools.texturepacker.MaxRectsPacker"""
 
    @staticmethod
    def _wrap(java_value: _MaxRectsPacker) -> 'MaxRectsPacker':
        return MaxRectsPacker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MaxRectsPacker):
        """
        Dynamic initializer for MaxRectsPacker.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MaxRectsPacker__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MaxRectsPacker__wrapper":
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

    @overload
    def pack(self, arg0: 'ProgressListener', arg1: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Page> com.badlogic.gdx.tools.texturepacker.MaxRectsPacker.pack(com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener,com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect>)"""
        return 'utils.Array'._wrap(super(_MaxRectsPacker, self).pack(arg0, arg1))

    @overload
    def pack(self, arg0: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Page> com.badlogic.gdx.tools.texturepacker.MaxRectsPacker.pack(com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect>)"""
        return 'utils.Array'._wrap(super(_MaxRectsPacker, self).pack(arg0))

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

    @overload
    def __init__(self, arg0: 'Settings'):
        """public com.badlogic.gdx.tools.texturepacker.MaxRectsPacker(com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings)"""
        val = _MaxRectsPacker(arg0)
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.TexturePacker$Resampling
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import com.badlogic.gdx.tools.texturepacker.TexturePacker as _TexturePacker_Resampling
_Resampling = _TexturePacker_Resampling.Resampling
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Resampling():
    """com.badlogic.gdx.tools.texturepacker.TexturePacker.Resampling"""
 
    @staticmethod
    def _wrap(java_value: _Resampling) -> 'Resampling':
        return Resampling(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Resampling):
        """
        Dynamic initializer for Resampling.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Resampling__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Resampling__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def values() -> List['Resampling']:
        """public static com.badlogic.gdx.tools.texturepacker.TexturePacker$Resampling[] com.badlogic.gdx.tools.texturepacker.TexturePacker$Resampling.values()"""
        return List[Resampling]._wrap(_Resampling.values())

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Resampling':
        """public static com.badlogic.gdx.tools.texturepacker.TexturePacker$Resampling com.badlogic.gdx.tools.texturepacker.TexturePacker$Resampling.valueOf(java.lang.String)"""
        return Resampling._wrap(_Resampling.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.TexturePacker$Alias
import com.badlogic.gdx.tools.texturepacker.TexturePacker as _TexturePacker_Alias
_Alias = _TexturePacker_Alias.Alias
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Alias():
    """com.badlogic.gdx.tools.texturepacker.TexturePacker.Alias"""
 
    @staticmethod
    def _wrap(java_value: _Alias) -> 'Alias':
        return Alias(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Alias):
        """
        Dynamic initializer for Alias.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Alias__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Alias__wrapper":
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

    @overload
    def apply(self, arg0: 'Rect'):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker$Alias.apply(com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect)"""
        super(_Alias, self).apply(arg0)

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
    def compareTo(self, arg0: 'Alias') -> int:
        """public int com.badlogic.gdx.tools.texturepacker.TexturePacker$Alias.compareTo(com.badlogic.gdx.tools.texturepacker.TexturePacker$Alias)"""
        return int._wrap(super(_Alias, self).compareTo(arg0))

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
    def __init__(self, arg0: 'Rect'):
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$Alias(com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect)"""
        val = _Alias(arg0)
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
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.GridPacker
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.tools.texturepacker.GridPacker as _GridPacker
_GridPacker = _GridPacker
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GridPacker():
    """com.badlogic.gdx.tools.texturepacker.GridPacker"""
 
    @staticmethod
    def _wrap(java_value: _GridPacker) -> 'GridPacker':
        return GridPacker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GridPacker):
        """
        Dynamic initializer for GridPacker.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GridPacker__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GridPacker__wrapper":
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

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Settings'):
        """public com.badlogic.gdx.tools.texturepacker.GridPacker(com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings)"""
        val = _GridPacker(arg0)
        self.__wrapper = val

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
    def pack(self, arg0: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Page> com.badlogic.gdx.tools.texturepacker.GridPacker.pack(com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect>)"""
        return 'utils.Array'._wrap(super(_GridPacker, self).pack(arg0))

    @overload
    def pack(self, arg0: 'ProgressListener', arg1: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Page> com.badlogic.gdx.tools.texturepacker.GridPacker.pack(com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener,com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect>)"""
        return 'utils.Array'._wrap(super(_GridPacker, self).pack(arg0, arg1))

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
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.TexturePacker
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.File as File
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.tools.texturepacker.TexturePacker as _TexturePacker
_TexturePacker = _TexturePacker
import java.lang.String as _string
import java.lang.Integer as _int
import java.awt.image.BufferedImage as BufferedImage
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TexturePacker():
    """com.badlogic.gdx.tools.texturepacker.TexturePacker"""
 
    @staticmethod
    def _wrap(java_value: _TexturePacker) -> 'TexturePacker':
        return TexturePacker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TexturePacker):
        """
        Dynamic initializer for TexturePacker.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TexturePacker__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TexturePacker__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getRootPath(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.texturepacker.TexturePacker.getRootPath()"""
        return str._wrap(super(TexturePacker, self).getRootPath())

    @staticmethod
    @overload
    def process(arg0: str, arg1: str, arg2: str):
        """public static void com.badlogic.gdx.tools.texturepacker.TexturePacker.process(java.lang.String,java.lang.String,java.lang.String)"""
        _TexturePacker.process(arg0, arg1, arg2)

    @overload
    def setProgressListener(self, arg0: 'ProgressListener'):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker.setProgressListener(com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener)"""
        super(_TexturePacker, self).setProgressListener(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def addImage(self, arg0: 'File'):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker.addImage(java.io.File)"""
        super(_TexturePacker, self).addImage(arg0)

    @overload
    def setPacker(self, arg0: 'Packer'):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker.setPacker(com.badlogic.gdx.tools.texturepacker.TexturePacker$Packer)"""
        super(_TexturePacker, self).setPacker(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def isModified(arg0: str, arg1: str, arg2: str, arg3: 'Settings') -> bool:
        """public static boolean com.badlogic.gdx.tools.texturepacker.TexturePacker.isModified(java.lang.String,java.lang.String,java.lang.String,com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings)"""
        return bool._wrap(_TexturePacker.isModified(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def processIfModified(arg0: 'Settings', arg1: str, arg2: str, arg3: str) -> bool:
        """public static boolean com.badlogic.gdx.tools.texturepacker.TexturePacker.processIfModified(com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings,java.lang.String,java.lang.String,java.lang.String)"""
        return bool._wrap(_TexturePacker.processIfModified(arg0, arg1, arg2, arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void com.badlogic.gdx.tools.texturepacker.TexturePacker.main(java.lang.String[]) throws java.lang.Exception"""
        _TexturePacker.main(arg0)

    @staticmethod
    @overload
    def process(arg0: 'Settings', arg1: str, arg2: str, arg3: str, arg4: 'ProgressListener'):
        """public static void com.badlogic.gdx.tools.texturepacker.TexturePacker.process(com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings,java.lang.String,java.lang.String,java.lang.String,com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener)"""
        _TexturePacker.process(arg0, arg1, arg2, arg3, arg4)

    @overload
    def setRootDir(self, arg0: 'File'):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker.setRootDir(java.io.File)"""
        super(_TexturePacker, self).setRootDir(arg0)

    @overload
    def addImage(self, arg0: 'BufferedImage', arg1: str):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker.addImage(java.awt.image.BufferedImage,java.lang.String)"""
        super(_TexturePacker, self).addImage(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Settings'):
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker(com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings)"""
        val = _TexturePacker(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def process(arg0: 'Settings', arg1: str, arg2: str, arg3: str):
        """public static void com.badlogic.gdx.tools.texturepacker.TexturePacker.process(com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings,java.lang.String,java.lang.String,java.lang.String)"""
        _TexturePacker.process(arg0, arg1, arg2, arg3)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def pack(self, arg0: 'File', arg1: str):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker.pack(java.io.File,java.lang.String)"""
        super(_TexturePacker, self).pack(arg0, arg1)

    @staticmethod
    @overload
    def processIfModified(arg0: str, arg1: str, arg2: str) -> bool:
        """public static boolean com.badlogic.gdx.tools.texturepacker.TexturePacker.processIfModified(java.lang.String,java.lang.String,java.lang.String)"""
        return bool._wrap(_TexturePacker.processIfModified(arg0, arg1, arg2))

    @overload
    def __init__(self, arg0: 'File', arg1: 'Settings'):
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker(java.io.File,com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings)"""
        val = _TexturePacker(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.ColorBleedEffect
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.awt.image.BufferedImage as _BufferedImage
_BufferedImage = _BufferedImage
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.tools.texturepacker.ColorBleedEffect as _ColorBleedEffect
_ColorBleedEffect = _ColorBleedEffect
import java.lang.Integer as _int
import java.awt.image.BufferedImage as BufferedImage
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ColorBleedEffect():
    """com.badlogic.gdx.tools.texturepacker.ColorBleedEffect"""
 
    @staticmethod
    def _wrap(java_value: _ColorBleedEffect) -> 'ColorBleedEffect':
        return ColorBleedEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ColorBleedEffect):
        """
        Dynamic initializer for ColorBleedEffect.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ColorBleedEffect__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ColorBleedEffect__wrapper":
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
    def __init__(self, ):
        """public com.badlogic.gdx.tools.texturepacker.ColorBleedEffect()"""
        val = _ColorBleedEffect()
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

    @overload
    def processImage(self, arg0: 'BufferedImage', arg1: int) -> 'BufferedImage':
        """public java.awt.image.BufferedImage com.badlogic.gdx.tools.texturepacker.ColorBleedEffect.processImage(java.awt.image.BufferedImage,int)"""
        return 'BufferedImage'._wrap(super(_ColorBleedEffect, self).processImage(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.texturepacker.ColorBleedEffect()"""
        val = _ColorBleedEffect()
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.TextureUnpacker
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import com.badlogic.gdx.tools.texturepacker.TextureUnpacker as _TextureUnpacker
_TextureUnpacker = _TextureUnpacker
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextureUnpacker():
    """com.badlogic.gdx.tools.texturepacker.TextureUnpacker"""
 
    @staticmethod
    def _wrap(java_value: _TextureUnpacker) -> 'TextureUnpacker':
        return TextureUnpacker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureUnpacker):
        """
        Dynamic initializer for TextureUnpacker.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureUnpacker__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureUnpacker__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.texturepacker.TextureUnpacker()"""
        val = _TextureUnpacker()
        self.__wrapper = val

    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void com.badlogic.gdx.tools.texturepacker.TextureUnpacker.main(java.lang.String[])"""
        _TextureUnpacker.main(arg0)

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setQuiet(self, arg0: bool):
        """public void com.badlogic.gdx.tools.texturepacker.TextureUnpacker.setQuiet(boolean)"""
        super(_TextureUnpacker, self).setQuiet(_boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.texturepacker.TextureUnpacker()"""
        val = _TextureUnpacker()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def splitAtlas(self, arg0: 'TextureAtlasData', arg1: str):
        """public void com.badlogic.gdx.tools.texturepacker.TextureUnpacker.splitAtlas(com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData,java.lang.String)"""
        super(_TextureUnpacker, self).splitAtlas(arg0, arg1)

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
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.TexturePackerUpscaleTest
from builtins import str
import com.badlogic.gdx.tools.texturepacker.TexturePackerUpscaleTest as _TexturePackerUpscaleTest
_TexturePackerUpscaleTest = _TexturePackerUpscaleTest
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TexturePackerUpscaleTest():
    """com.badlogic.gdx.tools.texturepacker.TexturePackerUpscaleTest"""
 
    @staticmethod
    def _wrap(java_value: _TexturePackerUpscaleTest) -> 'TexturePackerUpscaleTest':
        return TexturePackerUpscaleTest(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TexturePackerUpscaleTest):
        """
        Dynamic initializer for TexturePackerUpscaleTest.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TexturePackerUpscaleTest__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TexturePackerUpscaleTest__wrapper":
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

    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void com.badlogic.gdx.tools.texturepacker.TexturePackerUpscaleTest.main(java.lang.String[])"""
        _TexturePackerUpscaleTest.main(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.texturepacker.TexturePackerUpscaleTest()"""
        val = _TexturePackerUpscaleTest()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.texturepacker.TexturePackerUpscaleTest()"""
        val = _TexturePackerUpscaleTest()
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
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.tools.texturepacker.TexturePacker as _TexturePacker_Settings
_Settings = _TexturePacker_Settings.Settings
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Settings():
    """com.badlogic.gdx.tools.texturepacker.TexturePacker.Settings"""
 
    @staticmethod
    def _wrap(java_value: _Settings) -> 'Settings':
        return Settings(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Settings):
        """
        Dynamic initializer for Settings.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Settings__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Settings__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getScaledPackFileName(self, arg0: str, arg1: int) -> str:
        """public java.lang.String com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings.getScaledPackFileName(java.lang.String,int)"""
        return str._wrap(super(_Settings, self).getScaledPackFileName(arg0, _int.valueOf(arg1)))

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
    def set(self, arg0: 'Settings'):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings.set(com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings)"""
        super(_Settings, self).set(arg0)

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
    def __init__(self, ):
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings()"""
        val = _Settings()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Settings'):
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings(com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings)"""
        val = _Settings(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings()"""
        val = _Settings()
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
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.ImageProcessor
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.File as File
import com.badlogic.gdx.tools.texturepacker.TexturePacker as _TexturePacker_Settings
_Settings = _TexturePacker_Settings.Settings
from builtins import float
import com.badlogic.gdx.tools.texturepacker.ImageProcessor as _ImageProcessor
_ImageProcessor = _ImageProcessor
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.tools.texturepacker.TexturePacker as _TexturePacker_Rect
_Rect = _TexturePacker_Rect.Rect
import java.awt.image.BufferedImage as BufferedImage
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ImageProcessor():
    """com.badlogic.gdx.tools.texturepacker.ImageProcessor"""
 
    @staticmethod
    def _wrap(java_value: _ImageProcessor) -> 'ImageProcessor':
        return ImageProcessor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ImageProcessor):
        """
        Dynamic initializer for ImageProcessor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ImageProcessor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ImageProcessor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addImage(self, arg0: 'BufferedImage', arg1: str) -> 'Rect':
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect com.badlogic.gdx.tools.texturepacker.ImageProcessor.addImage(java.awt.image.BufferedImage,java.lang.String)"""
        return 'Rect'._wrap(super(_ImageProcessor, self).addImage(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.tools.texturepacker.ImageProcessor.clear()"""
        super(ImageProcessor, self).clear()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getSettings(self) -> 'Settings':
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings com.badlogic.gdx.tools.texturepacker.ImageProcessor.getSettings()"""
        return 'Settings'._wrap(super(ImageProcessor, self).getSettings())

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
    def addImage(self, arg0: 'File', arg1: str) -> 'Rect':
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect com.badlogic.gdx.tools.texturepacker.ImageProcessor.addImage(java.io.File,java.lang.String)"""
        return 'Rect'._wrap(super(_ImageProcessor, self).addImage(arg0, arg1))

    @overload
    def setResampling(self, arg0: 'Resampling'):
        """public void com.badlogic.gdx.tools.texturepacker.ImageProcessor.setResampling(com.badlogic.gdx.tools.texturepacker.TexturePacker$Resampling)"""
        super(_ImageProcessor, self).setResampling(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getScale(self) -> float:
        """public float com.badlogic.gdx.tools.texturepacker.ImageProcessor.getScale()"""
        return float._wrap(super(ImageProcessor, self).getScale())

    @overload
    def __init__(self, arg0: 'Settings'):
        """public com.badlogic.gdx.tools.texturepacker.ImageProcessor(com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings)"""
        val = _ImageProcessor(arg0)
        self.__wrapper = val

    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.tools.texturepacker.ImageProcessor.setScale(float)"""
        super(_ImageProcessor, self).setScale(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getImages(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect> com.badlogic.gdx.tools.texturepacker.ImageProcessor.getImages()"""
        return 'utils.Array'._wrap(super(ImageProcessor, self).getImages())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.TexturePackerFileProcessor
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.tools.texturepacker.TexturePacker as _TexturePacker_ProgressListener
_ProgressListener = _TexturePacker_ProgressListener.ProgressListener
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.File as File
try:
    from pygdx import tools
except ImportError:
    tools = _import_once("pygdx.tools")

import com.badlogic.gdx.tools.FileProcessor as _FileProcessor
_FileProcessor = _FileProcessor
import java.lang.String as _String
_String = _String
import java.util.ArrayList as _ArrayList
_ArrayList = _ArrayList
import java.lang.String as _string
import java.util.Comparator as Comparator
import java.util.ArrayList as ArrayList
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.io.FilenameFilter as FilenameFilter
import com.badlogic.gdx.tools.texturepacker.TexturePackerFileProcessor as _TexturePackerFileProcessor
_TexturePackerFileProcessor = _TexturePackerFileProcessor
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TexturePackerFileProcessor():
    """com.badlogic.gdx.tools.texturepacker.TexturePackerFileProcessor"""
 
    @staticmethod
    def _wrap(java_value: _TexturePackerFileProcessor) -> 'TexturePackerFileProcessor':
        return TexturePackerFileProcessor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TexturePackerFileProcessor):
        """
        Dynamic initializer for TexturePackerFileProcessor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TexturePackerFileProcessor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TexturePackerFileProcessor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addInputSuffix(self, *arg0: str) -> 'tools.FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.addInputSuffix(java.lang.String...)"""
        return 'tools.FileProcessor'._wrap(super(_tools.FileProcessor, self).addInputSuffix(arg0))

    @overload
    def addInputRegex(self, *arg0: str) -> 'tools.FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.addInputRegex(java.lang.String...)"""
        return 'tools.FileProcessor'._wrap(super(_tools.FileProcessor, self).addInputRegex(arg0))

    @overload
    def __init__(self, arg0: 'Settings', arg1: str, arg2: 'ProgressListener'):
        """public com.badlogic.gdx.tools.texturepacker.TexturePackerFileProcessor(com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings,java.lang.String,com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener)"""
        val = _TexturePackerFileProcessor(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def process(self, arg0: 'File', arg1: 'File') -> 'ArrayList':
        """public java.util.ArrayList<com.badlogic.gdx.tools.FileProcessor$Entry> com.badlogic.gdx.tools.texturepacker.TexturePackerFileProcessor.process(java.io.File,java.io.File) throws java.lang.Exception"""
        return 'ArrayList'._wrap(super(_TexturePackerFileProcessor, self).process(arg0, arg1))

    @overload
    def getProgressListener(self) -> 'ProgressListener':
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener com.badlogic.gdx.tools.texturepacker.TexturePackerFileProcessor.getProgressListener()"""
        return 'ProgressListener'._wrap(super(TexturePackerFileProcessor, self).getProgressListener())

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
    def process(self, arg0: str, arg1: str) -> 'ArrayList':
        """public java.util.ArrayList<com.badlogic.gdx.tools.FileProcessor$Entry> com.badlogic.gdx.tools.FileProcessor.process(java.lang.String,java.lang.String) throws java.lang.Exception"""
        return 'ArrayList'._wrap(super(_tools.FileProcessor, self).process(arg0, arg1))

    @overload
    def setRecursive(self, arg0: bool) -> 'tools.FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.setRecursive(boolean)"""
        return 'tools.FileProcessor'._wrap(super(_tools.FileProcessor, self).setRecursive(_boolean.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.texturepacker.TexturePackerFileProcessor()"""
        val = _TexturePackerFileProcessor()
        self.__wrapper = val

    @overload
    def setInputFilter(self, arg0: 'FilenameFilter') -> 'tools.FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.setInputFilter(java.io.FilenameFilter)"""
        return 'tools.FileProcessor'._wrap(super(_tools.FileProcessor, self).setInputFilter(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.texturepacker.TexturePackerFileProcessor()"""
        val = _TexturePackerFileProcessor()
        self.__wrapper = val

    @overload
    def setFlattenOutput(self, arg0: bool) -> 'tools.FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.setFlattenOutput(boolean)"""
        return 'tools.FileProcessor'._wrap(super(_tools.FileProcessor, self).setFlattenOutput(_boolean.valueOf(arg0)))

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
    def process(self, arg0: 'File', arg1: 'File') -> 'ArrayList':
        """public java.util.ArrayList<com.badlogic.gdx.tools.FileProcessor$Entry> com.badlogic.gdx.tools.texturepacker.TexturePackerFileProcessor.process(java.io.File[],java.io.File) throws java.lang.Exception"""
        return 'ArrayList'._wrap(super(_TexturePackerFileProcessor, self).process(arg0, arg1))

    @overload
    def setOutputSuffix(self, arg0: str) -> 'tools.FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.setOutputSuffix(java.lang.String)"""
        return 'tools.FileProcessor'._wrap(super(_tools.FileProcessor, self).setOutputSuffix(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setComparator(self, arg0: 'Comparator') -> 'tools.FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.setComparator(java.util.Comparator<java.io.File>)"""
        return 'tools.FileProcessor'._wrap(super(_tools.FileProcessor, self).setComparator(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.TexturePackerTest
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ApplicationAdapter as _ApplicationAdapter
_ApplicationAdapter = _ApplicationAdapter
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.tools.texturepacker.TexturePackerTest as _TexturePackerTest
_TexturePackerTest = _TexturePackerTest
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TexturePackerTest():
    """com.badlogic.gdx.tools.texturepacker.TexturePackerTest"""
 
    @staticmethod
    def _wrap(java_value: _TexturePackerTest) -> 'TexturePackerTest':
        return TexturePackerTest(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TexturePackerTest):
        """
        Dynamic initializer for TexturePackerTest.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TexturePackerTest__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TexturePackerTest__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void com.badlogic.gdx.tools.texturepacker.TexturePackerTest.main(java.lang.String[]) throws java.lang.Exception"""
        _TexturePackerTest.main(arg0)

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
    def create(self):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePackerTest.create()"""
        super(TexturePackerTest, self).create()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.ApplicationAdapter.dispose()"""
        super(pygdx.ApplicationAdapter, self).dispose()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def resume(self):
        """public void com.badlogic.gdx.ApplicationAdapter.resume()"""
        super(pygdx.ApplicationAdapter, self).resume()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.texturepacker.TexturePackerTest()"""
        val = _TexturePackerTest()
        self.__wrapper = val

    @override
    @overload
    def render(self):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePackerTest.render()"""
        super(TexturePackerTest, self).render()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.texturepacker.TexturePackerTest()"""
        val = _TexturePackerTest()
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePackerTest.resize(int,int)"""
        super(_TexturePackerTest, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def pause(self):
        """public void com.badlogic.gdx.ApplicationAdapter.pause()"""
        super(pygdx.ApplicationAdapter, self).pause()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.MaxRectsPacker$FreeRectChoiceHeuristic
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.tools.texturepacker.MaxRectsPacker as _MaxRectsPacker_FreeRectChoiceHeuristic
_FreeRectChoiceHeuristic = _MaxRectsPacker_FreeRectChoiceHeuristic.FreeRectChoiceHeuristic
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FreeRectChoiceHeuristic():
    """com.badlogic.gdx.tools.texturepacker.MaxRectsPacker.FreeRectChoiceHeuristic"""
 
    @staticmethod
    def _wrap(java_value: _FreeRectChoiceHeuristic) -> 'FreeRectChoiceHeuristic':
        return FreeRectChoiceHeuristic(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FreeRectChoiceHeuristic):
        """
        Dynamic initializer for FreeRectChoiceHeuristic.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FreeRectChoiceHeuristic__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FreeRectChoiceHeuristic__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'FreeRectChoiceHeuristic':
        """public static com.badlogic.gdx.tools.texturepacker.MaxRectsPacker$FreeRectChoiceHeuristic com.badlogic.gdx.tools.texturepacker.MaxRectsPacker$FreeRectChoiceHeuristic.valueOf(java.lang.String)"""
        return FreeRectChoiceHeuristic._wrap(_FreeRectChoiceHeuristic.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def values() -> List['FreeRectChoiceHeuristic']:
        """public static com.badlogic.gdx.tools.texturepacker.MaxRectsPacker$FreeRectChoiceHeuristic[] com.badlogic.gdx.tools.texturepacker.MaxRectsPacker$FreeRectChoiceHeuristic.values()"""
        return List[FreeRectChoiceHeuristic]._wrap(_FreeRectChoiceHeuristic.values())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.File as File
import java.awt.image.BufferedImage as _BufferedImage
_BufferedImage = _BufferedImage
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.tools.texturepacker.TexturePacker as _TexturePacker_Rect
_Rect = _TexturePacker_Rect.Rect
import java.awt.image.BufferedImage as BufferedImage
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Rect():
    """com.badlogic.gdx.tools.texturepacker.TexturePacker.Rect"""
 
    @staticmethod
    def _wrap(java_value: _Rect) -> 'Rect':
        return Rect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Rect):
        """
        Dynamic initializer for Rect.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Rect__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Rect__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect.toString()"""
        return str._wrap(super(Rect, self).toString())

    @overload
    def unloadImage(self, arg0: 'File'):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect.unloadImage(java.io.File)"""
        super(_Rect, self).unloadImage(arg0)

    @overload
    def __init__(self, arg0: 'BufferedImage', arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool):
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect(java.awt.image.BufferedImage,int,int,int,int,boolean)"""
        val = _Rect(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _boolean.valueOf(arg5))
        self.__wrapper = val

    @staticmethod
    @overload
    def getAtlasName(arg0: str, arg1: bool) -> str:
        """public static java.lang.String com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect.getAtlasName(java.lang.String,boolean)"""
        return str._wrap(_Rect.getAtlasName(arg0, _boolean.valueOf(arg1)))

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
    def compareTo(self, arg0: 'Rect') -> int:
        """public int com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect.compareTo(com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect)"""
        return int._wrap(super(_Rect, self).compareTo(arg0))

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getImage(self, arg0: 'ImageProcessor') -> 'BufferedImage':
        """public java.awt.image.BufferedImage com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect.getImage(com.badlogic.gdx.tools.texturepacker.ImageProcessor)"""
        return 'BufferedImage'._wrap(super(_Rect, self).getImage(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect.equals(java.lang.Object)"""
        return bool._wrap(super(_Rect, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())