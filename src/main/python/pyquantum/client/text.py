from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import java.util.Locale as Locale
import dev.ultreon.quantum.client.text.Language as _Language
_Language = _Language
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import dev.ultreon.libs.commons.v0.Logger as _Logger
_Logger = _Logger
import java.util.Set as _Set
_Set = _Set
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
try:
    from pyquantum import registry
except ImportError:
    registry = _import_once("pyquantum.registry")

import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.util.Set as Set
import java.lang.Integer as _int
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = _import_once("pycorelibs.commons.v0")

import java.io.Reader as Reader
import dev.ultreon.quantum.client.text.LanguageManager as _LanguageManager
_LanguageManager = _LanguageManager
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
try:
    from pyquantum import resources
except ImportError:
    resources = _import_once("pyquantum.resources")

import java.lang.Long as _long
import java.util.Locale as _Locale
_Locale = _Locale
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LanguageManager():
    """dev.ultreon.quantum.client.text.LanguageManager"""
 
    @staticmethod
    def _wrap(java_value: _LanguageManager) -> 'LanguageManager':
        return LanguageManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LanguageManager):
        """
        Dynamic initializer for LanguageManager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LanguageManager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LanguageManager__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.client.text.Language> dev.ultreon.quantum.client.text.LanguageManager.REGISTRY
    REGISTRY: 'registry.Registry' = _wrap(_registry.Registry.REGISTRY)


    @overload
    def register(self, arg0: 'Locale', arg1: 'Identifier'):
        """public void dev.ultreon.quantum.client.text.LanguageManager.register(java.util.Locale,dev.ultreon.quantum.util.Identifier)"""
        super(_LanguageManager, self).register(arg0, arg1)

    @overload
    def get(self, arg0: 'Locale') -> 'Language':
        """public dev.ultreon.quantum.client.text.Language dev.ultreon.quantum.client.text.LanguageManager.get(java.util.Locale)"""
        return 'Language'._wrap(super(_LanguageManager, self).get(arg0))

    @staticmethod
    @overload
    def getCurrentLanguage() -> 'Locale':
        """public static java.util.Locale dev.ultreon.quantum.client.text.LanguageManager.getCurrentLanguage()"""
        return Locale._wrap(_LanguageManager.getCurrentLanguage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getLocales(self) -> 'Set':
        """public java.util.Set<java.util.Locale> dev.ultreon.quantum.client.text.LanguageManager.getLocales()"""
        return 'Set'._wrap(super(LanguageManager, self).getLocales())

    @overload
    def getLanguageIDs(self) -> 'Set':
        """public java.util.Set<dev.ultreon.quantum.util.Identifier> dev.ultreon.quantum.client.text.LanguageManager.getLanguageIDs()"""
        return 'Set'._wrap(super(LanguageManager, self).getLanguageIDs())

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
    def getLanguages(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.text.Language> dev.ultreon.quantum.client.text.LanguageManager.getLanguages()"""
        return 'List'._wrap(super(LanguageManager, self).getLanguages())

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
    def getLanguageID(self, arg0: 'Locale') -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.text.LanguageManager.getLanguageID(java.util.Locale)"""
        return 'util.Identifier'._wrap(super(_LanguageManager, self).getLanguageID(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getLocale(self, arg0: 'Identifier') -> 'Locale':
        """public java.util.Locale dev.ultreon.quantum.client.text.LanguageManager.getLocale(dev.ultreon.quantum.util.Identifier)"""
        return 'Locale'._wrap(super(_LanguageManager, self).getLocale(arg0))

    @overload
    def getLogger(self) -> 'v0.Logger':
        """public dev.ultreon.libs.commons.v0.Logger dev.ultreon.quantum.client.text.LanguageManager.getLogger()"""
        return 'v0.Logger'._wrap(super(LanguageManager, self).getLogger())

    @overload
    def load(self, arg0: 'Locale', arg1: 'Identifier', arg2: 'ResourceManager') -> 'Language':
        """public dev.ultreon.quantum.client.text.Language dev.ultreon.quantum.client.text.LanguageManager.load(java.util.Locale,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.resources.ResourceManager)"""
        return 'Language'._wrap(super(_LanguageManager, self).load(arg0, arg1, arg2))

    @overload
    def load(self, arg0: 'Locale', arg1: 'Identifier', arg2: 'Reader') -> 'Language':
        """public dev.ultreon.quantum.client.text.Language dev.ultreon.quantum.client.text.LanguageManager.load(java.util.Locale,dev.ultreon.quantum.util.Identifier,java.io.Reader)"""
        return 'Language'._wrap(super(_LanguageManager, self).load(arg0, arg1, arg2))

    @staticmethod
    @overload
    def setCurrentLanguage(arg0: 'Locale'):
        """public static void dev.ultreon.quantum.client.text.LanguageManager.setCurrentLanguage(java.util.Locale)"""
        _LanguageManager.setCurrentLanguage(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setLogger(self, arg0: 'Logger'):
        """public void dev.ultreon.quantum.client.text.LanguageManager.setLogger(dev.ultreon.libs.commons.v0.Logger)"""
        super(_LanguageManager, self).setLogger(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())


LanguageManager.INSTANCE = LanguageManager._wrap(_INSTANCE.INSTANCE)

 
 
 
# CLASS: dev.ultreon.quantum.client.text.LanguageManager
from pyquantum_helper import import_once as _import_once
import java.util.Locale as Locale
import dev.ultreon.quantum.client.text.Language as _Language
_Language = _Language
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import dev.ultreon.libs.commons.v0.Logger as _Logger
_Logger = _Logger
import java.util.Set as _Set
_Set = _Set
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
try:
    from pyquantum import registry
except ImportError:
    registry = _import_once("pyquantum.registry")

import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.util.Set as Set
import java.lang.Integer as _int
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = _import_once("pycorelibs.commons.v0")

import java.io.Reader as Reader
import dev.ultreon.quantum.client.text.LanguageManager as _LanguageManager
_LanguageManager = _LanguageManager
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
try:
    from pyquantum import resources
except ImportError:
    resources = _import_once("pyquantum.resources")

import java.lang.Long as _long
import java.util.Locale as _Locale
_Locale = _Locale
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LanguageManager():
    """dev.ultreon.quantum.client.text.LanguageManager"""
 
    @staticmethod
    def _wrap(java_value: _LanguageManager) -> 'LanguageManager':
        return LanguageManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LanguageManager):
        """
        Dynamic initializer for LanguageManager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LanguageManager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LanguageManager__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.registry.Registry<dev.ultreon.quantum.client.text.Language> dev.ultreon.quantum.client.text.LanguageManager.REGISTRY
    REGISTRY: 'registry.Registry' = _wrap(_registry.Registry.REGISTRY)


    @overload
    def register(self, arg0: 'Locale', arg1: 'Identifier'):
        """public void dev.ultreon.quantum.client.text.LanguageManager.register(java.util.Locale,dev.ultreon.quantum.util.Identifier)"""
        super(_LanguageManager, self).register(arg0, arg1)

    @overload
    def get(self, arg0: 'Locale') -> 'Language':
        """public dev.ultreon.quantum.client.text.Language dev.ultreon.quantum.client.text.LanguageManager.get(java.util.Locale)"""
        return 'Language'._wrap(super(_LanguageManager, self).get(arg0))

    @staticmethod
    @overload
    def getCurrentLanguage() -> 'Locale':
        """public static java.util.Locale dev.ultreon.quantum.client.text.LanguageManager.getCurrentLanguage()"""
        return Locale._wrap(_LanguageManager.getCurrentLanguage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getLocales(self) -> 'Set':
        """public java.util.Set<java.util.Locale> dev.ultreon.quantum.client.text.LanguageManager.getLocales()"""
        return 'Set'._wrap(super(LanguageManager, self).getLocales())

    @overload
    def getLanguageIDs(self) -> 'Set':
        """public java.util.Set<dev.ultreon.quantum.util.Identifier> dev.ultreon.quantum.client.text.LanguageManager.getLanguageIDs()"""
        return 'Set'._wrap(super(LanguageManager, self).getLanguageIDs())

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
    def getLanguages(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.text.Language> dev.ultreon.quantum.client.text.LanguageManager.getLanguages()"""
        return 'List'._wrap(super(LanguageManager, self).getLanguages())

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
    def getLanguageID(self, arg0: 'Locale') -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.text.LanguageManager.getLanguageID(java.util.Locale)"""
        return 'util.Identifier'._wrap(super(_LanguageManager, self).getLanguageID(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getLocale(self, arg0: 'Identifier') -> 'Locale':
        """public java.util.Locale dev.ultreon.quantum.client.text.LanguageManager.getLocale(dev.ultreon.quantum.util.Identifier)"""
        return 'Locale'._wrap(super(_LanguageManager, self).getLocale(arg0))

    @overload
    def getLogger(self) -> 'v0.Logger':
        """public dev.ultreon.libs.commons.v0.Logger dev.ultreon.quantum.client.text.LanguageManager.getLogger()"""
        return 'v0.Logger'._wrap(super(LanguageManager, self).getLogger())

    @overload
    def load(self, arg0: 'Locale', arg1: 'Identifier', arg2: 'ResourceManager') -> 'Language':
        """public dev.ultreon.quantum.client.text.Language dev.ultreon.quantum.client.text.LanguageManager.load(java.util.Locale,dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.resources.ResourceManager)"""
        return 'Language'._wrap(super(_LanguageManager, self).load(arg0, arg1, arg2))

    @overload
    def load(self, arg0: 'Locale', arg1: 'Identifier', arg2: 'Reader') -> 'Language':
        """public dev.ultreon.quantum.client.text.Language dev.ultreon.quantum.client.text.LanguageManager.load(java.util.Locale,dev.ultreon.quantum.util.Identifier,java.io.Reader)"""
        return 'Language'._wrap(super(_LanguageManager, self).load(arg0, arg1, arg2))

    @staticmethod
    @overload
    def setCurrentLanguage(arg0: 'Locale'):
        """public static void dev.ultreon.quantum.client.text.LanguageManager.setCurrentLanguage(java.util.Locale)"""
        _LanguageManager.setCurrentLanguage(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setLogger(self, arg0: 'Logger'):
        """public void dev.ultreon.quantum.client.text.LanguageManager.setLogger(dev.ultreon.libs.commons.v0.Logger)"""
        super(_LanguageManager, self).setLogger(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())


LanguageManager.INSTANCE = LanguageManager._wrap(_INSTANCE.INSTANCE)

 
 
 
# CLASS: dev.ultreon.quantum.client.text.LanguageManager 
 
 
# CLASS: dev.ultreon.quantum.client.text.WordGenerator
import dev.ultreon.quantum.client.text.WordGenerator as _WordGenerator
_WordGenerator = _WordGenerator
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
 
class WordGenerator():
    """dev.ultreon.quantum.client.text.WordGenerator"""
 
    @staticmethod
    def _wrap(java_value: _WordGenerator) -> 'WordGenerator':
        return WordGenerator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WordGenerator):
        """
        Dynamic initializer for WordGenerator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WordGenerator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WordGenerator__wrapper":
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
    def generate(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.text.WordGenerator.generate()"""
        return str._wrap(super(WordGenerator, self).generate())

    @overload
    def __init__(self, arg0: 'Config'):
        """public dev.ultreon.quantum.client.text.WordGenerator(dev.ultreon.quantum.client.text.WordGenerator$Config)"""
        val = _WordGenerator(arg0)
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.text.LanguageData
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
import java.util.ListIterator as _ListIterator
_ListIterator = _ListIterator
from builtins import type
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import dev.ultreon.quantum.client.text.LanguageData as _LanguageData
_LanguageData = _LanguageData
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.Iterator as Iterator
from typing import List
import java.util.ArrayList as _ArrayList
_ArrayList = _ArrayList
import java.util.Comparator as Comparator
import java.util.ListIterator as ListIterator
import java.util.AbstractCollection as _AbstractCollection
_AbstractCollection = _AbstractCollection
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class LanguageData():
    """dev.ultreon.quantum.client.text.LanguageData"""
 
    @staticmethod
    def _wrap(java_value: _LanguageData) -> 'LanguageData':
        return LanguageData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LanguageData):
        """
        Dynamic initializer for LanguageData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LanguageData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LanguageData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def addLast(self, arg0: object):
        """public void java.util.ArrayList.addLast(E)"""
        super(_ArrayList, self).addLast(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.ArrayList.hashCode()"""
        return int._wrap(super(ArrayList, self).hashCode())

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> java.util.ArrayList.listIterator(int)"""
        return 'ListIterator'._wrap(super(_ArrayList, self).listIterator(_int.valueOf(arg0)))

    @override
    @overload
    def getFirst(self) -> object:
        """public E java.util.ArrayList.getFirst()"""
        return object._wrap(super(ArrayList, self).getFirst())

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> java.util.ArrayList.listIterator()"""
        return 'ListIterator'._wrap(super(ArrayList, self).listIterator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void java.util.ArrayList.add(int,E)"""
        super(_ArrayList, self).add(_int.valueOf(arg0), arg1)

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.ArrayList.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_ArrayList, self).removeAll(arg0))

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
    def add(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.add(E)"""
        return bool._wrap(super(_ArrayList, self).add(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.ArrayList.isEmpty()"""
        return bool._wrap(super(ArrayList, self).isEmpty())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean java.util.ArrayList.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_ArrayList, self).removeIf(arg0))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int java.util.ArrayList.indexOf(java.lang.Object)"""
        return int._wrap(super(_ArrayList, self).indexOf(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).containsAll(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<E> java.util.ArrayList.spliterator()"""
        return 'Spliterator'._wrap(super(ArrayList, self).spliterator())

    @override
    @overload
    def ensureCapacity(self, arg0: int):
        """public void java.util.ArrayList.ensureCapacity(int)"""
        super(_ArrayList, self).ensureCapacity(_int.valueOf(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean java.util.ArrayList.addAll(int,java.util.Collection<? extends E>)"""
        return bool._wrap(super(_ArrayList, self).addAll(_int.valueOf(arg0), arg1))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void java.util.ArrayList.forEach(java.util.function.Consumer<? super E>)"""
        super(_ArrayList, self).forEach(arg0)

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public void java.util.ArrayList.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(_ArrayList, self).replaceAll(arg0)

    @override
    @overload
    def addFirst(self, arg0: object):
        """public void java.util.ArrayList.addFirst(E)"""
        super(_ArrayList, self).addFirst(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public void java.util.ArrayList.sort(java.util.Comparator<? super E>)"""
        super(_ArrayList, self).sort(arg0)

    @override
    @overload
    def removeFirst(self) -> object:
        """public E java.util.ArrayList.removeFirst()"""
        return object._wrap(super(ArrayList, self).removeFirst())

    @override
    @overload
    def clone(self) -> object:
        """public java.lang.Object java.util.ArrayList.clone()"""
        return object._wrap(super(ArrayList, self).clone())

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E java.util.ArrayList.set(int,E)"""
        return object._wrap(super(_ArrayList, self).set(_int.valueOf(arg0), arg1))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] java.util.ArrayList.toArray(T[])"""
        return List[object]._wrap(super(_ArrayList, self).toArray(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.ArrayList.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_ArrayList, self).addAll(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def get(self, arg0: int) -> object:
        """public E java.util.ArrayList.get(int)"""
        return object._wrap(super(_ArrayList, self).get(_int.valueOf(arg0)))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.text.LanguageData()"""
        val = _LanguageData()
        self.__wrapper = val

    @override
    @overload
    def trimToSize(self):
        """public void java.util.ArrayList.trimToSize()"""
        super(ArrayList, self).trimToSize()

    @override
    @overload
    def getLast(self) -> object:
        """public E java.util.ArrayList.getLast()"""
        return object._wrap(super(ArrayList, self).getLast())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.text.LanguageData()"""
        val = _LanguageData()
        self.__wrapper = val

    @override
    @overload
    def clear(self):
        """public void java.util.ArrayList.clear()"""
        super(ArrayList, self).clear()

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int java.util.ArrayList.lastIndexOf(java.lang.Object)"""
        return int._wrap(super(_ArrayList, self).lastIndexOf(arg0))

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> java.util.ArrayList.subList(int,int)"""
        return 'List'._wrap(super(_ArrayList, self).subList(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.util.AbstractCollection.toString()"""
        return str._wrap(super(AbstractCollection, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.contains(java.lang.Object)"""
        return bool._wrap(super(_ArrayList, self).contains(arg0))

    @overload
    def remove(self, arg0: int) -> object:
        """public E java.util.ArrayList.remove(int)"""
        return object._wrap(super(_ArrayList, self).remove(_int.valueOf(arg0)))

    @override
    @overload
    def size(self) -> int:
        """public int java.util.ArrayList.size()"""
        return int._wrap(super(ArrayList, self).size())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] java.util.ArrayList.toArray()"""
        return List[object]._wrap(super(ArrayList, self).toArray())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.ArrayList.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_ArrayList, self).retainAll(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.remove(java.lang.Object)"""
        return bool._wrap(super(_ArrayList, self).remove(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.equals(java.lang.Object)"""
        return bool._wrap(super(_ArrayList, self).equals(arg0))

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'._wrap(super(List, self).reversed())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def removeLast(self) -> object:
        """public E java.util.ArrayList.removeLast()"""
        return object._wrap(super(ArrayList, self).removeLast())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> java.util.ArrayList.iterator()"""
        return 'Iterator'._wrap(super(ArrayList, self).iterator()) 
 
 
# CLASS: dev.ultreon.quantum.client.text.Language
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.util.Locale as Locale
import dev.ultreon.quantum.client.text.Language as _Language
_Language = _Language
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
import java.util.Locale as _Locale
_Locale = _Locale
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Language():
    """dev.ultreon.quantum.client.text.Language"""
 
    @staticmethod
    def _wrap(java_value: _Language) -> 'Language':
        return Language(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Language):
        """
        Dynamic initializer for Language.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Language__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Language__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def translate(arg0: str, *arg1: object) -> str:
        """public static java.lang.String dev.ultreon.quantum.client.text.Language.translate(java.lang.String,java.lang.Object...)"""
        return str._wrap(_Language.translate(arg0, arg1))

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
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.text.Language.getId()"""
        return 'util.Identifier'._wrap(super(Language, self).getId())

    @overload
    def getLocale(self) -> 'Locale':
        """public java.util.Locale dev.ultreon.quantum.client.text.Language.getLocale()"""
        return 'Locale'._wrap(super(Language, self).getLocale())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def get(self, arg0: str, *arg1: object) -> str:
        """public java.lang.String dev.ultreon.quantum.client.text.Language.get(java.lang.String,java.lang.Object...)"""
        return str._wrap(super(_Language, self).get(arg0, arg1))

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
    def __init__(self, arg0: 'Locale', arg1: 'Map', arg2: 'Identifier'):
        """public dev.ultreon.quantum.client.text.Language(java.util.Locale,java.util.Map<java.lang.String, java.lang.String>,dev.ultreon.quantum.util.Identifier)"""
        val = _Language(arg0, arg1, arg2)
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
 
 
# CLASS: dev.ultreon.quantum.client.text.WordGenerator$Config
from builtins import str
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.text.WordGenerator as _WordGenerator_Config
_Config = _WordGenerator_Config.Config
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Config():
    """dev.ultreon.quantum.client.text.WordGenerator.Config"""
 
    @staticmethod
    def _wrap(java_value: _Config) -> 'Config':
        return Config(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Config):
        """
        Dynamic initializer for Config.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Config__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Config__wrapper":
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

    @overload
    def seed(self, arg0: int) -> 'Config':
        """public dev.ultreon.quantum.client.text.WordGenerator$Config dev.ultreon.quantum.client.text.WordGenerator$Config.seed(long)"""
        return 'Config'._wrap(super(_Config, self).seed(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def minSize(self, arg0: int) -> 'Config':
        """public dev.ultreon.quantum.client.text.WordGenerator$Config dev.ultreon.quantum.client.text.WordGenerator$Config.minSize(int)"""
        return 'Config'._wrap(super(_Config, self).minSize(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def named(self) -> 'Config':
        """public dev.ultreon.quantum.client.text.WordGenerator$Config dev.ultreon.quantum.client.text.WordGenerator$Config.named()"""
        return 'Config'._wrap(super(Config, self).named())

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
    def __init__(self):
        """public dev.ultreon.quantum.client.text.WordGenerator$Config()"""
        val = _Config()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.text.WordGenerator$Config()"""
        val = _Config()
        self.__wrapper = val

    @overload
    def maxSize(self, arg0: int) -> 'Config':
        """public dev.ultreon.quantum.client.text.WordGenerator$Config dev.ultreon.quantum.client.text.WordGenerator$Config.maxSize(int)"""
        return 'Config'._wrap(super(_Config, self).maxSize(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.text.Translation
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.client.text.Translation as _Translation
_Translation = _Translation
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Translation():
    """dev.ultreon.quantum.client.text.Translation"""
 
    @staticmethod
    def _wrap(java_value: _Translation) -> 'Translation':
        return Translation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Translation):
        """
        Dynamic initializer for Translation.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Translation__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Translation__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: str, *arg1: object):
        """public dev.ultreon.quantum.client.text.Translation(java.lang.String,java.lang.Object...)"""
        val = _Translation(arg0, arg1)
        self.__wrapper = val

    @overload
    def set(self, arg0: int, arg1: object):
        """public void dev.ultreon.quantum.client.text.Translation.set(int,java.lang.Object)"""
        super(_Translation, self).set(_int.valueOf(arg0), arg1)

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.text.Translation.toString()"""
        return str._wrap(super(Translation, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def get(self, arg0: int) -> object:
        """public java.lang.Object dev.ultreon.quantum.client.text.Translation.get(int)"""
        return object._wrap(super(_Translation, self).get(_int.valueOf(arg0)))

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
 
 
# CLASS: dev.ultreon.quantum.client.text.UITranslations
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.text.UITranslations as _UITranslations
_UITranslations = _UITranslations
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UITranslations():
    """dev.ultreon.quantum.client.text.UITranslations"""
 
    @staticmethod
    def _wrap(java_value: _UITranslations) -> 'UITranslations':
        return UITranslations(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UITranslations):
        """
        Dynamic initializer for UITranslations.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UITranslations__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UITranslations__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.TOGGLE_ALL
    TOGGLE_ALL: 'text.TranslationText' = _wrap(_text.TranslationText.TOGGLE_ALL)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.ENABLE_ALL
    ENABLE_ALL: 'text.TranslationText' = _wrap(_text.TranslationText.ENABLE_ALL)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.TOGGLE
    TOGGLE: 'text.TranslationText' = _wrap(_text.TranslationText.TOGGLE)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.DENY
    DENY: 'text.TranslationText' = _wrap(_text.TranslationText.DENY)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.YES
    YES: 'text.TranslationText' = _wrap(_text.TranslationText.YES)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.DISABLE
    DISABLE: 'text.TranslationText' = _wrap(_text.TranslationText.DISABLE)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.DONE
    DONE: 'text.TranslationText' = _wrap(_text.TranslationText.DONE)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.CANCEL
    CANCEL: 'text.TranslationText' = _wrap(_text.TranslationText.CANCEL)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.ENABLE
    ENABLE: 'text.TranslationText' = _wrap(_text.TranslationText.ENABLE)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.NO
    NO: 'text.TranslationText' = _wrap(_text.TranslationText.NO)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.BACK
    BACK: 'text.TranslationText' = _wrap(_text.TranslationText.BACK)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.CONFIRM
    CONFIRM: 'text.TranslationText' = _wrap(_text.TranslationText.CONFIRM)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.DISABLE_ALL
    DISABLE_ALL: 'text.TranslationText' = _wrap(_text.TranslationText.DISABLE_ALL)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.OK
    OK: 'text.TranslationText' = _wrap(_text.TranslationText.OK)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.OKAY
    OKAY: 'text.TranslationText' = _wrap(_text.TranslationText.OKAY)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.PROCEED
    PROCEED: 'text.TranslationText' = _wrap(_text.TranslationText.PROCEED)

    # public static final dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.client.text.UITranslations.ACCEPT
    ACCEPT: 'text.TranslationText' = _wrap(_text.TranslationText.ACCEPT)


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
        """public dev.ultreon.quantum.client.text.UITranslations()"""
        val = _UITranslations()
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.text.UITranslations()"""
        val = _UITranslations()
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())