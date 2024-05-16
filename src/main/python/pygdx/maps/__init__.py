from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g2d.TextureRegion as _TextureRegion
_TextureRegion = _TextureRegion
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.maps.ImageResolver as _ImageResolver_DirectImageResolver
_DirectImageResolver = _ImageResolver_DirectImageResolver.DirectImageResolver
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DirectImageResolver():
    """com.badlogic.gdx.maps.ImageResolver.DirectImageResolver"""
 
    @staticmethod
    def _wrap(java_value: _DirectImageResolver) -> 'DirectImageResolver':
        return DirectImageResolver(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DirectImageResolver):
        """
        Dynamic initializer for DirectImageResolver.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DirectImageResolver__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DirectImageResolver__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getImage(self, arg0: str) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.ImageResolver$DirectImageResolver.getImage(java.lang.String)"""
        return 'g2d.TextureRegion'._wrap(super(_DirectImageResolver, self).getImage(arg0))

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
    def __init__(self, arg0: 'ObjectMap'):
        """public com.badlogic.gdx.maps.ImageResolver$DirectImageResolver(com.badlogic.gdx.utils.ObjectMap<java.lang.String, com.badlogic.gdx.graphics.Texture>)"""
        val = _DirectImageResolver(arg0)
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

 
 
 
# CLASS: com.badlogic.gdx.maps.ImageResolver$DirectImageResolver
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g2d.TextureRegion as _TextureRegion
_TextureRegion = _TextureRegion
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.maps.ImageResolver as _ImageResolver_DirectImageResolver
_DirectImageResolver = _ImageResolver_DirectImageResolver.DirectImageResolver
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DirectImageResolver():
    """com.badlogic.gdx.maps.ImageResolver.DirectImageResolver"""
 
    @staticmethod
    def _wrap(java_value: _DirectImageResolver) -> 'DirectImageResolver':
        return DirectImageResolver(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DirectImageResolver):
        """
        Dynamic initializer for DirectImageResolver.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DirectImageResolver__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DirectImageResolver__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getImage(self, arg0: str) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.ImageResolver$DirectImageResolver.getImage(java.lang.String)"""
        return 'g2d.TextureRegion'._wrap(super(_DirectImageResolver, self).getImage(arg0))

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
    def __init__(self, arg0: 'ObjectMap'):
        """public com.badlogic.gdx.maps.ImageResolver$DirectImageResolver(com.badlogic.gdx.utils.ObjectMap<java.lang.String, com.badlogic.gdx.graphics.Texture>)"""
        val = _DirectImageResolver(arg0)
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

 
 
 
# CLASS: com.badlogic.gdx.maps.ImageResolver$DirectImageResolver 
 
 
# CLASS: com.badlogic.gdx.maps.ImageResolver$AssetManagerImageResolver
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
import java.lang.Object as _object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import com.badlogic.gdx.maps.ImageResolver as _ImageResolver_AssetManagerImageResolver
_AssetManagerImageResolver = _ImageResolver_AssetManagerImageResolver.AssetManagerImageResolver
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AssetManagerImageResolver():
    """com.badlogic.gdx.maps.ImageResolver.AssetManagerImageResolver"""
 
    @staticmethod
    def _wrap(java_value: _AssetManagerImageResolver) -> 'AssetManagerImageResolver':
        return AssetManagerImageResolver(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AssetManagerImageResolver):
        """
        Dynamic initializer for AssetManagerImageResolver.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AssetManagerImageResolver__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AssetManagerImageResolver__wrapper":
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
    def __init__(self, arg0: 'AssetManager'):
        """public com.badlogic.gdx.maps.ImageResolver$AssetManagerImageResolver(com.badlogic.gdx.assets.AssetManager)"""
        val = _AssetManagerImageResolver(arg0)
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

    @overload
    def getImage(self, arg0: str) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.ImageResolver$AssetManagerImageResolver.getImage(java.lang.String)"""
        return 'g2d.TextureRegion'._wrap(super(_AssetManagerImageResolver, self).getImage(arg0))

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
 
 
# CLASS: com.badlogic.gdx.maps.MapLayers
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.maps.MapLayers as _MapLayers
_MapLayers = _MapLayers
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
import java.lang.String as _string
import java.util.Spliterator as Spliterator
import com.badlogic.gdx.maps.MapLayer as _MapLayer
_MapLayer = _MapLayer
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MapLayers():
    """com.badlogic.gdx.maps.MapLayers"""
 
    @staticmethod
    def _wrap(java_value: _MapLayers) -> 'MapLayers':
        return MapLayers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MapLayers):
        """
        Dynamic initializer for MapLayers.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MapLayers__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MapLayers__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getByType(self, arg0: 'Class') -> 'utils.Array':
        """public <T extends com.badlogic.gdx.maps.MapLayer> com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.maps.MapLayers.getByType(java.lang.Class<T>)"""
        return 'utils.Array'._wrap(super(_MapLayers, self).getByType(arg0))

    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.maps.MapLayers.size()"""
        return int._wrap(super(MapLayers, self).size())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def get(self, arg0: int) -> 'MapLayer':
        """public com.badlogic.gdx.maps.MapLayer com.badlogic.gdx.maps.MapLayers.get(int)"""
        return 'MapLayer'._wrap(super(_MapLayers, self).get(_int.valueOf(arg0)))

    @overload
    def getCount(self) -> int:
        """public int com.badlogic.gdx.maps.MapLayers.getCount()"""
        return int._wrap(super(MapLayers, self).getCount())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

    @overload
    def getByType(self, arg0: 'Class', arg1: 'Array') -> 'utils.Array':
        """public <T extends com.badlogic.gdx.maps.MapLayer> com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.maps.MapLayers.getByType(java.lang.Class<T>,com.badlogic.gdx.utils.Array<T>)"""
        return 'utils.Array'._wrap(super(_MapLayers, self).getByType(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def get(self, arg0: str) -> 'MapLayer':
        """public com.badlogic.gdx.maps.MapLayer com.badlogic.gdx.maps.MapLayers.get(java.lang.String)"""
        return 'MapLayer'._wrap(super(_MapLayers, self).get(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.MapLayers()"""
        val = _MapLayers()
        self.__wrapper = val

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<com.badlogic.gdx.maps.MapLayer> com.badlogic.gdx.maps.MapLayers.iterator()"""
        return 'Iterator'._wrap(super(MapLayers, self).iterator())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.MapLayers()"""
        val = _MapLayers()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def remove(self, arg0: 'MapLayer'):
        """public void com.badlogic.gdx.maps.MapLayers.remove(com.badlogic.gdx.maps.MapLayer)"""
        super(_MapLayers, self).remove(arg0)

    @overload
    def getIndex(self, arg0: str) -> int:
        """public int com.badlogic.gdx.maps.MapLayers.getIndex(java.lang.String)"""
        return int._wrap(super(_MapLayers, self).getIndex(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getIndex(self, arg0: 'MapLayer') -> int:
        """public int com.badlogic.gdx.maps.MapLayers.getIndex(com.badlogic.gdx.maps.MapLayer)"""
        return int._wrap(super(_MapLayers, self).getIndex(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def add(self, arg0: 'MapLayer'):
        """public void com.badlogic.gdx.maps.MapLayers.add(com.badlogic.gdx.maps.MapLayer)"""
        super(_MapLayers, self).add(arg0)

    @overload
    def remove(self, arg0: int):
        """public void com.badlogic.gdx.maps.MapLayers.remove(int)"""
        super(_MapLayers, self).remove(_int.valueOf(arg0))

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

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.maps.MapProperties
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.lang.String as _string
import java.lang.Integer as _int
import java.util.Iterator as _Iterator
_Iterator = _Iterator
import com.badlogic.gdx.maps.MapProperties as _MapProperties
_MapProperties = _MapProperties
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MapProperties():
    """com.badlogic.gdx.maps.MapProperties"""
 
    @staticmethod
    def _wrap(java_value: _MapProperties) -> 'MapProperties':
        return MapProperties(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MapProperties):
        """
        Dynamic initializer for MapProperties.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MapProperties__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MapProperties__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def get(self, arg0: str) -> object:
        """public java.lang.Object com.badlogic.gdx.maps.MapProperties.get(java.lang.String)"""
        return object._wrap(super(_MapProperties, self).get(arg0))

    @overload
    def remove(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapProperties.remove(java.lang.String)"""
        super(_MapProperties, self).remove(arg0)

    @overload
    def get(self, arg0: str, arg1: object, arg2: 'Class') -> object:
        """public <T> T com.badlogic.gdx.maps.MapProperties.get(java.lang.String,T,java.lang.Class<T>)"""
        return object._wrap(super(_MapProperties, self).get(arg0, arg1, arg2))

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
    def get(self, arg0: str, arg1: 'Class') -> object:
        """public <T> T com.badlogic.gdx.maps.MapProperties.get(java.lang.String,java.lang.Class<T>)"""
        return object._wrap(super(_MapProperties, self).get(arg0, arg1))

    @overload
    def putAll(self, arg0: 'MapProperties'):
        """public void com.badlogic.gdx.maps.MapProperties.putAll(com.badlogic.gdx.maps.MapProperties)"""
        super(_MapProperties, self).putAll(arg0)

    @overload
    def clear(self):
        """public void com.badlogic.gdx.maps.MapProperties.clear()"""
        super(MapProperties, self).clear()

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

    @overload
    def getValues(self) -> 'Iterator':
        """public java.util.Iterator<java.lang.Object> com.badlogic.gdx.maps.MapProperties.getValues()"""
        return 'Iterator'._wrap(super(MapProperties, self).getValues())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.MapProperties()"""
        val = _MapProperties()
        self.__wrapper = val

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
    def put(self, arg0: str, arg1: object):
        """public void com.badlogic.gdx.maps.MapProperties.put(java.lang.String,java.lang.Object)"""
        super(_MapProperties, self).put(arg0, arg1)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.MapProperties()"""
        val = _MapProperties()
        self.__wrapper = val

    @overload
    def containsKey(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.maps.MapProperties.containsKey(java.lang.String)"""
        return bool._wrap(super(_MapProperties, self).containsKey(arg0))

    @overload
    def getKeys(self) -> 'Iterator':
        """public java.util.Iterator<java.lang.String> com.badlogic.gdx.maps.MapProperties.getKeys()"""
        return 'Iterator'._wrap(super(MapProperties, self).getKeys())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.maps.ImageResolver
import com.badlogic.gdx.maps.ImageResolver as _ImageResolver
_ImageResolver = _ImageResolver
from abc import abstractmethod, ABC
 
class ImageResolver():
    """com.badlogic.gdx.maps.ImageResolver"""
 
    @staticmethod
    def _wrap(java_value: _ImageResolver) -> 'ImageResolver':
        return ImageResolver(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ImageResolver):
        """
        Dynamic initializer for ImageResolver.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ImageResolver__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ImageResolver__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getImage(self, arg0: str):
        """public abstract com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.ImageResolver.getImage(java.lang.String)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.maps.Map
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.maps.MapLayers as _MapLayers
_MapLayers = _MapLayers
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.maps.Map as _Map
_Map = _Map
import com.badlogic.gdx.maps.MapProperties as _MapProperties
_MapProperties = _MapProperties
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Map():
    """com.badlogic.gdx.maps.Map"""
 
    @staticmethod
    def _wrap(java_value: _Map) -> 'Map':
        return Map(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Map):
        """
        Dynamic initializer for Map.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Map__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Map__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.Map()"""
        val = _Map()
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

    @overload
    def getProperties(self) -> 'MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.Map.getProperties()"""
        return 'MapProperties'._wrap(super(Map, self).getProperties())

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

    @overload
    def getLayers(self) -> 'MapLayers':
        """public com.badlogic.gdx.maps.MapLayers com.badlogic.gdx.maps.Map.getLayers()"""
        return 'MapLayers'._wrap(super(Map, self).getLayers())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.maps.Map.dispose()"""
        super(Map, self).dispose()

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.Map()"""
        val = _Map()
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.maps.MapLayer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.maps.MapObjects as _MapObjects
_MapObjects = _MapObjects
import java.lang.String as _string
import com.badlogic.gdx.maps.MapLayer as _MapLayer
_MapLayer = _MapLayer
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.maps.MapProperties as _MapProperties
_MapProperties = _MapProperties
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MapLayer():
    """com.badlogic.gdx.maps.MapLayer"""
 
    @staticmethod
    def _wrap(java_value: _MapLayer) -> 'MapLayer':
        return MapLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MapLayer):
        """
        Dynamic initializer for MapLayer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MapLayer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MapLayer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setOpacity(float)"""
        super(_MapLayer, self).setOpacity(_float.valueOf(arg0))

    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.MapLayer.getName()"""
        return str._wrap(super(MapLayer, self).getName())

    @overload
    def getOffsetX(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getOffsetX()"""
        return float._wrap(super(MapLayer, self).getOffsetX())

    @overload
    def getObjects(self) -> 'MapObjects':
        """public com.badlogic.gdx.maps.MapObjects com.badlogic.gdx.maps.MapLayer.getObjects()"""
        return 'MapObjects'._wrap(super(MapLayer, self).getObjects())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getProperties(self) -> 'MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.MapLayer.getProperties()"""
        return 'MapProperties'._wrap(super(MapLayer, self).getProperties())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.MapLayer()"""
        val = _MapLayer()
        self.__wrapper = val

    @overload
    def setOffsetX(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setOffsetX(float)"""
        super(_MapLayer, self).setOffsetX(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.MapLayer()"""
        val = _MapLayer()
        self.__wrapper = val

    @overload
    def getParallaxX(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getParallaxX()"""
        return float._wrap(super(MapLayer, self).getParallaxX())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getRenderOffsetX(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getRenderOffsetX()"""
        return float._wrap(super(MapLayer, self).getRenderOffsetX())

    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.maps.MapLayer.setVisible(boolean)"""
        super(_MapLayer, self).setVisible(_boolean.valueOf(arg0))

    @overload
    def setParallaxX(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setParallaxX(float)"""
        super(_MapLayer, self).setParallaxX(_float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setOffsetY(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setOffsetY(float)"""
        super(_MapLayer, self).setOffsetY(_float.valueOf(arg0))

    @overload
    def setParallaxY(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setParallaxY(float)"""
        super(_MapLayer, self).setParallaxY(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getOpacity(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getOpacity()"""
        return float._wrap(super(MapLayer, self).getOpacity())

    @overload
    def getOffsetY(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getOffsetY()"""
        return float._wrap(super(MapLayer, self).getOffsetY())

    @overload
    def getParent(self) -> 'MapLayer':
        """public com.badlogic.gdx.maps.MapLayer com.badlogic.gdx.maps.MapLayer.getParent()"""
        return 'MapLayer'._wrap(super(MapLayer, self).getParent())

    @overload
    def getRenderOffsetY(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getRenderOffsetY()"""
        return float._wrap(super(MapLayer, self).getRenderOffsetY())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.maps.MapLayer.isVisible()"""
        return bool._wrap(super(MapLayer, self).isVisible())

    @overload
    def invalidateRenderOffset(self):
        """public void com.badlogic.gdx.maps.MapLayer.invalidateRenderOffset()"""
        super(MapLayer, self).invalidateRenderOffset()

    @overload
    def setParent(self, arg0: 'MapLayer'):
        """public void com.badlogic.gdx.maps.MapLayer.setParent(com.badlogic.gdx.maps.MapLayer)"""
        super(_MapLayer, self).setParent(arg0)

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
    def getParallaxY(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getParallaxY()"""
        return float._wrap(super(MapLayer, self).getParallaxY())

    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapLayer.setName(java.lang.String)"""
        super(_MapLayer, self).setName(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.maps.MapObject
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.maps.MapObject as _MapObject
_MapObject = _MapObject
import com.badlogic.gdx.maps.MapProperties as _MapProperties
_MapProperties = _MapProperties
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MapObject():
    """com.badlogic.gdx.maps.MapObject"""
 
    @staticmethod
    def _wrap(java_value: _MapObject) -> 'MapObject':
        return MapObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MapObject):
        """
        Dynamic initializer for MapObject.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MapObject__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MapObject__wrapper":
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
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapObject.setOpacity(float)"""
        super(_MapObject, self).setOpacity(_float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.MapObject()"""
        val = _MapObject()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.MapObject()"""
        val = _MapObject()
        self.__wrapper = val

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
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.maps.MapObject.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_MapObject, self).setColor(arg0)

    @overload
    def getOpacity(self) -> float:
        """public float com.badlogic.gdx.maps.MapObject.getOpacity()"""
        return float._wrap(super(MapObject, self).getOpacity())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getProperties(self) -> 'MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.MapObject.getProperties()"""
        return 'MapProperties'._wrap(super(MapObject, self).getProperties())

    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.maps.MapObject.isVisible()"""
        return bool._wrap(super(MapObject, self).isVisible())

    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapObject.setName(java.lang.String)"""
        super(_MapObject, self).setName(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.MapObject.getName()"""
        return str._wrap(super(MapObject, self).getName())

    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.maps.MapObject.setVisible(boolean)"""
        super(_MapObject, self).setVisible(_boolean.valueOf(arg0))

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.maps.MapObject.getColor()"""
        return 'graphics.Color'._wrap(super(MapObject, self).getColor())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.maps.ImageResolver$TextureAtlasImageResolver
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
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.maps.ImageResolver as _ImageResolver_TextureAtlasImageResolver
_TextureAtlasImageResolver = _ImageResolver_TextureAtlasImageResolver.TextureAtlasImageResolver
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextureAtlasImageResolver():
    """com.badlogic.gdx.maps.ImageResolver.TextureAtlasImageResolver"""
 
    @staticmethod
    def _wrap(java_value: _TextureAtlasImageResolver) -> 'TextureAtlasImageResolver':
        return TextureAtlasImageResolver(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureAtlasImageResolver):
        """
        Dynamic initializer for TextureAtlasImageResolver.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureAtlasImageResolver__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureAtlasImageResolver__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getImage(self, arg0: str) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.ImageResolver$TextureAtlasImageResolver.getImage(java.lang.String)"""
        return 'g2d.TextureRegion'._wrap(super(_TextureAtlasImageResolver, self).getImage(arg0))

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
    def __init__(self, arg0: 'TextureAtlas'):
        """public com.badlogic.gdx.maps.ImageResolver$TextureAtlasImageResolver(com.badlogic.gdx.graphics.g2d.TextureAtlas)"""
        val = _TextureAtlasImageResolver(arg0)
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
 
 
# CLASS: com.badlogic.gdx.maps.MapRenderer
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.maps.MapRenderer as _MapRenderer
_MapRenderer = _MapRenderer
from abc import abstractmethod, ABC
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import int
 
class MapRenderer():
    """com.badlogic.gdx.maps.MapRenderer"""
 
    @staticmethod
    def _wrap(java_value: _MapRenderer) -> 'MapRenderer':
        return MapRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MapRenderer):
        """
        Dynamic initializer for MapRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MapRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MapRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def setView(self, arg0: 'Matrix4', arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.maps.MapRenderer.setView(com.badlogic.gdx.math.Matrix4,float,float,float,float)"""
        pass

    @abstractmethod
    def render(self, arg0: 'int'):
        """public abstract void com.badlogic.gdx.maps.MapRenderer.render(int[])"""
        pass

    @abstractmethod
    def setView(self, arg0: 'OrthographicCamera'):
        """public abstract void com.badlogic.gdx.maps.MapRenderer.setView(com.badlogic.gdx.graphics.OrthographicCamera)"""
        pass

    @abstractmethod
    def render(self, ):
        """public abstract void com.badlogic.gdx.maps.MapRenderer.render()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.maps.MapGroupLayer
from builtins import str
import com.badlogic.gdx.maps.MapGroupLayer as _MapGroupLayer
_MapGroupLayer = _MapGroupLayer
from pyquantum_helper import override
import com.badlogic.gdx.maps.MapLayers as _MapLayers
_MapLayers = _MapLayers
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.maps.MapObjects as _MapObjects
_MapObjects = _MapObjects
import java.lang.String as _string
import com.badlogic.gdx.maps.MapLayer as _MapLayer
_MapLayer = _MapLayer
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.maps.MapProperties as _MapProperties
_MapProperties = _MapProperties
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MapGroupLayer():
    """com.badlogic.gdx.maps.MapGroupLayer"""
 
    @staticmethod
    def _wrap(java_value: _MapGroupLayer) -> 'MapGroupLayer':
        return MapGroupLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MapGroupLayer):
        """
        Dynamic initializer for MapGroupLayer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MapGroupLayer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MapGroupLayer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.maps.MapLayer.isVisible()"""
        return bool._wrap(super(MapLayer, self).isVisible())

    @override
    @overload
    def setOffsetX(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setOffsetX(float)"""
        super(_MapLayer, self).setOffsetX(_float.valueOf(arg0))

    @override
    @overload
    def getRenderOffsetX(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getRenderOffsetX()"""
        return float._wrap(super(MapLayer, self).getRenderOffsetX())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.MapGroupLayer()"""
        val = _MapGroupLayer()
        self.__wrapper = val

    @override
    @overload
    def getParent(self) -> 'MapLayer':
        """public com.badlogic.gdx.maps.MapLayer com.badlogic.gdx.maps.MapLayer.getParent()"""
        return 'MapLayer'._wrap(super(MapLayer, self).getParent())

    @override
    @overload
    def setParent(self, arg0: 'MapLayer'):
        """public void com.badlogic.gdx.maps.MapLayer.setParent(com.badlogic.gdx.maps.MapLayer)"""
        super(_MapLayer, self).setParent(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getParallaxX(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getParallaxX()"""
        return float._wrap(super(MapLayer, self).getParallaxX())

    @override
    @overload
    def getObjects(self) -> 'MapObjects':
        """public com.badlogic.gdx.maps.MapObjects com.badlogic.gdx.maps.MapLayer.getObjects()"""
        return 'MapObjects'._wrap(super(MapLayer, self).getObjects())

    @override
    @overload
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setOpacity(float)"""
        super(_MapLayer, self).setOpacity(_float.valueOf(arg0))

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
    def getRenderOffsetY(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getRenderOffsetY()"""
        return float._wrap(super(MapLayer, self).getRenderOffsetY())

    @override
    @overload
    def getOffsetX(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getOffsetX()"""
        return float._wrap(super(MapLayer, self).getOffsetX())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getProperties(self) -> 'MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.MapLayer.getProperties()"""
        return 'MapProperties'._wrap(super(MapLayer, self).getProperties())

    @override
    @overload
    def setParallaxX(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setParallaxX(float)"""
        super(_MapLayer, self).setParallaxX(_float.valueOf(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.MapLayer.getName()"""
        return str._wrap(super(MapLayer, self).getName())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.MapGroupLayer()"""
        val = _MapGroupLayer()
        self.__wrapper = val

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapLayer.setName(java.lang.String)"""
        super(_MapLayer, self).setName(arg0)

    @override
    @overload
    def getParallaxY(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getParallaxY()"""
        return float._wrap(super(MapLayer, self).getParallaxY())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getLayers(self) -> 'MapLayers':
        """public com.badlogic.gdx.maps.MapLayers com.badlogic.gdx.maps.MapGroupLayer.getLayers()"""
        return 'MapLayers'._wrap(super(MapGroupLayer, self).getLayers())

    @override
    @overload
    def getOffsetY(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getOffsetY()"""
        return float._wrap(super(MapLayer, self).getOffsetY())

    @override
    @overload
    def setOffsetY(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setOffsetY(float)"""
        super(_MapLayer, self).setOffsetY(_float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.maps.MapLayer.setVisible(boolean)"""
        super(_MapLayer, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def getOpacity(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getOpacity()"""
        return float._wrap(super(MapLayer, self).getOpacity())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setParallaxY(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setParallaxY(float)"""
        super(_MapLayer, self).setParallaxY(_float.valueOf(arg0))

    @override
    @overload
    def invalidateRenderOffset(self):
        """public void com.badlogic.gdx.maps.MapGroupLayer.invalidateRenderOffset()"""
        super(MapGroupLayer, self).invalidateRenderOffset()

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
 
 
# CLASS: com.badlogic.gdx.maps.MapObjects
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
import com.badlogic.gdx.maps.MapObjects as _MapObjects
_MapObjects = _MapObjects
import java.lang.String as _string
import java.util.Spliterator as Spliterator
import java.lang.Integer as _int
import com.badlogic.gdx.maps.MapObject as _MapObject
_MapObject = _MapObject
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MapObjects():
    """com.badlogic.gdx.maps.MapObjects"""
 
    @staticmethod
    def _wrap(java_value: _MapObjects) -> 'MapObjects':
        return MapObjects(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MapObjects):
        """
        Dynamic initializer for MapObjects.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MapObjects__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MapObjects__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def remove(self, arg0: int):
        """public void com.badlogic.gdx.maps.MapObjects.remove(int)"""
        super(_MapObjects, self).remove(_int.valueOf(arg0))

    @overload
    def remove(self, arg0: 'MapObject'):
        """public void com.badlogic.gdx.maps.MapObjects.remove(com.badlogic.gdx.maps.MapObject)"""
        super(_MapObjects, self).remove(arg0)

    @overload
    def getCount(self) -> int:
        """public int com.badlogic.gdx.maps.MapObjects.getCount()"""
        return int._wrap(super(MapObjects, self).getCount())

    @overload
    def get(self, arg0: str) -> 'MapObject':
        """public com.badlogic.gdx.maps.MapObject com.badlogic.gdx.maps.MapObjects.get(java.lang.String)"""
        return 'MapObject'._wrap(super(_MapObjects, self).get(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.MapObjects()"""
        val = _MapObjects()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def get(self, arg0: int) -> 'MapObject':
        """public com.badlogic.gdx.maps.MapObject com.badlogic.gdx.maps.MapObjects.get(int)"""
        return 'MapObject'._wrap(super(_MapObjects, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<com.badlogic.gdx.maps.MapObject> com.badlogic.gdx.maps.MapObjects.iterator()"""
        return 'Iterator'._wrap(super(MapObjects, self).iterator())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getIndex(self, arg0: str) -> int:
        """public int com.badlogic.gdx.maps.MapObjects.getIndex(java.lang.String)"""
        return int._wrap(super(_MapObjects, self).getIndex(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getByType(self, arg0: 'Class', arg1: 'Array') -> 'utils.Array':
        """public <T extends com.badlogic.gdx.maps.MapObject> com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.maps.MapObjects.getByType(java.lang.Class<T>,com.badlogic.gdx.utils.Array<T>)"""
        return 'utils.Array'._wrap(super(_MapObjects, self).getByType(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getIndex(self, arg0: 'MapObject') -> int:
        """public int com.badlogic.gdx.maps.MapObjects.getIndex(com.badlogic.gdx.maps.MapObject)"""
        return int._wrap(super(_MapObjects, self).getIndex(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def add(self, arg0: 'MapObject'):
        """public void com.badlogic.gdx.maps.MapObjects.add(com.badlogic.gdx.maps.MapObject)"""
        super(_MapObjects, self).add(arg0)

    @overload
    def getByType(self, arg0: 'Class') -> 'utils.Array':
        """public <T extends com.badlogic.gdx.maps.MapObject> com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.maps.MapObjects.getByType(java.lang.Class<T>)"""
        return 'utils.Array'._wrap(super(_MapObjects, self).getByType(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.MapObjects()"""
        val = _MapObjects()
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