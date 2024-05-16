from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.base.MoreObjects as __MoreObjects_ToStringHelper
__ToStringHelper = __MoreObjects_ToStringHelper.ToStringHelper
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.base.MoreObjects as __MoreObjects
__MoreObjects = __MoreObjects
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MoreObjects():
    """com.google.common.base.MoreObjects"""
 
    @staticmethod
    def __wrap(java_value: __MoreObjects) -> 'MoreObjects':
        return MoreObjects(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MoreObjects):
        """
        Dynamic initializer for MoreObjects.
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
 
    @staticmethod
    @overload
    def firstNonNull(first: object, second: object) -> object:
        """public static <T> T com.google.common.base.MoreObjects.firstNonNull(T,T)"""
        return object.__wrap(__MoreObjects.firstNonNull(first, second))

    @staticmethod
    @overload
    def toStringHelper(self: object) -> 'ToStringHelper':
        """public static com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects.toStringHelper(java.lang.Object)"""
        return ToStringHelper.__wrap(__MoreObjects.toStringHelper(self))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def toStringHelper(clazz: 'Class') -> 'ToStringHelper':
        """public static com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects.toStringHelper(java.lang.Class<?>)"""
        return ToStringHelper.__wrap(__MoreObjects.toStringHelper(clazz))

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

    @staticmethod
    @overload
    def toStringHelper(className: str) -> 'ToStringHelper':
        """public static com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects.toStringHelper(java.lang.String)"""
        return ToStringHelper.__wrap(__MoreObjects.toStringHelper(className))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.google.common.base.MoreObjects
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.base.MoreObjects as __MoreObjects_ToStringHelper
__ToStringHelper = __MoreObjects_ToStringHelper.ToStringHelper
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.base.MoreObjects as __MoreObjects
__MoreObjects = __MoreObjects
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MoreObjects():
    """com.google.common.base.MoreObjects"""
 
    @staticmethod
    def __wrap(java_value: __MoreObjects) -> 'MoreObjects':
        return MoreObjects(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MoreObjects):
        """
        Dynamic initializer for MoreObjects.
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
 
    @staticmethod
    @overload
    def firstNonNull(first: object, second: object) -> object:
        """public static <T> T com.google.common.base.MoreObjects.firstNonNull(T,T)"""
        return object.__wrap(__MoreObjects.firstNonNull(first, second))

    @staticmethod
    @overload
    def toStringHelper(self: object) -> 'ToStringHelper':
        """public static com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects.toStringHelper(java.lang.Object)"""
        return ToStringHelper.__wrap(__MoreObjects.toStringHelper(self))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def toStringHelper(clazz: 'Class') -> 'ToStringHelper':
        """public static com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects.toStringHelper(java.lang.Class<?>)"""
        return ToStringHelper.__wrap(__MoreObjects.toStringHelper(clazz))

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

    @staticmethod
    @overload
    def toStringHelper(className: str) -> 'ToStringHelper':
        """public static com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects.toStringHelper(java.lang.String)"""
        return ToStringHelper.__wrap(__MoreObjects.toStringHelper(className))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.google.common.base.MoreObjects 
 
 
# CLASS: com.google.common.base.Objects
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.google.common.base.Objects as __Objects
__Objects = __Objects
from builtins import type
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Objects(__ExtraObjectsMethodsForWeb, ExtraObjectsMethodsForWeb):
    """com.google.common.base.Objects"""
 
    @staticmethod
    def __wrap(java_value: __Objects) -> 'Objects':
        return Objects(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Objects):
        """
        Dynamic initializer for Objects.
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

    @staticmethod
    @overload
    def equal(a: object, b: object) -> bool:
        """public static boolean com.google.common.base.Objects.equal(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(__Objects.equal(a, b))

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

    @staticmethod
    @overload
    def hashCode(*objects: object) -> int:
        """public static int com.google.common.base.Objects.hashCode(java.lang.Object...)"""
        return int.__wrap(__Objects.hashCode(objects))

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
 
 
# CLASS: com.google.common.base.StandardSystemProperty
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import com.google.common.base.StandardSystemProperty as __StandardSystemProperty
__StandardSystemProperty = __StandardSystemProperty
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class StandardSystemProperty(__Enum, Enum):
    """com.google.common.base.StandardSystemProperty"""
 
    @staticmethod
    def __wrap(java_value: __StandardSystemProperty) -> 'StandardSystemProperty':
        return StandardSystemProperty(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StandardSystemProperty):
        """
        Dynamic initializer for StandardSystemProperty.
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
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def values() -> List['StandardSystemProperty']:
        """public static com.google.common.base.StandardSystemProperty[] com.google.common.base.StandardSystemProperty.values()"""
        return List[StandardSystemProperty].__wrap(__StandardSystemProperty.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @overload
    def value(self) -> str:
        """public java.lang.String com.google.common.base.StandardSystemProperty.value()"""
        return str.__wrap(super(StandardSystemProperty, self).value())

    @staticmethod
    @overload
    def valueOf(name: str) -> 'StandardSystemProperty':
        """public static com.google.common.base.StandardSystemProperty com.google.common.base.StandardSystemProperty.valueOf(java.lang.String)"""
        return StandardSystemProperty.__wrap(__StandardSystemProperty.valueOf(name))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.base.StandardSystemProperty.toString()"""
        return str.__wrap(super(StandardSystemProperty, self).toString())

    @overload
    def key(self) -> str:
        """public java.lang.String com.google.common.base.StandardSystemProperty.key()"""
        return str.__wrap(super(StandardSystemProperty, self).key()) 
 
 
# CLASS: com.google.common.base.Equivalence
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.base.Equivalence as __Equivalence
__Equivalence = __Equivalence
import java.util.function.BiPredicate as __BiPredicate
__BiPredicate = __BiPredicate
import com.google.common.base.Equivalence as __Equivalence_Wrapper
__Wrapper = __Equivalence_Wrapper.Wrapper
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.function.BiPredicate as BiPredicate
import java.lang.Object as __Object
__Object = __Object
import com.google.common.base.Predicate as __Predicate
__Predicate = __Predicate
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Equivalence(ABC, __BiPredicate, BiPredicate):
    """com.google.common.base.Equivalence"""
 
    @staticmethod
    def __wrap(java_value: __Equivalence) -> 'Equivalence':
        return Equivalence(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Equivalence):
        """
        Dynamic initializer for Equivalence.
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
    def and(self, arg0: 'BiPredicate') -> 'BiPredicate':
        """public default java.util.function.BiPredicate<T, U> java.util.function.BiPredicate.and(java.util.function.BiPredicate<? super T, ? super U>)"""
        return 'BiPredicate'.__wrap(super(__BiPredicate, self).and(arg0))

    @overload
    def equivalent(self, a: object, b: object) -> bool:
        """public final boolean com.google.common.base.Equivalence.equivalent(T,T)"""
        return bool.__wrap(super(__Equivalence, self).equivalent(a, b))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def pairwise(self) -> 'Equivalence':
        """public final <S extends T> com.google.common.base.Equivalence<java.lang.Iterable<S>> com.google.common.base.Equivalence.pairwise()"""
        return 'Equivalence'.__wrap(super(Equivalence, self).pairwise())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def negate(self) -> 'BiPredicate':
        """public default java.util.function.BiPredicate<T, U> java.util.function.BiPredicate.negate()"""
        return 'BiPredicate'.__wrap(super(BiPredicate, self).negate())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def or(self, arg0: 'BiPredicate') -> 'BiPredicate':
        """public default java.util.function.BiPredicate<T, U> java.util.function.BiPredicate.or(java.util.function.BiPredicate<? super T, ? super U>)"""
        return 'BiPredicate'.__wrap(super(__BiPredicate, self).or(arg0))

    @overload
    def wrap(self, reference: object) -> 'Wrapper':
        """public final <S extends T> com.google.common.base.Equivalence$Wrapper<S> com.google.common.base.Equivalence.wrap(S)"""
        return 'Wrapper'.__wrap(super(__Equivalence, self).wrap(reference))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def identity() -> 'Equivalence':
        """public static com.google.common.base.Equivalence<java.lang.Object> com.google.common.base.Equivalence.identity()"""
        return Equivalence.__wrap(__Equivalence.identity())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def equals() -> 'Equivalence':
        """public static com.google.common.base.Equivalence<java.lang.Object> com.google.common.base.Equivalence.equals()"""
        return Equivalence.__wrap(__Equivalence.equals())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equivalentTo(self, target: object) -> 'Predicate':
        """public final com.google.common.base.Predicate<T> com.google.common.base.Equivalence.equivalentTo(T)"""
        return 'Predicate'.__wrap(super(__Equivalence, self).equivalentTo(target))

    @overload
    def test(self, t: object, u: object) -> bool:
        """public final boolean com.google.common.base.Equivalence.test(T,T)"""
        return bool.__wrap(super(__Equivalence, self).test(t, u))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def hash(self, t: object) -> int:
        """public final int com.google.common.base.Equivalence.hash(T)"""
        return int.__wrap(super(__Equivalence, self).hash(t))

    @overload
    def onResultOf(self, function: 'Function') -> 'Equivalence':
        """public final <F> com.google.common.base.Equivalence<F> com.google.common.base.Equivalence.onResultOf(com.google.common.base.Function<? super F, ? extends T>)"""
        return 'Equivalence'.__wrap(super(__Equivalence, self).onResultOf(function))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.base.VerifyException
import com.google.common.base.VerifyException as __VerifyException
__VerifyException = __VerifyException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class VerifyException(__RuntimeException, RuntimeException):
    """com.google.common.base.VerifyException"""
 
    @staticmethod
    def __wrap(java_value: __VerifyException) -> 'VerifyException':
        return VerifyException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __VerifyException):
        """
        Dynamic initializer for VerifyException.
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
    def __init__(self, message: str, cause: 'Throwable'):
        """public com.google.common.base.VerifyException(java.lang.String,java.lang.Throwable)"""
        val = __VerifyException(message, cause)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, message: str):
        """public com.google.common.base.VerifyException(java.lang.String)"""
        val = __VerifyException(message)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @overload
    def __init__(self):
        """public com.google.common.base.VerifyException()"""
        val = __VerifyException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, cause: 'Throwable'):
        """public com.google.common.base.VerifyException(java.lang.Throwable)"""
        val = __VerifyException(cause)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @overload
    def __init__(self, ):
        """public com.google.common.base.VerifyException()"""
        val = __VerifyException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: com.google.common.base.Predicate
import java.util.function.Predicate as Predicate
import java.lang.Object as __object
import java.util.function.Predicate as __Predicate
__Predicate = __Predicate
import com.google.common.base.Predicate as __Predicate
__Predicate = __Predicate
from abc import abstractmethod, ABC
from builtins import bool
 
class Predicate(ABC, __Predicate, Predicate):
    """com.google.common.base.Predicate"""
 
    @staticmethod
    def __wrap(java_value: __Predicate) -> 'Predicate':
        return Predicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Predicate):
        """
        Dynamic initializer for Predicate.
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
    def apply(self, input: object):
        """public abstract boolean com.google.common.base.Predicate.apply(T)"""
        pass

    @override
    @overload
    def negate(self) -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.negate()"""
        return 'Predicate'.__wrap(super(Predicate, self).negate())

    @overload
    def test(self, input: object) -> bool:
        """public default boolean com.google.common.base.Predicate.test(T)"""
        return bool.__wrap(super(__Predicate, self).test(input))

    @overload
    def and(self, arg0: 'Predicate') -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.and(java.util.function.Predicate<? super T>)"""
        return 'Predicate'.__wrap(super(__Predicate, self).and(arg0))

    @overload
    def or(self, arg0: 'Predicate') -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.or(java.util.function.Predicate<? super T>)"""
        return 'Predicate'.__wrap(super(__Predicate, self).or(arg0))

    @abstractmethod
    def equals(self, object: object):
        """public abstract boolean com.google.common.base.Predicate.equals(java.lang.Object)"""
        pass 
 
 
