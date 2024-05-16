from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.util.Locale as Locale
try:
    import pygson
except ImportError:
    pygson = _import_once("pygson")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import dev.ultreon.libs.translations.v0.Language as _Language
_Language = _Language
import java.lang.String as _string
import dev.ultreon.libs.commons.v0.Identifier as _Identifier
_Identifier = _Identifier
import java.lang.Integer as _int
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = _import_once("pycorelibs.commons.v0")

from builtins import bool
import java.lang.Long as _long
import java.util.Locale as _Locale
_Locale = _Locale
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Language():
    """dev.ultreon.libs.translations.v0.Language"""
 
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
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def translate(arg0: str, *arg1: object) -> str:
        """public static java.lang.String dev.ultreon.libs.translations.v0.Language.translate(java.lang.String,java.lang.Object...)"""
        return str._wrap(_Language.translate(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Locale', arg1: 'JsonObject', arg2: 'Identifier'):
        """public dev.ultreon.libs.translations.v0.Language(java.util.Locale,com.google.gson.JsonObject,dev.ultreon.libs.commons.v0.Identifier)"""
        val = _Language(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getId(self) -> 'v0.Identifier':
        """public dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.translations.v0.Language.getId()"""
        return 'v0.Identifier'._wrap(super(Language, self).getId())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def get(self, arg0: str, *arg1: object) -> str:
        """public java.lang.String dev.ultreon.libs.translations.v0.Language.get(java.lang.String,java.lang.Object...)"""
        return str._wrap(super(_Language, self).get(arg0, arg1))

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
    def getLocale(self) -> 'Locale':
        """public java.util.Locale dev.ultreon.libs.translations.v0.Language.getLocale()"""
        return 'Locale'._wrap(super(Language, self).getLocale())

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

 
 
 
# CLASS: dev.ultreon.libs.translations.v0.Language
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.util.Locale as Locale
try:
    import pygson
except ImportError:
    pygson = _import_once("pygson")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import dev.ultreon.libs.translations.v0.Language as _Language
_Language = _Language
import java.lang.String as _string
import dev.ultreon.libs.commons.v0.Identifier as _Identifier
_Identifier = _Identifier
import java.lang.Integer as _int
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = _import_once("pycorelibs.commons.v0")

from builtins import bool
import java.lang.Long as _long
import java.util.Locale as _Locale
_Locale = _Locale
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Language():
    """dev.ultreon.libs.translations.v0.Language"""
 
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
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def translate(arg0: str, *arg1: object) -> str:
        """public static java.lang.String dev.ultreon.libs.translations.v0.Language.translate(java.lang.String,java.lang.Object...)"""
        return str._wrap(_Language.translate(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Locale', arg1: 'JsonObject', arg2: 'Identifier'):
        """public dev.ultreon.libs.translations.v0.Language(java.util.Locale,com.google.gson.JsonObject,dev.ultreon.libs.commons.v0.Identifier)"""
        val = _Language(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getId(self) -> 'v0.Identifier':
        """public dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.translations.v0.Language.getId()"""
        return 'v0.Identifier'._wrap(super(Language, self).getId())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def get(self, arg0: str, *arg1: object) -> str:
        """public java.lang.String dev.ultreon.libs.translations.v0.Language.get(java.lang.String,java.lang.Object...)"""
        return str._wrap(super(_Language, self).get(arg0, arg1))

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
    def getLocale(self) -> 'Locale':
        """public java.util.Locale dev.ultreon.libs.translations.v0.Language.getLocale()"""
        return 'Locale'._wrap(super(Language, self).getLocale())

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

 
 
 
# CLASS: dev.ultreon.libs.translations.v0.Language 
 
 
# CLASS: dev.ultreon.libs.translations.v0.Translation
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
import dev.ultreon.libs.translations.v0.Translation as _Translation
_Translation = _Translation
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Translation():
    """dev.ultreon.libs.translations.v0.Translation"""
 
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
    def set(self, arg0: int, arg1: object):
        """public void dev.ultreon.libs.translations.v0.Translation.set(int,java.lang.Object)"""
        super(_Translation, self).set(_int.valueOf(arg0), arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: str, *arg1: object):
        """public dev.ultreon.libs.translations.v0.Translation(java.lang.String,java.lang.Object...)"""
        val = _Translation(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def get(self, arg0: int) -> object:
        """public java.lang.Object dev.ultreon.libs.translations.v0.Translation.get(int)"""
        return object._wrap(super(_Translation, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.translations.v0.Translation.toString()"""
        return str._wrap(super(Translation, self).toString())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.libs.translations.v0.LanguageManager
from pyquantum_helper import import_once as _import_once
import java.util.Locale as Locale
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.libs.translations.v0.LanguageManager as _LanguageManager
_LanguageManager = _LanguageManager
import java.lang.String as _String
_String = _String
import dev.ultreon.libs.translations.v0.Language as _Language
_Language = _Language
try:
    from pycorelibs.resources import v0
except ImportError:
    v0 = _import_once("pycorelibs.resources.v0")

import java.util.List as _List
_List = _List
import java.util.Set as _Set
_Set = _Set
import java.lang.String as _string
import java.util.Set as Set
import java.lang.Integer as _int
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = _import_once("pycorelibs.commons.v0")

import java.io.Reader as Reader
from builtins import bool
import java.lang.Long as _long
import java.util.Locale as _Locale
_Locale = _Locale
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LanguageManager():
    """dev.ultreon.libs.translations.v0.LanguageManager"""
 
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
 
    @overload
    def load(self, arg0: 'Locale', arg1: 'Identifier', arg2: 'ResourceManager') -> 'Language':
        """public dev.ultreon.libs.translations.v0.Language dev.ultreon.libs.translations.v0.LanguageManager.load(java.util.Locale,dev.ultreon.libs.commons.v0.Identifier,dev.ultreon.libs.resources.v0.ResourceManager)"""
        return 'Language'._wrap(super(_LanguageManager, self).load(arg0, arg1, arg2))

    @overload
    def load(self, arg0: 'Locale', arg1: 'Identifier', arg2: 'Reader') -> 'Language':
        """public dev.ultreon.libs.translations.v0.Language dev.ultreon.libs.translations.v0.LanguageManager.load(java.util.Locale,dev.ultreon.libs.commons.v0.Identifier,java.io.Reader)"""
        return 'Language'._wrap(super(_LanguageManager, self).load(arg0, arg1, arg2))

    @overload
    def getLocales(self) -> 'Set':
        """public java.util.Set<java.util.Locale> dev.ultreon.libs.translations.v0.LanguageManager.getLocales()"""
        return 'Set'._wrap(super(LanguageManager, self).getLocales())

    @overload
    def getLocale(self, arg0: str) -> 'Locale':
        """public java.util.Locale dev.ultreon.libs.translations.v0.LanguageManager.getLocale(java.lang.String)"""
        return 'Locale'._wrap(super(_LanguageManager, self).getLocale(arg0))

    @overload
    def getLanguageIDs(self) -> 'Set':
        """public java.util.Set<java.lang.String> dev.ultreon.libs.translations.v0.LanguageManager.getLanguageIDs()"""
        return 'Set'._wrap(super(LanguageManager, self).getLanguageIDs())

    @staticmethod
    @overload
    def getCurrentLanguage() -> 'Locale':
        """public static java.util.Locale dev.ultreon.libs.translations.v0.LanguageManager.getCurrentLanguage()"""
        return Locale._wrap(_LanguageManager.getCurrentLanguage())

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
    def setCurrentLanguage(arg0: 'Locale'):
        """public static void dev.ultreon.libs.translations.v0.LanguageManager.setCurrentLanguage(java.util.Locale)"""
        _LanguageManager.setCurrentLanguage(arg0)

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
    def getLanguages(self) -> 'List':
        """public java.util.List<dev.ultreon.libs.translations.v0.Language> dev.ultreon.libs.translations.v0.LanguageManager.getLanguages()"""
        return 'List'._wrap(super(LanguageManager, self).getLanguages())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def get(self, arg0: 'Locale') -> 'Language':
        """public dev.ultreon.libs.translations.v0.Language dev.ultreon.libs.translations.v0.LanguageManager.get(java.util.Locale)"""
        return 'Language'._wrap(super(_LanguageManager, self).get(arg0))

    @overload
    def getLanguageID(self, arg0: 'Locale') -> str:
        """public java.lang.String dev.ultreon.libs.translations.v0.LanguageManager.getLanguageID(java.util.Locale)"""
        return str._wrap(super(_LanguageManager, self).getLanguageID(arg0))

    @overload
    def register(self, arg0: 'Locale', arg1: str):
        """public void dev.ultreon.libs.translations.v0.LanguageManager.register(java.util.Locale,java.lang.String)"""
        super(_LanguageManager, self).register(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())