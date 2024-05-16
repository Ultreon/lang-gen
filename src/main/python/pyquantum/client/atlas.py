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
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
import dev.ultreon.quantum.client.atlas.TextureStitcher as _TextureStitcher_Type
_Type = _TextureStitcher_Type.Type
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Type():
    """dev.ultreon.quantum.client.atlas.TextureStitcher.Type"""
 
    @staticmethod
    def _wrap(java_value: _Type) -> 'Type':
        return Type(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Type):
        """
        Dynamic initializer for Type.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Type__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Type__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def values() -> List['Type']:
        """public static dev.ultreon.quantum.client.atlas.TextureStitcher$Type[] dev.ultreon.quantum.client.atlas.TextureStitcher$Type.values()"""
        return List[Type]._wrap(_Type.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Type':
        """public static dev.ultreon.quantum.client.atlas.TextureStitcher$Type dev.ultreon.quantum.client.atlas.TextureStitcher$Type.valueOf(java.lang.String)"""
        return Type._wrap(_Type.valueOf(arg0))


Type.EMISSIVE = Type._wrap(_EMISSIVE.EMISSIVE)

Type.DIFFUSE = Type._wrap(_DIFFUSE.DIFFUSE)

 
 
 
# CLASS: dev.ultreon.quantum.client.atlas.TextureStitcher$Type
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
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
import dev.ultreon.quantum.client.atlas.TextureStitcher as _TextureStitcher_Type
_Type = _TextureStitcher_Type.Type
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Type():
    """dev.ultreon.quantum.client.atlas.TextureStitcher.Type"""
 
    @staticmethod
    def _wrap(java_value: _Type) -> 'Type':
        return Type(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Type):
        """
        Dynamic initializer for Type.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Type__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Type__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def values() -> List['Type']:
        """public static dev.ultreon.quantum.client.atlas.TextureStitcher$Type[] dev.ultreon.quantum.client.atlas.TextureStitcher$Type.values()"""
        return List[Type]._wrap(_Type.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Type':
        """public static dev.ultreon.quantum.client.atlas.TextureStitcher$Type dev.ultreon.quantum.client.atlas.TextureStitcher$Type.valueOf(java.lang.String)"""
        return Type._wrap(_Type.valueOf(arg0))


Type.EMISSIVE = Type._wrap(_EMISSIVE.EMISSIVE)

Type.DIFFUSE = Type._wrap(_DIFFUSE.DIFFUSE)

 
 
 
# CLASS: dev.ultreon.quantum.client.atlas.TextureStitcher$Type 
 
 
# CLASS: dev.ultreon.quantum.client.atlas.TextureStitcher
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.client.atlas.TextureAtlas as _TextureAtlas
_TextureAtlas = _TextureAtlas
import java.lang.Integer as _int
import dev.ultreon.quantum.client.atlas.TextureStitcher as _TextureStitcher
_TextureStitcher = _TextureStitcher
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextureStitcher():
    """dev.ultreon.quantum.client.atlas.TextureStitcher"""
 
    @staticmethod
    def _wrap(java_value: _TextureStitcher) -> 'TextureStitcher':
        return TextureStitcher(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureStitcher):
        """
        Dynamic initializer for TextureStitcher.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureStitcher__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureStitcher__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.atlas.TextureStitcher.dispose()"""
        super(TextureStitcher, self).dispose()

    @overload
    def add(self, arg0: 'Identifier', arg1: 'Texture', arg2: 'Texture'):
        """public void dev.ultreon.quantum.client.atlas.TextureStitcher.add(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.Texture,com.badlogic.gdx.graphics.Texture)"""
        super(_TextureStitcher, self).add(arg0, arg1, arg2)

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

    @overload
    def stitch(self) -> 'TextureAtlas':
        """public dev.ultreon.quantum.client.atlas.TextureAtlas dev.ultreon.quantum.client.atlas.TextureStitcher.stitch()"""
        return 'TextureAtlas'._wrap(super(TextureStitcher, self).stitch())

    @overload
    def add(self, arg0: 'Identifier', arg1: 'Texture'):
        """public void dev.ultreon.quantum.client.atlas.TextureStitcher.add(dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.Texture)"""
        super(_TextureStitcher, self).add(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Identifier'):
        """public dev.ultreon.quantum.client.atlas.TextureStitcher(dev.ultreon.quantum.util.Identifier)"""
        val = _TextureStitcher(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.client.atlas.TextureAtlas
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g2d.TextureRegion as _TextureRegion
_TextureRegion = _TextureRegion
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.Texture as _Texture
_Texture = _Texture
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.client.atlas.TextureAtlas as _TextureAtlas
_TextureAtlas = _TextureAtlas
import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextureAtlas():
    """dev.ultreon.quantum.client.atlas.TextureAtlas"""
 
    @staticmethod
    def _wrap(java_value: _TextureAtlas) -> 'TextureAtlas':
        return TextureAtlas(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureAtlas):
        """
        Dynamic initializer for TextureAtlas.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureAtlas__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureAtlas__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.atlas.TextureAtlas.getTexture()"""
        return 'graphics.Texture'._wrap(super(TextureAtlas, self).getTexture())

    @overload
    def get(self, arg0: 'Identifier') -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion dev.ultreon.quantum.client.atlas.TextureAtlas.get(dev.ultreon.quantum.util.Identifier)"""
        return 'g2d.TextureRegion'._wrap(super(_TextureAtlas, self).get(arg0))

    @overload
    def getEmissiveTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture dev.ultreon.quantum.client.atlas.TextureAtlas.getEmissiveTexture()"""
        return 'graphics.Texture'._wrap(super(TextureAtlas, self).getEmissiveTexture())

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
    def getEmissive(self, arg0: 'Identifier') -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion dev.ultreon.quantum.client.atlas.TextureAtlas.getEmissive(dev.ultreon.quantum.util.Identifier)"""
        return 'g2d.TextureRegion'._wrap(super(_TextureAtlas, self).getEmissive(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.client.atlas.TextureAtlas.dispose()"""
        super(TextureAtlas, self).dispose()

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
    def __init__(self, arg0: 'TextureStitcher', arg1: 'Identifier', arg2: 'Texture', arg3: 'Texture', arg4: 'Map'):
        """public dev.ultreon.quantum.client.atlas.TextureAtlas(dev.ultreon.quantum.client.atlas.TextureStitcher,dev.ultreon.quantum.util.Identifier,com.badlogic.gdx.graphics.Texture,com.badlogic.gdx.graphics.Texture,java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.util.TextureOffset>)"""
        val = _TextureAtlas(arg0, arg1, arg2, arg3, arg4)
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