# CLASS: com.google.common.base.Joiner$MapJoiner
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Appendable as __Appendable
__Appendable = __Appendable
from builtins import type
import java.lang.Iterable as Iterable
import java.util.Iterator as Iterator
import java.lang.Appendable as Appendable
import com.google.common.base.Joiner as __Joiner_MapJoiner
__MapJoiner = __Joiner_MapJoiner.MapJoiner
import java.lang.Long as __long
import java.lang.StringBuilder as __StringBuilder
__StringBuilder = __StringBuilder
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class MapJoiner():
    """com.google.common.base.Joiner.MapJoiner"""
 
    @staticmethod
    def __wrap(java_value: __MapJoiner) -> 'MapJoiner':
        return MapJoiner(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MapJoiner):
        """
        Dynamic initializer for MapJoiner.
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
    def appendTo(self, appendable: 'Appendable', entries: 'Iterable') -> 'Appendable':
        """public <A extends java.lang.Appendable> A com.google.common.base.Joiner$MapJoiner.appendTo(A,java.lang.Iterable<? extends java.util.Map$Entry<?, ?>>) throws java.io.IOException"""
        return 'Appendable'.__wrap(super(__MapJoiner, self).appendTo(appendable, entries))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def join(self, entries: 'Iterable') -> str:
        """public java.lang.String com.google.common.base.Joiner$MapJoiner.join(java.lang.Iterable<? extends java.util.Map$Entry<?, ?>>)"""
        return str.__wrap(super(__MapJoiner, self).join(entries))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def appendTo(self, appendable: 'Appendable', map: 'Map') -> 'Appendable':
        """public <A extends java.lang.Appendable> A com.google.common.base.Joiner$MapJoiner.appendTo(A,java.util.Map<?, ?>) throws java.io.IOException"""
        return 'Appendable'.__wrap(super(__MapJoiner, self).appendTo(appendable, map))

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
    def appendTo(self, builder: 'StringBuilder', map: 'Map') -> 'StringBuilder':
        """public java.lang.StringBuilder com.google.common.base.Joiner$MapJoiner.appendTo(java.lang.StringBuilder,java.util.Map<?, ?>)"""
        return 'StringBuilder'.__wrap(super(__MapJoiner, self).appendTo(builder, map))

    @overload
    def join(self, entries: 'Iterator') -> str:
        """public java.lang.String com.google.common.base.Joiner$MapJoiner.join(java.util.Iterator<? extends java.util.Map$Entry<?, ?>>)"""
        return str.__wrap(super(__MapJoiner, self).join(entries))

    @overload
    def appendTo(self, appendable: 'Appendable', parts: 'Iterator') -> 'Appendable':
        """public <A extends java.lang.Appendable> A com.google.common.base.Joiner$MapJoiner.appendTo(A,java.util.Iterator<? extends java.util.Map$Entry<?, ?>>) throws java.io.IOException"""
        return 'Appendable'.__wrap(super(__MapJoiner, self).appendTo(appendable, parts))

    @overload
    def appendTo(self, builder: 'StringBuilder', entries: 'Iterable') -> 'StringBuilder':
        """public java.lang.StringBuilder com.google.common.base.Joiner$MapJoiner.appendTo(java.lang.StringBuilder,java.lang.Iterable<? extends java.util.Map$Entry<?, ?>>)"""
        return 'StringBuilder'.__wrap(super(__MapJoiner, self).appendTo(builder, entries))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def join(self, map: 'Map') -> str:
        """public java.lang.String com.google.common.base.Joiner$MapJoiner.join(java.util.Map<?, ?>)"""
        return str.__wrap(super(__MapJoiner, self).join(map))

    @overload
    def useForNull(self, nullText: str) -> 'MapJoiner':
        """public com.google.common.base.Joiner$MapJoiner com.google.common.base.Joiner$MapJoiner.useForNull(java.lang.String)"""
        return 'MapJoiner'.__wrap(super(__MapJoiner, self).useForNull(nullText))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def appendTo(self, builder: 'StringBuilder', entries: 'Iterator') -> 'StringBuilder':
        """public java.lang.StringBuilder com.google.common.base.Joiner$MapJoiner.appendTo(java.lang.StringBuilder,java.util.Iterator<? extends java.util.Map$Entry<?, ?>>)"""
        return 'StringBuilder'.__wrap(super(__MapJoiner, self).appendTo(builder, entries))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.base.Verify
from builtins import str
import java.lang.Character as __char
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import com.google.common.base.Verify as __Verify
__Verify = __Verify
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
from builtins import int
 
class Verify():
    """com.google.common.base.Verify"""
 
    @staticmethod
    def __wrap(java_value: __Verify) -> 'Verify':
        return Verify(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Verify):
        """
        Dynamic initializer for Verify.
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
    def verify(expression: bool, errorMessageTemplate: str, p1: int, p2: object):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,int,java.lang.Object)"""
        __Verify.verify(__boolean.valueOf(expression), errorMessageTemplate, __int.valueOf(p1), p2)

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: int, p2: int):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,long,int)"""
        __Verify.verify(__boolean.valueOf(expression), errorMessageTemplate, __long.valueOf(p1), __int.valueOf(p2))

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: object):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,java.lang.Object)"""
        __Verify.verify(__boolean.valueOf(expression), errorMessageTemplate, p1)

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: str):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,char)"""
        __Verify.verify(__boolean.valueOf(expression), errorMessageTemplate, __char.valueOf(p1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: object, p2: str):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,java.lang.Object,char)"""
        __Verify.verify(__boolean.valueOf(expression), errorMessageTemplate, p1, __char.valueOf(p2))

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: object, p2: object, p3: object, p4: object):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        __Verify.verify(__boolean.valueOf(expression), errorMessageTemplate, p1, p2, p3, p4)

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: int):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,int)"""
        __Verify.verify(__boolean.valueOf(expression), errorMessageTemplate, __int.valueOf(p1))

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, *errorMessageArgs: object):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,java.lang.Object...)"""
        __Verify.verify(__boolean.valueOf(expression), errorMessageTemplate, errorMessageArgs)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def verifyNotNull(reference: object) -> object:
        """public static <T> T com.google.common.base.Verify.verifyNotNull(T)"""
        return object.__wrap(__Verify.verifyNotNull(reference))

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: str, p2: object):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,char,java.lang.Object)"""
        __Verify.verify(__boolean.valueOf(expression), errorMessageTemplate, __char.valueOf(p1), p2)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: object, p2: object, p3: object):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        __Verify.verify(__boolean.valueOf(expression), errorMessageTemplate, p1, p2, p3)

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: int, p2: str):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,long,char)"""
        __Verify.verify(__boolean.valueOf(expression), errorMessageTemplate, __long.valueOf(p1), __char.valueOf(p2))

    @staticmethod
    @overload
    def verify(expression: bool):
        """public static void com.google.common.base.Verify.verify(boolean)"""
        __Verify.verify(__boolean.valueOf(expression))

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: int, p2: object):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,long,java.lang.Object)"""
        __Verify.verify(__boolean.valueOf(expression), errorMessageTemplate, __long.valueOf(p1), p2)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: int, p2: int):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,int,long)"""
        __Verify.verify(__boolean.valueOf(expression), errorMessageTemplate, __int.valueOf(p1), __long.valueOf(p2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def verifyNotNull(reference: object, errorMessageTemplate: str, *errorMessageArgs: object) -> object:
        """public static <T> T com.google.common.base.Verify.verifyNotNull(T,java.lang.String,java.lang.Object...)"""
        return object.__wrap(__Verify.verifyNotNull(reference, errorMessageTemplate, errorMessageArgs))

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: object, p2: object):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,java.lang.Object,java.lang.Object)"""
        __Verify.verify(__boolean.valueOf(expression), errorMessageTemplate, p1, p2)

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: int):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,long)"""
        __Verify.verify(__boolean.valueOf(expression), errorMessageTemplate, __long.valueOf(p1))

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: object, p2: int):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,java.lang.Object,int)"""
        __Verify.verify(__boolean.valueOf(expression), errorMessageTemplate, p1, __int.valueOf(p2))

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: str, p2: int):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,char,long)"""
        __Verify.verify(__boolean.valueOf(expression), errorMessageTemplate, __char.valueOf(p1), __long.valueOf(p2))

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: int, p2: int):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,int,int)"""
        __Verify.verify(__boolean.valueOf(expression), errorMessageTemplate, __int.valueOf(p1), __int.valueOf(p2))

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: int, p2: str):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,int,char)"""
        __Verify.verify(__boolean.valueOf(expression), errorMessageTemplate, __int.valueOf(p1), __char.valueOf(p2))

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

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: str, p2: str):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,char,char)"""
        __Verify.verify(__boolean.valueOf(expression), errorMessageTemplate, __char.valueOf(p1), __char.valueOf(p2))

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: object, p2: int):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,java.lang.Object,long)"""
        __Verify.verify(__boolean.valueOf(expression), errorMessageTemplate, p1, __long.valueOf(p2))

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: int, p2: int):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,long,long)"""
        __Verify.verify(__boolean.valueOf(expression), errorMessageTemplate, __long.valueOf(p1), __long.valueOf(p2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def verify(expression: bool, errorMessageTemplate: str, p1: str, p2: int):
        """public static void com.google.common.base.Verify.verify(boolean,java.lang.String,char,int)"""
        __Verify.verify(__boolean.valueOf(expression), errorMessageTemplate, __char.valueOf(p1), __int.valueOf(p2)) 
 
 
# CLASS: com.google.common.base.FinalizablePhantomReference
from builtins import str
from pyquantum_helper import override
import java.lang.ref.PhantomReference as __PhantomReference
__PhantomReference = __PhantomReference
import java.lang.Object as __object
from builtins import type
from builtins import object
from abc import abstractmethod, ABC
import java.lang.ref.Reference as __Reference
__Reference = __Reference
import java.lang.Long as __long
import com.google.common.base.FinalizableReference as __FinalizableReference
__FinalizableReference = __FinalizableReference
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.base.FinalizablePhantomReference as __FinalizablePhantomReference
__FinalizablePhantomReference = __FinalizablePhantomReference
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FinalizablePhantomReference(ABC, __PhantomReference, PhantomReference, __FinalizableReference, FinalizableReference):
    """com.google.common.base.FinalizablePhantomReference"""
 
    @staticmethod
    def __wrap(java_value: __FinalizablePhantomReference) -> 'FinalizablePhantomReference':
        return FinalizablePhantomReference(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FinalizablePhantomReference):
        """
        Dynamic initializer for FinalizablePhantomReference.
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
    def refersTo(self, arg0: object) -> bool:
        """public final boolean java.lang.ref.Reference.refersTo(T)"""
        return bool.__wrap(super(__Reference, self).refersTo(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def get(self) -> object:
        """public T java.lang.ref.PhantomReference.get()"""
        return object.__wrap(super(PhantomReference, self).get())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def clear(self):
        """public void java.lang.ref.Reference.clear()"""
        super(Reference, self).clear()

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

    @staticmethod
    @overload
    def reachabilityFence(arg0: object):
        """public static void java.lang.ref.Reference.reachabilityFence(java.lang.Object)"""
        __Reference.reachabilityFence(arg0)

    @override
    @overload
    def enqueue(self) -> bool:
        """public boolean java.lang.ref.Reference.enqueue()"""
        return bool.__wrap(super(Reference, self).enqueue())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @abstractmethod
    def finalizeReferent(self, ):
        """public abstract void com.google.common.base.FinalizableReference.finalizeReferent()"""
        pass

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
    def isEnqueued(self) -> bool:
        """public boolean java.lang.ref.Reference.isEnqueued()"""
        return bool.__wrap(super(Reference, self).isEnqueued()) 
 
 
# CLASS: com.google.common.base.Equivalence$Wrapper
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.base.Equivalence as __Equivalence_Wrapper
__Wrapper = __Equivalence_Wrapper.Wrapper
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Wrapper(__Serializable, Serializable):
    """com.google.common.base.Equivalence.Wrapper"""
 
    @staticmethod
    def __wrap(java_value: __Wrapper) -> 'Wrapper':
        return Wrapper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Wrapper):
        """
        Dynamic initializer for Wrapper.
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

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.base.Equivalence$Wrapper.equals(java.lang.Object)"""
        return bool.__wrap(super(__Wrapper, self).equals(obj))

    @overload
    def get(self) -> object:
        """public T com.google.common.base.Equivalence$Wrapper.get()"""
        return object.__wrap(super(Wrapper, self).get())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.base.Equivalence$Wrapper.hashCode()"""
        return int.__wrap(super(Wrapper, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.base.Equivalence$Wrapper.toString()"""
        return str.__wrap(super(Wrapper, self).toString())

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.common.base.Stopwatch
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.time.Duration as Duration
import com.google.common.base.Stopwatch as __Stopwatch
__Stopwatch = __Stopwatch
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.concurrent.TimeUnit as TimeUnit
import java.time.Duration as __Duration
__Duration = __Duration
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Stopwatch():
    """com.google.common.base.Stopwatch"""
 
    @staticmethod
    def __wrap(java_value: __Stopwatch) -> 'Stopwatch':
        return Stopwatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Stopwatch):
        """
        Dynamic initializer for Stopwatch.
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
    def elapsed(self, desiredUnit: 'TimeUnit') -> int:
        """public long com.google.common.base.Stopwatch.elapsed(java.util.concurrent.TimeUnit)"""
        return int.__wrap(super(__Stopwatch, self).elapsed(desiredUnit))

    @staticmethod
    @overload
    def createUnstarted(ticker: 'Ticker') -> 'Stopwatch':
        """public static com.google.common.base.Stopwatch com.google.common.base.Stopwatch.createUnstarted(com.google.common.base.Ticker)"""
        return Stopwatch.__wrap(__Stopwatch.createUnstarted(ticker))

    @overload
    def elapsed(self) -> 'Duration':
        """public java.time.Duration com.google.common.base.Stopwatch.elapsed()"""
        return 'Duration'.__wrap(super(Stopwatch, self).elapsed())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.base.Stopwatch.toString()"""
        return str.__wrap(super(Stopwatch, self).toString())

    @overload
    def stop(self) -> 'Stopwatch':
        """public com.google.common.base.Stopwatch com.google.common.base.Stopwatch.stop()"""
        return 'Stopwatch'.__wrap(super(Stopwatch, self).stop())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def reset(self) -> 'Stopwatch':
        """public com.google.common.base.Stopwatch com.google.common.base.Stopwatch.reset()"""
        return 'Stopwatch'.__wrap(super(Stopwatch, self).reset())

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

    @staticmethod
    @overload
    def createStarted(ticker: 'Ticker') -> 'Stopwatch':
        """public static com.google.common.base.Stopwatch com.google.common.base.Stopwatch.createStarted(com.google.common.base.Ticker)"""
        return Stopwatch.__wrap(__Stopwatch.createStarted(ticker))

    @staticmethod
    @overload
    def createUnstarted() -> 'Stopwatch':
        """public static com.google.common.base.Stopwatch com.google.common.base.Stopwatch.createUnstarted()"""
        return Stopwatch.__wrap(__Stopwatch.createUnstarted())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def start(self) -> 'Stopwatch':
        """public com.google.common.base.Stopwatch com.google.common.base.Stopwatch.start()"""
        return 'Stopwatch'.__wrap(super(Stopwatch, self).start())

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

    @staticmethod
    @overload
    def createStarted() -> 'Stopwatch':
        """public static com.google.common.base.Stopwatch com.google.common.base.Stopwatch.createStarted()"""
        return Stopwatch.__wrap(__Stopwatch.createStarted())

    @overload
    def isRunning(self) -> bool:
        """public boolean com.google.common.base.Stopwatch.isRunning()"""
        return bool.__wrap(super(Stopwatch, self).isRunning())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.base.Enums
import com.google.common.base.Converter as __Converter
__Converter = __Converter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.reflect.Field as Field
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.reflect.Field as __Field
__Field = __Field
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.google.common.base.Optional as __Optional
__Optional = __Optional
import com.google.common.base.Enums as __Enums
__Enums = __Enums
from builtins import int
 
class Enums():
    """com.google.common.base.Enums"""
 
    @staticmethod
    def __wrap(java_value: __Enums) -> 'Enums':
        return Enums(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Enums):
        """
        Dynamic initializer for Enums.
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

    @staticmethod
    @overload
    def getIfPresent(enumClass: 'Class', value: str) -> 'Optional':
        """public static <T extends java.lang.Enum<T>> com.google.common.base.Optional<T> com.google.common.base.Enums.getIfPresent(java.lang.Class<T>,java.lang.String)"""
        return Optional.__wrap(__Enums.getIfPresent(enumClass, value))

    @staticmethod
    @overload
    def getField(enumValue: 'Enum') -> 'Field':
        """public static java.lang.reflect.Field com.google.common.base.Enums.getField(java.lang.Enum<?>)"""
        return Field.__wrap(__Enums.getField(enumValue))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def stringConverter(enumClass: 'Class') -> 'Converter':
        """public static <T extends java.lang.Enum<T>> com.google.common.base.Converter<java.lang.String, T> com.google.common.base.Enums.stringConverter(java.lang.Class<T>)"""
        return Converter.__wrap(__Enums.stringConverter(enumClass)) 
 
 
# CLASS: com.google.common.base.Ticker
from builtins import str
import com.google.common.base.Ticker as __Ticker
__Ticker = __Ticker
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
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
from builtins import int
 
class Ticker(ABC):
    """com.google.common.base.Ticker"""
 
    @staticmethod
    def __wrap(java_value: __Ticker) -> 'Ticker':
        return Ticker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Ticker):
        """
        Dynamic initializer for Ticker.
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

    @abstractmethod
    def read(self, ):
        """public abstract long com.google.common.base.Ticker.read()"""
        pass

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

    @staticmethod
    @overload
    def systemTicker() -> 'Ticker':
        """public static com.google.common.base.Ticker com.google.common.base.Ticker.systemTicker()"""
        return Ticker.__wrap(__Ticker.systemTicker())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.common.base.Functions
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.base.Function as __Function
__Function = __Function
import com.google.common.base.Functions as __Functions
__Functions = __Functions
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class Functions():
    """com.google.common.base.Functions"""
 
    @staticmethod
    def __wrap(java_value: __Functions) -> 'Functions':
        return Functions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Functions):
        """
        Dynamic initializer for Functions.
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
    def forSupplier(supplier: 'Supplier') -> 'Function':
        """public static <F,T> com.google.common.base.Function<F, T> com.google.common.base.Functions.forSupplier(com.google.common.base.Supplier<T>)"""
        return Function.__wrap(__Functions.forSupplier(supplier))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def identity() -> 'Function':
        """public static <E> com.google.common.base.Function<E, E> com.google.common.base.Functions.identity()"""
        return Function.__wrap(__Functions.identity())

    @staticmethod
    @overload
    def compose(g: 'Function', f: 'Function') -> 'Function':
        """public static <A,B,C> com.google.common.base.Function<A, C> com.google.common.base.Functions.compose(com.google.common.base.Function<B, C>,com.google.common.base.Function<A, ? extends B>)"""
        return Function.__wrap(__Functions.compose(g, f))

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

    @staticmethod
    @overload
    def forMap(map: 'Map', defaultValue: object) -> 'Function':
        """public static <K,V> com.google.common.base.Function<K, V> com.google.common.base.Functions.forMap(java.util.Map<K, ? extends V>,V)"""
        return Function.__wrap(__Functions.forMap(map, defaultValue))

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

    @staticmethod
    @overload
    def forPredicate(predicate: 'Predicate') -> 'Function':
        """public static <T> com.google.common.base.Function<T, java.lang.Boolean> com.google.common.base.Functions.forPredicate(com.google.common.base.Predicate<T>)"""
        return Function.__wrap(__Functions.forPredicate(predicate))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def forMap(map: 'Map') -> 'Function':
        """public static <K,V> com.google.common.base.Function<K, V> com.google.common.base.Functions.forMap(java.util.Map<K, V>)"""
        return Function.__wrap(__Functions.forMap(map))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def toStringFunction() -> 'Function':
        """public static com.google.common.base.Function<java.lang.Object, java.lang.String> com.google.common.base.Functions.toStringFunction()"""
        return Function.__wrap(__Functions.toStringFunction())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def constant(value: object) -> 'Function':
        """public static <E> com.google.common.base.Function<java.lang.Object, E> com.google.common.base.Functions.constant(E)"""
        return Function.__wrap(__Functions.constant(value)) 
 
 
# CLASS: com.google.common.base.FinalizableWeakReference
import com.google.common.base.FinalizableWeakReference as __FinalizableWeakReference
__FinalizableWeakReference = __FinalizableWeakReference
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
from abc import abstractmethod, ABC
import java.lang.ref.Reference as __Reference
__Reference = __Reference
import java.lang.Long as __long
import com.google.common.base.FinalizableReference as __FinalizableReference
__FinalizableReference = __FinalizableReference
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FinalizableWeakReference(ABC, __WeakReference, WeakReference, __FinalizableReference, FinalizableReference):
    """com.google.common.base.FinalizableWeakReference"""
 
    @staticmethod
    def __wrap(java_value: __FinalizableWeakReference) -> 'FinalizableWeakReference':
        return FinalizableWeakReference(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FinalizableWeakReference):
        """
        Dynamic initializer for FinalizableWeakReference.
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
    def refersTo(self, arg0: object) -> bool:
        """public final boolean java.lang.ref.Reference.refersTo(T)"""
        return bool.__wrap(super(__Reference, self).refersTo(arg0))

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
    def clear(self):
        """public void java.lang.ref.Reference.clear()"""
        super(Reference, self).clear()

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

    @staticmethod
    @overload
    def reachabilityFence(arg0: object):
        """public static void java.lang.ref.Reference.reachabilityFence(java.lang.Object)"""
        __Reference.reachabilityFence(arg0)

    @override
    @overload
    def enqueue(self) -> bool:
        """public boolean java.lang.ref.Reference.enqueue()"""
        return bool.__wrap(super(Reference, self).enqueue())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @abstractmethod
    def finalizeReferent(self, ):
        """public abstract void com.google.common.base.FinalizableReference.finalizeReferent()"""
        pass

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def get(self) -> object:
        """public T java.lang.ref.Reference.get()"""
        return object.__wrap(super(Reference, self).get())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def isEnqueued(self) -> bool:
        """public boolean java.lang.ref.Reference.isEnqueued()"""
        return bool.__wrap(super(Reference, self).isEnqueued()) 
 
 
# CLASS: com.google.common.base.Throwables
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.lang.RuntimeException as __RuntimeException
__RuntimeException = __RuntimeException
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.google.common.base.Throwables as __Throwables
__Throwables = __Throwables
import java.lang.String as __String
__String = __String
import java.lang.RuntimeException as RuntimeException
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class Throwables():
    """com.google.common.base.Throwables"""
 
    @staticmethod
    def __wrap(java_value: __Throwables) -> 'Throwables':
        return Throwables(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Throwables):
        """
        Dynamic initializer for Throwables.
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
    def propagateIfInstanceOf(throwable: 'Throwable', declaredType: 'Class'):
        """public static <X extends java.lang.Throwable> void com.google.common.base.Throwables.propagateIfInstanceOf(java.lang.Throwable,java.lang.Class<X>) throws X"""
        __Throwables.propagateIfInstanceOf(throwable, declaredType)

    @staticmethod
    @overload
    def throwIfInstanceOf(throwable: 'Throwable', declaredType: 'Class'):
        """public static <X extends java.lang.Throwable> void com.google.common.base.Throwables.throwIfInstanceOf(java.lang.Throwable,java.lang.Class<X>) throws X"""
        __Throwables.throwIfInstanceOf(throwable, declaredType)

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
    def getStackTraceAsString(throwable: 'Throwable') -> str:
        """public static java.lang.String com.google.common.base.Throwables.getStackTraceAsString(java.lang.Throwable)"""
        return str.__wrap(__Throwables.getStackTraceAsString(throwable))

    @staticmethod
    @overload
    def lazyStackTrace(throwable: 'Throwable') -> 'List':
        """public static java.util.List<java.lang.StackTraceElement> com.google.common.base.Throwables.lazyStackTrace(java.lang.Throwable)"""
        return List.__wrap(__Throwables.lazyStackTrace(throwable))

    @staticmethod
    @overload
    def throwIfUnchecked(throwable: 'Throwable'):
        """public static void com.google.common.base.Throwables.throwIfUnchecked(java.lang.Throwable)"""
        __Throwables.throwIfUnchecked(throwable)

    @staticmethod
    @overload
    def propagateIfPossible(throwable: 'Throwable'):
        """public static void com.google.common.base.Throwables.propagateIfPossible(java.lang.Throwable)"""
        __Throwables.propagateIfPossible(throwable)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def getRootCause(throwable: 'Throwable') -> 'Throwable':
        """public static java.lang.Throwable com.google.common.base.Throwables.getRootCause(java.lang.Throwable)"""
        return Throwable.__wrap(__Throwables.getRootCause(throwable))

    @staticmethod
    @overload
    def getCausalChain(throwable: 'Throwable') -> 'List':
        """public static java.util.List<java.lang.Throwable> com.google.common.base.Throwables.getCausalChain(java.lang.Throwable)"""
        return List.__wrap(__Throwables.getCausalChain(throwable))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def propagate(throwable: 'Throwable') -> 'RuntimeException':
        """public static java.lang.RuntimeException com.google.common.base.Throwables.propagate(java.lang.Throwable)"""
        return RuntimeException.__wrap(__Throwables.propagate(throwable))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getCauseAs(throwable: 'Throwable', expectedCauseType: 'Class') -> 'Throwable':
        """public static <X extends java.lang.Throwable> X com.google.common.base.Throwables.getCauseAs(java.lang.Throwable,java.lang.Class<X>)"""
        return Throwable.__wrap(__Throwables.getCauseAs(throwable, expectedCauseType))

    @staticmethod
    @overload
    def lazyStackTraceIsLazy() -> bool:
        """public static boolean com.google.common.base.Throwables.lazyStackTraceIsLazy()"""
        return bool.__wrap(__Throwables.lazyStackTraceIsLazy())

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

    @staticmethod
    @overload
    def propagateIfPossible(throwable: 'Throwable', declaredType1: 'Class', declaredType2: 'Class'):
        """public static <X1 extends java.lang.Throwable,X2 extends java.lang.Throwable> void com.google.common.base.Throwables.propagateIfPossible(java.lang.Throwable,java.lang.Class<X1>,java.lang.Class<X2>) throws X1,X2"""
        __Throwables.propagateIfPossible(throwable, declaredType1, declaredType2)

    @staticmethod
    @overload
    def propagateIfPossible(throwable: 'Throwable', declaredType: 'Class'):
        """public static <X extends java.lang.Throwable> void com.google.common.base.Throwables.propagateIfPossible(java.lang.Throwable,java.lang.Class<X>) throws X"""
        __Throwables.propagateIfPossible(throwable, declaredType)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.base.Supplier
import com.google.common.base.Supplier as __Supplier
__Supplier = __Supplier
from abc import abstractmethod, ABC
 
class Supplier(ABC, __Supplier, Supplier):
    """com.google.common.base.Supplier"""
 
    @staticmethod
    def __wrap(java_value: __Supplier) -> 'Supplier':
        return Supplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Supplier):
        """
        Dynamic initializer for Supplier.
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
    def get(self, ):
        """public abstract T com.google.common.base.Supplier.get()"""
        pass 
 
 
# CLASS: com.google.common.base.Optional
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import java.lang.Iterable as Iterable
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.google.common.base.Optional as __Optional
__Optional = __Optional
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Optional(ABC, __Serializable, Serializable):
    """com.google.common.base.Optional"""
 
    @staticmethod
    def __wrap(java_value: __Optional) -> 'Optional':
        return Optional(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Optional):
        """
        Dynamic initializer for Optional.
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

    @abstractmethod
    def equals(self, object: object):
        """public abstract boolean com.google.common.base.Optional.equals(java.lang.Object)"""
        pass

    @overload
    def toJavaUtil(self) -> 'Optional':
        """public java.util.Optional<T> com.google.common.base.Optional.toJavaUtil()"""
        return 'Optional'.__wrap(super(Optional, self).toJavaUtil())

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String com.google.common.base.Optional.toString()"""
        pass

    @staticmethod
    @overload
    def fromNullable(nullableReference: object) -> 'Optional':
        """public static <T> com.google.common.base.Optional<T> com.google.common.base.Optional.fromNullable(T)"""
        return Optional.__wrap(__Optional.fromNullable(nullableReference))

    @staticmethod
    @overload
    def toJavaUtil(googleOptional: 'Optional') -> 'Optional':
        """public static <T> java.util.Optional<T> com.google.common.base.Optional.toJavaUtil(com.google.common.base.Optional<T>)"""
        return Optional.__wrap(__Optional.toJavaUtil(googleOptional))

    @abstractmethod
    def or(self, secondChoice: 'Optional'):
        """public abstract com.google.common.base.Optional<T> com.google.common.base.Optional.or(com.google.common.base.Optional<? extends T>)"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def isPresent(self, ):
        """public abstract boolean com.google.common.base.Optional.isPresent()"""
        pass

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

    @abstractmethod
    def hashCode(self, ):
        """public abstract int com.google.common.base.Optional.hashCode()"""
        pass

    @staticmethod
    @overload
    def of(reference: object) -> 'Optional':
        """public static <T> com.google.common.base.Optional<T> com.google.common.base.Optional.of(T)"""
        return Optional.__wrap(__Optional.of(reference))

    @abstractmethod
    def or(self, supplier: 'Supplier'):
        """public abstract T com.google.common.base.Optional.or(com.google.common.base.Supplier<? extends T>)"""
        pass

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def presentInstances(optionals: 'Iterable') -> 'Iterable':
        """public static <T> java.lang.Iterable<T> com.google.common.base.Optional.presentInstances(java.lang.Iterable<? extends com.google.common.base.Optional<? extends T>>)"""
        return Iterable.__wrap(__Optional.presentInstances(optionals))

    @abstractmethod
    def or(self, defaultValue: object):
        """public abstract T com.google.common.base.Optional.or(T)"""
        pass

    @staticmethod
    @overload
    def absent() -> 'Optional':
        """public static <T> com.google.common.base.Optional<T> com.google.common.base.Optional.absent()"""
        return Optional.__wrap(__Optional.absent())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def get(self, ):
        """public abstract T com.google.common.base.Optional.get()"""
        pass

    @abstractmethod
    def transform(self, function: 'Function'):
        """public abstract <V> com.google.common.base.Optional<V> com.google.common.base.Optional.transform(com.google.common.base.Function<? super T, V>)"""
        pass

    @abstractmethod
    def orNull(self, ):
        """public abstract T com.google.common.base.Optional.orNull()"""
        pass

    @staticmethod
    @overload
    def fromJavaUtil(javaUtilOptional: 'Optional') -> 'Optional':
        """public static <T> com.google.common.base.Optional<T> com.google.common.base.Optional.fromJavaUtil(java.util.Optional<T>)"""
        return Optional.__wrap(__Optional.fromJavaUtil(javaUtilOptional))

    @abstractmethod
    def asSet(self, ):
        """public abstract java.util.Set<T> com.google.common.base.Optional.asSet()"""
        pass 
 
 
# CLASS: com.google.common.base.CaseFormat
from builtins import str
import com.google.common.base.Converter as __Converter
__Converter = __Converter
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import com.google.common.base.CaseFormat as __CaseFormat
__CaseFormat = __CaseFormat
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class CaseFormat(ABC, __Enum, Enum):
    """com.google.common.base.CaseFormat"""
 
    @staticmethod
    def __wrap(java_value: __CaseFormat) -> 'CaseFormat':
        return CaseFormat(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CaseFormat):
        """
        Dynamic initializer for CaseFormat.
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
    def values() -> List['CaseFormat']:
        """public static com.google.common.base.CaseFormat[] com.google.common.base.CaseFormat.values()"""
        return List[CaseFormat].__wrap(__CaseFormat.values())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def valueOf(name: str) -> 'CaseFormat':
        """public static com.google.common.base.CaseFormat com.google.common.base.CaseFormat.valueOf(java.lang.String)"""
        return CaseFormat.__wrap(__CaseFormat.valueOf(name))

    @overload
    def converterTo(self, targetFormat: 'CaseFormat') -> 'Converter':
        """public com.google.common.base.Converter<java.lang.String, java.lang.String> com.google.common.base.CaseFormat.converterTo(com.google.common.base.CaseFormat)"""
        return 'Converter'.__wrap(super(__CaseFormat, self).converterTo(targetFormat))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def to(self, format: 'CaseFormat', str: str) -> str:
        """public final java.lang.String com.google.common.base.CaseFormat.to(com.google.common.base.CaseFormat,java.lang.String)"""
        return str.__wrap(super(__CaseFormat, self).to(format, str))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: com.google.common.base.Converter
import com.google.common.base.Converter as __Converter
__Converter = __Converter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
import java.util.function.Function as __Function
__Function = __Function
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
from builtins import bool
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
from builtins import int
 
class Converter(ABC, __Function, Function):
    """com.google.common.base.Converter"""
 
    @staticmethod
    def __wrap(java_value: __Converter) -> 'Converter':
        return Converter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Converter):
        """
        Dynamic initializer for Converter.
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
    def convertAll(self, fromIterable: 'Iterable') -> 'Iterable':
        """public java.lang.Iterable<B> com.google.common.base.Converter.convertAll(java.lang.Iterable<? extends A>)"""
        return 'Iterable'.__wrap(super(__Converter, self).convertAll(fromIterable))

    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'.__wrap(super(__Function, self).andThen(arg0))

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

    @staticmethod
    @overload
    def identity() -> 'Converter':
        """public static <T> com.google.common.base.Converter<T, T> com.google.common.base.Converter.identity()"""
        return Converter.__wrap(__Converter.identity())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def apply(self, a: object) -> object:
        """public final B com.google.common.base.Converter.apply(A)"""
        return object.__wrap(super(__Converter, self).apply(a))

    @staticmethod
    @overload
    def from(forwardFunction: 'Function', backwardFunction: 'Function') -> 'Converter':
        """public static <A,B> com.google.common.base.Converter<A, B> com.google.common.base.Converter.from(com.google.common.base.Function<? super A, ? extends B>,com.google.common.base.Function<? super B, ? extends A>)"""
        return Converter.__wrap(__Converter.from(forwardFunction, backwardFunction))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, object: object) -> bool:
        """public boolean com.google.common.base.Converter.equals(java.lang.Object)"""
        return bool.__wrap(super(__Converter, self).equals(object))

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
    def reverse(self) -> 'Converter':
        """public com.google.common.base.Converter<B, A> com.google.common.base.Converter.reverse()"""
        return 'Converter'.__wrap(super(Converter, self).reverse())

    @overload
    def convert(self, a: object) -> object:
        """public final B com.google.common.base.Converter.convert(A)"""
        return object.__wrap(super(__Converter, self).convert(a))

    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'.__wrap(super(__Function, self).compose(arg0))

    @overload
    def andThen(self, secondConverter: 'Converter') -> 'Converter':
        """public final <C> com.google.common.base.Converter<A, C> com.google.common.base.Converter.andThen(com.google.common.base.Converter<B, C>)"""
        return 'Converter'.__wrap(super(__Converter, self).andThen(secondConverter)) 
 
 
# CLASS: com.google.common.base.Ascii
from builtins import str
import java.lang.Character as __char
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
import com.google.common.base.Ascii as __Ascii
__Ascii = __Ascii
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Ascii():
    """com.google.common.base.Ascii"""
 
    @staticmethod
    def __wrap(java_value: __Ascii) -> 'Ascii':
        return Ascii(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Ascii):
        """
        Dynamic initializer for Ascii.
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
 
    @staticmethod
    @overload
    def toUpperCase(string: str) -> str:
        """public static java.lang.String com.google.common.base.Ascii.toUpperCase(java.lang.String)"""
        return str.__wrap(__Ascii.toUpperCase(string))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def isLowerCase(c: str) -> bool:
        """public static boolean com.google.common.base.Ascii.isLowerCase(char)"""
        return bool.__wrap(__Ascii.isLowerCase(__char.valueOf(c)))

    @staticmethod
    @overload
    def isUpperCase(c: str) -> bool:
        """public static boolean com.google.common.base.Ascii.isUpperCase(char)"""
        return bool.__wrap(__Ascii.isUpperCase(__char.valueOf(c)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def truncate(seq: 'CharSequence', maxLength: int, truncationIndicator: str) -> str:
        """public static java.lang.String com.google.common.base.Ascii.truncate(java.lang.CharSequence,int,java.lang.String)"""
        return str.__wrap(__Ascii.truncate(seq, __int.valueOf(maxLength), truncationIndicator))

    @staticmethod
    @overload
    def toLowerCase(string: str) -> str:
        """public static java.lang.String com.google.common.base.Ascii.toLowerCase(java.lang.String)"""
        return str.__wrap(__Ascii.toLowerCase(string))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def toLowerCase(c: str) -> str:
        """public static char com.google.common.base.Ascii.toLowerCase(char)"""
        return str.__wrap(__Ascii.toLowerCase(__char.valueOf(c)))

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

    @staticmethod
    @overload
    def toLowerCase(chars: 'CharSequence') -> str:
        """public static java.lang.String com.google.common.base.Ascii.toLowerCase(java.lang.CharSequence)"""
        return str.__wrap(__Ascii.toLowerCase(chars))

    @staticmethod
    @overload
    def toUpperCase(c: str) -> str:
        """public static char com.google.common.base.Ascii.toUpperCase(char)"""
        return str.__wrap(__Ascii.toUpperCase(__char.valueOf(c)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def toUpperCase(chars: 'CharSequence') -> str:
        """public static java.lang.String com.google.common.base.Ascii.toUpperCase(java.lang.CharSequence)"""
        return str.__wrap(__Ascii.toUpperCase(chars))

    @staticmethod
    @overload
    def equalsIgnoreCase(s1: 'CharSequence', s2: 'CharSequence') -> bool:
        """public static boolean com.google.common.base.Ascii.equalsIgnoreCase(java.lang.CharSequence,java.lang.CharSequence)"""
        return bool.__wrap(__Ascii.equalsIgnoreCase(s1, s2)) 
 
 
# CLASS: com.google.common.base.Charsets
import com.google.common.base.Charsets as __Charsets
__Charsets = __Charsets
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Charsets():
    """com.google.common.base.Charsets"""
 
    @staticmethod
    def __wrap(java_value: __Charsets) -> 'Charsets':
        return Charsets(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Charsets):
        """
        Dynamic initializer for Charsets.
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.common.base.Predicates
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.base.Predicates as __Predicates
__Predicates = __Predicates
import java.util.regex.Pattern as Pattern
import com.google.common.base.Predicate as __Predicate
__Predicate = __Predicate
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Predicates():
    """com.google.common.base.Predicates"""
 
    @staticmethod
    def __wrap(java_value: __Predicates) -> 'Predicates':
        return Predicates(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Predicates):
        """
        Dynamic initializer for Predicates.
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
    def alwaysFalse() -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.alwaysFalse()"""
        return Predicate.__wrap(__Predicates.alwaysFalse())

    @staticmethod
    @overload
    def in(target: 'Collection') -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.in(java.util.Collection<? extends T>)"""
        return Predicate.__wrap(__Predicates.in(target))

    @staticmethod
    @overload
    def instanceOf(clazz: 'Class') -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.instanceOf(java.lang.Class<?>)"""
        return Predicate.__wrap(__Predicates.instanceOf(clazz))

    @staticmethod
    @overload
    def and(components: 'Iterable') -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.and(java.lang.Iterable<? extends com.google.common.base.Predicate<? super T>>)"""
        return Predicate.__wrap(__Predicates.and(components))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def notNull() -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.notNull()"""
        return Predicate.__wrap(__Predicates.notNull())

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
    def and(*components: 'Predicate') -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.and(com.google.common.base.Predicate<? super T>...)"""
        return Predicate.__wrap(__Predicates.and(components))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def containsPattern(pattern: str) -> 'Predicate':
        """public static com.google.common.base.Predicate<java.lang.CharSequence> com.google.common.base.Predicates.containsPattern(java.lang.String)"""
        return Predicate.__wrap(__Predicates.containsPattern(pattern))

    @staticmethod
    @overload
    def contains(pattern: 'Pattern') -> 'Predicate':
        """public static com.google.common.base.Predicate<java.lang.CharSequence> com.google.common.base.Predicates.contains(java.util.regex.Pattern)"""
        return Predicate.__wrap(__Predicates.contains(pattern))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def compose(predicate: 'Predicate', function: 'Function') -> 'Predicate':
        """public static <A,B> com.google.common.base.Predicate<A> com.google.common.base.Predicates.compose(com.google.common.base.Predicate<B>,com.google.common.base.Function<A, ? extends B>)"""
        return Predicate.__wrap(__Predicates.compose(predicate, function))

    @staticmethod
    @overload
    def and(first: 'Predicate', second: 'Predicate') -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.and(com.google.common.base.Predicate<? super T>,com.google.common.base.Predicate<? super T>)"""
        return Predicate.__wrap(__Predicates.and(first, second))

    @staticmethod
    @overload
    def alwaysTrue() -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.alwaysTrue()"""
        return Predicate.__wrap(__Predicates.alwaysTrue())

    @staticmethod
    @overload
    def or(*components: 'Predicate') -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.or(com.google.common.base.Predicate<? super T>...)"""
        return Predicate.__wrap(__Predicates.or(components))

    @staticmethod
    @overload
    def equalTo(target: object) -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.equalTo(T)"""
        return Predicate.__wrap(__Predicates.equalTo(target))

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

    @staticmethod
    @overload
    def isNull() -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.isNull()"""
        return Predicate.__wrap(__Predicates.isNull())

    @staticmethod
    @overload
    def subtypeOf(clazz: 'Class') -> 'Predicate':
        """public static com.google.common.base.Predicate<java.lang.Class<?>> com.google.common.base.Predicates.subtypeOf(java.lang.Class<?>)"""
        return Predicate.__wrap(__Predicates.subtypeOf(clazz))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def or(components: 'Iterable') -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.or(java.lang.Iterable<? extends com.google.common.base.Predicate<? super T>>)"""
        return Predicate.__wrap(__Predicates.or(components))

    @staticmethod
    @overload
    def not(predicate: 'Predicate') -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.not(com.google.common.base.Predicate<T>)"""
        return Predicate.__wrap(__Predicates.not(predicate))

    @staticmethod
    @overload
    def or(first: 'Predicate', second: 'Predicate') -> 'Predicate':
        """public static <T> com.google.common.base.Predicate<T> com.google.common.base.Predicates.or(com.google.common.base.Predicate<? super T>,com.google.common.base.Predicate<? super T>)"""
        return Predicate.__wrap(__Predicates.or(first, second)) 
 
 
# CLASS: com.google.common.base.FinalizableReferenceQueue
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import com.google.common.base.FinalizableReferenceQueue as __FinalizableReferenceQueue
__FinalizableReferenceQueue = __FinalizableReferenceQueue
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FinalizableReferenceQueue(__Closeable, Closeable):
    """com.google.common.base.FinalizableReferenceQueue"""
 
    @staticmethod
    def __wrap(java_value: __FinalizableReferenceQueue) -> 'FinalizableReferenceQueue':
        return FinalizableReferenceQueue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FinalizableReferenceQueue):
        """
        Dynamic initializer for FinalizableReferenceQueue.
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
    def __init__(self):
        """public com.google.common.base.FinalizableReferenceQueue()"""
        val = __FinalizableReferenceQueue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.google.common.base.FinalizableReferenceQueue()"""
        val = __FinalizableReferenceQueue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def close(self):
        """public void com.google.common.base.FinalizableReferenceQueue.close()"""
        super(FinalizableReferenceQueue, self).close()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.common.base.Function
