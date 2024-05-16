from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.escape.Escapers as __Escapers_Builder
__Builder = __Escapers_Builder.Builder
import com.google.common.escape.Escapers as __Escapers
__Escapers = __Escapers
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.google.common.escape.Escaper as __Escaper
__Escaper = __Escaper
from builtins import int
 
class Escapers():
    """com.google.common.escape.Escapers"""
 
    @staticmethod
    def __wrap(java_value: __Escapers) -> 'Escapers':
        return Escapers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Escapers):
        """
        Dynamic initializer for Escapers.
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

    @staticmethod
    @overload
    def computeReplacement(escaper: 'UnicodeEscaper', cp: int) -> str:
        """public static java.lang.String com.google.common.escape.Escapers.computeReplacement(com.google.common.escape.UnicodeEscaper,int)"""
        return str.__wrap(__Escapers.computeReplacement(escaper, __int.valueOf(cp)))

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

    @staticmethod
    @overload
    def computeReplacement(escaper: 'CharEscaper', c: str) -> str:
        """public static java.lang.String com.google.common.escape.Escapers.computeReplacement(com.google.common.escape.CharEscaper,char)"""
        return str.__wrap(__Escapers.computeReplacement(escaper, __char.valueOf(c)))

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def builder() -> 'Builder':
        """public static com.google.common.escape.Escapers$Builder com.google.common.escape.Escapers.builder()"""
        return Builder.__wrap(__Escapers.builder())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nullEscaper() -> 'Escaper':
        """public static com.google.common.escape.Escaper com.google.common.escape.Escapers.nullEscaper()"""
        return Escaper.__wrap(__Escapers.nullEscaper())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.google.common.escape.Escapers
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.escape.Escapers as __Escapers_Builder
__Builder = __Escapers_Builder.Builder
import com.google.common.escape.Escapers as __Escapers
__Escapers = __Escapers
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.google.common.escape.Escaper as __Escaper
__Escaper = __Escaper
from builtins import int
 
class Escapers():
    """com.google.common.escape.Escapers"""
 
    @staticmethod
    def __wrap(java_value: __Escapers) -> 'Escapers':
        return Escapers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Escapers):
        """
        Dynamic initializer for Escapers.
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

    @staticmethod
    @overload
    def computeReplacement(escaper: 'UnicodeEscaper', cp: int) -> str:
        """public static java.lang.String com.google.common.escape.Escapers.computeReplacement(com.google.common.escape.UnicodeEscaper,int)"""
        return str.__wrap(__Escapers.computeReplacement(escaper, __int.valueOf(cp)))

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

    @staticmethod
    @overload
    def computeReplacement(escaper: 'CharEscaper', c: str) -> str:
        """public static java.lang.String com.google.common.escape.Escapers.computeReplacement(com.google.common.escape.CharEscaper,char)"""
        return str.__wrap(__Escapers.computeReplacement(escaper, __char.valueOf(c)))

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def builder() -> 'Builder':
        """public static com.google.common.escape.Escapers$Builder com.google.common.escape.Escapers.builder()"""
        return Builder.__wrap(__Escapers.builder())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nullEscaper() -> 'Escaper':
        """public static com.google.common.escape.Escaper com.google.common.escape.Escapers.nullEscaper()"""
        return Escaper.__wrap(__Escapers.nullEscaper())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.google.common.escape.Escapers 
 
 
# CLASS: com.google.common.escape.ArrayBasedCharEscaper
from pyquantum_helper import import_once as __import_once__
try:
    from pygcommon import base
except ImportError:
    base = __import_once__("pygcommon.base")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.escape.ArrayBasedCharEscaper as __ArrayBasedCharEscaper
__ArrayBasedCharEscaper = __ArrayBasedCharEscaper
import com.google.common.base.Function as __Function
__Function = __Function
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.google.common.escape.Escaper as __Escaper
__Escaper = __Escaper
from builtins import int
 
