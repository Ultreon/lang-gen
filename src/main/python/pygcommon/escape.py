from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.google.common.escape.ArrayBasedEscaperMap as _ArrayBasedEscaperMap
_ArrayBasedEscaperMap = _ArrayBasedEscaperMap
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ArrayBasedEscaperMap():
    """com.google.common.escape.ArrayBasedEscaperMap"""
 
    @staticmethod
    def _wrap(java_value: _ArrayBasedEscaperMap) -> 'ArrayBasedEscaperMap':
        return ArrayBasedEscaperMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ArrayBasedEscaperMap):
        """
        Dynamic initializer for ArrayBasedEscaperMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ArrayBasedEscaperMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ArrayBasedEscaperMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def create(replacements: 'Map') -> 'ArrayBasedEscaperMap':
        """public static com.google.common.escape.ArrayBasedEscaperMap com.google.common.escape.ArrayBasedEscaperMap.create(java.util.Map<java.lang.Character, java.lang.String>)"""
        return ArrayBasedEscaperMap._wrap(_ArrayBasedEscaperMap.create(replacements))

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

 
 
 
# CLASS: com.google.common.escape.ArrayBasedEscaperMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.google.common.escape.ArrayBasedEscaperMap as _ArrayBasedEscaperMap
_ArrayBasedEscaperMap = _ArrayBasedEscaperMap
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ArrayBasedEscaperMap():
    """com.google.common.escape.ArrayBasedEscaperMap"""
 
    @staticmethod
    def _wrap(java_value: _ArrayBasedEscaperMap) -> 'ArrayBasedEscaperMap':
        return ArrayBasedEscaperMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ArrayBasedEscaperMap):
        """
        Dynamic initializer for ArrayBasedEscaperMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ArrayBasedEscaperMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ArrayBasedEscaperMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def create(replacements: 'Map') -> 'ArrayBasedEscaperMap':
        """public static com.google.common.escape.ArrayBasedEscaperMap com.google.common.escape.ArrayBasedEscaperMap.create(java.util.Map<java.lang.Character, java.lang.String>)"""
        return ArrayBasedEscaperMap._wrap(_ArrayBasedEscaperMap.create(replacements))

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

 
 
 
# CLASS: com.google.common.escape.ArrayBasedEscaperMap 
 
 
# CLASS: com.google.common.escape.CharEscaper
from pyquantum_helper import import_once as _import_once
try:
    from pygcommon import base
except ImportError:
    base = _import_once("pygcommon.base")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import com.google.common.base.Function as _Function
_Function = _Function
import com.google.common.escape.Escaper as _Escaper
_Escaper = _Escaper
import java.lang.Integer as _int
import com.google.common.escape.CharEscaper as _CharEscaper
_CharEscaper = _CharEscaper
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CharEscaper():
    """com.google.common.escape.CharEscaper"""
 
    @staticmethod
    def _wrap(java_value: _CharEscaper) -> 'CharEscaper':
        return CharEscaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CharEscaper):
        """
        Dynamic initializer for CharEscaper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CharEscaper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CharEscaper__wrapper":
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
    def asFunction(self) -> 'base.Function':
        """public final com.google.common.base.Function<java.lang.String, java.lang.String> com.google.common.escape.Escaper.asFunction()"""
        return 'base.Function'._wrap(super(Escaper, self).asFunction())

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

    @overload
    def escape(self, string: str) -> str:
        """public java.lang.String com.google.common.escape.CharEscaper.escape(java.lang.String)"""
        return str._wrap(super(_CharEscaper, self).escape(string))

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
 
 
# CLASS: com.google.common.escape.Escaper
from pyquantum_helper import import_once as _import_once
try:
    from pygcommon import base
except ImportError:
    base = _import_once("pygcommon.base")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import com.google.common.escape.Escaper as _Escaper
_Escaper = _Escaper
import com.google.common.base.Function as _Function
_Function = _Function
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Escaper():
    """com.google.common.escape.Escaper"""
 
    @staticmethod
    def _wrap(java_value: _Escaper) -> 'Escaper':
        return Escaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Escaper):
        """
        Dynamic initializer for Escaper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Escaper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Escaper__wrapper":
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
    def asFunction(self) -> 'base.Function':
        """public final com.google.common.base.Function<java.lang.String, java.lang.String> com.google.common.escape.Escaper.asFunction()"""
        return 'base.Function'._wrap(super(Escaper, self).asFunction())

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

    @abstractmethod
    def escape(self, string: str):
        """public abstract java.lang.String com.google.common.escape.Escaper.escape(java.lang.String)"""
        pass

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
 
 
# CLASS: com.google.common.escape.ArrayBasedCharEscaper
from pyquantum_helper import import_once as _import_once
try:
    from pygcommon import base
except ImportError:
    base = _import_once("pygcommon.base")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import com.google.common.base.Function as _Function
