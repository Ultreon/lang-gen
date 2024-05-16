from __future__ import annotations
from overload import overload


 
from builtins import str
import com.badlogic.gdx.tools.imagepacker.ImagePacker as __ImagePacker
__ImagePacker = __ImagePacker
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.awt.image.BufferedImage as __BufferedImage
__BufferedImage = __BufferedImage
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.awt.image.BufferedImage as BufferedImage
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class ImagePacker():
    """com.badlogic.gdx.tools.imagepacker.ImagePacker"""
 
    @staticmethod
    def __wrap(java_value: __ImagePacker) -> 'ImagePacker':
        return ImagePacker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ImagePacker):
        """
        Dynamic initializer for ImagePacker.
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
    def getRects(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.awt.Rectangle> com.badlogic.gdx.tools.imagepacker.ImagePacker.getRects()"""
        return 'Map'.__wrap(super(ImagePacker, self).getRects())

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
    def insertImage(self, arg0: str, arg1: 'BufferedImage'):
        """public void com.badlogic.gdx.tools.imagepacker.ImagePacker.insertImage(java.lang.String,java.awt.image.BufferedImage)"""
        super(__ImagePacker, self).insertImage(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: bool):
        """public com.badlogic.gdx.tools.imagepacker.ImagePacker(int,int,int,boolean)"""
        val = __ImagePacker(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getImage(self) -> 'BufferedImage':
        """public java.awt.image.BufferedImage com.badlogic.gdx.tools.imagepacker.ImagePacker.getImage()"""
        return 'BufferedImage'.__wrap(super(ImagePacker, self).getImage())

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
    def main(arg0: 'String'):
        """public static void com.badlogic.gdx.tools.imagepacker.ImagePacker.main(java.lang.String[]) throws java.io.IOException"""
        __ImagePacker.main(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.tools.imagepacker.ImagePacker
from builtins import str
import com.badlogic.gdx.tools.imagepacker.ImagePacker as __ImagePacker
__ImagePacker = __ImagePacker
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.awt.image.BufferedImage as __BufferedImage
__BufferedImage = __BufferedImage
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.awt.image.BufferedImage as BufferedImage
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class ImagePacker():
    """com.badlogic.gdx.tools.imagepacker.ImagePacker"""
 
    @staticmethod
    def __wrap(java_value: __ImagePacker) -> 'ImagePacker':
        return ImagePacker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ImagePacker):
        """
        Dynamic initializer for ImagePacker.
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
    def getRects(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.awt.Rectangle> com.badlogic.gdx.tools.imagepacker.ImagePacker.getRects()"""
        return 'Map'.__wrap(super(ImagePacker, self).getRects())

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
    def insertImage(self, arg0: str, arg1: 'BufferedImage'):
        """public void com.badlogic.gdx.tools.imagepacker.ImagePacker.insertImage(java.lang.String,java.awt.image.BufferedImage)"""
        super(__ImagePacker, self).insertImage(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: bool):
        """public com.badlogic.gdx.tools.imagepacker.ImagePacker(int,int,int,boolean)"""
        val = __ImagePacker(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getImage(self) -> 'BufferedImage':
        """public java.awt.image.BufferedImage com.badlogic.gdx.tools.imagepacker.ImagePacker.getImage()"""
        return 'BufferedImage'.__wrap(super(ImagePacker, self).getImage())

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
    def main(arg0: 'String'):
        """public static void com.badlogic.gdx.tools.imagepacker.ImagePacker.main(java.lang.String[]) throws java.io.IOException"""
        __ImagePacker.main(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.tools.imagepacker.ImagePacker