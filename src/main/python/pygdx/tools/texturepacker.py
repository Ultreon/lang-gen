from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.File as File
from builtins import float
import com.badlogic.gdx.tools.texturepacker.TexturePacker as __TexturePacker_Rect
__Rect = __TexturePacker_Rect.Rect
import com.badlogic.gdx.tools.texturepacker.TexturePacker as __TexturePacker_Settings
__Settings = __TexturePacker_Settings.Settings
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.awt.image.BufferedImage as BufferedImage
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.tools.texturepacker.ImageProcessor as __ImageProcessor
__ImageProcessor = __ImageProcessor
from builtins import int
 
class ImageProcessor():
    """com.badlogic.gdx.tools.texturepacker.ImageProcessor"""
 
    @staticmethod
    def __wrap(java_value: __ImageProcessor) -> 'ImageProcessor':
        return ImageProcessor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ImageProcessor):
        """
        Dynamic initializer for ImageProcessor.
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
    def getScale(self) -> float:
        """public float com.badlogic.gdx.tools.texturepacker.ImageProcessor.getScale()"""
        return float.__wrap(super(ImageProcessor, self).getScale())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.tools.texturepacker.ImageProcessor.setScale(float)"""
        super(__ImageProcessor, self).setScale(__float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getImages(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect> com.badlogic.gdx.tools.texturepacker.ImageProcessor.getImages()"""
        return 'utils.Array'.__wrap(super(ImageProcessor, self).getImages())

    @overload
    def getSettings(self) -> 'Settings':
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings com.badlogic.gdx.tools.texturepacker.ImageProcessor.getSettings()"""
        return 'Settings'.__wrap(super(ImageProcessor, self).getSettings())

    @overload
    def clear(self):
        """public void com.badlogic.gdx.tools.texturepacker.ImageProcessor.clear()"""
        super(ImageProcessor, self).clear()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setResampling(self, arg0: 'Resampling'):
        """public void com.badlogic.gdx.tools.texturepacker.ImageProcessor.setResampling(com.badlogic.gdx.tools.texturepacker.TexturePacker$Resampling)"""
        super(__ImageProcessor, self).setResampling(arg0)

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
    def addImage(self, arg0: 'File', arg1: str) -> 'Rect':
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect com.badlogic.gdx.tools.texturepacker.ImageProcessor.addImage(java.io.File,java.lang.String)"""
        return 'Rect'.__wrap(super(__ImageProcessor, self).addImage(arg0, arg1))

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
    def addImage(self, arg0: 'BufferedImage', arg1: str) -> 'Rect':
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect com.badlogic.gdx.tools.texturepacker.ImageProcessor.addImage(java.awt.image.BufferedImage,java.lang.String)"""
        return 'Rect'.__wrap(super(__ImageProcessor, self).addImage(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Settings'):
        """public com.badlogic.gdx.tools.texturepacker.ImageProcessor(com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings)"""
        val = __ImageProcessor(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.ImageProcessor
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.File as File
from builtins import float
import com.badlogic.gdx.tools.texturepacker.TexturePacker as __TexturePacker_Rect
__Rect = __TexturePacker_Rect.Rect
import com.badlogic.gdx.tools.texturepacker.TexturePacker as __TexturePacker_Settings
__Settings = __TexturePacker_Settings.Settings
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.awt.image.BufferedImage as BufferedImage
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.tools.texturepacker.ImageProcessor as __ImageProcessor
__ImageProcessor = __ImageProcessor
from builtins import int
 
class ImageProcessor():
    """com.badlogic.gdx.tools.texturepacker.ImageProcessor"""
 
    @staticmethod
    def __wrap(java_value: __ImageProcessor) -> 'ImageProcessor':
        return ImageProcessor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ImageProcessor):
        """
        Dynamic initializer for ImageProcessor.
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
    def getScale(self) -> float:
        """public float com.badlogic.gdx.tools.texturepacker.ImageProcessor.getScale()"""
        return float.__wrap(super(ImageProcessor, self).getScale())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.tools.texturepacker.ImageProcessor.setScale(float)"""
        super(__ImageProcessor, self).setScale(__float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getImages(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect> com.badlogic.gdx.tools.texturepacker.ImageProcessor.getImages()"""
        return 'utils.Array'.__wrap(super(ImageProcessor, self).getImages())

    @overload
    def getSettings(self) -> 'Settings':
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings com.badlogic.gdx.tools.texturepacker.ImageProcessor.getSettings()"""
        return 'Settings'.__wrap(super(ImageProcessor, self).getSettings())

    @overload
    def clear(self):
        """public void com.badlogic.gdx.tools.texturepacker.ImageProcessor.clear()"""
        super(ImageProcessor, self).clear()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setResampling(self, arg0: 'Resampling'):
        """public void com.badlogic.gdx.tools.texturepacker.ImageProcessor.setResampling(com.badlogic.gdx.tools.texturepacker.TexturePacker$Resampling)"""
        super(__ImageProcessor, self).setResampling(arg0)

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
    def addImage(self, arg0: 'File', arg1: str) -> 'Rect':
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect com.badlogic.gdx.tools.texturepacker.ImageProcessor.addImage(java.io.File,java.lang.String)"""
        return 'Rect'.__wrap(super(__ImageProcessor, self).addImage(arg0, arg1))

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
    def addImage(self, arg0: 'BufferedImage', arg1: str) -> 'Rect':
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect com.badlogic.gdx.tools.texturepacker.ImageProcessor.addImage(java.awt.image.BufferedImage,java.lang.String)"""
        return 'Rect'.__wrap(super(__ImageProcessor, self).addImage(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Settings'):
        """public com.badlogic.gdx.tools.texturepacker.ImageProcessor(com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings)"""
        val = __ImageProcessor(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.ImageProcessor 
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.TexturePackerUpscaleTest
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.tools.texturepacker.TexturePackerUpscaleTest as __TexturePackerUpscaleTest
__TexturePackerUpscaleTest = __TexturePackerUpscaleTest
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TexturePackerUpscaleTest():
    """com.badlogic.gdx.tools.texturepacker.TexturePackerUpscaleTest"""
 
    @staticmethod
    def __wrap(java_value: __TexturePackerUpscaleTest) -> 'TexturePackerUpscaleTest':
        return TexturePackerUpscaleTest(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TexturePackerUpscaleTest):
        """
        Dynamic initializer for TexturePackerUpscaleTest.
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
    def __init__(self):
        """public com.badlogic.gdx.tools.texturepacker.TexturePackerUpscaleTest()"""
        val = __TexturePackerUpscaleTest()
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

    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void com.badlogic.gdx.tools.texturepacker.TexturePackerUpscaleTest.main(java.lang.String[])"""
        __TexturePackerUpscaleTest.main(arg0)

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
    def __init__(self, ):
        """public com.badlogic.gdx.tools.texturepacker.TexturePackerUpscaleTest()"""
        val = __TexturePackerUpscaleTest()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.TexturePacker$Resampling
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
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
import com.badlogic.gdx.tools.texturepacker.TexturePacker as __TexturePacker_Resampling
__Resampling = __TexturePacker_Resampling.Resampling
from builtins import int
 
class Resampling():
    """com.badlogic.gdx.tools.texturepacker.TexturePacker.Resampling"""
 
    @staticmethod
    def __wrap(java_value: __Resampling) -> 'Resampling':
        return Resampling(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Resampling):
        """
        Dynamic initializer for Resampling.
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
    def valueOf(arg0: str) -> 'Resampling':
        """public static com.badlogic.gdx.tools.texturepacker.TexturePacker$Resampling com.badlogic.gdx.tools.texturepacker.TexturePacker$Resampling.valueOf(java.lang.String)"""
        return Resampling.__wrap(__Resampling.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def values() -> List['Resampling']:
        """public static com.badlogic.gdx.tools.texturepacker.TexturePacker$Resampling[] com.badlogic.gdx.tools.texturepacker.TexturePacker$Resampling.values()"""
        return List[Resampling].__wrap(__Resampling.values())

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
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.MaxRectsPacker
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.tools.texturepacker.MaxRectsPacker as __MaxRectsPacker
__MaxRectsPacker = __MaxRectsPacker
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MaxRectsPacker():
    """com.badlogic.gdx.tools.texturepacker.MaxRectsPacker"""
 
    @staticmethod
    def __wrap(java_value: __MaxRectsPacker) -> 'MaxRectsPacker':
        return MaxRectsPacker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MaxRectsPacker):
        """
        Dynamic initializer for MaxRectsPacker.
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
    def pack(self, arg0: 'ProgressListener', arg1: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Page> com.badlogic.gdx.tools.texturepacker.MaxRectsPacker.pack(com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener,com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect>)"""
        return 'utils.Array'.__wrap(super(__MaxRectsPacker, self).pack(arg0, arg1))

    @overload
    def pack(self, arg0: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Page> com.badlogic.gdx.tools.texturepacker.MaxRectsPacker.pack(com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect>)"""
        return 'utils.Array'.__wrap(super(__MaxRectsPacker, self).pack(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Settings'):
        """public com.badlogic.gdx.tools.texturepacker.MaxRectsPacker(com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings)"""
        val = __MaxRectsPacker(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.tools.texturepacker.TexturePacker as __TexturePacker_Settings
__Settings = __TexturePacker_Settings.Settings
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
 
class Settings():
    """com.badlogic.gdx.tools.texturepacker.TexturePacker.Settings"""
 
    @staticmethod
    def __wrap(java_value: __Settings) -> 'Settings':
        return Settings(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Settings):
        """
        Dynamic initializer for Settings.
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
    def __init__(self, arg0: 'Settings'):
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings(com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings)"""
        val = __Settings(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: 'Settings'):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings.set(com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings)"""
        super(__Settings, self).set(arg0)

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
    def __init__(self, ):
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings()"""
        val = __Settings()
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
    def getScaledPackFileName(self, arg0: str, arg1: int) -> str:
        """public java.lang.String com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings.getScaledPackFileName(java.lang.String,int)"""
        return str.__wrap(super(__Settings, self).getScaledPackFileName(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings()"""
        val = __Settings()
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
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.TexturePackerFileProcessor
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import com.badlogic.gdx.tools.texturepacker.TexturePacker as __TexturePacker_ProgressListener
__ProgressListener = __TexturePacker_ProgressListener.ProgressListener
import java.lang.Object as __object
from builtins import type
import java.io.File as File
try:
    from pygdx import tools
except ImportError:
    tools = __import_once__("pygdx.tools")

import com.badlogic.gdx.tools.FileProcessor as __FileProcessor
__FileProcessor = __FileProcessor
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.util.ArrayList as ArrayList
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.io.FilenameFilter as FilenameFilter
import java.util.ArrayList as __ArrayList
__ArrayList = __ArrayList
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.tools.texturepacker.TexturePackerFileProcessor as __TexturePackerFileProcessor
__TexturePackerFileProcessor = __TexturePackerFileProcessor
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TexturePackerFileProcessor():
    """com.badlogic.gdx.tools.texturepacker.TexturePackerFileProcessor"""
 
    @staticmethod
    def __wrap(java_value: __TexturePackerFileProcessor) -> 'TexturePackerFileProcessor':
        return TexturePackerFileProcessor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TexturePackerFileProcessor):
        """
        Dynamic initializer for TexturePackerFileProcessor.
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
    def process(self, arg0: 'File', arg1: 'File') -> 'ArrayList':
        """public java.util.ArrayList<com.badlogic.gdx.tools.FileProcessor$Entry> com.badlogic.gdx.tools.texturepacker.TexturePackerFileProcessor.process(java.io.File,java.io.File) throws java.lang.Exception"""
        return 'ArrayList'.__wrap(super(__TexturePackerFileProcessor, self).process(arg0, arg1))

    @overload
    def __init__(self, arg0: 'Settings', arg1: str, arg2: 'ProgressListener'):
        """public com.badlogic.gdx.tools.texturepacker.TexturePackerFileProcessor(com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings,java.lang.String,com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener)"""
        val = __TexturePackerFileProcessor(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def process(self, arg0: str, arg1: str) -> 'ArrayList':
        """public java.util.ArrayList<com.badlogic.gdx.tools.FileProcessor$Entry> com.badlogic.gdx.tools.FileProcessor.process(java.lang.String,java.lang.String) throws java.lang.Exception"""
        return 'ArrayList'.__wrap(super(__tools.FileProcessor, self).process(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.texturepacker.TexturePackerFileProcessor()"""
        val = __TexturePackerFileProcessor()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setInputFilter(self, arg0: 'FilenameFilter') -> 'tools.FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.setInputFilter(java.io.FilenameFilter)"""
        return 'tools.FileProcessor'.__wrap(super(__tools.FileProcessor, self).setInputFilter(arg0))

    @overload
    def addInputRegex(self, *arg0: str) -> 'tools.FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.addInputRegex(java.lang.String...)"""
        return 'tools.FileProcessor'.__wrap(super(__tools.FileProcessor, self).addInputRegex(arg0))

    @overload
    def addInputSuffix(self, *arg0: str) -> 'tools.FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.addInputSuffix(java.lang.String...)"""
        return 'tools.FileProcessor'.__wrap(super(__tools.FileProcessor, self).addInputSuffix(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.texturepacker.TexturePackerFileProcessor()"""
        val = __TexturePackerFileProcessor()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setFlattenOutput(self, arg0: bool) -> 'tools.FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.setFlattenOutput(boolean)"""
        return 'tools.FileProcessor'.__wrap(super(__tools.FileProcessor, self).setFlattenOutput(__boolean.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getProgressListener(self) -> 'ProgressListener':
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener com.badlogic.gdx.tools.texturepacker.TexturePackerFileProcessor.getProgressListener()"""
        return 'ProgressListener'.__wrap(super(TexturePackerFileProcessor, self).getProgressListener())

    @overload
    def setComparator(self, arg0: 'Comparator') -> 'tools.FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.setComparator(java.util.Comparator<java.io.File>)"""
        return 'tools.FileProcessor'.__wrap(super(__tools.FileProcessor, self).setComparator(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setRecursive(self, arg0: bool) -> 'tools.FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.setRecursive(boolean)"""
        return 'tools.FileProcessor'.__wrap(super(__tools.FileProcessor, self).setRecursive(__boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setOutputSuffix(self, arg0: str) -> 'tools.FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.setOutputSuffix(java.lang.String)"""
        return 'tools.FileProcessor'.__wrap(super(__tools.FileProcessor, self).setOutputSuffix(arg0))

    @overload
    def process(self, arg0: 'File', arg1: 'File') -> 'ArrayList':
        """public java.util.ArrayList<com.badlogic.gdx.tools.FileProcessor$Entry> com.badlogic.gdx.tools.texturepacker.TexturePackerFileProcessor.process(java.io.File[],java.io.File) throws java.lang.Exception"""
        return 'ArrayList'.__wrap(super(__TexturePackerFileProcessor, self).process(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.TexturePacker$Packer
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import com.badlogic.gdx.tools.texturepacker.TexturePacker as __TexturePacker_Packer
__Packer = __TexturePacker_Packer.Packer
from abc import abstractmethod, ABC
 
class Packer(ABC):
    """com.badlogic.gdx.tools.texturepacker.TexturePacker.Packer"""
 
    @staticmethod
    def __wrap(java_value: __Packer) -> 'Packer':
        return Packer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Packer):
        """
        Dynamic initializer for Packer.
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
    def pack(self, arg0: 'Array'):
        """public abstract com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Page> com.badlogic.gdx.tools.texturepacker.TexturePacker$Packer.pack(com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect>)"""
        pass

    @abstractmethod
    def pack(self, arg0: 'ProgressListener', arg1: 'Array'):
        """public abstract com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Page> com.badlogic.gdx.tools.texturepacker.TexturePacker$Packer.pack(com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener,com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect>)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.TexturePacker$Alias
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
import com.badlogic.gdx.tools.texturepacker.TexturePacker as __TexturePacker_Alias
__Alias = __TexturePacker_Alias.Alias
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Alias():
    """com.badlogic.gdx.tools.texturepacker.TexturePacker.Alias"""
 
    @staticmethod
    def __wrap(java_value: __Alias) -> 'Alias':
        return Alias(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Alias):
        """
        Dynamic initializer for Alias.
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
    def apply(self, arg0: 'Rect'):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker$Alias.apply(com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect)"""
        super(__Alias, self).apply(arg0)

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
    def __init__(self, arg0: 'Rect'):
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$Alias(com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect)"""
        val = __Alias(arg0)
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

    @overload
    def compareTo(self, arg0: 'Alias') -> int:
        """public int com.badlogic.gdx.tools.texturepacker.TexturePacker$Alias.compareTo(com.badlogic.gdx.tools.texturepacker.TexturePacker$Alias)"""
        return int.__wrap(super(__Alias, self).compareTo(arg0))

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
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.TexturePackerTest
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.tools.texturepacker.TexturePackerTest as __TexturePackerTest
__TexturePackerTest = __TexturePackerTest
import com.badlogic.gdx.ApplicationAdapter as __ApplicationAdapter
__ApplicationAdapter = __ApplicationAdapter
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
 
class TexturePackerTest():
    """com.badlogic.gdx.tools.texturepacker.TexturePackerTest"""
 
    @staticmethod
    def __wrap(java_value: __TexturePackerTest) -> 'TexturePackerTest':
        return TexturePackerTest(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TexturePackerTest):
        """
        Dynamic initializer for TexturePackerTest.
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
    def main(arg0: 'String'):
        """public static void com.badlogic.gdx.tools.texturepacker.TexturePackerTest.main(java.lang.String[]) throws java.lang.Exception"""
        __TexturePackerTest.main(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.texturepacker.TexturePackerTest()"""
        val = __TexturePackerTest()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePackerTest.resize(int,int)"""
        super(__TexturePackerTest, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def create(self):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePackerTest.create()"""
        super(TexturePackerTest, self).create()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.ApplicationAdapter.dispose()"""
        super(pygdx.ApplicationAdapter, self).dispose()

    @override
    @overload
    def resume(self):
        """public void com.badlogic.gdx.ApplicationAdapter.resume()"""
        super(pygdx.ApplicationAdapter, self).resume()

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
    def render(self):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePackerTest.render()"""
        super(TexturePackerTest, self).render()

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
    def __init__(self):
        """public com.badlogic.gdx.tools.texturepacker.TexturePackerTest()"""
        val = __TexturePackerTest()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def pause(self):
        """public void com.badlogic.gdx.ApplicationAdapter.pause()"""
        super(pygdx.ApplicationAdapter, self).pause()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.TexturePacker$Page
import com.badlogic.gdx.tools.texturepacker.TexturePacker as __TexturePacker_Page
__Page = __TexturePacker_Page.Page
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
 
class Page():
    """com.badlogic.gdx.tools.texturepacker.TexturePacker.Page"""
 
    @staticmethod
    def __wrap(java_value: __Page) -> 'Page':
        return Page(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Page):
        """
        Dynamic initializer for Page.
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
    def __init__(self):
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$Page()"""
        val = __Page()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$Page()"""
        val = __Page()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.tools.texturepacker.TexturePacker as __TexturePacker_ProgressListener
__ProgressListener = __TexturePacker_ProgressListener.ProgressListener
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Float as __float
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
 
class ProgressListener(ABC):
    """com.badlogic.gdx.tools.texturepacker.TexturePacker.ProgressListener"""
 
    @staticmethod
    def __wrap(java_value: __ProgressListener) -> 'ProgressListener':
        return ProgressListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ProgressListener):
        """
        Dynamic initializer for ProgressListener.
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
    def end(self):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.end()"""
        super(ProgressListener, self).end()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getTotal(self) -> int:
        """public int com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.getTotal()"""
        return int.__wrap(super(ProgressListener, self).getTotal())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def update(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.update(int,int)"""
        return bool.__wrap(super(__ProgressListener, self).update(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def update(self, arg0: float):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.update(float)"""
        super(__ProgressListener, self).update(__float.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener()"""
        val = __ProgressListener()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def reset(self):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.reset()"""
        super(ProgressListener, self).reset()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def cancel(self):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.cancel()"""
        super(ProgressListener, self).cancel()

    @overload
    def isCancelled(self) -> bool:
        """public boolean com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.isCancelled()"""
        return bool.__wrap(super(ProgressListener, self).isCancelled())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setCount(self, arg0: int):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.setCount(int)"""
        super(__ProgressListener, self).setCount(__int.valueOf(arg0))

    @overload
    def start(self, arg0: float):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.start(float)"""
        super(__ProgressListener, self).start(__float.valueOf(arg0))

    @overload
    def setTotal(self, arg0: int):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.setTotal(int)"""
        super(__ProgressListener, self).setTotal(__int.valueOf(arg0))

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
    def progress(self, arg0: float):
        """public abstract void com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.progress(float)"""
        pass

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener()"""
        val = __ProgressListener()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getMessage(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.getMessage()"""
        return str.__wrap(super(ProgressListener, self).getMessage())

    @overload
    def getCount(self) -> int:
        """public int com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.getCount()"""
        return int.__wrap(super(ProgressListener, self).getCount())

    @overload
    def setMessage(self, arg0: str):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.setMessage(java.lang.String)"""
        super(__ProgressListener, self).setMessage(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: str):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener.set(java.lang.String)"""
        super(__ProgressListener, self).set(arg0) 
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.ColorBleedEffect
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.tools.texturepacker.ColorBleedEffect as __ColorBleedEffect
__ColorBleedEffect = __ColorBleedEffect
import java.awt.image.BufferedImage as __BufferedImage
__BufferedImage = __BufferedImage
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.awt.image.BufferedImage as BufferedImage
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ColorBleedEffect():
    """com.badlogic.gdx.tools.texturepacker.ColorBleedEffect"""
 
    @staticmethod
    def __wrap(java_value: __ColorBleedEffect) -> 'ColorBleedEffect':
        return ColorBleedEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ColorBleedEffect):
        """
        Dynamic initializer for ColorBleedEffect.
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.texturepacker.ColorBleedEffect()"""
        val = __ColorBleedEffect()
        self.__dict__ = val.__dict__
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.texturepacker.ColorBleedEffect()"""
        val = __ColorBleedEffect()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def processImage(self, arg0: 'BufferedImage', arg1: int) -> 'BufferedImage':
        """public java.awt.image.BufferedImage com.badlogic.gdx.tools.texturepacker.ColorBleedEffect.processImage(java.awt.image.BufferedImage,int)"""
        return 'BufferedImage'.__wrap(super(__ColorBleedEffect, self).processImage(arg0, __int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.GridPacker
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.tools.texturepacker.GridPacker as __GridPacker
__GridPacker = __GridPacker
from builtins import bool
from builtins import int
 
class GridPacker():
    """com.badlogic.gdx.tools.texturepacker.GridPacker"""
 
    @staticmethod
    def __wrap(java_value: __GridPacker) -> 'GridPacker':
        return GridPacker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GridPacker):
        """
        Dynamic initializer for GridPacker.
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
    def pack(self, arg0: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Page> com.badlogic.gdx.tools.texturepacker.GridPacker.pack(com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect>)"""
        return 'utils.Array'.__wrap(super(__GridPacker, self).pack(arg0))

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
    def pack(self, arg0: 'ProgressListener', arg1: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Page> com.badlogic.gdx.tools.texturepacker.GridPacker.pack(com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener,com.badlogic.gdx.utils.Array<com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect>)"""
        return 'utils.Array'.__wrap(super(__GridPacker, self).pack(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Settings'):
        """public com.badlogic.gdx.tools.texturepacker.GridPacker(com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings)"""
        val = __GridPacker(arg0)
        self.__dict__ = val.__dict__
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.MaxRectsPacker$FreeRectChoiceHeuristic
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import com.badlogic.gdx.tools.texturepacker.MaxRectsPacker as __MaxRectsPacker_FreeRectChoiceHeuristic
__FreeRectChoiceHeuristic = __MaxRectsPacker_FreeRectChoiceHeuristic.FreeRectChoiceHeuristic
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
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class FreeRectChoiceHeuristic():
    """com.badlogic.gdx.tools.texturepacker.MaxRectsPacker.FreeRectChoiceHeuristic"""
 
    @staticmethod
    def __wrap(java_value: __FreeRectChoiceHeuristic) -> 'FreeRectChoiceHeuristic':
        return FreeRectChoiceHeuristic(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FreeRectChoiceHeuristic):
        """
        Dynamic initializer for FreeRectChoiceHeuristic.
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'FreeRectChoiceHeuristic':
        """public static com.badlogic.gdx.tools.texturepacker.MaxRectsPacker$FreeRectChoiceHeuristic com.badlogic.gdx.tools.texturepacker.MaxRectsPacker$FreeRectChoiceHeuristic.valueOf(java.lang.String)"""
        return FreeRectChoiceHeuristic.__wrap(__FreeRectChoiceHeuristic.valueOf(arg0))

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
    def values() -> List['FreeRectChoiceHeuristic']:
        """public static com.badlogic.gdx.tools.texturepacker.MaxRectsPacker$FreeRectChoiceHeuristic[] com.badlogic.gdx.tools.texturepacker.MaxRectsPacker$FreeRectChoiceHeuristic.values()"""
        return List[FreeRectChoiceHeuristic].__wrap(__FreeRectChoiceHeuristic.values())

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
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.TextureUnpacker
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
from builtins import type
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
import com.badlogic.gdx.tools.texturepacker.TextureUnpacker as __TextureUnpacker
__TextureUnpacker = __TextureUnpacker
from builtins import int
 
class TextureUnpacker():
    """com.badlogic.gdx.tools.texturepacker.TextureUnpacker"""
 
    @staticmethod
    def __wrap(java_value: __TextureUnpacker) -> 'TextureUnpacker':
        return TextureUnpacker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextureUnpacker):
        """
        Dynamic initializer for TextureUnpacker.
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
    def main(arg0: 'String'):
        """public static void com.badlogic.gdx.tools.texturepacker.TextureUnpacker.main(java.lang.String[])"""
        __TextureUnpacker.main(arg0)

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
    def splitAtlas(self, arg0: 'TextureAtlasData', arg1: str):
        """public void com.badlogic.gdx.tools.texturepacker.TextureUnpacker.splitAtlas(com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData,java.lang.String)"""
        super(__TextureUnpacker, self).splitAtlas(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.texturepacker.TextureUnpacker()"""
        val = __TextureUnpacker()
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

    @overload
    def setQuiet(self, arg0: bool):
        """public void com.badlogic.gdx.tools.texturepacker.TextureUnpacker.setQuiet(boolean)"""
        super(__TextureUnpacker, self).setQuiet(__boolean.valueOf(arg0))

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
    def __init__(self):
        """public com.badlogic.gdx.tools.texturepacker.TextureUnpacker()"""
        val = __TextureUnpacker()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.TexturePacker
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.File as File
import com.badlogic.gdx.tools.texturepacker.TexturePacker as __TexturePacker
__TexturePacker = __TexturePacker
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
from builtins import bool
from builtins import int
 
class TexturePacker():
    """com.badlogic.gdx.tools.texturepacker.TexturePacker"""
 
    @staticmethod
    def __wrap(java_value: __TexturePacker) -> 'TexturePacker':
        return TexturePacker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TexturePacker):
        """
        Dynamic initializer for TexturePacker.
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
    def getRootPath(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.texturepacker.TexturePacker.getRootPath()"""
        return str.__wrap(super(TexturePacker, self).getRootPath())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def isModified(arg0: str, arg1: str, arg2: str, arg3: 'Settings') -> bool:
        """public static boolean com.badlogic.gdx.tools.texturepacker.TexturePacker.isModified(java.lang.String,java.lang.String,java.lang.String,com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings)"""
        return bool.__wrap(__TexturePacker.isModified(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def process(arg0: str, arg1: str, arg2: str):
        """public static void com.badlogic.gdx.tools.texturepacker.TexturePacker.process(java.lang.String,java.lang.String,java.lang.String)"""
        __TexturePacker.process(arg0, arg1, arg2)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setRootDir(self, arg0: 'File'):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker.setRootDir(java.io.File)"""
        super(__TexturePacker, self).setRootDir(arg0)

    @staticmethod
    @overload
    def processIfModified(arg0: 'Settings', arg1: str, arg2: str, arg3: str) -> bool:
        """public static boolean com.badlogic.gdx.tools.texturepacker.TexturePacker.processIfModified(com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings,java.lang.String,java.lang.String,java.lang.String)"""
        return bool.__wrap(__TexturePacker.processIfModified(arg0, arg1, arg2, arg3))

    @overload
    def pack(self, arg0: 'File', arg1: str):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker.pack(java.io.File,java.lang.String)"""
        super(__TexturePacker, self).pack(arg0, arg1)

    @overload
    def __init__(self, arg0: 'File', arg1: 'Settings'):
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker(java.io.File,com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings)"""
        val = __TexturePacker(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addImage(self, arg0: 'BufferedImage', arg1: str):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker.addImage(java.awt.image.BufferedImage,java.lang.String)"""
        super(__TexturePacker, self).addImage(arg0, arg1)

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
    def setPacker(self, arg0: 'Packer'):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker.setPacker(com.badlogic.gdx.tools.texturepacker.TexturePacker$Packer)"""
        super(__TexturePacker, self).setPacker(arg0)

    @overload
    def addImage(self, arg0: 'File'):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker.addImage(java.io.File)"""
        super(__TexturePacker, self).addImage(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void com.badlogic.gdx.tools.texturepacker.TexturePacker.main(java.lang.String[]) throws java.lang.Exception"""
        __TexturePacker.main(arg0)

    @staticmethod
    @overload
    def process(arg0: 'Settings', arg1: str, arg2: str, arg3: str):
        """public static void com.badlogic.gdx.tools.texturepacker.TexturePacker.process(com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings,java.lang.String,java.lang.String,java.lang.String)"""
        __TexturePacker.process(arg0, arg1, arg2, arg3)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Settings'):
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker(com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings)"""
        val = __TexturePacker(arg0)
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

    @staticmethod
    @overload
    def processIfModified(arg0: str, arg1: str, arg2: str) -> bool:
        """public static boolean com.badlogic.gdx.tools.texturepacker.TexturePacker.processIfModified(java.lang.String,java.lang.String,java.lang.String)"""
        return bool.__wrap(__TexturePacker.processIfModified(arg0, arg1, arg2))

    @staticmethod
    @overload
    def process(arg0: 'Settings', arg1: str, arg2: str, arg3: str, arg4: 'ProgressListener'):
        """public static void com.badlogic.gdx.tools.texturepacker.TexturePacker.process(com.badlogic.gdx.tools.texturepacker.TexturePacker$Settings,java.lang.String,java.lang.String,java.lang.String,com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener)"""
        __TexturePacker.process(arg0, arg1, arg2, arg3, arg4)

    @overload
    def setProgressListener(self, arg0: 'ProgressListener'):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker.setProgressListener(com.badlogic.gdx.tools.texturepacker.TexturePacker$ProgressListener)"""
        super(__TexturePacker, self).setProgressListener(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.io.File as File
import java.awt.image.BufferedImage as __BufferedImage
__BufferedImage = __BufferedImage
import com.badlogic.gdx.tools.texturepacker.TexturePacker as __TexturePacker_Rect
__Rect = __TexturePacker_Rect.Rect
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.awt.image.BufferedImage as BufferedImage
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Rect():
    """com.badlogic.gdx.tools.texturepacker.TexturePacker.Rect"""
 
    @staticmethod
    def __wrap(java_value: __Rect) -> 'Rect':
        return Rect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Rect):
        """
        Dynamic initializer for Rect.
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
    def unloadImage(self, arg0: 'File'):
        """public void com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect.unloadImage(java.io.File)"""
        super(__Rect, self).unloadImage(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'BufferedImage', arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool):
        """public com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect(java.awt.image.BufferedImage,int,int,int,int,boolean)"""
        val = __Rect(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __boolean.valueOf(arg5))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect.toString()"""
        return str.__wrap(super(Rect, self).toString())

    @overload
    def compareTo(self, arg0: 'Rect') -> int:
        """public int com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect.compareTo(com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect)"""
        return int.__wrap(super(__Rect, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect.equals(java.lang.Object)"""
        return bool.__wrap(super(__Rect, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getAtlasName(arg0: str, arg1: bool) -> str:
        """public static java.lang.String com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect.getAtlasName(java.lang.String,boolean)"""
        return str.__wrap(__Rect.getAtlasName(arg0, __boolean.valueOf(arg1)))

    @overload
    def getImage(self, arg0: 'ImageProcessor') -> 'BufferedImage':
        """public java.awt.image.BufferedImage com.badlogic.gdx.tools.texturepacker.TexturePacker$Rect.getImage(com.badlogic.gdx.tools.texturepacker.ImageProcessor)"""
        return 'BufferedImage'.__wrap(super(__Rect, self).getImage(arg0))

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