_Function = _Function
import com.google.common.escape.Escaper as _Escaper
_Escaper = _Escaper
import java.lang.Integer as _int
from builtins import bool
import com.google.common.escape.ArrayBasedCharEscaper as _ArrayBasedCharEscaper
_ArrayBasedCharEscaper = _ArrayBasedCharEscaper
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ArrayBasedCharEscaper():
    """com.google.common.escape.ArrayBasedCharEscaper"""
 
    @staticmethod
    def _wrap(java_value: _ArrayBasedCharEscaper) -> 'ArrayBasedCharEscaper':
        return ArrayBasedCharEscaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ArrayBasedCharEscaper):
        """
        Dynamic initializer for ArrayBasedCharEscaper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ArrayBasedCharEscaper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ArrayBasedCharEscaper__wrapper":
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
    def asFunction(self) -> 'base.Function':
        """public final com.google.common.base.Function<java.lang.String, java.lang.String> com.google.common.escape.Escaper.asFunction()"""
        return 'base.Function'._wrap(super(Escaper, self).asFunction())

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

    @overload
    def escape(self, s: str) -> str:
        """public final java.lang.String com.google.common.escape.ArrayBasedCharEscaper.escape(java.lang.String)"""
        return str._wrap(super(_ArrayBasedCharEscaper, self).escape(s))

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
 
 
# CLASS: com.google.common.escape.CharEscaperBuilder
from builtins import str
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.String as _string
import com.google.common.escape.Escaper as _Escaper
_Escaper = _Escaper
import java.lang.Integer as _int
import com.google.common.escape.CharEscaperBuilder as _CharEscaperBuilder
_CharEscaperBuilder = _CharEscaperBuilder
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CharEscaperBuilder():
    """com.google.common.escape.CharEscaperBuilder"""
 
    @staticmethod
    def _wrap(java_value: _CharEscaperBuilder) -> 'CharEscaperBuilder':
        return CharEscaperBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CharEscaperBuilder):
        """
        Dynamic initializer for CharEscaperBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CharEscaperBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CharEscaperBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.google.common.escape.CharEscaperBuilder()"""
        val = _CharEscaperBuilder()
        self.__wrapper = val

    @overload
    def toEscaper(self) -> 'Escaper':
        """public com.google.common.escape.Escaper com.google.common.escape.CharEscaperBuilder.toEscaper()"""
        return 'Escaper'._wrap(super(CharEscaperBuilder, self).toEscaper())

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
    def addEscape(self, c: str, r: str) -> 'CharEscaperBuilder':
        """public com.google.common.escape.CharEscaperBuilder com.google.common.escape.CharEscaperBuilder.addEscape(char,java.lang.String)"""
        return 'CharEscaperBuilder'._wrap(super(_CharEscaperBuilder, self).addEscape(_char.valueOf(c), r))

    @overload
    def addEscapes(self, cs: 'char', r: str) -> 'CharEscaperBuilder':
        """public com.google.common.escape.CharEscaperBuilder com.google.common.escape.CharEscaperBuilder.addEscapes(char[],java.lang.String)"""
        return 'CharEscaperBuilder'._wrap(super(_CharEscaperBuilder, self).addEscapes(cs, r))

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
    def toArray(self) -> List[List[str]]:
        """public char[][] com.google.common.escape.CharEscaperBuilder.toArray()"""
        return List[List[str]]._wrap(super(CharEscaperBuilder, self).toArray())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.google.common.escape.CharEscaperBuilder()"""
        val = _CharEscaperBuilder()
        self.__wrapper = val

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
 
 
# CLASS: com.google.common.escape.ArrayBasedUnicodeEscaper
from pyquantum_helper import import_once as _import_once
try:
    from pygcommon import base
except ImportError:
    base = _import_once("pygcommon.base")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.google.common.escape.ArrayBasedUnicodeEscaper as _ArrayBasedUnicodeEscaper
