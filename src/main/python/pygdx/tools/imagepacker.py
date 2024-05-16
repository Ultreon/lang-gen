from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.tools.imagepacker.ImagePacker as _ImagePacker
_ImagePacker = _ImagePacker
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.awt.image.BufferedImage as _BufferedImage
_BufferedImage = _BufferedImage
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.awt.image.BufferedImage as BufferedImage
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ImagePacker():
    """com.badlogic.gdx.tools.imagepacker.ImagePacker"""
 
    @staticmethod
    def _wrap(java_value: _ImagePacker) -> 'ImagePacker':
        return ImagePacker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ImagePacker):
        """
        Dynamic initializer for ImagePacker.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ImagePacker__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ImagePacker__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getImage(self) -> 'BufferedImage':
        """public java.awt.image.BufferedImage com.badlogic.gdx.tools.imagepacker.ImagePacker.getImage()"""
        return 'BufferedImage'._wrap(super(ImagePacker, self).getImage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: bool):
        """public com.badlogic.gdx.tools.imagepacker.ImagePacker(int,int,int,boolean)"""
        val = _ImagePacker(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void com.badlogic.gdx.tools.imagepacker.ImagePacker.main(java.lang.String[]) throws java.io.IOException"""
        _ImagePacker.main(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def insertImage(self, arg0: str, arg1: 'BufferedImage'):
        """public void com.badlogic.gdx.tools.imagepacker.ImagePacker.insertImage(java.lang.String,java.awt.image.BufferedImage)"""
        super(_ImagePacker, self).insertImage(arg0, arg1)

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
    def getRects(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.awt.Rectangle> com.badlogic.gdx.tools.imagepacker.ImagePacker.getRects()"""
        return 'Map'._wrap(super(ImagePacker, self).getRects())

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

 
 
 
# CLASS: com.badlogic.gdx.tools.imagepacker.ImagePacker
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.tools.imagepacker.ImagePacker as _ImagePacker
_ImagePacker = _ImagePacker
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.awt.image.BufferedImage as _BufferedImage
_BufferedImage = _BufferedImage
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.awt.image.BufferedImage as BufferedImage
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ImagePacker():
    """com.badlogic.gdx.tools.imagepacker.ImagePacker"""
 
    @staticmethod
    def _wrap(java_value: _ImagePacker) -> 'ImagePacker':
        return ImagePacker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ImagePacker):
        """
        Dynamic initializer for ImagePacker.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ImagePacker__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ImagePacker__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getImage(self) -> 'BufferedImage':
        """public java.awt.image.BufferedImage com.badlogic.gdx.tools.imagepacker.ImagePacker.getImage()"""
        return 'BufferedImage'._wrap(super(ImagePacker, self).getImage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: bool):
        """public com.badlogic.gdx.tools.imagepacker.ImagePacker(int,int,int,boolean)"""
        val = _ImagePacker(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void com.badlogic.gdx.tools.imagepacker.ImagePacker.main(java.lang.String[]) throws java.io.IOException"""
        _ImagePacker.main(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def insertImage(self, arg0: str, arg1: 'BufferedImage'):
        """public void com.badlogic.gdx.tools.imagepacker.ImagePacker.insertImage(java.lang.String,java.awt.image.BufferedImage)"""
        super(_ImagePacker, self).insertImage(arg0, arg1)

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
    def getRects(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.awt.Rectangle> com.badlogic.gdx.tools.imagepacker.ImagePacker.getRects()"""
        return 'Map'._wrap(super(ImagePacker, self).getRects())

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

 
 
 
# CLASS: com.badlogic.gdx.tools.imagepacker.ImagePacker