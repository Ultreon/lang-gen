from __future__ import annotations
from overload import overload


 
import java.lang.Thread as Thread
import java.util.function.Predicate as Predicate
from builtins import str
import java.lang.Thread as _Thread
_Thread = _Thread
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.ThreadGroup as _ThreadGroup
_ThreadGroup = _ThreadGroup
import java.lang.Object as _object
from builtins import type
import java.time.Duration as Duration
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.lang.ThreadGroup as ThreadGroup
from builtins import bool
import java.lang.Long as _long
import org.apache.commons.lang3.ThreadUtils as _ThreadUtils
_ThreadUtils = _ThreadUtils
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ThreadUtils():
    """org.apache.commons.lang3.ThreadUtils"""
 
    @staticmethod
    def _wrap(java_value: _ThreadUtils) -> 'ThreadUtils':
        return ThreadUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ThreadUtils):
        """
        Dynamic initializer for ThreadUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ThreadUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ThreadUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def findThreadById(arg0: int, arg1: 'ThreadGroup') -> 'Thread':
        """public static java.lang.Thread org.apache.commons.lang3.ThreadUtils.findThreadById(long,java.lang.ThreadGroup)"""
        return Thread._wrap(_ThreadUtils.findThreadById(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def findThreads(arg0: 'Predicate') -> 'Collection':
        """public static java.util.Collection<java.lang.Thread> org.apache.commons.lang3.ThreadUtils.findThreads(java.util.function.Predicate<java.lang.Thread>)"""
        return Collection._wrap(_ThreadUtils.findThreads(arg0))

    @staticmethod
    @overload
    def findThreadById(arg0: int, arg1: str) -> 'Thread':
        """public static java.lang.Thread org.apache.commons.lang3.ThreadUtils.findThreadById(long,java.lang.String)"""
        return Thread._wrap(_ThreadUtils.findThreadById(_long.valueOf(arg0), arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def sleepQuietly(arg0: 'Duration'):
        """public static void org.apache.commons.lang3.ThreadUtils.sleepQuietly(java.time.Duration)"""
        _ThreadUtils.sleepQuietly(arg0)

    @staticmethod
    @overload
    def findThreadGroups(arg0: 'Predicate') -> 'Collection':
        """public static java.util.Collection<java.lang.ThreadGroup> org.apache.commons.lang3.ThreadUtils.findThreadGroups(java.util.function.Predicate<java.lang.ThreadGroup>)"""
        return Collection._wrap(_ThreadUtils.findThreadGroups(arg0))

    @staticmethod
    @overload
    def findThreads(arg0: 'ThreadGroup', arg1: bool, arg2: 'Predicate') -> 'Collection':
        """public static java.util.Collection<java.lang.Thread> org.apache.commons.lang3.ThreadUtils.findThreads(java.lang.ThreadGroup,boolean,java.util.function.Predicate<java.lang.Thread>)"""
        return Collection._wrap(_ThreadUtils.findThreads(arg0, _boolean.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def findThreadsByName(arg0: str, arg1: str) -> 'Collection':
        """public static java.util.Collection<java.lang.Thread> org.apache.commons.lang3.ThreadUtils.findThreadsByName(java.lang.String,java.lang.String)"""
        return Collection._wrap(_ThreadUtils.findThreadsByName(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def getAllThreadGroups() -> 'Collection':
        """public static java.util.Collection<java.lang.ThreadGroup> org.apache.commons.lang3.ThreadUtils.getAllThreadGroups()"""
        return Collection._wrap(_ThreadUtils.getAllThreadGroups())

    @staticmethod
    @overload
    def findThreads(arg0: 'ThreadGroup', arg1: bool, arg2: 'ThreadPredicate') -> 'Collection':
        """public static java.util.Collection<java.lang.Thread> org.apache.commons.lang3.ThreadUtils.findThreads(java.lang.ThreadGroup,boolean,org.apache.commons.lang3.ThreadUtils$ThreadPredicate)"""
        return Collection._wrap(_ThreadUtils.findThreads(arg0, _boolean.valueOf(arg1), arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def join(arg0: 'Thread', arg1: 'Duration'):
        """public static void org.apache.commons.lang3.ThreadUtils.join(java.lang.Thread,java.time.Duration) throws java.lang.InterruptedException"""
        _ThreadUtils.join(arg0, arg1)

    @staticmethod
    @overload
    def getSystemThreadGroup() -> 'ThreadGroup':
        """public static java.lang.ThreadGroup org.apache.commons.lang3.ThreadUtils.getSystemThreadGroup()"""
        return ThreadGroup._wrap(_ThreadUtils.getSystemThreadGroup())

    @staticmethod
    @overload
    def findThreadGroups(arg0: 'ThreadGroup', arg1: bool, arg2: 'Predicate') -> 'Collection':
        """public static java.util.Collection<java.lang.ThreadGroup> org.apache.commons.lang3.ThreadUtils.findThreadGroups(java.lang.ThreadGroup,boolean,java.util.function.Predicate<java.lang.ThreadGroup>)"""
        return Collection._wrap(_ThreadUtils.findThreadGroups(arg0, _boolean.valueOf(arg1), arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.ThreadUtils()"""
        val = _ThreadUtils()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.ThreadUtils()"""
        val = _ThreadUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def findThreadsByName(arg0: str) -> 'Collection':
        """public static java.util.Collection<java.lang.Thread> org.apache.commons.lang3.ThreadUtils.findThreadsByName(java.lang.String)"""
        return Collection._wrap(_ThreadUtils.findThreadsByName(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def findThreads(arg0: 'ThreadPredicate') -> 'Collection':
        """public static java.util.Collection<java.lang.Thread> org.apache.commons.lang3.ThreadUtils.findThreads(org.apache.commons.lang3.ThreadUtils$ThreadPredicate)"""
        return Collection._wrap(_ThreadUtils.findThreads(arg0))

    @staticmethod
    @overload
    def findThreadsByName(arg0: str, arg1: 'ThreadGroup') -> 'Collection':
        """public static java.util.Collection<java.lang.Thread> org.apache.commons.lang3.ThreadUtils.findThreadsByName(java.lang.String,java.lang.ThreadGroup)"""
        return Collection._wrap(_ThreadUtils.findThreadsByName(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def findThreadGroups(arg0: 'ThreadGroup', arg1: bool, arg2: 'ThreadGroupPredicate') -> 'Collection':
        """public static java.util.Collection<java.lang.ThreadGroup> org.apache.commons.lang3.ThreadUtils.findThreadGroups(java.lang.ThreadGroup,boolean,org.apache.commons.lang3.ThreadUtils$ThreadGroupPredicate)"""
        return Collection._wrap(_ThreadUtils.findThreadGroups(arg0, _boolean.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def sleep(arg0: 'Duration'):
        """public static void org.apache.commons.lang3.ThreadUtils.sleep(java.time.Duration) throws java.lang.InterruptedException"""
        _ThreadUtils.sleep(arg0)

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
    def getAllThreads() -> 'Collection':
        """public static java.util.Collection<java.lang.Thread> org.apache.commons.lang3.ThreadUtils.getAllThreads()"""
        return Collection._wrap(_ThreadUtils.getAllThreads())

    @staticmethod
    @overload
    def findThreadGroupsByName(arg0: str) -> 'Collection':
        """public static java.util.Collection<java.lang.ThreadGroup> org.apache.commons.lang3.ThreadUtils.findThreadGroupsByName(java.lang.String)"""
        return Collection._wrap(_ThreadUtils.findThreadGroupsByName(arg0))

    @staticmethod
    @overload
    def findThreadById(arg0: int) -> 'Thread':
        """public static java.lang.Thread org.apache.commons.lang3.ThreadUtils.findThreadById(long)"""
        return Thread._wrap(_ThreadUtils.findThreadById(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def findThreadGroups(arg0: 'ThreadGroupPredicate') -> 'Collection':
        """public static java.util.Collection<java.lang.ThreadGroup> org.apache.commons.lang3.ThreadUtils.findThreadGroups(org.apache.commons.lang3.ThreadUtils$ThreadGroupPredicate)"""
        return Collection._wrap(_ThreadUtils.findThreadGroups(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.apache.commons.lang3.ThreadUtils
import java.lang.Thread as Thread
import java.util.function.Predicate as Predicate
from builtins import str
import java.lang.Thread as _Thread
_Thread = _Thread
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.ThreadGroup as _ThreadGroup
_ThreadGroup = _ThreadGroup
import java.lang.Object as _object
from builtins import type
import java.time.Duration as Duration
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.lang.ThreadGroup as ThreadGroup
from builtins import bool
import java.lang.Long as _long
import org.apache.commons.lang3.ThreadUtils as _ThreadUtils
_ThreadUtils = _ThreadUtils
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ThreadUtils():
    """org.apache.commons.lang3.ThreadUtils"""
 
    @staticmethod
    def _wrap(java_value: _ThreadUtils) -> 'ThreadUtils':
        return ThreadUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ThreadUtils):
        """
        Dynamic initializer for ThreadUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ThreadUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ThreadUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def findThreadById(arg0: int, arg1: 'ThreadGroup') -> 'Thread':
        """public static java.lang.Thread org.apache.commons.lang3.ThreadUtils.findThreadById(long,java.lang.ThreadGroup)"""
        return Thread._wrap(_ThreadUtils.findThreadById(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def findThreads(arg0: 'Predicate') -> 'Collection':
        """public static java.util.Collection<java.lang.Thread> org.apache.commons.lang3.ThreadUtils.findThreads(java.util.function.Predicate<java.lang.Thread>)"""
        return Collection._wrap(_ThreadUtils.findThreads(arg0))

    @staticmethod
    @overload
    def findThreadById(arg0: int, arg1: str) -> 'Thread':
        """public static java.lang.Thread org.apache.commons.lang3.ThreadUtils.findThreadById(long,java.lang.String)"""
        return Thread._wrap(_ThreadUtils.findThreadById(_long.valueOf(arg0), arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def sleepQuietly(arg0: 'Duration'):
        """public static void org.apache.commons.lang3.ThreadUtils.sleepQuietly(java.time.Duration)"""
        _ThreadUtils.sleepQuietly(arg0)

    @staticmethod
    @overload
    def findThreadGroups(arg0: 'Predicate') -> 'Collection':
        """public static java.util.Collection<java.lang.ThreadGroup> org.apache.commons.lang3.ThreadUtils.findThreadGroups(java.util.function.Predicate<java.lang.ThreadGroup>)"""
        return Collection._wrap(_ThreadUtils.findThreadGroups(arg0))

    @staticmethod
    @overload
    def findThreads(arg0: 'ThreadGroup', arg1: bool, arg2: 'Predicate') -> 'Collection':
        """public static java.util.Collection<java.lang.Thread> org.apache.commons.lang3.ThreadUtils.findThreads(java.lang.ThreadGroup,boolean,java.util.function.Predicate<java.lang.Thread>)"""
        return Collection._wrap(_ThreadUtils.findThreads(arg0, _boolean.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def findThreadsByName(arg0: str, arg1: str) -> 'Collection':
        """public static java.util.Collection<java.lang.Thread> org.apache.commons.lang3.ThreadUtils.findThreadsByName(java.lang.String,java.lang.String)"""
        return Collection._wrap(_ThreadUtils.findThreadsByName(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def getAllThreadGroups() -> 'Collection':
        """public static java.util.Collection<java.lang.ThreadGroup> org.apache.commons.lang3.ThreadUtils.getAllThreadGroups()"""
        return Collection._wrap(_ThreadUtils.getAllThreadGroups())

    @staticmethod
    @overload
    def findThreads(arg0: 'ThreadGroup', arg1: bool, arg2: 'ThreadPredicate') -> 'Collection':
        """public static java.util.Collection<java.lang.Thread> org.apache.commons.lang3.ThreadUtils.findThreads(java.lang.ThreadGroup,boolean,org.apache.commons.lang3.ThreadUtils$ThreadPredicate)"""
        return Collection._wrap(_ThreadUtils.findThreads(arg0, _boolean.valueOf(arg1), arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def join(arg0: 'Thread', arg1: 'Duration'):
        """public static void org.apache.commons.lang3.ThreadUtils.join(java.lang.Thread,java.time.Duration) throws java.lang.InterruptedException"""
        _ThreadUtils.join(arg0, arg1)

    @staticmethod
    @overload
    def getSystemThreadGroup() -> 'ThreadGroup':
        """public static java.lang.ThreadGroup org.apache.commons.lang3.ThreadUtils.getSystemThreadGroup()"""
        return ThreadGroup._wrap(_ThreadUtils.getSystemThreadGroup())

    @staticmethod
    @overload
    def findThreadGroups(arg0: 'ThreadGroup', arg1: bool, arg2: 'Predicate') -> 'Collection':
        """public static java.util.Collection<java.lang.ThreadGroup> org.apache.commons.lang3.ThreadUtils.findThreadGroups(java.lang.ThreadGroup,boolean,java.util.function.Predicate<java.lang.ThreadGroup>)"""
        return Collection._wrap(_ThreadUtils.findThreadGroups(arg0, _boolean.valueOf(arg1), arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.ThreadUtils()"""
        val = _ThreadUtils()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.ThreadUtils()"""
        val = _ThreadUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def findThreadsByName(arg0: str) -> 'Collection':
        """public static java.util.Collection<java.lang.Thread> org.apache.commons.lang3.ThreadUtils.findThreadsByName(java.lang.String)"""
        return Collection._wrap(_ThreadUtils.findThreadsByName(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def findThreads(arg0: 'ThreadPredicate') -> 'Collection':
        """public static java.util.Collection<java.lang.Thread> org.apache.commons.lang3.ThreadUtils.findThreads(org.apache.commons.lang3.ThreadUtils$ThreadPredicate)"""
        return Collection._wrap(_ThreadUtils.findThreads(arg0))

    @staticmethod
    @overload
    def findThreadsByName(arg0: str, arg1: 'ThreadGroup') -> 'Collection':
        """public static java.util.Collection<java.lang.Thread> org.apache.commons.lang3.ThreadUtils.findThreadsByName(java.lang.String,java.lang.ThreadGroup)"""
        return Collection._wrap(_ThreadUtils.findThreadsByName(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def findThreadGroups(arg0: 'ThreadGroup', arg1: bool, arg2: 'ThreadGroupPredicate') -> 'Collection':
        """public static java.util.Collection<java.lang.ThreadGroup> org.apache.commons.lang3.ThreadUtils.findThreadGroups(java.lang.ThreadGroup,boolean,org.apache.commons.lang3.ThreadUtils$ThreadGroupPredicate)"""
        return Collection._wrap(_ThreadUtils.findThreadGroups(arg0, _boolean.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def sleep(arg0: 'Duration'):
        """public static void org.apache.commons.lang3.ThreadUtils.sleep(java.time.Duration) throws java.lang.InterruptedException"""
        _ThreadUtils.sleep(arg0)

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
    def getAllThreads() -> 'Collection':
        """public static java.util.Collection<java.lang.Thread> org.apache.commons.lang3.ThreadUtils.getAllThreads()"""
        return Collection._wrap(_ThreadUtils.getAllThreads())

    @staticmethod
    @overload
    def findThreadGroupsByName(arg0: str) -> 'Collection':
        """public static java.util.Collection<java.lang.ThreadGroup> org.apache.commons.lang3.ThreadUtils.findThreadGroupsByName(java.lang.String)"""
        return Collection._wrap(_ThreadUtils.findThreadGroupsByName(arg0))

    @staticmethod
    @overload
    def findThreadById(arg0: int) -> 'Thread':
        """public static java.lang.Thread org.apache.commons.lang3.ThreadUtils.findThreadById(long)"""
        return Thread._wrap(_ThreadUtils.findThreadById(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def findThreadGroups(arg0: 'ThreadGroupPredicate') -> 'Collection':
        """public static java.util.Collection<java.lang.ThreadGroup> org.apache.commons.lang3.ThreadUtils.findThreadGroups(org.apache.commons.lang3.ThreadUtils$ThreadGroupPredicate)"""
        return Collection._wrap(_ThreadUtils.findThreadGroups(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.apache.commons.lang3.ThreadUtils 
 
 
# CLASS: org.apache.commons.lang3.LocaleUtils
import java.util.Locale as Locale
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.LocaleUtils as _LocaleUtils
_LocaleUtils = _LocaleUtils
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.Set as _Set
_Set = _Set
import java.lang.String as _string
import java.util.Set as Set
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import java.util.Locale as _Locale
_Locale = _Locale
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LocaleUtils():
    """org.apache.commons.lang3.LocaleUtils"""
 
    @staticmethod
    def _wrap(java_value: _LocaleUtils) -> 'LocaleUtils':
        return LocaleUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LocaleUtils):
        """
        Dynamic initializer for LocaleUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LocaleUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LocaleUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def availableLocaleSet() -> 'Set':
        """public static java.util.Set<java.util.Locale> org.apache.commons.lang3.LocaleUtils.availableLocaleSet()"""
        return Set._wrap(_LocaleUtils.availableLocaleSet())

    @staticmethod
    @overload
    def localeLookupList(arg0: 'Locale', arg1: 'Locale') -> 'List':
        """public static java.util.List<java.util.Locale> org.apache.commons.lang3.LocaleUtils.localeLookupList(java.util.Locale,java.util.Locale)"""
        return List._wrap(_LocaleUtils.localeLookupList(arg0, arg1))

    @staticmethod
    @overload
    def toLocale(arg0: str) -> 'Locale':
        """public static java.util.Locale org.apache.commons.lang3.LocaleUtils.toLocale(java.lang.String)"""
        return Locale._wrap(_LocaleUtils.toLocale(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.LocaleUtils()"""
        val = _LocaleUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def localeLookupList(arg0: 'Locale') -> 'List':
        """public static java.util.List<java.util.Locale> org.apache.commons.lang3.LocaleUtils.localeLookupList(java.util.Locale)"""
        return List._wrap(_LocaleUtils.localeLookupList(arg0))

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

    @staticmethod
    @overload
    def availableLocaleList() -> 'List':
        """public static java.util.List<java.util.Locale> org.apache.commons.lang3.LocaleUtils.availableLocaleList()"""
        return List._wrap(_LocaleUtils.availableLocaleList())

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
    def languagesByCountry(arg0: str) -> 'List':
        """public static java.util.List<java.util.Locale> org.apache.commons.lang3.LocaleUtils.languagesByCountry(java.lang.String)"""
        return List._wrap(_LocaleUtils.languagesByCountry(arg0))

    @staticmethod
    @overload
    def toLocale(arg0: 'Locale') -> 'Locale':
        """public static java.util.Locale org.apache.commons.lang3.LocaleUtils.toLocale(java.util.Locale)"""
        return Locale._wrap(_LocaleUtils.toLocale(arg0))

    @staticmethod
    @overload
    def countriesByLanguage(arg0: str) -> 'List':
        """public static java.util.List<java.util.Locale> org.apache.commons.lang3.LocaleUtils.countriesByLanguage(java.lang.String)"""
        return List._wrap(_LocaleUtils.countriesByLanguage(arg0))

    @staticmethod
    @overload
    def isAvailableLocale(arg0: 'Locale') -> bool:
        """public static boolean org.apache.commons.lang3.LocaleUtils.isAvailableLocale(java.util.Locale)"""
        return bool._wrap(_LocaleUtils.isAvailableLocale(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.LocaleUtils()"""
        val = _LocaleUtils()
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.lang3.Functions$FailablePredicate
import org.apache.commons.lang3.Functions as _Functions_FailablePredicate
_FailablePredicate = _Functions_FailablePredicate.FailablePredicate
from abc import abstractmethod, ABC
 
class FailablePredicate():
    """org.apache.commons.lang3.Functions.FailablePredicate"""
 
    @staticmethod
    def _wrap(java_value: _FailablePredicate) -> 'FailablePredicate':
        return FailablePredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailablePredicate):
        """
        Dynamic initializer for FailablePredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailablePredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailablePredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def test(self, arg0: object):
        """public abstract boolean org.apache.commons.lang3.Functions$FailablePredicate.test(I) throws T"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.ThreadUtils$ThreadIdPredicate
import java.lang.Thread as Thread
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import org.apache.commons.lang3.ThreadUtils as _ThreadUtils_ThreadIdPredicate
_ThreadIdPredicate = _ThreadUtils_ThreadIdPredicate.ThreadIdPredicate
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ThreadIdPredicate():
    """org.apache.commons.lang3.ThreadUtils.ThreadIdPredicate"""
 
    @staticmethod
    def _wrap(java_value: _ThreadIdPredicate) -> 'ThreadIdPredicate':
        return ThreadIdPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ThreadIdPredicate):
        """
        Dynamic initializer for ThreadIdPredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ThreadIdPredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ThreadIdPredicate__wrapper":
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
    def __init__(self, arg0: int):
        """public org.apache.commons.lang3.ThreadUtils$ThreadIdPredicate(long)"""
        val = _ThreadIdPredicate(_long.valueOf(arg0))
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

    @overload
    def test(self, arg0: 'Thread') -> bool:
        """public boolean org.apache.commons.lang3.ThreadUtils$ThreadIdPredicate.test(java.lang.Thread)"""
        return bool._wrap(super(_ThreadIdPredicate, self).test(arg0))

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
 
 
# CLASS: org.apache.commons.lang3.ArrayUtils
import java.util.function.Supplier as Supplier
import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Long as Long
import java.lang.Object as _Object
_Object = _Object
import java.lang.Short as Short
import java.lang.Byte as _Byte
_Byte = _Byte
import java.lang.Double as _Double
_Double = _Double
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.lang.Boolean as _Boolean
_Boolean = _Boolean
import java.lang.Short as _short
import java.util.BitSet as BitSet
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Byte as _byte
import java.lang.Character as Character
from builtins import bool
import java.lang.Boolean as Boolean
from builtins import str
import java.lang.Long as _Long
_Long = _Long
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
from builtins import float
import java.lang.Float as Float
import org.apache.commons.lang3.ArrayUtils as _ArrayUtils
_ArrayUtils = _ArrayUtils
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Comparable as Comparable
import java.lang.Byte as Byte
import java.util.BitSet as _BitSet
_BitSet = _BitSet
from typing import List
import java.lang.Float as _float
import java.util.Comparator as Comparator
import java.lang.Float as _Float
_Float = _Float
import java.lang.Integer as _int
import java.lang.Character as _Character
_Character = _Character
import java.lang.Integer as Integer
import java.lang.Integer as _Integer
_Integer = _Integer
import java.util.Map as Map
import java.lang.Short as _Short
_Short = _Short
import java.lang.Long as _long
import java.lang.Double as Double
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.util.Random as Random
 
class ArrayUtils():
    """org.apache.commons.lang3.ArrayUtils"""
 
    @staticmethod
    def _wrap(java_value: _ArrayUtils) -> 'ArrayUtils':
        return ArrayUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ArrayUtils):
        """
        Dynamic initializer for ArrayUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ArrayUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ArrayUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def lastIndexOf(arg0: 'Object', arg1: object, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(java.lang.Object[],java.lang.Object,int)"""
        return int._wrap(_ArrayUtils.lastIndexOf(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def add(arg0: 'boolean', arg1: bool) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.add(boolean[],boolean)"""
        return List[bool]._wrap(_ArrayUtils.add(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def shuffle(arg0: bytes):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(byte[])"""
        _ArrayUtils.shuffle(bytes)

    @staticmethod
    @overload
    def removeAllOccurences(arg0: 'float', arg1: float) -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.removeAllOccurences(float[],float)"""
        return List[float]._wrap(_ArrayUtils.removeAllOccurences(arg0, _float.valueOf(arg1)))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'String') -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(java.lang.String[])"""
        return List[str]._wrap(_ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def indexesOf(arg0: 'long', arg1: int, arg2: int) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(long[],long,int)"""
        return BitSet._wrap(_ArrayUtils.indexesOf(arg0, _long.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def reverse(arg0: bytes):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(byte[])"""
        _ArrayUtils.reverse(bytes)

    @staticmethod
    @overload
    def add(arg0: 'long', arg1: int, arg2: int) -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.add(long[],int,long)"""
        return List[int]._wrap(_ArrayUtils.add(arg0, _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def indexOf(arg0: 'boolean', arg1: bool, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(boolean[],boolean,int)"""
        return int._wrap(_ArrayUtils.indexOf(arg0, _boolean.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def indexOf(arg0: 'short', arg1: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(short[],short)"""
        return int._wrap(_ArrayUtils.indexOf(arg0, _short.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def toObject(arg0: 'int') -> List['Integer']:
        """public static java.lang.Integer[] org.apache.commons.lang3.ArrayUtils.toObject(int[])"""
        return List[Integer]._wrap(_ArrayUtils.toObject(arg0))

    @staticmethod
    @overload
    def insert(arg0: int, arg1: bytes, *arg2: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.insert(int,byte[],byte...)"""
        return List[int]._wrap(_ArrayUtils.insert(_int.valueOf(arg0), bytes, bytes))

    @staticmethod
    @overload
    def shuffle(arg0: 'Object', arg1: 'Random'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(java.lang.Object[],java.util.Random)"""
        _ArrayUtils.shuffle(arg0, arg1)

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'Double') -> List['Double']:
        """public static java.lang.Double[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(java.lang.Double[])"""
        return List[Double]._wrap(_ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def indexesOf(arg0: 'short', arg1: int, arg2: int) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(short[],short,int)"""
        return BitSet._wrap(_ArrayUtils.indexesOf(arg0, _short.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def addFirst(arg0: 'int', arg1: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.addFirst(int[],int)"""
        return List[int]._wrap(_ArrayUtils.addFirst(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def indexOf(arg0: 'int', arg1: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(int[],int)"""
        return int._wrap(_ArrayUtils.indexOf(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def clone(arg0: 'int') -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.clone(int[])"""
        return List[int]._wrap(_ArrayUtils.clone(arg0))

    @staticmethod
    @overload
    def add(arg0: 'boolean', arg1: int, arg2: bool) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.add(boolean[],int,boolean)"""
        return List[bool]._wrap(_ArrayUtils.add(arg0, _int.valueOf(arg1), _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def isSorted(arg0: 'Object', arg1: 'Comparator') -> bool:
        """public static <T> boolean org.apache.commons.lang3.ArrayUtils.isSorted(T[],java.util.Comparator<T>)"""
        return bool._wrap(_ArrayUtils.isSorted(arg0, arg1))

    @staticmethod
    @overload
    def add(arg0: 'double', arg1: float) -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.add(double[],double)"""
        return List[float]._wrap(_ArrayUtils.add(arg0, _double.valueOf(arg1)))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Long', arg1: int) -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Long[],long)"""
        return List[int]._wrap(_ArrayUtils.toPrimitive(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def toMap(arg0: 'Object') -> 'Map':
        """public static java.util.Map<java.lang.Object, java.lang.Object> org.apache.commons.lang3.ArrayUtils.toMap(java.lang.Object[])"""
        return Map._wrap(_ArrayUtils.toMap(arg0))

    @staticmethod
    @overload
    def indexesOf(arg0: 'boolean', arg1: bool) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(boolean[],boolean)"""
        return BitSet._wrap(_ArrayUtils.indexesOf(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def swap(arg0: bytes, arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(byte[],int,int)"""
        _ArrayUtils.swap(bytes, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def toObject(arg0: 'short') -> List['Short']:
        """public static java.lang.Short[] org.apache.commons.lang3.ArrayUtils.toObject(short[])"""
        return List[Short]._wrap(_ArrayUtils.toObject(arg0))

    @staticmethod
    @overload
    def removeElements(arg0: 'char', *arg1: str) -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.removeElements(char[],char...)"""
        return List[str]._wrap(_ArrayUtils.removeElements(arg0, arg1))

    @staticmethod
    @overload
    def toObject(arg0: 'long') -> List['Long']:
        """public static java.lang.Long[] org.apache.commons.lang3.ArrayUtils.toObject(long[])"""
        return List[Long]._wrap(_ArrayUtils.toObject(arg0))

    @staticmethod
    @overload
    def indexesOf(arg0: 'Object', arg1: object) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(java.lang.Object[],java.lang.Object)"""
        return BitSet._wrap(_ArrayUtils.indexesOf(arg0, arg1))

    @staticmethod
    @overload
    def reverse(arg0: 'Object', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(java.lang.Object[],int,int)"""
        _ArrayUtils.reverse(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def toObject(arg0: 'boolean') -> List['Boolean']:
        """public static java.lang.Boolean[] org.apache.commons.lang3.ArrayUtils.toObject(boolean[])"""
        return List[Boolean]._wrap(_ArrayUtils.toObject(arg0))

    @staticmethod
    @overload
    def isEmpty(arg0: 'int') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isEmpty(int[])"""
        return bool._wrap(_ArrayUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def addAll(arg0: 'int', *arg1: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.addAll(int[],int...)"""
        return List[int]._wrap(_ArrayUtils.addAll(arg0, arg1))

    @staticmethod
    @overload
    def addFirst(arg0: 'float', arg1: float) -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.addFirst(float[],float)"""
        return List[float]._wrap(_ArrayUtils.addFirst(arg0, _float.valueOf(arg1)))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'Byte') -> List['Byte']:
        """public static java.lang.Byte[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(java.lang.Byte[])"""
        return List[Byte]._wrap(_ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def add(arg0: 'short', arg1: int, arg2: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.add(short[],int,short)"""
        return List[int]._wrap(_ArrayUtils.add(arg0, _int.valueOf(arg1), _short.valueOf(arg2)))

    @staticmethod
    @overload
    def indexesOf(arg0: 'double', arg1: float) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(double[],double)"""
        return BitSet._wrap(_ArrayUtils.indexesOf(arg0, _double.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'boolean', arg1: bool) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(boolean[],boolean)"""
        return int._wrap(_ArrayUtils.lastIndexOf(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def reverse(arg0: 'long', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(long[],int,int)"""
        _ArrayUtils.reverse(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def add(arg0: 'int', arg1: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.add(int[],int)"""
        return List[int]._wrap(_ArrayUtils.add(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'int', arg1: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(int[],int)"""
        return int._wrap(_ArrayUtils.lastIndexOf(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def setAll(arg0: 'Object', arg1: 'IntFunction') -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.setAll(T[],java.util.function.IntFunction<? extends T>)"""
        return List[object]._wrap(_ArrayUtils.setAll(arg0, arg1))

    @staticmethod
    @overload
    def removeAllOccurences(arg0: 'int', arg1: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.removeAllOccurences(int[],int)"""
        return List[int]._wrap(_ArrayUtils.removeAllOccurences(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'float', arg1: float, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(float[],float,int)"""
        return int._wrap(_ArrayUtils.lastIndexOf(arg0, _float.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def isSorted(arg0: bytes) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSorted(byte[])"""
        return bool._wrap(_ArrayUtils.isSorted(bytes))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.ArrayUtils()"""
        val = _ArrayUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'double') -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(double[])"""
        return List[float]._wrap(_ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def add(arg0: 'char', arg1: int, arg2: str) -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.add(char[],int,char)"""
        return List[str]._wrap(_ArrayUtils.add(arg0, _int.valueOf(arg1), _char.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def removeAllOccurences(arg0: 'char', arg1: str) -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.removeAllOccurences(char[],char)"""
        return List[str]._wrap(_ArrayUtils.removeAllOccurences(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def removeElements(arg0: bytes, *arg1: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.removeElements(byte[],byte...)"""
        return List[int]._wrap(_ArrayUtils.removeElements(bytes, bytes))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Double') -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Double[])"""
        return List[float]._wrap(_ArrayUtils.toPrimitive(arg0))

    @staticmethod
    @overload
    def getLength(arg0: object) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.getLength(java.lang.Object)"""
        return int._wrap(_ArrayUtils.getLength(arg0))

    @staticmethod
    @overload
    def shuffle(arg0: 'Object'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(java.lang.Object[])"""
        _ArrayUtils.shuffle(arg0)

    @staticmethod
    @overload
    def removeAllOccurences(arg0: 'boolean', arg1: bool) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.removeAllOccurences(boolean[],boolean)"""
        return List[bool]._wrap(_ArrayUtils.removeAllOccurences(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def shift(arg0: bytes, arg1: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(byte[],int)"""
        _ArrayUtils.shift(bytes, _int.valueOf(arg1))

    @staticmethod
    @overload
    def isSameType(arg0: object, arg1: object) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSameType(java.lang.Object,java.lang.Object)"""
        return bool._wrap(_ArrayUtils.isSameType(arg0, arg1))

    @staticmethod
    @overload
    def removeElement(arg0: 'float', arg1: float) -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.removeElement(float[],float)"""
        return List[float]._wrap(_ArrayUtils.removeElement(arg0, _float.valueOf(arg1)))

    @staticmethod
    @overload
    def removeElements(arg0: 'short', *arg1: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.removeElements(short[],short...)"""
        return List[int]._wrap(_ArrayUtils.removeElements(arg0, arg1))

    @staticmethod
    @overload
    def subarray(arg0: 'int', arg1: int, arg2: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.subarray(int[],int,int)"""
        return List[int]._wrap(_ArrayUtils.subarray(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def swap(arg0: 'long', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(long[],int,int)"""
        _ArrayUtils.swap(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def insert(arg0: int, arg1: 'long', *arg2: int) -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.insert(int,long[],long...)"""
        return List[int]._wrap(_ArrayUtils.insert(_int.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def shift(arg0: 'double', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(double[],int,int,int)"""
        _ArrayUtils.shift(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'int') -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(int[])"""
        return List[int]._wrap(_ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Float', arg1: float) -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Float[],float)"""
        return List[float]._wrap(_ArrayUtils.toPrimitive(arg0, _float.valueOf(arg1)))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'Object', arg1: object) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(java.lang.Object[],java.lang.Object)"""
        return int._wrap(_ArrayUtils.lastIndexOf(arg0, arg1))

    @staticmethod
    @overload
    def shuffle(arg0: 'boolean'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(boolean[])"""
        _ArrayUtils.shuffle(arg0)

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'double', arg1: float, arg2: float) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(double[],double,double)"""
        return int._wrap(_ArrayUtils.lastIndexOf(arg0, _double.valueOf(arg1), _double.valueOf(arg2)))

    @staticmethod
    @overload
    def removeElement(arg0: 'char', arg1: str) -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.removeElement(char[],char)"""
        return List[str]._wrap(_ArrayUtils.removeElement(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def add(arg0: bytes, arg1: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.add(byte[],byte)"""
        return List[int]._wrap(_ArrayUtils.add(bytes, _byte.valueOf(arg1)))

    @staticmethod
    @overload
    def contains(arg0: 'double', arg1: float) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.contains(double[],double)"""
        return bool._wrap(_ArrayUtils.contains(arg0, _double.valueOf(arg1)))

    @staticmethod
    @overload
    def isSameLength(arg0: object, arg1: object) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSameLength(java.lang.Object,java.lang.Object)"""
        return bool._wrap(_ArrayUtils.isSameLength(arg0, arg1))

    @staticmethod
    @overload
    def toObject(arg0: bytes) -> List['Byte']:
        """public static java.lang.Byte[] org.apache.commons.lang3.ArrayUtils.toObject(byte[])"""
        return List[Byte]._wrap(_ArrayUtils.toObject(bytes))

    @staticmethod
    @overload
    def shift(arg0: bytes, arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(byte[],int,int,int)"""
        _ArrayUtils.shift(bytes, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def add(arg0: 'float', arg1: int, arg2: float) -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.add(float[],int,float)"""
        return List[float]._wrap(_ArrayUtils.add(arg0, _int.valueOf(arg1), _float.valueOf(arg2)))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Integer', arg1: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Integer[],int)"""
        return List[int]._wrap(_ArrayUtils.toPrimitive(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def shuffle(arg0: 'int'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(int[])"""
        _ArrayUtils.shuffle(arg0)

    @staticmethod
    @overload
    def toString(arg0: object, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ArrayUtils.toString(java.lang.Object,java.lang.String)"""
        return str._wrap(_ArrayUtils.toString(arg0, arg1))

    @staticmethod
    @overload
    def removeAllOccurrences(arg0: bytes, arg1: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.removeAllOccurrences(byte[],byte)"""
        return List[int]._wrap(_ArrayUtils.removeAllOccurrences(bytes, _byte.valueOf(arg1)))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'Object', arg1: 'Class') -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(T[],java.lang.Class<T[]>)"""
        return List[object]._wrap(_ArrayUtils.nullToEmpty(arg0, arg1))

    @staticmethod
    @overload
    def isNotEmpty(arg0: 'float') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isNotEmpty(float[])"""
        return bool._wrap(_ArrayUtils.isNotEmpty(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def isEmpty(arg0: 'short') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isEmpty(short[])"""
        return bool._wrap(_ArrayUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'Boolean') -> List['Boolean']:
        """public static java.lang.Boolean[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(java.lang.Boolean[])"""
        return List[Boolean]._wrap(_ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def swap(arg0: 'char', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(char[],int,int)"""
        _ArrayUtils.swap(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def toStringArray(arg0: 'Object', arg1: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.ArrayUtils.toStringArray(java.lang.Object[],java.lang.String)"""
        return List[str]._wrap(_ArrayUtils.toStringArray(arg0, arg1))

    @staticmethod
    @overload
    def indexOf(arg0: 'Object', arg1: object, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(java.lang.Object[],java.lang.Object,int)"""
        return int._wrap(_ArrayUtils.indexOf(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def swap(arg0: 'float', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(float[],int,int)"""
        _ArrayUtils.swap(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def reverse(arg0: 'char', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(char[],int,int)"""
        _ArrayUtils.reverse(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def lastIndexOf(arg0: bytes, arg1: int, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(byte[],byte,int)"""
        return int._wrap(_ArrayUtils.lastIndexOf(bytes, _byte.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def removeElements(arg0: 'int', *arg1: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.removeElements(int[],int...)"""
        return List[int]._wrap(_ArrayUtils.removeElements(arg0, arg1))

    @staticmethod
    @overload
    def indexesOf(arg0: 'double', arg1: float, arg2: float) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(double[],double,double)"""
        return BitSet._wrap(_ArrayUtils.indexesOf(arg0, _double.valueOf(arg1), _double.valueOf(arg2)))

    @staticmethod
    @overload
    def clone(arg0: 'short') -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.clone(short[])"""
        return List[int]._wrap(_ArrayUtils.clone(arg0))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Short') -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Short[])"""
        return List[int]._wrap(_ArrayUtils.toPrimitive(arg0))

    @staticmethod
    @overload
    def reverse(arg0: 'long'):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(long[])"""
        _ArrayUtils.reverse(arg0)

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'int', arg1: int, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(int[],int,int)"""
        return int._wrap(_ArrayUtils.lastIndexOf(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def isEmpty(arg0: 'double') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isEmpty(double[])"""
        return bool._wrap(_ArrayUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def isEmpty(arg0: 'boolean') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isEmpty(boolean[])"""
        return bool._wrap(_ArrayUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def swap(arg0: 'int', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(int[],int,int)"""
        _ArrayUtils.swap(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def insert(arg0: int, arg1: 'char', *arg2: str) -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.insert(int,char[],char...)"""
        return List[str]._wrap(_ArrayUtils.insert(_int.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'float', arg1: float) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(float[],float)"""
        return int._wrap(_ArrayUtils.lastIndexOf(arg0, _float.valueOf(arg1)))

    @staticmethod
    @overload
    def remove(arg0: 'short', arg1: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.remove(short[],int)"""
        return List[int]._wrap(_ArrayUtils.remove(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'char', arg1: str) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(char[],char)"""
        return int._wrap(_ArrayUtils.lastIndexOf(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Boolean') -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Boolean[])"""
        return List[bool]._wrap(_ArrayUtils.toPrimitive(arg0))

    @staticmethod
    @overload
    def shuffle(arg0: 'long', arg1: 'Random'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(long[],java.util.Random)"""
        _ArrayUtils.shuffle(arg0, arg1)

    @staticmethod
    @overload
    def shift(arg0: 'Object', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(java.lang.Object[],int,int,int)"""
        _ArrayUtils.shift(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def reverse(arg0: 'float', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(float[],int,int)"""
        _ArrayUtils.reverse(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def shift(arg0: 'long', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(long[],int,int,int)"""
        _ArrayUtils.shift(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'double', arg1: float) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(double[],double)"""
        return int._wrap(_ArrayUtils.lastIndexOf(arg0, _double.valueOf(arg1)))

    @staticmethod
    @overload
    def contains(arg0: 'Object', arg1: object) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.contains(java.lang.Object[],java.lang.Object)"""
        return bool._wrap(_ArrayUtils.contains(arg0, arg1))

    @staticmethod
    @overload
    def shuffle(arg0: 'char', arg1: 'Random'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(char[],java.util.Random)"""
        _ArrayUtils.shuffle(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def reverse(arg0: 'Object'):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(java.lang.Object[])"""
        _ArrayUtils.reverse(arg0)

    @staticmethod
    @overload
    def removeAll(arg0: 'float', *arg1: int) -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.removeAll(float[],int...)"""
        return List[float]._wrap(_ArrayUtils.removeAll(arg0, arg1))

    @staticmethod
    @overload
    def subarray(arg0: 'char', arg1: int, arg2: int) -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.subarray(char[],int,int)"""
        return List[str]._wrap(_ArrayUtils.subarray(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def swap(arg0: 'short', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(short[],int,int)"""
        _ArrayUtils.swap(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def shuffle(arg0: 'int', arg1: 'Random'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(int[],java.util.Random)"""
        _ArrayUtils.shuffle(arg0, arg1)

    @staticmethod
    @overload
    def removeElements(arg0: 'boolean', *arg1: bool) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.removeElements(boolean[],boolean...)"""
        return List[bool]._wrap(_ArrayUtils.removeElements(arg0, arg1))

    @staticmethod
    @overload
    def swap(arg0: 'Object', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(java.lang.Object[],int,int,int)"""
        _ArrayUtils.swap(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def addAll(arg0: 'long', *arg1: int) -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.addAll(long[],long...)"""
        return List[int]._wrap(_ArrayUtils.addAll(arg0, arg1))

    @staticmethod
    @overload
    def getComponentType(arg0: 'Object') -> 'type.Class':
        """public static <T> java.lang.Class<T> org.apache.commons.lang3.ArrayUtils.getComponentType(T[])"""
        return type.Class._wrap(_ArrayUtils.getComponentType(arg0))

    @staticmethod
    @overload
    def isNotEmpty(arg0: 'short') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isNotEmpty(short[])"""
        return bool._wrap(_ArrayUtils.isNotEmpty(arg0))

    @staticmethod
    @overload
    def isNotEmpty(arg0: 'double') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isNotEmpty(double[])"""
        return bool._wrap(_ArrayUtils.isNotEmpty(arg0))

    @staticmethod
    @overload
    def clone(arg0: 'boolean') -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.clone(boolean[])"""
        return List[bool]._wrap(_ArrayUtils.clone(arg0))

    @staticmethod
    @overload
    def shift(arg0: 'short', arg1: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(short[],int)"""
        _ArrayUtils.shift(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def indexesOf(arg0: 'int', arg1: int, arg2: int) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(int[],int,int)"""
        return BitSet._wrap(_ArrayUtils.indexesOf(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def toObject(arg0: 'float') -> List['Float']:
        """public static java.lang.Float[] org.apache.commons.lang3.ArrayUtils.toObject(float[])"""
        return List[Float]._wrap(_ArrayUtils.toObject(arg0))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Boolean', arg1: bool) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Boolean[],boolean)"""
        return List[bool]._wrap(_ArrayUtils.toPrimitive(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def indexOf(arg0: 'double', arg1: float, arg2: float) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(double[],double,double)"""
        return int._wrap(_ArrayUtils.indexOf(arg0, _double.valueOf(arg1), _double.valueOf(arg2)))

    @staticmethod
    @overload
    def addFirst(arg0: 'long', arg1: int) -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.addFirst(long[],long)"""
        return List[int]._wrap(_ArrayUtils.addFirst(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Character', arg1: str) -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Character[],char)"""
        return List[str]._wrap(_ArrayUtils.toPrimitive(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def addFirst(arg0: bytes, arg1: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.addFirst(byte[],byte)"""
        return List[int]._wrap(_ArrayUtils.addFirst(bytes, _byte.valueOf(arg1)))

    @staticmethod
    @overload
    def isNotEmpty(arg0: bytes) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isNotEmpty(byte[])"""
        return bool._wrap(_ArrayUtils.isNotEmpty(bytes))

    @staticmethod
    @overload
    def shuffle(arg0: 'boolean', arg1: 'Random'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(boolean[],java.util.Random)"""
        _ArrayUtils.shuffle(arg0, arg1)

    @staticmethod
    @overload
    def indexOf(arg0: 'long', arg1: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(long[],long)"""
        return int._wrap(_ArrayUtils.indexOf(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def add(arg0: 'int', arg1: int, arg2: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.add(int[],int,int)"""
        return List[int]._wrap(_ArrayUtils.add(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def swap(arg0: 'int', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(int[],int,int,int)"""
        _ArrayUtils.swap(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def reverse(arg0: 'float'):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(float[])"""
        _ArrayUtils.reverse(arg0)

    @staticmethod
    @overload
    def shift(arg0: 'float', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(float[],int,int,int)"""
        _ArrayUtils.shift(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Integer') -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Integer[])"""
        return List[int]._wrap(_ArrayUtils.toPrimitive(arg0))

    @staticmethod
    @overload
    def insert(arg0: int, arg1: 'boolean', *arg2: bool) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.insert(int,boolean[],boolean...)"""
        return List[bool]._wrap(_ArrayUtils.insert(_int.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def reverse(arg0: bytes, arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(byte[],int,int)"""
        _ArrayUtils.reverse(bytes, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def addAll(arg0: 'double', *arg1: float) -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.addAll(double[],double...)"""
        return List[float]._wrap(_ArrayUtils.addAll(arg0, arg1))

    @staticmethod
    @overload
    def shuffle(arg0: 'float'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(float[])"""
        _ArrayUtils.shuffle(arg0)

    @staticmethod
    @overload
    def removeElement(arg0: bytes, arg1: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.removeElement(byte[],byte)"""
        return List[int]._wrap(_ArrayUtils.removeElement(bytes, _byte.valueOf(arg1)))

    @staticmethod
    @overload
    def add(arg0: 'char', arg1: str) -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.add(char[],char)"""
        return List[str]._wrap(_ArrayUtils.add(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def subarray(arg0: 'Object', arg1: int, arg2: int) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.subarray(T[],int,int)"""
        return List[object]._wrap(_ArrayUtils.subarray(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def remove(arg0: 'long', arg1: int) -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.remove(long[],int)"""
        return List[int]._wrap(_ArrayUtils.remove(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def toArray(*arg0: object) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.toArray(T...)"""
        return List[object]._wrap(_ArrayUtils.toArray(arg0))

    @staticmethod
    @overload
    def clone(arg0: 'char') -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.clone(char[])"""
        return List[str]._wrap(_ArrayUtils.clone(arg0))

    @staticmethod
    @overload
    def newInstance(arg0: 'Class', arg1: int) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.newInstance(java.lang.Class<T>,int)"""
        return List[object]._wrap(_ArrayUtils.newInstance(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def addAll(arg0: 'boolean', *arg1: bool) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.addAll(boolean[],boolean...)"""
        return List[bool]._wrap(_ArrayUtils.addAll(arg0, arg1))

    @staticmethod
    @overload
    def removeAllOccurences(arg0: 'short', arg1: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.removeAllOccurences(short[],short)"""
        return List[int]._wrap(_ArrayUtils.removeAllOccurences(arg0, _short.valueOf(arg1)))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'Float') -> List['Float']:
        """public static java.lang.Float[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(java.lang.Float[])"""
        return List[Float]._wrap(_ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def nullToEmpty(arg0: bytes) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(byte[])"""
        return List[int]._wrap(_ArrayUtils.nullToEmpty(bytes))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'long') -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(long[])"""
        return List[int]._wrap(_ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def indexesOf(arg0: 'short', arg1: int) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(short[],short)"""
        return BitSet._wrap(_ArrayUtils.indexesOf(arg0, _short.valueOf(arg1)))

    @staticmethod
    @overload
    def removeAll(arg0: 'int', *arg1: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.removeAll(int[],int...)"""
        return List[int]._wrap(_ArrayUtils.removeAll(arg0, arg1))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'char') -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(char[])"""
        return List[str]._wrap(_ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def isNotEmpty(arg0: 'char') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isNotEmpty(char[])"""
        return bool._wrap(_ArrayUtils.isNotEmpty(arg0))

    @staticmethod
    @overload
    def isSameLength(arg0: 'short', arg1: 'short') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSameLength(short[],short[])"""
        return bool._wrap(_ArrayUtils.isSameLength(arg0, arg1))

    @staticmethod
    @overload
    def indexesOf(arg0: 'float', arg1: float, arg2: int) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(float[],float,int)"""
        return BitSet._wrap(_ArrayUtils.indexesOf(arg0, _float.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def setAll(arg0: 'Object', arg1: 'Supplier') -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.setAll(T[],java.util.function.Supplier<? extends T>)"""
        return List[object]._wrap(_ArrayUtils.setAll(arg0, arg1))

    @staticmethod
    @overload
    def removeElement(arg0: 'int', arg1: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.removeElement(int[],int)"""
        return List[int]._wrap(_ArrayUtils.removeElement(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def removeAllOccurrences(arg0: 'short', arg1: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.removeAllOccurrences(short[],short)"""
        return List[int]._wrap(_ArrayUtils.removeAllOccurrences(arg0, _short.valueOf(arg1)))

    @staticmethod
    @overload
    def insert(arg0: int, arg1: 'float', *arg2: float) -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.insert(int,float[],float...)"""
        return List[float]._wrap(_ArrayUtils.insert(_int.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def removeAllOccurrences(arg0: 'int', arg1: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.removeAllOccurrences(int[],int)"""
        return List[int]._wrap(_ArrayUtils.removeAllOccurrences(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def add(arg0: 'long', arg1: int) -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.add(long[],long)"""
        return List[int]._wrap(_ArrayUtils.add(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def contains(arg0: 'float', arg1: float) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.contains(float[],float)"""
        return bool._wrap(_ArrayUtils.contains(arg0, _float.valueOf(arg1)))

    @staticmethod
    @overload
    def removeAllOccurrences(arg0: 'boolean', arg1: bool) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.removeAllOccurrences(boolean[],boolean)"""
        return List[bool]._wrap(_ArrayUtils.removeAllOccurrences(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def contains(arg0: 'int', arg1: int) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.contains(int[],int)"""
        return bool._wrap(_ArrayUtils.contains(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def isEmpty(arg0: 'char') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isEmpty(char[])"""
        return bool._wrap(_ArrayUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'char', arg1: str, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(char[],char,int)"""
        return int._wrap(_ArrayUtils.lastIndexOf(arg0, _char.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def add(arg0: 'Object', arg1: int, arg2: object) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.add(T[],int,T)"""
        return List[object]._wrap(_ArrayUtils.add(arg0, _int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def removeElement(arg0: 'double', arg1: float) -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.removeElement(double[],double)"""
        return List[float]._wrap(_ArrayUtils.removeElement(arg0, _double.valueOf(arg1)))

    @staticmethod
    @overload
    def remove(arg0: 'float', arg1: int) -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.remove(float[],int)"""
        return List[float]._wrap(_ArrayUtils.remove(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def reverse(arg0: 'short', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(short[],int,int)"""
        _ArrayUtils.reverse(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def isNotEmpty(arg0: 'boolean') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isNotEmpty(boolean[])"""
        return bool._wrap(_ArrayUtils.isNotEmpty(arg0))

    @staticmethod
    @overload
    def swap(arg0: 'char', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(char[],int,int,int)"""
        _ArrayUtils.swap(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def addAll(arg0: 'char', *arg1: str) -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.addAll(char[],char...)"""
        return List[str]._wrap(_ArrayUtils.addAll(arg0, arg1))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'long', arg1: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(long[],long)"""
        return int._wrap(_ArrayUtils.lastIndexOf(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def isEquals(arg0: object, arg1: object) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isEquals(java.lang.Object,java.lang.Object)"""
        return bool._wrap(_ArrayUtils.isEquals(arg0, arg1))

    @staticmethod
    @overload
    def removeAllOccurrences(arg0: 'long', arg1: int) -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.removeAllOccurrences(long[],long)"""
        return List[int]._wrap(_ArrayUtils.removeAllOccurrences(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def removeAll(arg0: 'long', *arg1: int) -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.removeAll(long[],int...)"""
        return List[int]._wrap(_ArrayUtils.removeAll(arg0, arg1))

    @staticmethod
    @overload
    def reverse(arg0: 'short'):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(short[])"""
        _ArrayUtils.reverse(arg0)

    @staticmethod
    @overload
    def indexOf(arg0: 'long', arg1: int, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(long[],long,int)"""
        return int._wrap(_ArrayUtils.indexOf(arg0, _long.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'float') -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(float[])"""
        return List[float]._wrap(_ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def isNotEmpty(arg0: 'int') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isNotEmpty(int[])"""
        return bool._wrap(_ArrayUtils.isNotEmpty(arg0))

    @staticmethod
    @overload
    def indexesOf(arg0: 'char', arg1: str, arg2: int) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(char[],char,int)"""
        return BitSet._wrap(_ArrayUtils.indexesOf(arg0, _char.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def indexOf(arg0: 'double', arg1: float, arg2: int, arg3: float) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(double[],double,int,double)"""
        return int._wrap(_ArrayUtils.indexOf(arg0, _double.valueOf(arg1), _int.valueOf(arg2), _double.valueOf(arg3)))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'short', arg1: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(short[],short)"""
        return int._wrap(_ArrayUtils.lastIndexOf(arg0, _short.valueOf(arg1)))

    @staticmethod
    @overload
    def addFirst(arg0: 'Object', arg1: object) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.addFirst(T[],T)"""
        return List[object]._wrap(_ArrayUtils.addFirst(arg0, arg1))

    @staticmethod
    @overload
    def swap(arg0: 'double', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(double[],int,int,int)"""
        _ArrayUtils.swap(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def removeAllOccurrences(arg0: 'char', arg1: str) -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.removeAllOccurrences(char[],char)"""
        return List[str]._wrap(_ArrayUtils.removeAllOccurrences(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def reverse(arg0: 'boolean', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(boolean[],int,int)"""
        _ArrayUtils.reverse(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def insert(arg0: int, arg1: 'double', *arg2: float) -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.insert(int,double[],double...)"""
        return List[float]._wrap(_ArrayUtils.insert(_int.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def swap(arg0: 'Object', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(java.lang.Object[],int,int)"""
        _ArrayUtils.swap(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def isSameLength(arg0: 'boolean', arg1: 'boolean') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSameLength(boolean[],boolean[])"""
        return bool._wrap(_ArrayUtils.isSameLength(arg0, arg1))

    @staticmethod
    @overload
    def indexesOf(arg0: 'int', arg1: int) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(int[],int)"""
        return BitSet._wrap(_ArrayUtils.indexesOf(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def isSameLength(arg0: 'double', arg1: 'double') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSameLength(double[],double[])"""
        return bool._wrap(_ArrayUtils.isSameLength(arg0, arg1))

    @staticmethod
    @overload
    def isSorted(arg0: 'boolean') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSorted(boolean[])"""
        return bool._wrap(_ArrayUtils.isSorted(arg0))

    @staticmethod
    @overload
    def removeElements(arg0: 'double', *arg1: float) -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.removeElements(double[],double...)"""
        return List[float]._wrap(_ArrayUtils.removeElements(arg0, arg1))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'long', arg1: int, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(long[],long,int)"""
        return int._wrap(_ArrayUtils.lastIndexOf(arg0, _long.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def removeElement(arg0: 'boolean', arg1: bool) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.removeElement(boolean[],boolean)"""
        return List[bool]._wrap(_ArrayUtils.removeElement(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def shuffle(arg0: 'long'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(long[])"""
        _ArrayUtils.shuffle(arg0)

    @staticmethod
    @overload
    def shuffle(arg0: 'double', arg1: 'Random'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(double[],java.util.Random)"""
        _ArrayUtils.shuffle(arg0, arg1)

    @staticmethod
    @overload
    def indexOf(arg0: 'double', arg1: float) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(double[],double)"""
        return int._wrap(_ArrayUtils.indexOf(arg0, _double.valueOf(arg1)))

    @staticmethod
    @overload
    def removeAll(arg0: bytes, *arg1: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.removeAll(byte[],int...)"""
        return List[int]._wrap(_ArrayUtils.removeAll(bytes, arg1))

    @staticmethod
    @overload
    def contains(arg0: 'boolean', arg1: bool) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.contains(boolean[],boolean)"""
        return bool._wrap(_ArrayUtils.contains(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def addAll(arg0: 'Object', *arg1: object) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.addAll(T[],T...)"""
        return List[object]._wrap(_ArrayUtils.addAll(arg0, arg1))

    @staticmethod
    @overload
    def shift(arg0: 'char', arg1: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(char[],int)"""
        _ArrayUtils.shift(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def toPrimitive(arg0: object) -> object:
        """public static java.lang.Object org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Object)"""
        return object._wrap(_ArrayUtils.toPrimitive(arg0))

    @staticmethod
    @overload
    def reverse(arg0: 'double'):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(double[])"""
        _ArrayUtils.reverse(arg0)

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'double', arg1: float, arg2: int, arg3: float) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(double[],double,int,double)"""
        return int._wrap(_ArrayUtils.lastIndexOf(arg0, _double.valueOf(arg1), _int.valueOf(arg2), _double.valueOf(arg3)))

    @staticmethod
    @overload
    def insert(arg0: int, arg1: 'Object', *arg2: object) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.insert(int,T[],T...)"""
        return List[object]._wrap(_ArrayUtils.insert(_int.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def shuffle(arg0: 'short'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(short[])"""
        _ArrayUtils.shuffle(arg0)

    @staticmethod
    @overload
    def contains(arg0: 'short', arg1: int) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.contains(short[],short)"""
        return bool._wrap(_ArrayUtils.contains(arg0, _short.valueOf(arg1)))

    @staticmethod
    @overload
    def removeAllOccurences(arg0: 'double', arg1: float) -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.removeAllOccurences(double[],double)"""
        return List[float]._wrap(_ArrayUtils.removeAllOccurences(arg0, _double.valueOf(arg1)))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'Character') -> List['Character']:
        """public static java.lang.Character[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(java.lang.Character[])"""
        return List[Character]._wrap(_ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def removeAll(arg0: 'char', *arg1: int) -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.removeAll(char[],int...)"""
        return List[str]._wrap(_ArrayUtils.removeAll(arg0, arg1))

    @staticmethod
    @overload
    def clone(arg0: 'double') -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.clone(double[])"""
        return List[float]._wrap(_ArrayUtils.clone(arg0))

    @staticmethod
    @overload
    def isSameLength(arg0: 'Object', arg1: 'Object') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSameLength(java.lang.Object[],java.lang.Object[])"""
        return bool._wrap(_ArrayUtils.isSameLength(arg0, arg1))

    @staticmethod
    @overload
    def isSorted(arg0: 'short') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSorted(short[])"""
        return bool._wrap(_ArrayUtils.isSorted(arg0))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Long') -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Long[])"""
        return List[int]._wrap(_ArrayUtils.toPrimitive(arg0))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Float') -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Float[])"""
        return List[float]._wrap(_ArrayUtils.toPrimitive(arg0))

    @staticmethod
    @overload
    def reverse(arg0: 'double', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(double[],int,int)"""
        _ArrayUtils.reverse(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def shift(arg0: 'Object', arg1: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(java.lang.Object[],int)"""
        _ArrayUtils.shift(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def addFirst(arg0: 'double', arg1: float) -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.addFirst(double[],double)"""
        return List[float]._wrap(_ArrayUtils.addFirst(arg0, _double.valueOf(arg1)))

    @staticmethod
    @overload
    def isSameLength(arg0: bytes, arg1: bytes) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSameLength(byte[],byte[])"""
        return bool._wrap(_ArrayUtils.isSameLength(bytes, bytes))

    @staticmethod
    @overload
    def shift(arg0: 'int', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(int[],int,int,int)"""
        _ArrayUtils.shift(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'Integer') -> List['Integer']:
        """public static java.lang.Integer[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(java.lang.Integer[])"""
        return List[Integer]._wrap(_ArrayUtils.nullToEmpty(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def swap(arg0: 'boolean', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(boolean[],int,int)"""
        _ArrayUtils.swap(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def swap(arg0: 'double', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(double[],int,int)"""
        _ArrayUtils.swap(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def removeElements(arg0: 'long', *arg1: int) -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.removeElements(long[],long...)"""
        return List[int]._wrap(_ArrayUtils.removeElements(arg0, arg1))

    @staticmethod
    @overload
    def subarray(arg0: 'double', arg1: int, arg2: int) -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.subarray(double[],int,int)"""
        return List[float]._wrap(_ArrayUtils.subarray(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def removeAllOccurrences(arg0: 'double', arg1: float) -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.removeAllOccurrences(double[],double)"""
        return List[float]._wrap(_ArrayUtils.removeAllOccurrences(arg0, _double.valueOf(arg1)))

    @staticmethod
    @overload
    def removeAllOccurences(arg0: bytes, arg1: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.removeAllOccurences(byte[],byte)"""
        return List[int]._wrap(_ArrayUtils.removeAllOccurences(bytes, _byte.valueOf(arg1)))

    @staticmethod
    @overload
    def clone(arg0: 'Object') -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.clone(T[])"""
        return List[object]._wrap(_ArrayUtils.clone(arg0))

    @staticmethod
    @overload
    def removeAll(arg0: 'double', *arg1: int) -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.removeAll(double[],int...)"""
        return List[float]._wrap(_ArrayUtils.removeAll(arg0, arg1))

    @staticmethod
    @overload
    def indexOf(arg0: 'short', arg1: int, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(short[],short,int)"""
        return int._wrap(_ArrayUtils.indexOf(arg0, _short.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def shift(arg0: 'float', arg1: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(float[],int)"""
        _ArrayUtils.shift(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def remove(arg0: 'char', arg1: int) -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.remove(char[],int)"""
        return List[str]._wrap(_ArrayUtils.remove(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def isEmpty(arg0: bytes) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isEmpty(byte[])"""
        return bool._wrap(_ArrayUtils.isEmpty(bytes))

    @staticmethod
    @overload
    def indexOf(arg0: 'double', arg1: float, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(double[],double,int)"""
        return int._wrap(_ArrayUtils.indexOf(arg0, _double.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Byte') -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Byte[])"""
        return List[int]._wrap(_ArrayUtils.toPrimitive(arg0))

    @staticmethod
    @overload
    def addAll(arg0: bytes, *arg1: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.addAll(byte[],byte...)"""
        return List[int]._wrap(_ArrayUtils.addAll(bytes, bytes))

    @staticmethod
    @overload
    def indexesOf(arg0: 'double', arg1: float, arg2: int) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(double[],double,int)"""
        return BitSet._wrap(_ArrayUtils.indexesOf(arg0, _double.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def shift(arg0: 'int', arg1: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(int[],int)"""
        _ArrayUtils.shift(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Short', arg1: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Short[],short)"""
        return List[int]._wrap(_ArrayUtils.toPrimitive(arg0, _short.valueOf(arg1)))

    @staticmethod
    @overload
    def indexOf(arg0: 'float', arg1: float, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(float[],float,int)"""
        return int._wrap(_ArrayUtils.indexOf(arg0, _float.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def isSorted(arg0: 'Comparable') -> bool:
        """public static <T extends java.lang.Comparable<? super T>> boolean org.apache.commons.lang3.ArrayUtils.isSorted(T[])"""
        return bool._wrap(_ArrayUtils.isSorted(arg0))

    @staticmethod
    @overload
    def toObject(arg0: 'char') -> List['Character']:
        """public static java.lang.Character[] org.apache.commons.lang3.ArrayUtils.toObject(char[])"""
        return List[Character]._wrap(_ArrayUtils.toObject(arg0))

    @staticmethod
    @overload
    def toObject(arg0: 'double') -> List['Double']:
        """public static java.lang.Double[] org.apache.commons.lang3.ArrayUtils.toObject(double[])"""
        return List[Double]._wrap(_ArrayUtils.toObject(arg0))

    @staticmethod
    @overload
    def remove(arg0: 'Object', arg1: int) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.remove(T[],int)"""
        return List[object]._wrap(_ArrayUtils.remove(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def addFirst(arg0: 'boolean', arg1: bool) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.addFirst(boolean[],boolean)"""
        return List[bool]._wrap(_ArrayUtils.addFirst(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def shuffle(arg0: 'char'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(char[])"""
        _ArrayUtils.shuffle(arg0)

    @staticmethod
    @overload
    def shift(arg0: 'long', arg1: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(long[],int)"""
        _ArrayUtils.shift(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def indexOf(arg0: 'int', arg1: int, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(int[],int,int)"""
        return int._wrap(_ArrayUtils.indexOf(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def contains(arg0: 'long', arg1: int) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.contains(long[],long)"""
        return bool._wrap(_ArrayUtils.contains(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def reverse(arg0: 'int'):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(int[])"""
        _ArrayUtils.reverse(arg0)

    @staticmethod
    @overload
    def swap(arg0: 'short', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(short[],int,int,int)"""
        _ArrayUtils.swap(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def removeAllOccurrences(arg0: 'float', arg1: float) -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.removeAllOccurrences(float[],float)"""
        return List[float]._wrap(_ArrayUtils.removeAllOccurrences(arg0, _float.valueOf(arg1)))

    @staticmethod
    @overload
    def add(arg0: 'short', arg1: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.add(short[],short)"""
        return List[int]._wrap(_ArrayUtils.add(arg0, _short.valueOf(arg1)))

    @staticmethod
    @overload
    def swap(arg0: bytes, arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(byte[],int,int,int)"""
        _ArrayUtils.swap(bytes, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def isArrayIndexValid(arg0: 'Object', arg1: int) -> bool:
        """public static <T> boolean org.apache.commons.lang3.ArrayUtils.isArrayIndexValid(T[],int)"""
        return bool._wrap(_ArrayUtils.isArrayIndexValid(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def indexesOf(arg0: 'double', arg1: float, arg2: int, arg3: float) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(double[],double,int,double)"""
        return BitSet._wrap(_ArrayUtils.indexesOf(arg0, _double.valueOf(arg1), _int.valueOf(arg2), _double.valueOf(arg3)))

    @staticmethod
    @overload
    def indexOf(arg0: 'char', arg1: str) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(char[],char)"""
        return int._wrap(_ArrayUtils.indexOf(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def indexOf(arg0: 'Object', arg1: object) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(java.lang.Object[],java.lang.Object)"""
        return int._wrap(_ArrayUtils.indexOf(arg0, arg1))

    @staticmethod
    @overload
    def isSameLength(arg0: 'float', arg1: 'float') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSameLength(float[],float[])"""
        return bool._wrap(_ArrayUtils.isSameLength(arg0, arg1))

    @staticmethod
    @overload
    def indexOf(arg0: bytes, arg1: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(byte[],byte)"""
        return int._wrap(_ArrayUtils.indexOf(bytes, _byte.valueOf(arg1)))

    @staticmethod
    @overload
    def get(arg0: 'Object', arg1: int, arg2: object) -> object:
        """public static <T> T org.apache.commons.lang3.ArrayUtils.get(T[],int,T)"""
        return object._wrap(_ArrayUtils.get(arg0, _int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def removeElements(arg0: 'Object', *arg1: object) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.removeElements(T[],T...)"""
        return List[object]._wrap(_ArrayUtils.removeElements(arg0, arg1))

    @staticmethod
    @overload
    def reverse(arg0: 'int', arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(int[],int,int)"""
        _ArrayUtils.reverse(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'short', arg1: int, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(short[],short,int)"""
        return int._wrap(_ArrayUtils.lastIndexOf(arg0, _short.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def removeAll(arg0: 'Object', *arg1: int) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.removeAll(T[],int...)"""
        return List[object]._wrap(_ArrayUtils.removeAll(arg0, arg1))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'Class') -> List['type.Class']:
        """public static java.lang.Class<?>[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(java.lang.Class<?>[])"""
        return List[type.Class]._wrap(_ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def reverse(arg0: 'boolean'):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(boolean[])"""
        _ArrayUtils.reverse(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def add(arg0: 'Object', arg1: object) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.add(T[],T)"""
        return List[object]._wrap(_ArrayUtils.add(arg0, arg1))

    @staticmethod
    @overload
    def shift(arg0: 'char', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(char[],int,int,int)"""
        _ArrayUtils.shift(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'Long') -> List['Long']:
        """public static java.lang.Long[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(java.lang.Long[])"""
        return List[Long]._wrap(_ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def addAll(arg0: 'float', *arg1: float) -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.addAll(float[],float...)"""
        return List[float]._wrap(_ArrayUtils.addAll(arg0, arg1))

    @staticmethod
    @overload
    def contains(arg0: 'double', arg1: float, arg2: float) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.contains(double[],double,double)"""
        return bool._wrap(_ArrayUtils.contains(arg0, _double.valueOf(arg1), _double.valueOf(arg2)))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'short') -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(short[])"""
        return List[int]._wrap(_ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def indexesOf(arg0: bytes, arg1: int) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(byte[],byte)"""
        return BitSet._wrap(_ArrayUtils.indexesOf(bytes, _byte.valueOf(arg1)))

    @staticmethod
    @overload
    def remove(arg0: bytes, arg1: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.remove(byte[],int)"""
        return List[int]._wrap(_ArrayUtils.remove(bytes, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def indexesOf(arg0: 'char', arg1: str) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(char[],char)"""
        return BitSet._wrap(_ArrayUtils.indexesOf(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def removeAll(arg0: 'boolean', *arg1: int) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.removeAll(boolean[],int...)"""
        return List[bool]._wrap(_ArrayUtils.removeAll(arg0, arg1))

    @staticmethod
    @overload
    def shuffle(arg0: 'double'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(double[])"""
        _ArrayUtils.shuffle(arg0)

    @staticmethod
    @overload
    def isNotEmpty(arg0: 'Object') -> bool:
        """public static <T> boolean org.apache.commons.lang3.ArrayUtils.isNotEmpty(T[])"""
        return bool._wrap(_ArrayUtils.isNotEmpty(arg0))

    @staticmethod
    @overload
    def lastIndexOf(arg0: bytes, arg1: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(byte[],byte)"""
        return int._wrap(_ArrayUtils.lastIndexOf(bytes, _byte.valueOf(arg1)))

    @staticmethod
    @overload
    def shift(arg0: 'boolean', arg1: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(boolean[],int)"""
        _ArrayUtils.shift(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def removeElement(arg0: 'short', arg1: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.removeElement(short[],short)"""
        return List[int]._wrap(_ArrayUtils.removeElement(arg0, _short.valueOf(arg1)))

    @staticmethod
    @overload
    def isSameLength(arg0: 'int', arg1: 'int') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSameLength(int[],int[])"""
        return bool._wrap(_ArrayUtils.isSameLength(arg0, arg1))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Character') -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Character[])"""
        return List[str]._wrap(_ArrayUtils.toPrimitive(arg0))

    @staticmethod
    @overload
    def shift(arg0: 'double', arg1: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(double[],int)"""
        _ArrayUtils.shift(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def isSorted(arg0: 'long') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSorted(long[])"""
        return bool._wrap(_ArrayUtils.isSorted(arg0))

    @staticmethod
    @overload
    def removeElement(arg0: 'long', arg1: int) -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.removeElement(long[],long)"""
        return List[int]._wrap(_ArrayUtils.removeElement(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def indexOf(arg0: bytes, arg1: int, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(byte[],byte,int)"""
        return int._wrap(_ArrayUtils.indexOf(bytes, _byte.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def removeElement(arg0: 'Object', arg1: object) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.removeElement(T[],java.lang.Object)"""
        return List[object]._wrap(_ArrayUtils.removeElement(arg0, arg1))

    @staticmethod
    @overload
    def removeAllOccurences(arg0: 'Object', arg1: object) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.removeAllOccurences(T[],T)"""
        return List[object]._wrap(_ArrayUtils.removeAllOccurences(arg0, arg1))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'boolean', arg1: bool, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(boolean[],boolean,int)"""
        return int._wrap(_ArrayUtils.lastIndexOf(arg0, _boolean.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def indexOf(arg0: 'boolean', arg1: bool) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(boolean[],boolean)"""
        return int._wrap(_ArrayUtils.indexOf(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def isSorted(arg0: 'double') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSorted(double[])"""
        return bool._wrap(_ArrayUtils.isSorted(arg0))

    @staticmethod
    @overload
    def subarray(arg0: 'long', arg1: int, arg2: int) -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.subarray(long[],int,int)"""
        return List[int]._wrap(_ArrayUtils.subarray(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Double', arg1: float) -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Double[],double)"""
        return List[float]._wrap(_ArrayUtils.toPrimitive(arg0, _double.valueOf(arg1)))

    @staticmethod
    @overload
    def indexesOf(arg0: 'float', arg1: float) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(float[],float)"""
        return BitSet._wrap(_ArrayUtils.indexesOf(arg0, _float.valueOf(arg1)))

    @staticmethod
    @overload
    def swap(arg0: 'boolean', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(boolean[],int,int,int)"""
        _ArrayUtils.swap(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def indexesOf(arg0: bytes, arg1: int, arg2: int) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(byte[],byte,int)"""
        return BitSet._wrap(_ArrayUtils.indexesOf(bytes, _byte.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def remove(arg0: 'double', arg1: int) -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.remove(double[],int)"""
        return List[float]._wrap(_ArrayUtils.remove(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def removeElements(arg0: 'float', *arg1: float) -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.removeElements(float[],float...)"""
        return List[float]._wrap(_ArrayUtils.removeElements(arg0, arg1))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'double', arg1: float, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.lastIndexOf(double[],double,int)"""
        return int._wrap(_ArrayUtils.lastIndexOf(arg0, _double.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def indexOf(arg0: 'float', arg1: float) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(float[],float)"""
        return int._wrap(_ArrayUtils.indexOf(arg0, _float.valueOf(arg1)))

    @staticmethod
    @overload
    def add(arg0: 'double', arg1: int, arg2: float) -> List[float]:
        """public static double[] org.apache.commons.lang3.ArrayUtils.add(double[],int,double)"""
        return List[float]._wrap(_ArrayUtils.add(arg0, _int.valueOf(arg1), _double.valueOf(arg2)))

    @staticmethod
    @overload
    def isEmpty(arg0: 'long') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isEmpty(long[])"""
        return bool._wrap(_ArrayUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def contains(arg0: 'char', arg1: str) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.contains(char[],char)"""
        return bool._wrap(_ArrayUtils.contains(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def indexesOf(arg0: 'boolean', arg1: bool, arg2: int) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(boolean[],boolean,int)"""
        return BitSet._wrap(_ArrayUtils.indexesOf(arg0, _boolean.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def indexesOf(arg0: 'long', arg1: int) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(long[],long)"""
        return BitSet._wrap(_ArrayUtils.indexesOf(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def isSorted(arg0: 'int') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSorted(int[])"""
        return bool._wrap(_ArrayUtils.isSorted(arg0))

    @staticmethod
    @overload
    def isEmpty(arg0: 'Object') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isEmpty(java.lang.Object[])"""
        return bool._wrap(_ArrayUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def indexesOf(arg0: 'Object', arg1: object, arg2: int) -> 'BitSet':
        """public static java.util.BitSet org.apache.commons.lang3.ArrayUtils.indexesOf(java.lang.Object[],java.lang.Object,int)"""
        return BitSet._wrap(_ArrayUtils.indexesOf(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def removeAll(arg0: 'short', *arg1: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.removeAll(short[],int...)"""
        return List[int]._wrap(_ArrayUtils.removeAll(arg0, arg1))

    @staticmethod
    @overload
    def insert(arg0: int, arg1: 'int', *arg2: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.insert(int,int[],int...)"""
        return List[int]._wrap(_ArrayUtils.insert(_int.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def shift(arg0: 'short', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(short[],int,int,int)"""
        _ArrayUtils.shift(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def shift(arg0: 'boolean', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.shift(boolean[],int,int,int)"""
        _ArrayUtils.shift(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def toString(arg0: object) -> str:
        """public static java.lang.String org.apache.commons.lang3.ArrayUtils.toString(java.lang.Object)"""
        return str._wrap(_ArrayUtils.toString(arg0))

    @staticmethod
    @overload
    def reverse(arg0: 'char'):
        """public static void org.apache.commons.lang3.ArrayUtils.reverse(char[])"""
        _ArrayUtils.reverse(arg0)

    @staticmethod
    @overload
    def isSorted(arg0: 'float') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSorted(float[])"""
        return bool._wrap(_ArrayUtils.isSorted(arg0))

    @staticmethod
    @overload
    def remove(arg0: 'int', arg1: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.ArrayUtils.remove(int[],int)"""
        return List[int]._wrap(_ArrayUtils.remove(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def shuffle(arg0: 'float', arg1: 'Random'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(float[],java.util.Random)"""
        _ArrayUtils.shuffle(arg0, arg1)

    @staticmethod
    @overload
    def toStringArray(arg0: 'Object') -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.ArrayUtils.toStringArray(java.lang.Object[])"""
        return List[str]._wrap(_ArrayUtils.toStringArray(arg0))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'Object') -> List[object]:
        """public static java.lang.Object[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(java.lang.Object[])"""
        return List[object]._wrap(_ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def containsAny(arg0: 'Object', *arg1: object) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.containsAny(java.lang.Object[],java.lang.Object...)"""
        return bool._wrap(_ArrayUtils.containsAny(arg0, arg1))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'boolean') -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(boolean[])"""
        return List[bool]._wrap(_ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def indexOf(arg0: 'char', arg1: str, arg2: int) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.indexOf(char[],char,int)"""
        return int._wrap(_ArrayUtils.indexOf(arg0, _char.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def subarray(arg0: bytes, arg1: int, arg2: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.subarray(byte[],int,int)"""
        return List[int]._wrap(_ArrayUtils.subarray(bytes, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def clone(arg0: bytes) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.clone(byte[])"""
        return List[int]._wrap(_ArrayUtils.clone(bytes))

    @staticmethod
    @overload
    def addAll(arg0: 'short', *arg1: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.addAll(short[],short...)"""
        return List[int]._wrap(_ArrayUtils.addAll(arg0, arg1))

    @staticmethod
    @overload
    def shuffle(arg0: 'short', arg1: 'Random'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(short[],java.util.Random)"""
        _ArrayUtils.shuffle(arg0, arg1)

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.ArrayUtils()"""
        val = _ArrayUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def hashCode(arg0: object) -> int:
        """public static int org.apache.commons.lang3.ArrayUtils.hashCode(java.lang.Object)"""
        return int._wrap(_ArrayUtils.hashCode(arg0))

    @staticmethod
    @overload
    def isEmpty(arg0: 'float') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isEmpty(float[])"""
        return bool._wrap(_ArrayUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def swap(arg0: 'long', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(long[],int,int,int)"""
        _ArrayUtils.swap(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def addFirst(arg0: 'short', arg1: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.addFirst(short[],short)"""
        return List[int]._wrap(_ArrayUtils.addFirst(arg0, _short.valueOf(arg1)))

    @staticmethod
    @overload
    def isSameLength(arg0: 'long', arg1: 'long') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSameLength(long[],long[])"""
        return bool._wrap(_ArrayUtils.isSameLength(arg0, arg1))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'Short') -> List['Short']:
        """public static java.lang.Short[] org.apache.commons.lang3.ArrayUtils.nullToEmpty(java.lang.Short[])"""
        return List[Short]._wrap(_ArrayUtils.nullToEmpty(arg0))

    @staticmethod
    @overload
    def clone(arg0: 'long') -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.clone(long[])"""
        return List[int]._wrap(_ArrayUtils.clone(arg0))

    @staticmethod
    @overload
    def subarray(arg0: 'float', arg1: int, arg2: int) -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.subarray(float[],int,int)"""
        return List[float]._wrap(_ArrayUtils.subarray(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def isSameLength(arg0: 'char', arg1: 'char') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSameLength(char[],char[])"""
        return bool._wrap(_ArrayUtils.isSameLength(arg0, arg1))

    @staticmethod
    @overload
    def swap(arg0: 'float', arg1: int, arg2: int, arg3: int):
        """public static void org.apache.commons.lang3.ArrayUtils.swap(float[],int,int,int)"""
        _ArrayUtils.swap(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def addFirst(arg0: 'char', arg1: str) -> List[str]:
        """public static char[] org.apache.commons.lang3.ArrayUtils.addFirst(char[],char)"""
        return List[str]._wrap(_ArrayUtils.addFirst(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def remove(arg0: 'boolean', arg1: int) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.remove(boolean[],int)"""
        return List[bool]._wrap(_ArrayUtils.remove(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def add(arg0: 'float', arg1: float) -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.add(float[],float)"""
        return List[float]._wrap(_ArrayUtils.add(arg0, _float.valueOf(arg1)))

    @staticmethod
    @overload
    def toPrimitive(arg0: 'Byte', arg1: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.toPrimitive(java.lang.Byte[],byte)"""
        return List[int]._wrap(_ArrayUtils.toPrimitive(arg0, _byte.valueOf(arg1)))

    @staticmethod
    @overload
    def removeAllOccurrences(arg0: 'Object', arg1: object) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArrayUtils.removeAllOccurrences(T[],T)"""
        return List[object]._wrap(_ArrayUtils.removeAllOccurrences(arg0, arg1))

    @staticmethod
    @overload
    def add(arg0: bytes, arg1: int, arg2: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArrayUtils.add(byte[],int,byte)"""
        return List[int]._wrap(_ArrayUtils.add(bytes, _int.valueOf(arg1), _byte.valueOf(arg2)))

    @staticmethod
    @overload
    def shuffle(arg0: bytes, arg1: 'Random'):
        """public static void org.apache.commons.lang3.ArrayUtils.shuffle(byte[],java.util.Random)"""
        _ArrayUtils.shuffle(bytes, arg1)

    @staticmethod
    @overload
    def isNotEmpty(arg0: 'long') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isNotEmpty(long[])"""
        return bool._wrap(_ArrayUtils.isNotEmpty(arg0))

    @staticmethod
    @overload
    def contains(arg0: bytes, arg1: int) -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.contains(byte[],byte)"""
        return bool._wrap(_ArrayUtils.contains(bytes, _byte.valueOf(arg1)))

    @staticmethod
    @overload
    def isSorted(arg0: 'char') -> bool:
        """public static boolean org.apache.commons.lang3.ArrayUtils.isSorted(char[])"""
        return bool._wrap(_ArrayUtils.isSorted(arg0))

    @staticmethod
    @overload
    def subarray(arg0: 'short', arg1: int, arg2: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.subarray(short[],int,int)"""
        return List[int]._wrap(_ArrayUtils.subarray(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def removeAllOccurences(arg0: 'long', arg1: int) -> List[int]:
        """public static long[] org.apache.commons.lang3.ArrayUtils.removeAllOccurences(long[],long)"""
        return List[int]._wrap(_ArrayUtils.removeAllOccurences(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def subarray(arg0: 'boolean', arg1: int, arg2: int) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.ArrayUtils.subarray(boolean[],int,int)"""
        return List[bool]._wrap(_ArrayUtils.subarray(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def insert(arg0: int, arg1: 'short', *arg2: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.ArrayUtils.insert(int,short[],short...)"""
        return List[int]._wrap(_ArrayUtils.insert(_int.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def clone(arg0: 'float') -> List[float]:
        """public static float[] org.apache.commons.lang3.ArrayUtils.clone(float[])"""
        return List[float]._wrap(_ArrayUtils.clone(arg0))

    @staticmethod
    @overload
    def get(arg0: 'Object', arg1: int) -> object:
        """public static <T> T org.apache.commons.lang3.ArrayUtils.get(T[],int)"""
        return object._wrap(_ArrayUtils.get(arg0, _int.valueOf(arg1))) 
 
 
# CLASS: org.apache.commons.lang3.Functions$FailableFunction
import org.apache.commons.lang3.Functions as _Functions_FailableFunction
_FailableFunction = _Functions_FailableFunction.FailableFunction
from abc import abstractmethod, ABC
 
class FailableFunction():
    """org.apache.commons.lang3.Functions.FailableFunction"""
 
    @staticmethod
    def _wrap(java_value: _FailableFunction) -> 'FailableFunction':
        return FailableFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableFunction):
        """
        Dynamic initializer for FailableFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def apply(self, arg0: object):
        """public abstract R org.apache.commons.lang3.Functions$FailableFunction.apply(I) throws T"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.Validate
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.lang.CharSequence as _CharSequence
_CharSequence = _CharSequence
import java.util.Collection as Collection
import org.apache.commons.lang3.Validate as _Validate
_Validate = _Validate
import java.lang.String as _string
import java.lang.Boolean as _boolean
from builtins import bool
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.Iterable as Iterable
from builtins import object
import java.lang.Comparable as Comparable
import java.lang.String as _String
_String = _String
from typing import List
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Validate():
    """org.apache.commons.lang3.Validate"""
 
    @staticmethod
    def _wrap(java_value: _Validate) -> 'Validate':
        return Validate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Validate):
        """
        Dynamic initializer for Validate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Validate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Validate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def inclusiveBetween(arg0: float, arg1: float, arg2: float):
        """public static void org.apache.commons.lang3.Validate.inclusiveBetween(double,double,double)"""
        _Validate.inclusiveBetween(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))

    @staticmethod
    @overload
    def validState(arg0: bool, arg1: str, *arg2: object):
        """public static void org.apache.commons.lang3.Validate.validState(boolean,java.lang.String,java.lang.Object...)"""
        _Validate.validState(_boolean.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def exclusiveBetween(arg0: int, arg1: int, arg2: int, arg3: str):
        """public static void org.apache.commons.lang3.Validate.exclusiveBetween(long,long,long,java.lang.String)"""
        _Validate.exclusiveBetween(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def validIndex(arg0: 'Object', arg1: int) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.Validate.validIndex(T[],int)"""
        return List[object]._wrap(_Validate.validIndex(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def notEmpty(arg0: 'Collection', arg1: str, *arg2: object) -> 'Collection':
        """public static <T extends java.util.Collection<?>> T org.apache.commons.lang3.Validate.notEmpty(T,java.lang.String,java.lang.Object...)"""
        return Collection._wrap(_Validate.notEmpty(arg0, arg1, arg2))

    @staticmethod
    @overload
    def inclusiveBetween(arg0: int, arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.Validate.inclusiveBetween(long,long,long)"""
        _Validate.inclusiveBetween(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def notEmpty(arg0: 'CharSequence') -> 'CharSequence':
        """public static <T extends java.lang.CharSequence> T org.apache.commons.lang3.Validate.notEmpty(T)"""
        return CharSequence._wrap(_Validate.notEmpty(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def noNullElements(arg0: 'Iterable', arg1: str, *arg2: object) -> 'Iterable':
        """public static <T extends java.lang.Iterable<?>> T org.apache.commons.lang3.Validate.noNullElements(T,java.lang.String,java.lang.Object...)"""
        return Iterable._wrap(_Validate.noNullElements(arg0, arg1, arg2))

    @staticmethod
    @overload
    def isAssignableFrom(arg0: 'Class', arg1: 'Class', arg2: str, *arg3: object):
        """public static void org.apache.commons.lang3.Validate.isAssignableFrom(java.lang.Class<?>,java.lang.Class<?>,java.lang.String,java.lang.Object...)"""
        _Validate.isAssignableFrom(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def exclusiveBetween(arg0: object, arg1: object, arg2: 'Comparable'):
        """public static <T> void org.apache.commons.lang3.Validate.exclusiveBetween(T,T,java.lang.Comparable<T>)"""
        _Validate.exclusiveBetween(arg0, arg1, arg2)

    @staticmethod
    @overload
    def notEmpty(arg0: 'Collection') -> 'Collection':
        """public static <T extends java.util.Collection<?>> T org.apache.commons.lang3.Validate.notEmpty(T)"""
        return Collection._wrap(_Validate.notEmpty(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def validIndex(arg0: 'CharSequence', arg1: int, arg2: str, *arg3: object) -> 'CharSequence':
        """public static <T extends java.lang.CharSequence> T org.apache.commons.lang3.Validate.validIndex(T,int,java.lang.String,java.lang.Object...)"""
        return CharSequence._wrap(_Validate.validIndex(arg0, _int.valueOf(arg1), arg2, arg3))

    @staticmethod
    @overload
    def validIndex(arg0: 'CharSequence', arg1: int) -> 'CharSequence':
        """public static <T extends java.lang.CharSequence> T org.apache.commons.lang3.Validate.validIndex(T,int)"""
        return CharSequence._wrap(_Validate.validIndex(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def matchesPattern(arg0: 'CharSequence', arg1: str):
        """public static void org.apache.commons.lang3.Validate.matchesPattern(java.lang.CharSequence,java.lang.String)"""
        _Validate.matchesPattern(arg0, arg1)

    @staticmethod
    @overload
    def noNullElements(arg0: 'Iterable') -> 'Iterable':
        """public static <T extends java.lang.Iterable<?>> T org.apache.commons.lang3.Validate.noNullElements(T)"""
        return Iterable._wrap(_Validate.noNullElements(arg0))

    @staticmethod
    @overload
    def exclusiveBetween(arg0: float, arg1: float, arg2: float, arg3: str):
        """public static void org.apache.commons.lang3.Validate.exclusiveBetween(double,double,double,java.lang.String)"""
        _Validate.exclusiveBetween(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def notNull(arg0: object) -> object:
        """public static <T> T org.apache.commons.lang3.Validate.notNull(T)"""
        return object._wrap(_Validate.notNull(arg0))

    @staticmethod
    @overload
    def isAssignableFrom(arg0: 'Class', arg1: 'Class'):
        """public static void org.apache.commons.lang3.Validate.isAssignableFrom(java.lang.Class<?>,java.lang.Class<?>)"""
        _Validate.isAssignableFrom(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.Validate()"""
        val = _Validate()
        self.__wrapper = val

    @staticmethod
    @overload
    def isTrue(arg0: bool, arg1: str, arg2: int):
        """public static void org.apache.commons.lang3.Validate.isTrue(boolean,java.lang.String,long)"""
        _Validate.isTrue(_boolean.valueOf(arg0), arg1, _long.valueOf(arg2))

    @staticmethod
    @overload
    def notEmpty(arg0: 'Object', arg1: str, *arg2: object) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.Validate.notEmpty(T[],java.lang.String,java.lang.Object...)"""
        return List[object]._wrap(_Validate.notEmpty(arg0, arg1, arg2))

    @staticmethod
    @overload
    def finite(arg0: float, arg1: str, *arg2: object):
        """public static void org.apache.commons.lang3.Validate.finite(double,java.lang.String,java.lang.Object...)"""
        _Validate.finite(_double.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def inclusiveBetween(arg0: object, arg1: object, arg2: 'Comparable', arg3: str, *arg4: object):
        """public static <T> void org.apache.commons.lang3.Validate.inclusiveBetween(T,T,java.lang.Comparable<T>,java.lang.String,java.lang.Object...)"""
        _Validate.inclusiveBetween(arg0, arg1, arg2, arg3, arg4)

    @staticmethod
    @overload
    def matchesPattern(arg0: 'CharSequence', arg1: str, arg2: str, *arg3: object):
        """public static void org.apache.commons.lang3.Validate.matchesPattern(java.lang.CharSequence,java.lang.String,java.lang.String,java.lang.Object...)"""
        _Validate.matchesPattern(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def isTrue(arg0: bool, arg1: str, *arg2: object):
        """public static void org.apache.commons.lang3.Validate.isTrue(boolean,java.lang.String,java.lang.Object...)"""
        _Validate.isTrue(_boolean.valueOf(arg0), arg1, arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def notEmpty(arg0: 'Object') -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.Validate.notEmpty(T[])"""
        return List[object]._wrap(_Validate.notEmpty(arg0))

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

    @staticmethod
    @overload
    def isInstanceOf(arg0: 'Class', arg1: object):
        """public static void org.apache.commons.lang3.Validate.isInstanceOf(java.lang.Class<?>,java.lang.Object)"""
        _Validate.isInstanceOf(arg0, arg1)

    @staticmethod
    @overload
    def exclusiveBetween(arg0: object, arg1: object, arg2: 'Comparable', arg3: str, *arg4: object):
        """public static <T> void org.apache.commons.lang3.Validate.exclusiveBetween(T,T,java.lang.Comparable<T>,java.lang.String,java.lang.Object...)"""
        _Validate.exclusiveBetween(arg0, arg1, arg2, arg3, arg4)

    @staticmethod
    @overload
    def notBlank(arg0: 'CharSequence', arg1: str, *arg2: object) -> 'CharSequence':
        """public static <T extends java.lang.CharSequence> T org.apache.commons.lang3.Validate.notBlank(T,java.lang.String,java.lang.Object...)"""
        return CharSequence._wrap(_Validate.notBlank(arg0, arg1, arg2))

    @staticmethod
    @overload
    def notNaN(arg0: float):
        """public static void org.apache.commons.lang3.Validate.notNaN(double)"""
        _Validate.notNaN(_double.valueOf(arg0))

    @staticmethod
    @overload
    def notEmpty(arg0: 'Map', arg1: str, *arg2: object) -> 'Map':
        """public static <T extends java.util.Map<?, ?>> T org.apache.commons.lang3.Validate.notEmpty(T,java.lang.String,java.lang.Object...)"""
        return Map._wrap(_Validate.notEmpty(arg0, arg1, arg2))

    @staticmethod
    @overload
    def inclusiveBetween(arg0: object, arg1: object, arg2: 'Comparable'):
        """public static <T> void org.apache.commons.lang3.Validate.inclusiveBetween(T,T,java.lang.Comparable<T>)"""
        _Validate.inclusiveBetween(arg0, arg1, arg2)

    @staticmethod
    @overload
    def notNaN(arg0: float, arg1: str, *arg2: object):
        """public static void org.apache.commons.lang3.Validate.notNaN(double,java.lang.String,java.lang.Object...)"""
        _Validate.notNaN(_double.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def exclusiveBetween(arg0: int, arg1: int, arg2: int):
        """public static void org.apache.commons.lang3.Validate.exclusiveBetween(long,long,long)"""
        _Validate.exclusiveBetween(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def notEmpty(arg0: 'Map') -> 'Map':
        """public static <T extends java.util.Map<?, ?>> T org.apache.commons.lang3.Validate.notEmpty(T)"""
        return Map._wrap(_Validate.notEmpty(arg0))

    @staticmethod
    @overload
    def finite(arg0: float):
        """public static void org.apache.commons.lang3.Validate.finite(double)"""
        _Validate.finite(_double.valueOf(arg0))

    @staticmethod
    @overload
    def notNull(arg0: object, arg1: str, *arg2: object) -> object:
        """public static <T> T org.apache.commons.lang3.Validate.notNull(T,java.lang.String,java.lang.Object...)"""
        return object._wrap(_Validate.notNull(arg0, arg1, arg2))

    @staticmethod
    @overload
    def validState(arg0: bool):
        """public static void org.apache.commons.lang3.Validate.validState(boolean)"""
        _Validate.validState(_boolean.valueOf(arg0))

    @staticmethod
    @overload
    def notBlank(arg0: 'CharSequence') -> 'CharSequence':
        """public static <T extends java.lang.CharSequence> T org.apache.commons.lang3.Validate.notBlank(T)"""
        return CharSequence._wrap(_Validate.notBlank(arg0))

    @staticmethod
    @overload
    def inclusiveBetween(arg0: float, arg1: float, arg2: float, arg3: str):
        """public static void org.apache.commons.lang3.Validate.inclusiveBetween(double,double,double,java.lang.String)"""
        _Validate.inclusiveBetween(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def isTrue(arg0: bool, arg1: str, arg2: float):
        """public static void org.apache.commons.lang3.Validate.isTrue(boolean,java.lang.String,double)"""
        _Validate.isTrue(_boolean.valueOf(arg0), arg1, _double.valueOf(arg2))

    @staticmethod
    @overload
    def validIndex(arg0: 'Object', arg1: int, arg2: str, *arg3: object) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.Validate.validIndex(T[],int,java.lang.String,java.lang.Object...)"""
        return List[object]._wrap(_Validate.validIndex(arg0, _int.valueOf(arg1), arg2, arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def validIndex(arg0: 'Collection', arg1: int, arg2: str, *arg3: object) -> 'Collection':
        """public static <T extends java.util.Collection<?>> T org.apache.commons.lang3.Validate.validIndex(T,int,java.lang.String,java.lang.Object...)"""
        return Collection._wrap(_Validate.validIndex(arg0, _int.valueOf(arg1), arg2, arg3))

    @staticmethod
    @overload
    def validIndex(arg0: 'Collection', arg1: int) -> 'Collection':
        """public static <T extends java.util.Collection<?>> T org.apache.commons.lang3.Validate.validIndex(T,int)"""
        return Collection._wrap(_Validate.validIndex(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def noNullElements(arg0: 'Object', arg1: str, *arg2: object) -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.Validate.noNullElements(T[],java.lang.String,java.lang.Object...)"""
        return List[object]._wrap(_Validate.noNullElements(arg0, arg1, arg2))

    @staticmethod
    @overload
    def exclusiveBetween(arg0: float, arg1: float, arg2: float):
        """public static void org.apache.commons.lang3.Validate.exclusiveBetween(double,double,double)"""
        _Validate.exclusiveBetween(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))

    @staticmethod
    @overload
    def isInstanceOf(arg0: 'Class', arg1: object, arg2: str, *arg3: object):
        """public static void org.apache.commons.lang3.Validate.isInstanceOf(java.lang.Class<?>,java.lang.Object,java.lang.String,java.lang.Object...)"""
        _Validate.isInstanceOf(arg0, arg1, arg2, arg3)

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.Validate()"""
        val = _Validate()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def inclusiveBetween(arg0: int, arg1: int, arg2: int, arg3: str):
        """public static void org.apache.commons.lang3.Validate.inclusiveBetween(long,long,long,java.lang.String)"""
        _Validate.inclusiveBetween(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def notEmpty(arg0: 'CharSequence', arg1: str, *arg2: object) -> 'CharSequence':
        """public static <T extends java.lang.CharSequence> T org.apache.commons.lang3.Validate.notEmpty(T,java.lang.String,java.lang.Object...)"""
        return CharSequence._wrap(_Validate.notEmpty(arg0, arg1, arg2))

    @staticmethod
    @overload
    def isTrue(arg0: bool):
        """public static void org.apache.commons.lang3.Validate.isTrue(boolean)"""
        _Validate.isTrue(_boolean.valueOf(arg0))

    @staticmethod
    @overload
    def noNullElements(arg0: 'Object') -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.Validate.noNullElements(T[])"""
        return List[object]._wrap(_Validate.noNullElements(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.Functions$FailableConsumer
import org.apache.commons.lang3.Functions as _Functions_FailableConsumer
_FailableConsumer = _Functions_FailableConsumer.FailableConsumer
from abc import abstractmethod, ABC
 
class FailableConsumer():
    """org.apache.commons.lang3.Functions.FailableConsumer"""
 
    @staticmethod
    def _wrap(java_value: _FailableConsumer) -> 'FailableConsumer':
        return FailableConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableConsumer):
        """
        Dynamic initializer for FailableConsumer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableConsumer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableConsumer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def accept(self, arg0: object):
        """public abstract void org.apache.commons.lang3.Functions$FailableConsumer.accept(O) throws T"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.ArchUtils
from pyquantum_helper import import_once as _import_once
import org.apache.commons.lang3.ArchUtils as _ArchUtils
_ArchUtils = _ArchUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
try:
    from pyapache.lang3 import arch
except ImportError:
    arch = _import_once("pyapache.lang3.arch")

import org.apache.commons.lang3.arch.Processor as _Processor
_Processor = _Processor
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ArchUtils():
    """org.apache.commons.lang3.ArchUtils"""
 
    @staticmethod
    def _wrap(java_value: _ArchUtils) -> 'ArchUtils':
        return ArchUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ArchUtils):
        """
        Dynamic initializer for ArchUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ArchUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ArchUtils__wrapper":
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

    @staticmethod
    @overload
    def getProcessor(arg0: str) -> 'arch.Processor':
        """public static org.apache.commons.lang3.arch.Processor org.apache.commons.lang3.ArchUtils.getProcessor(java.lang.String)"""
        return arch.Processor._wrap(_ArchUtils.getProcessor(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.ArchUtils()"""
        val = _ArchUtils()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.ArchUtils()"""
        val = _ArchUtils()
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

    @staticmethod
    @overload
    def getProcessor() -> 'arch.Processor':
        """public static org.apache.commons.lang3.arch.Processor org.apache.commons.lang3.ArchUtils.getProcessor()"""
        return arch.Processor._wrap(_ArchUtils.getProcessor())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.BooleanUtils
import java.lang.Boolean as Boolean
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.Boolean as _Boolean
_Boolean = _Boolean
import java.util.function.Consumer as Consumer
from typing import List
import java.lang.String as _string
import org.apache.commons.lang3.BooleanUtils as _BooleanUtils
_BooleanUtils = _BooleanUtils
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.lang.Integer as Integer
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BooleanUtils():
    """org.apache.commons.lang3.BooleanUtils"""
 
    @staticmethod
    def _wrap(java_value: _BooleanUtils) -> 'BooleanUtils':
        return BooleanUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BooleanUtils):
        """
        Dynamic initializer for BooleanUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BooleanUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BooleanUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def negate(arg0: 'Boolean') -> 'Boolean':
        """public static java.lang.Boolean org.apache.commons.lang3.BooleanUtils.negate(java.lang.Boolean)"""
        return Boolean._wrap(_BooleanUtils.negate(arg0))

    @staticmethod
    @overload
    def isFalse(arg0: 'Boolean') -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.isFalse(java.lang.Boolean)"""
        return bool._wrap(_BooleanUtils.isFalse(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.BooleanUtils()"""
        val = _BooleanUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def toStringYesNo(arg0: 'Boolean') -> str:
        """public static java.lang.String org.apache.commons.lang3.BooleanUtils.toStringYesNo(java.lang.Boolean)"""
        return str._wrap(_BooleanUtils.toStringYesNo(arg0))

    @staticmethod
    @overload
    def isTrue(arg0: 'Boolean') -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.isTrue(java.lang.Boolean)"""
        return bool._wrap(_BooleanUtils.isTrue(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def xor(*arg0: bool) -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.xor(boolean...)"""
        return bool._wrap(_BooleanUtils.xor(arg0))

    @staticmethod
    @overload
    def toIntegerObject(toIntegerObject) -> 'Integer':
        """public static java.lang.Integer org.apache.commons.lang3.BooleanUtils.toIntegerObject(java.lang.Boolean,java.lang.Integer,java.lang.Integer,java.lang.Integer)"""
        return _transform(_arg0, arg1, arg2, arg3.BooleanUtils(arg0: 'Boolean', arg1: 'Integer', arg2: 'Integer', arg3: 'Integer')).'Integer'Value()

    @staticmethod
    @overload
    def toStringOnOff(arg0: 'Boolean') -> str:
        """public static java.lang.String org.apache.commons.lang3.BooleanUtils.toStringOnOff(java.lang.Boolean)"""
        return str._wrap(_BooleanUtils.toStringOnOff(arg0))

    @staticmethod
    @overload
    def toBooleanObject(arg0: int, arg1: int, arg2: int, arg3: int) -> 'Boolean':
        """public static java.lang.Boolean org.apache.commons.lang3.BooleanUtils.toBooleanObject(int,int,int,int)"""
        return Boolean._wrap(_BooleanUtils.toBooleanObject(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def toStringYesNo(arg0: bool) -> str:
        """public static java.lang.String org.apache.commons.lang3.BooleanUtils.toStringYesNo(boolean)"""
        return str._wrap(_BooleanUtils.toStringYesNo(_boolean.valueOf(arg0)))

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

    @staticmethod
    @overload
    def toBooleanObject(arg0: 'Integer') -> 'Boolean':
        """public static java.lang.Boolean org.apache.commons.lang3.BooleanUtils.toBooleanObject(java.lang.Integer)"""
        return Boolean._wrap(_BooleanUtils.toBooleanObject(arg0))

    @staticmethod
    @overload
    def toBoolean(arg0: 'Boolean') -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.toBoolean(java.lang.Boolean)"""
        return bool._wrap(_BooleanUtils.toBoolean(arg0))

    @staticmethod
    @overload
    def toBooleanDefaultIfNull(arg0: 'Boolean', arg1: bool) -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.toBooleanDefaultIfNull(java.lang.Boolean,boolean)"""
        return bool._wrap(_BooleanUtils.toBooleanDefaultIfNull(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def toInteger(arg0: 'Boolean', arg1: int, arg2: int, arg3: int) -> int:
        """public static int org.apache.commons.lang3.BooleanUtils.toInteger(java.lang.Boolean,int,int,int)"""
        return int._wrap(_BooleanUtils.toInteger(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def toBooleanObject(arg0: str) -> 'Boolean':
        """public static java.lang.Boolean org.apache.commons.lang3.BooleanUtils.toBooleanObject(java.lang.String)"""
        return Boolean._wrap(_BooleanUtils.toBooleanObject(arg0))

    @staticmethod
    @overload
    def values() -> 'List':
        """public static java.util.List<java.lang.Boolean> org.apache.commons.lang3.BooleanUtils.values()"""
        return List._wrap(_BooleanUtils.values())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.BooleanUtils()"""
        val = _BooleanUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def toIntegerObject(toIntegerObject) -> 'Integer':
        """public static java.lang.Integer org.apache.commons.lang3.BooleanUtils.toIntegerObject(boolean)"""
        return _transform(__boolean.valueOf(arg0).BooleanUtils(arg0: bool)).'Integer'Value()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def xor(*arg0: 'Boolean') -> 'Boolean':
        """public static java.lang.Boolean org.apache.commons.lang3.BooleanUtils.xor(java.lang.Boolean...)"""
        return Boolean._wrap(_BooleanUtils.xor(arg0))

    @staticmethod
    @overload
    def forEach(arg0: 'Consumer'):
        """public static void org.apache.commons.lang3.BooleanUtils.forEach(java.util.function.Consumer<java.lang.Boolean>)"""
        _BooleanUtils.forEach(arg0)

    @staticmethod
    @overload
    def or(*arg0: 'Boolean') -> 'Boolean':
        """public static java.lang.Boolean org.apache.commons.lang3.BooleanUtils.or(java.lang.Boolean...)"""
        return Boolean._wrap(_BooleanUtils.or(arg0))

    @staticmethod
    @overload
    def toBooleanObject(arg0: int) -> 'Boolean':
        """public static java.lang.Boolean org.apache.commons.lang3.BooleanUtils.toBooleanObject(int)"""
        return Boolean._wrap(_BooleanUtils.toBooleanObject(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def toIntegerObject(toIntegerObject) -> 'Integer':
        """public static java.lang.Integer org.apache.commons.lang3.BooleanUtils.toIntegerObject(boolean,java.lang.Integer,java.lang.Integer)"""
        return _transform(__boolean.valueOf(arg0), arg1, arg2.BooleanUtils(arg0: bool, arg1: 'Integer', arg2: 'Integer')).'Integer'Value()

    @staticmethod
    @overload
    def toStringOnOff(arg0: bool) -> str:
        """public static java.lang.String org.apache.commons.lang3.BooleanUtils.toStringOnOff(boolean)"""
        return str._wrap(_BooleanUtils.toStringOnOff(_boolean.valueOf(arg0)))

    @staticmethod
    @overload
    def toString(arg0: 'Boolean', arg1: str, arg2: str, arg3: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.BooleanUtils.toString(java.lang.Boolean,java.lang.String,java.lang.String,java.lang.String)"""
        return str._wrap(_BooleanUtils.toString(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def primitiveValues() -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.BooleanUtils.primitiveValues()"""
        return List[bool]._wrap(_BooleanUtils.primitiveValues())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def and(*arg0: bool) -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.and(boolean...)"""
        return bool._wrap(_BooleanUtils.and(arg0))

    @staticmethod
    @overload
    def toBooleanObject(arg0: 'Integer', arg1: 'Integer', arg2: 'Integer', arg3: 'Integer') -> 'Boolean':
        """public static java.lang.Boolean org.apache.commons.lang3.BooleanUtils.toBooleanObject(java.lang.Integer,java.lang.Integer,java.lang.Integer,java.lang.Integer)"""
        return Boolean._wrap(_BooleanUtils.toBooleanObject(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def toBoolean(arg0: int) -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.toBoolean(int)"""
        return bool._wrap(_BooleanUtils.toBoolean(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def toInteger(arg0: bool) -> int:
        """public static int org.apache.commons.lang3.BooleanUtils.toInteger(boolean)"""
        return int._wrap(_BooleanUtils.toInteger(_boolean.valueOf(arg0)))

    @staticmethod
    @overload
    def toBoolean(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.toBoolean(java.lang.String)"""
        return bool._wrap(_BooleanUtils.toBoolean(arg0))

    @staticmethod
    @overload
    def compare(arg0: bool, arg1: bool) -> int:
        """public static int org.apache.commons.lang3.BooleanUtils.compare(boolean,boolean)"""
        return int._wrap(_BooleanUtils.compare(_boolean.valueOf(arg0), _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def isNotFalse(arg0: 'Boolean') -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.isNotFalse(java.lang.Boolean)"""
        return bool._wrap(_BooleanUtils.isNotFalse(arg0))

    @staticmethod
    @overload
    def toStringTrueFalse(arg0: 'Boolean') -> str:
        """public static java.lang.String org.apache.commons.lang3.BooleanUtils.toStringTrueFalse(java.lang.Boolean)"""
        return str._wrap(_BooleanUtils.toStringTrueFalse(arg0))

    @staticmethod
    @overload
    def isNotTrue(arg0: 'Boolean') -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.isNotTrue(java.lang.Boolean)"""
        return bool._wrap(_BooleanUtils.isNotTrue(arg0))

    @staticmethod
    @overload
    def toInteger(arg0: bool, arg1: int, arg2: int) -> int:
        """public static int org.apache.commons.lang3.BooleanUtils.toInteger(boolean,int,int)"""
        return int._wrap(_BooleanUtils.toInteger(_boolean.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def toBooleanObject(arg0: str, arg1: str, arg2: str, arg3: str) -> 'Boolean':
        """public static java.lang.Boolean org.apache.commons.lang3.BooleanUtils.toBooleanObject(java.lang.String,java.lang.String,java.lang.String,java.lang.String)"""
        return Boolean._wrap(_BooleanUtils.toBooleanObject(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def or(*arg0: bool) -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.or(boolean...)"""
        return bool._wrap(_BooleanUtils.or(arg0))

    @staticmethod
    @overload
    def toBoolean(arg0: str, arg1: str, arg2: str) -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.toBoolean(java.lang.String,java.lang.String,java.lang.String)"""
        return bool._wrap(_BooleanUtils.toBoolean(arg0, arg1, arg2))

    @staticmethod
    @overload
    def toStringTrueFalse(arg0: bool) -> str:
        """public static java.lang.String org.apache.commons.lang3.BooleanUtils.toStringTrueFalse(boolean)"""
        return str._wrap(_BooleanUtils.toStringTrueFalse(_boolean.valueOf(arg0)))

    @staticmethod
    @overload
    def and(*arg0: 'Boolean') -> 'Boolean':
        """public static java.lang.Boolean org.apache.commons.lang3.BooleanUtils.and(java.lang.Boolean...)"""
        return Boolean._wrap(_BooleanUtils.and(arg0))

    @staticmethod
    @overload
    def oneHot(*arg0: bool) -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.oneHot(boolean...)"""
        return bool._wrap(_BooleanUtils.oneHot(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def toBoolean(arg0: int, arg1: int, arg2: int) -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.toBoolean(int,int,int)"""
        return bool._wrap(_BooleanUtils.toBoolean(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def oneHot(*arg0: 'Boolean') -> 'Boolean':
        """public static java.lang.Boolean org.apache.commons.lang3.BooleanUtils.oneHot(java.lang.Boolean...)"""
        return Boolean._wrap(_BooleanUtils.oneHot(arg0))

    @staticmethod
    @overload
    def booleanValues() -> List['Boolean']:
        """public static java.lang.Boolean[] org.apache.commons.lang3.BooleanUtils.booleanValues()"""
        return List[Boolean]._wrap(_BooleanUtils.booleanValues())

    @staticmethod
    @overload
    def toIntegerObject(toIntegerObject) -> 'Integer':
        """public static java.lang.Integer org.apache.commons.lang3.BooleanUtils.toIntegerObject(java.lang.Boolean)"""
        return _transform(_arg0.BooleanUtils(arg0: 'Boolean')).'Integer'Value()

    @staticmethod
    @overload
    def toBoolean(arg0: 'Integer', arg1: 'Integer', arg2: 'Integer') -> bool:
        """public static boolean org.apache.commons.lang3.BooleanUtils.toBoolean(java.lang.Integer,java.lang.Integer,java.lang.Integer)"""
        return bool._wrap(_BooleanUtils.toBoolean(arg0, arg1, arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def toString(arg0: bool, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.BooleanUtils.toString(boolean,java.lang.String,java.lang.String)"""
        return str._wrap(_BooleanUtils.toString(_boolean.valueOf(arg0), arg1, arg2)) 
 
 
# CLASS: org.apache.commons.lang3.IntegerRange
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Comparable as Comparable
from builtins import object
import java.lang.String as _string
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.lang.Integer as Integer
import org.apache.commons.lang3.Range as _Range
_Range = _Range
import org.apache.commons.lang3.IntegerRange as _IntegerRange
_IntegerRange = _IntegerRange
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IntegerRange():
    """org.apache.commons.lang3.IntegerRange"""
 
    @staticmethod
    def _wrap(java_value: _IntegerRange) -> 'IntegerRange':
        return IntegerRange(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IntegerRange):
        """
        Dynamic initializer for IntegerRange.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IntegerRange__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IntegerRange__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def intersectionWith(self, arg0: 'Range') -> 'Range':
        """public org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.intersectionWith(org.apache.commons.lang3.Range<T>)"""
        return 'Range'._wrap(super(_Range, self).intersectionWith(arg0))

    @staticmethod
    @overload
    def of(arg0: int, arg1: int) -> 'IntegerRange':
        """public static org.apache.commons.lang3.IntegerRange org.apache.commons.lang3.IntegerRange.of(int,int)"""
        return IntegerRange._wrap(_IntegerRange.of(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def isBeforeRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isBeforeRange(org.apache.commons.lang3.Range<T>)"""
        return bool._wrap(super(_Range, self).isBeforeRange(arg0))

    @staticmethod
    @overload
    def is(arg0: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.is(T)"""
        return Range._wrap(_Range.is(arg0))

    @overload
    def isAfter(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isAfter(T)"""
        return bool._wrap(super(_Range, self).isAfter(arg0))

    @overload
    def containsRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.containsRange(org.apache.commons.lang3.Range<T>)"""
        return bool._wrap(super(_Range, self).containsRange(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.Range.toString()"""
        return str._wrap(super(Range, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.Range.hashCode()"""
        return int._wrap(super(Range, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isNaturalOrdering(self) -> bool:
        """public boolean org.apache.commons.lang3.Range.isNaturalOrdering()"""
        return bool._wrap(super(Range, self).isNaturalOrdering())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def isEndedBy(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isEndedBy(T)"""
        return bool._wrap(super(_Range, self).isEndedBy(arg0))

    @staticmethod
    @overload
    def of(arg0: 'Integer', arg1: 'Integer') -> 'IntegerRange':
        """public static org.apache.commons.lang3.IntegerRange org.apache.commons.lang3.IntegerRange.of(java.lang.Integer,java.lang.Integer)"""
        return IntegerRange._wrap(_IntegerRange.of(arg0, arg1))

    @overload
    def elementCompareTo(self, arg0: object) -> int:
        """public int org.apache.commons.lang3.Range.elementCompareTo(T)"""
        return int._wrap(super(_Range, self).elementCompareTo(arg0))

    @override
    @overload
    def getComparator(self) -> 'Comparator':
        """public java.util.Comparator<T> org.apache.commons.lang3.Range.getComparator()"""
        return 'Comparator'._wrap(super(Range, self).getComparator())

    @overload
    def isStartedBy(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isStartedBy(T)"""
        return bool._wrap(super(_Range, self).isStartedBy(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.equals(java.lang.Object)"""
        return bool._wrap(super(_Range, self).equals(arg0))

    @overload
    def isBefore(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isBefore(T)"""
        return bool._wrap(super(_Range, self).isBefore(arg0))

    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.of(T,T,java.util.Comparator<T>)"""
        return Range._wrap(_Range.of(arg0, arg1, arg2))

    @staticmethod
    @overload
    def between(arg0: object, arg1: object, arg2: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.between(T,T,java.util.Comparator<T>)"""
        return Range._wrap(_Range.between(arg0, arg1, arg2))

    @overload
    def isAfterRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isAfterRange(org.apache.commons.lang3.Range<T>)"""
        return bool._wrap(super(_Range, self).isAfterRange(arg0))

    @staticmethod
    @overload
    def between(arg0: 'Comparable', arg1: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.between(T,T)"""
        return Range._wrap(_Range.between(arg0, arg1))

    @override
    @overload
    def getMaximum(self) -> object:
        """public T org.apache.commons.lang3.Range.getMaximum()"""
        return object._wrap(super(Range, self).getMaximum())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.contains(T)"""
        return bool._wrap(super(_Range, self).contains(arg0))

    @staticmethod
    @overload
    def of(arg0: 'Comparable', arg1: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.of(T,T)"""
        return Range._wrap(_Range.of(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def fit(self, arg0: object) -> object:
        """public T org.apache.commons.lang3.Range.fit(T)"""
        return object._wrap(super(_Range, self).fit(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.Range.toString(java.lang.String)"""
        return str._wrap(super(_Range, self).toString(arg0))

    @override
    @overload
    def getMinimum(self) -> object:
        """public T org.apache.commons.lang3.Range.getMinimum()"""
        return object._wrap(super(Range, self).getMinimum())

    @overload
    def isOverlappedBy(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isOverlappedBy(org.apache.commons.lang3.Range<T>)"""
        return bool._wrap(super(_Range, self).isOverlappedBy(arg0))

    @staticmethod
    @overload
    def is(arg0: object, arg1: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.is(T,java.util.Comparator<T>)"""
        return Range._wrap(_Range.is(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.lang3.Functions$FailableCallable
import org.apache.commons.lang3.Functions as _Functions_FailableCallable
_FailableCallable = _Functions_FailableCallable.FailableCallable
from abc import abstractmethod, ABC
 
class FailableCallable():
    """org.apache.commons.lang3.Functions.FailableCallable"""
 
    @staticmethod
    def _wrap(java_value: _FailableCallable) -> 'FailableCallable':
        return FailableCallable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableCallable):
        """
        Dynamic initializer for FailableCallable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableCallable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableCallable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def call(self, ):
        """public abstract R org.apache.commons.lang3.Functions$FailableCallable.call() throws T"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.Functions$FailableSupplier
from abc import abstractmethod, ABC
import org.apache.commons.lang3.Functions as _Functions_FailableSupplier
_FailableSupplier = _Functions_FailableSupplier.FailableSupplier
 
class FailableSupplier():
    """org.apache.commons.lang3.Functions.FailableSupplier"""
 
    @staticmethod
    def _wrap(java_value: _FailableSupplier) -> 'FailableSupplier':
        return FailableSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableSupplier):
        """
        Dynamic initializer for FailableSupplier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableSupplier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableSupplier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def get(self, ):
        """public abstract R org.apache.commons.lang3.Functions$FailableSupplier.get() throws T"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.SystemProperties
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.function.BooleanSupplier as BooleanSupplier
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import java.util.function.IntSupplier as IntSupplier
import org.apache.commons.lang3.SystemProperties as _SystemProperties
_SystemProperties = _SystemProperties
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.function.LongSupplier as LongSupplier
import java.lang.Class as _Class
_Class = _Class
 
class SystemProperties():
    """org.apache.commons.lang3.SystemProperties"""
 
    @staticmethod
    def _wrap(java_value: _SystemProperties) -> 'SystemProperties':
        return SystemProperties(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SystemProperties):
        """
        Dynamic initializer for SystemProperties.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SystemProperties__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SystemProperties__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getJavaExtDirs() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaExtDirs()"""
        return str._wrap(_SystemProperties.getJavaExtDirs())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getJavaRuntimeVersion() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaRuntimeVersion()"""
        return str._wrap(_SystemProperties.getJavaRuntimeVersion())

    @staticmethod
    @overload
    def getFileEncoding() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getFileEncoding()"""
        return str._wrap(_SystemProperties.getFileEncoding())

    @staticmethod
    @overload
    def getJavaVersion() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaVersion()"""
        return str._wrap(_SystemProperties.getJavaVersion())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def getJavaLocaleProviders() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaLocaleProviders()"""
        return str._wrap(_SystemProperties.getJavaLocaleProviders())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getJavaSpecificationVersion() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaSpecificationVersion()"""
        return str._wrap(_SystemProperties.getJavaSpecificationVersion())

    @staticmethod
    @overload
    def getJavaHome() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaHome()"""
        return str._wrap(_SystemProperties.getJavaHome())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def getJavaAwtHeadless() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaAwtHeadless()"""
        return str._wrap(_SystemProperties.getJavaAwtHeadless())

    @staticmethod
    @overload
    def getJavaClassVersion() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaClassVersion()"""
        return str._wrap(_SystemProperties.getJavaClassVersion())

    @staticmethod
    @overload
    def getOsArch() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getOsArch()"""
        return str._wrap(_SystemProperties.getOsArch())

    @staticmethod
    @overload
    def getJavaCompiler() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaCompiler()"""
        return str._wrap(_SystemProperties.getJavaCompiler())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getUserName() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getUserName()"""
        return str._wrap(_SystemProperties.getUserName())

    @staticmethod
    @overload
    def getJavaClassPath() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaClassPath()"""
        return str._wrap(_SystemProperties.getJavaClassPath())

    @staticmethod
    @overload
    def getUserHome() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getUserHome()"""
        return str._wrap(_SystemProperties.getUserHome())

    @staticmethod
    @overload
    def getJavaEndorsedDirs() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaEndorsedDirs()"""
        return str._wrap(_SystemProperties.getJavaEndorsedDirs())

    @staticmethod
    @overload
    def getProperty(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getProperty(java.lang.String)"""
        return str._wrap(_SystemProperties.getProperty(arg0))

    @staticmethod
    @overload
    def getUserTimezone() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getUserTimezone()"""
        return str._wrap(_SystemProperties.getUserTimezone())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getJavaVmSpecificationVendor() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaVmSpecificationVendor()"""
        return str._wrap(_SystemProperties.getJavaVmSpecificationVendor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.SystemProperties()"""
        val = _SystemProperties()
        self.__wrapper = val

    @staticmethod
    @overload
    def getJavaAwtFonts() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaAwtFonts()"""
        return str._wrap(_SystemProperties.getJavaAwtFonts())

    @staticmethod
    @overload
    def getJavaAwtGraphicsenv() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaAwtGraphicsenv()"""
        return str._wrap(_SystemProperties.getJavaAwtGraphicsenv())

    @staticmethod
    @overload
    def getJavaVmSpecificationName() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaVmSpecificationName()"""
        return str._wrap(_SystemProperties.getJavaVmSpecificationName())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.SystemProperties()"""
        val = _SystemProperties()
        self.__wrapper = val

    @staticmethod
    @overload
    def getJavaAwtPrinterjob() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaAwtPrinterjob()"""
        return str._wrap(_SystemProperties.getJavaAwtPrinterjob())

    @staticmethod
    @overload
    def getJavaVmVendor() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaVmVendor()"""
        return str._wrap(_SystemProperties.getJavaVmVendor())

    @staticmethod
    @overload
    def getJavaVmSpecificationVersion() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaVmSpecificationVersion()"""
        return str._wrap(_SystemProperties.getJavaVmSpecificationVersion())

    @staticmethod
    @overload
    def getJavaVmVersion() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaVmVersion()"""
        return str._wrap(_SystemProperties.getJavaVmVersion())

    @staticmethod
    @overload
    def getUserCountry() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getUserCountry()"""
        return str._wrap(_SystemProperties.getUserCountry())

    @staticmethod
    @overload
    def getJavaVmName() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaVmName()"""
        return str._wrap(_SystemProperties.getJavaVmName())

    @staticmethod
    @overload
    def getJavaVmInfo() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaVmInfo()"""
        return str._wrap(_SystemProperties.getJavaVmInfo())

    @staticmethod
    @overload
    def getJavaRuntimeName() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaRuntimeName()"""
        return str._wrap(_SystemProperties.getJavaRuntimeName())

    @staticmethod
    @overload
    def getOsVersion() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getOsVersion()"""
        return str._wrap(_SystemProperties.getOsVersion())

    @staticmethod
    @overload
    def getBoolean(arg0: str, arg1: 'BooleanSupplier') -> bool:
        """public static boolean org.apache.commons.lang3.SystemProperties.getBoolean(java.lang.String,java.util.function.BooleanSupplier)"""
        return bool._wrap(_SystemProperties.getBoolean(arg0, arg1))

    @staticmethod
    @overload
    def getJavaLibraryPath() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaLibraryPath()"""
        return str._wrap(_SystemProperties.getJavaLibraryPath())

    @staticmethod
    @overload
    def getJavaIoTmpdir() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaIoTmpdir()"""
        return str._wrap(_SystemProperties.getJavaIoTmpdir())

    @staticmethod
    @overload
    def getJavaSpecificationName() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaSpecificationName()"""
        return str._wrap(_SystemProperties.getJavaSpecificationName())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getUserDir() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getUserDir()"""
        return str._wrap(_SystemProperties.getUserDir())

    @staticmethod
    @overload
    def getAwtToolkit() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getAwtToolkit()"""
        return str._wrap(_SystemProperties.getAwtToolkit())

    @staticmethod
    @overload
    def getJavaVendor() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaVendor()"""
        return str._wrap(_SystemProperties.getJavaVendor())

    @staticmethod
    @overload
    def getJavaSpecificationVendor() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaSpecificationVendor()"""
        return str._wrap(_SystemProperties.getJavaSpecificationVendor())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getPathSeparator() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getPathSeparator()"""
        return str._wrap(_SystemProperties.getPathSeparator())

    @staticmethod
    @overload
    def getLineSeparator() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getLineSeparator()"""
        return str._wrap(_SystemProperties.getLineSeparator())

    @staticmethod
    @overload
    def getOsName() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getOsName()"""
        return str._wrap(_SystemProperties.getOsName())

    @staticmethod
    @overload
    def getUserLanguage() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getUserLanguage()"""
        return str._wrap(_SystemProperties.getUserLanguage())

    @staticmethod
    @overload
    def getJavaUtilPrefsPreferencesFactory() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaUtilPrefsPreferencesFactory()"""
        return str._wrap(_SystemProperties.getJavaUtilPrefsPreferencesFactory())

    @staticmethod
    @overload
    def getJavaVendorUrl() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getJavaVendorUrl()"""
        return str._wrap(_SystemProperties.getJavaVendorUrl())

    @staticmethod
    @overload
    def getInt(arg0: str, arg1: 'IntSupplier') -> int:
        """public static int org.apache.commons.lang3.SystemProperties.getInt(java.lang.String,java.util.function.IntSupplier)"""
        return int._wrap(_SystemProperties.getInt(arg0, arg1))

    @staticmethod
    @overload
    def getLong(arg0: str, arg1: 'LongSupplier') -> int:
        """public static long org.apache.commons.lang3.SystemProperties.getLong(java.lang.String,java.util.function.LongSupplier)"""
        return int._wrap(_SystemProperties.getLong(arg0, arg1))

    @staticmethod
    @overload
    def getFileSeparator() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemProperties.getFileSeparator()"""
        return str._wrap(_SystemProperties.getFileSeparator()) 
 
 
# CLASS: org.apache.commons.lang3.LongRange
from builtins import str
import java.lang.Long as Long
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Comparable as Comparable
from builtins import object
import org.apache.commons.lang3.LongRange as _LongRange
_LongRange = _LongRange
import java.lang.String as _string
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import org.apache.commons.lang3.Range as _Range
_Range = _Range
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LongRange():
    """org.apache.commons.lang3.LongRange"""
 
    @staticmethod
    def _wrap(java_value: _LongRange) -> 'LongRange':
        return LongRange(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LongRange):
        """
        Dynamic initializer for LongRange.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LongRange__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LongRange__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def intersectionWith(self, arg0: 'Range') -> 'Range':
        """public org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.intersectionWith(org.apache.commons.lang3.Range<T>)"""
        return 'Range'._wrap(super(_Range, self).intersectionWith(arg0))

    @overload
    def isBeforeRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isBeforeRange(org.apache.commons.lang3.Range<T>)"""
        return bool._wrap(super(_Range, self).isBeforeRange(arg0))

    @staticmethod
    @overload
    def is(arg0: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.is(T)"""
        return Range._wrap(_Range.is(arg0))

    @overload
    def isAfter(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isAfter(T)"""
        return bool._wrap(super(_Range, self).isAfter(arg0))

    @overload
    def containsRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.containsRange(org.apache.commons.lang3.Range<T>)"""
        return bool._wrap(super(_Range, self).containsRange(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def of(arg0: 'Long', arg1: 'Long') -> 'LongRange':
        """public static org.apache.commons.lang3.LongRange org.apache.commons.lang3.LongRange.of(java.lang.Long,java.lang.Long)"""
        return LongRange._wrap(_LongRange.of(arg0, arg1))

    @staticmethod
    @overload
    def of(arg0: int, arg1: int) -> 'LongRange':
        """public static org.apache.commons.lang3.LongRange org.apache.commons.lang3.LongRange.of(long,long)"""
        return LongRange._wrap(_LongRange.of(_long.valueOf(arg0), _long.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.Range.toString()"""
        return str._wrap(super(Range, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.Range.hashCode()"""
        return int._wrap(super(Range, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isNaturalOrdering(self) -> bool:
        """public boolean org.apache.commons.lang3.Range.isNaturalOrdering()"""
        return bool._wrap(super(Range, self).isNaturalOrdering())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def isEndedBy(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isEndedBy(T)"""
        return bool._wrap(super(_Range, self).isEndedBy(arg0))

    @overload
    def elementCompareTo(self, arg0: object) -> int:
        """public int org.apache.commons.lang3.Range.elementCompareTo(T)"""
        return int._wrap(super(_Range, self).elementCompareTo(arg0))

    @override
    @overload
    def getComparator(self) -> 'Comparator':
        """public java.util.Comparator<T> org.apache.commons.lang3.Range.getComparator()"""
        return 'Comparator'._wrap(super(Range, self).getComparator())

    @overload
    def isStartedBy(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isStartedBy(T)"""
        return bool._wrap(super(_Range, self).isStartedBy(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.equals(java.lang.Object)"""
        return bool._wrap(super(_Range, self).equals(arg0))

    @overload
    def isBefore(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isBefore(T)"""
        return bool._wrap(super(_Range, self).isBefore(arg0))

    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.of(T,T,java.util.Comparator<T>)"""
        return Range._wrap(_Range.of(arg0, arg1, arg2))

    @staticmethod
    @overload
    def between(arg0: object, arg1: object, arg2: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.between(T,T,java.util.Comparator<T>)"""
        return Range._wrap(_Range.between(arg0, arg1, arg2))

    @overload
    def isAfterRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isAfterRange(org.apache.commons.lang3.Range<T>)"""
        return bool._wrap(super(_Range, self).isAfterRange(arg0))

    @staticmethod
    @overload
    def between(arg0: 'Comparable', arg1: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.between(T,T)"""
        return Range._wrap(_Range.between(arg0, arg1))

    @override
    @overload
    def getMaximum(self) -> object:
        """public T org.apache.commons.lang3.Range.getMaximum()"""
        return object._wrap(super(Range, self).getMaximum())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.contains(T)"""
        return bool._wrap(super(_Range, self).contains(arg0))

    @staticmethod
    @overload
    def of(arg0: 'Comparable', arg1: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.of(T,T)"""
        return Range._wrap(_Range.of(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def fit(self, arg0: object) -> object:
        """public T org.apache.commons.lang3.Range.fit(T)"""
        return object._wrap(super(_Range, self).fit(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.Range.toString(java.lang.String)"""
        return str._wrap(super(_Range, self).toString(arg0))

    @override
    @overload
    def getMinimum(self) -> object:
        """public T org.apache.commons.lang3.Range.getMinimum()"""
        return object._wrap(super(Range, self).getMinimum())

    @overload
    def isOverlappedBy(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isOverlappedBy(org.apache.commons.lang3.Range<T>)"""
        return bool._wrap(super(_Range, self).isOverlappedBy(arg0))

    @staticmethod
    @overload
    def is(arg0: object, arg1: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.is(T,java.util.Comparator<T>)"""
        return Range._wrap(_Range.is(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.lang3.AnnotationUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import java.lang.annotation.Annotation as Annotation
import org.apache.commons.lang3.AnnotationUtils as _AnnotationUtils
_AnnotationUtils = _AnnotationUtils
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AnnotationUtils():
    """org.apache.commons.lang3.AnnotationUtils"""
 
    @staticmethod
    def _wrap(java_value: _AnnotationUtils) -> 'AnnotationUtils':
        return AnnotationUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AnnotationUtils):
        """
        Dynamic initializer for AnnotationUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AnnotationUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AnnotationUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def isValidAnnotationMemberType(arg0: 'Class') -> bool:
        """public static boolean org.apache.commons.lang3.AnnotationUtils.isValidAnnotationMemberType(java.lang.Class<?>)"""
        return bool._wrap(_AnnotationUtils.isValidAnnotationMemberType(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.AnnotationUtils()"""
        val = _AnnotationUtils()
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

    @staticmethod
    @overload
    def equals(arg0: 'Annotation', arg1: 'Annotation') -> bool:
        """public static boolean org.apache.commons.lang3.AnnotationUtils.equals(java.lang.annotation.Annotation,java.lang.annotation.Annotation)"""
        return bool._wrap(_AnnotationUtils.equals(arg0, arg1))

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

    @staticmethod
    @overload
    def hashCode(arg0: 'Annotation') -> int:
        """public static int org.apache.commons.lang3.AnnotationUtils.hashCode(java.lang.annotation.Annotation)"""
        return int._wrap(_AnnotationUtils.hashCode(arg0))

    @staticmethod
    @overload
    def toString(arg0: 'Annotation') -> str:
        """public static java.lang.String org.apache.commons.lang3.AnnotationUtils.toString(java.lang.annotation.Annotation)"""
        return str._wrap(_AnnotationUtils.toString(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.AnnotationUtils()"""
        val = _AnnotationUtils()
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
 
 
# CLASS: org.apache.commons.lang3.Functions
import java.util.function.Predicate as Predicate
import java.util.function.Supplier as Supplier
import java.util.function.Function as _Function
_Function = _Function
import java.lang.Object as _Object
_Object = _Object
import java.util.function.BiFunction as _BiFunction
_BiFunction = _BiFunction
from builtins import type
import java.util.Collection as Collection
import org.apache.commons.lang3.Functions as _Functions
_Functions = _Functions
import java.util.function.Consumer as Consumer
import java.lang.RuntimeException as RuntimeException
import java.util.concurrent.Callable as Callable
from builtins import bool
import java.util.function.Supplier as _Supplier
_Supplier = _Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.Runnable as Runnable
import java.util.function.BiConsumer as _BiConsumer
_BiConsumer = _BiConsumer
from builtins import object
import org.apache.commons.lang3.Streams as _Streams_FailableStream
_FailableStream = _Streams_FailableStream.FailableStream
import java.lang.String as _String
_String = _String
import java.util.function.Predicate as _Predicate
_Predicate = _Predicate
import java.util.function.BiFunction as BiFunction
import java.util.function.Consumer as _Consumer
_Consumer = _Consumer
import java.lang.RuntimeException as _RuntimeException
_RuntimeException = _RuntimeException
import java.util.function.BiConsumer as BiConsumer
import java.lang.Integer as _int
import java.util.function.BiPredicate as BiPredicate
import java.util.function.BiPredicate as _BiPredicate
_BiPredicate = _BiPredicate
import java.lang.Runnable as _Runnable
_Runnable = _Runnable
import java.util.concurrent.Callable as _Callable
_Callable = _Callable
import java.util.stream.Stream as Stream
import java.lang.Throwable as Throwable
import java.util.function.Function as Function
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Functions():
    """org.apache.commons.lang3.Functions"""
 
    @staticmethod
    def _wrap(java_value: _Functions) -> 'Functions':
        return Functions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Functions):
        """
        Dynamic initializer for Functions.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Functions__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Functions__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def asBiConsumer(arg0: 'FailableBiConsumer') -> 'BiConsumer':
        """public static <O1,O2> java.util.function.BiConsumer<O1, O2> org.apache.commons.lang3.Functions.asBiConsumer(org.apache.commons.lang3.Functions$FailableBiConsumer<O1, O2, ?>)"""
        return BiConsumer._wrap(_Functions.asBiConsumer(arg0))

    @staticmethod
    @overload
    def asFunction(arg0: 'FailableFunction') -> 'Function':
        """public static <I,O> java.util.function.Function<I, O> org.apache.commons.lang3.Functions.asFunction(org.apache.commons.lang3.Functions$FailableFunction<I, O, ?>)"""
        return Function._wrap(_Functions.asFunction(arg0))

    @staticmethod
    @overload
    def asPredicate(arg0: 'FailablePredicate') -> 'Predicate':
        """public static <I> java.util.function.Predicate<I> org.apache.commons.lang3.Functions.asPredicate(org.apache.commons.lang3.Functions$FailablePredicate<I, ?>)"""
        return Predicate._wrap(_Functions.asPredicate(arg0))

    @staticmethod
    @overload
    def stream(arg0: 'Collection') -> 'FailableStream':
        """public static <O> org.apache.commons.lang3.Streams$FailableStream<O> org.apache.commons.lang3.Functions.stream(java.util.Collection<O>)"""
        return FailableStream._wrap(_Functions.stream(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def accept(arg0: 'FailableConsumer', arg1: object):
        """public static <O,T extends java.lang.Throwable> void org.apache.commons.lang3.Functions.accept(org.apache.commons.lang3.Functions$FailableConsumer<O, T>,O)"""
        _Functions.accept(arg0, arg1)

    @staticmethod
    @overload
    def asBiPredicate(arg0: 'FailableBiPredicate') -> 'BiPredicate':
        """public static <O1,O2> java.util.function.BiPredicate<O1, O2> org.apache.commons.lang3.Functions.asBiPredicate(org.apache.commons.lang3.Functions$FailableBiPredicate<O1, O2, ?>)"""
        return BiPredicate._wrap(_Functions.asBiPredicate(arg0))

    @staticmethod
    @overload
    def run(arg0: 'FailableRunnable'):
        """public static <T extends java.lang.Throwable> void org.apache.commons.lang3.Functions.run(org.apache.commons.lang3.Functions$FailableRunnable<T>)"""
        _Functions.run(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def apply(arg0: 'FailableBiFunction', arg1: object, arg2: object) -> object:
        """public static <O1,O2,O,T extends java.lang.Throwable> O org.apache.commons.lang3.Functions.apply(org.apache.commons.lang3.Functions$FailableBiFunction<O1, O2, O, T>,O1,O2)"""
        return object._wrap(_Functions.apply(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def call(arg0: 'FailableCallable') -> object:
        """public static <O,T extends java.lang.Throwable> O org.apache.commons.lang3.Functions.call(org.apache.commons.lang3.Functions$FailableCallable<O, T>)"""
        return object._wrap(_Functions.call(arg0))

    @staticmethod
    @overload
    def stream(arg0: 'Stream') -> 'FailableStream':
        """public static <O> org.apache.commons.lang3.Streams$FailableStream<O> org.apache.commons.lang3.Functions.stream(java.util.stream.Stream<O>)"""
        return FailableStream._wrap(_Functions.stream(arg0))

    @staticmethod
    @overload
    def asConsumer(arg0: 'FailableConsumer') -> 'Consumer':
        """public static <I> java.util.function.Consumer<I> org.apache.commons.lang3.Functions.asConsumer(org.apache.commons.lang3.Functions$FailableConsumer<I, ?>)"""
        return Consumer._wrap(_Functions.asConsumer(arg0))

    @staticmethod
    @overload
    def asSupplier(arg0: 'FailableSupplier') -> 'Supplier':
        """public static <O> java.util.function.Supplier<O> org.apache.commons.lang3.Functions.asSupplier(org.apache.commons.lang3.Functions$FailableSupplier<O, ?>)"""
        return Supplier._wrap(_Functions.asSupplier(arg0))

    @staticmethod
    @overload
    def tryWithResources(arg0: 'FailableRunnable', arg1: 'FailableConsumer', *arg2: 'FailableRunnable'):
        """public static void org.apache.commons.lang3.Functions.tryWithResources(org.apache.commons.lang3.Functions$FailableRunnable<? extends java.lang.Throwable>,org.apache.commons.lang3.Functions$FailableConsumer<java.lang.Throwable, ? extends java.lang.Throwable>,org.apache.commons.lang3.Functions$FailableRunnable<? extends java.lang.Throwable>...)"""
        _Functions.tryWithResources(arg0, arg1, arg2)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def apply(arg0: 'FailableFunction', arg1: object) -> object:
        """public static <I,O,T extends java.lang.Throwable> O org.apache.commons.lang3.Functions.apply(org.apache.commons.lang3.Functions$FailableFunction<I, O, T>,I)"""
        return object._wrap(_Functions.apply(arg0, arg1))

    @staticmethod
    @overload
    def rethrow(arg0: 'Throwable') -> 'RuntimeException':
        """public static java.lang.RuntimeException org.apache.commons.lang3.Functions.rethrow(java.lang.Throwable)"""
        return RuntimeException._wrap(_Functions.rethrow(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def asRunnable(arg0: 'FailableRunnable') -> 'Runnable':
        """public static java.lang.Runnable org.apache.commons.lang3.Functions.asRunnable(org.apache.commons.lang3.Functions$FailableRunnable<?>)"""
        return Runnable._wrap(_Functions.asRunnable(arg0))

    @staticmethod
    @overload
    def asBiFunction(arg0: 'FailableBiFunction') -> 'BiFunction':
        """public static <O1,O2,O> java.util.function.BiFunction<O1, O2, O> org.apache.commons.lang3.Functions.asBiFunction(org.apache.commons.lang3.Functions$FailableBiFunction<O1, O2, O, ?>)"""
        return BiFunction._wrap(_Functions.asBiFunction(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def test(arg0: 'FailablePredicate', arg1: object) -> bool:
        """public static <O,T extends java.lang.Throwable> boolean org.apache.commons.lang3.Functions.test(org.apache.commons.lang3.Functions$FailablePredicate<O, T>,O)"""
        return bool._wrap(_Functions.test(arg0, arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.Functions()"""
        val = _Functions()
        self.__wrapper = val

    @staticmethod
    @overload
    def test(arg0: 'FailableBiPredicate', arg1: object, arg2: object) -> bool:
        """public static <O1,O2,T extends java.lang.Throwable> boolean org.apache.commons.lang3.Functions.test(org.apache.commons.lang3.Functions$FailableBiPredicate<O1, O2, T>,O1,O2)"""
        return bool._wrap(_Functions.test(arg0, arg1, arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def accept(arg0: 'FailableBiConsumer', arg1: object, arg2: object):
        """public static <O1,O2,T extends java.lang.Throwable> void org.apache.commons.lang3.Functions.accept(org.apache.commons.lang3.Functions$FailableBiConsumer<O1, O2, T>,O1,O2)"""
        _Functions.accept(arg0, arg1, arg2)

    @staticmethod
    @overload
    def asCallable(arg0: 'FailableCallable') -> 'Callable':
        """public static <O> java.util.concurrent.Callable<O> org.apache.commons.lang3.Functions.asCallable(org.apache.commons.lang3.Functions$FailableCallable<O, ?>)"""
        return Callable._wrap(_Functions.asCallable(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.Functions()"""
        val = _Functions()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def tryWithResources(arg0: 'FailableRunnable', *arg1: 'FailableRunnable'):
        """public static void org.apache.commons.lang3.Functions.tryWithResources(org.apache.commons.lang3.Functions$FailableRunnable<? extends java.lang.Throwable>,org.apache.commons.lang3.Functions$FailableRunnable<? extends java.lang.Throwable>...)"""
        _Functions.tryWithResources(arg0, arg1)

    @staticmethod
    @overload
    def get(arg0: 'FailableSupplier') -> object:
        """public static <O,T extends java.lang.Throwable> O org.apache.commons.lang3.Functions.get(org.apache.commons.lang3.Functions$FailableSupplier<O, T>)"""
        return object._wrap(_Functions.get(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.ThreadUtils$ThreadGroupPredicate
import java.lang.ThreadGroup as ThreadGroup
import org.apache.commons.lang3.ThreadUtils as _ThreadUtils_ThreadGroupPredicate
_ThreadGroupPredicate = _ThreadUtils_ThreadGroupPredicate.ThreadGroupPredicate
from abc import abstractmethod, ABC
 
class ThreadGroupPredicate():
    """org.apache.commons.lang3.ThreadUtils.ThreadGroupPredicate"""
 
    @staticmethod
    def _wrap(java_value: _ThreadGroupPredicate) -> 'ThreadGroupPredicate':
        return ThreadGroupPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ThreadGroupPredicate):
        """
        Dynamic initializer for ThreadGroupPredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ThreadGroupPredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ThreadGroupPredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def test(self, arg0: 'ThreadGroup'):
        """public abstract boolean org.apache.commons.lang3.ThreadUtils$ThreadGroupPredicate.test(java.lang.ThreadGroup)"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.CharEncoding
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import org.apache.commons.lang3.CharEncoding as _CharEncoding
_CharEncoding = _CharEncoding
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CharEncoding():
    """org.apache.commons.lang3.CharEncoding"""
 
    @staticmethod
    def _wrap(java_value: _CharEncoding) -> 'CharEncoding':
        return CharEncoding(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CharEncoding):
        """
        Dynamic initializer for CharEncoding.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CharEncoding__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CharEncoding__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def isSupported(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.CharEncoding.isSupported(java.lang.String)"""
        return bool._wrap(_CharEncoding.isSupported(arg0))

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
    def __init__(self, ):
        """public org.apache.commons.lang3.CharEncoding()"""
        val = _CharEncoding()
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.CharEncoding()"""
        val = _CharEncoding()
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
 
 
# CLASS: org.apache.commons.lang3.StringUtils
import java.util.Locale as Locale
import java.util.function.Supplier as Supplier
import java.lang.Character as _char
import java.nio.charset.Charset as Charset
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.CharSequence as _CharSequence
_CharSequence = _CharSequence
import java.lang.String as _string
import java.lang.Boolean as _boolean
from builtins import bool
from builtins import str
import org.apache.commons.lang3.StringUtils as _StringUtils
_StringUtils = _StringUtils
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.lang.Integer as _int
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class StringUtils():
    """org.apache.commons.lang3.StringUtils"""
 
    @staticmethod
    def _wrap(java_value: _StringUtils) -> 'StringUtils':
        return StringUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StringUtils):
        """
        Dynamic initializer for StringUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StringUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StringUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def lowerCase(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.lowerCase(java.lang.String)"""
        return str._wrap(_StringUtils.lowerCase(arg0))

    @staticmethod
    @overload
    def truncate(arg0: str, arg1: int, arg2: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.truncate(java.lang.String,int,int)"""
        return str._wrap(_StringUtils.truncate(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def isWhitespace(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isWhitespace(java.lang.CharSequence)"""
        return bool._wrap(_StringUtils.isWhitespace(arg0))

    @staticmethod
    @overload
    def removePattern(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.removePattern(java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.removePattern(arg0, arg1))

    @staticmethod
    @overload
    def lastOrdinalIndexOf(arg0: 'CharSequence', arg1: 'CharSequence', arg2: int) -> int:
        """public static int org.apache.commons.lang3.StringUtils.lastOrdinalIndexOf(java.lang.CharSequence,java.lang.CharSequence,int)"""
        return int._wrap(_StringUtils.lastOrdinalIndexOf(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def isAllLowerCase(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isAllLowerCase(java.lang.CharSequence)"""
        return bool._wrap(_StringUtils.isAllLowerCase(arg0))

    @staticmethod
    @overload
    def join(arg0: 'short', arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(short[],char,int,int)"""
        return str._wrap(_StringUtils.join(arg0, _char.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def contains(arg0: 'CharSequence', arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.contains(java.lang.CharSequence,java.lang.CharSequence)"""
        return bool._wrap(_StringUtils.contains(arg0, arg1))

    @staticmethod
    @overload
    def toRootLowerCase(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.toRootLowerCase(java.lang.String)"""
        return str._wrap(_StringUtils.toRootLowerCase(arg0))

    @staticmethod
    @overload
    def containsNone(arg0: 'CharSequence', arg1: str) -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.containsNone(java.lang.CharSequence,java.lang.String)"""
        return bool._wrap(_StringUtils.containsNone(arg0, arg1))

    @staticmethod
    @overload
    def join(arg0: 'char', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(char[],char)"""
        return str._wrap(_StringUtils.join(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def join(arg0: bytes, arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(byte[],char,int,int)"""
        return str._wrap(_StringUtils.join(bytes, _char.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def upperCase(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.upperCase(java.lang.String)"""
        return str._wrap(_StringUtils.upperCase(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def repeat(arg0: str, arg1: str, arg2: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.repeat(java.lang.String,java.lang.String,int)"""
        return str._wrap(_StringUtils.repeat(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def split(arg0: str, arg1: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.split(java.lang.String,char)"""
        return List[str]._wrap(_StringUtils.split(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def join(arg0: 'long', arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(long[],char,int,int)"""
        return str._wrap(_StringUtils.join(arg0, _char.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def splitByWholeSeparator(arg0: str, arg1: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.splitByWholeSeparator(java.lang.String,java.lang.String)"""
        return List[str]._wrap(_StringUtils.splitByWholeSeparator(arg0, arg1))

    @staticmethod
    @overload
    def stripToNull(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.stripToNull(java.lang.String)"""
        return str._wrap(_StringUtils.stripToNull(arg0))

    @staticmethod
    @overload
    def join(arg0: 'double', arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(double[],char,int,int)"""
        return str._wrap(_StringUtils.join(arg0, _char.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def uncapitalize(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.uncapitalize(java.lang.String)"""
        return str._wrap(_StringUtils.uncapitalize(arg0))

    @staticmethod
    @overload
    def truncate(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.truncate(java.lang.String,int)"""
        return str._wrap(_StringUtils.truncate(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def abbreviate(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.abbreviate(java.lang.String,int)"""
        return str._wrap(_StringUtils.abbreviate(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def removeFirst(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.removeFirst(java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.removeFirst(arg0, arg1))

    @staticmethod
    @overload
    def isAllEmpty(*arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isAllEmpty(java.lang.CharSequence...)"""
        return bool._wrap(_StringUtils.isAllEmpty(arg0))

    @staticmethod
    @overload
    def join(arg0: 'int', arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(int[],char,int,int)"""
        return str._wrap(_StringUtils.join(arg0, _char.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def indexOfDifference(arg0: 'CharSequence', arg1: 'CharSequence') -> int:
        """public static int org.apache.commons.lang3.StringUtils.indexOfDifference(java.lang.CharSequence,java.lang.CharSequence)"""
        return int._wrap(_StringUtils.indexOfDifference(arg0, arg1))

    @staticmethod
    @overload
    def isAlphanumeric(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isAlphanumeric(java.lang.CharSequence)"""
        return bool._wrap(_StringUtils.isAlphanumeric(arg0))

    @staticmethod
    @overload
    def lastIndexOfAny(arg0: 'CharSequence', *arg1: 'CharSequence') -> int:
        """public static int org.apache.commons.lang3.StringUtils.lastIndexOfAny(java.lang.CharSequence,java.lang.CharSequence...)"""
        return int._wrap(_StringUtils.lastIndexOfAny(arg0, arg1))

    @staticmethod
    @overload
    def join(arg0: 'char', arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(char[],char,int,int)"""
        return str._wrap(_StringUtils.join(arg0, _char.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def substringAfterLast(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.substringAfterLast(java.lang.String,int)"""
        return str._wrap(_StringUtils.substringAfterLast(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def remove(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.remove(java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.remove(arg0, arg1))

    @staticmethod
    @overload
    def replaceFirst(arg0: str, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.replaceFirst(java.lang.String,java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.replaceFirst(arg0, arg1, arg2))

    @staticmethod
    @overload
    def join(arg0: 'Iterator', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(java.util.Iterator<?>,char)"""
        return str._wrap(_StringUtils.join(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def trimToNull(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.trimToNull(java.lang.String)"""
        return str._wrap(_StringUtils.trimToNull(arg0))

    @staticmethod
    @overload
    def equalsIgnoreCase(arg0: 'CharSequence', arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.equalsIgnoreCase(java.lang.CharSequence,java.lang.CharSequence)"""
        return bool._wrap(_StringUtils.equalsIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def containsWhitespace(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.containsWhitespace(java.lang.CharSequence)"""
        return bool._wrap(_StringUtils.containsWhitespace(arg0))

    @staticmethod
    @overload
    def equalsAnyIgnoreCase(arg0: 'CharSequence', *arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.equalsAnyIgnoreCase(java.lang.CharSequence,java.lang.CharSequence...)"""
        return bool._wrap(_StringUtils.equalsAnyIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def substringBefore(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.substringBefore(java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.substringBefore(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def isNotEmpty(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isNotEmpty(java.lang.CharSequence)"""
        return bool._wrap(_StringUtils.isNotEmpty(arg0))

    @staticmethod
    @overload
    def indexOf(arg0: 'CharSequence', arg1: 'CharSequence', arg2: int) -> int:
        """public static int org.apache.commons.lang3.StringUtils.indexOf(java.lang.CharSequence,java.lang.CharSequence,int)"""
        return int._wrap(_StringUtils.indexOf(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def deleteWhitespace(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.deleteWhitespace(java.lang.String)"""
        return str._wrap(_StringUtils.deleteWhitespace(arg0))

    @staticmethod
    @overload
    def compare(arg0: str, arg1: str) -> int:
        """public static int org.apache.commons.lang3.StringUtils.compare(java.lang.String,java.lang.String)"""
        return int._wrap(_StringUtils.compare(arg0, arg1))

    @staticmethod
    @overload
    def containsNone(arg0: 'CharSequence', *arg1: str) -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.containsNone(java.lang.CharSequence,char...)"""
        return bool._wrap(_StringUtils.containsNone(arg0, arg1))

    @staticmethod
    @overload
    def split(arg0: str, arg1: str, arg2: int) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.split(java.lang.String,java.lang.String,int)"""
        return List[str]._wrap(_StringUtils.split(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def center(arg0: str, arg1: int, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.center(java.lang.String,int,char)"""
        return str._wrap(_StringUtils.center(arg0, _int.valueOf(arg1), _char.valueOf(arg2)))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.StringUtils()"""
        val = _StringUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'CharSequence', arg1: int) -> int:
        """public static int org.apache.commons.lang3.StringUtils.lastIndexOf(java.lang.CharSequence,int)"""
        return int._wrap(_StringUtils.lastIndexOf(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def center(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.center(java.lang.String,int)"""
        return str._wrap(_StringUtils.center(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def indexOfIgnoreCase(arg0: 'CharSequence', arg1: 'CharSequence') -> int:
        """public static int org.apache.commons.lang3.StringUtils.indexOfIgnoreCase(java.lang.CharSequence,java.lang.CharSequence)"""
        return int._wrap(_StringUtils.indexOfIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def join(arg0: 'boolean', arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(boolean[],char,int,int)"""
        return str._wrap(_StringUtils.join(arg0, _char.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def containsIgnoreCase(arg0: 'CharSequence', arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.containsIgnoreCase(java.lang.CharSequence,java.lang.CharSequence)"""
        return bool._wrap(_StringUtils.containsIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def startsWithIgnoreCase(arg0: 'CharSequence', arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.startsWithIgnoreCase(java.lang.CharSequence,java.lang.CharSequence)"""
        return bool._wrap(_StringUtils.startsWithIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def isMixedCase(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isMixedCase(java.lang.CharSequence)"""
        return bool._wrap(_StringUtils.isMixedCase(arg0))

    @staticmethod
    @overload
    def containsOnly(arg0: 'CharSequence', arg1: str) -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.containsOnly(java.lang.CharSequence,java.lang.String)"""
        return bool._wrap(_StringUtils.containsOnly(arg0, arg1))

    @staticmethod
    @overload
    def isNoneBlank(*arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isNoneBlank(java.lang.CharSequence...)"""
        return bool._wrap(_StringUtils.isNoneBlank(arg0))

    @staticmethod
    @overload
    def compareIgnoreCase(arg0: str, arg1: str) -> int:
        """public static int org.apache.commons.lang3.StringUtils.compareIgnoreCase(java.lang.String,java.lang.String)"""
        return int._wrap(_StringUtils.compareIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def stripAll(*arg0: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.stripAll(java.lang.String...)"""
        return List[str]._wrap(_StringUtils.stripAll(arg0))

    @staticmethod
    @overload
    def substringAfterLast(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.substringAfterLast(java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.substringAfterLast(arg0, arg1))

    @staticmethod
    @overload
    def toRootUpperCase(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.toRootUpperCase(java.lang.String)"""
        return str._wrap(_StringUtils.toRootUpperCase(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def compare(arg0: str, arg1: str, arg2: bool) -> int:
        """public static int org.apache.commons.lang3.StringUtils.compare(java.lang.String,java.lang.String,boolean)"""
        return int._wrap(_StringUtils.compare(arg0, arg1, _boolean.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def substringAfter(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.substringAfter(java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.substringAfter(arg0, arg1))

    @staticmethod
    @overload
    def leftPad(arg0: str, arg1: int, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.leftPad(java.lang.String,int,java.lang.String)"""
        return str._wrap(_StringUtils.leftPad(arg0, _int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def containsAny(arg0: 'CharSequence', arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.containsAny(java.lang.CharSequence,java.lang.CharSequence)"""
        return bool._wrap(_StringUtils.containsAny(arg0, arg1))

    @staticmethod
    @overload
    def defaultString(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.defaultString(java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.defaultString(arg0, arg1))

    @staticmethod
    @overload
    def abbreviate(arg0: str, arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.abbreviate(java.lang.String,java.lang.String,int,int)"""
        return str._wrap(_StringUtils.abbreviate(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def getLevenshteinDistance(arg0: 'CharSequence', arg1: 'CharSequence', arg2: int) -> int:
        """public static int org.apache.commons.lang3.StringUtils.getLevenshteinDistance(java.lang.CharSequence,java.lang.CharSequence,int)"""
        return int._wrap(_StringUtils.getLevenshteinDistance(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def capitalize(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.capitalize(java.lang.String)"""
        return str._wrap(_StringUtils.capitalize(arg0))

    @staticmethod
    @overload
    def join(arg0: 'int', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(int[],char)"""
        return str._wrap(_StringUtils.join(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def lowerCase(arg0: str, arg1: 'Locale') -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.lowerCase(java.lang.String,java.util.Locale)"""
        return str._wrap(_StringUtils.lowerCase(arg0, arg1))

    @staticmethod
    @overload
    def countMatches(arg0: 'CharSequence', arg1: 'CharSequence') -> int:
        """public static int org.apache.commons.lang3.StringUtils.countMatches(java.lang.CharSequence,java.lang.CharSequence)"""
        return int._wrap(_StringUtils.countMatches(arg0, arg1))

    @staticmethod
    @overload
    def indexOfAnyBut(arg0: 'CharSequence', *arg1: str) -> int:
        """public static int org.apache.commons.lang3.StringUtils.indexOfAnyBut(java.lang.CharSequence,char...)"""
        return int._wrap(_StringUtils.indexOfAnyBut(arg0, arg1))

    @staticmethod
    @overload
    def indexOfAnyBut(arg0: 'CharSequence', arg1: 'CharSequence') -> int:
        """public static int org.apache.commons.lang3.StringUtils.indexOfAnyBut(java.lang.CharSequence,java.lang.CharSequence)"""
        return int._wrap(_StringUtils.indexOfAnyBut(arg0, arg1))

    @staticmethod
    @overload
    def equals(arg0: 'CharSequence', arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.equals(java.lang.CharSequence,java.lang.CharSequence)"""
        return bool._wrap(_StringUtils.equals(arg0, arg1))

    @staticmethod
    @overload
    def stripStart(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.stripStart(java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.stripStart(arg0, arg1))

    @staticmethod
    @overload
    def wrap(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.wrap(java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.wrap(arg0, arg1))

    @staticmethod
    @overload
    def isNumeric(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isNumeric(java.lang.CharSequence)"""
        return bool._wrap(_StringUtils.isNumeric(arg0))

    @staticmethod
    @overload
    def repeat(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.repeat(java.lang.String,int)"""
        return str._wrap(_StringUtils.repeat(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def containsAnyIgnoreCase(arg0: 'CharSequence', *arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.containsAnyIgnoreCase(java.lang.CharSequence,java.lang.CharSequence...)"""
        return bool._wrap(_StringUtils.containsAnyIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def startsWith(arg0: 'CharSequence', arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.startsWith(java.lang.CharSequence,java.lang.CharSequence)"""
        return bool._wrap(_StringUtils.startsWith(arg0, arg1))

    @staticmethod
    @overload
    def leftPad(arg0: str, arg1: int, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.leftPad(java.lang.String,int,char)"""
        return str._wrap(_StringUtils.leftPad(arg0, _int.valueOf(arg1), _char.valueOf(arg2)))

    @staticmethod
    @overload
    def indexOfAny(arg0: 'CharSequence', *arg1: str) -> int:
        """public static int org.apache.commons.lang3.StringUtils.indexOfAny(java.lang.CharSequence,char...)"""
        return int._wrap(_StringUtils.indexOfAny(arg0, arg1))

    @staticmethod
    @overload
    def strip(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.strip(java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.strip(arg0, arg1))

    @staticmethod
    @overload
    def isNumericSpace(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isNumericSpace(java.lang.CharSequence)"""
        return bool._wrap(_StringUtils.isNumericSpace(arg0))

    @staticmethod
    @overload
    def split(arg0: str, arg1: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.split(java.lang.String,java.lang.String)"""
        return List[str]._wrap(_StringUtils.split(arg0, arg1))

    @staticmethod
    @overload
    def overlay(arg0: str, arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.overlay(java.lang.String,java.lang.String,int,int)"""
        return str._wrap(_StringUtils.overlay(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def getFuzzyDistance(arg0: 'CharSequence', arg1: 'CharSequence', arg2: 'Locale') -> int:
        """public static int org.apache.commons.lang3.StringUtils.getFuzzyDistance(java.lang.CharSequence,java.lang.CharSequence,java.util.Locale)"""
        return int._wrap(_StringUtils.getFuzzyDistance(arg0, arg1, arg2))

    @staticmethod
    @overload
    def prependIfMissingIgnoreCase(arg0: str, arg1: 'CharSequence', *arg2: 'CharSequence') -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.prependIfMissingIgnoreCase(java.lang.String,java.lang.CharSequence,java.lang.CharSequence...)"""
        return str._wrap(_StringUtils.prependIfMissingIgnoreCase(arg0, arg1, arg2))

    @staticmethod
    @overload
    def removeEnd(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.removeEnd(java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.removeEnd(arg0, arg1))

    @staticmethod
    @overload
    def ordinalIndexOf(arg0: 'CharSequence', arg1: 'CharSequence', arg2: int) -> int:
        """public static int org.apache.commons.lang3.StringUtils.ordinalIndexOf(java.lang.CharSequence,java.lang.CharSequence,int)"""
        return int._wrap(_StringUtils.ordinalIndexOf(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def replaceIgnoreCase(arg0: str, arg1: str, arg2: str, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.replaceIgnoreCase(java.lang.String,java.lang.String,java.lang.String,int)"""
        return str._wrap(_StringUtils.replaceIgnoreCase(arg0, arg1, arg2, _int.valueOf(arg3)))

    @staticmethod
    @overload
    def toEncodedString(arg0: bytes, arg1: 'Charset') -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.toEncodedString(byte[],java.nio.charset.Charset)"""
        return str._wrap(_StringUtils.toEncodedString(bytes, arg1))

    @staticmethod
    @overload
    def countMatches(arg0: 'CharSequence', arg1: str) -> int:
        """public static int org.apache.commons.lang3.StringUtils.countMatches(java.lang.CharSequence,char)"""
        return int._wrap(_StringUtils.countMatches(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def join(arg0: 'Iterable', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(java.lang.Iterable<?>,java.lang.String)"""
        return str._wrap(_StringUtils.join(arg0, arg1))

    @staticmethod
    @overload
    def containsAny(arg0: 'CharSequence', *arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.containsAny(java.lang.CharSequence,java.lang.CharSequence...)"""
        return bool._wrap(_StringUtils.containsAny(arg0, arg1))

    @staticmethod
    @overload
    def length(arg0: 'CharSequence') -> int:
        """public static int org.apache.commons.lang3.StringUtils.length(java.lang.CharSequence)"""
        return int._wrap(_StringUtils.length(arg0))

    @staticmethod
    @overload
    def lastIndexOfIgnoreCase(arg0: 'CharSequence', arg1: 'CharSequence') -> int:
        """public static int org.apache.commons.lang3.StringUtils.lastIndexOfIgnoreCase(java.lang.CharSequence,java.lang.CharSequence)"""
        return int._wrap(_StringUtils.lastIndexOfIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def isNoneEmpty(*arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isNoneEmpty(java.lang.CharSequence...)"""
        return bool._wrap(_StringUtils.isNoneEmpty(arg0))

    @staticmethod
    @overload
    def indexOfAny(arg0: 'CharSequence', *arg1: 'CharSequence') -> int:
        """public static int org.apache.commons.lang3.StringUtils.indexOfAny(java.lang.CharSequence,java.lang.CharSequence...)"""
        return int._wrap(_StringUtils.indexOfAny(arg0, arg1))

    @staticmethod
    @overload
    def splitByCharacterTypeCamelCase(arg0: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.splitByCharacterTypeCamelCase(java.lang.String)"""
        return List[str]._wrap(_StringUtils.splitByCharacterTypeCamelCase(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.StringUtils()"""
        val = _StringUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'CharSequence', arg1: int, arg2: int) -> int:
        """public static int org.apache.commons.lang3.StringUtils.lastIndexOf(java.lang.CharSequence,int,int)"""
        return int._wrap(_StringUtils.lastIndexOf(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def split(arg0: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.split(java.lang.String)"""
        return List[str]._wrap(_StringUtils.split(arg0))

    @staticmethod
    @overload
    def center(arg0: str, arg1: int, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.center(java.lang.String,int,java.lang.String)"""
        return str._wrap(_StringUtils.center(arg0, _int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def replaceOnce(arg0: str, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.replaceOnce(java.lang.String,java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.replaceOnce(arg0, arg1, arg2))

    @staticmethod
    @overload
    def indexOf(arg0: 'CharSequence', arg1: int, arg2: int) -> int:
        """public static int org.apache.commons.lang3.StringUtils.indexOf(java.lang.CharSequence,int,int)"""
        return int._wrap(_StringUtils.indexOf(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def indexOf(arg0: 'CharSequence', arg1: 'CharSequence') -> int:
        """public static int org.apache.commons.lang3.StringUtils.indexOf(java.lang.CharSequence,java.lang.CharSequence)"""
        return int._wrap(_StringUtils.indexOf(arg0, arg1))

    @staticmethod
    @overload
    def removeStart(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.removeStart(java.lang.String,char)"""
        return str._wrap(_StringUtils.removeStart(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def join(arg0: 'boolean', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(boolean[],char)"""
        return str._wrap(_StringUtils.join(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def getCommonPrefix(*arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.getCommonPrefix(java.lang.String...)"""
        return str._wrap(_StringUtils.getCommonPrefix(arg0))

    @staticmethod
    @overload
    def isAlphanumericSpace(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isAlphanumericSpace(java.lang.CharSequence)"""
        return bool._wrap(_StringUtils.isAlphanumericSpace(arg0))

    @staticmethod
    @overload
    def getBytes(arg0: str, arg1: 'Charset') -> List[int]:
        """public static byte[] org.apache.commons.lang3.StringUtils.getBytes(java.lang.String,java.nio.charset.Charset)"""
        return List[int]._wrap(_StringUtils.getBytes(arg0, arg1))

    @staticmethod
    @overload
    def rotate(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.rotate(java.lang.String,int)"""
        return str._wrap(_StringUtils.rotate(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def chop(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.chop(java.lang.String)"""
        return str._wrap(_StringUtils.chop(arg0))

    @staticmethod
    @overload
    def unwrap(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.unwrap(java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.unwrap(arg0, arg1))

    @staticmethod
    @overload
    def splitPreserveAllTokens(arg0: str, arg1: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.splitPreserveAllTokens(java.lang.String,char)"""
        return List[str]._wrap(_StringUtils.splitPreserveAllTokens(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def splitByWholeSeparatorPreserveAllTokens(arg0: str, arg1: str, arg2: int) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.splitByWholeSeparatorPreserveAllTokens(java.lang.String,java.lang.String,int)"""
        return List[str]._wrap(_StringUtils.splitByWholeSeparatorPreserveAllTokens(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def rightPad(arg0: str, arg1: int, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.rightPad(java.lang.String,int,java.lang.String)"""
        return str._wrap(_StringUtils.rightPad(arg0, _int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def indexOfIgnoreCase(arg0: 'CharSequence', arg1: 'CharSequence', arg2: int) -> int:
        """public static int org.apache.commons.lang3.StringUtils.indexOfIgnoreCase(java.lang.CharSequence,java.lang.CharSequence,int)"""
        return int._wrap(_StringUtils.indexOfIgnoreCase(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def replaceAll(arg0: str, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.replaceAll(java.lang.String,java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.replaceAll(arg0, arg1, arg2))

    @staticmethod
    @overload
    def removeAll(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.removeAll(java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.removeAll(arg0, arg1))

    @staticmethod
    @overload
    def lastIndexOfIgnoreCase(arg0: 'CharSequence', arg1: 'CharSequence', arg2: int) -> int:
        """public static int org.apache.commons.lang3.StringUtils.lastIndexOfIgnoreCase(java.lang.CharSequence,java.lang.CharSequence,int)"""
        return int._wrap(_StringUtils.lastIndexOfIgnoreCase(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'CharSequence', arg1: 'CharSequence', arg2: int) -> int:
        """public static int org.apache.commons.lang3.StringUtils.lastIndexOf(java.lang.CharSequence,java.lang.CharSequence,int)"""
        return int._wrap(_StringUtils.lastIndexOf(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def difference(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.difference(java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.difference(arg0, arg1))

    @staticmethod
    @overload
    def replaceOnceIgnoreCase(arg0: str, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.replaceOnceIgnoreCase(java.lang.String,java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.replaceOnceIgnoreCase(arg0, arg1, arg2))

    @staticmethod
    @overload
    def join(arg0: 'float', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(float[],char)"""
        return str._wrap(_StringUtils.join(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def indexOfDifference(*arg0: 'CharSequence') -> int:
        """public static int org.apache.commons.lang3.StringUtils.indexOfDifference(java.lang.CharSequence...)"""
        return int._wrap(_StringUtils.indexOfDifference(arg0))

    @staticmethod
    @overload
    def getDigits(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.getDigits(java.lang.String)"""
        return str._wrap(_StringUtils.getDigits(arg0))

    @staticmethod
    @overload
    def join(arg0: 'Object', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(java.lang.Object[],char)"""
        return str._wrap(_StringUtils.join(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def getLevenshteinDistance(arg0: 'CharSequence', arg1: 'CharSequence') -> int:
        """public static int org.apache.commons.lang3.StringUtils.getLevenshteinDistance(java.lang.CharSequence,java.lang.CharSequence)"""
        return int._wrap(_StringUtils.getLevenshteinDistance(arg0, arg1))

    @staticmethod
    @overload
    def substring(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.substring(java.lang.String,int)"""
        return str._wrap(_StringUtils.substring(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def reverseDelimited(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.reverseDelimited(java.lang.String,char)"""
        return str._wrap(_StringUtils.reverseDelimited(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def remove(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.remove(java.lang.String,char)"""
        return str._wrap(_StringUtils.remove(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def getIfBlank(arg0: 'CharSequence', arg1: 'Supplier') -> 'CharSequence':
        """public static <T extends java.lang.CharSequence> T org.apache.commons.lang3.StringUtils.getIfBlank(T,java.util.function.Supplier<T>)"""
        return CharSequence._wrap(_StringUtils.getIfBlank(arg0, arg1))

    @staticmethod
    @overload
    def endsWith(arg0: 'CharSequence', arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.endsWith(java.lang.CharSequence,java.lang.CharSequence)"""
        return bool._wrap(_StringUtils.endsWith(arg0, arg1))

    @staticmethod
    @overload
    def replaceEach(arg0: str, arg1: 'String', arg2: 'String') -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.replaceEach(java.lang.String,java.lang.String[],java.lang.String[])"""
        return str._wrap(_StringUtils.replaceEach(arg0, arg1, arg2))

    @staticmethod
    @overload
    def indexOf(arg0: 'CharSequence', arg1: int) -> int:
        """public static int org.apache.commons.lang3.StringUtils.indexOf(java.lang.CharSequence,int)"""
        return int._wrap(_StringUtils.indexOf(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def isAnyEmpty(*arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isAnyEmpty(java.lang.CharSequence...)"""
        return bool._wrap(_StringUtils.isAnyEmpty(arg0))

    @staticmethod
    @overload
    def rightPad(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.rightPad(java.lang.String,int)"""
        return str._wrap(_StringUtils.rightPad(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def abbreviate(arg0: str, arg1: str, arg2: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.abbreviate(java.lang.String,java.lang.String,int)"""
        return str._wrap(_StringUtils.abbreviate(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def removeStart(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.removeStart(java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.removeStart(arg0, arg1))

    @staticmethod
    @overload
    def appendIfMissingIgnoreCase(arg0: str, arg1: 'CharSequence', *arg2: 'CharSequence') -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.appendIfMissingIgnoreCase(java.lang.String,java.lang.CharSequence,java.lang.CharSequence...)"""
        return str._wrap(_StringUtils.appendIfMissingIgnoreCase(arg0, arg1, arg2))

    @staticmethod
    @overload
    def indexOfAny(arg0: 'CharSequence', arg1: str) -> int:
        """public static int org.apache.commons.lang3.StringUtils.indexOfAny(java.lang.CharSequence,java.lang.String)"""
        return int._wrap(_StringUtils.indexOfAny(arg0, arg1))

    @staticmethod
    @overload
    def splitByWholeSeparator(arg0: str, arg1: str, arg2: int) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.splitByWholeSeparator(java.lang.String,java.lang.String,int)"""
        return List[str]._wrap(_StringUtils.splitByWholeSeparator(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def join(arg0: 'Iterator', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(java.util.Iterator<?>,java.lang.String)"""
        return str._wrap(_StringUtils.join(arg0, arg1))

    @staticmethod
    @overload
    def left(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.left(java.lang.String,int)"""
        return str._wrap(_StringUtils.left(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def upperCase(arg0: str, arg1: 'Locale') -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.upperCase(java.lang.String,java.util.Locale)"""
        return str._wrap(_StringUtils.upperCase(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def reverse(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.reverse(java.lang.String)"""
        return str._wrap(_StringUtils.reverse(arg0))

    @staticmethod
    @overload
    def join(arg0: 'Object', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(java.lang.Object[],java.lang.String)"""
        return str._wrap(_StringUtils.join(arg0, arg1))

    @staticmethod
    @overload
    def abbreviate(arg0: str, arg1: int, arg2: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.abbreviate(java.lang.String,int,int)"""
        return str._wrap(_StringUtils.abbreviate(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def prependIfMissing(arg0: str, arg1: 'CharSequence', *arg2: 'CharSequence') -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.prependIfMissing(java.lang.String,java.lang.CharSequence,java.lang.CharSequence...)"""
        return str._wrap(_StringUtils.prependIfMissing(arg0, arg1, arg2))

    @staticmethod
    @overload
    def substringsBetween(arg0: str, arg1: str, arg2: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.substringsBetween(java.lang.String,java.lang.String,java.lang.String)"""
        return List[str]._wrap(_StringUtils.substringsBetween(arg0, arg1, arg2))

    @staticmethod
    @overload
    def normalizeSpace(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.normalizeSpace(java.lang.String)"""
        return str._wrap(_StringUtils.normalizeSpace(arg0))

    @staticmethod
    @overload
    def substringBetween(arg0: str, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.substringBetween(java.lang.String,java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.substringBetween(arg0, arg1, arg2))

    @staticmethod
    @overload
    def containsAny(arg0: 'CharSequence', *arg1: str) -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.containsAny(java.lang.CharSequence,char...)"""
        return bool._wrap(_StringUtils.containsAny(arg0, arg1))

    @staticmethod
    @overload
    def lastIndexOf(arg0: 'CharSequence', arg1: 'CharSequence') -> int:
        """public static int org.apache.commons.lang3.StringUtils.lastIndexOf(java.lang.CharSequence,java.lang.CharSequence)"""
        return int._wrap(_StringUtils.lastIndexOf(arg0, arg1))

    @staticmethod
    @overload
    def isBlank(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isBlank(java.lang.CharSequence)"""
        return bool._wrap(_StringUtils.isBlank(arg0))

    @staticmethod
    @overload
    def replaceChars(arg0: str, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.replaceChars(java.lang.String,char,char)"""
        return str._wrap(_StringUtils.replaceChars(arg0, _char.valueOf(arg1), _char.valueOf(arg2)))

    @staticmethod
    @overload
    def isAllUpperCase(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isAllUpperCase(java.lang.CharSequence)"""
        return bool._wrap(_StringUtils.isAllUpperCase(arg0))

    @staticmethod
    @overload
    def join(arg0: 'Object', arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(java.lang.Object[],java.lang.String,int,int)"""
        return str._wrap(_StringUtils.join(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def containsOnly(arg0: 'CharSequence', *arg1: str) -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.containsOnly(java.lang.CharSequence,char...)"""
        return bool._wrap(_StringUtils.containsOnly(arg0, arg1))

    @staticmethod
    @overload
    def replaceChars(arg0: str, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.replaceChars(java.lang.String,java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.replaceChars(arg0, arg1, arg2))

    @staticmethod
    @overload
    def substring(arg0: str, arg1: int, arg2: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.substring(java.lang.String,int,int)"""
        return str._wrap(_StringUtils.substring(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def join(*arg0: object) -> str:
        """public static <T> java.lang.String org.apache.commons.lang3.StringUtils.join(T...)"""
        return str._wrap(_StringUtils.join(arg0))

    @staticmethod
    @overload
    def startsWithAny(arg0: 'CharSequence', *arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.startsWithAny(java.lang.CharSequence,java.lang.CharSequence...)"""
        return bool._wrap(_StringUtils.startsWithAny(arg0, arg1))

    @staticmethod
    @overload
    def chomp(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.chomp(java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.chomp(arg0, arg1))

    @staticmethod
    @overload
    def splitPreserveAllTokens(arg0: str, arg1: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.splitPreserveAllTokens(java.lang.String,java.lang.String)"""
        return List[str]._wrap(_StringUtils.splitPreserveAllTokens(arg0, arg1))

    @staticmethod
    @overload
    def trim(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.trim(java.lang.String)"""
        return str._wrap(_StringUtils.trim(arg0))

    @staticmethod
    @overload
    def replaceEachRepeatedly(arg0: str, arg1: 'String', arg2: 'String') -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.replaceEachRepeatedly(java.lang.String,java.lang.String[],java.lang.String[])"""
        return str._wrap(_StringUtils.replaceEachRepeatedly(arg0, arg1, arg2))

    @staticmethod
    @overload
    def wrapIfMissing(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.wrapIfMissing(java.lang.String,char)"""
        return str._wrap(_StringUtils.wrapIfMissing(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def join(arg0: 'long', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(long[],char)"""
        return str._wrap(_StringUtils.join(arg0, _char.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def substringBefore(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.substringBefore(java.lang.String,int)"""
        return str._wrap(_StringUtils.substringBefore(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def splitByCharacterType(arg0: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.splitByCharacterType(java.lang.String)"""
        return List[str]._wrap(_StringUtils.splitByCharacterType(arg0))

    @staticmethod
    @overload
    def join(arg0: 'short', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(short[],char)"""
        return str._wrap(_StringUtils.join(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def strip(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.strip(java.lang.String)"""
        return str._wrap(_StringUtils.strip(arg0))

    @staticmethod
    @overload
    def getJaroWinklerDistance(arg0: 'CharSequence', arg1: 'CharSequence') -> float:
        """public static double org.apache.commons.lang3.StringUtils.getJaroWinklerDistance(java.lang.CharSequence,java.lang.CharSequence)"""
        return float._wrap(_StringUtils.getJaroWinklerDistance(arg0, arg1))

    @staticmethod
    @overload
    def joinWith(arg0: str, *arg1: object) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.joinWith(java.lang.String,java.lang.Object...)"""
        return str._wrap(_StringUtils.joinWith(arg0, arg1))

    @staticmethod
    @overload
    def leftPad(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.leftPad(java.lang.String,int)"""
        return str._wrap(_StringUtils.leftPad(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def contains(arg0: 'CharSequence', arg1: int) -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.contains(java.lang.CharSequence,int)"""
        return bool._wrap(_StringUtils.contains(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def substringBeforeLast(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.substringBeforeLast(java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.substringBeforeLast(arg0, arg1))

    @staticmethod
    @overload
    def abbreviateMiddle(arg0: str, arg1: str, arg2: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.abbreviateMiddle(java.lang.String,java.lang.String,int)"""
        return str._wrap(_StringUtils.abbreviateMiddle(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def splitByWholeSeparatorPreserveAllTokens(arg0: str, arg1: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.splitByWholeSeparatorPreserveAllTokens(java.lang.String,java.lang.String)"""
        return List[str]._wrap(_StringUtils.splitByWholeSeparatorPreserveAllTokens(arg0, arg1))

    @staticmethod
    @overload
    def stripAccents(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.stripAccents(java.lang.String)"""
        return str._wrap(_StringUtils.stripAccents(arg0))

    @staticmethod
    @overload
    def isAlpha(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isAlpha(java.lang.CharSequence)"""
        return bool._wrap(_StringUtils.isAlpha(arg0))

    @staticmethod
    @overload
    def defaultIfEmpty(arg0: 'CharSequence', arg1: 'CharSequence') -> 'CharSequence':
        """public static <T extends java.lang.CharSequence> T org.apache.commons.lang3.StringUtils.defaultIfEmpty(T,T)"""
        return CharSequence._wrap(_StringUtils.defaultIfEmpty(arg0, arg1))

    @staticmethod
    @overload
    def removeEndIgnoreCase(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.removeEndIgnoreCase(java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.removeEndIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def splitPreserveAllTokens(arg0: str, arg1: str, arg2: int) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.splitPreserveAllTokens(java.lang.String,java.lang.String,int)"""
        return List[str]._wrap(_StringUtils.splitPreserveAllTokens(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def repeat(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.repeat(char,int)"""
        return str._wrap(_StringUtils.repeat(_char.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def toCodePoints(arg0: 'CharSequence') -> List[int]:
        """public static int[] org.apache.commons.lang3.StringUtils.toCodePoints(java.lang.CharSequence)"""
        return List[int]._wrap(_StringUtils.toCodePoints(arg0))

    @staticmethod
    @overload
    def toString(arg0: bytes, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.toString(byte[],java.lang.String) throws java.io.UnsupportedEncodingException"""
        return str._wrap(_StringUtils.toString(bytes, arg1))

    @staticmethod
    @overload
    def firstNonBlank(*arg0: 'CharSequence') -> 'CharSequence':
        """public static <T extends java.lang.CharSequence> T org.apache.commons.lang3.StringUtils.firstNonBlank(T...)"""
        return CharSequence._wrap(_StringUtils.firstNonBlank(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def replace(arg0: str, arg1: str, arg2: str, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.replace(java.lang.String,java.lang.String,java.lang.String,int)"""
        return str._wrap(_StringUtils.replace(arg0, arg1, arg2, _int.valueOf(arg3)))

    @staticmethod
    @overload
    def join(arg0: 'double', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(double[],char)"""
        return str._wrap(_StringUtils.join(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def join(arg0: 'List', arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(java.util.List<?>,char,int,int)"""
        return str._wrap(_StringUtils.join(arg0, _char.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def removeIgnoreCase(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.removeIgnoreCase(java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.removeIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def stripToEmpty(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.stripToEmpty(java.lang.String)"""
        return str._wrap(_StringUtils.stripToEmpty(arg0))

    @staticmethod
    @overload
    def splitPreserveAllTokens(arg0: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.splitPreserveAllTokens(java.lang.String)"""
        return List[str]._wrap(_StringUtils.splitPreserveAllTokens(arg0))

    @staticmethod
    @overload
    def rightPad(arg0: str, arg1: int, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.rightPad(java.lang.String,int,char)"""
        return str._wrap(_StringUtils.rightPad(arg0, _int.valueOf(arg1), _char.valueOf(arg2)))

    @staticmethod
    @overload
    def wrap(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.wrap(java.lang.String,char)"""
        return str._wrap(_StringUtils.wrap(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def chomp(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.chomp(java.lang.String)"""
        return str._wrap(_StringUtils.chomp(arg0))

    @staticmethod
    @overload
    def defaultIfBlank(arg0: 'CharSequence', arg1: 'CharSequence') -> 'CharSequence':
        """public static <T extends java.lang.CharSequence> T org.apache.commons.lang3.StringUtils.defaultIfBlank(T,T)"""
        return CharSequence._wrap(_StringUtils.defaultIfBlank(arg0, arg1))

    @staticmethod
    @overload
    def getBytes(arg0: str, arg1: str) -> List[int]:
        """public static byte[] org.apache.commons.lang3.StringUtils.getBytes(java.lang.String,java.lang.String) throws java.io.UnsupportedEncodingException"""
        return List[int]._wrap(_StringUtils.getBytes(arg0, arg1))

    @staticmethod
    @overload
    def stripAll(arg0: 'String', arg1: str) -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.StringUtils.stripAll(java.lang.String[],java.lang.String)"""
        return List[str]._wrap(_StringUtils.stripAll(arg0, arg1))

    @staticmethod
    @overload
    def valueOf(arg0: 'char') -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.valueOf(char[])"""
        return str._wrap(_StringUtils.valueOf(arg0))

    @staticmethod
    @overload
    def firstNonEmpty(*arg0: 'CharSequence') -> 'CharSequence':
        """public static <T extends java.lang.CharSequence> T org.apache.commons.lang3.StringUtils.firstNonEmpty(T...)"""
        return CharSequence._wrap(_StringUtils.firstNonEmpty(arg0))

    @staticmethod
    @overload
    def appendIfMissing(arg0: str, arg1: 'CharSequence', *arg2: 'CharSequence') -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.appendIfMissing(java.lang.String,java.lang.CharSequence,java.lang.CharSequence...)"""
        return str._wrap(_StringUtils.appendIfMissing(arg0, arg1, arg2))

    @staticmethod
    @overload
    def join(arg0: 'List', arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(java.util.List<?>,java.lang.String,int,int)"""
        return str._wrap(_StringUtils.join(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def defaultString(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.defaultString(java.lang.String)"""
        return str._wrap(_StringUtils.defaultString(arg0))

    @staticmethod
    @overload
    def swapCase(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.swapCase(java.lang.String)"""
        return str._wrap(_StringUtils.swapCase(arg0))

    @staticmethod
    @overload
    def replace(arg0: str, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.replace(java.lang.String,java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.replace(arg0, arg1, arg2))

    @staticmethod
    @overload
    def replaceIgnoreCase(arg0: str, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.replaceIgnoreCase(java.lang.String,java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.replaceIgnoreCase(arg0, arg1, arg2))

    @staticmethod
    @overload
    def right(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.right(java.lang.String,int)"""
        return str._wrap(_StringUtils.right(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def endsWithIgnoreCase(arg0: 'CharSequence', arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.endsWithIgnoreCase(java.lang.CharSequence,java.lang.CharSequence)"""
        return bool._wrap(_StringUtils.endsWithIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def join(arg0: 'Iterable', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(java.lang.Iterable<?>,char)"""
        return str._wrap(_StringUtils.join(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def isAlphaSpace(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isAlphaSpace(java.lang.CharSequence)"""
        return bool._wrap(_StringUtils.isAlphaSpace(arg0))

    @staticmethod
    @overload
    def unwrap(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.unwrap(java.lang.String,char)"""
        return str._wrap(_StringUtils.unwrap(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def substringBetween(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.substringBetween(java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.substringBetween(arg0, arg1))

    @staticmethod
    @overload
    def isNotBlank(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isNotBlank(java.lang.CharSequence)"""
        return bool._wrap(_StringUtils.isNotBlank(arg0))

    @staticmethod
    @overload
    def trimToEmpty(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.trimToEmpty(java.lang.String)"""
        return str._wrap(_StringUtils.trimToEmpty(arg0))

    @staticmethod
    @overload
    def mid(arg0: str, arg1: int, arg2: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.mid(java.lang.String,int,int)"""
        return str._wrap(_StringUtils.mid(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def removeStartIgnoreCase(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.removeStartIgnoreCase(java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.removeStartIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def wrapIfMissing(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.wrapIfMissing(java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.wrapIfMissing(arg0, arg1))

    @staticmethod
    @overload
    def isAllBlank(*arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isAllBlank(java.lang.CharSequence...)"""
        return bool._wrap(_StringUtils.isAllBlank(arg0))

    @staticmethod
    @overload
    def join(arg0: 'float', arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(float[],char,int,int)"""
        return str._wrap(_StringUtils.join(arg0, _char.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def endsWithAny(arg0: 'CharSequence', *arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.endsWithAny(java.lang.CharSequence,java.lang.CharSequence...)"""
        return bool._wrap(_StringUtils.endsWithAny(arg0, arg1))

    @staticmethod
    @overload
    def isAnyBlank(*arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isAnyBlank(java.lang.CharSequence...)"""
        return bool._wrap(_StringUtils.isAnyBlank(arg0))

    @staticmethod
    @overload
    def join(arg0: 'Object', arg1: str, arg2: int, arg3: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(java.lang.Object[],char,int,int)"""
        return str._wrap(_StringUtils.join(arg0, _char.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def isAsciiPrintable(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isAsciiPrintable(java.lang.CharSequence)"""
        return bool._wrap(_StringUtils.isAsciiPrintable(arg0))

    @staticmethod
    @overload
    def substringAfter(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.substringAfter(java.lang.String,int)"""
        return str._wrap(_StringUtils.substringAfter(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def join(arg0: bytes, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.join(byte[],char)"""
        return str._wrap(_StringUtils.join(bytes, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def equalsAny(arg0: 'CharSequence', *arg1: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.equalsAny(java.lang.CharSequence,java.lang.CharSequence...)"""
        return bool._wrap(_StringUtils.equalsAny(arg0, arg1))

    @staticmethod
    @overload
    def replacePattern(arg0: str, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.replacePattern(java.lang.String,java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.replacePattern(arg0, arg1, arg2))

    @staticmethod
    @overload
    def stripEnd(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringUtils.stripEnd(java.lang.String,java.lang.String)"""
        return str._wrap(_StringUtils.stripEnd(arg0, arg1))

    @staticmethod
    @overload
    def getIfEmpty(arg0: 'CharSequence', arg1: 'Supplier') -> 'CharSequence':
        """public static <T extends java.lang.CharSequence> T org.apache.commons.lang3.StringUtils.getIfEmpty(T,java.util.function.Supplier<T>)"""
        return CharSequence._wrap(_StringUtils.getIfEmpty(arg0, arg1))

    @staticmethod
    @overload
    def isEmpty(arg0: 'CharSequence') -> bool:
        """public static boolean org.apache.commons.lang3.StringUtils.isEmpty(java.lang.CharSequence)"""
        return bool._wrap(_StringUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def compareIgnoreCase(arg0: str, arg1: str, arg2: bool) -> int:
        """public static int org.apache.commons.lang3.StringUtils.compareIgnoreCase(java.lang.String,java.lang.String,boolean)"""
        return int._wrap(_StringUtils.compareIgnoreCase(arg0, arg1, _boolean.valueOf(arg2))) 
 
 
# CLASS: org.apache.commons.lang3.ClassLoaderUtils
from builtins import str
from pyquantum_helper import override
import java.net.URLClassLoader as URLClassLoader
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.net.URL as URL
import java.net.URL as _URL
_URL = _URL
import java.lang.Integer as _int
import org.apache.commons.lang3.ClassLoaderUtils as _ClassLoaderUtils
_ClassLoaderUtils = _ClassLoaderUtils
import java.lang.ClassLoader as ClassLoader
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ClassLoaderUtils():
    """org.apache.commons.lang3.ClassLoaderUtils"""
 
    @staticmethod
    def _wrap(java_value: _ClassLoaderUtils) -> 'ClassLoaderUtils':
        return ClassLoaderUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClassLoaderUtils):
        """
        Dynamic initializer for ClassLoaderUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClassLoaderUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClassLoaderUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def toString(arg0: 'URLClassLoader') -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassLoaderUtils.toString(java.net.URLClassLoader)"""
        return str._wrap(_ClassLoaderUtils.toString(arg0))

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
    def __init__(self):
        """public org.apache.commons.lang3.ClassLoaderUtils()"""
        val = _ClassLoaderUtils()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.ClassLoaderUtils()"""
        val = _ClassLoaderUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def getSystemURLs() -> List['URL']:
        """public static java.net.URL[] org.apache.commons.lang3.ClassLoaderUtils.getSystemURLs()"""
        return List[URL]._wrap(_ClassLoaderUtils.getSystemURLs())

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
    def getThreadURLs() -> List['URL']:
        """public static java.net.URL[] org.apache.commons.lang3.ClassLoaderUtils.getThreadURLs()"""
        return List[URL]._wrap(_ClassLoaderUtils.getThreadURLs())

    @staticmethod
    @overload
    def toString(arg0: 'ClassLoader') -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassLoaderUtils.toString(java.lang.ClassLoader)"""
        return str._wrap(_ClassLoaderUtils.toString(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.Functions$FailableBiPredicate
import org.apache.commons.lang3.Functions as _Functions_FailableBiPredicate
_FailableBiPredicate = _Functions_FailableBiPredicate.FailableBiPredicate
from abc import abstractmethod, ABC
 
class FailableBiPredicate():
    """org.apache.commons.lang3.Functions.FailableBiPredicate"""
 
    @staticmethod
    def _wrap(java_value: _FailableBiPredicate) -> 'FailableBiPredicate':
        return FailableBiPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableBiPredicate):
        """
        Dynamic initializer for FailableBiPredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableBiPredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableBiPredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def test(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.lang3.Functions$FailableBiPredicate.test(O1,O2) throws T"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.JavaVersion
from builtins import str
import org.apache.commons.lang3.JavaVersion as _JavaVersion
_JavaVersion = _JavaVersion
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
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JavaVersion():
    """org.apache.commons.lang3.JavaVersion"""
 
    @staticmethod
    def _wrap(java_value: _JavaVersion) -> 'JavaVersion':
        return JavaVersion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JavaVersion):
        """
        Dynamic initializer for JavaVersion.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JavaVersion__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JavaVersion__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def atLeast(self, arg0: 'JavaVersion') -> bool:
        """public boolean org.apache.commons.lang3.JavaVersion.atLeast(org.apache.commons.lang3.JavaVersion)"""
        return bool._wrap(super(_JavaVersion, self).atLeast(arg0))

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
    def valueOf(arg0: str) -> 'JavaVersion':
        """public static org.apache.commons.lang3.JavaVersion org.apache.commons.lang3.JavaVersion.valueOf(java.lang.String)"""
        return JavaVersion._wrap(_JavaVersion.valueOf(arg0))

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
    def values() -> List['JavaVersion']:
        """public static org.apache.commons.lang3.JavaVersion[] org.apache.commons.lang3.JavaVersion.values()"""
        return List[JavaVersion]._wrap(_JavaVersion.values())

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
    def atMost(self, arg0: 'JavaVersion') -> bool:
        """public boolean org.apache.commons.lang3.JavaVersion.atMost(org.apache.commons.lang3.JavaVersion)"""
        return bool._wrap(super(_JavaVersion, self).atMost(arg0))

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.JavaVersion.toString()"""
        return str._wrap(super(JavaVersion, self).toString()) 
 
 
# CLASS: org.apache.commons.lang3.ArraySorter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import org.apache.commons.lang3.ArraySorter as _ArraySorter
_ArraySorter = _ArraySorter
from builtins import object
import java.lang.String as _String
_String = _String
from typing import List
import java.util.Comparator as Comparator
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ArraySorter():
    """org.apache.commons.lang3.ArraySorter"""
 
    @staticmethod
    def _wrap(java_value: _ArraySorter) -> 'ArraySorter':
        return ArraySorter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ArraySorter):
        """
        Dynamic initializer for ArraySorter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ArraySorter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ArraySorter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def sort(arg0: 'char') -> List[str]:
        """public static char[] org.apache.commons.lang3.ArraySorter.sort(char[])"""
        return List[str]._wrap(_ArraySorter.sort(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.ArraySorter()"""
        val = _ArraySorter()
        self.__wrapper = val

    @staticmethod
    @overload
    def sort(arg0: 'float') -> List[float]:
        """public static float[] org.apache.commons.lang3.ArraySorter.sort(float[])"""
        return List[float]._wrap(_ArraySorter.sort(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def sort(arg0: 'Object', arg1: 'Comparator') -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArraySorter.sort(T[],java.util.Comparator<? super T>)"""
        return List[object]._wrap(_ArraySorter.sort(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def sort(arg0: bytes) -> List[int]:
        """public static byte[] org.apache.commons.lang3.ArraySorter.sort(byte[])"""
        return List[int]._wrap(_ArraySorter.sort(bytes))

    @staticmethod
    @overload
    def sort(arg0: 'double') -> List[float]:
        """public static double[] org.apache.commons.lang3.ArraySorter.sort(double[])"""
        return List[float]._wrap(_ArraySorter.sort(arg0))

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

    @staticmethod
    @overload
    def sort(arg0: 'short') -> List[int]:
        """public static short[] org.apache.commons.lang3.ArraySorter.sort(short[])"""
        return List[int]._wrap(_ArraySorter.sort(arg0))

    @staticmethod
    @overload
    def sort(arg0: 'Object') -> List[object]:
        """public static <T> T[] org.apache.commons.lang3.ArraySorter.sort(T[])"""
        return List[object]._wrap(_ArraySorter.sort(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def sort(arg0: 'long') -> List[int]:
        """public static long[] org.apache.commons.lang3.ArraySorter.sort(long[])"""
        return List[int]._wrap(_ArraySorter.sort(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def sort(arg0: 'int') -> List[int]:
        """public static int[] org.apache.commons.lang3.ArraySorter.sort(int[])"""
        return List[int]._wrap(_ArraySorter.sort(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.ArraySorter()"""
        val = _ArraySorter()
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
 
 
# CLASS: org.apache.commons.lang3.ClassPathUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Package as Package
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import org.apache.commons.lang3.ClassPathUtils as _ClassPathUtils
_ClassPathUtils = _ClassPathUtils
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ClassPathUtils():
    """org.apache.commons.lang3.ClassPathUtils"""
 
    @staticmethod
    def _wrap(java_value: _ClassPathUtils) -> 'ClassPathUtils':
        return ClassPathUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClassPathUtils):
        """
        Dynamic initializer for ClassPathUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClassPathUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClassPathUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.ClassPathUtils()"""
        val = _ClassPathUtils()
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

    @staticmethod
    @overload
    def packageToPath(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassPathUtils.packageToPath(java.lang.String)"""
        return str._wrap(_ClassPathUtils.packageToPath(arg0))

    @staticmethod
    @overload
    def pathToPackage(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassPathUtils.pathToPackage(java.lang.String)"""
        return str._wrap(_ClassPathUtils.pathToPackage(arg0))

    @staticmethod
    @overload
    def toFullyQualifiedName(arg0: 'Class', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassPathUtils.toFullyQualifiedName(java.lang.Class<?>,java.lang.String)"""
        return str._wrap(_ClassPathUtils.toFullyQualifiedName(arg0, arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.ClassPathUtils()"""
        val = _ClassPathUtils()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def toFullyQualifiedName(arg0: 'Package', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassPathUtils.toFullyQualifiedName(java.lang.Package,java.lang.String)"""
        return str._wrap(_ClassPathUtils.toFullyQualifiedName(arg0, arg1))

    @staticmethod
    @overload
    def toFullyQualifiedPath(arg0: 'Package', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassPathUtils.toFullyQualifiedPath(java.lang.Package,java.lang.String)"""
        return str._wrap(_ClassPathUtils.toFullyQualifiedPath(arg0, arg1))

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

    @staticmethod
    @overload
    def toFullyQualifiedPath(arg0: 'Class', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassPathUtils.toFullyQualifiedPath(java.lang.Class<?>,java.lang.String)"""
        return str._wrap(_ClassPathUtils.toFullyQualifiedPath(arg0, arg1))

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
 
 
# CLASS: org.apache.commons.lang3.CharSet
from builtins import str
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.apache.commons.lang3.CharSet as _CharSet
_CharSet = _CharSet
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CharSet():
    """org.apache.commons.lang3.CharSet"""
 
    @staticmethod
    def _wrap(java_value: _CharSet) -> 'CharSet':
        return CharSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CharSet):
        """
        Dynamic initializer for CharSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CharSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CharSet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getInstance(*arg0: str) -> 'CharSet':
        """public static org.apache.commons.lang3.CharSet org.apache.commons.lang3.CharSet.getInstance(java.lang.String...)"""
        return CharSet._wrap(_CharSet.getInstance(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.CharSet.toString()"""
        return str._wrap(super(CharSet, self).toString())

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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.CharSet.equals(java.lang.Object)"""
        return bool._wrap(super(_CharSet, self).equals(arg0))

    @overload
    def contains(self, arg0: str) -> bool:
        """public boolean org.apache.commons.lang3.CharSet.contains(char)"""
        return bool._wrap(super(_CharSet, self).contains(_char.valueOf(arg0)))

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
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.CharSet.hashCode()"""
        return int._wrap(super(CharSet, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.Functions$FailableBiFunction
import org.apache.commons.lang3.Functions as _Functions_FailableBiFunction
_FailableBiFunction = _Functions_FailableBiFunction.FailableBiFunction
from abc import abstractmethod, ABC
 
class FailableBiFunction():
    """org.apache.commons.lang3.Functions.FailableBiFunction"""
 
    @staticmethod
    def _wrap(java_value: _FailableBiFunction) -> 'FailableBiFunction':
        return FailableBiFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableBiFunction):
        """
        Dynamic initializer for FailableBiFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableBiFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableBiFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def apply(self, arg0: object, arg1: object):
        """public abstract R org.apache.commons.lang3.Functions$FailableBiFunction.apply(O1,O2) throws T"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.NumberRange
from builtins import str
import java.lang.Number as Number
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Comparable as Comparable
from builtins import object
import java.lang.String as _string
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import org.apache.commons.lang3.Range as _Range
_Range = _Range
import org.apache.commons.lang3.NumberRange as _NumberRange
_NumberRange = _NumberRange
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NumberRange():
    """org.apache.commons.lang3.NumberRange"""
 
    @staticmethod
    def _wrap(java_value: _NumberRange) -> 'NumberRange':
        return NumberRange(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NumberRange):
        """
        Dynamic initializer for NumberRange.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NumberRange__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NumberRange__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def intersectionWith(self, arg0: 'Range') -> 'Range':
        """public org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.intersectionWith(org.apache.commons.lang3.Range<T>)"""
        return 'Range'._wrap(super(_Range, self).intersectionWith(arg0))

    @overload
    def isBeforeRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isBeforeRange(org.apache.commons.lang3.Range<T>)"""
        return bool._wrap(super(_Range, self).isBeforeRange(arg0))

    @staticmethod
    @overload
    def is(arg0: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.is(T)"""
        return Range._wrap(_Range.is(arg0))

    @overload
    def isAfter(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isAfter(T)"""
        return bool._wrap(super(_Range, self).isAfter(arg0))

    @overload
    def containsRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.containsRange(org.apache.commons.lang3.Range<T>)"""
        return bool._wrap(super(_Range, self).containsRange(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Number', arg1: 'Number', arg2: 'Comparator'):
        """public org.apache.commons.lang3.NumberRange(N,N,java.util.Comparator<N>)"""
        val = _NumberRange(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.Range.toString()"""
        return str._wrap(super(Range, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.Range.hashCode()"""
        return int._wrap(super(Range, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isNaturalOrdering(self) -> bool:
        """public boolean org.apache.commons.lang3.Range.isNaturalOrdering()"""
        return bool._wrap(super(Range, self).isNaturalOrdering())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def isEndedBy(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isEndedBy(T)"""
        return bool._wrap(super(_Range, self).isEndedBy(arg0))

    @overload
    def elementCompareTo(self, arg0: object) -> int:
        """public int org.apache.commons.lang3.Range.elementCompareTo(T)"""
        return int._wrap(super(_Range, self).elementCompareTo(arg0))

    @override
    @overload
    def getComparator(self) -> 'Comparator':
        """public java.util.Comparator<T> org.apache.commons.lang3.Range.getComparator()"""
        return 'Comparator'._wrap(super(Range, self).getComparator())

    @overload
    def isStartedBy(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isStartedBy(T)"""
        return bool._wrap(super(_Range, self).isStartedBy(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.equals(java.lang.Object)"""
        return bool._wrap(super(_Range, self).equals(arg0))

    @overload
    def isBefore(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isBefore(T)"""
        return bool._wrap(super(_Range, self).isBefore(arg0))

    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.of(T,T,java.util.Comparator<T>)"""
        return Range._wrap(_Range.of(arg0, arg1, arg2))

    @staticmethod
    @overload
    def between(arg0: object, arg1: object, arg2: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.between(T,T,java.util.Comparator<T>)"""
        return Range._wrap(_Range.between(arg0, arg1, arg2))

    @overload
    def isAfterRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isAfterRange(org.apache.commons.lang3.Range<T>)"""
        return bool._wrap(super(_Range, self).isAfterRange(arg0))

    @staticmethod
    @overload
    def between(arg0: 'Comparable', arg1: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.between(T,T)"""
        return Range._wrap(_Range.between(arg0, arg1))

    @override
    @overload
    def getMaximum(self) -> object:
        """public T org.apache.commons.lang3.Range.getMaximum()"""
        return object._wrap(super(Range, self).getMaximum())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.contains(T)"""
        return bool._wrap(super(_Range, self).contains(arg0))

    @staticmethod
    @overload
    def of(arg0: 'Comparable', arg1: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.of(T,T)"""
        return Range._wrap(_Range.of(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def fit(self, arg0: object) -> object:
        """public T org.apache.commons.lang3.Range.fit(T)"""
        return object._wrap(super(_Range, self).fit(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.Range.toString(java.lang.String)"""
        return str._wrap(super(_Range, self).toString(arg0))

    @override
    @overload
    def getMinimum(self) -> object:
        """public T org.apache.commons.lang3.Range.getMinimum()"""
        return object._wrap(super(Range, self).getMinimum())

    @overload
    def isOverlappedBy(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isOverlappedBy(org.apache.commons.lang3.Range<T>)"""
        return bool._wrap(super(_Range, self).isOverlappedBy(arg0))

    @staticmethod
    @overload
    def is(arg0: object, arg1: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.is(T,java.util.Comparator<T>)"""
        return Range._wrap(_Range.is(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.lang3.Functions$FailableBiConsumer
import org.apache.commons.lang3.Functions as _Functions_FailableBiConsumer
_FailableBiConsumer = _Functions_FailableBiConsumer.FailableBiConsumer
from abc import abstractmethod, ABC
 
class FailableBiConsumer():
    """org.apache.commons.lang3.Functions.FailableBiConsumer"""
 
    @staticmethod
    def _wrap(java_value: _FailableBiConsumer) -> 'FailableBiConsumer':
        return FailableBiConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableBiConsumer):
        """
        Dynamic initializer for FailableBiConsumer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableBiConsumer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableBiConsumer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def accept(self, arg0: object, arg1: object):
        """public abstract void org.apache.commons.lang3.Functions$FailableBiConsumer.accept(O1,O2) throws T"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.ClassUtils$Interfaces
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
import org.apache.commons.lang3.ClassUtils as _ClassUtils_Interfaces
_Interfaces = _ClassUtils_Interfaces.Interfaces
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
 
class Interfaces():
    """org.apache.commons.lang3.ClassUtils.Interfaces"""
 
    @staticmethod
    def _wrap(java_value: _Interfaces) -> 'Interfaces':
        return Interfaces(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Interfaces):
        """
        Dynamic initializer for Interfaces.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Interfaces__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Interfaces__wrapper":
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
    def valueOf(arg0: str) -> 'Interfaces':
        """public static org.apache.commons.lang3.ClassUtils$Interfaces org.apache.commons.lang3.ClassUtils$Interfaces.valueOf(java.lang.String)"""
        return Interfaces._wrap(_Interfaces.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['Interfaces']:
        """public static org.apache.commons.lang3.ClassUtils$Interfaces[] org.apache.commons.lang3.ClassUtils$Interfaces.values()"""
        return List[Interfaces]._wrap(_Interfaces.values())

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
 
 
# CLASS: org.apache.commons.lang3.Streams
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.util.Collection as Collection
import java.util.stream.Collector as Collector
import org.apache.commons.lang3.Streams as _Streams_FailableStream
_FailableStream = _Streams_FailableStream.FailableStream
import java.lang.String as _String
_String = _String
import java.util.stream.Collector as _Collector
_Collector = _Collector
import java.lang.Integer as _int
import org.apache.commons.lang3.Streams as _Streams
_Streams = _Streams
import java.util.stream.Stream as Stream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Streams():
    """org.apache.commons.lang3.Streams"""
 
    @staticmethod
    def _wrap(java_value: _Streams) -> 'Streams':
        return Streams(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Streams):
        """
        Dynamic initializer for Streams.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Streams__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Streams__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def toArray(arg0: 'Class') -> 'Collector':
        """public static <O> java.util.stream.Collector<O, ?, O[]> org.apache.commons.lang3.Streams.toArray(java.lang.Class<O>)"""
        return Collector._wrap(_Streams.toArray(arg0))

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

    @staticmethod
    @overload
    def stream(arg0: 'Stream') -> 'FailableStream':
        """public static <O> org.apache.commons.lang3.Streams$FailableStream<O> org.apache.commons.lang3.Streams.stream(java.util.stream.Stream<O>)"""
        return FailableStream._wrap(_Streams.stream(arg0))

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
    def __init__(self, ):
        """public org.apache.commons.lang3.Streams()"""
        val = _Streams()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def stream(arg0: 'Collection') -> 'FailableStream':
        """public static <O> org.apache.commons.lang3.Streams$FailableStream<O> org.apache.commons.lang3.Streams.stream(java.util.Collection<O>)"""
        return FailableStream._wrap(_Streams.stream(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.Streams()"""
        val = _Streams()
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
 
 
# CLASS: org.apache.commons.lang3.StringEscapeUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import org.apache.commons.lang3.StringEscapeUtils as _StringEscapeUtils
_StringEscapeUtils = _StringEscapeUtils
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StringEscapeUtils():
    """org.apache.commons.lang3.StringEscapeUtils"""
 
    @staticmethod
    def _wrap(java_value: _StringEscapeUtils) -> 'StringEscapeUtils':
        return StringEscapeUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StringEscapeUtils):
        """
        Dynamic initializer for StringEscapeUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StringEscapeUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StringEscapeUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public org.apache.commons.lang3.StringEscapeUtils()"""
        val = _StringEscapeUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def unescapeJava(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.unescapeJava(java.lang.String)"""
        return str._wrap(_StringEscapeUtils.unescapeJava(arg0))

    @staticmethod
    @overload
    def escapeHtml4(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.escapeHtml4(java.lang.String)"""
        return str._wrap(_StringEscapeUtils.escapeHtml4(arg0))

    @staticmethod
    @overload
    def unescapeHtml3(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.unescapeHtml3(java.lang.String)"""
        return str._wrap(_StringEscapeUtils.unescapeHtml3(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.StringEscapeUtils()"""
        val = _StringEscapeUtils()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def escapeXml10(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringEscapeUtils.escapeXml10(java.lang.String)"""
        return str._wrap(_StringEscapeUtils.escapeXml10(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def escapeCsv(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.escapeCsv(java.lang.String)"""
        return str._wrap(_StringEscapeUtils.escapeCsv(arg0))

    @staticmethod
    @overload
    def escapeXml11(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.StringEscapeUtils.escapeXml11(java.lang.String)"""
        return str._wrap(_StringEscapeUtils.escapeXml11(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def unescapeHtml4(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.unescapeHtml4(java.lang.String)"""
        return str._wrap(_StringEscapeUtils.unescapeHtml4(arg0))

    @staticmethod
    @overload
    def unescapeXml(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.unescapeXml(java.lang.String)"""
        return str._wrap(_StringEscapeUtils.unescapeXml(arg0))

    @staticmethod
    @overload
    def unescapeCsv(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.unescapeCsv(java.lang.String)"""
        return str._wrap(_StringEscapeUtils.unescapeCsv(arg0))

    @staticmethod
    @overload
    def unescapeEcmaScript(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.unescapeEcmaScript(java.lang.String)"""
        return str._wrap(_StringEscapeUtils.unescapeEcmaScript(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def escapeJava(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.escapeJava(java.lang.String)"""
        return str._wrap(_StringEscapeUtils.escapeJava(arg0))

    @staticmethod
    @overload
    def unescapeJson(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.unescapeJson(java.lang.String)"""
        return str._wrap(_StringEscapeUtils.unescapeJson(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def escapeJson(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.escapeJson(java.lang.String)"""
        return str._wrap(_StringEscapeUtils.escapeJson(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def escapeHtml3(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.escapeHtml3(java.lang.String)"""
        return str._wrap(_StringEscapeUtils.escapeHtml3(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def escapeXml(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.escapeXml(java.lang.String)"""
        return str._wrap(_StringEscapeUtils.escapeXml(arg0))

    @staticmethod
    @overload
    def escapeEcmaScript(arg0: str) -> str:
        """public static final java.lang.String org.apache.commons.lang3.StringEscapeUtils.escapeEcmaScript(java.lang.String)"""
        return str._wrap(_StringEscapeUtils.escapeEcmaScript(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.Streams$FailableStream
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.Streams as _Streams_FailableStream
_FailableStream = _Streams_FailableStream.FailableStream
import java.util.stream.Collector as Collector
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiConsumer as BiConsumer
import java.lang.Integer as _int
import java.util.function.BinaryOperator as BinaryOperator
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FailableStream():
    """org.apache.commons.lang3.Streams.FailableStream"""
 
    @staticmethod
    def _wrap(java_value: _FailableStream) -> 'FailableStream':
        return FailableStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableStream):
        """
        Dynamic initializer for FailableStream.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableStream__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableStream__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def filter(self, arg0: 'FailablePredicate') -> 'FailableStream':
        """public org.apache.commons.lang3.Streams$FailableStream<O> org.apache.commons.lang3.Streams$FailableStream.filter(org.apache.commons.lang3.Functions$FailablePredicate<O, ?>)"""
        return 'FailableStream'._wrap(super(_FailableStream, self).filter(arg0))

    @overload
    def __init__(self, arg0: 'Stream'):
        """public org.apache.commons.lang3.Streams$FailableStream(java.util.stream.Stream<O>)"""
        val = _FailableStream(arg0)
        self.__wrapper = val

    @overload
    def map(self, arg0: 'FailableFunction') -> 'FailableStream':
        """public <R> org.apache.commons.lang3.Streams$FailableStream<R> org.apache.commons.lang3.Streams$FailableStream.map(org.apache.commons.lang3.Functions$FailableFunction<O, R, ?>)"""
        return 'FailableStream'._wrap(super(_FailableStream, self).map(arg0))

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
    def collect(self, arg0: 'Collector') -> object:
        """public <A,R> R org.apache.commons.lang3.Streams$FailableStream.collect(java.util.stream.Collector<? super O, A, R>)"""
        return object._wrap(super(_FailableStream, self).collect(arg0))

    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<O> org.apache.commons.lang3.Streams$FailableStream.stream()"""
        return 'Stream'._wrap(super(FailableStream, self).stream())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def anyMatch(self, arg0: 'FailablePredicate') -> bool:
        """public boolean org.apache.commons.lang3.Streams$FailableStream.anyMatch(org.apache.commons.lang3.Functions$FailablePredicate<O, ?>)"""
        return bool._wrap(super(_FailableStream, self).anyMatch(arg0))

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
    def reduce(self, arg0: object, arg1: 'BinaryOperator') -> object:
        """public O org.apache.commons.lang3.Streams$FailableStream.reduce(O,java.util.function.BinaryOperator<O>)"""
        return object._wrap(super(_FailableStream, self).reduce(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def collect(self, arg0: 'Supplier', arg1: 'BiConsumer', arg2: 'BiConsumer') -> object:
        """public <A,R> R org.apache.commons.lang3.Streams$FailableStream.collect(java.util.function.Supplier<R>,java.util.function.BiConsumer<R, ? super O>,java.util.function.BiConsumer<R, R>)"""
        return object._wrap(super(_FailableStream, self).collect(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def allMatch(self, arg0: 'FailablePredicate') -> bool:
        """public boolean org.apache.commons.lang3.Streams$FailableStream.allMatch(org.apache.commons.lang3.Functions$FailablePredicate<O, ?>)"""
        return bool._wrap(super(_FailableStream, self).allMatch(arg0))

    @overload
    def forEach(self, arg0: 'FailableConsumer'):
        """public void org.apache.commons.lang3.Streams$FailableStream.forEach(org.apache.commons.lang3.Functions$FailableConsumer<O, ?>)"""
        super(_FailableStream, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.CharUtils
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
import java.lang.Integer as _int
import java.lang.Character as _Character
_Character = _Character
import java.lang.Character as Character
from builtins import bool
import org.apache.commons.lang3.CharUtils as _CharUtils
_CharUtils = _CharUtils
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CharUtils():
    """org.apache.commons.lang3.CharUtils"""
 
    @staticmethod
    def _wrap(java_value: _CharUtils) -> 'CharUtils':
        return CharUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CharUtils):
        """
        Dynamic initializer for CharUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CharUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CharUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def toString(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.CharUtils.toString(char)"""
        return str._wrap(_CharUtils.toString(_char.valueOf(arg0)))

    @staticmethod
    @overload
    def toChar(arg0: 'Character', arg1: str) -> str:
        """public static char org.apache.commons.lang3.CharUtils.toChar(java.lang.Character,char)"""
        return str._wrap(_CharUtils.toChar(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def toString(arg0: 'Character') -> str:
        """public static java.lang.String org.apache.commons.lang3.CharUtils.toString(java.lang.Character)"""
        return str._wrap(_CharUtils.toString(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def toIntValue(arg0: 'Character', arg1: int) -> int:
        """public static int org.apache.commons.lang3.CharUtils.toIntValue(java.lang.Character,int)"""
        return int._wrap(_CharUtils.toIntValue(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def toCharacterObject(arg0: str) -> 'Character':
        """public static java.lang.Character org.apache.commons.lang3.CharUtils.toCharacterObject(char)"""
        return Character._wrap(_CharUtils.toCharacterObject(_char.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def isAsciiAlphanumeric(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.CharUtils.isAsciiAlphanumeric(char)"""
        return bool._wrap(_CharUtils.isAsciiAlphanumeric(_char.valueOf(arg0)))

    @staticmethod
    @overload
    def toIntValue(arg0: 'Character') -> int:
        """public static int org.apache.commons.lang3.CharUtils.toIntValue(java.lang.Character)"""
        return int._wrap(_CharUtils.toIntValue(arg0))

    @staticmethod
    @overload
    def toIntValue(arg0: str) -> int:
        """public static int org.apache.commons.lang3.CharUtils.toIntValue(char)"""
        return int._wrap(_CharUtils.toIntValue(_char.valueOf(arg0)))

    @staticmethod
    @overload
    def isAsciiAlpha(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.CharUtils.isAsciiAlpha(char)"""
        return bool._wrap(_CharUtils.isAsciiAlpha(_char.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def isAsciiControl(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.CharUtils.isAsciiControl(char)"""
        return bool._wrap(_CharUtils.isAsciiControl(_char.valueOf(arg0)))

    @staticmethod
    @overload
    def isAscii(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.CharUtils.isAscii(char)"""
        return bool._wrap(_CharUtils.isAscii(_char.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def toIntValue(arg0: str, arg1: int) -> int:
        """public static int org.apache.commons.lang3.CharUtils.toIntValue(char,int)"""
        return int._wrap(_CharUtils.toIntValue(_char.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def toCharacterObject(arg0: str) -> 'Character':
        """public static java.lang.Character org.apache.commons.lang3.CharUtils.toCharacterObject(java.lang.String)"""
        return Character._wrap(_CharUtils.toCharacterObject(arg0))

    @staticmethod
    @overload
    def unicodeEscaped(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.CharUtils.unicodeEscaped(char)"""
        return str._wrap(_CharUtils.unicodeEscaped(_char.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def toChar(arg0: str) -> str:
        """public static char org.apache.commons.lang3.CharUtils.toChar(java.lang.String)"""
        return str._wrap(_CharUtils.toChar(arg0))

    @staticmethod
    @overload
    def isAsciiAlphaLower(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.CharUtils.isAsciiAlphaLower(char)"""
        return bool._wrap(_CharUtils.isAsciiAlphaLower(_char.valueOf(arg0)))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.CharUtils()"""
        val = _CharUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def isAsciiAlphaUpper(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.CharUtils.isAsciiAlphaUpper(char)"""
        return bool._wrap(_CharUtils.isAsciiAlphaUpper(_char.valueOf(arg0)))

    @staticmethod
    @overload
    def isAsciiNumeric(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.CharUtils.isAsciiNumeric(char)"""
        return bool._wrap(_CharUtils.isAsciiNumeric(_char.valueOf(arg0)))

    @staticmethod
    @overload
    def isAsciiPrintable(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.CharUtils.isAsciiPrintable(char)"""
        return bool._wrap(_CharUtils.isAsciiPrintable(_char.valueOf(arg0)))

    @staticmethod
    @overload
    def unicodeEscaped(arg0: 'Character') -> str:
        """public static java.lang.String org.apache.commons.lang3.CharUtils.unicodeEscaped(java.lang.Character)"""
        return str._wrap(_CharUtils.unicodeEscaped(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.CharUtils()"""
        val = _CharUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def toChar(arg0: str, arg1: str) -> str:
        """public static char org.apache.commons.lang3.CharUtils.toChar(java.lang.String,char)"""
        return str._wrap(_CharUtils.toChar(arg0, _char.valueOf(arg1)))

    @staticmethod
    @overload
    def compare(arg0: str, arg1: str) -> int:
        """public static int org.apache.commons.lang3.CharUtils.compare(char,char)"""
        return int._wrap(_CharUtils.compare(_char.valueOf(arg0), _char.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def toChar(arg0: 'Character') -> str:
        """public static char org.apache.commons.lang3.CharUtils.toChar(java.lang.Character)"""
        return str._wrap(_CharUtils.toChar(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.RegExUtils
from builtins import str
import java.util.regex.Pattern as _Pattern
_Pattern = _Pattern
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.regex.Matcher as Matcher
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import java.util.regex.Matcher as _Matcher
_Matcher = _Matcher
import java.util.regex.Pattern as Pattern
import org.apache.commons.lang3.RegExUtils as _RegExUtils
_RegExUtils = _RegExUtils
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RegExUtils():
    """org.apache.commons.lang3.RegExUtils"""
 
    @staticmethod
    def _wrap(java_value: _RegExUtils) -> 'RegExUtils':
        return RegExUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RegExUtils):
        """
        Dynamic initializer for RegExUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RegExUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RegExUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def dotAllMatcher(arg0: str, arg1: str) -> 'Matcher':
        """public static java.util.regex.Matcher org.apache.commons.lang3.RegExUtils.dotAllMatcher(java.lang.String,java.lang.String)"""
        return Matcher._wrap(_RegExUtils.dotAllMatcher(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def removeAll(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.RegExUtils.removeAll(java.lang.String,java.lang.String)"""
        return str._wrap(_RegExUtils.removeAll(arg0, arg1))

    @staticmethod
    @overload
    def replacePattern(arg0: str, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.RegExUtils.replacePattern(java.lang.String,java.lang.String,java.lang.String)"""
        return str._wrap(_RegExUtils.replacePattern(arg0, arg1, arg2))

    @staticmethod
    @overload
    def replaceFirst(arg0: str, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.RegExUtils.replaceFirst(java.lang.String,java.lang.String,java.lang.String)"""
        return str._wrap(_RegExUtils.replaceFirst(arg0, arg1, arg2))

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

    @staticmethod
    @overload
    def replaceFirst(arg0: str, arg1: 'Pattern', arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.RegExUtils.replaceFirst(java.lang.String,java.util.regex.Pattern,java.lang.String)"""
        return str._wrap(_RegExUtils.replaceFirst(arg0, arg1, arg2))

    @staticmethod
    @overload
    def replaceAll(arg0: str, arg1: 'Pattern', arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.RegExUtils.replaceAll(java.lang.String,java.util.regex.Pattern,java.lang.String)"""
        return str._wrap(_RegExUtils.replaceAll(arg0, arg1, arg2))

    @staticmethod
    @overload
    def replaceAll(arg0: str, arg1: str, arg2: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.RegExUtils.replaceAll(java.lang.String,java.lang.String,java.lang.String)"""
        return str._wrap(_RegExUtils.replaceAll(arg0, arg1, arg2))

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

    @staticmethod
    @overload
    def removeAll(arg0: str, arg1: 'Pattern') -> str:
        """public static java.lang.String org.apache.commons.lang3.RegExUtils.removeAll(java.lang.String,java.util.regex.Pattern)"""
        return str._wrap(_RegExUtils.removeAll(arg0, arg1))

    @staticmethod
    @overload
    def removeFirst(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.RegExUtils.removeFirst(java.lang.String,java.lang.String)"""
        return str._wrap(_RegExUtils.removeFirst(arg0, arg1))

    @staticmethod
    @overload
    def removeFirst(arg0: str, arg1: 'Pattern') -> str:
        """public static java.lang.String org.apache.commons.lang3.RegExUtils.removeFirst(java.lang.String,java.util.regex.Pattern)"""
        return str._wrap(_RegExUtils.removeFirst(arg0, arg1))

    @staticmethod
    @overload
    def dotAll(arg0: str) -> 'Pattern':
        """public static java.util.regex.Pattern org.apache.commons.lang3.RegExUtils.dotAll(java.lang.String)"""
        return Pattern._wrap(_RegExUtils.dotAll(arg0))

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
    def __init__(self):
        """public org.apache.commons.lang3.RegExUtils()"""
        val = _RegExUtils()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.RegExUtils()"""
        val = _RegExUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def removePattern(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.RegExUtils.removePattern(java.lang.String,java.lang.String)"""
        return str._wrap(_RegExUtils.removePattern(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.Range
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Comparable as Comparable
from builtins import object
import java.lang.String as _string
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import org.apache.commons.lang3.Range as _Range
_Range = _Range
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Range():
    """org.apache.commons.lang3.Range"""
 
    @staticmethod
    def _wrap(java_value: _Range) -> 'Range':
        return Range(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Range):
        """
        Dynamic initializer for Range.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Range__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Range__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def intersectionWith(self, arg0: 'Range') -> 'Range':
        """public org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.intersectionWith(org.apache.commons.lang3.Range<T>)"""
        return 'Range'._wrap(super(_Range, self).intersectionWith(arg0))

    @overload
    def isBeforeRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isBeforeRange(org.apache.commons.lang3.Range<T>)"""
        return bool._wrap(super(_Range, self).isBeforeRange(arg0))

    @staticmethod
    @overload
    def is(arg0: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.is(T)"""
        return Range._wrap(_Range.is(arg0))

    @overload
    def isAfter(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isAfter(T)"""
        return bool._wrap(super(_Range, self).isAfter(arg0))

    @overload
    def containsRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.containsRange(org.apache.commons.lang3.Range<T>)"""
        return bool._wrap(super(_Range, self).containsRange(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.Range.toString()"""
        return str._wrap(super(Range, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.Range.hashCode()"""
        return int._wrap(super(Range, self).hashCode())

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
    def isEndedBy(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isEndedBy(T)"""
        return bool._wrap(super(_Range, self).isEndedBy(arg0))

    @overload
    def elementCompareTo(self, arg0: object) -> int:
        """public int org.apache.commons.lang3.Range.elementCompareTo(T)"""
        return int._wrap(super(_Range, self).elementCompareTo(arg0))

    @overload
    def getMaximum(self) -> object:
        """public T org.apache.commons.lang3.Range.getMaximum()"""
        return object._wrap(super(Range, self).getMaximum())

    @overload
    def isStartedBy(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isStartedBy(T)"""
        return bool._wrap(super(_Range, self).isStartedBy(arg0))

    @overload
    def getComparator(self) -> 'Comparator':
        """public java.util.Comparator<T> org.apache.commons.lang3.Range.getComparator()"""
        return 'Comparator'._wrap(super(Range, self).getComparator())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.equals(java.lang.Object)"""
        return bool._wrap(super(_Range, self).equals(arg0))

    @overload
    def isBefore(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isBefore(T)"""
        return bool._wrap(super(_Range, self).isBefore(arg0))

    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.of(T,T,java.util.Comparator<T>)"""
        return Range._wrap(_Range.of(arg0, arg1, arg2))

    @staticmethod
    @overload
    def between(arg0: object, arg1: object, arg2: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.between(T,T,java.util.Comparator<T>)"""
        return Range._wrap(_Range.between(arg0, arg1, arg2))

    @overload
    def isAfterRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isAfterRange(org.apache.commons.lang3.Range<T>)"""
        return bool._wrap(super(_Range, self).isAfterRange(arg0))

    @staticmethod
    @overload
    def between(arg0: 'Comparable', arg1: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.between(T,T)"""
        return Range._wrap(_Range.between(arg0, arg1))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.contains(T)"""
        return bool._wrap(super(_Range, self).contains(arg0))

    @staticmethod
    @overload
    def of(arg0: 'Comparable', arg1: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.of(T,T)"""
        return Range._wrap(_Range.of(arg0, arg1))

    @overload
    def getMinimum(self) -> object:
        """public T org.apache.commons.lang3.Range.getMinimum()"""
        return object._wrap(super(Range, self).getMinimum())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def fit(self, arg0: object) -> object:
        """public T org.apache.commons.lang3.Range.fit(T)"""
        return object._wrap(super(_Range, self).fit(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.Range.toString(java.lang.String)"""
        return str._wrap(super(_Range, self).toString(arg0))

    @overload
    def isOverlappedBy(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isOverlappedBy(org.apache.commons.lang3.Range<T>)"""
        return bool._wrap(super(_Range, self).isOverlappedBy(arg0))

    @overload
    def isNaturalOrdering(self) -> bool:
        """public boolean org.apache.commons.lang3.Range.isNaturalOrdering()"""
        return bool._wrap(super(Range, self).isNaturalOrdering())

    @staticmethod
    @overload
    def is(arg0: object, arg1: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.is(T,java.util.Comparator<T>)"""
        return Range._wrap(_Range.is(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.lang3.SystemUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.File as File
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.io.File as _File
_File = _File
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import org.apache.commons.lang3.SystemUtils as _SystemUtils
_SystemUtils = _SystemUtils
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SystemUtils():
    """org.apache.commons.lang3.SystemUtils"""
 
    @staticmethod
    def _wrap(java_value: _SystemUtils) -> 'SystemUtils':
        return SystemUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SystemUtils):
        """
        Dynamic initializer for SystemUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SystemUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SystemUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getUserName(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemUtils.getUserName(java.lang.String)"""
        return str._wrap(_SystemUtils.getUserName(arg0))

    @staticmethod
    @overload
    def getHostName() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemUtils.getHostName()"""
        return str._wrap(_SystemUtils.getHostName())

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
        """public org.apache.commons.lang3.SystemUtils()"""
        val = _SystemUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def getUserHome() -> 'File':
        """public static java.io.File org.apache.commons.lang3.SystemUtils.getUserHome()"""
        return File._wrap(_SystemUtils.getUserHome())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def isJavaAwtHeadless() -> bool:
        """public static boolean org.apache.commons.lang3.SystemUtils.isJavaAwtHeadless()"""
        return bool._wrap(_SystemUtils.isJavaAwtHeadless())

    @staticmethod
    @overload
    def getUserDir() -> 'File':
        """public static java.io.File org.apache.commons.lang3.SystemUtils.getUserDir()"""
        return File._wrap(_SystemUtils.getUserDir())

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

    @staticmethod
    @overload
    def isJavaVersionAtLeast(arg0: 'JavaVersion') -> bool:
        """public static boolean org.apache.commons.lang3.SystemUtils.isJavaVersionAtLeast(org.apache.commons.lang3.JavaVersion)"""
        return bool._wrap(_SystemUtils.isJavaVersionAtLeast(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getEnvironmentVariable(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemUtils.getEnvironmentVariable(java.lang.String,java.lang.String)"""
        return str._wrap(_SystemUtils.getEnvironmentVariable(arg0, arg1))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.SystemUtils()"""
        val = _SystemUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def getUserName() -> str:
        """public static java.lang.String org.apache.commons.lang3.SystemUtils.getUserName()"""
        return str._wrap(_SystemUtils.getUserName())

    @staticmethod
    @overload
    def getJavaHome() -> 'File':
        """public static java.io.File org.apache.commons.lang3.SystemUtils.getJavaHome()"""
        return File._wrap(_SystemUtils.getJavaHome())

    @staticmethod
    @overload
    def getJavaIoTmpDir() -> 'File':
        """public static java.io.File org.apache.commons.lang3.SystemUtils.getJavaIoTmpDir()"""
        return File._wrap(_SystemUtils.getJavaIoTmpDir())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def isJavaVersionAtMost(arg0: 'JavaVersion') -> bool:
        """public static boolean org.apache.commons.lang3.SystemUtils.isJavaVersionAtMost(org.apache.commons.lang3.JavaVersion)"""
        return bool._wrap(_SystemUtils.isJavaVersionAtMost(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.ObjectUtils$Null
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.ObjectUtils as _ObjectUtils_Null
_Null = _ObjectUtils_Null.Null
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Null():
    """org.apache.commons.lang3.ObjectUtils.Null"""
 
    @staticmethod
    def _wrap(java_value: _Null) -> 'Null':
        return Null(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Null):
        """
        Dynamic initializer for Null.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Null__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Null__wrapper":
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
 
 
# CLASS: org.apache.commons.lang3.ClassUtils
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.String as _string
import java.lang.Boolean as _boolean
import org.apache.commons.lang3.ClassUtils as _ClassUtils
_ClassUtils = _ClassUtils
import java.lang.ClassLoader as ClassLoader
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.Iterable as Iterable
import java.lang.reflect.Method as _Method
_Method = _Method
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.List as _List
_List = _List
from typing import List
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
import java.util.List as List
import java.lang.reflect.Method as Method
from builtins import int
 
class ClassUtils():
    """org.apache.commons.lang3.ClassUtils"""
 
    @staticmethod
    def _wrap(java_value: _ClassUtils) -> 'ClassUtils':
        return ClassUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClassUtils):
        """
        Dynamic initializer for ClassUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClassUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClassUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getName(arg0: object, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getName(java.lang.Object,java.lang.String)"""
        return str._wrap(_ClassUtils.getName(arg0, arg1))

    @staticmethod
    @overload
    def getShortClassName(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getShortClassName(java.lang.String)"""
        return str._wrap(_ClassUtils.getShortClassName(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def primitiveToWrapper(arg0: 'Class') -> 'type.Class':
        """public static java.lang.Class<?> org.apache.commons.lang3.ClassUtils.primitiveToWrapper(java.lang.Class<?>)"""
        return type.Class._wrap(_ClassUtils.primitiveToWrapper(arg0))

    @staticmethod
    @overload
    def getPackageName(arg0: object, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getPackageName(java.lang.Object,java.lang.String)"""
        return str._wrap(_ClassUtils.getPackageName(arg0, arg1))

    @staticmethod
    @overload
    def isPublic(arg0: 'Class') -> bool:
        """public static boolean org.apache.commons.lang3.ClassUtils.isPublic(java.lang.Class<?>)"""
        return bool._wrap(_ClassUtils.isPublic(arg0))

    @staticmethod
    @overload
    def isAssignable(arg0: 'Class', arg1: 'Class', arg2: bool) -> bool:
        """public static boolean org.apache.commons.lang3.ClassUtils.isAssignable(java.lang.Class<?>[],java.lang.Class<?>[],boolean)"""
        return bool._wrap(_ClassUtils.isAssignable(arg0, arg1, _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def isPrimitiveOrWrapper(arg0: 'Class') -> bool:
        """public static boolean org.apache.commons.lang3.ClassUtils.isPrimitiveOrWrapper(java.lang.Class<?>)"""
        return bool._wrap(_ClassUtils.isPrimitiveOrWrapper(arg0))

    @staticmethod
    @overload
    def wrappersToPrimitives(*arg0: 'type.Class') -> List['type.Class']:
        """public static java.lang.Class<?>[] org.apache.commons.lang3.ClassUtils.wrappersToPrimitives(java.lang.Class<?>...)"""
        return List[type.Class]._wrap(_ClassUtils.wrappersToPrimitives(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def getPackageCanonicalName(arg0: 'Class') -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getPackageCanonicalName(java.lang.Class<?>)"""
        return str._wrap(_ClassUtils.getPackageCanonicalName(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def wrapperToPrimitive(arg0: 'Class') -> 'type.Class':
        """public static java.lang.Class<?> org.apache.commons.lang3.ClassUtils.wrapperToPrimitive(java.lang.Class<?>)"""
        return type.Class._wrap(_ClassUtils.wrapperToPrimitive(arg0))

    @staticmethod
    @overload
    def getShortCanonicalName(arg0: 'Class') -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getShortCanonicalName(java.lang.Class<?>)"""
        return str._wrap(_ClassUtils.getShortCanonicalName(arg0))

    @staticmethod
    @overload
    def convertClassNamesToClasses(arg0: 'List') -> 'List':
        """public static java.util.List<java.lang.Class<?>> org.apache.commons.lang3.ClassUtils.convertClassNamesToClasses(java.util.List<java.lang.String>)"""
        return List._wrap(_ClassUtils.convertClassNamesToClasses(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def primitivesToWrappers(*arg0: 'type.Class') -> List['type.Class']:
        """public static java.lang.Class<?>[] org.apache.commons.lang3.ClassUtils.primitivesToWrappers(java.lang.Class<?>...)"""
        return List[type.Class]._wrap(_ClassUtils.primitivesToWrappers(arg0))

    @staticmethod
    @overload
    def getAbbreviatedName(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getAbbreviatedName(java.lang.String,int)"""
        return str._wrap(_ClassUtils.getAbbreviatedName(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def getClass(arg0: 'ClassLoader', arg1: str) -> 'type.Class':
        """public static java.lang.Class<?> org.apache.commons.lang3.ClassUtils.getClass(java.lang.ClassLoader,java.lang.String) throws java.lang.ClassNotFoundException"""
        return type.Class._wrap(_ClassUtils.getClass(arg0, arg1))

    @staticmethod
    @overload
    def getPackageName(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getPackageName(java.lang.String)"""
        return str._wrap(_ClassUtils.getPackageName(arg0))

    @staticmethod
    @overload
    def getShortCanonicalName(arg0: object, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getShortCanonicalName(java.lang.Object,java.lang.String)"""
        return str._wrap(_ClassUtils.getShortCanonicalName(arg0, arg1))

    @staticmethod
    @overload
    def isAssignable(arg0: 'Class', *arg1: 'type.Class') -> bool:
        """public static boolean org.apache.commons.lang3.ClassUtils.isAssignable(java.lang.Class<?>[],java.lang.Class<?>...)"""
        return bool._wrap(_ClassUtils.isAssignable(arg0, arg1))

    @staticmethod
    @overload
    def toClass(*arg0: object) -> List['type.Class']:
        """public static java.lang.Class<?>[] org.apache.commons.lang3.ClassUtils.toClass(java.lang.Object...)"""
        return List[type.Class]._wrap(_ClassUtils.toClass(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getName(arg0: 'Class', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getName(java.lang.Class<?>,java.lang.String)"""
        return str._wrap(_ClassUtils.getName(arg0, arg1))

    @staticmethod
    @overload
    def getCanonicalName(arg0: 'Class', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getCanonicalName(java.lang.Class<?>,java.lang.String)"""
        return str._wrap(_ClassUtils.getCanonicalName(arg0, arg1))

    @staticmethod
    @overload
    def getCanonicalName(arg0: object, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getCanonicalName(java.lang.Object,java.lang.String)"""
        return str._wrap(_ClassUtils.getCanonicalName(arg0, arg1))

    @staticmethod
    @overload
    def getAllSuperclasses(arg0: 'Class') -> 'List':
        """public static java.util.List<java.lang.Class<?>> org.apache.commons.lang3.ClassUtils.getAllSuperclasses(java.lang.Class<?>)"""
        return List._wrap(_ClassUtils.getAllSuperclasses(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def hierarchy(arg0: 'Class') -> 'Iterable':
        """public static java.lang.Iterable<java.lang.Class<?>> org.apache.commons.lang3.ClassUtils.hierarchy(java.lang.Class<?>)"""
        return Iterable._wrap(_ClassUtils.hierarchy(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def convertClassesToClassNames(arg0: 'List') -> 'List':
        """public static java.util.List<java.lang.String> org.apache.commons.lang3.ClassUtils.convertClassesToClassNames(java.util.List<java.lang.Class<?>>)"""
        return List._wrap(_ClassUtils.convertClassesToClassNames(arg0))

    @staticmethod
    @overload
    def getAbbreviatedName(arg0: 'Class', arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getAbbreviatedName(java.lang.Class<?>,int)"""
        return str._wrap(_ClassUtils.getAbbreviatedName(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def isAssignable(arg0: 'Class', arg1: 'Class', arg2: bool) -> bool:
        """public static boolean org.apache.commons.lang3.ClassUtils.isAssignable(java.lang.Class<?>,java.lang.Class<?>,boolean)"""
        return bool._wrap(_ClassUtils.isAssignable(arg0, arg1, _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def getShortClassName(arg0: object, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getShortClassName(java.lang.Object,java.lang.String)"""
        return str._wrap(_ClassUtils.getShortClassName(arg0, arg1))

    @staticmethod
    @overload
    def getAllInterfaces(arg0: 'Class') -> 'List':
        """public static java.util.List<java.lang.Class<?>> org.apache.commons.lang3.ClassUtils.getAllInterfaces(java.lang.Class<?>)"""
        return List._wrap(_ClassUtils.getAllInterfaces(arg0))

    @staticmethod
    @overload
    def getShortCanonicalName(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getShortCanonicalName(java.lang.String)"""
        return str._wrap(_ClassUtils.getShortCanonicalName(arg0))

    @staticmethod
    @overload
    def getName(arg0: object) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getName(java.lang.Object)"""
        return str._wrap(_ClassUtils.getName(arg0))

    @staticmethod
    @overload
    def getPackageName(arg0: 'Class') -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getPackageName(java.lang.Class<?>)"""
        return str._wrap(_ClassUtils.getPackageName(arg0))

    @staticmethod
    @overload
    def getClass(arg0: str) -> 'type.Class':
        """public static java.lang.Class<?> org.apache.commons.lang3.ClassUtils.getClass(java.lang.String) throws java.lang.ClassNotFoundException"""
        return type.Class._wrap(_ClassUtils.getClass(arg0))

    @staticmethod
    @overload
    def isAssignable(arg0: 'Class', arg1: 'Class') -> bool:
        """public static boolean org.apache.commons.lang3.ClassUtils.isAssignable(java.lang.Class<?>,java.lang.Class<?>)"""
        return bool._wrap(_ClassUtils.isAssignable(arg0, arg1))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.ClassUtils()"""
        val = _ClassUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def getPackageCanonicalName(arg0: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getPackageCanonicalName(java.lang.String)"""
        return str._wrap(_ClassUtils.getPackageCanonicalName(arg0))

    @staticmethod
    @overload
    def getClass(arg0: str, arg1: bool) -> 'type.Class':
        """public static java.lang.Class<?> org.apache.commons.lang3.ClassUtils.getClass(java.lang.String,boolean) throws java.lang.ClassNotFoundException"""
        return type.Class._wrap(_ClassUtils.getClass(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def getShortClassName(arg0: 'Class') -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getShortClassName(java.lang.Class<?>)"""
        return str._wrap(_ClassUtils.getShortClassName(arg0))

    @staticmethod
    @overload
    def getCanonicalName(arg0: 'Class') -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getCanonicalName(java.lang.Class<?>)"""
        return str._wrap(_ClassUtils.getCanonicalName(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getSimpleName(arg0: 'Class') -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getSimpleName(java.lang.Class<?>)"""
        return str._wrap(_ClassUtils.getSimpleName(arg0))

    @staticmethod
    @overload
    def comparator() -> 'Comparator':
        """public static java.util.Comparator<java.lang.Class<?>> org.apache.commons.lang3.ClassUtils.comparator()"""
        return Comparator._wrap(_ClassUtils.comparator())

    @staticmethod
    @overload
    def getClass(arg0: 'ClassLoader', arg1: str, arg2: bool) -> 'type.Class':
        """public static java.lang.Class<?> org.apache.commons.lang3.ClassUtils.getClass(java.lang.ClassLoader,java.lang.String,boolean) throws java.lang.ClassNotFoundException"""
        return type.Class._wrap(_ClassUtils.getClass(arg0, arg1, _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def getPackageCanonicalName(arg0: object, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getPackageCanonicalName(java.lang.Object,java.lang.String)"""
        return str._wrap(_ClassUtils.getPackageCanonicalName(arg0, arg1))

    @staticmethod
    @overload
    def isPrimitiveWrapper(arg0: 'Class') -> bool:
        """public static boolean org.apache.commons.lang3.ClassUtils.isPrimitiveWrapper(java.lang.Class<?>)"""
        return bool._wrap(_ClassUtils.isPrimitiveWrapper(arg0))

    @staticmethod
    @overload
    def getName(arg0: 'Class') -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getName(java.lang.Class<?>)"""
        return str._wrap(_ClassUtils.getName(arg0))

    @staticmethod
    @overload
    def hierarchy(arg0: 'Class', arg1: 'Interfaces') -> 'Iterable':
        """public static java.lang.Iterable<java.lang.Class<?>> org.apache.commons.lang3.ClassUtils.hierarchy(java.lang.Class<?>,org.apache.commons.lang3.ClassUtils$Interfaces)"""
        return Iterable._wrap(_ClassUtils.hierarchy(arg0, arg1))

    @staticmethod
    @overload
    def getPublicMethod(arg0: 'Class', arg1: str, *arg2: 'type.Class') -> 'Method':
        """public static java.lang.reflect.Method org.apache.commons.lang3.ClassUtils.getPublicMethod(java.lang.Class<?>,java.lang.String,java.lang.Class<?>...) throws java.lang.NoSuchMethodException"""
        return Method._wrap(_ClassUtils.getPublicMethod(arg0, arg1, arg2))

    @staticmethod
    @overload
    def getSimpleName(arg0: object, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getSimpleName(java.lang.Object,java.lang.String)"""
        return str._wrap(_ClassUtils.getSimpleName(arg0, arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.ClassUtils()"""
        val = _ClassUtils()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getSimpleName(arg0: 'Class', arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getSimpleName(java.lang.Class<?>,java.lang.String)"""
        return str._wrap(_ClassUtils.getSimpleName(arg0, arg1))

    @staticmethod
    @overload
    def getCanonicalName(arg0: object) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getCanonicalName(java.lang.Object)"""
        return str._wrap(_ClassUtils.getCanonicalName(arg0))

    @staticmethod
    @overload
    def getComponentType(arg0: 'Class') -> 'type.Class':
        """public static <T> java.lang.Class<T> org.apache.commons.lang3.ClassUtils.getComponentType(java.lang.Class<T[]>)"""
        return type.Class._wrap(_ClassUtils.getComponentType(arg0))

    @staticmethod
    @overload
    def isInnerClass(arg0: 'Class') -> bool:
        """public static boolean org.apache.commons.lang3.ClassUtils.isInnerClass(java.lang.Class<?>)"""
        return bool._wrap(_ClassUtils.isInnerClass(arg0))

    @staticmethod
    @overload
    def getSimpleName(arg0: object) -> str:
        """public static java.lang.String org.apache.commons.lang3.ClassUtils.getSimpleName(java.lang.Object)"""
        return str._wrap(_ClassUtils.getSimpleName(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.DoubleRange
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import org.apache.commons.lang3.DoubleRange as _DoubleRange
_DoubleRange = _DoubleRange
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Comparable as Comparable
from builtins import object
import java.lang.String as _string
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import org.apache.commons.lang3.Range as _Range
_Range = _Range
from builtins import bool
import java.lang.Double as Double
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DoubleRange():
    """org.apache.commons.lang3.DoubleRange"""
 
    @staticmethod
    def _wrap(java_value: _DoubleRange) -> 'DoubleRange':
        return DoubleRange(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DoubleRange):
        """
        Dynamic initializer for DoubleRange.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DoubleRange__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DoubleRange__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def intersectionWith(self, arg0: 'Range') -> 'Range':
        """public org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.intersectionWith(org.apache.commons.lang3.Range<T>)"""
        return 'Range'._wrap(super(_Range, self).intersectionWith(arg0))

    @overload
    def isBeforeRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isBeforeRange(org.apache.commons.lang3.Range<T>)"""
        return bool._wrap(super(_Range, self).isBeforeRange(arg0))

    @staticmethod
    @overload
    def is(arg0: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.is(T)"""
        return Range._wrap(_Range.is(arg0))

    @overload
    def isAfter(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isAfter(T)"""
        return bool._wrap(super(_Range, self).isAfter(arg0))

    @overload
    def containsRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.containsRange(org.apache.commons.lang3.Range<T>)"""
        return bool._wrap(super(_Range, self).containsRange(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.Range.toString()"""
        return str._wrap(super(Range, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.Range.hashCode()"""
        return int._wrap(super(Range, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def of(arg0: float, arg1: float) -> 'DoubleRange':
        """public static org.apache.commons.lang3.DoubleRange org.apache.commons.lang3.DoubleRange.of(double,double)"""
        return DoubleRange._wrap(_DoubleRange.of(_double.valueOf(arg0), _double.valueOf(arg1)))

    @override
    @overload
    def isNaturalOrdering(self) -> bool:
        """public boolean org.apache.commons.lang3.Range.isNaturalOrdering()"""
        return bool._wrap(super(Range, self).isNaturalOrdering())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def isEndedBy(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isEndedBy(T)"""
        return bool._wrap(super(_Range, self).isEndedBy(arg0))

    @staticmethod
    @overload
    def of(arg0: 'Double', arg1: 'Double') -> 'DoubleRange':
        """public static org.apache.commons.lang3.DoubleRange org.apache.commons.lang3.DoubleRange.of(java.lang.Double,java.lang.Double)"""
        return DoubleRange._wrap(_DoubleRange.of(arg0, arg1))

    @overload
    def elementCompareTo(self, arg0: object) -> int:
        """public int org.apache.commons.lang3.Range.elementCompareTo(T)"""
        return int._wrap(super(_Range, self).elementCompareTo(arg0))

    @override
    @overload
    def getComparator(self) -> 'Comparator':
        """public java.util.Comparator<T> org.apache.commons.lang3.Range.getComparator()"""
        return 'Comparator'._wrap(super(Range, self).getComparator())

    @overload
    def isStartedBy(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isStartedBy(T)"""
        return bool._wrap(super(_Range, self).isStartedBy(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.equals(java.lang.Object)"""
        return bool._wrap(super(_Range, self).equals(arg0))

    @overload
    def isBefore(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.isBefore(T)"""
        return bool._wrap(super(_Range, self).isBefore(arg0))

    @staticmethod
    @overload
    def of(arg0: object, arg1: object, arg2: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.of(T,T,java.util.Comparator<T>)"""
        return Range._wrap(_Range.of(arg0, arg1, arg2))

    @staticmethod
    @overload
    def between(arg0: object, arg1: object, arg2: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.between(T,T,java.util.Comparator<T>)"""
        return Range._wrap(_Range.between(arg0, arg1, arg2))

    @overload
    def isAfterRange(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isAfterRange(org.apache.commons.lang3.Range<T>)"""
        return bool._wrap(super(_Range, self).isAfterRange(arg0))

    @staticmethod
    @overload
    def between(arg0: 'Comparable', arg1: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.between(T,T)"""
        return Range._wrap(_Range.between(arg0, arg1))

    @override
    @overload
    def getMaximum(self) -> object:
        """public T org.apache.commons.lang3.Range.getMaximum()"""
        return object._wrap(super(Range, self).getMaximum())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.Range.contains(T)"""
        return bool._wrap(super(_Range, self).contains(arg0))

    @staticmethod
    @overload
    def of(arg0: 'Comparable', arg1: 'Comparable') -> 'Range':
        """public static <T extends java.lang.Comparable<? super T>> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.of(T,T)"""
        return Range._wrap(_Range.of(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def fit(self, arg0: object) -> object:
        """public T org.apache.commons.lang3.Range.fit(T)"""
        return object._wrap(super(_Range, self).fit(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.Range.toString(java.lang.String)"""
        return str._wrap(super(_Range, self).toString(arg0))

    @override
    @overload
    def getMinimum(self) -> object:
        """public T org.apache.commons.lang3.Range.getMinimum()"""
        return object._wrap(super(Range, self).getMinimum())

    @overload
    def isOverlappedBy(self, arg0: 'Range') -> bool:
        """public boolean org.apache.commons.lang3.Range.isOverlappedBy(org.apache.commons.lang3.Range<T>)"""
        return bool._wrap(super(_Range, self).isOverlappedBy(arg0))

    @staticmethod
    @overload
    def is(arg0: object, arg1: 'Comparator') -> 'Range':
        """public static <T> org.apache.commons.lang3.Range<T> org.apache.commons.lang3.Range.is(T,java.util.Comparator<T>)"""
        return Range._wrap(_Range.is(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.lang3.SerializationException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import org.apache.commons.lang3.SerializationException as _SerializationException
_SerializationException = _SerializationException
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SerializationException():
    """org.apache.commons.lang3.SerializationException"""
 
    @staticmethod
    def _wrap(java_value: _SerializationException) -> 'SerializationException':
        return SerializationException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SerializationException):
        """
        Dynamic initializer for SerializationException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SerializationException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SerializationException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.SerializationException(java.lang.Throwable)"""
        val = _SerializationException(arg0)
        self.__wrapper = val

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.SerializationException()"""
        val = _SerializationException()
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

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
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.SerializationException(java.lang.String)"""
        val = _SerializationException(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

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
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public org.apache.commons.lang3.SerializationException(java.lang.String,java.lang.Throwable)"""
        val = _SerializationException(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.SerializationException()"""
        val = _SerializationException()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.ObjectUtils
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
import java.lang.Double as _double
import java.lang.Character as _char
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.StringBuffer as StringBuffer
import java.lang.Short as _short
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Byte as _byte
import java.lang.Comparable as _Comparable
_Comparable = _Comparable
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.time.Duration as Duration
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Comparable as Comparable
import java.lang.Appendable as Appendable
import org.apache.commons.lang3.ObjectUtils as _ObjectUtils
_ObjectUtils = _ObjectUtils
import java.lang.Float as _float
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.lang.StringBuilder as StringBuilder
try:
    from pyapache.lang3 import text
except ImportError:
    text = _import_once("pyapache.lang3.text")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ObjectUtils():
    """org.apache.commons.lang3.ObjectUtils"""
 
    @staticmethod
    def _wrap(java_value: _ObjectUtils) -> 'ObjectUtils':
        return ObjectUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ObjectUtils):
        """
        Dynamic initializer for ObjectUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ObjectUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ObjectUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def identityToString(arg0: 'StrBuilder', arg1: object):
        """public static void org.apache.commons.lang3.ObjectUtils.identityToString(org.apache.commons.lang3.text.StrBuilder,java.lang.Object)"""
        _ObjectUtils.identityToString(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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

    @staticmethod
    @overload
    def requireNonEmpty(arg0: object) -> object:
        """public static <T> T org.apache.commons.lang3.ObjectUtils.requireNonEmpty(T)"""
        return object._wrap(_ObjectUtils.requireNonEmpty(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.ObjectUtils()"""
        val = _ObjectUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def CONST_BYTE(arg0: int) -> int:
        """public static byte org.apache.commons.lang3.ObjectUtils.CONST_BYTE(int)"""
        return int._wrap(_ObjectUtils.CONST_BYTE(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def hashCodeHex(arg0: object) -> str:
        """public static java.lang.String org.apache.commons.lang3.ObjectUtils.hashCodeHex(java.lang.Object)"""
        return str._wrap(_ObjectUtils.hashCodeHex(arg0))

    @staticmethod
    @overload
    def max(*arg0: 'Comparable') -> 'Comparable':
        """public static <T extends java.lang.Comparable<? super T>> T org.apache.commons.lang3.ObjectUtils.max(T...)"""
        return Comparable._wrap(_ObjectUtils.max(arg0))

    @staticmethod
    @overload
    def notEqual(arg0: object, arg1: object) -> bool:
        """public static boolean org.apache.commons.lang3.ObjectUtils.notEqual(java.lang.Object,java.lang.Object)"""
        return bool._wrap(_ObjectUtils.notEqual(arg0, arg1))

    @staticmethod
    @overload
    def isArray(arg0: object) -> bool:
        """public static boolean org.apache.commons.lang3.ObjectUtils.isArray(java.lang.Object)"""
        return bool._wrap(_ObjectUtils.isArray(arg0))

    @staticmethod
    @overload
    def identityHashCodeHex(arg0: object) -> str:
        """public static java.lang.String org.apache.commons.lang3.ObjectUtils.identityHashCodeHex(java.lang.Object)"""
        return str._wrap(_ObjectUtils.identityHashCodeHex(arg0))

    @staticmethod
    @overload
    def CONST(arg0: str) -> str:
        """public static char org.apache.commons.lang3.ObjectUtils.CONST(char)"""
        return str._wrap(_ObjectUtils.CONST(_char.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def anyNull(*arg0: object) -> bool:
        """public static boolean org.apache.commons.lang3.ObjectUtils.anyNull(java.lang.Object...)"""
        return bool._wrap(_ObjectUtils.anyNull(arg0))

    @staticmethod
    @overload
    def getClass(arg0: object) -> 'type.Class':
        """public static <T> java.lang.Class<T> org.apache.commons.lang3.ObjectUtils.getClass(T)"""
        return type.Class._wrap(_ObjectUtils.getClass(arg0))

    @staticmethod
    @overload
    def CONST(arg0: int) -> int:
        """public static short org.apache.commons.lang3.ObjectUtils.CONST(short)"""
        return int._wrap(_ObjectUtils.CONST(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def clone(arg0: object) -> object:
        """public static <T> T org.apache.commons.lang3.ObjectUtils.clone(T)"""
        return object._wrap(_ObjectUtils.clone(arg0))

    @staticmethod
    @overload
    def wait(arg0: object, arg1: 'Duration'):
        """public static void org.apache.commons.lang3.ObjectUtils.wait(java.lang.Object,java.time.Duration) throws java.lang.InterruptedException"""
        _ObjectUtils.wait(arg0, arg1)

    @staticmethod
    @overload
    def equals(arg0: object, arg1: object) -> bool:
        """public static boolean org.apache.commons.lang3.ObjectUtils.equals(java.lang.Object,java.lang.Object)"""
        return bool._wrap(_ObjectUtils.equals(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def CONST(arg0: float) -> float:
        """public static float org.apache.commons.lang3.ObjectUtils.CONST(float)"""
        return float._wrap(_ObjectUtils.CONST(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def compare(arg0: 'Comparable', arg1: 'Comparable') -> int:
        """public static <T extends java.lang.Comparable<? super T>> int org.apache.commons.lang3.ObjectUtils.compare(T,T)"""
        return int._wrap(_ObjectUtils.compare(arg0, arg1))

    @staticmethod
    @overload
    def toString(arg0: object) -> str:
        """public static java.lang.String org.apache.commons.lang3.ObjectUtils.toString(java.lang.Object)"""
        return str._wrap(_ObjectUtils.toString(arg0))

    @staticmethod
    @overload
    def CONST(arg0: float) -> float:
        """public static double org.apache.commons.lang3.ObjectUtils.CONST(double)"""
        return float._wrap(_ObjectUtils.CONST(_double.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def CONST(arg0: int) -> int:
        """public static int org.apache.commons.lang3.ObjectUtils.CONST(int)"""
        return int._wrap(_ObjectUtils.CONST(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def min(*arg0: 'Comparable') -> 'Comparable':
        """public static <T extends java.lang.Comparable<? super T>> T org.apache.commons.lang3.ObjectUtils.min(T...)"""
        return Comparable._wrap(_ObjectUtils.min(arg0))

    @staticmethod
    @overload
    def median(*arg0: 'Comparable') -> 'Comparable':
        """public static <T extends java.lang.Comparable<? super T>> T org.apache.commons.lang3.ObjectUtils.median(T...)"""
        return Comparable._wrap(_ObjectUtils.median(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def mode(*arg0: object) -> object:
        """public static <T> T org.apache.commons.lang3.ObjectUtils.mode(T...)"""
        return object._wrap(_ObjectUtils.mode(arg0))

    @staticmethod
    @overload
    def cloneIfPossible(arg0: object) -> object:
        """public static <T> T org.apache.commons.lang3.ObjectUtils.cloneIfPossible(T)"""
        return object._wrap(_ObjectUtils.cloneIfPossible(arg0))

    @staticmethod
    @overload
    def getIfNull(arg0: object, arg1: 'Supplier') -> object:
        """public static <T> T org.apache.commons.lang3.ObjectUtils.getIfNull(T,java.util.function.Supplier<T>)"""
        return object._wrap(_ObjectUtils.getIfNull(arg0, arg1))

    @staticmethod
    @overload
    def CONST(arg0: int) -> int:
        """public static long org.apache.commons.lang3.ObjectUtils.CONST(long)"""
        return int._wrap(_ObjectUtils.CONST(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def defaultIfNull(arg0: object, arg1: object) -> object:
        """public static <T> T org.apache.commons.lang3.ObjectUtils.defaultIfNull(T,T)"""
        return object._wrap(_ObjectUtils.defaultIfNull(arg0, arg1))

    @staticmethod
    @overload
    def hashCodeMulti(*arg0: object) -> int:
        """public static int org.apache.commons.lang3.ObjectUtils.hashCodeMulti(java.lang.Object...)"""
        return int._wrap(_ObjectUtils.hashCodeMulti(arg0))

    @staticmethod
    @overload
    def CONST_SHORT(arg0: int) -> int:
        """public static short org.apache.commons.lang3.ObjectUtils.CONST_SHORT(int)"""
        return int._wrap(_ObjectUtils.CONST_SHORT(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def compare(arg0: 'Comparable', arg1: 'Comparable', arg2: bool) -> int:
        """public static <T extends java.lang.Comparable<? super T>> int org.apache.commons.lang3.ObjectUtils.compare(T,T,boolean)"""
        return int._wrap(_ObjectUtils.compare(arg0, arg1, _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def firstNonNull(*arg0: object) -> object:
        """public static <T> T org.apache.commons.lang3.ObjectUtils.firstNonNull(T...)"""
        return object._wrap(_ObjectUtils.firstNonNull(arg0))

    @staticmethod
    @overload
    def CONST(arg0: object) -> object:
        """public static <T> T org.apache.commons.lang3.ObjectUtils.CONST(T)"""
        return object._wrap(_ObjectUtils.CONST(arg0))

    @staticmethod
    @overload
    def CONST(arg0: int) -> int:
        """public static byte org.apache.commons.lang3.ObjectUtils.CONST(byte)"""
        return int._wrap(_ObjectUtils.CONST(_byte.valueOf(arg0)))

    @staticmethod
    @overload
    def allNull(*arg0: object) -> bool:
        """public static boolean org.apache.commons.lang3.ObjectUtils.allNull(java.lang.Object...)"""
        return bool._wrap(_ObjectUtils.allNull(arg0))

    @staticmethod
    @overload
    def isEmpty(arg0: object) -> bool:
        """public static boolean org.apache.commons.lang3.ObjectUtils.isEmpty(java.lang.Object)"""
        return bool._wrap(_ObjectUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def median(arg0: 'Comparator', *arg1: object) -> object:
        """public static <T> T org.apache.commons.lang3.ObjectUtils.median(java.util.Comparator<T>,T...)"""
        return object._wrap(_ObjectUtils.median(arg0, arg1))

    @staticmethod
    @overload
    def isNotEmpty(arg0: object) -> bool:
        """public static boolean org.apache.commons.lang3.ObjectUtils.isNotEmpty(java.lang.Object)"""
        return bool._wrap(_ObjectUtils.isNotEmpty(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def anyNotNull(*arg0: object) -> bool:
        """public static boolean org.apache.commons.lang3.ObjectUtils.anyNotNull(java.lang.Object...)"""
        return bool._wrap(_ObjectUtils.anyNotNull(arg0))

    @staticmethod
    @overload
    def toString(arg0: object, arg1: 'Supplier') -> str:
        """public static java.lang.String org.apache.commons.lang3.ObjectUtils.toString(java.lang.Object,java.util.function.Supplier<java.lang.String>)"""
        return str._wrap(_ObjectUtils.toString(arg0, arg1))

    @staticmethod
    @overload
    def identityToString(arg0: object) -> str:
        """public static java.lang.String org.apache.commons.lang3.ObjectUtils.identityToString(java.lang.Object)"""
        return str._wrap(_ObjectUtils.identityToString(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.ObjectUtils()"""
        val = _ObjectUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def toString(arg0: object, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.ObjectUtils.toString(java.lang.Object,java.lang.String)"""
        return str._wrap(_ObjectUtils.toString(arg0, arg1))

    @staticmethod
    @overload
    def allNotNull(*arg0: object) -> bool:
        """public static boolean org.apache.commons.lang3.ObjectUtils.allNotNull(java.lang.Object...)"""
        return bool._wrap(_ObjectUtils.allNotNull(arg0))

    @staticmethod
    @overload
    def getFirstNonNull(*arg0: 'Supplier') -> object:
        """public static <T> T org.apache.commons.lang3.ObjectUtils.getFirstNonNull(java.util.function.Supplier<T>...)"""
        return object._wrap(_ObjectUtils.getFirstNonNull(arg0))

    @staticmethod
    @overload
    def identityToString(arg0: 'StringBuffer', arg1: object):
        """public static void org.apache.commons.lang3.ObjectUtils.identityToString(java.lang.StringBuffer,java.lang.Object)"""
        _ObjectUtils.identityToString(arg0, arg1)

    @staticmethod
    @overload
    def identityToString(arg0: 'StringBuilder', arg1: object):
        """public static void org.apache.commons.lang3.ObjectUtils.identityToString(java.lang.StringBuilder,java.lang.Object)"""
        _ObjectUtils.identityToString(arg0, arg1)

    @staticmethod
    @overload
    def identityToString(arg0: 'Appendable', arg1: object):
        """public static void org.apache.commons.lang3.ObjectUtils.identityToString(java.lang.Appendable,java.lang.Object) throws java.io.IOException"""
        _ObjectUtils.identityToString(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def hashCode(arg0: object) -> int:
        """public static int org.apache.commons.lang3.ObjectUtils.hashCode(java.lang.Object)"""
        return int._wrap(_ObjectUtils.hashCode(arg0))

    @staticmethod
    @overload
    def requireNonEmpty(arg0: object, arg1: str) -> object:
        """public static <T> T org.apache.commons.lang3.ObjectUtils.requireNonEmpty(T,java.lang.String)"""
        return object._wrap(_ObjectUtils.requireNonEmpty(arg0, arg1))

    @staticmethod
    @overload
    def CONST(arg0: bool) -> bool:
        """public static boolean org.apache.commons.lang3.ObjectUtils.CONST(boolean)"""
        return bool._wrap(_ObjectUtils.CONST(_boolean.valueOf(arg0))) 
 
 
# CLASS: org.apache.commons.lang3.CharSetUtils
from builtins import str
import org.apache.commons.lang3.CharSetUtils as _CharSetUtils
_CharSetUtils = _CharSetUtils
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CharSetUtils():
    """org.apache.commons.lang3.CharSetUtils"""
 
    @staticmethod
    def _wrap(java_value: _CharSetUtils) -> 'CharSetUtils':
        return CharSetUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CharSetUtils):
        """
        Dynamic initializer for CharSetUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CharSetUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CharSetUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def count(arg0: str, *arg1: str) -> int:
        """public static int org.apache.commons.lang3.CharSetUtils.count(java.lang.String,java.lang.String...)"""
        return int._wrap(_CharSetUtils.count(arg0, arg1))

    @staticmethod
    @overload
    def containsAny(arg0: str, *arg1: str) -> bool:
        """public static boolean org.apache.commons.lang3.CharSetUtils.containsAny(java.lang.String,java.lang.String...)"""
        return bool._wrap(_CharSetUtils.containsAny(arg0, arg1))

    @staticmethod
    @overload
    def squeeze(arg0: str, *arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.CharSetUtils.squeeze(java.lang.String,java.lang.String...)"""
        return str._wrap(_CharSetUtils.squeeze(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def keep(arg0: str, *arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.CharSetUtils.keep(java.lang.String,java.lang.String...)"""
        return str._wrap(_CharSetUtils.keep(arg0, arg1))

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
    def __init__(self):
        """public org.apache.commons.lang3.CharSetUtils()"""
        val = _CharSetUtils()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def delete(arg0: str, *arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.CharSetUtils.delete(java.lang.String,java.lang.String...)"""
        return str._wrap(_CharSetUtils.delete(arg0, arg1))

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
    def __init__(self, ):
        """public org.apache.commons.lang3.CharSetUtils()"""
        val = _CharSetUtils()
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
 
 
# CLASS: org.apache.commons.lang3.NotImplementedException
from builtins import str
import org.apache.commons.lang3.NotImplementedException as _NotImplementedException
_NotImplementedException = _NotImplementedException
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NotImplementedException():
    """org.apache.commons.lang3.NotImplementedException"""
 
    @staticmethod
    def _wrap(java_value: _NotImplementedException) -> 'NotImplementedException':
        return NotImplementedException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NotImplementedException):
        """
        Dynamic initializer for NotImplementedException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NotImplementedException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NotImplementedException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public org.apache.commons.lang3.NotImplementedException(java.lang.String,java.lang.String)"""
        val = _NotImplementedException(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable', arg2: str):
        """public org.apache.commons.lang3.NotImplementedException(java.lang.String,java.lang.Throwable,java.lang.String)"""
        val = _NotImplementedException(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Throwable', arg1: str):
        """public org.apache.commons.lang3.NotImplementedException(java.lang.Throwable,java.lang.String)"""
        val = _NotImplementedException(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.NotImplementedException()"""
        val = _NotImplementedException()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.NotImplementedException(java.lang.Throwable)"""
        val = _NotImplementedException(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getCode(self) -> str:
        """public java.lang.String org.apache.commons.lang3.NotImplementedException.getCode()"""
        return str._wrap(super(NotImplementedException, self).getCode())

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public org.apache.commons.lang3.NotImplementedException(java.lang.String,java.lang.Throwable)"""
        val = _NotImplementedException(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.NotImplementedException(java.lang.String)"""
        val = _NotImplementedException(arg0)
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.NotImplementedException()"""
        val = _NotImplementedException()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.ThreadUtils$ThreadPredicate
import java.lang.Thread as Thread
import org.apache.commons.lang3.ThreadUtils as _ThreadUtils_ThreadPredicate
_ThreadPredicate = _ThreadUtils_ThreadPredicate.ThreadPredicate
from abc import abstractmethod, ABC
 
class ThreadPredicate():
    """org.apache.commons.lang3.ThreadUtils.ThreadPredicate"""
 
    @staticmethod
    def _wrap(java_value: _ThreadPredicate) -> 'ThreadPredicate':
        return ThreadPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ThreadPredicate):
        """
        Dynamic initializer for ThreadPredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ThreadPredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ThreadPredicate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def test(self, arg0: 'Thread'):
        """public abstract boolean org.apache.commons.lang3.ThreadUtils$ThreadPredicate.test(java.lang.Thread)"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.RandomStringUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import org.apache.commons.lang3.RandomStringUtils as _RandomStringUtils
_RandomStringUtils = _RandomStringUtils
from builtins import bool
import java.lang.Long as _long
import java.util.Random as Random
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RandomStringUtils():
    """org.apache.commons.lang3.RandomStringUtils"""
 
    @staticmethod
    def _wrap(java_value: _RandomStringUtils) -> 'RandomStringUtils':
        return RandomStringUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RandomStringUtils):
        """
        Dynamic initializer for RandomStringUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RandomStringUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RandomStringUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def random(arg0: int, arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.random(int,java.lang.String)"""
        return str._wrap(_RandomStringUtils.random(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def randomAscii(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.randomAscii(int)"""
        return str._wrap(_RandomStringUtils.randomAscii(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.RandomStringUtils()"""
        val = _RandomStringUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def random(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.random(int)"""
        return str._wrap(_RandomStringUtils.random(_int.valueOf(arg0)))

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

    @staticmethod
    @overload
    def random(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: bool, *arg5: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.random(int,int,int,boolean,boolean,char...)"""
        return str._wrap(_RandomStringUtils.random(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _boolean.valueOf(arg4), arg5))

    @staticmethod
    @overload
    def randomAlphanumeric(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.randomAlphanumeric(int)"""
        return str._wrap(_RandomStringUtils.randomAlphanumeric(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def random(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: bool) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.random(int,int,int,boolean,boolean)"""
        return str._wrap(_RandomStringUtils.random(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _boolean.valueOf(arg4)))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.RandomStringUtils()"""
        val = _RandomStringUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def randomNumeric(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.randomNumeric(int,int)"""
        return str._wrap(_RandomStringUtils.randomNumeric(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def random(arg0: int, *arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.random(int,char...)"""
        return str._wrap(_RandomStringUtils.random(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def random(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: bool, arg5: 'char', arg6: 'Random') -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.random(int,int,int,boolean,boolean,char[],java.util.Random)"""
        return str._wrap(_RandomStringUtils.random(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _boolean.valueOf(arg4), arg5, arg6))

    @staticmethod
    @overload
    def randomAlphabetic(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.randomAlphabetic(int)"""
        return str._wrap(_RandomStringUtils.randomAlphabetic(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def random(arg0: int, arg1: bool, arg2: bool) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.random(int,boolean,boolean)"""
        return str._wrap(_RandomStringUtils.random(_int.valueOf(arg0), _boolean.valueOf(arg1), _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def randomNumeric(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.randomNumeric(int)"""
        return str._wrap(_RandomStringUtils.randomNumeric(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def randomPrint(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.randomPrint(int)"""
        return str._wrap(_RandomStringUtils.randomPrint(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def randomAlphanumeric(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.randomAlphanumeric(int,int)"""
        return str._wrap(_RandomStringUtils.randomAlphanumeric(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def randomPrint(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.randomPrint(int,int)"""
        return str._wrap(_RandomStringUtils.randomPrint(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def randomAlphabetic(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.randomAlphabetic(int,int)"""
        return str._wrap(_RandomStringUtils.randomAlphabetic(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def randomAscii(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.randomAscii(int,int)"""
        return str._wrap(_RandomStringUtils.randomAscii(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def randomGraph(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.randomGraph(int)"""
        return str._wrap(_RandomStringUtils.randomGraph(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def randomGraph(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.RandomStringUtils.randomGraph(int,int)"""
        return str._wrap(_RandomStringUtils.randomGraph(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.Functions$FailableRunnable
import org.apache.commons.lang3.Functions as _Functions_FailableRunnable
_FailableRunnable = _Functions_FailableRunnable.FailableRunnable
from abc import abstractmethod, ABC
 
class FailableRunnable():
    """org.apache.commons.lang3.Functions.FailableRunnable"""
 
    @staticmethod
    def _wrap(java_value: _FailableRunnable) -> 'FailableRunnable':
        return FailableRunnable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FailableRunnable):
        """
        Dynamic initializer for FailableRunnable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FailableRunnable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FailableRunnable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def run(self, ):
        """public abstract void org.apache.commons.lang3.Functions$FailableRunnable.run() throws T"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.ThreadUtils$NamePredicate
import java.lang.Thread as Thread
from builtins import str
import org.apache.commons.lang3.ThreadUtils as _ThreadUtils_NamePredicate
_NamePredicate = _ThreadUtils_NamePredicate.NamePredicate
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import java.lang.ThreadGroup as ThreadGroup
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NamePredicate():
    """org.apache.commons.lang3.ThreadUtils.NamePredicate"""
 
    @staticmethod
    def _wrap(java_value: _NamePredicate) -> 'NamePredicate':
        return NamePredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NamePredicate):
        """
        Dynamic initializer for NamePredicate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NamePredicate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NamePredicate__wrapper":
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
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.ThreadUtils$NamePredicate(java.lang.String)"""
        val = _NamePredicate(arg0)
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
    def test(self, arg0: 'Thread') -> bool:
        """public boolean org.apache.commons.lang3.ThreadUtils$NamePredicate.test(java.lang.Thread)"""
        return bool._wrap(super(_NamePredicate, self).test(arg0))

    @overload
    def test(self, arg0: 'ThreadGroup') -> bool:
        """public boolean org.apache.commons.lang3.ThreadUtils$NamePredicate.test(java.lang.ThreadGroup)"""
        return bool._wrap(super(_NamePredicate, self).test(arg0))

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
 
 
# CLASS: org.apache.commons.lang3.RandomUtils
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import org.apache.commons.lang3.RandomUtils as _RandomUtils
_RandomUtils = _RandomUtils
from typing import List
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RandomUtils():
    """org.apache.commons.lang3.RandomUtils"""
 
    @staticmethod
    def _wrap(java_value: _RandomUtils) -> 'RandomUtils':
        return RandomUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RandomUtils):
        """
        Dynamic initializer for RandomUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RandomUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RandomUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nextLong(arg0: int, arg1: int) -> int:
        """public static long org.apache.commons.lang3.RandomUtils.nextLong(long,long)"""
        return int._wrap(_RandomUtils.nextLong(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nextLong() -> int:
        """public static long org.apache.commons.lang3.RandomUtils.nextLong()"""
        return int._wrap(_RandomUtils.nextLong())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.RandomUtils()"""
        val = _RandomUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def nextBoolean() -> bool:
        """public static boolean org.apache.commons.lang3.RandomUtils.nextBoolean()"""
        return bool._wrap(_RandomUtils.nextBoolean())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nextDouble(arg0: float, arg1: float) -> float:
        """public static double org.apache.commons.lang3.RandomUtils.nextDouble(double,double)"""
        return float._wrap(_RandomUtils.nextDouble(_double.valueOf(arg0), _double.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nextFloat(arg0: float, arg1: float) -> float:
        """public static float org.apache.commons.lang3.RandomUtils.nextFloat(float,float)"""
        return float._wrap(_RandomUtils.nextFloat(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.RandomUtils()"""
        val = _RandomUtils()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nextDouble() -> float:
        """public static double org.apache.commons.lang3.RandomUtils.nextDouble()"""
        return float._wrap(_RandomUtils.nextDouble())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nextFloat() -> float:
        """public static float org.apache.commons.lang3.RandomUtils.nextFloat()"""
        return float._wrap(_RandomUtils.nextFloat())

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

    @staticmethod
    @overload
    def nextBytes(arg0: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.RandomUtils.nextBytes(int)"""
        return List[int]._wrap(_RandomUtils.nextBytes(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nextInt() -> int:
        """public static int org.apache.commons.lang3.RandomUtils.nextInt()"""
        return int._wrap(_RandomUtils.nextInt())

    @staticmethod
    @overload
    def nextInt(arg0: int, arg1: int) -> int:
        """public static int org.apache.commons.lang3.RandomUtils.nextInt(int,int)"""
        return int._wrap(_RandomUtils.nextInt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.CharSequenceUtils
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.CharSequenceUtils as _CharSequenceUtils
_CharSequenceUtils = _CharSequenceUtils
import java.lang.CharSequence as _CharSequence
_CharSequence = _CharSequence
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CharSequenceUtils():
    """org.apache.commons.lang3.CharSequenceUtils"""
 
    @staticmethod
    def _wrap(java_value: _CharSequenceUtils) -> 'CharSequenceUtils':
        return CharSequenceUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CharSequenceUtils):
        """
        Dynamic initializer for CharSequenceUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CharSequenceUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CharSequenceUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.CharSequenceUtils()"""
        val = _CharSequenceUtils()
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
    def __init__(self):
        """public org.apache.commons.lang3.CharSequenceUtils()"""
        val = _CharSequenceUtils()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def subSequence(arg0: 'CharSequence', arg1: int) -> 'CharSequence':
        """public static java.lang.CharSequence org.apache.commons.lang3.CharSequenceUtils.subSequence(java.lang.CharSequence,int)"""
        return CharSequence._wrap(_CharSequenceUtils.subSequence(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def toCharArray(arg0: 'CharSequence') -> List[str]:
        """public static char[] org.apache.commons.lang3.CharSequenceUtils.toCharArray(java.lang.CharSequence)"""
        return List[str]._wrap(_CharSequenceUtils.toCharArray(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.Streams$ArrayCollector
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.util.function.Function as _Function
_Function = _Function
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.function.BiConsumer as _BiConsumer
_BiConsumer = _BiConsumer
import java.lang.String as _String
_String = _String
import java.util.Set as _Set
_Set = _Set
import java.util.Set as Set
import java.util.function.BiConsumer as BiConsumer
import java.lang.Integer as _int
import java.util.function.BinaryOperator as BinaryOperator
import org.apache.commons.lang3.Streams as _Streams_ArrayCollector
_ArrayCollector = _Streams_ArrayCollector.ArrayCollector
import java.util.function.BinaryOperator as _BinaryOperator
_BinaryOperator = _BinaryOperator
import java.util.function.Function as Function
from builtins import bool
import java.lang.Long as _long
import java.util.function.Supplier as _Supplier
_Supplier = _Supplier
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ArrayCollector():
    """org.apache.commons.lang3.Streams.ArrayCollector"""
 
    @staticmethod
    def _wrap(java_value: _ArrayCollector) -> 'ArrayCollector':
        return ArrayCollector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ArrayCollector):
        """
        Dynamic initializer for ArrayCollector.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ArrayCollector__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ArrayCollector__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def finisher(self) -> 'Function':
        """public java.util.function.Function<java.util.List<O>, O[]> org.apache.commons.lang3.Streams$ArrayCollector.finisher()"""
        return 'Function'._wrap(super(ArrayCollector, self).finisher())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def combiner(self) -> 'BinaryOperator':
        """public java.util.function.BinaryOperator<java.util.List<O>> org.apache.commons.lang3.Streams$ArrayCollector.combiner()"""
        return 'BinaryOperator'._wrap(super(ArrayCollector, self).combiner())

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
    def __init__(self, arg0: 'Class'):
        """public org.apache.commons.lang3.Streams$ArrayCollector(java.lang.Class<O>)"""
        val = _ArrayCollector(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def accumulator(self) -> 'BiConsumer':
        """public java.util.function.BiConsumer<java.util.List<O>, O> org.apache.commons.lang3.Streams$ArrayCollector.accumulator()"""
        return 'BiConsumer'._wrap(super(ArrayCollector, self).accumulator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def characteristics(self) -> 'Set':
        """public java.util.Set<java.util.stream.Collector$Characteristics> org.apache.commons.lang3.Streams$ArrayCollector.characteristics()"""
        return 'Set'._wrap(super(ArrayCollector, self).characteristics())

    @override
    @overload
    def supplier(self) -> 'Supplier':
        """public java.util.function.Supplier<java.util.List<O>> org.apache.commons.lang3.Streams$ArrayCollector.supplier()"""
        return 'Supplier'._wrap(super(ArrayCollector, self).supplier())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.Conversion
from builtins import str
import java.util.UUID as UUID
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Short as _short
from typing import List
import java.lang.String as _string
import java.lang.Integer as _int
import java.lang.Byte as _byte
import org.apache.commons.lang3.Conversion as _Conversion
_Conversion = _Conversion
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.UUID as _UUID
_UUID = _UUID
import java.lang.Class as _Class
_Class = _Class
 
class Conversion():
    """org.apache.commons.lang3.Conversion"""
 
    @staticmethod
    def _wrap(java_value: _Conversion) -> 'Conversion':
        return Conversion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Conversion):
        """
        Dynamic initializer for Conversion.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Conversion__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Conversion__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def shortArrayToInt(arg0: 'short', arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.apache.commons.lang3.Conversion.shortArrayToInt(short[],int,int,int,int)"""
        return int._wrap(_Conversion.shortArrayToInt(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def binaryToInt(arg0: 'boolean', arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.apache.commons.lang3.Conversion.binaryToInt(boolean[],int,int,int,int)"""
        return int._wrap(_Conversion.binaryToInt(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def hexToShort(arg0: str, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static short org.apache.commons.lang3.Conversion.hexToShort(java.lang.String,int,short,int,int)"""
        return int._wrap(_Conversion.hexToShort(arg0, _int.valueOf(arg1), _short.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def intToBinary(arg0: int, arg1: int, arg2: 'boolean', arg3: int, arg4: int) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.Conversion.intToBinary(int,int,boolean[],int,int)"""
        return List[bool]._wrap(_Conversion.intToBinary(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def byteToHex(arg0: int, arg1: int, arg2: str, arg3: int, arg4: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.Conversion.byteToHex(byte,int,java.lang.String,int,int)"""
        return str._wrap(_Conversion.byteToHex(_byte.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def uuidToByteArray(arg0: 'UUID', arg1: bytes, arg2: int, arg3: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.Conversion.uuidToByteArray(java.util.UUID,byte[],int,int)"""
        return List[int]._wrap(_Conversion.uuidToByteArray(arg0, bytes, _int.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def shortArrayToLong(arg0: 'short', arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static long org.apache.commons.lang3.Conversion.shortArrayToLong(short[],int,long,int,int)"""
        return int._wrap(_Conversion.shortArrayToLong(arg0, _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def binaryToHexDigit(arg0: 'boolean') -> str:
        """public static char org.apache.commons.lang3.Conversion.binaryToHexDigit(boolean[])"""
        return str._wrap(_Conversion.binaryToHexDigit(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def hexDigitMsb0ToBinary(arg0: str) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.Conversion.hexDigitMsb0ToBinary(char)"""
        return List[bool]._wrap(_Conversion.hexDigitMsb0ToBinary(_char.valueOf(arg0)))

    @staticmethod
    @overload
    def hexDigitMsb0ToInt(arg0: str) -> int:
        """public static int org.apache.commons.lang3.Conversion.hexDigitMsb0ToInt(char)"""
        return int._wrap(_Conversion.hexDigitMsb0ToInt(_char.valueOf(arg0)))

    @staticmethod
    @overload
    def intArrayToLong(arg0: 'int', arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static long org.apache.commons.lang3.Conversion.intArrayToLong(int[],int,long,int,int)"""
        return int._wrap(_Conversion.intArrayToLong(arg0, _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def longToShortArray(arg0: int, arg1: int, arg2: 'short', arg3: int, arg4: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.Conversion.longToShortArray(long,int,short[],int,int)"""
        return List[int]._wrap(_Conversion.longToShortArray(_long.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def longToHex(arg0: int, arg1: int, arg2: str, arg3: int, arg4: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.Conversion.longToHex(long,int,java.lang.String,int,int)"""
        return str._wrap(_Conversion.longToHex(_long.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def longToIntArray(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int) -> List[int]:
        """public static int[] org.apache.commons.lang3.Conversion.longToIntArray(long,int,int[],int,int)"""
        return List[int]._wrap(_Conversion.longToIntArray(_long.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def byteToBinary(arg0: int, arg1: int, arg2: 'boolean', arg3: int, arg4: int) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.Conversion.byteToBinary(byte,int,boolean[],int,int)"""
        return List[bool]._wrap(_Conversion.byteToBinary(_byte.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.Conversion()"""
        val = _Conversion()
        self.__wrapper = val

    @staticmethod
    @overload
    def byteArrayToShort(arg0: bytes, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static short org.apache.commons.lang3.Conversion.byteArrayToShort(byte[],int,short,int,int)"""
        return int._wrap(_Conversion.byteArrayToShort(bytes, _int.valueOf(arg1), _short.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def binaryToHexDigitMsb0_4bits(arg0: 'boolean', arg1: int) -> str:
        """public static char org.apache.commons.lang3.Conversion.binaryToHexDigitMsb0_4bits(boolean[],int)"""
        return str._wrap(_Conversion.binaryToHexDigitMsb0_4bits(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def hexToInt(arg0: str, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.apache.commons.lang3.Conversion.hexToInt(java.lang.String,int,int,int,int)"""
        return int._wrap(_Conversion.hexToInt(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.Conversion()"""
        val = _Conversion()
        self.__wrapper = val

    @staticmethod
    @overload
    def hexDigitToBinary(arg0: str) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.Conversion.hexDigitToBinary(char)"""
        return List[bool]._wrap(_Conversion.hexDigitToBinary(_char.valueOf(arg0)))

    @staticmethod
    @overload
    def longToByteArray(arg0: int, arg1: int, arg2: bytes, arg3: int, arg4: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.Conversion.longToByteArray(long,int,byte[],int,int)"""
        return List[int]._wrap(_Conversion.longToByteArray(_long.valueOf(arg0), _int.valueOf(arg1), bytes, _int.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def shortToHex(arg0: int, arg1: int, arg2: str, arg3: int, arg4: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.Conversion.shortToHex(short,int,java.lang.String,int,int)"""
        return str._wrap(_Conversion.shortToHex(_short.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def byteArrayToUuid(arg0: bytes, arg1: int) -> 'UUID':
        """public static java.util.UUID org.apache.commons.lang3.Conversion.byteArrayToUuid(byte[],int)"""
        return UUID._wrap(_Conversion.byteArrayToUuid(bytes, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def shortToByteArray(arg0: int, arg1: int, arg2: bytes, arg3: int, arg4: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.Conversion.shortToByteArray(short,int,byte[],int,int)"""
        return List[int]._wrap(_Conversion.shortToByteArray(_short.valueOf(arg0), _int.valueOf(arg1), bytes, _int.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def binaryToLong(arg0: 'boolean', arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static long org.apache.commons.lang3.Conversion.binaryToLong(boolean[],int,long,int,int)"""
        return int._wrap(_Conversion.binaryToLong(arg0, _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def binaryBeMsb0ToHexDigit(arg0: 'boolean') -> str:
        """public static char org.apache.commons.lang3.Conversion.binaryBeMsb0ToHexDigit(boolean[])"""
        return str._wrap(_Conversion.binaryBeMsb0ToHexDigit(arg0))

    @staticmethod
    @overload
    def intToShortArray(arg0: int, arg1: int, arg2: 'short', arg3: int, arg4: int) -> List[int]:
        """public static short[] org.apache.commons.lang3.Conversion.intToShortArray(int,int,short[],int,int)"""
        return List[int]._wrap(_Conversion.intToShortArray(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def byteArrayToInt(arg0: bytes, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.apache.commons.lang3.Conversion.byteArrayToInt(byte[],int,int,int,int)"""
        return int._wrap(_Conversion.byteArrayToInt(bytes, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def binaryToByte(arg0: 'boolean', arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static byte org.apache.commons.lang3.Conversion.binaryToByte(boolean[],int,byte,int,int)"""
        return int._wrap(_Conversion.binaryToByte(arg0, _int.valueOf(arg1), _byte.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def binaryBeMsb0ToHexDigit(arg0: 'boolean', arg1: int) -> str:
        """public static char org.apache.commons.lang3.Conversion.binaryBeMsb0ToHexDigit(boolean[],int)"""
        return str._wrap(_Conversion.binaryBeMsb0ToHexDigit(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def intToHexDigitMsb0(arg0: int) -> str:
        """public static char org.apache.commons.lang3.Conversion.intToHexDigitMsb0(int)"""
        return str._wrap(_Conversion.intToHexDigitMsb0(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def byteArrayToLong(arg0: bytes, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static long org.apache.commons.lang3.Conversion.byteArrayToLong(byte[],int,long,int,int)"""
        return int._wrap(_Conversion.byteArrayToLong(bytes, _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def shortToBinary(arg0: int, arg1: int, arg2: 'boolean', arg3: int, arg4: int) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.Conversion.shortToBinary(short,int,boolean[],int,int)"""
        return List[bool]._wrap(_Conversion.shortToBinary(_short.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def intToByteArray(arg0: int, arg1: int, arg2: bytes, arg3: int, arg4: int) -> List[int]:
        """public static byte[] org.apache.commons.lang3.Conversion.intToByteArray(int,int,byte[],int,int)"""
        return List[int]._wrap(_Conversion.intToByteArray(_int.valueOf(arg0), _int.valueOf(arg1), bytes, _int.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def intToHex(arg0: int, arg1: int, arg2: str, arg3: int, arg4: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.Conversion.intToHex(int,int,java.lang.String,int,int)"""
        return str._wrap(_Conversion.intToHex(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def binaryToHexDigitMsb0_4bits(arg0: 'boolean') -> str:
        """public static char org.apache.commons.lang3.Conversion.binaryToHexDigitMsb0_4bits(boolean[])"""
        return str._wrap(_Conversion.binaryToHexDigitMsb0_4bits(arg0))

    @staticmethod
    @overload
    def hexToLong(arg0: str, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static long org.apache.commons.lang3.Conversion.hexToLong(java.lang.String,int,long,int,int)"""
        return int._wrap(_Conversion.hexToLong(arg0, _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def hexDigitToInt(arg0: str) -> int:
        """public static int org.apache.commons.lang3.Conversion.hexDigitToInt(char)"""
        return int._wrap(_Conversion.hexDigitToInt(_char.valueOf(arg0)))

    @staticmethod
    @overload
    def intToHexDigit(arg0: int) -> str:
        """public static char org.apache.commons.lang3.Conversion.intToHexDigit(int)"""
        return str._wrap(_Conversion.intToHexDigit(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def longToBinary(arg0: int, arg1: int, arg2: 'boolean', arg3: int, arg4: int) -> List[bool]:
        """public static boolean[] org.apache.commons.lang3.Conversion.longToBinary(long,int,boolean[],int,int)"""
        return List[bool]._wrap(_Conversion.longToBinary(_long.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def hexToByte(arg0: str, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static byte org.apache.commons.lang3.Conversion.hexToByte(java.lang.String,int,byte,int,int)"""
        return int._wrap(_Conversion.hexToByte(arg0, _int.valueOf(arg1), _byte.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def binaryToHexDigit(arg0: 'boolean', arg1: int) -> str:
        """public static char org.apache.commons.lang3.Conversion.binaryToHexDigit(boolean[],int)"""
        return str._wrap(_Conversion.binaryToHexDigit(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def binaryToShort(arg0: 'boolean', arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static short org.apache.commons.lang3.Conversion.binaryToShort(boolean[],int,short,int,int)"""
        return int._wrap(_Conversion.binaryToShort(arg0, _int.valueOf(arg1), _short.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))) 
 
 
# CLASS: org.apache.commons.lang3.SerializationUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.Serializable as _Serializable
_Serializable = _Serializable
from builtins import object
import java.lang.String as _String
_String = _String
from typing import List
import java.io.OutputStream as OutputStream
import java.lang.Integer as _int
import java.io.InputStream as InputStream
import org.apache.commons.lang3.SerializationUtils as _SerializationUtils
_SerializationUtils = _SerializationUtils
import java.io.Serializable as Serializable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SerializationUtils():
    """org.apache.commons.lang3.SerializationUtils"""
 
    @staticmethod
    def _wrap(java_value: _SerializationUtils) -> 'SerializationUtils':
        return SerializationUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SerializationUtils):
        """
        Dynamic initializer for SerializationUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SerializationUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SerializationUtils__wrapper":
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

    @staticmethod
    @overload
    def deserialize(arg0: bytes) -> object:
        """public static <T> T org.apache.commons.lang3.SerializationUtils.deserialize(byte[])"""
        return object._wrap(_SerializationUtils.deserialize(bytes))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.SerializationUtils()"""
        val = _SerializationUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def deserialize(arg0: 'InputStream') -> object:
        """public static <T> T org.apache.commons.lang3.SerializationUtils.deserialize(java.io.InputStream)"""
        return object._wrap(_SerializationUtils.deserialize(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def serialize(arg0: 'Serializable') -> List[int]:
        """public static byte[] org.apache.commons.lang3.SerializationUtils.serialize(java.io.Serializable)"""
        return List[int]._wrap(_SerializationUtils.serialize(arg0))

    @staticmethod
    @overload
    def roundtrip(arg0: 'Serializable') -> 'Serializable':
        """public static <T extends java.io.Serializable> T org.apache.commons.lang3.SerializationUtils.roundtrip(T)"""
        return Serializable._wrap(_SerializationUtils.roundtrip(arg0))

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
    def __init__(self):
        """public org.apache.commons.lang3.SerializationUtils()"""
        val = _SerializationUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def clone(arg0: 'Serializable') -> 'Serializable':
        """public static <T extends java.io.Serializable> T org.apache.commons.lang3.SerializationUtils.clone(T)"""
        return Serializable._wrap(_SerializationUtils.clone(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def serialize(arg0: 'Serializable', arg1: 'OutputStream'):
        """public static void org.apache.commons.lang3.SerializationUtils.serialize(java.io.Serializable,java.io.OutputStream)"""
        _SerializationUtils.serialize(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.EnumUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.util.Map as _Map
_Map = _Map
import java.lang.Iterable as Iterable
import org.apache.commons.lang3.EnumUtils as _EnumUtils
_EnumUtils = _EnumUtils
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.EnumSet as EnumSet
import java.util.EnumSet as _EnumSet
_EnumSet = _EnumSet
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class EnumUtils():
    """org.apache.commons.lang3.EnumUtils"""
 
    @staticmethod
    def _wrap(java_value: _EnumUtils) -> 'EnumUtils':
        return EnumUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EnumUtils):
        """
        Dynamic initializer for EnumUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EnumUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EnumUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def isValidEnumIgnoreCase(arg0: 'Class', arg1: str) -> bool:
        """public static <E extends java.lang.Enum<E>> boolean org.apache.commons.lang3.EnumUtils.isValidEnumIgnoreCase(java.lang.Class<E>,java.lang.String)"""
        return bool._wrap(_EnumUtils.isValidEnumIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def getEnumList(arg0: 'Class') -> 'List':
        """public static <E extends java.lang.Enum<E>> java.util.List<E> org.apache.commons.lang3.EnumUtils.getEnumList(java.lang.Class<E>)"""
        return List._wrap(_EnumUtils.getEnumList(arg0))

    @staticmethod
    @overload
    def generateBitVectors(arg0: 'Class', *arg1: 'Enum') -> List[int]:
        """public static <E extends java.lang.Enum<E>> long[] org.apache.commons.lang3.EnumUtils.generateBitVectors(java.lang.Class<E>,E...)"""
        return List[int]._wrap(_EnumUtils.generateBitVectors(arg0, arg1))

    @staticmethod
    @overload
    def getEnumSystemProperty(arg0: 'Class', arg1: str, arg2: 'Enum') -> 'Enum':
        """public static <E extends java.lang.Enum<E>> E org.apache.commons.lang3.EnumUtils.getEnumSystemProperty(java.lang.Class<E>,java.lang.String,E)"""
        return Enum._wrap(_EnumUtils.getEnumSystemProperty(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getEnumIgnoreCase(arg0: 'Class', arg1: str, arg2: 'Enum') -> 'Enum':
        """public static <E extends java.lang.Enum<E>> E org.apache.commons.lang3.EnumUtils.getEnumIgnoreCase(java.lang.Class<E>,java.lang.String,E)"""
        return Enum._wrap(_EnumUtils.getEnumIgnoreCase(arg0, arg1, arg2))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.EnumUtils()"""
        val = _EnumUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def getEnumIgnoreCase(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <E extends java.lang.Enum<E>> E org.apache.commons.lang3.EnumUtils.getEnumIgnoreCase(java.lang.Class<E>,java.lang.String)"""
        return Enum._wrap(_EnumUtils.getEnumIgnoreCase(arg0, arg1))

    @staticmethod
    @overload
    def getFirstEnumIgnoreCase(arg0: 'Class', arg1: str, arg2: 'Function', arg3: 'Enum') -> 'Enum':
        """public static <E extends java.lang.Enum<E>> E org.apache.commons.lang3.EnumUtils.getFirstEnumIgnoreCase(java.lang.Class<E>,java.lang.String,java.util.function.Function<E, java.lang.String>,E)"""
        return Enum._wrap(_EnumUtils.getFirstEnumIgnoreCase(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def generateBitVector(arg0: 'Class', arg1: 'Iterable') -> int:
        """public static <E extends java.lang.Enum<E>> long org.apache.commons.lang3.EnumUtils.generateBitVector(java.lang.Class<E>,java.lang.Iterable<? extends E>)"""
        return int._wrap(_EnumUtils.generateBitVector(arg0, arg1))

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

    @staticmethod
    @overload
    def getEnumMap(arg0: 'Class', arg1: 'Function') -> 'Map':
        """public static <E extends java.lang.Enum<E>,K> java.util.Map<K, E> org.apache.commons.lang3.EnumUtils.getEnumMap(java.lang.Class<E>,java.util.function.Function<E, K>)"""
        return Map._wrap(_EnumUtils.getEnumMap(arg0, arg1))

    @staticmethod
    @overload
    def getEnum(arg0: 'Class', arg1: str, arg2: 'Enum') -> 'Enum':
        """public static <E extends java.lang.Enum<E>> E org.apache.commons.lang3.EnumUtils.getEnum(java.lang.Class<E>,java.lang.String,E)"""
        return Enum._wrap(_EnumUtils.getEnum(arg0, arg1, arg2))

    @staticmethod
    @overload
    def getEnumMap(arg0: 'Class') -> 'Map':
        """public static <E extends java.lang.Enum<E>> java.util.Map<java.lang.String, E> org.apache.commons.lang3.EnumUtils.getEnumMap(java.lang.Class<E>)"""
        return Map._wrap(_EnumUtils.getEnumMap(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def processBitVector(arg0: 'Class', arg1: int) -> 'EnumSet':
        """public static <E extends java.lang.Enum<E>> java.util.EnumSet<E> org.apache.commons.lang3.EnumUtils.processBitVector(java.lang.Class<E>,long)"""
        return EnumSet._wrap(_EnumUtils.processBitVector(arg0, _long.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getEnum(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <E extends java.lang.Enum<E>> E org.apache.commons.lang3.EnumUtils.getEnum(java.lang.Class<E>,java.lang.String)"""
        return Enum._wrap(_EnumUtils.getEnum(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.EnumUtils()"""
        val = _EnumUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def generateBitVectors(arg0: 'Class', arg1: 'Iterable') -> List[int]:
        """public static <E extends java.lang.Enum<E>> long[] org.apache.commons.lang3.EnumUtils.generateBitVectors(java.lang.Class<E>,java.lang.Iterable<? extends E>)"""
        return List[int]._wrap(_EnumUtils.generateBitVectors(arg0, arg1))

    @staticmethod
    @overload
    def generateBitVector(arg0: 'Class', *arg1: 'Enum') -> int:
        """public static <E extends java.lang.Enum<E>> long org.apache.commons.lang3.EnumUtils.generateBitVector(java.lang.Class<E>,E...)"""
        return int._wrap(_EnumUtils.generateBitVector(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def processBitVectors(arg0: 'Class', *arg1: int) -> 'EnumSet':
        """public static <E extends java.lang.Enum<E>> java.util.EnumSet<E> org.apache.commons.lang3.EnumUtils.processBitVectors(java.lang.Class<E>,long...)"""
        return EnumSet._wrap(_EnumUtils.processBitVectors(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def isValidEnum(arg0: 'Class', arg1: str) -> bool:
        """public static <E extends java.lang.Enum<E>> boolean org.apache.commons.lang3.EnumUtils.isValidEnum(java.lang.Class<E>,java.lang.String)"""
        return bool._wrap(_EnumUtils.isValidEnum(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.BitField
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Short as _short
import org.apache.commons.lang3.BitField as _BitField
_BitField = _BitField
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.lang.Byte as _byte
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BitField():
    """org.apache.commons.lang3.BitField"""
 
    @staticmethod
    def _wrap(java_value: _BitField) -> 'BitField':
        return BitField(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BitField):
        """
        Dynamic initializer for BitField.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BitField__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BitField__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setShortValue(self, arg0: int, arg1: int) -> int:
        """public short org.apache.commons.lang3.BitField.setShortValue(short,short)"""
        return int._wrap(super(_BitField, self).setShortValue(_short.valueOf(arg0), _short.valueOf(arg1)))

    @overload
    def isSet(self, arg0: int) -> bool:
        """public boolean org.apache.commons.lang3.BitField.isSet(int)"""
        return bool._wrap(super(_BitField, self).isSet(_int.valueOf(arg0)))

    @overload
    def getShortValue(self, arg0: int) -> int:
        """public short org.apache.commons.lang3.BitField.getShortValue(short)"""
        return int._wrap(super(_BitField, self).getShortValue(_short.valueOf(arg0)))

    @overload
    def setByteBoolean(self, arg0: int, arg1: bool) -> int:
        """public byte org.apache.commons.lang3.BitField.setByteBoolean(byte,boolean)"""
        return int._wrap(super(_BitField, self).setByteBoolean(_byte.valueOf(arg0), _boolean.valueOf(arg1)))

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.lang3.BitField(int)"""
        val = _BitField(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getValue(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.BitField.getValue(int)"""
        return int._wrap(super(_BitField, self).getValue(_int.valueOf(arg0)))

    @overload
    def setBoolean(self, arg0: int, arg1: bool) -> int:
        """public int org.apache.commons.lang3.BitField.setBoolean(int,boolean)"""
        return int._wrap(super(_BitField, self).setBoolean(_int.valueOf(arg0), _boolean.valueOf(arg1)))

    @overload
    def isAllSet(self, arg0: int) -> bool:
        """public boolean org.apache.commons.lang3.BitField.isAllSet(int)"""
        return bool._wrap(super(_BitField, self).isAllSet(_int.valueOf(arg0)))

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
    def setShortBoolean(self, arg0: int, arg1: bool) -> int:
        """public short org.apache.commons.lang3.BitField.setShortBoolean(short,boolean)"""
        return int._wrap(super(_BitField, self).setShortBoolean(_short.valueOf(arg0), _boolean.valueOf(arg1)))

    @overload
    def setByte(self, arg0: int) -> int:
        """public byte org.apache.commons.lang3.BitField.setByte(byte)"""
        return int._wrap(super(_BitField, self).setByte(_byte.valueOf(arg0)))

    @overload
    def clearByte(self, arg0: int) -> int:
        """public byte org.apache.commons.lang3.BitField.clearByte(byte)"""
        return int._wrap(super(_BitField, self).clearByte(_byte.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def clear(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.BitField.clear(int)"""
        return int._wrap(super(_BitField, self).clear(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setValue(self, arg0: int, arg1: int) -> int:
        """public int org.apache.commons.lang3.BitField.setValue(int,int)"""
        return int._wrap(super(_BitField, self).setValue(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setShort(self, arg0: int) -> int:
        """public short org.apache.commons.lang3.BitField.setShort(short)"""
        return int._wrap(super(_BitField, self).setShort(_short.valueOf(arg0)))

    @overload
    def clearShort(self, arg0: int) -> int:
        """public short org.apache.commons.lang3.BitField.clearShort(short)"""
        return int._wrap(super(_BitField, self).clearShort(_short.valueOf(arg0)))

    @overload
    def getShortRawValue(self, arg0: int) -> int:
        """public short org.apache.commons.lang3.BitField.getShortRawValue(short)"""
        return int._wrap(super(_BitField, self).getShortRawValue(_short.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def set(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.BitField.set(int)"""
        return int._wrap(super(_BitField, self).set(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getRawValue(self, arg0: int) -> int:
        """public int org.apache.commons.lang3.BitField.getRawValue(int)"""
        return int._wrap(super(_BitField, self).getRawValue(_int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())