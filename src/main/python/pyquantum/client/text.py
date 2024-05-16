from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import java.util.Locale as Locale
from builtins import type
import dev.ultreon.libs.commons.v0.Logger as __Logger
__Logger = __Logger
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.client.text.Language as __Language
__Language = __Language
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
try:
    from pyquantum import registry
except ImportError:
    registry = __import_once__("pyquantum.registry")

try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.Set as Set
import java.util.List as __List
__List = __List
import java.lang.Long as __long
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = __import_once__("pycorelibs.commons.v0")

import java.lang.String as __String
__String = __String
import java.io.Reader as Reader
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import dev.ultreon.quantum.client.text.LanguageManager as __LanguageManager
__LanguageManager = __LanguageManager
import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

import java.lang.Integer as __int
import java.util.Locale as __Locale
__Locale = __Locale
import java.util.List as List
from builtins import int
 
class LanguageManager():
    """dev.ultreon.quantum.client.text.LanguageManager"""
 
    @staticmethod
    def __wrap(java_value: __LanguageManager) -> 'LanguageManager':
        return LanguageManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LanguageManager):
        """
        Dynamic initializer for LanguageManager.
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
 
    # public static final dev.ultreon.quantum.client.text.LanguageManager dev.ultreon.quantum.client.text.LanguageManager.INSTANCE
    INSTANCE: 'LanguageManager' = __wrap(__LanguageManager.INSTANCE)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.client.text.Language> dev.ultreon.quantum.client.text.LanguageManager.REGISTRY
    REGISTRY: 'registry.Registry' = __wrap(__registry.Registry.REGISTRY)


    @overload
    def getLanguageIDs(self) -> 'Set':
        """public java.util.Set<dev.ultreon.quantum.util.Identifier> dev.ultreon.quantum.client.text.LanguageManager.getLanguageIDs()"""
        return 'Set'.__wrap(super(LanguageManager, self).getLanguageIDs())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def load(self, arg0: 'Locale', arg1: 'Identifier', arg2: 'Reader') -> 'Language':
        """public dev.ultreon.quantum.client.text.Language dev.ultreon.quantum.client.text.LanguageManager.load(java.util.Locale,dev.ultreon.quantum.util.Identifier,java.io.Reader)"""
        return 'Language'.__wrap(super(__LanguageManager, self).load(arg0, arg1, arg2))

    @overload
    def getLocale(self, arg0: 'Identifier') -> 'Locale':
        """public java.util.Locale dev.ultreon.quantum.client.text.LanguageManager.getLocale(dev.ultreon.quantum.util.Identifier)"""
        return 'Locale'.__wrap(super(__LanguageManager, self).getLocale(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setLogger(self, arg0: 'Logger'):
        """public void dev.ultreon.quantum.client.text.LanguageManager.setLogger(dev.ultreon.libs.commons.v0.Logger)"""
        super(__LanguageManager, self).setLogger(arg0)

    @staticmethod
    @overload
    def getCurrentLanguage() -> 'Locale':
        """public static java.util.Locale dev.ultreon.quantum.client.text.LanguageManager.getCurrentLanguage()"""
        return Locale.__wrap(__LanguageManager.getCurrentLanguage())

    @overload
    def register(self, arg0: 'Locale', arg1: 'Identifier'):
        """public void dev.ultreon.quantum.client.text.LanguageManager.register(java.util.Locale,dev.ultreon.quantum.util.Identifier)"""
        super(__LanguageManager, self).register(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def load(self, arg0: 'Locale', arg1: 'Identifier', arg2: 'ResourceManager') -> 'Language':
        """public dev.ultreon.quantum.client.text.Language dev.ultreon.quantum.client.text.LanguageManager.load(java.util.Locale,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.resources.ResourceManager)"""
        return 'Language'.__wrap(super(__LanguageManager, self).load(arg0, arg1, arg2))

    @overload
    def getLanguageID(self, arg0: 'Locale') -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.text.LanguageManager.getLanguageID(java.util.Locale)"""
        return 'util.Identifier'.__wrap(super(__LanguageManager, self).getLanguageID(arg0))

    @overload
    def getLogger(self) -> 'v0.Logger':
        """public dev.ultreon.libs.commons.v0.Logger dev.ultreon.quantum.client.text.LanguageManager.getLogger()"""
        return 'v0.Logger'.__wrap(super(LanguageManager, self).getLogger())

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
    def getLocales(self) -> 'Set':
        """public java.util.Set<java.util.Locale> dev.ultreon.quantum.client.text.LanguageManager.getLocales()"""
        return 'Set'.__wrap(super(LanguageManager, self).getLocales())

    @overload
    def getLanguages(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.text.Language> dev.ultreon.quantum.client.text.LanguageManager.getLanguages()"""
        return 'List'.__wrap(super(LanguageManager, self).getLanguages())

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
    def get(self, arg0: 'Locale') -> 'Language':
        """public dev.ultreon.quantum.client.text.Language dev.ultreon.quantum.client.text.LanguageManager.get(java.util.Locale)"""
        return 'Language'.__wrap(super(__LanguageManager, self).get(arg0))

    @staticmethod
    @overload
    def setCurrentLanguage(arg0: 'Locale'):
        """public static void dev.ultreon.quantum.client.text.LanguageManager.setCurrentLanguage(java.util.Locale)"""
        __LanguageManager.setCurrentLanguage(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.text.LanguageManager
from pyquantum_helper import import_once as __import_once__
import java.util.Locale as Locale
from builtins import type
import dev.ultreon.libs.commons.v0.Logger as __Logger
__Logger = __Logger
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.client.text.Language as __Language
__Language = __Language
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
try:
    from pyquantum import registry
except ImportError:
    registry = __import_once__("pyquantum.registry")

try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.Set as Set
import java.util.List as __List
__List = __List
import java.lang.Long as __long
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = __import_once__("pycorelibs.commons.v0")

import java.lang.String as __String
__String = __String
import java.io.Reader as Reader
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import dev.ultreon.quantum.client.text.LanguageManager as __LanguageManager
__LanguageManager = __LanguageManager
import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

import java.lang.Integer as __int
import java.util.Locale as __Locale
__Locale = __Locale
import java.util.List as List
from builtins import int
 
class LanguageManager():
    """dev.ultreon.quantum.client.text.LanguageManager"""
 
    @staticmethod
    def __wrap(java_value: __LanguageManager) -> 'LanguageManager':
        return LanguageManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LanguageManager):
        """
        Dynamic initializer for LanguageManager.
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
 
    # public static final dev.ultreon.quantum.client.text.LanguageManager dev.ultreon.quantum.client.text.LanguageManager.INSTANCE
    INSTANCE: 'LanguageManager' = __wrap(__LanguageManager.INSTANCE)

    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.client.text.Language> dev.ultreon.quantum.client.text.LanguageManager.REGISTRY
    REGISTRY: 'registry.Registry' = __wrap(__registry.Registry.REGISTRY)


    @overload
    def getLanguageIDs(self) -> 'Set':
        """public java.util.Set<dev.ultreon.quantum.util.Identifier> dev.ultreon.quantum.client.text.LanguageManager.getLanguageIDs()"""
        return 'Set'.__wrap(super(LanguageManager, self).getLanguageIDs())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def load(self, arg0: 'Locale', arg1: 'Identifier', arg2: 'Reader') -> 'Language':
        """public dev.ultreon.quantum.client.text.Language dev.ultreon.quantum.client.text.LanguageManager.load(java.util.Locale,dev.ultreon.quantum.util.Identifier,java.io.Reader)"""
        return 'Language'.__wrap(super(__LanguageManager, self).load(arg0, arg1, arg2))

    @overload
    def getLocale(self, arg0: 'Identifier') -> 'Locale':
        """public java.util.Locale dev.ultreon.quantum.client.text.LanguageManager.getLocale(dev.ultreon.quantum.util.Identifier)"""
        return 'Locale'.__wrap(super(__LanguageManager, self).getLocale(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setLogger(self, arg0: 'Logger'):
        """public void dev.ultreon.quantum.client.text.LanguageManager.setLogger(dev.ultreon.libs.commons.v0.Logger)"""
        super(__LanguageManager, self).setLogger(arg0)

    @staticmethod
    @overload
    def getCurrentLanguage() -> 'Locale':
        """public static java.util.Locale dev.ultreon.quantum.client.text.LanguageManager.getCurrentLanguage()"""
        return Locale.__wrap(__LanguageManager.getCurrentLanguage())

    @overload
    def register(self, arg0: 'Locale', arg1: 'Identifier'):
        """public void dev.ultreon.quantum.client.text.LanguageManager.register(java.util.Locale,dev.ultreon.quantum.util.Identifier)"""
        super(__LanguageManager, self).register(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def load(self, arg0: 'Locale', arg1: 'Identifier', arg2: 'ResourceManager') -> 'Language':
        """public dev.ultreon.quantum.client.text.Language dev.ultreon.quantum.client.text.LanguageManager.load(java.util.Locale,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.resources.ResourceManager)"""
        return 'Language'.__wrap(super(__LanguageManager, self).load(arg0, arg1, arg2))

    @overload
    def getLanguageID(self, arg0: 'Locale') -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.text.LanguageManager.getLanguageID(java.util.Locale)"""
        return 'util.Identifier'.__wrap(super(__LanguageManager, self).getLanguageID(arg0))

    @overload
    def getLogger(self) -> 'v0.Logger':
        """public dev.ultreon.libs.commons.v0.Logger dev.ultreon.quantum.client.text.LanguageManager.getLogger()"""
        return 'v0.Logger'.__wrap(super(LanguageManager, self).getLogger())

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
    def getLocales(self) -> 'Set':
        """public java.util.Set<java.util.Locale> dev.ultreon.quantum.client.text.LanguageManager.getLocales()"""
        return 'Set'.__wrap(super(LanguageManager, self).getLocales())

    @overload
    def getLanguages(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.text.Language> dev.ultreon.quantum.client.text.LanguageManager.getLanguages()"""
        return 'List'.__wrap(super(LanguageManager, self).getLanguages())

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
    def get(self, arg0: 'Locale') -> 'Language':
        """public dev.ultreon.quantum.client.text.Language dev.ultreon.quantum.client.text.LanguageManager.get(java.util.Locale)"""
        return 'Language'.__wrap(super(__LanguageManager, self).get(arg0))

    @staticmethod
    @overload
    def setCurrentLanguage(arg0: 'Locale'):
        """public static void dev.ultreon.quantum.client.text.LanguageManager.setCurrentLanguage(java.util.Locale)"""
        __LanguageManager.setCurrentLanguage(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.text.LanguageManager 
 
 
# CLASS: dev.ultreon.quantum.client.text.WordGenerator
import dev.ultreon.quantum.client.text.WordGenerator as __WordGenerator
__WordGenerator = __WordGenerator
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
 
class WordGenerator():
    """dev.ultreon.quantum.client.text.WordGenerator"""
 
    @staticmethod
    def __wrap(java_value: __WordGenerator) -> 'WordGenerator':
        return WordGenerator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WordGenerator):
        """
        Dynamic initializer for WordGenerator.
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
    def __init__(self, arg0: 'Config'):
        """public dev.ultreon.quantum.client.text.WordGenerator(dev.ultreon.quantum.client.text.WordGenerator$Config)"""
        val = __WordGenerator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def generate(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.text.WordGenerator.generate()"""
        return str.__wrap(super(WordGenerator, self).generate())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.text.LanguageData
import java.util.ListIterator as __ListIterator
__ListIterator = __ListIterator
import java.util.function.Predicate as Predicate
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import java.util.AbstractCollection as __AbstractCollection
__AbstractCollection = __AbstractCollection
import java.util.ArrayList as __ArrayList
__ArrayList = __ArrayList
import dev.ultreon.quantum.client.text.LanguageData as __LanguageData
__LanguageData = __LanguageData
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.util.ListIterator as ListIterator
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.util.List as List
 
class LanguageData(__ArrayList, ArrayList):
    """dev.ultreon.quantum.client.text.LanguageData"""
 
    @staticmethod
    def __wrap(java_value: __LanguageData) -> 'LanguageData':
        return LanguageData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LanguageData):
        """
        Dynamic initializer for LanguageData.
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
    def remove(self, arg0: int) -> object:
        """public E java.util.ArrayList.remove(int)"""
        return object.__wrap(super(__ArrayList, self).remove(__int.valueOf(arg0)))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.ArrayList.isEmpty()"""
        return bool.__wrap(super(ArrayList, self).isEmpty())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.util.AbstractCollection.toString()"""
        return str.__wrap(super(AbstractCollection, self).toString())

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> java.util.ArrayList.subList(int,int)"""
        return 'List'.__wrap(super(__ArrayList, self).subList(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> java.util.ArrayList.iterator()"""
        return 'Iterator'.__wrap(super(ArrayList, self).iterator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.ArrayList.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__ArrayList, self).retainAll(arg0))

    @override
    @overload
    def ensureCapacity(self, arg0: int):
        """public void java.util.ArrayList.ensureCapacity(int)"""
        super(__ArrayList, self).ensureCapacity(__int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.add(E)"""
        return bool.__wrap(super(__ArrayList, self).add(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).containsAll(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public void java.util.ArrayList.sort(java.util.Comparator<? super E>)"""
        super(__ArrayList, self).sort(arg0)

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] java.util.ArrayList.toArray(T[])"""
        return List[object].__wrap(super(__ArrayList, self).toArray(arg0))

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E java.util.ArrayList.set(int,E)"""
        return object.__wrap(super(__ArrayList, self).set(__int.valueOf(arg0), arg1))

    @override
    @overload
    def removeFirst(self) -> object:
        """public E java.util.ArrayList.removeFirst()"""
        return object.__wrap(super(ArrayList, self).removeFirst())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] java.util.ArrayList.toArray()"""
        return List[object].__wrap(super(ArrayList, self).toArray())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean java.util.ArrayList.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__ArrayList, self).removeIf(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<E> java.util.ArrayList.spliterator()"""
        return 'Spliterator'.__wrap(super(ArrayList, self).spliterator())

    @override
    @overload
    def size(self) -> int:
        """public int java.util.ArrayList.size()"""
        return int.__wrap(super(ArrayList, self).size())

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void java.util.ArrayList.add(int,E)"""
        super(__ArrayList, self).add(__int.valueOf(arg0), arg1)

    @override
    @overload
    def clone(self) -> object:
        """public java.lang.Object java.util.ArrayList.clone()"""
        return object.__wrap(super(ArrayList, self).clone())

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int java.util.ArrayList.indexOf(java.lang.Object)"""
        return int.__wrap(super(__ArrayList, self).indexOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> java.util.ArrayList.listIterator(int)"""
        return 'ListIterator'.__wrap(super(__ArrayList, self).listIterator(__int.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.text.LanguageData()"""
        val = __LanguageData()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def get(self, arg0: int) -> object:
        """public E java.util.ArrayList.get(int)"""
        return object.__wrap(super(__ArrayList, self).get(__int.valueOf(arg0)))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.ArrayList.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__ArrayList, self).removeAll(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.ArrayList.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__ArrayList, self).addAll(arg0))

    @override
    @overload
    def addFirst(self, arg0: object):
        """public void java.util.ArrayList.addFirst(E)"""
        super(__ArrayList, self).addFirst(arg0)

    @override
    @overload
    def removeLast(self) -> object:
        """public E java.util.ArrayList.removeLast()"""
        return object.__wrap(super(ArrayList, self).removeLast())

    @override
    @overload
    def getFirst(self) -> object:
        """public E java.util.ArrayList.getFirst()"""
        return object.__wrap(super(ArrayList, self).getFirst())

    @override
    @overload
    def trimToSize(self):
        """public void java.util.ArrayList.trimToSize()"""
        super(ArrayList, self).trimToSize()

    @override
    @overload
    def clear(self):
        """public void java.util.ArrayList.clear()"""
        super(ArrayList, self).clear()

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.ArrayList.hashCode()"""
        return int.__wrap(super(ArrayList, self).hashCode())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.contains(java.lang.Object)"""
        return bool.__wrap(super(__ArrayList, self).contains(arg0))

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean java.util.ArrayList.addAll(int,java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__ArrayList, self).addAll(__int.valueOf(arg0), arg1))

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public void java.util.ArrayList.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(__ArrayList, self).replaceAll(arg0)

    @override
    @overload
    def getLast(self) -> object:
        """public E java.util.ArrayList.getLast()"""
        return object.__wrap(super(ArrayList, self).getLast())

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
    def __init__(self):
        """public dev.ultreon.quantum.client.text.LanguageData()"""
        val = __LanguageData()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.remove(java.lang.Object)"""
        return bool.__wrap(super(__ArrayList, self).remove(arg0))

    @override
    @overload
    def addLast(self, arg0: object):
        """public void java.util.ArrayList.addLast(E)"""
        super(__ArrayList, self).addLast(arg0)

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'.__wrap(super(List, self).reversed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.equals(java.lang.Object)"""
        return bool.__wrap(super(__ArrayList, self).equals(arg0))

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int java.util.ArrayList.lastIndexOf(java.lang.Object)"""
        return int.__wrap(super(__ArrayList, self).lastIndexOf(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void java.util.ArrayList.forEach(java.util.function.Consumer<? super E>)"""
        super(__ArrayList, self).forEach(arg0)

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> java.util.ArrayList.listIterator()"""
        return 'ListIterator'.__wrap(super(ArrayList, self).listIterator()) 
 
 
# CLASS: dev.ultreon.quantum.client.text.Language
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.util.Locale as Locale
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.client.text.Language as __Language
__Language = __Language
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Locale as __Locale
__Locale = __Locale
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class Language():
    """dev.ultreon.quantum.client.text.Language"""
 
    @staticmethod
    def __wrap(java_value: __Language) -> 'Language':
        return Language(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Language):
        """
        Dynamic initializer for Language.
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
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.text.Language.getId()"""
        return 'util.Identifier'.__wrap(super(Language, self).getId())

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
    def getLocale(self) -> 'Locale':
        """public java.util.Locale dev.ultreon.quantum.client.text.Language.getLocale()"""
        return 'Locale'.__wrap(super(Language, self).getLocale())

    @staticmethod
    @overload
    def translate(arg0: str, *arg1: object) -> str:
        """public static java.lang.String dev.ultreon.quantum.client.text.Language.translate(java.lang.String,java.lang.Object...)"""
        return str.__wrap(__Language.translate(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def get(self, arg0: str, *arg1: object) -> str:
        """public java.lang.String dev.ultreon.quantum.client.text.Language.get(java.lang.String,java.lang.Object...)"""
        return str.__wrap(super(__Language, self).get(arg0, arg1))

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

    @overload
    def __init__(self, arg0: 'Locale', arg1: 'Map', arg2: 'Identifier'):
        """public dev.ultreon.quantum.client.text.Language(java.util.Locale,java.util.Map<java.lang.String, java.lang.String>,dev.ultreon.quantum.util.Identifier)"""
        val = __Language(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.text.WordGenerator$Config
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
import dev.ultreon.quantum.client.text.WordGenerator as __WordGenerator_Config
__Config = __WordGenerator_Config.Config
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Config():
    """dev.ultreon.quantum.client.text.WordGenerator.Config"""
 
    @staticmethod
    def __wrap(java_value: __Config) -> 'Config':
        return Config(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Config):
        """
        Dynamic initializer for Config.
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
    def __init__(self):
        """public dev.ultreon.quantum.client.text.WordGenerator$Config()"""
        val = __Config()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.text.WordGenerator$Config()"""
        val = __Config()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def seed(self, arg0: int) -> 'Config':
        """public dev.ultreon.quantum.client.text.WordGenerator$Config dev.ultreon.quantum.client.text.WordGenerator$Config.seed(long)"""
        return 'Config'.__wrap(super(__Config, self).seed(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def maxSize(self, arg0: int) -> 'Config':
        """public dev.ultreon.quantum.client.text.WordGenerator$Config dev.ultreon.quantum.client.text.WordGenerator$Config.maxSize(int)"""
        return 'Config'.__wrap(super(__Config, self).maxSize(__int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def named(self) -> 'Config':
        """public dev.ultreon.quantum.client.text.WordGenerator$Config dev.ultreon.quantum.client.text.WordGenerator$Config.named()"""
        return 'Config'.__wrap(super(Config, self).named())

    @overload
    def minSize(self, arg0: int) -> 'Config':
        """public dev.ultreon.quantum.client.text.WordGenerator$Config dev.ultreon.quantum.client.text.WordGenerator$Config.minSize(int)"""
        return 'Config'.__wrap(super(__Config, self).minSize(__int.valueOf(arg0)))

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
 
 
# CLASS: dev.ultreon.quantum.client.text.Translation
import dev.ultreon.quantum.client.text.Translation as __Translation
__Translation = __Translation
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
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Translation():
    """dev.ultreon.quantum.client.text.Translation"""
 
    @staticmethod
    def __wrap(java_value: __Translation) -> 'Translation':
        return Translation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Translation):
        """
        Dynamic initializer for Translation.
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
    def __init__(self, arg0: str, *arg1: object):
        """public dev.ultreon.quantum.client.text.Translation(java.lang.String,java.lang.Object...)"""
        val = __Translation(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def set(self, arg0: int, arg1: object):
        """public void dev.ultreon.quantum.client.text.Translation.set(int,java.lang.Object)"""
        super(__Translation, self).set(__int.valueOf(arg0), arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.text.Translation.toString()"""
        return str.__wrap(super(Translation, self).toString())

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
    def get(self, arg0: int) -> object:
        """public java.lang.Object dev.ultreon.quantum.client.text.Translation.get(int)"""
        return object.__wrap(super(__Translation, self).get(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.text.UITranslations
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.text.UITranslations as __UITranslations
__UITranslations = __UITranslations
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class UITranslations():
    """dev.ultreon.quantum.client.text.UITranslations"""
 
    @staticmethod
    def __wrap(java_value: __UITranslations) -> 'UITranslations':
        return UITranslations(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UITranslations):
        """
        Dynamic initializer for UITranslations.
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
 
    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.CONFIRM
    CONFIRM: 'text.TranslationText' = __wrap(__text.TranslationText.CONFIRM)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.TOGGLE
    TOGGLE: 'text.TranslationText' = __wrap(__text.TranslationText.TOGGLE)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.DONE
    DONE: 'text.TranslationText' = __wrap(__text.TranslationText.DONE)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.OK
    OK: 'text.TranslationText' = __wrap(__text.TranslationText.OK)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.NO
    NO: 'text.TranslationText' = __wrap(__text.TranslationText.NO)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.TOGGLE_ALL
    TOGGLE_ALL: 'text.TranslationText' = __wrap(__text.TranslationText.TOGGLE_ALL)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.CANCEL
    CANCEL: 'text.TranslationText' = __wrap(__text.TranslationText.CANCEL)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.ENABLE_ALL
    ENABLE_ALL: 'text.TranslationText' = __wrap(__text.TranslationText.ENABLE_ALL)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.ENABLE
    ENABLE: 'text.TranslationText' = __wrap(__text.TranslationText.ENABLE)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.DISABLE_ALL
    DISABLE_ALL: 'text.TranslationText' = __wrap(__text.TranslationText.DISABLE_ALL)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.PROCEED
    PROCEED: 'text.TranslationText' = __wrap(__text.TranslationText.PROCEED)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.BACK
    BACK: 'text.TranslationText' = __wrap(__text.TranslationText.BACK)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.OKAY
    OKAY: 'text.TranslationText' = __wrap(__text.TranslationText.OKAY)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.DENY
    DENY: 'text.TranslationText' = __wrap(__text.TranslationText.DENY)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.YES
    YES: 'text.TranslationText' = __wrap(__text.TranslationText.YES)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.DISABLE
    DISABLE: 'text.TranslationText' = __wrap(__text.TranslationText.DISABLE)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.ACCEPT
    ACCEPT: 'text.TranslationText' = __wrap(__text.TranslationText.ACCEPT)


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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.text.UITranslations()"""
        val = __UITranslations()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
        """public dev.ultreon.quantum.client.text.UITranslations()"""
        val = __UITranslations()
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