class ArrayBasedCharEscaper(ABC):
    """com.google.common.escape.ArrayBasedCharEscaper"""
 
    @staticmethod
    def __wrap(java_value: __ArrayBasedCharEscaper) -> 'ArrayBasedCharEscaper':
        return ArrayBasedCharEscaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ArrayBasedCharEscaper):
        """
        Dynamic initializer for ArrayBasedCharEscaper.
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
    def asFunction(self) -> 'base.Function':
        """public final com.google.common.base.Function<java.lang.String, java.lang.String> com.google.common.escape.Escaper.asFunction()"""
        return 'base.Function'.__wrap(super(Escaper, self).asFunction())

    @overload
    def escape(self, s: str) -> str:
        """public final java.lang.String com.google.common.escape.ArrayBasedCharEscaper.escape(java.lang.String)"""
        return str.__wrap(super(__ArrayBasedCharEscaper, self).escape(s))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.common.escape.CharEscaperBuilder
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.escape.CharEscaperBuilder as __CharEscaperBuilder
__CharEscaperBuilder = __CharEscaperBuilder
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.google.common.escape.Escaper as __Escaper
__Escaper = __Escaper
from builtins import int
 
class CharEscaperBuilder():
    """com.google.common.escape.CharEscaperBuilder"""
 
    @staticmethod
    def __wrap(java_value: __CharEscaperBuilder) -> 'CharEscaperBuilder':
        return CharEscaperBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CharEscaperBuilder):
        """
        Dynamic initializer for CharEscaperBuilder.
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
    def __init__(self, ):
        """public com.google.common.escape.CharEscaperBuilder()"""
        val = __CharEscaperBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def toEscaper(self) -> 'Escaper':
        """public com.google.common.escape.Escaper com.google.common.escape.CharEscaperBuilder.toEscaper()"""
        return 'Escaper'.__wrap(super(CharEscaperBuilder, self).toEscaper())

    @overload
    def addEscapes(self, cs: 'char', r: str) -> 'CharEscaperBuilder':
        """public com.google.common.escape.CharEscaperBuilder com.google.common.escape.CharEscaperBuilder.addEscapes(char[],java.lang.String)"""
        return 'CharEscaperBuilder'.__wrap(super(__CharEscaperBuilder, self).addEscapes(cs, r))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def addEscape(self, c: str, r: str) -> 'CharEscaperBuilder':
        """public com.google.common.escape.CharEscaperBuilder com.google.common.escape.CharEscaperBuilder.addEscape(char,java.lang.String)"""
        return 'CharEscaperBuilder'.__wrap(super(__CharEscaperBuilder, self).addEscape(__char.valueOf(c), r))

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.google.common.escape.CharEscaperBuilder()"""
        val = __CharEscaperBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def toArray(self) -> List[List[str]]:
        """public char[][] com.google.common.escape.CharEscaperBuilder.toArray()"""
        return List[List[str]].__wrap(super(CharEscaperBuilder, self).toArray()) 
 
 
# CLASS: com.google.common.escape.ArrayBasedEscaperMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.google.common.escape.ArrayBasedEscaperMap as __ArrayBasedEscaperMap
__ArrayBasedEscaperMap = __ArrayBasedEscaperMap
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class ArrayBasedEscaperMap():
    """com.google.common.escape.ArrayBasedEscaperMap"""
 
    @staticmethod
    def __wrap(java_value: __ArrayBasedEscaperMap) -> 'ArrayBasedEscaperMap':
        return ArrayBasedEscaperMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ArrayBasedEscaperMap):
        """
        Dynamic initializer for ArrayBasedEscaperMap.
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

    @staticmethod
    @overload
    def create(replacements: 'Map') -> 'ArrayBasedEscaperMap':
        """public static com.google.common.escape.ArrayBasedEscaperMap com.google.common.escape.ArrayBasedEscaperMap.create(java.util.Map<java.lang.Character, java.lang.String>)"""
        return ArrayBasedEscaperMap.__wrap(__ArrayBasedEscaperMap.create(replacements))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.common.escape.UnicodeEscaper
from pyquantum_helper import import_once as __import_once__
try:
    from pygcommon import base
except ImportError:
    base = __import_once__("pygcommon.base")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.base.Function as __Function
__Function = __Function
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.escape.UnicodeEscaper as __UnicodeEscaper
__UnicodeEscaper = __UnicodeEscaper
import java.lang.Integer as __int
from builtins import bool
import com.google.common.escape.Escaper as __Escaper
__Escaper = __Escaper
from builtins import int
 
class UnicodeEscaper(ABC):
    """com.google.common.escape.UnicodeEscaper"""
 
    @staticmethod
    def __wrap(java_value: __UnicodeEscaper) -> 'UnicodeEscaper':
        return UnicodeEscaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnicodeEscaper):
        """
        Dynamic initializer for UnicodeEscaper.
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
    def asFunction(self) -> 'base.Function':
        """public final com.google.common.base.Function<java.lang.String, java.lang.String> com.google.common.escape.Escaper.asFunction()"""
        return 'base.Function'.__wrap(super(Escaper, self).asFunction())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def escape(self, string: str) -> str:
        """public java.lang.String com.google.common.escape.UnicodeEscaper.escape(java.lang.String)"""
        return str.__wrap(super(__UnicodeEscaper, self).escape(string)) 
 
 
# CLASS: com.google.common.escape.ArrayBasedUnicodeEscaper
from pyquantum_helper import import_once as __import_once__
try:
    from pygcommon import base
except ImportError:
    base = __import_once__("pygcommon.base")

import com.google.common.escape.ArrayBasedUnicodeEscaper as __ArrayBasedUnicodeEscaper
__ArrayBasedUnicodeEscaper = __ArrayBasedUnicodeEscaper
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.base.Function as __Function
__Function = __Function
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.google.common.escape.Escaper as __Escaper
__Escaper = __Escaper
from builtins import int
 
class ArrayBasedUnicodeEscaper(ABC):
    """com.google.common.escape.ArrayBasedUnicodeEscaper"""
 
    @staticmethod
    def __wrap(java_value: __ArrayBasedUnicodeEscaper) -> 'ArrayBasedUnicodeEscaper':
        return ArrayBasedUnicodeEscaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ArrayBasedUnicodeEscaper):
        """
        Dynamic initializer for ArrayBasedUnicodeEscaper.
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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def escape(self, s: str) -> str:
        """public final java.lang.String com.google.common.escape.ArrayBasedUnicodeEscaper.escape(java.lang.String)"""
        return str.__wrap(super(__ArrayBasedUnicodeEscaper, self).escape(s))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def asFunction(self) -> 'base.Function':
        """public final com.google.common.base.Function<java.lang.String, java.lang.String> com.google.common.escape.Escaper.asFunction()"""
        return 'base.Function'.__wrap(super(Escaper, self).asFunction())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.common.escape.CharEscaper