import java.util.function.Function as __Function
__Function = __Function
import com.google.common.base.Function as __Function
__Function = __Function
from abc import abstractmethod, ABC
import java.util.function.Function as Function
 
class Function(ABC, __Function, Function):
    """com.google.common.base.Function"""
 
    @staticmethod
    def __wrap(java_value: __Function) -> 'Function':
        return Function(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Function):
        """
        Dynamic initializer for Function.
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
 
    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'.__wrap(super(__Function, self).andThen(arg0))

    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'.__wrap(super(__Function, self).compose(arg0))

    @abstractmethod
    def equals(self, object: object):
        """public abstract boolean com.google.common.base.Function.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def apply(self, input: object):
        """public abstract T com.google.common.base.Function.apply(F)"""
        pass 
 
 
# CLASS: com.google.common.base.CharMatcher
from builtins import str
import java.util.function.Predicate as Predicate
import java.lang.CharSequence as CharSequence
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.function.Predicate as __Predicate
__Predicate = __Predicate
import com.google.common.base.CharMatcher as __CharMatcher
__CharMatcher = __CharMatcher
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Character as Character
import java.lang.Integer as __int
import com.google.common.base.Predicate as __Predicate
__Predicate = __Predicate
from builtins import bool
from builtins import int
 
class CharMatcher(ABC, __Predicate, Predicate):
    """com.google.common.base.CharMatcher"""
 
    @staticmethod
    def __wrap(java_value: __CharMatcher) -> 'CharMatcher':
        return CharMatcher(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CharMatcher):
        """
        Dynamic initializer for CharMatcher.
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
    def toString(self) -> str:
        """public java.lang.String com.google.common.base.CharMatcher.toString()"""
        return str.__wrap(super(CharMatcher, self).toString())

    @staticmethod
    @overload
    def javaDigit() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.javaDigit()"""
        return CharMatcher.__wrap(__CharMatcher.javaDigit())

    @overload
    def matchesAnyOf(self, sequence: 'CharSequence') -> bool:
        """public boolean com.google.common.base.CharMatcher.matchesAnyOf(java.lang.CharSequence)"""
        return bool.__wrap(super(__CharMatcher, self).matchesAnyOf(sequence))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def negate(self) -> 'CharMatcher':
        """public com.google.common.base.CharMatcher com.google.common.base.CharMatcher.negate()"""
        return 'CharMatcher'.__wrap(super(CharMatcher, self).negate())

    @overload
    def trimTrailingFrom(self, sequence: 'CharSequence') -> str:
        """public java.lang.String com.google.common.base.CharMatcher.trimTrailingFrom(java.lang.CharSequence)"""
        return str.__wrap(super(__CharMatcher, self).trimTrailingFrom(sequence))

    @staticmethod
    @overload
    def javaLetterOrDigit() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.javaLetterOrDigit()"""
        return CharMatcher.__wrap(__CharMatcher.javaLetterOrDigit())

    @overload
    def replaceFrom(self, sequence: 'CharSequence', replacement: 'CharSequence') -> str:
        """public java.lang.String com.google.common.base.CharMatcher.replaceFrom(java.lang.CharSequence,java.lang.CharSequence)"""
        return str.__wrap(super(__CharMatcher, self).replaceFrom(sequence, replacement))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def none() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.none()"""
        return CharMatcher.__wrap(__CharMatcher.none())

    @staticmethod
    @overload
    def ascii() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.ascii()"""
        return CharMatcher.__wrap(__CharMatcher.ascii())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def trimAndCollapseFrom(self, sequence: 'CharSequence', replacement: str) -> str:
        """public java.lang.String com.google.common.base.CharMatcher.trimAndCollapseFrom(java.lang.CharSequence,char)"""
        return str.__wrap(super(__CharMatcher, self).trimAndCollapseFrom(sequence, __char.valueOf(replacement)))

    @abstractmethod
    def matches(self, c: str):
        """public abstract boolean com.google.common.base.CharMatcher.matches(char)"""
        pass

    @staticmethod
    @overload
    def anyOf(sequence: 'CharSequence') -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.anyOf(java.lang.CharSequence)"""
        return CharMatcher.__wrap(__CharMatcher.anyOf(sequence))

    @staticmethod
    @overload
    def is(match: str) -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.is(char)"""
        return CharMatcher.__wrap(__CharMatcher.is(__char.valueOf(match)))

    @staticmethod
    @overload
    def inRange(startInclusive: str, endInclusive: str) -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.inRange(char,char)"""
        return CharMatcher.__wrap(__CharMatcher.inRange(__char.valueOf(startInclusive), __char.valueOf(endInclusive)))

    @staticmethod
    @overload
    def javaLowerCase() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.javaLowerCase()"""
        return CharMatcher.__wrap(__CharMatcher.javaLowerCase())

    @overload
    def or(self, other: 'CharMatcher') -> 'CharMatcher':
        """public com.google.common.base.CharMatcher com.google.common.base.CharMatcher.or(com.google.common.base.CharMatcher)"""
        return 'CharMatcher'.__wrap(super(__CharMatcher, self).or(other))

    @staticmethod
    @overload
    def noneOf(sequence: 'CharSequence') -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.noneOf(java.lang.CharSequence)"""
        return CharMatcher.__wrap(__CharMatcher.noneOf(sequence))

    @overload
    def trimFrom(self, sequence: 'CharSequence') -> str:
        """public java.lang.String com.google.common.base.CharMatcher.trimFrom(java.lang.CharSequence)"""
        return str.__wrap(super(__CharMatcher, self).trimFrom(sequence))

    @overload
    def and(self, other: 'CharMatcher') -> 'CharMatcher':
        """public com.google.common.base.CharMatcher com.google.common.base.CharMatcher.and(com.google.common.base.CharMatcher)"""
        return 'CharMatcher'.__wrap(super(__CharMatcher, self).and(other))

    @overload
    def collapseFrom(self, sequence: 'CharSequence', replacement: str) -> str:
        """public java.lang.String com.google.common.base.CharMatcher.collapseFrom(java.lang.CharSequence,char)"""
        return str.__wrap(super(__CharMatcher, self).collapseFrom(sequence, __char.valueOf(replacement)))

    @overload
    def removeFrom(self, sequence: 'CharSequence') -> str:
        """public java.lang.String com.google.common.base.CharMatcher.removeFrom(java.lang.CharSequence)"""
        return str.__wrap(super(__CharMatcher, self).removeFrom(sequence))

    @staticmethod
    @overload
    def invisible() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.invisible()"""
        return CharMatcher.__wrap(__CharMatcher.invisible())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def javaIsoControl() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.javaIsoControl()"""
        return CharMatcher.__wrap(__CharMatcher.javaIsoControl())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def replaceFrom(self, sequence: 'CharSequence', replacement: str) -> str:
        """public java.lang.String com.google.common.base.CharMatcher.replaceFrom(java.lang.CharSequence,char)"""
        return str.__wrap(super(__CharMatcher, self).replaceFrom(sequence, __char.valueOf(replacement)))

    @staticmethod
    @overload
    def forPredicate(predicate: 'Predicate') -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.forPredicate(com.google.common.base.Predicate<? super java.lang.Character>)"""
        return CharMatcher.__wrap(__CharMatcher.forPredicate(predicate))

    @staticmethod
    @overload
    def breakingWhitespace() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.breakingWhitespace()"""
        return CharMatcher.__wrap(__CharMatcher.breakingWhitespace())

    @overload
    def retainFrom(self, sequence: 'CharSequence') -> str:
        """public java.lang.String com.google.common.base.CharMatcher.retainFrom(java.lang.CharSequence)"""
        return str.__wrap(super(__CharMatcher, self).retainFrom(sequence))

    @overload
    def countIn(self, sequence: 'CharSequence') -> int:
        """public int com.google.common.base.CharMatcher.countIn(java.lang.CharSequence)"""
        return int.__wrap(super(__CharMatcher, self).countIn(sequence))

    @staticmethod
    @overload
    def singleWidth() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.singleWidth()"""
        return CharMatcher.__wrap(__CharMatcher.singleWidth())

    @overload
    def trimLeadingFrom(self, sequence: 'CharSequence') -> str:
        """public java.lang.String com.google.common.base.CharMatcher.trimLeadingFrom(java.lang.CharSequence)"""
        return str.__wrap(super(__CharMatcher, self).trimLeadingFrom(sequence))

    @overload
    def or(self, arg0: 'Predicate') -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.or(java.util.function.Predicate<? super T>)"""
        return 'Predicate'.__wrap(super(__Predicate, self).or(arg0))

    @staticmethod
    @overload
    def isNot(match: str) -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.isNot(char)"""
        return CharMatcher.__wrap(__CharMatcher.isNot(__char.valueOf(match)))

    @overload
    def and(self, arg0: 'Predicate') -> 'Predicate':
        """public default java.util.function.Predicate<T> java.util.function.Predicate.and(java.util.function.Predicate<? super T>)"""
        return 'Predicate'.__wrap(super(__Predicate, self).and(arg0))

    @overload
    def apply(self, character: 'Character') -> bool:
        """public boolean com.google.common.base.CharMatcher.apply(java.lang.Character)"""
        return bool.__wrap(super(__CharMatcher, self).apply(character))

    @overload
    def matchesAllOf(self, sequence: 'CharSequence') -> bool:
        """public boolean com.google.common.base.CharMatcher.matchesAllOf(java.lang.CharSequence)"""
        return bool.__wrap(super(__CharMatcher, self).matchesAllOf(sequence))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def matchesNoneOf(self, sequence: 'CharSequence') -> bool:
        """public boolean com.google.common.base.CharMatcher.matchesNoneOf(java.lang.CharSequence)"""
        return bool.__wrap(super(__CharMatcher, self).matchesNoneOf(sequence))

    @staticmethod
    @overload
    def digit() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.digit()"""
        return CharMatcher.__wrap(__CharMatcher.digit())

    @overload
    def indexIn(self, sequence: 'CharSequence', start: int) -> int:
        """public int com.google.common.base.CharMatcher.indexIn(java.lang.CharSequence,int)"""
        return int.__wrap(super(__CharMatcher, self).indexIn(sequence, __int.valueOf(start)))

    @overload
    def indexIn(self, sequence: 'CharSequence') -> int:
        """public int com.google.common.base.CharMatcher.indexIn(java.lang.CharSequence)"""
        return int.__wrap(super(__CharMatcher, self).indexIn(sequence))

    @staticmethod
    @overload
    def javaUpperCase() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.javaUpperCase()"""
        return CharMatcher.__wrap(__CharMatcher.javaUpperCase())

    @overload
    def lastIndexIn(self, sequence: 'CharSequence') -> int:
        """public int com.google.common.base.CharMatcher.lastIndexIn(java.lang.CharSequence)"""
        return int.__wrap(super(__CharMatcher, self).lastIndexIn(sequence))

    @staticmethod
    @overload
    def any() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.any()"""
        return CharMatcher.__wrap(__CharMatcher.any())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def precomputed(self) -> 'CharMatcher':
        """public com.google.common.base.CharMatcher com.google.common.base.CharMatcher.precomputed()"""
        return 'CharMatcher'.__wrap(super(CharMatcher, self).precomputed())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def test(self, input: object) -> bool:
        """public default boolean com.google.common.base.Predicate.test(T)"""
        return bool.__wrap(super(__Predicate, self).test(input))

    @staticmethod
    @overload
    def javaLetter() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.javaLetter()"""
        return CharMatcher.__wrap(__CharMatcher.javaLetter())

    @staticmethod
    @overload
    def whitespace() -> 'CharMatcher':
        """public static com.google.common.base.CharMatcher com.google.common.base.CharMatcher.whitespace()"""
        return CharMatcher.__wrap(__CharMatcher.whitespace()) 
 
 
# CLASS: com.google.common.base.Defaults
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.google.common.base.Defaults as __Defaults
__Defaults = __Defaults
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Defaults():
    """com.google.common.base.Defaults"""
 
    @staticmethod
    def __wrap(java_value: __Defaults) -> 'Defaults':
        return Defaults(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Defaults):
        """
        Dynamic initializer for Defaults.
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

    @staticmethod
    @overload
    def defaultValue(type: 'Class') -> object:
        """public static <T> T com.google.common.base.Defaults.defaultValue(java.lang.Class<T>)"""
        return object.__wrap(__Defaults.defaultValue(type))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.common.base.Utf8
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.google.common.base.Utf8 as __Utf8
__Utf8 = __Utf8
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Utf8():
    """com.google.common.base.Utf8"""
 
    @staticmethod
    def __wrap(java_value: __Utf8) -> 'Utf8':
        return Utf8(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Utf8):
        """
        Dynamic initializer for Utf8.
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

    @staticmethod
    @overload
    def isWellFormed(bytes: bytes, off: int, len: int) -> bool:
        """public static boolean com.google.common.base.Utf8.isWellFormed(byte[],int,int)"""
        return bool.__wrap(__Utf8.isWellFormed(bytes, __int.valueOf(off), __int.valueOf(len)))

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

    @staticmethod
    @overload
    def encodedLength(sequence: 'CharSequence') -> int:
        """public static int com.google.common.base.Utf8.encodedLength(java.lang.CharSequence)"""
        return int.__wrap(__Utf8.encodedLength(sequence))

    @staticmethod
    @overload
    def isWellFormed(bytes: bytes) -> bool:
        """public static boolean com.google.common.base.Utf8.isWellFormed(byte[])"""
        return bool.__wrap(__Utf8.isWellFormed(bytes))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.common.base.Splitter
from builtins import str
import java.lang.CharSequence as CharSequence
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.lang.Iterable as Iterable
import com.google.common.base.Splitter as __Splitter_MapSplitter
__MapSplitter = __Splitter_MapSplitter.MapSplitter
import com.google.common.base.Splitter as __Splitter
__Splitter = __Splitter
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
import java.util.regex.Pattern as Pattern
from builtins import bool
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
import java.util.List as List
from builtins import int
 
class Splitter():
    """com.google.common.base.Splitter"""
 
    @staticmethod
    def __wrap(java_value: __Splitter) -> 'Splitter':
        return Splitter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Splitter):
        """
        Dynamic initializer for Splitter.
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
    def trimResults(self) -> 'Splitter':
        """public com.google.common.base.Splitter com.google.common.base.Splitter.trimResults()"""
        return 'Splitter'.__wrap(super(Splitter, self).trimResults())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def on(separatorPattern: 'Pattern') -> 'Splitter':
        """public static com.google.common.base.Splitter com.google.common.base.Splitter.on(java.util.regex.Pattern)"""
        return Splitter.__wrap(__Splitter.on(separatorPattern))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def on(separatorMatcher: 'CharMatcher') -> 'Splitter':
        """public static com.google.common.base.Splitter com.google.common.base.Splitter.on(com.google.common.base.CharMatcher)"""
        return Splitter.__wrap(__Splitter.on(separatorMatcher))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def limit(self, maxItems: int) -> 'Splitter':
        """public com.google.common.base.Splitter com.google.common.base.Splitter.limit(int)"""
        return 'Splitter'.__wrap(super(__Splitter, self).limit(__int.valueOf(maxItems)))

    @staticmethod
    @overload
    def on(separator: str) -> 'Splitter':
        """public static com.google.common.base.Splitter com.google.common.base.Splitter.on(char)"""
        return Splitter.__wrap(__Splitter.on(__char.valueOf(separator)))

    @staticmethod
    @overload
    def on(separator: str) -> 'Splitter':
        """public static com.google.common.base.Splitter com.google.common.base.Splitter.on(java.lang.String)"""
        return Splitter.__wrap(__Splitter.on(separator))

    @overload
    def omitEmptyStrings(self) -> 'Splitter':
        """public com.google.common.base.Splitter com.google.common.base.Splitter.omitEmptyStrings()"""
        return 'Splitter'.__wrap(super(Splitter, self).omitEmptyStrings())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def withKeyValueSeparator(self, keyValueSplitter: 'Splitter') -> 'MapSplitter':
        """public com.google.common.base.Splitter$MapSplitter com.google.common.base.Splitter.withKeyValueSeparator(com.google.common.base.Splitter)"""
        return 'MapSplitter'.__wrap(super(__Splitter, self).withKeyValueSeparator(keyValueSplitter))

    @staticmethod
    @overload
    def onPattern(separatorPattern: str) -> 'Splitter':
        """public static com.google.common.base.Splitter com.google.common.base.Splitter.onPattern(java.lang.String)"""
        return Splitter.__wrap(__Splitter.onPattern(separatorPattern))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def trimResults(self, trimmer: 'CharMatcher') -> 'Splitter':
        """public com.google.common.base.Splitter com.google.common.base.Splitter.trimResults(com.google.common.base.CharMatcher)"""
        return 'Splitter'.__wrap(super(__Splitter, self).trimResults(trimmer))

    @overload
    def split(self, sequence: 'CharSequence') -> 'Iterable':
        """public java.lang.Iterable<java.lang.String> com.google.common.base.Splitter.split(java.lang.CharSequence)"""
        return 'Iterable'.__wrap(super(__Splitter, self).split(sequence))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def fixedLength(length: int) -> 'Splitter':
        """public static com.google.common.base.Splitter com.google.common.base.Splitter.fixedLength(int)"""
        return Splitter.__wrap(__Splitter.fixedLength(__int.valueOf(length)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def withKeyValueSeparator(self, separator: str) -> 'MapSplitter':
        """public com.google.common.base.Splitter$MapSplitter com.google.common.base.Splitter.withKeyValueSeparator(char)"""
        return 'MapSplitter'.__wrap(super(__Splitter, self).withKeyValueSeparator(__char.valueOf(separator)))

    @overload
    def splitToStream(self, sequence: 'CharSequence') -> 'Stream':
        """public java.util.stream.Stream<java.lang.String> com.google.common.base.Splitter.splitToStream(java.lang.CharSequence)"""
        return 'Stream'.__wrap(super(__Splitter, self).splitToStream(sequence))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def withKeyValueSeparator(self, separator: str) -> 'MapSplitter':
        """public com.google.common.base.Splitter$MapSplitter com.google.common.base.Splitter.withKeyValueSeparator(java.lang.String)"""
        return 'MapSplitter'.__wrap(super(__Splitter, self).withKeyValueSeparator(separator))

    @overload
    def splitToList(self, sequence: 'CharSequence') -> 'List':
        """public java.util.List<java.lang.String> com.google.common.base.Splitter.splitToList(java.lang.CharSequence)"""
        return 'List'.__wrap(super(__Splitter, self).splitToList(sequence)) 
 
 
# CLASS: com.google.common.base.MoreObjects$ToStringHelper
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.google.common.base.MoreObjects as __MoreObjects_ToStringHelper
__ToStringHelper = __MoreObjects_ToStringHelper.ToStringHelper
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
from builtins import int
 
class ToStringHelper():
    """com.google.common.base.MoreObjects.ToStringHelper"""
 
    @staticmethod
    def __wrap(java_value: __ToStringHelper) -> 'ToStringHelper':
        return ToStringHelper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ToStringHelper):
        """
        Dynamic initializer for ToStringHelper.
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
    def add(self, name: str, value: int) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.add(java.lang.String,long)"""
        return 'ToStringHelper'.__wrap(super(__ToStringHelper, self).add(name, __long.valueOf(value)))

    @overload
    def addValue(self, value: str) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.addValue(char)"""
        return 'ToStringHelper'.__wrap(super(__ToStringHelper, self).addValue(__char.valueOf(value)))

    @overload
    def addValue(self, value: object) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.addValue(java.lang.Object)"""
        return 'ToStringHelper'.__wrap(super(__ToStringHelper, self).addValue(value))

    @overload
    def add(self, name: str, value: bool) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.add(java.lang.String,boolean)"""
        return 'ToStringHelper'.__wrap(super(__ToStringHelper, self).add(name, __boolean.valueOf(value)))

    @overload
    def addValue(self, value: int) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.addValue(int)"""
        return 'ToStringHelper'.__wrap(super(__ToStringHelper, self).addValue(__int.valueOf(value)))

    @overload
    def addValue(self, value: float) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.addValue(float)"""
        return 'ToStringHelper'.__wrap(super(__ToStringHelper, self).addValue(__float.valueOf(value)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def addValue(self, value: int) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.addValue(long)"""
        return 'ToStringHelper'.__wrap(super(__ToStringHelper, self).addValue(__long.valueOf(value)))

    @overload
    def add(self, name: str, value: str) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.add(java.lang.String,char)"""
        return 'ToStringHelper'.__wrap(super(__ToStringHelper, self).add(name, __char.valueOf(value)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.base.MoreObjects$ToStringHelper.toString()"""
        return str.__wrap(super(ToStringHelper, self).toString())

    @overload
    def add(self, name: str, value: float) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.add(java.lang.String,float)"""
        return 'ToStringHelper'.__wrap(super(__ToStringHelper, self).add(name, __float.valueOf(value)))

    @overload
    def add(self, name: str, value: object) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.add(java.lang.String,java.lang.Object)"""
        return 'ToStringHelper'.__wrap(super(__ToStringHelper, self).add(name, value))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def omitNullValues(self) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.omitNullValues()"""
        return 'ToStringHelper'.__wrap(super(ToStringHelper, self).omitNullValues())

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

    @overload
    def add(self, name: str, value: int) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.add(java.lang.String,int)"""
        return 'ToStringHelper'.__wrap(super(__ToStringHelper, self).add(name, __int.valueOf(value)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def add(self, name: str, value: float) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.add(java.lang.String,double)"""
        return 'ToStringHelper'.__wrap(super(__ToStringHelper, self).add(name, __double.valueOf(value)))

    @overload
    def addValue(self, value: bool) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.addValue(boolean)"""
        return 'ToStringHelper'.__wrap(super(__ToStringHelper, self).addValue(__boolean.valueOf(value)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def addValue(self, value: float) -> 'ToStringHelper':
        """public com.google.common.base.MoreObjects$ToStringHelper com.google.common.base.MoreObjects$ToStringHelper.addValue(double)"""
        return 'ToStringHelper'.__wrap(super(__ToStringHelper, self).addValue(__double.valueOf(value))) 
 
 
# CLASS: com.google.common.base.Splitter$MapSplitter
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
import com.google.common.base.Splitter as __Splitter_MapSplitter
__MapSplitter = __Splitter_MapSplitter.MapSplitter
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class MapSplitter():
    """com.google.common.base.Splitter.MapSplitter"""
 
    @staticmethod
    def __wrap(java_value: __MapSplitter) -> 'MapSplitter':
        return MapSplitter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MapSplitter):
        """
        Dynamic initializer for MapSplitter.
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

    @overload
    def split(self, sequence: 'CharSequence') -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.String> com.google.common.base.Splitter$MapSplitter.split(java.lang.CharSequence)"""
        return 'Map'.__wrap(super(__MapSplitter, self).split(sequence))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.common.base.Strings
import com.google.common.base.Strings as __Strings
__Strings = __Strings
from builtins import str
import java.lang.CharSequence as CharSequence
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
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
from builtins import int
 
class Strings():
    """com.google.common.base.Strings"""
 
    @staticmethod
    def __wrap(java_value: __Strings) -> 'Strings':
        return Strings(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Strings):
        """
        Dynamic initializer for Strings.
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

    @staticmethod
    @overload
    def lenientFormat(template: str, *args: object) -> str:
        """public static java.lang.String com.google.common.base.Strings.lenientFormat(java.lang.String,java.lang.Object...)"""
        return str.__wrap(__Strings.lenientFormat(template, args))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def emptyToNull(string: str) -> str:
        """public static java.lang.String com.google.common.base.Strings.emptyToNull(java.lang.String)"""
        return str.__wrap(__Strings.emptyToNull(string))

    @staticmethod
    @overload
    def nullToEmpty(string: str) -> str:
        """public static java.lang.String com.google.common.base.Strings.nullToEmpty(java.lang.String)"""
        return str.__wrap(__Strings.nullToEmpty(string))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def commonPrefix(a: 'CharSequence', b: 'CharSequence') -> str:
        """public static java.lang.String com.google.common.base.Strings.commonPrefix(java.lang.CharSequence,java.lang.CharSequence)"""
        return str.__wrap(__Strings.commonPrefix(a, b))

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
    def padStart(string: str, minLength: int, padChar: str) -> str:
        """public static java.lang.String com.google.common.base.Strings.padStart(java.lang.String,int,char)"""
        return str.__wrap(__Strings.padStart(string, __int.valueOf(minLength), __char.valueOf(padChar)))

    @staticmethod
    @overload
    def repeat(string: str, count: int) -> str:
        """public static java.lang.String com.google.common.base.Strings.repeat(java.lang.String,int)"""
        return str.__wrap(__Strings.repeat(string, __int.valueOf(count)))

    @staticmethod
    @overload
    def commonSuffix(a: 'CharSequence', b: 'CharSequence') -> str:
        """public static java.lang.String com.google.common.base.Strings.commonSuffix(java.lang.CharSequence,java.lang.CharSequence)"""
        return str.__wrap(__Strings.commonSuffix(a, b))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def isNullOrEmpty(string: str) -> bool:
        """public static boolean com.google.common.base.Strings.isNullOrEmpty(java.lang.String)"""
        return bool.__wrap(__Strings.isNullOrEmpty(string))

    @staticmethod
    @overload
    def padEnd(string: str, minLength: int, padChar: str) -> str:
        """public static java.lang.String com.google.common.base.Strings.padEnd(java.lang.String,int,char)"""
        return str.__wrap(__Strings.padEnd(string, __int.valueOf(minLength), __char.valueOf(padChar)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.base.FinalizableReference
import com.google.common.base.FinalizableReference as __FinalizableReference
__FinalizableReference = __FinalizableReference
from abc import abstractmethod, ABC
 
class FinalizableReference(ABC):
    """com.google.common.base.FinalizableReference"""
 
    @staticmethod
    def __wrap(java_value: __FinalizableReference) -> 'FinalizableReference':
        return FinalizableReference(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FinalizableReference):
        """
        Dynamic initializer for FinalizableReference.
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
    def finalizeReferent(self, ):
        """public abstract void com.google.common.base.FinalizableReference.finalizeReferent()"""
        pass 
 
 
# CLASS: com.google.common.base.Preconditions
from builtins import str
import java.lang.Character as __char
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import com.google.common.base.Preconditions as __Preconditions
__Preconditions = __Preconditions
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
from builtins import int
 
class Preconditions():
    """com.google.common.base.Preconditions"""
 
    @staticmethod
    def __wrap(java_value: __Preconditions) -> 'Preconditions':
        return Preconditions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Preconditions):
        """
        Dynamic initializer for Preconditions.
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
 
    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: object, p2: object, p3: object) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return object.__wrap(__Preconditions.checkNotNull(reference, errorMessageTemplate, p1, p2, p3))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: str, p2: int):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,char,long)"""
        __Preconditions.checkArgument(__boolean.valueOf(expression), errorMessageTemplate, __char.valueOf(p1), __long.valueOf(p2))

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: object) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,java.lang.Object)"""
        return object.__wrap(__Preconditions.checkNotNull(reference, errorMessageTemplate, p1))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: int, p2: object):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,long,java.lang.Object)"""
        __Preconditions.checkState(__boolean.valueOf(expression), errorMessageTemplate, __long.valueOf(p1), p2)

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessage: object) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.Object)"""
        return object.__wrap(__Preconditions.checkNotNull(reference, errorMessage))

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: str, p2: str) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,char,char)"""
        return object.__wrap(__Preconditions.checkNotNull(reference, errorMessageTemplate, __char.valueOf(p1), __char.valueOf(p2)))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: int, p2: object):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,long,java.lang.Object)"""
        __Preconditions.checkArgument(__boolean.valueOf(expression), errorMessageTemplate, __long.valueOf(p1), p2)

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: int, p2: int) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,long,long)"""
        return object.__wrap(__Preconditions.checkNotNull(reference, errorMessageTemplate, __long.valueOf(p1), __long.valueOf(p2)))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: str, p2: int):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,char,int)"""
        __Preconditions.checkArgument(__boolean.valueOf(expression), errorMessageTemplate, __char.valueOf(p1), __int.valueOf(p2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: int, p2: int):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,long,int)"""
        __Preconditions.checkState(__boolean.valueOf(expression), errorMessageTemplate, __long.valueOf(p1), __int.valueOf(p2))

    @staticmethod
    @overload
    def checkPositionIndexes(start: int, end: int, size: int):
        """public static void com.google.common.base.Preconditions.checkPositionIndexes(int,int,int)"""
        __Preconditions.checkPositionIndexes(__int.valueOf(start), __int.valueOf(end), __int.valueOf(size))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: str):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,char)"""
        __Preconditions.checkState(__boolean.valueOf(expression), errorMessageTemplate, __char.valueOf(p1))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: object, p2: object):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,java.lang.Object,java.lang.Object)"""
        __Preconditions.checkState(__boolean.valueOf(expression), errorMessageTemplate, p1, p2)

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: str) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,char)"""
        return object.__wrap(__Preconditions.checkNotNull(reference, errorMessageTemplate, __char.valueOf(p1)))

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: int, p2: str) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,int,char)"""
        return object.__wrap(__Preconditions.checkNotNull(reference, errorMessageTemplate, __int.valueOf(p1), __char.valueOf(p2)))

    @staticmethod
    @overload
    def checkState(expression: bool):
        """public static void com.google.common.base.Preconditions.checkState(boolean)"""
        __Preconditions.checkState(__boolean.valueOf(expression))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: str, p2: int) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,char,int)"""
        return object.__wrap(__Preconditions.checkNotNull(reference, errorMessageTemplate, __char.valueOf(p1), __int.valueOf(p2)))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, *errorMessageArgs: object):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,java.lang.Object...)"""
        __Preconditions.checkArgument(__boolean.valueOf(expression), errorMessageTemplate, errorMessageArgs)

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: int, p2: int):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,long,long)"""
        __Preconditions.checkArgument(__boolean.valueOf(expression), errorMessageTemplate, __long.valueOf(p1), __long.valueOf(p2))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: object, p2: int):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,java.lang.Object,int)"""
        __Preconditions.checkArgument(__boolean.valueOf(expression), errorMessageTemplate, p1, __int.valueOf(p2))

    @staticmethod
    @overload
    def checkArgument(expression: bool):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean)"""
        __Preconditions.checkArgument(__boolean.valueOf(expression))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: int, p2: object) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,long,java.lang.Object)"""
        return object.__wrap(__Preconditions.checkNotNull(reference, errorMessageTemplate, __long.valueOf(p1), p2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: str, p2: str):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,char,char)"""
        __Preconditions.checkArgument(__boolean.valueOf(expression), errorMessageTemplate, __char.valueOf(p1), __char.valueOf(p2))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: str, p2: str):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,char,char)"""
        __Preconditions.checkState(__boolean.valueOf(expression), errorMessageTemplate, __char.valueOf(p1), __char.valueOf(p2))

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: int, p2: int) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,long,int)"""
        return object.__wrap(__Preconditions.checkNotNull(reference, errorMessageTemplate, __long.valueOf(p1), __int.valueOf(p2)))

    @staticmethod
    @overload
    def checkElementIndex(index: int, size: int) -> int:
        """public static int com.google.common.base.Preconditions.checkElementIndex(int,int)"""
        return int.__wrap(__Preconditions.checkElementIndex(__int.valueOf(index), __int.valueOf(size)))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: int):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,int)"""
        __Preconditions.checkArgument(__boolean.valueOf(expression), errorMessageTemplate, __int.valueOf(p1))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: int, p2: int):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,long,int)"""
        __Preconditions.checkArgument(__boolean.valueOf(expression), errorMessageTemplate, __long.valueOf(p1), __int.valueOf(p2))

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: int) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,long)"""
        return object.__wrap(__Preconditions.checkNotNull(reference, errorMessageTemplate, __long.valueOf(p1)))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: str, p2: object):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,char,java.lang.Object)"""
        __Preconditions.checkState(__boolean.valueOf(expression), errorMessageTemplate, __char.valueOf(p1), p2)

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: int, p2: int):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,int,int)"""
        __Preconditions.checkState(__boolean.valueOf(expression), errorMessageTemplate, __int.valueOf(p1), __int.valueOf(p2))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: int, p2: object):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,int,java.lang.Object)"""
        __Preconditions.checkState(__boolean.valueOf(expression), errorMessageTemplate, __int.valueOf(p1), p2)

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: str):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,char)"""
        __Preconditions.checkArgument(__boolean.valueOf(expression), errorMessageTemplate, __char.valueOf(p1))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: object, p2: object, p3: object, p4: object):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        __Preconditions.checkState(__boolean.valueOf(expression), errorMessageTemplate, p1, p2, p3, p4)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: int, p2: str):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,long,char)"""
        __Preconditions.checkState(__boolean.valueOf(expression), errorMessageTemplate, __long.valueOf(p1), __char.valueOf(p2))

    @staticmethod
    @overload
    def checkNotNull(reference: object) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T)"""
        return object.__wrap(__Preconditions.checkNotNull(reference))

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: int, p2: int) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,int,int)"""
        return object.__wrap(__Preconditions.checkNotNull(reference, errorMessageTemplate, __int.valueOf(p1), __int.valueOf(p2)))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: int):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,long)"""
        __Preconditions.checkArgument(__boolean.valueOf(expression), errorMessageTemplate, __long.valueOf(p1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: object, p2: str):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,java.lang.Object,char)"""
        __Preconditions.checkArgument(__boolean.valueOf(expression), errorMessageTemplate, p1, __char.valueOf(p2))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: str, p2: int):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,char,long)"""
        __Preconditions.checkState(__boolean.valueOf(expression), errorMessageTemplate, __char.valueOf(p1), __long.valueOf(p2))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: object, p2: object):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,java.lang.Object,java.lang.Object)"""
        __Preconditions.checkArgument(__boolean.valueOf(expression), errorMessageTemplate, p1, p2)

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: object, p2: int):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,java.lang.Object,long)"""
        __Preconditions.checkState(__boolean.valueOf(expression), errorMessageTemplate, p1, __long.valueOf(p2))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: int, p2: str):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,int,char)"""
        __Preconditions.checkState(__boolean.valueOf(expression), errorMessageTemplate, __int.valueOf(p1), __char.valueOf(p2))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: object, p2: object, p3: object):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        __Preconditions.checkState(__boolean.valueOf(expression), errorMessageTemplate, p1, p2, p3)

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: str, p2: object) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,char,java.lang.Object)"""
        return object.__wrap(__Preconditions.checkNotNull(reference, errorMessageTemplate, __char.valueOf(p1), p2))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: str, p2: object):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,char,java.lang.Object)"""
        __Preconditions.checkArgument(__boolean.valueOf(expression), errorMessageTemplate, __char.valueOf(p1), p2)

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: int, p2: int):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,int,long)"""
        __Preconditions.checkState(__boolean.valueOf(expression), errorMessageTemplate, __int.valueOf(p1), __long.valueOf(p2))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: int, p2: int):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,long,long)"""
        __Preconditions.checkState(__boolean.valueOf(expression), errorMessageTemplate, __long.valueOf(p1), __long.valueOf(p2))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: int, p2: int):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,int,int)"""
        __Preconditions.checkArgument(__boolean.valueOf(expression), errorMessageTemplate, __int.valueOf(p1), __int.valueOf(p2))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, *errorMessageArgs: object):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,java.lang.Object...)"""
        __Preconditions.checkState(__boolean.valueOf(expression), errorMessageTemplate, errorMessageArgs)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def checkPositionIndex(index: int, size: int) -> int:
        """public static int com.google.common.base.Preconditions.checkPositionIndex(int,int)"""
        return int.__wrap(__Preconditions.checkPositionIndex(__int.valueOf(index), __int.valueOf(size)))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: int, p2: object):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,int,java.lang.Object)"""
        __Preconditions.checkArgument(__boolean.valueOf(expression), errorMessageTemplate, __int.valueOf(p1), p2)

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: object, p2: int) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,java.lang.Object,int)"""
        return object.__wrap(__Preconditions.checkNotNull(reference, errorMessageTemplate, p1, __int.valueOf(p2)))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: int, p2: str):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,long,char)"""
        __Preconditions.checkArgument(__boolean.valueOf(expression), errorMessageTemplate, __long.valueOf(p1), __char.valueOf(p2))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: str, p2: int):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,char,int)"""
        __Preconditions.checkState(__boolean.valueOf(expression), errorMessageTemplate, __char.valueOf(p1), __int.valueOf(p2))

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: object, p2: object) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,java.lang.Object,java.lang.Object)"""
        return object.__wrap(__Preconditions.checkNotNull(reference, errorMessageTemplate, p1, p2))

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: int, p2: str) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,long,char)"""
        return object.__wrap(__Preconditions.checkNotNull(reference, errorMessageTemplate, __long.valueOf(p1), __char.valueOf(p2)))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessage: object):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.Object)"""
        __Preconditions.checkState(__boolean.valueOf(expression), errorMessage)

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: object, p2: int) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,java.lang.Object,long)"""
        return object.__wrap(__Preconditions.checkNotNull(reference, errorMessageTemplate, p1, __long.valueOf(p2)))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: object, p2: str):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,java.lang.Object,char)"""
        __Preconditions.checkState(__boolean.valueOf(expression), errorMessageTemplate, p1, __char.valueOf(p2))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: object, p2: object, p3: object):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        __Preconditions.checkArgument(__boolean.valueOf(expression), errorMessageTemplate, p1, p2, p3)

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: str, p2: int) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,char,long)"""
        return object.__wrap(__Preconditions.checkNotNull(reference, errorMessageTemplate, __char.valueOf(p1), __long.valueOf(p2)))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: object, p2: int):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,java.lang.Object,long)"""
        __Preconditions.checkArgument(__boolean.valueOf(expression), errorMessageTemplate, p1, __long.valueOf(p2))

    @staticmethod
    @overload
    def checkPositionIndex(index: int, size: int, desc: str) -> int:
        """public static int com.google.common.base.Preconditions.checkPositionIndex(int,int,java.lang.String)"""
        return int.__wrap(__Preconditions.checkPositionIndex(__int.valueOf(index), __int.valueOf(size), desc))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: object):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,java.lang.Object)"""
        __Preconditions.checkState(__boolean.valueOf(expression), errorMessageTemplate, p1)

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: int) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,int)"""
        return object.__wrap(__Preconditions.checkNotNull(reference, errorMessageTemplate, __int.valueOf(p1)))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: object):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,java.lang.Object)"""
        __Preconditions.checkArgument(__boolean.valueOf(expression), errorMessageTemplate, p1)

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: int, p2: int) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,int,long)"""
        return object.__wrap(__Preconditions.checkNotNull(reference, errorMessageTemplate, __int.valueOf(p1), __long.valueOf(p2)))

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: object, p2: str) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,java.lang.Object,char)"""
        return object.__wrap(__Preconditions.checkNotNull(reference, errorMessageTemplate, p1, __char.valueOf(p2)))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: int, p2: int):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,int,long)"""
        __Preconditions.checkArgument(__boolean.valueOf(expression), errorMessageTemplate, __int.valueOf(p1), __long.valueOf(p2))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: object, p2: object, p3: object, p4: object):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        __Preconditions.checkArgument(__boolean.valueOf(expression), errorMessageTemplate, p1, p2, p3, p4)

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, *errorMessageArgs: object) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,java.lang.Object...)"""
        return object.__wrap(__Preconditions.checkNotNull(reference, errorMessageTemplate, errorMessageArgs))

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

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: int, p2: object) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,int,java.lang.Object)"""
        return object.__wrap(__Preconditions.checkNotNull(reference, errorMessageTemplate, __int.valueOf(p1), p2))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: int):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,long)"""
        __Preconditions.checkState(__boolean.valueOf(expression), errorMessageTemplate, __long.valueOf(p1))

    @staticmethod
    @overload
    def checkNotNull(reference: object, errorMessageTemplate: str, p1: object, p2: object, p3: object, p4: object) -> object:
        """public static <T> T com.google.common.base.Preconditions.checkNotNull(T,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return object.__wrap(__Preconditions.checkNotNull(reference, errorMessageTemplate, p1, p2, p3, p4))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessage: object):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.Object)"""
        __Preconditions.checkArgument(__boolean.valueOf(expression), errorMessage)

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: int):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,int)"""
        __Preconditions.checkState(__boolean.valueOf(expression), errorMessageTemplate, __int.valueOf(p1))

    @staticmethod
    @overload
    def checkArgument(expression: bool, errorMessageTemplate: str, p1: int, p2: str):
        """public static void com.google.common.base.Preconditions.checkArgument(boolean,java.lang.String,int,char)"""
        __Preconditions.checkArgument(__boolean.valueOf(expression), errorMessageTemplate, __int.valueOf(p1), __char.valueOf(p2))

    @staticmethod
    @overload
    def checkElementIndex(index: int, size: int, desc: str) -> int:
        """public static int com.google.common.base.Preconditions.checkElementIndex(int,int,java.lang.String)"""
        return int.__wrap(__Preconditions.checkElementIndex(__int.valueOf(index), __int.valueOf(size), desc))

    @staticmethod
    @overload
    def checkState(expression: bool, errorMessageTemplate: str, p1: object, p2: int):
        """public static void com.google.common.base.Preconditions.checkState(boolean,java.lang.String,java.lang.Object,int)"""
        __Preconditions.checkState(__boolean.valueOf(expression), errorMessageTemplate, p1, __int.valueOf(p2)) 
 
 
