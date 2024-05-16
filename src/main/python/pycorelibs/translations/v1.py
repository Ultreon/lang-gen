from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.lang.Long as __long
import dev.ultreon.libs.translations.v1.Translation as __Translation
__Translation = __Translation
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
    """dev.ultreon.libs.translations.v1.Translation"""
 
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

    @overload
    def get(self, arg0: int) -> object:
        """public java.lang.Object dev.ultreon.libs.translations.v1.Translation.get(int)"""
        return object.__wrap(super(__Translation, self).get(__int.valueOf(arg0)))

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
    def __init__(self, arg0: str, *arg1: object):
        """public dev.ultreon.libs.translations.v1.Translation(java.lang.String,java.lang.Object...)"""
        val = __Translation(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.translations.v1.Translation.toString()"""
        return str.__wrap(super(Translation, self).toString())

    @overload
    def set(self, arg0: int, arg1: object):
        """public void dev.ultreon.libs.translations.v1.Translation.set(int,java.lang.Object)"""
        super(__Translation, self).set(__int.valueOf(arg0), arg1)

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

 
 
 
# CLASS: dev.ultreon.libs.translations.v1.Translation
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.lang.Long as __long
import dev.ultreon.libs.translations.v1.Translation as __Translation
__Translation = __Translation
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
    """dev.ultreon.libs.translations.v1.Translation"""
 
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

    @overload
    def get(self, arg0: int) -> object:
        """public java.lang.Object dev.ultreon.libs.translations.v1.Translation.get(int)"""
        return object.__wrap(super(__Translation, self).get(__int.valueOf(arg0)))

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
    def __init__(self, arg0: str, *arg1: object):
        """public dev.ultreon.libs.translations.v1.Translation(java.lang.String,java.lang.Object...)"""
        val = __Translation(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.translations.v1.Translation.toString()"""
        return str.__wrap(super(Translation, self).toString())

    @overload
    def set(self, arg0: int, arg1: object):
        """public void dev.ultreon.libs.translations.v1.Translation.set(int,java.lang.Object)"""
        super(__Translation, self).set(__int.valueOf(arg0), arg1)

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

 
 
 
# CLASS: dev.ultreon.libs.translations.v1.Translation 
 
 
# CLASS: dev.ultreon.libs.translations.v1.LanguageManager
from pyquantum_helper import import_once as __import_once__
import java.util.Locale as Locale
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import dev.ultreon.libs.translations.v1.LanguageManager as __LanguageManager
__LanguageManager = __LanguageManager
import dev.ultreon.libs.translations.v1.Language as __Language
__Language = __Language
try:
    from pycorelibs.resources import v0
except ImportError:
    v0 = __import_once__("pycorelibs.resources.v0")

import java.util.Set as Set
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = __import_once__("pycorelibs.commons.v0")

import java.lang.String as __String
__String = __String
import java.io.Reader as Reader
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.libs.commons.v0.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Integer as __int
import java.util.Locale as __Locale
__Locale = __Locale
from builtins import bool
import java.util.List as List
from builtins import int
 
class LanguageManager():
    """dev.ultreon.libs.translations.v1.LanguageManager"""
 
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
    def getLanguageIDs(self) -> 'Set':
        """public java.util.Set<dev.ultreon.libs.commons.v0.Identifier> dev.ultreon.libs.translations.v1.LanguageManager.getLanguageIDs()"""
        return 'Set'.__wrap(super(LanguageManager, self).getLanguageIDs())

    @overload
    def getLanguageID(self, arg0: 'Locale') -> 'v0.Identifier':
        """public dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.translations.v1.LanguageManager.getLanguageID(java.util.Locale)"""
        return 'v0.Identifier'.__wrap(super(__LanguageManager, self).getLanguageID(arg0))

    @overload
    def getLocales(self) -> 'Set':
        """public java.util.Set<java.util.Locale> dev.ultreon.libs.translations.v1.LanguageManager.getLocales()"""
        return 'Set'.__wrap(super(LanguageManager, self).getLocales())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getCurrentLanguage() -> 'Locale':
        """public static java.util.Locale dev.ultreon.libs.translations.v1.LanguageManager.getCurrentLanguage()"""
        return Locale.__wrap(__LanguageManager.getCurrentLanguage())

    @overload
    def getLocale(self, arg0: 'Identifier') -> 'Locale':
        """public java.util.Locale dev.ultreon.libs.translations.v1.LanguageManager.getLocale(dev.ultreon.libs.commons.v0.Identifier)"""
        return 'Locale'.__wrap(super(__LanguageManager, self).getLocale(arg0))

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
    def load(self, arg0: 'Locale', arg1: 'Identifier', arg2: 'ResourceManager') -> 'Language':
        """public dev.ultreon.libs.translations.v1.Language dev.ultreon.libs.translations.v1.LanguageManager.load(java.util.Locale,dev.ultreon.libs.commons.v0.Identifier,dev.ultreon.libs.resources.v0.ResourceManager)"""
        return 'Language'.__wrap(super(__LanguageManager, self).load(arg0, arg1, arg2))

    @overload
    def register(self, arg0: 'Locale', arg1: 'Identifier'):
        """public void dev.ultreon.libs.translations.v1.LanguageManager.register(java.util.Locale,dev.ultreon.libs.commons.v0.Identifier)"""
        super(__LanguageManager, self).register(arg0, arg1)

    @overload
    def getLanguages(self) -> 'List':
        """public java.util.List<dev.ultreon.libs.translations.v1.Language> dev.ultreon.libs.translations.v1.LanguageManager.getLanguages()"""
        return 'List'.__wrap(super(LanguageManager, self).getLanguages())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def load(self, arg0: 'Locale', arg1: 'Identifier', arg2: 'Reader') -> 'Language':
        """public dev.ultreon.libs.translations.v1.Language dev.ultreon.libs.translations.v1.LanguageManager.load(java.util.Locale,dev.ultreon.libs.commons.v0.Identifier,java.io.Reader)"""
        return 'Language'.__wrap(super(__LanguageManager, self).load(arg0, arg1, arg2))

    @overload
    def get(self, arg0: 'Locale') -> 'Language':
        """public dev.ultreon.libs.translations.v1.Language dev.ultreon.libs.translations.v1.LanguageManager.get(java.util.Locale)"""
        return 'Language'.__wrap(super(__LanguageManager, self).get(arg0))

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
    def setCurrentLanguage(arg0: 'Locale'):
        """public static void dev.ultreon.libs.translations.v1.LanguageManager.setCurrentLanguage(java.util.Locale)"""
        __LanguageManager.setCurrentLanguage(arg0) 
 
 
# CLASS: dev.ultreon.libs.translations.v1.Language
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.util.Locale as Locale
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.translations.v1.Language as __Language
__Language = __Language
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = __import_once__("pycorelibs.commons.v0")

import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.libs.commons.v0.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Integer as __int
import java.util.Locale as __Locale
__Locale = __Locale
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class Language():
    """dev.ultreon.libs.translations.v1.Language"""
 
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
    def getId(self) -> 'v0.Identifier':
        """public dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.translations.v1.Language.getId()"""
        return 'v0.Identifier'.__wrap(super(Language, self).getId())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Locale', arg1: 'Map', arg2: 'Identifier'):
        """public dev.ultreon.libs.translations.v1.Language(java.util.Locale,java.util.Map<java.lang.String, java.lang.String>,dev.ultreon.libs.commons.v0.Identifier)"""
        val = __Language(arg0, arg1, arg2)
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
    def translate(arg0: str, *arg1: object) -> str:
        """public static java.lang.String dev.ultreon.libs.translations.v1.Language.translate(java.lang.String,java.lang.Object...)"""
        return str.__wrap(__Language.translate(arg0, arg1))

    @overload
    def get(self, arg0: str, *arg1: object) -> str:
        """public java.lang.String dev.ultreon.libs.translations.v1.Language.get(java.lang.String,java.lang.Object...)"""
        return str.__wrap(super(__Language, self).get(arg0, arg1))

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
    def getLocale(self) -> 'Locale':
        """public java.util.Locale dev.ultreon.libs.translations.v1.Language.getLocale()"""
        return 'Locale'.__wrap(super(Language, self).getLocale())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))