from pyquantum_helper import import_once as __import_once__
try:
    from pygcommon import base
except ImportError:
    base = __import_once__("pygcommon.base")

from builtins import str
import com.google.common.escape.CharEscaper as __CharEscaper
__CharEscaper = __CharEscaper
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.base.Function as __Function
__Function = __Function
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.google.common.escape.Escaper as __Escaper
__Escaper = __Escaper
from builtins import int
 
class CharEscaper(ABC):
    """com.google.common.escape.CharEscaper"""
 
    @staticmethod
    def __wrap(java_value: __CharEscaper) -> 'CharEscaper':
        return CharEscaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CharEscaper):
        """
        Dynamic initializer for CharEscaper.
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
    def escape(self, string: str) -> str:
        """public java.lang.String com.google.common.escape.CharEscaper.escape(java.lang.String)"""
        return str.__wrap(super(__CharEscaper, self).escape(string))

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

    @override
    @overload
    def asFunction(self) -> 'base.Function':
        """public final com.google.common.base.Function<java.lang.String, java.lang.String> com.google.common.escape.Escaper.asFunction()"""
        return 'base.Function'.__wrap(super(Escaper, self).asFunction())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.common.escape.Escapers$Builder
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.escape.Escapers as __Escapers_Builder
__Builder = __Escapers_Builder.Builder
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.google.common.escape.Escaper as __Escaper
__Escaper = __Escaper
from builtins import int
 
class Builder():
    """com.google.common.escape.Escapers.Builder"""
 
    @staticmethod
    def __wrap(java_value: __Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Builder):
        """
        Dynamic initializer for Builder.
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
    def addEscape(self, c: str, replacement: str) -> 'Builder':
        """public com.google.common.escape.Escapers$Builder com.google.common.escape.Escapers$Builder.addEscape(char,java.lang.String)"""
        return 'Builder'.__wrap(super(__Builder, self).addEscape(__char.valueOf(c), replacement))

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
    def build(self) -> 'Escaper':
        """public com.google.common.escape.Escaper com.google.common.escape.Escapers$Builder.build()"""
        return 'Escaper'.__wrap(super(Builder, self).build())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setSafeRange(self, safeMin: str, safeMax: str) -> 'Builder':
        """public com.google.common.escape.Escapers$Builder com.google.common.escape.Escapers$Builder.setSafeRange(char,char)"""
        return 'Builder'.__wrap(super(__Builder, self).setSafeRange(__char.valueOf(safeMin), __char.valueOf(safeMax)))

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
    def setUnsafeReplacement(self, unsafeReplacement: str) -> 'Builder':
        """public com.google.common.escape.Escapers$Builder com.google.common.escape.Escapers$Builder.setUnsafeReplacement(java.lang.String)"""
        return 'Builder'.__wrap(super(__Builder, self).setUnsafeReplacement(unsafeReplacement)) 
 
 
# CLASS: com.google.common.escape.Escaper
from pyquantum_helper import import_once as __import_once__
try:
    from pygcommon import base
except ImportError:
    base = __import_once__("pygcommon.base")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.base.Function as __Function
__Function = __Function
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.google.common.escape.Escaper as __Escaper
__Escaper = __Escaper
from builtins import int
 
class Escaper(ABC):
    """com.google.common.escape.Escaper"""
 
    @staticmethod
    def __wrap(java_value: __Escaper) -> 'Escaper':
        return Escaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Escaper):
        """
        Dynamic initializer for Escaper.
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

    @overload
    def asFunction(self) -> 'base.Function':
        """public final com.google.common.base.Function<java.lang.String, java.lang.String> com.google.common.escape.Escaper.asFunction()"""
        return 'base.Function'.__wrap(super(Escaper, self).asFunction())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))