# CLASS: com.google.common.base.FinalizableSoftReference
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
from abc import abstractmethod, ABC
import java.lang.ref.Reference as __Reference
__Reference = __Reference
import com.google.common.base.FinalizableSoftReference as __FinalizableSoftReference
__FinalizableSoftReference = __FinalizableSoftReference
import java.lang.Long as __long
import com.google.common.base.FinalizableReference as __FinalizableReference
__FinalizableReference = __FinalizableReference
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.ref.SoftReference as __SoftReference
__SoftReference = __SoftReference
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FinalizableSoftReference(ABC, __SoftReference, SoftReference, __FinalizableReference, FinalizableReference):
    """com.google.common.base.FinalizableSoftReference"""
 
    @staticmethod
    def __wrap(java_value: __FinalizableSoftReference) -> 'FinalizableSoftReference':
        return FinalizableSoftReference(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FinalizableSoftReference):
        """
        Dynamic initializer for FinalizableSoftReference.
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
    def refersTo(self, arg0: object) -> bool:
        """public final boolean java.lang.ref.Reference.refersTo(T)"""
        return bool.__wrap(super(__Reference, self).refersTo(arg0))

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
    def clear(self):
        """public void java.lang.ref.Reference.clear()"""
        super(Reference, self).clear()

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

    @staticmethod
    @overload
    def reachabilityFence(arg0: object):
        """public static void java.lang.ref.Reference.reachabilityFence(java.lang.Object)"""
        __Reference.reachabilityFence(arg0)

    @override
    @overload
    def enqueue(self) -> bool:
        """public boolean java.lang.ref.Reference.enqueue()"""
        return bool.__wrap(super(Reference, self).enqueue())

    @override
    @overload
    def get(self) -> object:
        """public T java.lang.ref.SoftReference.get()"""
        return object.__wrap(super(SoftReference, self).get())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @abstractmethod
    def finalizeReferent(self, ):
        """public abstract void com.google.common.base.FinalizableReference.finalizeReferent()"""
        pass

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
    def isEnqueued(self) -> bool:
        """public boolean java.lang.ref.Reference.isEnqueued()"""
        return bool.__wrap(super(Reference, self).isEnqueued()) 
 
 
# CLASS: com.google.common.base.Joiner
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Appendable as __Appendable
__Appendable = __Appendable
from builtins import type
import java.lang.Iterable as Iterable
from builtins import object
import java.util.Iterator as Iterator
import java.lang.Appendable as Appendable
import com.google.common.base.Joiner as __Joiner
__Joiner = __Joiner
import com.google.common.base.Joiner as __Joiner_MapJoiner
__MapJoiner = __Joiner_MapJoiner.MapJoiner
import java.lang.Long as __long
import java.lang.StringBuilder as __StringBuilder
__StringBuilder = __StringBuilder
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Joiner():
    """com.google.common.base.Joiner"""
 
    @staticmethod
    def __wrap(java_value: __Joiner) -> 'Joiner':
        return Joiner(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Joiner):
        """
        Dynamic initializer for Joiner.
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
    def join(self, first: object, second: object, *rest: object) -> str:
        """public final java.lang.String com.google.common.base.Joiner.join(java.lang.Object,java.lang.Object,java.lang.Object...)"""
        return str.__wrap(super(__Joiner, self).join(first, second, rest))

    @overload
    def appendTo(self, appendable: 'Appendable', first: object, second: object, *rest: object) -> 'Appendable':
        """public final <A extends java.lang.Appendable> A com.google.common.base.Joiner.appendTo(A,java.lang.Object,java.lang.Object,java.lang.Object...) throws java.io.IOException"""
        return 'Appendable'.__wrap(super(__Joiner, self).appendTo(appendable, first, second, rest))

    @overload
    def skipNulls(self) -> 'Joiner':
        """public com.google.common.base.Joiner com.google.common.base.Joiner.skipNulls()"""
        return 'Joiner'.__wrap(super(Joiner, self).skipNulls())

    @overload
    def withKeyValueSeparator(self, keyValueSeparator: str) -> 'MapJoiner':
        """public com.google.common.base.Joiner$MapJoiner com.google.common.base.Joiner.withKeyValueSeparator(java.lang.String)"""
        return 'MapJoiner'.__wrap(super(__Joiner, self).withKeyValueSeparator(keyValueSeparator))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def join(self, parts: 'Object') -> str:
        """public final java.lang.String com.google.common.base.Joiner.join(java.lang.Object[])"""
        return str.__wrap(super(__Joiner, self).join(parts))

    @overload
    def appendTo(self, appendable: 'Appendable', parts: 'Iterable') -> 'Appendable':
        """public <A extends java.lang.Appendable> A com.google.common.base.Joiner.appendTo(A,java.lang.Iterable<?>) throws java.io.IOException"""
        return 'Appendable'.__wrap(super(__Joiner, self).appendTo(appendable, parts))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def useForNull(self, nullText: str) -> 'Joiner':
        """public com.google.common.base.Joiner com.google.common.base.Joiner.useForNull(java.lang.String)"""
        return 'Joiner'.__wrap(super(__Joiner, self).useForNull(nullText))

    @overload
    def withKeyValueSeparator(self, keyValueSeparator: str) -> 'MapJoiner':
        """public com.google.common.base.Joiner$MapJoiner com.google.common.base.Joiner.withKeyValueSeparator(char)"""
        return 'MapJoiner'.__wrap(super(__Joiner, self).withKeyValueSeparator(__char.valueOf(keyValueSeparator)))

    @overload
    def appendTo(self, appendable: 'Appendable', parts: 'Iterator') -> 'Appendable':
        """public <A extends java.lang.Appendable> A com.google.common.base.Joiner.appendTo(A,java.util.Iterator<?>) throws java.io.IOException"""
        return 'Appendable'.__wrap(super(__Joiner, self).appendTo(appendable, parts))

    @overload
    def appendTo(self, builder: 'StringBuilder', first: object, second: object, *rest: object) -> 'StringBuilder':
        """public final java.lang.StringBuilder com.google.common.base.Joiner.appendTo(java.lang.StringBuilder,java.lang.Object,java.lang.Object,java.lang.Object...)"""
        return 'StringBuilder'.__wrap(super(__Joiner, self).appendTo(builder, first, second, rest))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def join(self, parts: 'Iterator') -> str:
        """public final java.lang.String com.google.common.base.Joiner.join(java.util.Iterator<?>)"""
        return str.__wrap(super(__Joiner, self).join(parts))

    @staticmethod
    @overload
    def on(separator: str) -> 'Joiner':
        """public static com.google.common.base.Joiner com.google.common.base.Joiner.on(java.lang.String)"""
        return Joiner.__wrap(__Joiner.on(separator))

    @overload
    def appendTo(self, builder: 'StringBuilder', parts: 'Iterable') -> 'StringBuilder':
        """public final java.lang.StringBuilder com.google.common.base.Joiner.appendTo(java.lang.StringBuilder,java.lang.Iterable<?>)"""
        return 'StringBuilder'.__wrap(super(__Joiner, self).appendTo(builder, parts))

    @staticmethod
    @overload
    def on(separator: str) -> 'Joiner':
        """public static com.google.common.base.Joiner com.google.common.base.Joiner.on(char)"""
        return Joiner.__wrap(__Joiner.on(__char.valueOf(separator)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def join(self, parts: 'Iterable') -> str:
        """public final java.lang.String com.google.common.base.Joiner.join(java.lang.Iterable<?>)"""
        return str.__wrap(super(__Joiner, self).join(parts))

    @overload
    def appendTo(self, appendable: 'Appendable', parts: 'Object') -> 'Appendable':
        """public final <A extends java.lang.Appendable> A com.google.common.base.Joiner.appendTo(A,java.lang.Object[]) throws java.io.IOException"""
        return 'Appendable'.__wrap(super(__Joiner, self).appendTo(appendable, parts))

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
    def appendTo(self, builder: 'StringBuilder', parts: 'Iterator') -> 'StringBuilder':
        """public final java.lang.StringBuilder com.google.common.base.Joiner.appendTo(java.lang.StringBuilder,java.util.Iterator<?>)"""
        return 'StringBuilder'.__wrap(super(__Joiner, self).appendTo(builder, parts))

    @overload
    def appendTo(self, builder: 'StringBuilder', parts: 'Object') -> 'StringBuilder':
        """public final java.lang.StringBuilder com.google.common.base.Joiner.appendTo(java.lang.StringBuilder,java.lang.Object[])"""
        return 'StringBuilder'.__wrap(super(__Joiner, self).appendTo(builder, parts))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.google.common.base.Suppliers
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.time.Duration as Duration
import com.google.common.base.Function as __Function
__Function = __Function
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.google.common.base.Suppliers as __Suppliers
__Suppliers = __Suppliers
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.base.Supplier as __Supplier
__Supplier = __Supplier
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Suppliers():
    """com.google.common.base.Suppliers"""
 
    @staticmethod
    def __wrap(java_value: __Suppliers) -> 'Suppliers':
        return Suppliers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Suppliers):
        """
        Dynamic initializer for Suppliers.
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
    def synchronizedSupplier(delegate: 'Supplier') -> 'Supplier':
        """public static <T> com.google.common.base.Supplier<T> com.google.common.base.Suppliers.synchronizedSupplier(com.google.common.base.Supplier<T>)"""
        return Supplier.__wrap(__Suppliers.synchronizedSupplier(delegate))

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
    def memoizeWithExpiration(delegate: 'Supplier', duration: int, unit: 'TimeUnit') -> 'Supplier':
        """public static <T> com.google.common.base.Supplier<T> com.google.common.base.Suppliers.memoizeWithExpiration(com.google.common.base.Supplier<T>,long,java.util.concurrent.TimeUnit)"""
        return Supplier.__wrap(__Suppliers.memoizeWithExpiration(delegate, __long.valueOf(duration), unit))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def compose(function: 'Function', supplier: 'Supplier') -> 'Supplier':
        """public static <F,T> com.google.common.base.Supplier<T> com.google.common.base.Suppliers.compose(com.google.common.base.Function<? super F, T>,com.google.common.base.Supplier<F>)"""
        return Supplier.__wrap(__Suppliers.compose(function, supplier))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def memoize(delegate: 'Supplier') -> 'Supplier':
        """public static <T> com.google.common.base.Supplier<T> com.google.common.base.Suppliers.memoize(com.google.common.base.Supplier<T>)"""
        return Supplier.__wrap(__Suppliers.memoize(delegate))

    @staticmethod
    @overload
    def ofInstance(instance: object) -> 'Supplier':
        """public static <T> com.google.common.base.Supplier<T> com.google.common.base.Suppliers.ofInstance(T)"""
        return Supplier.__wrap(__Suppliers.ofInstance(instance))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def supplierFunction() -> 'Function':
        """public static <T> com.google.common.base.Function<com.google.common.base.Supplier<T>, T> com.google.common.base.Suppliers.supplierFunction()"""
        return Function.__wrap(__Suppliers.supplierFunction())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def memoizeWithExpiration(delegate: 'Supplier', duration: 'Duration') -> 'Supplier':
        """public static <T> com.google.common.base.Supplier<T> com.google.common.base.Suppliers.memoizeWithExpiration(com.google.common.base.Supplier<T>,java.time.Duration)"""
        return Supplier.__wrap(__Suppliers.memoizeWithExpiration(delegate, duration))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))