_ArrayBasedUnicodeEscaper = _ArrayBasedUnicodeEscaper
import java.lang.String as _string
import com.google.common.base.Function as _Function
_Function = _Function
import com.google.common.escape.Escaper as _Escaper
_Escaper = _Escaper
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ArrayBasedUnicodeEscaper():
    """com.google.common.escape.ArrayBasedUnicodeEscaper"""
 
    @staticmethod
    def _wrap(java_value: _ArrayBasedUnicodeEscaper) -> 'ArrayBasedUnicodeEscaper':
        return ArrayBasedUnicodeEscaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ArrayBasedUnicodeEscaper):
        """
        Dynamic initializer for ArrayBasedUnicodeEscaper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ArrayBasedUnicodeEscaper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ArrayBasedUnicodeEscaper__wrapper":
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
    def asFunction(self) -> 'base.Function':
        """public final com.google.common.base.Function<java.lang.String, java.lang.String> com.google.common.escape.Escaper.asFunction()"""
        return 'base.Function'._wrap(super(Escaper, self).asFunction())

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
    def escape(self, s: str) -> str:
        """public final java.lang.String com.google.common.escape.ArrayBasedUnicodeEscaper.escape(java.lang.String)"""
        return str._wrap(super(_ArrayBasedUnicodeEscaper, self).escape(s))

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
 
 
# CLASS: com.google.common.escape.Escapers
from builtins import str
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.google.common.escape.Escapers as _Escapers
_Escapers = _Escapers
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.google.common.escape.Escapers as _Escapers_Builder
_Builder = _Escapers_Builder.Builder
import com.google.common.escape.Escaper as _Escaper
_Escaper = _Escaper
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Escapers():
    """com.google.common.escape.Escapers"""
 
    @staticmethod
    def _wrap(java_value: _Escapers) -> 'Escapers':
        return Escapers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Escapers):
        """
        Dynamic initializer for Escapers.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Escapers__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Escapers__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def builder() -> 'Builder':
        """public static com.google.common.escape.Escapers$Builder com.google.common.escape.Escapers.builder()"""
        return Builder._wrap(_Escapers.builder())

    @staticmethod
    @overload
    def nullEscaper() -> 'Escaper':
        """public static com.google.common.escape.Escaper com.google.common.escape.Escapers.nullEscaper()"""
        return Escaper._wrap(_Escapers.nullEscaper())

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

    @staticmethod
    @overload
    def computeReplacement(escaper: 'UnicodeEscaper', cp: int) -> str:
        """public static java.lang.String com.google.common.escape.Escapers.computeReplacement(com.google.common.escape.UnicodeEscaper,int)"""
        return str._wrap(_Escapers.computeReplacement(escaper, _int.valueOf(cp)))

    @staticmethod
    @overload
    def computeReplacement(escaper: 'CharEscaper', c: str) -> str:
        """public static java.lang.String com.google.common.escape.Escapers.computeReplacement(com.google.common.escape.CharEscaper,char)"""
        return str._wrap(_Escapers.computeReplacement(escaper, _char.valueOf(c)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.escape.UnicodeEscaper
from pyquantum_helper import import_once as _import_once
try:
    from pygcommon import base
except ImportError:
    base = _import_once("pygcommon.base")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import com.google.common.base.Function as _Function
_Function = _Function
import com.google.common.escape.Escaper as _Escaper
_Escaper = _Escaper
import java.lang.Integer as _int
import com.google.common.escape.UnicodeEscaper as _UnicodeEscaper
_UnicodeEscaper = _UnicodeEscaper
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnicodeEscaper():
    """com.google.common.escape.UnicodeEscaper"""
 
    @staticmethod
    def _wrap(java_value: _UnicodeEscaper) -> 'UnicodeEscaper':
        return UnicodeEscaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnicodeEscaper):
        """
        Dynamic initializer for UnicodeEscaper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnicodeEscaper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnicodeEscaper__wrapper":
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
    def asFunction(self) -> 'base.Function':
        """public final com.google.common.base.Function<java.lang.String, java.lang.String> com.google.common.escape.Escaper.asFunction()"""
        return 'base.Function'._wrap(super(Escaper, self).asFunction())

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
    def escape(self, string: str) -> str:
        """public java.lang.String com.google.common.escape.UnicodeEscaper.escape(java.lang.String)"""
        return str._wrap(super(_UnicodeEscaper, self).escape(string))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.escape.Escapers$Builder
from builtins import str
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import com.google.common.escape.Escapers as _Escapers_Builder
_Builder = _Escapers_Builder.Builder
import com.google.common.escape.Escaper as _Escaper
_Escaper = _Escaper
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Builder():
    """com.google.common.escape.Escapers.Builder"""
 
    @staticmethod
    def _wrap(java_value: _Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Builder):
        """
        Dynamic initializer for Builder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Builder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Builder__wrapper":
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
    def setUnsafeReplacement(self, unsafeReplacement: str) -> 'Builder':
        """public com.google.common.escape.Escapers$Builder com.google.common.escape.Escapers$Builder.setUnsafeReplacement(java.lang.String)"""
        return 'Builder'._wrap(super(_Builder, self).setUnsafeReplacement(unsafeReplacement))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def addEscape(self, c: str, replacement: str) -> 'Builder':
        """public com.google.common.escape.Escapers$Builder com.google.common.escape.Escapers$Builder.addEscape(char,java.lang.String)"""
        return 'Builder'._wrap(super(_Builder, self).addEscape(_char.valueOf(c), replacement))

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

    @overload
    def build(self) -> 'Escaper':
        """public com.google.common.escape.Escaper com.google.common.escape.Escapers$Builder.build()"""
        return 'Escaper'._wrap(super(Builder, self).build())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setSafeRange(self, safeMin: str, safeMax: str) -> 'Builder':
        """public com.google.common.escape.Escapers$Builder com.google.common.escape.Escapers$Builder.setSafeRange(char,char)"""
        return 'Builder'._wrap(super(_Builder, self).setSafeRange(_char.valueOf(safeMin), _char.valueOf(safeMax)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())