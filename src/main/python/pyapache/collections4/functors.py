from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.Closure as __Closure
__Closure = __Closure
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.apache.commons.collections4.functors.ForClosure as __ForClosure
__ForClosure = __ForClosure
from builtins import bool
from builtins import int
 
class ForClosure():
    """org.apache.commons.collections4.functors.ForClosure"""
 
    @staticmethod
    def __wrap(java_value: __ForClosure) -> 'ForClosure':
        return ForClosure(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ForClosure):
        """
        Dynamic initializer for ForClosure.
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
    def getClosure(self) -> 'collections4.Closure':
        """public org.apache.commons.collections4.Closure<? super E> org.apache.commons.collections4.functors.ForClosure.getClosure()"""
        return 'collections4.Closure'.__wrap(super(ForClosure, self).getClosure())

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
    def forClosure(arg0: int, arg1: 'Closure') -> 'collections4.Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.functors.ForClosure.forClosure(int,org.apache.commons.collections4.Closure<? super E>)"""
        return collections4.Closure.__wrap(__ForClosure.forClosure(__int.valueOf(arg0), arg1))

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

    @overload
    def __init__(self, arg0: int, arg1: 'Closure'):
        """public org.apache.commons.collections4.functors.ForClosure(int,org.apache.commons.collections4.Closure<? super E>)"""
        val = __ForClosure(__int.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getCount(self) -> int:
        """public int org.apache.commons.collections4.functors.ForClosure.getCount()"""
        return int.__wrap(super(ForClosure, self).getCount())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def execute(self, arg0: object):
        """public void org.apache.commons.collections4.functors.ForClosure.execute(E)"""
        super(__ForClosure, self).execute(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: org.apache.commons.collections4.functors.ForClosure
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.Closure as __Closure
__Closure = __Closure
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.apache.commons.collections4.functors.ForClosure as __ForClosure
__ForClosure = __ForClosure
from builtins import bool
from builtins import int
 
class ForClosure():
    """org.apache.commons.collections4.functors.ForClosure"""
 
    @staticmethod
    def __wrap(java_value: __ForClosure) -> 'ForClosure':
        return ForClosure(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ForClosure):
        """
        Dynamic initializer for ForClosure.
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
    def getClosure(self) -> 'collections4.Closure':
        """public org.apache.commons.collections4.Closure<? super E> org.apache.commons.collections4.functors.ForClosure.getClosure()"""
        return 'collections4.Closure'.__wrap(super(ForClosure, self).getClosure())

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
    def forClosure(arg0: int, arg1: 'Closure') -> 'collections4.Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.functors.ForClosure.forClosure(int,org.apache.commons.collections4.Closure<? super E>)"""
        return collections4.Closure.__wrap(__ForClosure.forClosure(__int.valueOf(arg0), arg1))

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

    @overload
    def __init__(self, arg0: int, arg1: 'Closure'):
        """public org.apache.commons.collections4.functors.ForClosure(int,org.apache.commons.collections4.Closure<? super E>)"""
        val = __ForClosure(__int.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getCount(self) -> int:
        """public int org.apache.commons.collections4.functors.ForClosure.getCount()"""
        return int.__wrap(super(ForClosure, self).getCount())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def execute(self, arg0: object):
        """public void org.apache.commons.collections4.functors.ForClosure.execute(E)"""
        super(__ForClosure, self).execute(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: org.apache.commons.collections4.functors.ForClosure 
 
 
# CLASS: org.apache.commons.collections4.functors.InstantiateTransformer
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import org.apache.commons.collections4.functors.InstantiateTransformer as __InstantiateTransformer
__InstantiateTransformer = __InstantiateTransformer
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.apache.commons.collections4.Transformer as __Transformer
__Transformer = __Transformer
from builtins import bool
from builtins import int
 
class InstantiateTransformer():
    """org.apache.commons.collections4.functors.InstantiateTransformer"""
 
    @staticmethod
    def __wrap(java_value: __InstantiateTransformer) -> 'InstantiateTransformer':
        return InstantiateTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InstantiateTransformer):
        """
        Dynamic initializer for InstantiateTransformer.
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
    def transform(self, arg0: 'Class') -> object:
        """public T org.apache.commons.collections4.functors.InstantiateTransformer.transform(java.lang.Class<? extends T>)"""
        return object.__wrap(super(__InstantiateTransformer, self).transform(arg0))

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
    def instantiateTransformer(arg0: 'Class', arg1: 'Object') -> 'collections4.Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<java.lang.Class<? extends T>, T> org.apache.commons.collections4.functors.InstantiateTransformer.instantiateTransformer(java.lang.Class<?>[],java.lang.Object[])"""
        return collections4.Transformer.__wrap(__InstantiateTransformer.instantiateTransformer(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def instantiateTransformer() -> 'collections4.Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<java.lang.Class<? extends T>, T> org.apache.commons.collections4.functors.InstantiateTransformer.instantiateTransformer()"""
        return collections4.Transformer.__wrap(__InstantiateTransformer.instantiateTransformer())

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
    def __init__(self, arg0: 'Class', arg1: 'Object'):
        """public org.apache.commons.collections4.functors.InstantiateTransformer(java.lang.Class<?>[],java.lang.Object[])"""
        val = __InstantiateTransformer(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.WhileClosure
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.Closure as __Closure
__Closure = __Closure
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import org.apache.commons.collections4.functors.WhileClosure as __WhileClosure
__WhileClosure = __WhileClosure
from builtins import int
 
class WhileClosure():
    """org.apache.commons.collections4.functors.WhileClosure"""
 
    @staticmethod
    def __wrap(java_value: __WhileClosure) -> 'WhileClosure':
        return WhileClosure(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WhileClosure):
        """
        Dynamic initializer for WhileClosure.
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
    def __init__(self, arg0: 'Predicate', arg1: 'Closure', arg2: bool):
        """public org.apache.commons.collections4.functors.WhileClosure(org.apache.commons.collections4.Predicate<? super E>,org.apache.commons.collections4.Closure<? super E>,boolean)"""
        val = __WhileClosure(arg0, arg1, __boolean.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def whileClosure(arg0: 'Predicate', arg1: 'Closure', arg2: bool) -> 'collections4.Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.functors.WhileClosure.whileClosure(org.apache.commons.collections4.Predicate<? super E>,org.apache.commons.collections4.Closure<? super E>,boolean)"""
        return collections4.Closure.__wrap(__WhileClosure.whileClosure(arg0, arg1, __boolean.valueOf(arg2)))

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
    def isDoLoop(self) -> bool:
        """public boolean org.apache.commons.collections4.functors.WhileClosure.isDoLoop()"""
        return bool.__wrap(super(WhileClosure, self).isDoLoop())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getPredicate(self) -> 'collections4.Predicate':
        """public org.apache.commons.collections4.Predicate<? super E> org.apache.commons.collections4.functors.WhileClosure.getPredicate()"""
        return 'collections4.Predicate'.__wrap(super(WhileClosure, self).getPredicate())

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
    def getClosure(self) -> 'collections4.Closure':
        """public org.apache.commons.collections4.Closure<? super E> org.apache.commons.collections4.functors.WhileClosure.getClosure()"""
        return 'collections4.Closure'.__wrap(super(WhileClosure, self).getClosure())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def execute(self, arg0: object):
        """public void org.apache.commons.collections4.functors.WhileClosure.execute(E)"""
        super(__WhileClosure, self).execute(arg0) 
 
 
# CLASS: org.apache.commons.collections4.functors.ChainedClosure
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.Closure as __Closure
__Closure = __Closure
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Collection as Collection
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.functors.ChainedClosure as __ChainedClosure
__ChainedClosure = __ChainedClosure
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ChainedClosure():
    """org.apache.commons.collections4.functors.ChainedClosure"""
 
    @staticmethod
    def __wrap(java_value: __ChainedClosure) -> 'ChainedClosure':
        return ChainedClosure(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ChainedClosure):
        """
        Dynamic initializer for ChainedClosure.
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
    def chainedClosure(arg0: 'Collection') -> 'collections4.Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.functors.ChainedClosure.chainedClosure(java.util.Collection<? extends org.apache.commons.collections4.Closure<? super E>>)"""
        return collections4.Closure.__wrap(__ChainedClosure.chainedClosure(arg0))

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
    def execute(self, arg0: object):
        """public void org.apache.commons.collections4.functors.ChainedClosure.execute(E)"""
        super(__ChainedClosure, self).execute(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def chainedClosure(*arg0: 'collections4.Closure') -> 'collections4.Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.functors.ChainedClosure.chainedClosure(org.apache.commons.collections4.Closure<? super E>...)"""
        return collections4.Closure.__wrap(__ChainedClosure.chainedClosure(arg0))

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
    def getClosures(self) -> List['collections4.Closure']:
        """public org.apache.commons.collections4.Closure<? super E>[] org.apache.commons.collections4.functors.ChainedClosure.getClosures()"""
        return List['collections4.Closure'].__wrap(super(ChainedClosure, self).getClosures())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, *arg0: 'collections4.Closure'):
        """public org.apache.commons.collections4.functors.ChainedClosure(org.apache.commons.collections4.Closure<? super E>...)"""
        val = __ChainedClosure(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.InvokerTransformer
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import org.apache.commons.collections4.functors.InvokerTransformer as __InvokerTransformer
__InvokerTransformer = __InvokerTransformer
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.apache.commons.collections4.Transformer as __Transformer
__Transformer = __Transformer
from builtins import bool
from builtins import int
 
class InvokerTransformer():
    """org.apache.commons.collections4.functors.InvokerTransformer"""
 
    @staticmethod
    def __wrap(java_value: __InvokerTransformer) -> 'InvokerTransformer':
        return InvokerTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvokerTransformer):
        """
        Dynamic initializer for InvokerTransformer.
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
    def invokerTransformer(arg0: str) -> 'collections4.Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.functors.InvokerTransformer.invokerTransformer(java.lang.String)"""
        return collections4.Transformer.__wrap(__InvokerTransformer.invokerTransformer(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: str, arg1: 'Class', arg2: 'Object'):
        """public org.apache.commons.collections4.functors.InvokerTransformer(java.lang.String,java.lang.Class<?>[],java.lang.Object[])"""
        val = __InvokerTransformer(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def transform(self, arg0: object) -> object:
        """public O org.apache.commons.collections4.functors.InvokerTransformer.transform(java.lang.Object)"""
        return object.__wrap(super(__InvokerTransformer, self).transform(arg0))

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
    def invokerTransformer(arg0: str, arg1: 'Class', arg2: 'Object') -> 'collections4.Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.functors.InvokerTransformer.invokerTransformer(java.lang.String,java.lang.Class<?>[],java.lang.Object[])"""
        return collections4.Transformer.__wrap(__InvokerTransformer.invokerTransformer(arg0, arg1, arg2))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.ComparatorPredicate$Criterion
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
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import org.apache.commons.collections4.functors.ComparatorPredicate as __ComparatorPredicate_Criterion
__Criterion = __ComparatorPredicate_Criterion.Criterion
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Criterion():
    """org.apache.commons.collections4.functors.ComparatorPredicate.Criterion"""
 
    @staticmethod
    def __wrap(java_value: __Criterion) -> 'Criterion':
        return Criterion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Criterion):
        """
        Dynamic initializer for Criterion.
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Criterion':
        """public static org.apache.commons.collections4.functors.ComparatorPredicate$Criterion org.apache.commons.collections4.functors.ComparatorPredicate$Criterion.valueOf(java.lang.String)"""
        return Criterion.__wrap(__Criterion.valueOf(arg0))

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @staticmethod
    @overload
    def values() -> List['Criterion']:
        """public static org.apache.commons.collections4.functors.ComparatorPredicate$Criterion[] org.apache.commons.collections4.functors.ComparatorPredicate$Criterion.values()"""
        return List[Criterion].__wrap(__Criterion.values())

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
 
 
# CLASS: org.apache.commons.collections4.functors.SwitchClosure
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.Closure as __Closure
__Closure = __Closure
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
import org.apache.commons.collections4.functors.SwitchClosure as __SwitchClosure
__SwitchClosure = __SwitchClosure
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

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
 
class SwitchClosure():
    """org.apache.commons.collections4.functors.SwitchClosure"""
 
    @staticmethod
    def __wrap(java_value: __SwitchClosure) -> 'SwitchClosure':
        return SwitchClosure(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SwitchClosure):
        """
        Dynamic initializer for SwitchClosure.
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
    def getClosures(self) -> List['collections4.Closure']:
        """public org.apache.commons.collections4.Closure<? super E>[] org.apache.commons.collections4.functors.SwitchClosure.getClosures()"""
        return List['collections4.Closure'].__wrap(super(SwitchClosure, self).getClosures())

    @overload
    def __init__(self, arg0: 'Predicate', arg1: 'Closure', arg2: 'Closure'):
        """public org.apache.commons.collections4.functors.SwitchClosure(org.apache.commons.collections4.Predicate<? super E>[],org.apache.commons.collections4.Closure<? super E>[],org.apache.commons.collections4.Closure<? super E>)"""
        val = __SwitchClosure(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def switchClosure(arg0: 'Predicate', arg1: 'Closure', arg2: 'Closure') -> 'collections4.Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.functors.SwitchClosure.switchClosure(org.apache.commons.collections4.Predicate<? super E>[],org.apache.commons.collections4.Closure<? super E>[],org.apache.commons.collections4.Closure<? super E>)"""
        return collections4.Closure.__wrap(__SwitchClosure.switchClosure(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def execute(self, arg0: object):
        """public void org.apache.commons.collections4.functors.SwitchClosure.execute(E)"""
        super(__SwitchClosure, self).execute(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super E>[] org.apache.commons.collections4.functors.SwitchClosure.getPredicates()"""
        return List['collections4.Predicate'].__wrap(super(SwitchClosure, self).getPredicates())

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

    @overload
    def getDefaultClosure(self) -> 'collections4.Closure':
        """public org.apache.commons.collections4.Closure<? super E> org.apache.commons.collections4.functors.SwitchClosure.getDefaultClosure()"""
        return 'collections4.Closure'.__wrap(super(SwitchClosure, self).getDefaultClosure())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def switchClosure(arg0: 'Map') -> 'collections4.Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.functors.SwitchClosure.switchClosure(java.util.Map<org.apache.commons.collections4.Predicate<E>, org.apache.commons.collections4.Closure<E>>)"""
        return collections4.Closure.__wrap(__SwitchClosure.switchClosure(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.NonePredicate
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Collection as Collection
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.functors.NonePredicate as __NonePredicate
__NonePredicate = __NonePredicate
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import org.apache.commons.collections4.functors.AbstractQuantifierPredicate as __AbstractQuantifierPredicate
__AbstractQuantifierPredicate = __AbstractQuantifierPredicate
from builtins import int
 
class NonePredicate():
    """org.apache.commons.collections4.functors.NonePredicate"""
 
    @staticmethod
    def __wrap(java_value: __NonePredicate) -> 'NonePredicate':
        return NonePredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NonePredicate):
        """
        Dynamic initializer for NonePredicate.
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
    def nonePredicate(*arg0: 'collections4.Predicate') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.NonePredicate.nonePredicate(org.apache.commons.collections4.Predicate<? super T>...)"""
        return collections4.Predicate.__wrap(__NonePredicate.nonePredicate(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, *arg0: 'collections4.Predicate'):
        """public org.apache.commons.collections4.functors.NonePredicate(org.apache.commons.collections4.Predicate<? super T>...)"""
        val = __NonePredicate(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super T>[] org.apache.commons.collections4.functors.AbstractQuantifierPredicate.getPredicates()"""
        return List['collections4.Predicate'].__wrap(super(AbstractQuantifierPredicate, self).getPredicates())

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

    @staticmethod
    @overload
    def nonePredicate(arg0: 'Collection') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.NonePredicate.nonePredicate(java.util.Collection<? extends org.apache.commons.collections4.Predicate<? super T>>)"""
        return collections4.Predicate.__wrap(__NonePredicate.nonePredicate(arg0))

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
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.NonePredicate.evaluate(T)"""
        return bool.__wrap(super(__NonePredicate, self).evaluate(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.ConstantFactory
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.apache.commons.collections4.Factory as __Factory
__Factory = __Factory
from builtins import type
import org.apache.commons.collections4.functors.ConstantFactory as __ConstantFactory
__ConstantFactory = __ConstantFactory
from builtins import object
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

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
 
class ConstantFactory():
    """org.apache.commons.collections4.functors.ConstantFactory"""
 
    @staticmethod
    def __wrap(java_value: __ConstantFactory) -> 'ConstantFactory':
        return ConstantFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConstantFactory):
        """
        Dynamic initializer for ConstantFactory.
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
    def getConstant(self) -> object:
        """public T org.apache.commons.collections4.functors.ConstantFactory.getConstant()"""
        return object.__wrap(super(ConstantFactory, self).getConstant())

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
    def create(self) -> object:
        """public T org.apache.commons.collections4.functors.ConstantFactory.create()"""
        return object.__wrap(super(ConstantFactory, self).create())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def constantFactory(arg0: object) -> 'collections4.Factory':
        """public static <T> org.apache.commons.collections4.Factory<T> org.apache.commons.collections4.functors.ConstantFactory.constantFactory(T)"""
        return collections4.Factory.__wrap(__ConstantFactory.constantFactory(arg0))

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
    def __init__(self, arg0: object):
        """public org.apache.commons.collections4.functors.ConstantFactory(T)"""
        val = __ConstantFactory(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.EqualPredicate
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.functors.EqualPredicate as __EqualPredicate
__EqualPredicate = __EqualPredicate
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EqualPredicate():
    """org.apache.commons.collections4.functors.EqualPredicate"""
 
    @staticmethod
    def __wrap(java_value: __EqualPredicate) -> 'EqualPredicate':
        return EqualPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EqualPredicate):
        """
        Dynamic initializer for EqualPredicate.
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
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.EqualPredicate.evaluate(T)"""
        return bool.__wrap(super(__EqualPredicate, self).evaluate(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: object):
        """public org.apache.commons.collections4.functors.EqualPredicate(T)"""
        val = __EqualPredicate(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @staticmethod
    @overload
    def equalPredicate(arg0: object) -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.EqualPredicate.equalPredicate(T)"""
        return collections4.Predicate.__wrap(__EqualPredicate.equalPredicate(arg0))

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
    def equalPredicate(arg0: object, arg1: 'Equator') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.EqualPredicate.equalPredicate(T,org.apache.commons.collections4.Equator<T>)"""
        return collections4.Predicate.__wrap(__EqualPredicate.equalPredicate(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: object, arg1: 'Equator'):
        """public org.apache.commons.collections4.functors.EqualPredicate(T,org.apache.commons.collections4.Equator<T>)"""
        val = __EqualPredicate(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getValue(self) -> object:
        """public java.lang.Object org.apache.commons.collections4.functors.EqualPredicate.getValue()"""
        return object.__wrap(super(EqualPredicate, self).getValue()) 
 
 
# CLASS: org.apache.commons.collections4.functors.CatchAndRethrowClosure
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.functors.CatchAndRethrowClosure as __CatchAndRethrowClosure
__CatchAndRethrowClosure = __CatchAndRethrowClosure
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CatchAndRethrowClosure(ABC):
    """org.apache.commons.collections4.functors.CatchAndRethrowClosure"""
 
    @staticmethod
    def __wrap(java_value: __CatchAndRethrowClosure) -> 'CatchAndRethrowClosure':
        return CatchAndRethrowClosure(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CatchAndRethrowClosure):
        """
        Dynamic initializer for CatchAndRethrowClosure.
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
    def execute(self, arg0: object):
        """public void org.apache.commons.collections4.functors.CatchAndRethrowClosure.execute(E)"""
        super(__CatchAndRethrowClosure, self).execute(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.functors.CatchAndRethrowClosure()"""
        val = __CatchAndRethrowClosure()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.functors.CatchAndRethrowClosure()"""
        val = __CatchAndRethrowClosure()
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.TransformedPredicate
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import org.apache.commons.collections4.functors.TransformedPredicate as __TransformedPredicate
__TransformedPredicate = __TransformedPredicate
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import org.apache.commons.collections4.Transformer as __Transformer
__Transformer = __Transformer
from builtins import int
 
class TransformedPredicate():
    """org.apache.commons.collections4.functors.TransformedPredicate"""
 
    @staticmethod
    def __wrap(java_value: __TransformedPredicate) -> 'TransformedPredicate':
        return TransformedPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TransformedPredicate):
        """
        Dynamic initializer for TransformedPredicate.
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
    def __init__(self, arg0: 'Transformer', arg1: 'Predicate'):
        """public org.apache.commons.collections4.functors.TransformedPredicate(org.apache.commons.collections4.Transformer<? super T, ? extends T>,org.apache.commons.collections4.Predicate<? super T>)"""
        val = __TransformedPredicate(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.TransformedPredicate.evaluate(T)"""
        return bool.__wrap(super(__TransformedPredicate, self).evaluate(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getTransformer(self) -> 'collections4.Transformer':
        """public org.apache.commons.collections4.Transformer<? super T, ? extends T> org.apache.commons.collections4.functors.TransformedPredicate.getTransformer()"""
        return 'collections4.Transformer'.__wrap(super(TransformedPredicate, self).getTransformer())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super T>[] org.apache.commons.collections4.functors.TransformedPredicate.getPredicates()"""
        return List['collections4.Predicate'].__wrap(super(TransformedPredicate, self).getPredicates())

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
    def transformedPredicate(arg0: 'Transformer', arg1: 'Predicate') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.TransformedPredicate.transformedPredicate(org.apache.commons.collections4.Transformer<? super T, ? extends T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return collections4.Predicate.__wrap(__TransformedPredicate.transformedPredicate(arg0, arg1))

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
 
 
# CLASS: org.apache.commons.collections4.functors.StringValueTransformer
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.apache.commons.collections4.functors.StringValueTransformer as __StringValueTransformer
__StringValueTransformer = __StringValueTransformer
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.apache.commons.collections4.Transformer as __Transformer
__Transformer = __Transformer
from builtins import bool
from builtins import int
 
class StringValueTransformer():
    """org.apache.commons.collections4.functors.StringValueTransformer"""
 
    @staticmethod
    def __wrap(java_value: __StringValueTransformer) -> 'StringValueTransformer':
        return StringValueTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StringValueTransformer):
        """
        Dynamic initializer for StringValueTransformer.
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
    def transform(self, arg0: object) -> str:
        """public java.lang.String org.apache.commons.collections4.functors.StringValueTransformer.transform(T)"""
        return str.__wrap(super(__StringValueTransformer, self).transform(arg0))

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
    def stringValueTransformer() -> 'collections4.Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, java.lang.String> org.apache.commons.collections4.functors.StringValueTransformer.stringValueTransformer()"""
        return collections4.Transformer.__wrap(__StringValueTransformer.stringValueTransformer()) 
 
 
# CLASS: org.apache.commons.collections4.functors.NullPredicate
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.apache.commons.collections4.functors.NullPredicate as __NullPredicate
__NullPredicate = __NullPredicate
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

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
 
class NullPredicate():
    """org.apache.commons.collections4.functors.NullPredicate"""
 
    @staticmethod
    def __wrap(java_value: __NullPredicate) -> 'NullPredicate':
        return NullPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NullPredicate):
        """
        Dynamic initializer for NullPredicate.
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
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.NullPredicate.evaluate(T)"""
        return bool.__wrap(super(__NullPredicate, self).evaluate(arg0))

    @staticmethod
    @overload
    def nullPredicate() -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.NullPredicate.nullPredicate()"""
        return collections4.Predicate.__wrap(__NullPredicate.nullPredicate())

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
 
 
# CLASS: org.apache.commons.collections4.functors.ExceptionTransformer
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.apache.commons.collections4.functors.ExceptionTransformer as __ExceptionTransformer
__ExceptionTransformer = __ExceptionTransformer
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.apache.commons.collections4.Transformer as __Transformer
__Transformer = __Transformer
from builtins import bool
from builtins import int
 
class ExceptionTransformer():
    """org.apache.commons.collections4.functors.ExceptionTransformer"""
 
    @staticmethod
    def __wrap(java_value: __ExceptionTransformer) -> 'ExceptionTransformer':
        return ExceptionTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ExceptionTransformer):
        """
        Dynamic initializer for ExceptionTransformer.
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
    def transform(self, arg0: object) -> object:
        """public O org.apache.commons.collections4.functors.ExceptionTransformer.transform(I)"""
        return object.__wrap(super(__ExceptionTransformer, self).transform(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def exceptionTransformer() -> 'collections4.Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.functors.ExceptionTransformer.exceptionTransformer()"""
        return collections4.Transformer.__wrap(__ExceptionTransformer.exceptionTransformer())

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
 
 
# CLASS: org.apache.commons.collections4.functors.FalsePredicate
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.functors.FalsePredicate as __FalsePredicate
__FalsePredicate = __FalsePredicate
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

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
 
class FalsePredicate():
    """org.apache.commons.collections4.functors.FalsePredicate"""
 
    @staticmethod
    def __wrap(java_value: __FalsePredicate) -> 'FalsePredicate':
        return FalsePredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FalsePredicate):
        """
        Dynamic initializer for FalsePredicate.
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
    def falsePredicate() -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.FalsePredicate.falsePredicate()"""
        return collections4.Predicate.__wrap(__FalsePredicate.falsePredicate())

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
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.FalsePredicate.evaluate(T)"""
        return bool.__wrap(super(__FalsePredicate, self).evaluate(arg0))

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
 
 
# CLASS: org.apache.commons.collections4.functors.OnePredicate
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Collection as Collection
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.functors.OnePredicate as __OnePredicate
__OnePredicate = __OnePredicate
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import org.apache.commons.collections4.functors.AbstractQuantifierPredicate as __AbstractQuantifierPredicate
__AbstractQuantifierPredicate = __AbstractQuantifierPredicate
from builtins import int
 
class OnePredicate():
    """org.apache.commons.collections4.functors.OnePredicate"""
 
    @staticmethod
    def __wrap(java_value: __OnePredicate) -> 'OnePredicate':
        return OnePredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OnePredicate):
        """
        Dynamic initializer for OnePredicate.
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

    @staticmethod
    @overload
    def onePredicate(arg0: 'Collection') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.OnePredicate.onePredicate(java.util.Collection<? extends org.apache.commons.collections4.Predicate<? super T>>)"""
        return collections4.Predicate.__wrap(__OnePredicate.onePredicate(arg0))

    @override
    @overload
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super T>[] org.apache.commons.collections4.functors.AbstractQuantifierPredicate.getPredicates()"""
        return List['collections4.Predicate'].__wrap(super(AbstractQuantifierPredicate, self).getPredicates())

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
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.OnePredicate.evaluate(T)"""
        return bool.__wrap(super(__OnePredicate, self).evaluate(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def onePredicate(*arg0: 'collections4.Predicate') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.OnePredicate.onePredicate(org.apache.commons.collections4.Predicate<? super T>...)"""
        return collections4.Predicate.__wrap(__OnePredicate.onePredicate(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, *arg0: 'collections4.Predicate'):
        """public org.apache.commons.collections4.functors.OnePredicate(org.apache.commons.collections4.Predicate<? super T>...)"""
        val = __OnePredicate(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.ComparatorPredicate
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
import org.apache.commons.collections4.functors.ComparatorPredicate as __ComparatorPredicate
__ComparatorPredicate = __ComparatorPredicate
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Comparator as Comparator
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
 
class ComparatorPredicate():
    """org.apache.commons.collections4.functors.ComparatorPredicate"""
 
    @staticmethod
    def __wrap(java_value: __ComparatorPredicate) -> 'ComparatorPredicate':
        return ComparatorPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ComparatorPredicate):
        """
        Dynamic initializer for ComparatorPredicate.
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
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.ComparatorPredicate.evaluate(T)"""
        return bool.__wrap(super(__ComparatorPredicate, self).evaluate(arg0))

    @staticmethod
    @overload
    def comparatorPredicate(arg0: object, arg1: 'Comparator', arg2: 'Criterion') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.ComparatorPredicate.comparatorPredicate(T,java.util.Comparator<T>,org.apache.commons.collections4.functors.ComparatorPredicate$Criterion)"""
        return collections4.Predicate.__wrap(__ComparatorPredicate.comparatorPredicate(arg0, arg1, arg2))

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

    @overload
    def __init__(self, arg0: object, arg1: 'Comparator', arg2: 'Criterion'):
        """public org.apache.commons.collections4.functors.ComparatorPredicate(T,java.util.Comparator<T>,org.apache.commons.collections4.functors.ComparatorPredicate$Criterion)"""
        val = __ComparatorPredicate(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def comparatorPredicate(arg0: object, arg1: 'Comparator') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.ComparatorPredicate.comparatorPredicate(T,java.util.Comparator<T>)"""
        return collections4.Predicate.__wrap(__ComparatorPredicate.comparatorPredicate(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.NOPClosure
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.Closure as __Closure
__Closure = __Closure
from builtins import str
import org.apache.commons.collections4.functors.NOPClosure as __NOPClosure
__NOPClosure = __NOPClosure
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

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
 
class NOPClosure():
    """org.apache.commons.collections4.functors.NOPClosure"""
 
    @staticmethod
    def __wrap(java_value: __NOPClosure) -> 'NOPClosure':
        return NOPClosure(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NOPClosure):
        """
        Dynamic initializer for NOPClosure.
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
    def nopClosure() -> 'collections4.Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.functors.NOPClosure.nopClosure()"""
        return collections4.Closure.__wrap(__NOPClosure.nopClosure())

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
    def execute(self, arg0: object):
        """public void org.apache.commons.collections4.functors.NOPClosure.execute(E)"""
        super(__NOPClosure, self).execute(arg0)

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
 
 
# CLASS: org.apache.commons.collections4.functors.NullIsFalsePredicate
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import org.apache.commons.collections4.functors.NullIsFalsePredicate as __NullIsFalsePredicate
__NullIsFalsePredicate = __NullIsFalsePredicate
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NullIsFalsePredicate():
    """org.apache.commons.collections4.functors.NullIsFalsePredicate"""
 
    @staticmethod
    def __wrap(java_value: __NullIsFalsePredicate) -> 'NullIsFalsePredicate':
        return NullIsFalsePredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NullIsFalsePredicate):
        """
        Dynamic initializer for NullIsFalsePredicate.
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
    def __init__(self, arg0: 'Predicate'):
        """public org.apache.commons.collections4.functors.NullIsFalsePredicate(org.apache.commons.collections4.Predicate<? super T>)"""
        val = __NullIsFalsePredicate(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.NullIsFalsePredicate.evaluate(T)"""
        return bool.__wrap(super(__NullIsFalsePredicate, self).evaluate(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def nullIsFalsePredicate(arg0: 'Predicate') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.NullIsFalsePredicate.nullIsFalsePredicate(org.apache.commons.collections4.Predicate<? super T>)"""
        return collections4.Predicate.__wrap(__NullIsFalsePredicate.nullIsFalsePredicate(arg0))

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

    @override
    @overload
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super T>[] org.apache.commons.collections4.functors.NullIsFalsePredicate.getPredicates()"""
        return List['collections4.Predicate'].__wrap(super(NullIsFalsePredicate, self).getPredicates())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.NOPTransformer
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.apache.commons.collections4.functors.NOPTransformer as __NOPTransformer
__NOPTransformer = __NOPTransformer
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.apache.commons.collections4.Transformer as __Transformer
__Transformer = __Transformer
from builtins import bool
from builtins import int
 
class NOPTransformer():
    """org.apache.commons.collections4.functors.NOPTransformer"""
 
    @staticmethod
    def __wrap(java_value: __NOPTransformer) -> 'NOPTransformer':
        return NOPTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NOPTransformer):
        """
        Dynamic initializer for NOPTransformer.
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
    def transform(self, arg0: object) -> object:
        """public T org.apache.commons.collections4.functors.NOPTransformer.transform(T)"""
        return object.__wrap(super(__NOPTransformer, self).transform(arg0))

    @staticmethod
    @overload
    def nopTransformer() -> 'collections4.Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, T> org.apache.commons.collections4.functors.NOPTransformer.nopTransformer()"""
        return collections4.Transformer.__wrap(__NOPTransformer.nopTransformer())

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
 
 
# CLASS: org.apache.commons.collections4.functors.NullIsExceptionPredicate
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import org.apache.commons.collections4.functors.NullIsExceptionPredicate as __NullIsExceptionPredicate
__NullIsExceptionPredicate = __NullIsExceptionPredicate
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NullIsExceptionPredicate():
    """org.apache.commons.collections4.functors.NullIsExceptionPredicate"""
 
    @staticmethod
    def __wrap(java_value: __NullIsExceptionPredicate) -> 'NullIsExceptionPredicate':
        return NullIsExceptionPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NullIsExceptionPredicate):
        """
        Dynamic initializer for NullIsExceptionPredicate.
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
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super T>[] org.apache.commons.collections4.functors.NullIsExceptionPredicate.getPredicates()"""
        return List['collections4.Predicate'].__wrap(super(NullIsExceptionPredicate, self).getPredicates())

    @overload
    def __init__(self, arg0: 'Predicate'):
        """public org.apache.commons.collections4.functors.NullIsExceptionPredicate(org.apache.commons.collections4.Predicate<? super T>)"""
        val = __NullIsExceptionPredicate(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.NullIsExceptionPredicate.evaluate(T)"""
        return bool.__wrap(super(__NullIsExceptionPredicate, self).evaluate(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def nullIsExceptionPredicate(arg0: 'Predicate') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.NullIsExceptionPredicate.nullIsExceptionPredicate(org.apache.commons.collections4.Predicate<? super T>)"""
        return collections4.Predicate.__wrap(__NullIsExceptionPredicate.nullIsExceptionPredicate(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.ChainedTransformer
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Collection as Collection
from builtins import object
import org.apache.commons.collections4.functors.ChainedTransformer as __ChainedTransformer
__ChainedTransformer = __ChainedTransformer
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.apache.commons.collections4.Transformer as __Transformer
__Transformer = __Transformer
from builtins import bool
from builtins import int
 
class ChainedTransformer():
    """org.apache.commons.collections4.functors.ChainedTransformer"""
 
    @staticmethod
    def __wrap(java_value: __ChainedTransformer) -> 'ChainedTransformer':
        return ChainedTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ChainedTransformer):
        """
        Dynamic initializer for ChainedTransformer.
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
    def chainedTransformer(arg0: 'Collection') -> 'collections4.Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, T> org.apache.commons.collections4.functors.ChainedTransformer.chainedTransformer(java.util.Collection<? extends org.apache.commons.collections4.Transformer<? super T, ? extends T>>)"""
        return collections4.Transformer.__wrap(__ChainedTransformer.chainedTransformer(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def transform(self, arg0: object) -> object:
        """public T org.apache.commons.collections4.functors.ChainedTransformer.transform(T)"""
        return object.__wrap(super(__ChainedTransformer, self).transform(arg0))

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
    def getTransformers(self) -> List['collections4.Transformer']:
        """public org.apache.commons.collections4.Transformer<? super T, ? extends T>[] org.apache.commons.collections4.functors.ChainedTransformer.getTransformers()"""
        return List['collections4.Transformer'].__wrap(super(ChainedTransformer, self).getTransformers())

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
    def chainedTransformer(*arg0: 'collections4.Transformer') -> 'collections4.Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, T> org.apache.commons.collections4.functors.ChainedTransformer.chainedTransformer(org.apache.commons.collections4.Transformer<? super T, ? extends T>...)"""
        return collections4.Transformer.__wrap(__ChainedTransformer.chainedTransformer(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, *arg0: 'collections4.Transformer'):
        """public org.apache.commons.collections4.functors.ChainedTransformer(org.apache.commons.collections4.Transformer<? super T, ? extends T>...)"""
        val = __ChainedTransformer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.IfClosure
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.Closure as __Closure
__Closure = __Closure
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.functors.IfClosure as __IfClosure
__IfClosure = __IfClosure
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

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
 
class IfClosure():
    """org.apache.commons.collections4.functors.IfClosure"""
 
    @staticmethod
    def __wrap(java_value: __IfClosure) -> 'IfClosure':
        return IfClosure(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IfClosure):
        """
        Dynamic initializer for IfClosure.
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
    def ifClosure(arg0: 'Predicate', arg1: 'Closure', arg2: 'Closure') -> 'collections4.Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.functors.IfClosure.ifClosure(org.apache.commons.collections4.Predicate<? super E>,org.apache.commons.collections4.Closure<? super E>,org.apache.commons.collections4.Closure<? super E>)"""
        return collections4.Closure.__wrap(__IfClosure.ifClosure(arg0, arg1, arg2))

    @overload
    def __init__(self, arg0: 'Predicate', arg1: 'Closure', arg2: 'Closure'):
        """public org.apache.commons.collections4.functors.IfClosure(org.apache.commons.collections4.Predicate<? super E>,org.apache.commons.collections4.Closure<? super E>,org.apache.commons.collections4.Closure<? super E>)"""
        val = __IfClosure(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def ifClosure(arg0: 'Predicate', arg1: 'Closure') -> 'collections4.Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.functors.IfClosure.ifClosure(org.apache.commons.collections4.Predicate<? super E>,org.apache.commons.collections4.Closure<? super E>)"""
        return collections4.Closure.__wrap(__IfClosure.ifClosure(arg0, arg1))

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

    @overload
    def __init__(self, arg0: 'Predicate', arg1: 'Closure'):
        """public org.apache.commons.collections4.functors.IfClosure(org.apache.commons.collections4.Predicate<? super E>,org.apache.commons.collections4.Closure<? super E>)"""
        val = __IfClosure(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getPredicate(self) -> 'collections4.Predicate':
        """public org.apache.commons.collections4.Predicate<? super E> org.apache.commons.collections4.functors.IfClosure.getPredicate()"""
        return 'collections4.Predicate'.__wrap(super(IfClosure, self).getPredicate())

    @overload
    def getTrueClosure(self) -> 'collections4.Closure':
        """public org.apache.commons.collections4.Closure<? super E> org.apache.commons.collections4.functors.IfClosure.getTrueClosure()"""
        return 'collections4.Closure'.__wrap(super(IfClosure, self).getTrueClosure())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getFalseClosure(self) -> 'collections4.Closure':
        """public org.apache.commons.collections4.Closure<? super E> org.apache.commons.collections4.functors.IfClosure.getFalseClosure()"""
        return 'collections4.Closure'.__wrap(super(IfClosure, self).getFalseClosure())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def execute(self, arg0: object):
        """public void org.apache.commons.collections4.functors.IfClosure.execute(E)"""
        super(__IfClosure, self).execute(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.ClosureTransformer
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.Closure as __Closure
__Closure = __Closure
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.functors.ClosureTransformer as __ClosureTransformer
__ClosureTransformer = __ClosureTransformer
from builtins import object
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.apache.commons.collections4.Transformer as __Transformer
__Transformer = __Transformer
from builtins import bool
from builtins import int
 
class ClosureTransformer():
    """org.apache.commons.collections4.functors.ClosureTransformer"""
 
    @staticmethod
    def __wrap(java_value: __ClosureTransformer) -> 'ClosureTransformer':
        return ClosureTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClosureTransformer):
        """
        Dynamic initializer for ClosureTransformer.
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
    def closureTransformer(arg0: 'Closure') -> 'collections4.Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, T> org.apache.commons.collections4.functors.ClosureTransformer.closureTransformer(org.apache.commons.collections4.Closure<? super T>)"""
        return collections4.Transformer.__wrap(__ClosureTransformer.closureTransformer(arg0))

    @overload
    def transform(self, arg0: object) -> object:
        """public T org.apache.commons.collections4.functors.ClosureTransformer.transform(T)"""
        return object.__wrap(super(__ClosureTransformer, self).transform(arg0))

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

    @overload
    def __init__(self, arg0: 'Closure'):
        """public org.apache.commons.collections4.functors.ClosureTransformer(org.apache.commons.collections4.Closure<? super T>)"""
        val = __ClosureTransformer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def getClosure(self) -> 'collections4.Closure':
        """public org.apache.commons.collections4.Closure<? super T> org.apache.commons.collections4.functors.ClosureTransformer.getClosure()"""
        return 'collections4.Closure'.__wrap(super(ClosureTransformer, self).getClosure())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.DefaultEquator
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
import org.apache.commons.collections4.functors.DefaultEquator as __DefaultEquator
__DefaultEquator = __DefaultEquator
from builtins import int
 
class DefaultEquator():
    """org.apache.commons.collections4.functors.DefaultEquator"""
 
    @staticmethod
    def __wrap(java_value: __DefaultEquator) -> 'DefaultEquator':
        return DefaultEquator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefaultEquator):
        """
        Dynamic initializer for DefaultEquator.
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
    def equate(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.DefaultEquator.equate(T,T)"""
        return bool.__wrap(super(__DefaultEquator, self).equate(arg0, arg1))

    @overload
    def hash(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.functors.DefaultEquator.hash(T)"""
        return int.__wrap(super(__DefaultEquator, self).hash(arg0))

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

    @staticmethod
    @overload
    def defaultEquator() -> 'DefaultEquator':
        """public static <T> org.apache.commons.collections4.functors.DefaultEquator<T> org.apache.commons.collections4.functors.DefaultEquator.defaultEquator()"""
        return DefaultEquator.__wrap(__DefaultEquator.defaultEquator())

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
 
 
# CLASS: org.apache.commons.collections4.functors.ExceptionPredicate
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.functors.ExceptionPredicate as __ExceptionPredicate
__ExceptionPredicate = __ExceptionPredicate
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

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
 
class ExceptionPredicate():
    """org.apache.commons.collections4.functors.ExceptionPredicate"""
 
    @staticmethod
    def __wrap(java_value: __ExceptionPredicate) -> 'ExceptionPredicate':
        return ExceptionPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ExceptionPredicate):
        """
        Dynamic initializer for ExceptionPredicate.
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

    @staticmethod
    @overload
    def exceptionPredicate() -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.ExceptionPredicate.exceptionPredicate()"""
        return collections4.Predicate.__wrap(__ExceptionPredicate.exceptionPredicate())

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
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.ExceptionPredicate.evaluate(T)"""
        return bool.__wrap(super(__ExceptionPredicate, self).evaluate(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.IfTransformer
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.functors.IfTransformer as __IfTransformer
__IfTransformer = __IfTransformer
from builtins import object
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.apache.commons.collections4.Transformer as __Transformer
__Transformer = __Transformer
from builtins import bool
from builtins import int
 
class IfTransformer():
    """org.apache.commons.collections4.functors.IfTransformer"""
 
    @staticmethod
    def __wrap(java_value: __IfTransformer) -> 'IfTransformer':
        return IfTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IfTransformer):
        """
        Dynamic initializer for IfTransformer.
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
    def getFalseTransformer(self) -> 'collections4.Transformer':
        """public org.apache.commons.collections4.Transformer<? super I, ? extends O> org.apache.commons.collections4.functors.IfTransformer.getFalseTransformer()"""
        return 'collections4.Transformer'.__wrap(super(IfTransformer, self).getFalseTransformer())

    @overload
    def getPredicate(self) -> 'collections4.Predicate':
        """public org.apache.commons.collections4.Predicate<? super I> org.apache.commons.collections4.functors.IfTransformer.getPredicate()"""
        return 'collections4.Predicate'.__wrap(super(IfTransformer, self).getPredicate())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def ifTransformer(arg0: 'Predicate', arg1: 'Transformer') -> 'collections4.Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, T> org.apache.commons.collections4.functors.IfTransformer.ifTransformer(org.apache.commons.collections4.Predicate<? super T>,org.apache.commons.collections4.Transformer<? super T, ? extends T>)"""
        return collections4.Transformer.__wrap(__IfTransformer.ifTransformer(arg0, arg1))

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

    @overload
    def getTrueTransformer(self) -> 'collections4.Transformer':
        """public org.apache.commons.collections4.Transformer<? super I, ? extends O> org.apache.commons.collections4.functors.IfTransformer.getTrueTransformer()"""
        return 'collections4.Transformer'.__wrap(super(IfTransformer, self).getTrueTransformer())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def ifTransformer(arg0: 'Predicate', arg1: 'Transformer', arg2: 'Transformer') -> 'collections4.Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.functors.IfTransformer.ifTransformer(org.apache.commons.collections4.Predicate<? super I>,org.apache.commons.collections4.Transformer<? super I, ? extends O>,org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        return collections4.Transformer.__wrap(__IfTransformer.ifTransformer(arg0, arg1, arg2))

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
    def transform(self, arg0: object) -> object:
        """public O org.apache.commons.collections4.functors.IfTransformer.transform(I)"""
        return object.__wrap(super(__IfTransformer, self).transform(arg0))

    @overload
    def __init__(self, arg0: 'Predicate', arg1: 'Transformer', arg2: 'Transformer'):
        """public org.apache.commons.collections4.functors.IfTransformer(org.apache.commons.collections4.Predicate<? super I>,org.apache.commons.collections4.Transformer<? super I, ? extends O>,org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        val = __IfTransformer(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.NullIsTruePredicate
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.functors.NullIsTruePredicate as __NullIsTruePredicate
__NullIsTruePredicate = __NullIsTruePredicate
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NullIsTruePredicate():
    """org.apache.commons.collections4.functors.NullIsTruePredicate"""
 
    @staticmethod
    def __wrap(java_value: __NullIsTruePredicate) -> 'NullIsTruePredicate':
        return NullIsTruePredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NullIsTruePredicate):
        """
        Dynamic initializer for NullIsTruePredicate.
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
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super T>[] org.apache.commons.collections4.functors.NullIsTruePredicate.getPredicates()"""
        return List['collections4.Predicate'].__wrap(super(NullIsTruePredicate, self).getPredicates())

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
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.NullIsTruePredicate.evaluate(T)"""
        return bool.__wrap(super(__NullIsTruePredicate, self).evaluate(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Predicate'):
        """public org.apache.commons.collections4.functors.NullIsTruePredicate(org.apache.commons.collections4.Predicate<? super T>)"""
        val = __NullIsTruePredicate(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def nullIsTruePredicate(arg0: 'Predicate') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.NullIsTruePredicate.nullIsTruePredicate(org.apache.commons.collections4.Predicate<? super T>)"""
        return collections4.Predicate.__wrap(__NullIsTruePredicate.nullIsTruePredicate(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.AbstractQuantifierPredicate
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import org.apache.commons.collections4.functors.AbstractQuantifierPredicate as __AbstractQuantifierPredicate
__AbstractQuantifierPredicate = __AbstractQuantifierPredicate
from builtins import int
 
class AbstractQuantifierPredicate(ABC):
    """org.apache.commons.collections4.functors.AbstractQuantifierPredicate"""
 
    @staticmethod
    def __wrap(java_value: __AbstractQuantifierPredicate) -> 'AbstractQuantifierPredicate':
        return AbstractQuantifierPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractQuantifierPredicate):
        """
        Dynamic initializer for AbstractQuantifierPredicate.
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
    def __init__(self, *arg0: 'collections4.Predicate'):
        """public org.apache.commons.collections4.functors.AbstractQuantifierPredicate(org.apache.commons.collections4.Predicate<? super T>...)"""
        val = __AbstractQuantifierPredicate(arg0)
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

    @abstractmethod
    def evaluate(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Predicate.evaluate(T)"""
        pass

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super T>[] org.apache.commons.collections4.functors.AbstractQuantifierPredicate.getPredicates()"""
        return List['collections4.Predicate'].__wrap(super(AbstractQuantifierPredicate, self).getPredicates())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.TruePredicate
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.apache.commons.collections4.functors.TruePredicate as __TruePredicate
__TruePredicate = __TruePredicate
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

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
 
class TruePredicate():
    """org.apache.commons.collections4.functors.TruePredicate"""
 
    @staticmethod
    def __wrap(java_value: __TruePredicate) -> 'TruePredicate':
        return TruePredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TruePredicate):
        """
        Dynamic initializer for TruePredicate.
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
    def truePredicate() -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.TruePredicate.truePredicate()"""
        return collections4.Predicate.__wrap(__TruePredicate.truePredicate())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.TruePredicate.evaluate(T)"""
        return bool.__wrap(super(__TruePredicate, self).evaluate(arg0))

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
 
 
# CLASS: org.apache.commons.collections4.functors.UniquePredicate
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.functors.UniquePredicate as __UniquePredicate
__UniquePredicate = __UniquePredicate
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

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
 
class UniquePredicate():
    """org.apache.commons.collections4.functors.UniquePredicate"""
 
    @staticmethod
    def __wrap(java_value: __UniquePredicate) -> 'UniquePredicate':
        return UniquePredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UniquePredicate):
        """
        Dynamic initializer for UniquePredicate.
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
    def __init__(self):
        """public org.apache.commons.collections4.functors.UniquePredicate()"""
        val = __UniquePredicate()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.functors.UniquePredicate()"""
        val = __UniquePredicate()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def uniquePredicate() -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.UniquePredicate.uniquePredicate()"""
        return collections4.Predicate.__wrap(__UniquePredicate.uniquePredicate())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.UniquePredicate.evaluate(T)"""
        return bool.__wrap(super(__UniquePredicate, self).evaluate(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.PredicateDecorator
import org.apache.commons.collections4.functors.PredicateDecorator as __PredicateDecorator
__PredicateDecorator = __PredicateDecorator
from abc import abstractmethod, ABC
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
 
class PredicateDecorator(ABC):
    """org.apache.commons.collections4.functors.PredicateDecorator"""
 
    @staticmethod
    def __wrap(java_value: __PredicateDecorator) -> 'PredicateDecorator':
        return PredicateDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PredicateDecorator):
        """
        Dynamic initializer for PredicateDecorator.
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
    def getPredicates(self, ):
        """public abstract org.apache.commons.collections4.Predicate<? super T>[] org.apache.commons.collections4.functors.PredicateDecorator.getPredicates()"""
        pass

    @abstractmethod
    def evaluate(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Predicate.evaluate(T)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.functors.ExceptionFactory
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.apache.commons.collections4.Factory as __Factory
__Factory = __Factory
from builtins import type
from builtins import object
import org.apache.commons.collections4.functors.ExceptionFactory as __ExceptionFactory
__ExceptionFactory = __ExceptionFactory
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

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
 
class ExceptionFactory():
    """org.apache.commons.collections4.functors.ExceptionFactory"""
 
    @staticmethod
    def __wrap(java_value: __ExceptionFactory) -> 'ExceptionFactory':
        return ExceptionFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ExceptionFactory):
        """
        Dynamic initializer for ExceptionFactory.
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
    def create(self) -> object:
        """public T org.apache.commons.collections4.functors.ExceptionFactory.create()"""
        return object.__wrap(super(ExceptionFactory, self).create())

    @staticmethod
    @overload
    def exceptionFactory() -> 'collections4.Factory':
        """public static <T> org.apache.commons.collections4.Factory<T> org.apache.commons.collections4.functors.ExceptionFactory.exceptionFactory()"""
        return collections4.Factory.__wrap(__ExceptionFactory.exceptionFactory())

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
 
 
# CLASS: org.apache.commons.collections4.functors.SwitchTransformer
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.functors.SwitchTransformer as __SwitchTransformer
__SwitchTransformer = __SwitchTransformer
import java.lang.Integer as __int
import org.apache.commons.collections4.Transformer as __Transformer
__Transformer = __Transformer
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class SwitchTransformer():
    """org.apache.commons.collections4.functors.SwitchTransformer"""
 
    @staticmethod
    def __wrap(java_value: __SwitchTransformer) -> 'SwitchTransformer':
        return SwitchTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SwitchTransformer):
        """
        Dynamic initializer for SwitchTransformer.
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
    def switchTransformer(arg0: 'Predicate', arg1: 'Transformer', arg2: 'Transformer') -> 'collections4.Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.functors.SwitchTransformer.switchTransformer(org.apache.commons.collections4.Predicate<? super I>[],org.apache.commons.collections4.Transformer<? super I, ? extends O>[],org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        return collections4.Transformer.__wrap(__SwitchTransformer.switchTransformer(arg0, arg1, arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Predicate', arg1: 'Transformer', arg2: 'Transformer'):
        """public org.apache.commons.collections4.functors.SwitchTransformer(org.apache.commons.collections4.Predicate<? super I>[],org.apache.commons.collections4.Transformer<? super I, ? extends O>[],org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        val = __SwitchTransformer(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def transform(self, arg0: object) -> object:
        """public O org.apache.commons.collections4.functors.SwitchTransformer.transform(I)"""
        return object.__wrap(super(__SwitchTransformer, self).transform(arg0))

    @staticmethod
    @overload
    def switchTransformer(arg0: 'Map') -> 'collections4.Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.functors.SwitchTransformer.switchTransformer(java.util.Map<? extends org.apache.commons.collections4.Predicate<? super I>, ? extends org.apache.commons.collections4.Transformer<? super I, ? extends O>>)"""
        return collections4.Transformer.__wrap(__SwitchTransformer.switchTransformer(arg0))

    @overload
    def getTransformers(self) -> List['collections4.Transformer']:
        """public org.apache.commons.collections4.Transformer<? super I, ? extends O>[] org.apache.commons.collections4.functors.SwitchTransformer.getTransformers()"""
        return List['collections4.Transformer'].__wrap(super(SwitchTransformer, self).getTransformers())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super I>[] org.apache.commons.collections4.functors.SwitchTransformer.getPredicates()"""
        return List['collections4.Predicate'].__wrap(super(SwitchTransformer, self).getPredicates())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getDefaultTransformer(self) -> 'collections4.Transformer':
        """public org.apache.commons.collections4.Transformer<? super I, ? extends O> org.apache.commons.collections4.functors.SwitchTransformer.getDefaultTransformer()"""
        return 'collections4.Transformer'.__wrap(super(SwitchTransformer, self).getDefaultTransformer())

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
 
 
# CLASS: org.apache.commons.collections4.functors.AndPredicate
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.functors.AndPredicate as __AndPredicate
__AndPredicate = __AndPredicate
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

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
 
class AndPredicate():
    """org.apache.commons.collections4.functors.AndPredicate"""
 
    @staticmethod
    def __wrap(java_value: __AndPredicate) -> 'AndPredicate':
        return AndPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AndPredicate):
        """
        Dynamic initializer for AndPredicate.
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
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super T>[] org.apache.commons.collections4.functors.AndPredicate.getPredicates()"""
        return List['collections4.Predicate'].__wrap(super(AndPredicate, self).getPredicates())

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

    @staticmethod
    @overload
    def andPredicate(arg0: 'Predicate', arg1: 'Predicate') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.AndPredicate.andPredicate(org.apache.commons.collections4.Predicate<? super T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return collections4.Predicate.__wrap(__AndPredicate.andPredicate(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Predicate', arg1: 'Predicate'):
        """public org.apache.commons.collections4.functors.AndPredicate(org.apache.commons.collections4.Predicate<? super T>,org.apache.commons.collections4.Predicate<? super T>)"""
        val = __AndPredicate(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.AndPredicate.evaluate(T)"""
        return bool.__wrap(super(__AndPredicate, self).evaluate(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.PrototypeFactory
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.apache.commons.collections4.Factory as __Factory
__Factory = __Factory
from builtins import type
import org.apache.commons.collections4.functors.PrototypeFactory as __PrototypeFactory
__PrototypeFactory = __PrototypeFactory
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

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
 
class PrototypeFactory():
    """org.apache.commons.collections4.functors.PrototypeFactory"""
 
    @staticmethod
    def __wrap(java_value: __PrototypeFactory) -> 'PrototypeFactory':
        return PrototypeFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PrototypeFactory):
        """
        Dynamic initializer for PrototypeFactory.
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
    def prototypeFactory(arg0: object) -> 'collections4.Factory':
        """public static <T> org.apache.commons.collections4.Factory<T> org.apache.commons.collections4.functors.PrototypeFactory.prototypeFactory(T)"""
        return collections4.Factory.__wrap(__PrototypeFactory.prototypeFactory(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.TransformerPredicate
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import org.apache.commons.collections4.functors.TransformerPredicate as __TransformerPredicate
__TransformerPredicate = __TransformerPredicate
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import org.apache.commons.collections4.Transformer as __Transformer
__Transformer = __Transformer
from builtins import int
 
class TransformerPredicate():
    """org.apache.commons.collections4.functors.TransformerPredicate"""
 
    @staticmethod
    def __wrap(java_value: __TransformerPredicate) -> 'TransformerPredicate':
        return TransformerPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TransformerPredicate):
        """
        Dynamic initializer for TransformerPredicate.
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
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.TransformerPredicate.evaluate(T)"""
        return bool.__wrap(super(__TransformerPredicate, self).evaluate(arg0))

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

    @staticmethod
    @overload
    def transformerPredicate(arg0: 'Transformer') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.TransformerPredicate.transformerPredicate(org.apache.commons.collections4.Transformer<? super T, java.lang.Boolean>)"""
        return collections4.Predicate.__wrap(__TransformerPredicate.transformerPredicate(arg0))

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
    def __init__(self, arg0: 'Transformer'):
        """public org.apache.commons.collections4.functors.TransformerPredicate(org.apache.commons.collections4.Transformer<? super T, java.lang.Boolean>)"""
        val = __TransformerPredicate(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getTransformer(self) -> 'collections4.Transformer':
        """public org.apache.commons.collections4.Transformer<? super T, java.lang.Boolean> org.apache.commons.collections4.functors.TransformerPredicate.getTransformer()"""
        return 'collections4.Transformer'.__wrap(super(TransformerPredicate, self).getTransformer())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.MapTransformer
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
from builtins import object
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
import org.apache.commons.collections4.Transformer as __Transformer
__Transformer = __Transformer
from builtins import bool
import org.apache.commons.collections4.functors.MapTransformer as __MapTransformer
__MapTransformer = __MapTransformer
from builtins import int
 
class MapTransformer():
    """org.apache.commons.collections4.functors.MapTransformer"""
 
    @staticmethod
    def __wrap(java_value: __MapTransformer) -> 'MapTransformer':
        return MapTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MapTransformer):
        """
        Dynamic initializer for MapTransformer.
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
    def getMap(self) -> 'Map':
        """public java.util.Map<? super I, ? extends O> org.apache.commons.collections4.functors.MapTransformer.getMap()"""
        return 'Map'.__wrap(super(MapTransformer, self).getMap())

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
    def mapTransformer(arg0: 'Map') -> 'collections4.Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.functors.MapTransformer.mapTransformer(java.util.Map<? super I, ? extends O>)"""
        return collections4.Transformer.__wrap(__MapTransformer.mapTransformer(arg0))

    @overload
    def transform(self, arg0: object) -> object:
        """public O org.apache.commons.collections4.functors.MapTransformer.transform(I)"""
        return object.__wrap(super(__MapTransformer, self).transform(arg0))

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
 
 
# CLASS: org.apache.commons.collections4.functors.PredicateTransformer
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as Boolean
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Boolean as __Boolean
__Boolean = __Boolean
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
import org.apache.commons.collections4.functors.PredicateTransformer as __PredicateTransformer
__PredicateTransformer = __PredicateTransformer
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.apache.commons.collections4.Transformer as __Transformer
__Transformer = __Transformer
from builtins import bool
from builtins import int
 
class PredicateTransformer():
    """org.apache.commons.collections4.functors.PredicateTransformer"""
 
    @staticmethod
    def __wrap(java_value: __PredicateTransformer) -> 'PredicateTransformer':
        return PredicateTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PredicateTransformer):
        """
        Dynamic initializer for PredicateTransformer.
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
    def transform(self, arg0: object) -> 'Boolean':
        """public java.lang.Boolean org.apache.commons.collections4.functors.PredicateTransformer.transform(T)"""
        return 'Boolean'.__wrap(super(__PredicateTransformer, self).transform(arg0))

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
    def __init__(self, arg0: 'Predicate'):
        """public org.apache.commons.collections4.functors.PredicateTransformer(org.apache.commons.collections4.Predicate<? super T>)"""
        val = __PredicateTransformer(arg0)
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

    @overload
    def getPredicate(self) -> 'collections4.Predicate':
        """public org.apache.commons.collections4.Predicate<? super T> org.apache.commons.collections4.functors.PredicateTransformer.getPredicate()"""
        return 'collections4.Predicate'.__wrap(super(PredicateTransformer, self).getPredicate())

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

    @staticmethod
    @overload
    def predicateTransformer(arg0: 'Predicate') -> 'collections4.Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, java.lang.Boolean> org.apache.commons.collections4.functors.PredicateTransformer.predicateTransformer(org.apache.commons.collections4.Predicate<? super T>)"""
        return collections4.Transformer.__wrap(__PredicateTransformer.predicateTransformer(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.InstantiateFactory
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.Factory as __Factory
__Factory = __Factory
from builtins import object
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.functors.InstantiateFactory as __InstantiateFactory
__InstantiateFactory = __InstantiateFactory
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InstantiateFactory():
    """org.apache.commons.collections4.functors.InstantiateFactory"""
 
    @staticmethod
    def __wrap(java_value: __InstantiateFactory) -> 'InstantiateFactory':
        return InstantiateFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InstantiateFactory):
        """
        Dynamic initializer for InstantiateFactory.
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
    def __init__(self, arg0: 'Class', arg1: 'Class', arg2: 'Object'):
        """public org.apache.commons.collections4.functors.InstantiateFactory(java.lang.Class<T>,java.lang.Class<?>[],java.lang.Object[])"""
        val = __InstantiateFactory(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def instantiateFactory(arg0: 'Class', arg1: 'Class', arg2: 'Object') -> 'collections4.Factory':
        """public static <T> org.apache.commons.collections4.Factory<T> org.apache.commons.collections4.functors.InstantiateFactory.instantiateFactory(java.lang.Class<T>,java.lang.Class<?>[],java.lang.Object[])"""
        return collections4.Factory.__wrap(__InstantiateFactory.instantiateFactory(arg0, arg1, arg2))

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
    def create(self) -> object:
        """public T org.apache.commons.collections4.functors.InstantiateFactory.create()"""
        return object.__wrap(super(InstantiateFactory, self).create())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Class'):
        """public org.apache.commons.collections4.functors.InstantiateFactory(java.lang.Class<T>)"""
        val = __InstantiateFactory(arg0)
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.ConstantTransformer
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.functors.ConstantTransformer as __ConstantTransformer
__ConstantTransformer = __ConstantTransformer
import java.lang.Integer as __int
from builtins import bool
import org.apache.commons.collections4.Transformer as __Transformer
__Transformer = __Transformer
from builtins import int
 
class ConstantTransformer():
    """org.apache.commons.collections4.functors.ConstantTransformer"""
 
    @staticmethod
    def __wrap(java_value: __ConstantTransformer) -> 'ConstantTransformer':
        return ConstantTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConstantTransformer):
        """
        Dynamic initializer for ConstantTransformer.
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
    def transform(self, arg0: object) -> object:
        """public O org.apache.commons.collections4.functors.ConstantTransformer.transform(I)"""
        return object.__wrap(super(__ConstantTransformer, self).transform(arg0))

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
    def getConstant(self) -> object:
        """public O org.apache.commons.collections4.functors.ConstantTransformer.getConstant()"""
        return object.__wrap(super(ConstantTransformer, self).getConstant())

    @overload
    def __init__(self, arg0: object):
        """public org.apache.commons.collections4.functors.ConstantTransformer(O)"""
        val = __ConstantTransformer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.functors.ConstantTransformer.hashCode()"""
        return int.__wrap(super(ConstantTransformer, self).hashCode())

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
    def constantTransformer(arg0: object) -> 'collections4.Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.functors.ConstantTransformer.constantTransformer(O)"""
        return collections4.Transformer.__wrap(__ConstantTransformer.constantTransformer(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.ConstantTransformer.equals(java.lang.Object)"""
        return bool.__wrap(super(__ConstantTransformer, self).equals(arg0))

    @staticmethod
    @overload
    def nullTransformer() -> 'collections4.Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.functors.ConstantTransformer.nullTransformer()"""
        return collections4.Transformer.__wrap(__ConstantTransformer.nullTransformer())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.apache.commons.collections4.functors.ExceptionClosure
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.Closure as __Closure
__Closure = __Closure
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import org.apache.commons.collections4.functors.ExceptionClosure as __ExceptionClosure
__ExceptionClosure = __ExceptionClosure
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ExceptionClosure():
    """org.apache.commons.collections4.functors.ExceptionClosure"""
 
    @staticmethod
    def __wrap(java_value: __ExceptionClosure) -> 'ExceptionClosure':
        return ExceptionClosure(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ExceptionClosure):
        """
        Dynamic initializer for ExceptionClosure.
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
    def execute(self, arg0: object):
        """public void org.apache.commons.collections4.functors.ExceptionClosure.execute(E)"""
        super(__ExceptionClosure, self).execute(arg0)

    @staticmethod
    @overload
    def exceptionClosure() -> 'collections4.Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.functors.ExceptionClosure.exceptionClosure()"""
        return collections4.Closure.__wrap(__ExceptionClosure.exceptionClosure())

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
 
 
# CLASS: org.apache.commons.collections4.functors.NotNullPredicate
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
import org.apache.commons.collections4.functors.NotNullPredicate as __NotNullPredicate
__NotNullPredicate = __NotNullPredicate
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

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
 
class NotNullPredicate():
    """org.apache.commons.collections4.functors.NotNullPredicate"""
 
    @staticmethod
    def __wrap(java_value: __NotNullPredicate) -> 'NotNullPredicate':
        return NotNullPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NotNullPredicate):
        """
        Dynamic initializer for NotNullPredicate.
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
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.NotNullPredicate.evaluate(T)"""
        return bool.__wrap(super(__NotNullPredicate, self).evaluate(arg0))

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
    def notNullPredicate() -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.NotNullPredicate.notNullPredicate()"""
        return collections4.Predicate.__wrap(__NotNullPredicate.notNullPredicate())

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
 
 
# CLASS: org.apache.commons.collections4.functors.IdentityPredicate
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.functors.IdentityPredicate as __IdentityPredicate
__IdentityPredicate = __IdentityPredicate
from builtins import object
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

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
 
class IdentityPredicate():
    """org.apache.commons.collections4.functors.IdentityPredicate"""
 
    @staticmethod
    def __wrap(java_value: __IdentityPredicate) -> 'IdentityPredicate':
        return IdentityPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IdentityPredicate):
        """
        Dynamic initializer for IdentityPredicate.
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
    def getValue(self) -> object:
        """public T org.apache.commons.collections4.functors.IdentityPredicate.getValue()"""
        return object.__wrap(super(IdentityPredicate, self).getValue())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def identityPredicate(arg0: object) -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.IdentityPredicate.identityPredicate(T)"""
        return collections4.Predicate.__wrap(__IdentityPredicate.identityPredicate(arg0))

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
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.IdentityPredicate.evaluate(T)"""
        return bool.__wrap(super(__IdentityPredicate, self).evaluate(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: object):
        """public org.apache.commons.collections4.functors.IdentityPredicate(T)"""
        val = __IdentityPredicate(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.OrPredicate
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import org.apache.commons.collections4.functors.OrPredicate as __OrPredicate
__OrPredicate = __OrPredicate
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class OrPredicate():
    """org.apache.commons.collections4.functors.OrPredicate"""
 
    @staticmethod
    def __wrap(java_value: __OrPredicate) -> 'OrPredicate':
        return OrPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OrPredicate):
        """
        Dynamic initializer for OrPredicate.
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
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super T>[] org.apache.commons.collections4.functors.OrPredicate.getPredicates()"""
        return List['collections4.Predicate'].__wrap(super(OrPredicate, self).getPredicates())

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

    @staticmethod
    @overload
    def orPredicate(arg0: 'Predicate', arg1: 'Predicate') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.OrPredicate.orPredicate(org.apache.commons.collections4.Predicate<? super T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return collections4.Predicate.__wrap(__OrPredicate.orPredicate(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Predicate', arg1: 'Predicate'):
        """public org.apache.commons.collections4.functors.OrPredicate(org.apache.commons.collections4.Predicate<? super T>,org.apache.commons.collections4.Predicate<? super T>)"""
        val = __OrPredicate(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.OrPredicate.evaluate(T)"""
        return bool.__wrap(super(__OrPredicate, self).evaluate(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.InstanceofPredicate
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.functors.InstanceofPredicate as __InstanceofPredicate
__InstanceofPredicate = __InstanceofPredicate
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InstanceofPredicate():
    """org.apache.commons.collections4.functors.InstanceofPredicate"""
 
    @staticmethod
    def __wrap(java_value: __InstanceofPredicate) -> 'InstanceofPredicate':
        return InstanceofPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InstanceofPredicate):
        """
        Dynamic initializer for InstanceofPredicate.
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
    def __init__(self, arg0: 'Class'):
        """public org.apache.commons.collections4.functors.InstanceofPredicate(java.lang.Class<?>)"""
        val = __InstanceofPredicate(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getType(self) -> 'type.Class':
        """public java.lang.Class<?> org.apache.commons.collections4.functors.InstanceofPredicate.getType()"""
        return 'type.Class'.__wrap(super(InstanceofPredicate, self).getType())

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

    @overload
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.InstanceofPredicate.evaluate(java.lang.Object)"""
        return bool.__wrap(super(__InstanceofPredicate, self).evaluate(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def instanceOfPredicate(arg0: 'Class') -> 'collections4.Predicate':
        """public static org.apache.commons.collections4.Predicate<java.lang.Object> org.apache.commons.collections4.functors.InstanceofPredicate.instanceOfPredicate(java.lang.Class<?>)"""
        return collections4.Predicate.__wrap(__InstanceofPredicate.instanceOfPredicate(arg0))

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
 
 
# CLASS: org.apache.commons.collections4.functors.NotPredicate
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.apache.commons.collections4.functors.NotPredicate as __NotPredicate
__NotPredicate = __NotPredicate
from builtins import bool
from builtins import int
 
class NotPredicate():
    """org.apache.commons.collections4.functors.NotPredicate"""
 
    @staticmethod
    def __wrap(java_value: __NotPredicate) -> 'NotPredicate':
        return NotPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NotPredicate):
        """
        Dynamic initializer for NotPredicate.
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
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.NotPredicate.evaluate(T)"""
        return bool.__wrap(super(__NotPredicate, self).evaluate(arg0))

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
    def notPredicate(arg0: 'Predicate') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.NotPredicate.notPredicate(org.apache.commons.collections4.Predicate<? super T>)"""
        return collections4.Predicate.__wrap(__NotPredicate.notPredicate(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Predicate'):
        """public org.apache.commons.collections4.functors.NotPredicate(org.apache.commons.collections4.Predicate<? super T>)"""
        val = __NotPredicate(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super T>[] org.apache.commons.collections4.functors.NotPredicate.getPredicates()"""
        return List['collections4.Predicate'].__wrap(super(NotPredicate, self).getPredicates())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.AllPredicate
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Collection as Collection
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.apache.commons.collections4.functors.AllPredicate as __AllPredicate
__AllPredicate = __AllPredicate
from builtins import bool
import org.apache.commons.collections4.functors.AbstractQuantifierPredicate as __AbstractQuantifierPredicate
__AbstractQuantifierPredicate = __AbstractQuantifierPredicate
from builtins import int
 
class AllPredicate():
    """org.apache.commons.collections4.functors.AllPredicate"""
 
    @staticmethod
    def __wrap(java_value: __AllPredicate) -> 'AllPredicate':
        return AllPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AllPredicate):
        """
        Dynamic initializer for AllPredicate.
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
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.AllPredicate.evaluate(T)"""
        return bool.__wrap(super(__AllPredicate, self).evaluate(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, *arg0: 'collections4.Predicate'):
        """public org.apache.commons.collections4.functors.AllPredicate(org.apache.commons.collections4.Predicate<? super T>...)"""
        val = __AllPredicate(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def allPredicate(*arg0: 'collections4.Predicate') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.AllPredicate.allPredicate(org.apache.commons.collections4.Predicate<? super T>...)"""
        return collections4.Predicate.__wrap(__AllPredicate.allPredicate(arg0))

    @override
    @overload
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super T>[] org.apache.commons.collections4.functors.AbstractQuantifierPredicate.getPredicates()"""
        return List['collections4.Predicate'].__wrap(super(AbstractQuantifierPredicate, self).getPredicates())

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
    def allPredicate(arg0: 'Collection') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.AllPredicate.allPredicate(java.util.Collection<? extends org.apache.commons.collections4.Predicate<? super T>>)"""
        return collections4.Predicate.__wrap(__AllPredicate.allPredicate(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.FactoryTransformer
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.functors.FactoryTransformer as __FactoryTransformer
__FactoryTransformer = __FactoryTransformer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.apache.commons.collections4.Factory as __Factory
__Factory = __Factory
from builtins import type
from builtins import object
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.apache.commons.collections4.Transformer as __Transformer
__Transformer = __Transformer
from builtins import bool
from builtins import int
 
class FactoryTransformer():
    """org.apache.commons.collections4.functors.FactoryTransformer"""
 
    @staticmethod
    def __wrap(java_value: __FactoryTransformer) -> 'FactoryTransformer':
        return FactoryTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FactoryTransformer):
        """
        Dynamic initializer for FactoryTransformer.
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
    def getFactory(self) -> 'collections4.Factory':
        """public org.apache.commons.collections4.Factory<? extends O> org.apache.commons.collections4.functors.FactoryTransformer.getFactory()"""
        return 'collections4.Factory'.__wrap(super(FactoryTransformer, self).getFactory())

    @overload
    def __init__(self, arg0: 'Factory'):
        """public org.apache.commons.collections4.functors.FactoryTransformer(org.apache.commons.collections4.Factory<? extends O>)"""
        val = __FactoryTransformer(arg0)
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
    def transform(self, arg0: object) -> object:
        """public O org.apache.commons.collections4.functors.FactoryTransformer.transform(I)"""
        return object.__wrap(super(__FactoryTransformer, self).transform(arg0))

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

    @staticmethod
    @overload
    def factoryTransformer(arg0: 'Factory') -> 'collections4.Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.functors.FactoryTransformer.factoryTransformer(org.apache.commons.collections4.Factory<? extends O>)"""
        return collections4.Transformer.__wrap(__FactoryTransformer.factoryTransformer(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.CloneTransformer
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.functors.CloneTransformer as __CloneTransformer
__CloneTransformer = __CloneTransformer
import java.lang.Object as __object
from builtins import type
from builtins import object
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.apache.commons.collections4.Transformer as __Transformer
__Transformer = __Transformer
from builtins import bool
from builtins import int
 
class CloneTransformer():
    """org.apache.commons.collections4.functors.CloneTransformer"""
 
    @staticmethod
    def __wrap(java_value: __CloneTransformer) -> 'CloneTransformer':
        return CloneTransformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CloneTransformer):
        """
        Dynamic initializer for CloneTransformer.
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
    def transform(self, arg0: object) -> object:
        """public T org.apache.commons.collections4.functors.CloneTransformer.transform(T)"""
        return object.__wrap(super(__CloneTransformer, self).transform(arg0))

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
    def cloneTransformer() -> 'collections4.Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, T> org.apache.commons.collections4.functors.CloneTransformer.cloneTransformer()"""
        return collections4.Transformer.__wrap(__CloneTransformer.cloneTransformer())

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
 
 
# CLASS: org.apache.commons.collections4.functors.AnyPredicate
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.functors.AnyPredicate as __AnyPredicate
__AnyPredicate = __AnyPredicate
import java.util.Collection as Collection
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import org.apache.commons.collections4.functors.AbstractQuantifierPredicate as __AbstractQuantifierPredicate
__AbstractQuantifierPredicate = __AbstractQuantifierPredicate
from builtins import int
 
class AnyPredicate():
    """org.apache.commons.collections4.functors.AnyPredicate"""
 
    @staticmethod
    def __wrap(java_value: __AnyPredicate) -> 'AnyPredicate':
        return AnyPredicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AnyPredicate):
        """
        Dynamic initializer for AnyPredicate.
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
    def evaluate(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.functors.AnyPredicate.evaluate(T)"""
        return bool.__wrap(super(__AnyPredicate, self).evaluate(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def anyPredicate(*arg0: 'collections4.Predicate') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.AnyPredicate.anyPredicate(org.apache.commons.collections4.Predicate<? super T>...)"""
        return collections4.Predicate.__wrap(__AnyPredicate.anyPredicate(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getPredicates(self) -> List['collections4.Predicate']:
        """public org.apache.commons.collections4.Predicate<? super T>[] org.apache.commons.collections4.functors.AbstractQuantifierPredicate.getPredicates()"""
        return List['collections4.Predicate'].__wrap(super(AbstractQuantifierPredicate, self).getPredicates())

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

    @staticmethod
    @overload
    def anyPredicate(arg0: 'Collection') -> 'collections4.Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.functors.AnyPredicate.anyPredicate(java.util.Collection<? extends org.apache.commons.collections4.Predicate<? super T>>)"""
        return collections4.Predicate.__wrap(__AnyPredicate.anyPredicate(arg0))

    @overload
    def __init__(self, *arg0: 'collections4.Predicate'):
        """public org.apache.commons.collections4.functors.AnyPredicate(org.apache.commons.collections4.Predicate<? super T>...)"""
        val = __AnyPredicate(arg0)
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.functors.TransformerClosure
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.Closure as __Closure
__Closure = __Closure
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import org.apache.commons.collections4.functors.TransformerClosure as __TransformerClosure
__TransformerClosure = __TransformerClosure
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.apache.commons.collections4.Transformer as __Transformer
__Transformer = __Transformer
from builtins import bool
from builtins import int
 
class TransformerClosure():
    """org.apache.commons.collections4.functors.TransformerClosure"""
 
    @staticmethod
    def __wrap(java_value: __TransformerClosure) -> 'TransformerClosure':
        return TransformerClosure(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TransformerClosure):
        """
        Dynamic initializer for TransformerClosure.
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
    def execute(self, arg0: object):
        """public void org.apache.commons.collections4.functors.TransformerClosure.execute(E)"""
        super(__TransformerClosure, self).execute(arg0)

    @overload
    def __init__(self, arg0: 'Transformer'):
        """public org.apache.commons.collections4.functors.TransformerClosure(org.apache.commons.collections4.Transformer<? super E, ?>)"""
        val = __TransformerClosure(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def getTransformer(self) -> 'collections4.Transformer':
        """public org.apache.commons.collections4.Transformer<? super E, ?> org.apache.commons.collections4.functors.TransformerClosure.getTransformer()"""
        return 'collections4.Transformer'.__wrap(super(TransformerClosure, self).getTransformer())

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
    def transformerClosure(arg0: 'Transformer') -> 'collections4.Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.functors.TransformerClosure.transformerClosure(org.apache.commons.collections4.Transformer<? super E, ?>)"""
        return collections4.Closure.__wrap(__TransformerClosure.transformerClosure(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))