from __future__ import annotations
from overload import overload


 
import com.badlogic.gdx.graphics.TextureData as _TextureData
_TextureData = _TextureData
from abc import abstractmethod, ABC
 
class TextureData():
    """com.badlogic.gdx.graphics.TextureData"""
 
    @staticmethod
    def _wrap(java_value: _TextureData) -> 'TextureData':
        return TextureData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureData):
        """
        Dynamic initializer for TextureData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getFormat(self, ):
        """public abstract com.badlogic.gdx.graphics.Pixmap$Format com.badlogic.gdx.graphics.TextureData.getFormat()"""
        pass

    @abstractmethod
    def useMipMaps(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.TextureData.useMipMaps()"""
        pass

    @abstractmethod
    def getType(self, ):
        """public abstract com.badlogic.gdx.graphics.TextureData$TextureDataType com.badlogic.gdx.graphics.TextureData.getType()"""
        pass

    @abstractmethod
    def getHeight(self, ):
        """public abstract int com.badlogic.gdx.graphics.TextureData.getHeight()"""
        pass

    @abstractmethod
    def isManaged(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.TextureData.isManaged()"""
        pass

    @abstractmethod
    def isPrepared(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.TextureData.isPrepared()"""
        pass

    @abstractmethod
    def disposePixmap(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.TextureData.disposePixmap()"""
        pass

    @abstractmethod
    def consumeCustomData(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.TextureData.consumeCustomData(int)"""
        pass

    @abstractmethod
    def consumePixmap(self, ):
        """public abstract com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.graphics.TextureData.consumePixmap()"""
        pass

    @abstractmethod
    def prepare(self, ):
        """public abstract void com.badlogic.gdx.graphics.TextureData.prepare()"""
        pass

    @abstractmethod
    def getWidth(self, ):
        """public abstract int com.badlogic.gdx.graphics.TextureData.getWidth()"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.graphics.TextureData
import com.badlogic.gdx.graphics.TextureData as _TextureData
_TextureData = _TextureData
from abc import abstractmethod, ABC
 
class TextureData():
    """com.badlogic.gdx.graphics.TextureData"""
 
    @staticmethod
    def _wrap(java_value: _TextureData) -> 'TextureData':
        return TextureData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureData):
        """
        Dynamic initializer for TextureData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getFormat(self, ):
        """public abstract com.badlogic.gdx.graphics.Pixmap$Format com.badlogic.gdx.graphics.TextureData.getFormat()"""
        pass

    @abstractmethod
    def useMipMaps(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.TextureData.useMipMaps()"""
        pass

    @abstractmethod
    def getType(self, ):
        """public abstract com.badlogic.gdx.graphics.TextureData$TextureDataType com.badlogic.gdx.graphics.TextureData.getType()"""
        pass

    @abstractmethod
    def getHeight(self, ):
        """public abstract int com.badlogic.gdx.graphics.TextureData.getHeight()"""
        pass

    @abstractmethod
    def isManaged(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.TextureData.isManaged()"""
        pass

    @abstractmethod
    def isPrepared(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.TextureData.isPrepared()"""
        pass

    @abstractmethod
    def disposePixmap(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.TextureData.disposePixmap()"""
        pass

    @abstractmethod
    def consumeCustomData(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.TextureData.consumeCustomData(int)"""
        pass

    @abstractmethod
    def consumePixmap(self, ):
        """public abstract com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.graphics.TextureData.consumePixmap()"""
        pass

    @abstractmethod
    def prepare(self, ):
        """public abstract void com.badlogic.gdx.graphics.TextureData.prepare()"""
        pass

    @abstractmethod
    def getWidth(self, ):
        """public abstract int com.badlogic.gdx.graphics.TextureData.getWidth()"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.graphics.TextureData 
 
 
# CLASS: com.badlogic.gdx.graphics.TextureArray
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

from pyquantum_helper import override
import com.badlogic.gdx.graphics.Texture as _Texture_TextureFilter
_TextureFilter = _Texture_TextureFilter.TextureFilter
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.graphics.TextureArray as _TextureArray
_TextureArray = _TextureArray
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.Texture as _Texture_TextureWrap
_TextureWrap = _Texture_TextureWrap.TextureWrap
import java.lang.Float as _float
import com.badlogic.gdx.graphics.GLTexture as _GLTexture
_GLTexture = _GLTexture
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextureArray():
    """com.badlogic.gdx.graphics.TextureArray"""
 
    @staticmethod
    def _wrap(java_value: _TextureArray) -> 'TextureArray':
        return TextureArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureArray):
        """
        Dynamic initializer for TextureArray.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureArray__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureArray__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def unsafeSetAnisotropicFilter(self, arg0: float) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.unsafeSetAnisotropicFilter(float)"""
        return float._wrap(super(_GLTexture, self).unsafeSetAnisotropicFilter(_float.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'TextureArrayData'):
        """public com.badlogic.gdx.graphics.TextureArray(com.badlogic.gdx.graphics.TextureArrayData)"""
        val = _TextureArray(arg0)
        self.__wrapper = val

    @override
    @overload
    def unsafeSetFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter', arg2: bool):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,boolean)"""
        super(_GLTexture, self).unsafeSetFilter(arg0, arg1, _boolean.valueOf(arg2))

    @override
    @overload
    def getTextureObjectHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.GLTexture.getTextureObjectHandle()"""
        return int._wrap(super(GLTexture, self).getTextureObjectHandle())

    @override
    @overload
    def unsafeSetWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap'):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        super(_GLTexture, self).unsafeSetWrap(arg0, arg1)

    @overload
    def __init__(self, arg0: bool, arg1: 'Format', *arg2: 'files.FileHandle'):
        """public com.badlogic.gdx.graphics.TextureArray(boolean,com.badlogic.gdx.graphics.Pixmap$Format,com.badlogic.gdx.files.FileHandle...)"""
        val = _TextureArray(_boolean.valueOf(arg0), arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def unsafeSetAnisotropicFilter(self, arg0: float, arg1: bool) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.unsafeSetAnisotropicFilter(float,boolean)"""
        return float._wrap(super(_GLTexture, self).unsafeSetAnisotropicFilter(_float.valueOf(arg0), _boolean.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: bool, *arg1: 'files.FileHandle'):
        """public com.badlogic.gdx.graphics.TextureArray(boolean,com.badlogic.gdx.files.FileHandle...)"""
        val = _TextureArray(_boolean.valueOf(arg0), arg1)
        self.__wrapper = val

    @staticmethod
    @overload
    def clearAllTextureArrays(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.TextureArray.clearAllTextureArrays(com.badlogic.gdx.Application)"""
        _TextureArray.clearAllTextureArrays(arg0)

    @override
    @overload
    def setWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap'):
        """public void com.badlogic.gdx.graphics.GLTexture.setWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        super(_GLTexture, self).setWrap(arg0, arg1)

    @override
    @overload
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.TextureArray.isManaged()"""
        return bool._wrap(super(TextureArray, self).isManaged())

    @override
    @overload
    def getMinFilter(self) -> 'TextureFilter':
        """public com.badlogic.gdx.graphics.Texture$TextureFilter com.badlogic.gdx.graphics.GLTexture.getMinFilter()"""
        return 'TextureFilter'._wrap(super(GLTexture, self).getMinFilter())

    @override
    @overload
    def setFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter'):
        """public void com.badlogic.gdx.graphics.GLTexture.setFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter)"""
        super(_GLTexture, self).setFilter(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def getNumManagedTextureArrays() -> int:
        """public static int com.badlogic.gdx.graphics.TextureArray.getNumManagedTextureArrays()"""
        return int._wrap(_TextureArray.getNumManagedTextureArrays())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.GLTexture.dispose()"""
        super(GLTexture, self).dispose()

    @override
    @overload
    def bind(self, arg0: int):
        """public void com.badlogic.gdx.graphics.GLTexture.bind(int)"""
        super(_GLTexture, self).bind(_int.valueOf(arg0))

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.TextureArray.getWidth()"""
        return int._wrap(super(TextureArray, self).getWidth())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getMagFilter(self) -> 'TextureFilter':
        """public com.badlogic.gdx.graphics.Texture$TextureFilter com.badlogic.gdx.graphics.GLTexture.getMagFilter()"""
        return 'TextureFilter'._wrap(super(GLTexture, self).getMagFilter())

    @staticmethod
    @overload
    def invalidateAllTextureArrays(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.TextureArray.invalidateAllTextureArrays(com.badlogic.gdx.Application)"""
        _TextureArray.invalidateAllTextureArrays(arg0)

    @override
    @overload
    def getUWrap(self) -> 'TextureWrap':
        """public com.badlogic.gdx.graphics.Texture$TextureWrap com.badlogic.gdx.graphics.GLTexture.getUWrap()"""
        return 'TextureWrap'._wrap(super(GLTexture, self).getUWrap())

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.TextureArray.getHeight()"""
        return int._wrap(super(TextureArray, self).getHeight())

    @staticmethod
    @overload
    def getManagedStatus() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.TextureArray.getManagedStatus()"""
        return str._wrap(_TextureArray.getManagedStatus())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, *arg0: str):
        """public com.badlogic.gdx.graphics.TextureArray(java.lang.String...)"""
        val = _TextureArray(arg0)
        self.__wrapper = val

    @override
    @overload
    def getDepth(self) -> int:
        """public int com.badlogic.gdx.graphics.TextureArray.getDepth()"""
        return int._wrap(super(TextureArray, self).getDepth())

    @override
    @overload
    def bind(self):
        """public void com.badlogic.gdx.graphics.GLTexture.bind()"""
        super(GLTexture, self).bind()

    @override
    @overload
    def getVWrap(self) -> 'TextureWrap':
        """public com.badlogic.gdx.graphics.Texture$TextureWrap com.badlogic.gdx.graphics.GLTexture.getVWrap()"""
        return 'TextureWrap'._wrap(super(GLTexture, self).getVWrap())

    @override
    @overload
    def unsafeSetFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter'):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter)"""
        super(_GLTexture, self).unsafeSetFilter(arg0, arg1)

    @staticmethod
    @overload
    def getMaxAnisotropicFilterLevel() -> float:
        """public static float com.badlogic.gdx.graphics.GLTexture.getMaxAnisotropicFilterLevel()"""
        return float._wrap(_GLTexture.getMaxAnisotropicFilterLevel())

    @override
    @overload
    def getAnisotropicFilter(self) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.getAnisotropicFilter()"""
        return float._wrap(super(GLTexture, self).getAnisotropicFilter())

    @overload
    def __init__(self, *arg0: 'files.FileHandle'):
        """public com.badlogic.gdx.graphics.TextureArray(com.badlogic.gdx.files.FileHandle...)"""
        val = _TextureArray(arg0)
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

    @staticmethod
    @overload
    def uploadImageData(arg0: int, arg1: 'TextureData', arg2: int):
        """public static void com.badlogic.gdx.graphics.GLTexture.uploadImageData(int,com.badlogic.gdx.graphics.TextureData,int)"""
        _GLTexture.uploadImageData(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def unsafeSetWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap', arg2: bool):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap,boolean)"""
        super(_GLTexture, self).unsafeSetWrap(arg0, arg1, _boolean.valueOf(arg2))

    @overload
    def setAnisotropicFilter(self, arg0: float) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.setAnisotropicFilter(float)"""
        return float._wrap(super(_GLTexture, self).setAnisotropicFilter(_float.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.Pixmap
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.Pixmap as _Pixmap_Format
_Format = _Pixmap_Format.Format
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _object
from builtins import type
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import com.badlogic.gdx.graphics.Pixmap as _Pixmap_Filter
_Filter = _Pixmap_Filter.Filter
import com.badlogic.gdx.graphics.Pixmap as _Pixmap_Blending
_Blending = _Pixmap_Blending.Blending
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.Pixmap as _Pixmap
_Pixmap = _Pixmap
import java.nio.ByteBuffer as ByteBuffer
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Pixmap():
    """com.badlogic.gdx.graphics.Pixmap"""
 
    @staticmethod
    def _wrap(java_value: _Pixmap) -> 'Pixmap':
        return Pixmap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Pixmap):
        """
        Dynamic initializer for Pixmap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Pixmap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Pixmap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.Pixmap.getHeight()"""
        return int._wrap(super(Pixmap, self).getHeight())

    @overload
    def isDisposed(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.Pixmap.isDisposed()"""
        return bool._wrap(super(Pixmap, self).isDisposed())

    @overload
    def setPixels(self, arg0: 'ByteBuffer'):
        """public void com.badlogic.gdx.graphics.Pixmap.setPixels(java.nio.ByteBuffer)"""
        super(_Pixmap, self).setPixels(arg0)

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.Pixmap.setColor(float,float,float,float)"""
        super(_Pixmap, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getFormat(self) -> 'Format':
        """public com.badlogic.gdx.graphics.Pixmap$Format com.badlogic.gdx.graphics.Pixmap.getFormat()"""
        return 'Format'._wrap(super(Pixmap, self).getFormat())

    @overload
    def getFilter(self) -> 'Filter':
        """public com.badlogic.gdx.graphics.Pixmap$Filter com.badlogic.gdx.graphics.Pixmap.getFilter()"""
        return 'Filter'._wrap(super(Pixmap, self).getFilter())

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
    def drawPixmap(self, arg0: 'Pixmap', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.Pixmap.drawPixmap(com.badlogic.gdx.graphics.Pixmap,int,int)"""
        super(_Pixmap, self).drawPixmap(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def __init__(self, arg0: bytes, arg1: int, arg2: int):
        """public com.badlogic.gdx.graphics.Pixmap(byte[],int,int)"""
        val = _Pixmap(bytes, _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'Format'):
        """public com.badlogic.gdx.graphics.Pixmap(int,int,com.badlogic.gdx.graphics.Pixmap$Format)"""
        val = _Pixmap(_int.valueOf(arg0), _int.valueOf(arg1), arg2)
        self.__wrapper = val

    @overload
    def fill(self):
        """public void com.badlogic.gdx.graphics.Pixmap.fill()"""
        super(Pixmap, self).fill()

    @overload
    def getGLInternalFormat(self) -> int:
        """public int com.badlogic.gdx.graphics.Pixmap.getGLInternalFormat()"""
        return int._wrap(super(Pixmap, self).getGLInternalFormat())

    @overload
    def __init__(self, arg0: 'FileHandle'):
        """public com.badlogic.gdx.graphics.Pixmap(com.badlogic.gdx.files.FileHandle)"""
        val = _Pixmap(arg0)
        self.__wrapper = val

    @overload
    def getGLType(self) -> int:
        """public int com.badlogic.gdx.graphics.Pixmap.getGLType()"""
        return int._wrap(super(Pixmap, self).getGLType())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public com.badlogic.gdx.graphics.Pixmap(java.nio.ByteBuffer)"""
        val = _Pixmap(arg0)
        self.__wrapper = val

    @overload
    def getGLFormat(self) -> int:
        """public int com.badlogic.gdx.graphics.Pixmap.getGLFormat()"""
        return int._wrap(super(Pixmap, self).getGLFormat())

    @overload
    def drawPixmap(self, arg0: 'Pixmap', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public void com.badlogic.gdx.graphics.Pixmap.drawPixmap(com.badlogic.gdx.graphics.Pixmap,int,int,int,int,int,int,int,int)"""
        super(_Pixmap, self).drawPixmap(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8))

    @overload
    def drawPixel(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.Pixmap.drawPixel(int,int,int)"""
        super(_Pixmap, self).drawPixel(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def downloadFromUrl(arg0: str, arg1: 'DownloadPixmapResponseListener'):
        """public static void com.badlogic.gdx.graphics.Pixmap.downloadFromUrl(java.lang.String,com.badlogic.gdx.graphics.Pixmap$DownloadPixmapResponseListener)"""
        _Pixmap.downloadFromUrl(arg0, arg1)

    @overload
    def fillTriangle(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.Pixmap.fillTriangle(int,int,int,int,int,int)"""
        super(_Pixmap, self).fillTriangle(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @overload
    def drawLine(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.Pixmap.drawLine(int,int,int,int)"""
        super(_Pixmap, self).drawLine(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def setColor(self, arg0: int):
        """public void com.badlogic.gdx.graphics.Pixmap.setColor(int)"""
        super(_Pixmap, self).setColor(_int.valueOf(arg0))

    @overload
    def setFilter(self, arg0: 'Filter'):
        """public void com.badlogic.gdx.graphics.Pixmap.setFilter(com.badlogic.gdx.graphics.Pixmap$Filter)"""
        super(_Pixmap, self).setFilter(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def fillCircle(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.Pixmap.fillCircle(int,int,int)"""
        super(_Pixmap, self).fillCircle(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def getPixel(self, arg0: int, arg1: int) -> int:
        """public int com.badlogic.gdx.graphics.Pixmap.getPixel(int,int)"""
        return int._wrap(super(_Pixmap, self).getPixel(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def setBlending(self, arg0: 'Blending'):
        """public void com.badlogic.gdx.graphics.Pixmap.setBlending(com.badlogic.gdx.graphics.Pixmap$Blending)"""
        super(_Pixmap, self).setBlending(arg0)

    @overload
    def drawPixel(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.Pixmap.drawPixel(int,int)"""
        super(_Pixmap, self).drawPixel(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.Pixmap.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_Pixmap, self).setColor(arg0)

    @overload
    def drawRectangle(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.Pixmap.drawRectangle(int,int,int,int)"""
        super(_Pixmap, self).drawRectangle(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def drawCircle(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.Pixmap.drawCircle(int,int,int)"""
        super(_Pixmap, self).drawCircle(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.Pixmap.dispose()"""
        super(Pixmap, self).dispose()

    @staticmethod
    @overload
    def createFromFrameBuffer(arg0: int, arg1: int, arg2: int, arg3: int) -> 'Pixmap':
        """public static com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.graphics.Pixmap.createFromFrameBuffer(int,int,int,int)"""
        return Pixmap._wrap(_Pixmap.createFromFrameBuffer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def getBlending(self) -> 'Blending':
        """public com.badlogic.gdx.graphics.Pixmap$Blending com.badlogic.gdx.graphics.Pixmap.getBlending()"""
        return 'Blending'._wrap(super(Pixmap, self).getBlending())

    @overload
    def __init__(self, arg0: 'ByteBuffer', arg1: int, arg2: int):
        """public com.badlogic.gdx.graphics.Pixmap(java.nio.ByteBuffer,int,int)"""
        val = _Pixmap(arg0, _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @overload
    def drawPixmap(self, arg0: 'Pixmap', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.Pixmap.drawPixmap(com.badlogic.gdx.graphics.Pixmap,int,int,int,int,int,int)"""
        super(_Pixmap, self).drawPixmap(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6))

    @overload
    def __init__(self, arg0: 'Gdx2DPixmap'):
        """public com.badlogic.gdx.graphics.Pixmap(com.badlogic.gdx.graphics.g2d.Gdx2DPixmap)"""
        val = _Pixmap(arg0)
        self.__wrapper = val

    @overload
    def getPixels(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.graphics.Pixmap.getPixels()"""
        return 'ByteBuffer'._wrap(super(Pixmap, self).getPixels())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.Pixmap.getWidth()"""
        return int._wrap(super(Pixmap, self).getWidth())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def fillRectangle(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.Pixmap.fillRectangle(int,int,int,int)"""
        super(_Pixmap, self).fillRectangle(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.Pixmap$DownloadPixmapResponseListener
import java.lang.Throwable as Throwable
from abc import abstractmethod, ABC
import com.badlogic.gdx.graphics.Pixmap as _Pixmap_DownloadPixmapResponseListener
_DownloadPixmapResponseListener = _Pixmap_DownloadPixmapResponseListener.DownloadPixmapResponseListener
 
class DownloadPixmapResponseListener():
    """com.badlogic.gdx.graphics.Pixmap.DownloadPixmapResponseListener"""
 
    @staticmethod
    def _wrap(java_value: _DownloadPixmapResponseListener) -> 'DownloadPixmapResponseListener':
        return DownloadPixmapResponseListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DownloadPixmapResponseListener):
        """
        Dynamic initializer for DownloadPixmapResponseListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DownloadPixmapResponseListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DownloadPixmapResponseListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def downloadFailed(self, arg0: 'Throwable'):
        """public abstract void com.badlogic.gdx.graphics.Pixmap$DownloadPixmapResponseListener.downloadFailed(java.lang.Throwable)"""
        pass

    @abstractmethod
    def downloadComplete(self, arg0: 'Pixmap'):
        """public abstract void com.badlogic.gdx.graphics.Pixmap$DownloadPixmapResponseListener.downloadComplete(com.badlogic.gdx.graphics.Pixmap)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.TextureData$TextureDataType
import com.badlogic.gdx.graphics.TextureData as _TextureData_TextureDataType
_TextureDataType = _TextureData_TextureDataType.TextureDataType
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
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextureDataType():
    """com.badlogic.gdx.graphics.TextureData.TextureDataType"""
 
    @staticmethod
    def _wrap(java_value: _TextureDataType) -> 'TextureDataType':
        return TextureDataType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureDataType):
        """
        Dynamic initializer for TextureDataType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureDataType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureDataType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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

    @staticmethod
    @overload
    def values() -> List['TextureDataType']:
        """public static com.badlogic.gdx.graphics.TextureData$TextureDataType[] com.badlogic.gdx.graphics.TextureData$TextureDataType.values()"""
        return List[TextureDataType]._wrap(_TextureDataType.values())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'TextureDataType':
        """public static com.badlogic.gdx.graphics.TextureData$TextureDataType com.badlogic.gdx.graphics.TextureData$TextureDataType.valueOf(java.lang.String)"""
        return TextureDataType._wrap(_TextureDataType.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.Pixmap$Blending
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.Pixmap as _Pixmap_Blending
_Blending = _Pixmap_Blending.Blending
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
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Blending():
    """com.badlogic.gdx.graphics.Pixmap.Blending"""
 
    @staticmethod
    def _wrap(java_value: _Blending) -> 'Blending':
        return Blending(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Blending):
        """
        Dynamic initializer for Blending.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Blending__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Blending__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def values() -> List['Blending']:
        """public static com.badlogic.gdx.graphics.Pixmap$Blending[] com.badlogic.gdx.graphics.Pixmap$Blending.values()"""
        return List[Blending]._wrap(_Blending.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Blending':
        """public static com.badlogic.gdx.graphics.Pixmap$Blending com.badlogic.gdx.graphics.Pixmap$Blending.valueOf(java.lang.String)"""
        return Blending._wrap(_Blending.valueOf(arg0))

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
 
 
# CLASS: com.badlogic.gdx.graphics.TextureArrayData$Factory
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.TextureArrayData as _TextureArrayData
_TextureArrayData = _TextureArrayData
import com.badlogic.gdx.graphics.TextureArrayData as _TextureArrayData_Factory
_Factory = _TextureArrayData_Factory.Factory
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Factory():
    """com.badlogic.gdx.graphics.TextureArrayData.Factory"""
 
    @staticmethod
    def _wrap(java_value: _Factory) -> 'Factory':
        return Factory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Factory):
        """
        Dynamic initializer for Factory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Factory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Factory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def loadFromFiles(arg0: 'Format', arg1: bool, *arg2: 'files.FileHandle') -> 'TextureArrayData':
        """public static com.badlogic.gdx.graphics.TextureArrayData com.badlogic.gdx.graphics.TextureArrayData$Factory.loadFromFiles(com.badlogic.gdx.graphics.Pixmap$Format,boolean,com.badlogic.gdx.files.FileHandle...)"""
        return TextureArrayData._wrap(_Factory.loadFromFiles(arg0, _boolean.valueOf(arg1), arg2))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.TextureArrayData$Factory()"""
        val = _Factory()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.TextureArrayData$Factory()"""
        val = _Factory()
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
 
 
# CLASS: com.badlogic.gdx.graphics.PerspectiveCamera
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.Camera as _Camera
_Camera = _Camera
import com.badlogic.gdx.graphics.PerspectiveCamera as _PerspectiveCamera
_PerspectiveCamera = _PerspectiveCamera
import com.badlogic.gdx.math.collision.Ray as _Ray
_Ray = _Ray
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PerspectiveCamera():
    """com.badlogic.gdx.graphics.PerspectiveCamera"""
 
    @staticmethod
    def _wrap(java_value: _PerspectiveCamera) -> 'PerspectiveCamera':
        return PerspectiveCamera(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PerspectiveCamera):
        """
        Dynamic initializer for PerspectiveCamera.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PerspectiveCamera__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PerspectiveCamera__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def translate(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.Camera.translate(com.badlogic.gdx.math.Vector3)"""
        super(_Camera, self).translate(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def rotate(self, arg0: 'Quaternion'):
        """public void com.badlogic.gdx.graphics.Camera.rotate(com.badlogic.gdx.math.Quaternion)"""
        super(_Camera, self).rotate(arg0)

    @override
    @overload
    def lookAt(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.Camera.lookAt(com.badlogic.gdx.math.Vector3)"""
        super(_Camera, self).lookAt(arg0)

    @overload
    def unproject(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.unproject(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_Camera, self).unproject(arg0))

    @overload
    def getPickRay(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.graphics.Camera.getPickRay(float,float,float,float,float,float)"""
        return 'collision.Ray'._wrap(super(_Camera, self).getPickRay(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getPickRay(self, arg0: float, arg1: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.graphics.Camera.getPickRay(float,float)"""
        return 'collision.Ray'._wrap(super(_Camera, self).getPickRay(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.PerspectiveCamera()"""
        val = _PerspectiveCamera()
        self.__wrapper = val

    @override
    @overload
    def transform(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.Camera.transform(com.badlogic.gdx.math.Matrix4)"""
        super(_Camera, self).transform(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.PerspectiveCamera()"""
        val = _PerspectiveCamera()
        self.__wrapper = val

    @override
    @overload
    def rotateAround(self, arg0: 'Vector3', arg1: 'Vector3', arg2: float):
        """public void com.badlogic.gdx.graphics.Camera.rotateAround(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float)"""
        super(_Camera, self).rotateAround(arg0, arg1, _float.valueOf(arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def normalizeUp(self):
        """public void com.badlogic.gdx.graphics.Camera.normalizeUp()"""
        super(Camera, self).normalizeUp()

    @override
    @overload
    def translate(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.Camera.translate(float,float,float)"""
        super(_Camera, self).translate(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.PerspectiveCamera.update()"""
        super(PerspectiveCamera, self).update()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def update(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.PerspectiveCamera.update(boolean)"""
        super(_PerspectiveCamera, self).update(_boolean.valueOf(arg0))

    @overload
    def project(self, arg0: 'Vector3', arg1: float, arg2: float, arg3: float, arg4: float) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.project(com.badlogic.gdx.math.Vector3,float,float,float,float)"""
        return 'math.Vector3'._wrap(super(_Camera, self).project(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public com.badlogic.gdx.graphics.PerspectiveCamera(float,float,float)"""
        val = _PerspectiveCamera(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def lookAt(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.Camera.lookAt(float,float,float)"""
        super(_Camera, self).lookAt(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def rotate(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.Camera.rotate(com.badlogic.gdx.math.Vector3,float)"""
        super(_Camera, self).rotate(arg0, _float.valueOf(arg1))

    @overload
    def project(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.project(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_Camera, self).project(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def rotate(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.Camera.rotate(com.badlogic.gdx.math.Matrix4)"""
        super(_Camera, self).rotate(arg0)

    @override
    @overload
    def rotate(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.Camera.rotate(float,float,float,float)"""
        super(_Camera, self).rotate(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def unproject(self, arg0: 'Vector3', arg1: float, arg2: float, arg3: float, arg4: float) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.unproject(com.badlogic.gdx.math.Vector3,float,float,float,float)"""
        return 'math.Vector3'._wrap(super(_Camera, self).unproject(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

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
 
 
# CLASS: com.badlogic.gdx.graphics.Colors
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.Colors as _Colors
_Colors = _Colors
import com.badlogic.gdx.utils.ObjectMap as _ObjectMap
_ObjectMap = _ObjectMap
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Colors():
    """com.badlogic.gdx.graphics.Colors"""
 
    @staticmethod
    def _wrap(java_value: _Colors) -> 'Colors':
        return Colors(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Colors):
        """
        Dynamic initializer for Colors.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Colors__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Colors__wrapper":
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

    @staticmethod
    @overload
    def get(arg0: str) -> 'Color':
        """public static com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Colors.get(java.lang.String)"""
        return Color._wrap(_Colors.get(arg0))

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

    @staticmethod
    @overload
    def put(arg0: str, arg1: 'Color') -> 'Color':
        """public static com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Colors.put(java.lang.String,com.badlogic.gdx.graphics.Color)"""
        return Color._wrap(_Colors.put(arg0, arg1))

    @staticmethod
    @overload
    def getColors() -> 'utils.ObjectMap':
        """public static com.badlogic.gdx.utils.ObjectMap<java.lang.String, com.badlogic.gdx.graphics.Color> com.badlogic.gdx.graphics.Colors.getColors()"""
        return utils.ObjectMap._wrap(_Colors.getColors())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

        @staticmethod
        @overload
        def reset():
            """public static void com.badlogic.gdx.graphics.Colors.reset()"""
            _Colors.reset()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.Cursor$SystemCursor
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
import com.badlogic.gdx.graphics.Cursor as _Cursor_SystemCursor
_SystemCursor = _Cursor_SystemCursor.SystemCursor
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SystemCursor():
    """com.badlogic.gdx.graphics.Cursor.SystemCursor"""
 
    @staticmethod
    def _wrap(java_value: _SystemCursor) -> 'SystemCursor':
        return SystemCursor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SystemCursor):
        """
        Dynamic initializer for SystemCursor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SystemCursor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SystemCursor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'SystemCursor':
        """public static com.badlogic.gdx.graphics.Cursor$SystemCursor com.badlogic.gdx.graphics.Cursor$SystemCursor.valueOf(java.lang.String)"""
        return SystemCursor._wrap(_SystemCursor.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['SystemCursor']:
        """public static com.badlogic.gdx.graphics.Cursor$SystemCursor[] com.badlogic.gdx.graphics.Cursor$SystemCursor.values()"""
        return List[SystemCursor]._wrap(_SystemCursor.values())

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
 
 
# CLASS: com.badlogic.gdx.graphics.TextureArrayData
from abc import abstractmethod, ABC
import com.badlogic.gdx.graphics.TextureArrayData as _TextureArrayData
_TextureArrayData = _TextureArrayData
 
class TextureArrayData():
    """com.badlogic.gdx.graphics.TextureArrayData"""
 
    @staticmethod
    def _wrap(java_value: _TextureArrayData) -> 'TextureArrayData':
        return TextureArrayData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureArrayData):
        """
        Dynamic initializer for TextureArrayData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureArrayData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureArrayData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def prepare(self, ):
        """public abstract void com.badlogic.gdx.graphics.TextureArrayData.prepare()"""
        pass

    @abstractmethod
    def isPrepared(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.TextureArrayData.isPrepared()"""
        pass

    @abstractmethod
    def getInternalFormat(self, ):
        """public abstract int com.badlogic.gdx.graphics.TextureArrayData.getInternalFormat()"""
        pass

    @abstractmethod
    def getWidth(self, ):
        """public abstract int com.badlogic.gdx.graphics.TextureArrayData.getWidth()"""
        pass

    @abstractmethod
    def consumeTextureArrayData(self, ):
        """public abstract void com.badlogic.gdx.graphics.TextureArrayData.consumeTextureArrayData()"""
        pass

    @abstractmethod
    def getHeight(self, ):
        """public abstract int com.badlogic.gdx.graphics.TextureArrayData.getHeight()"""
        pass

    @abstractmethod
    def isManaged(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.TextureArrayData.isManaged()"""
        pass

    @abstractmethod
    def getGLType(self, ):
        """public abstract int com.badlogic.gdx.graphics.TextureArrayData.getGLType()"""
        pass

    @abstractmethod
    def getDepth(self, ):
        """public abstract int com.badlogic.gdx.graphics.TextureArrayData.getDepth()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.Texture3D
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

from pyquantum_helper import override
import com.badlogic.gdx.graphics.Texture as _Texture_TextureFilter
_TextureFilter = _Texture_TextureFilter.TextureFilter
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.Texture3D as _Texture3D
_Texture3D = _Texture3D
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.Texture as _Texture_TextureWrap
_TextureWrap = _Texture_TextureWrap.TextureWrap
import java.lang.Float as _float
import com.badlogic.gdx.graphics.Texture3DData as _Texture3DData
_Texture3DData = _Texture3DData
import java.lang.Boolean as _boolean
import com.badlogic.gdx.graphics.GLTexture as _GLTexture
_GLTexture = _GLTexture
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Texture3D():
    """com.badlogic.gdx.graphics.Texture3D"""
 
    @staticmethod
    def _wrap(java_value: _Texture3D) -> 'Texture3D':
        return Texture3D(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Texture3D):
        """
        Dynamic initializer for Texture3D.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Texture3D__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Texture3D__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public com.badlogic.gdx.graphics.Texture3D(int,int,int,int,int,int)"""
        val = _Texture3D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))
        self.__wrapper = val

    @staticmethod
    @overload
    def getManagedStatus() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.Texture3D.getManagedStatus()"""
        return str._wrap(_Texture3D.getManagedStatus())

    @staticmethod
    @overload
    def invalidateAllTextureArrays(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.Texture3D.invalidateAllTextureArrays(com.badlogic.gdx.Application)"""
        _Texture3D.invalidateAllTextureArrays(arg0)

    @overload
    def unsafeSetAnisotropicFilter(self, arg0: float) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.unsafeSetAnisotropicFilter(float)"""
        return float._wrap(super(_GLTexture, self).unsafeSetAnisotropicFilter(_float.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def unsafeSetWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap', arg2: 'TextureWrap', arg3: bool):
        """public void com.badlogic.gdx.graphics.Texture3D.unsafeSetWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap,boolean)"""
        super(_Texture3D, self).unsafeSetWrap(arg0, arg1, arg2, _boolean.valueOf(arg3))

    @overload
    def upload(self):
        """public void com.badlogic.gdx.graphics.Texture3D.upload()"""
        super(Texture3D, self).upload()

    @override
    @overload
    def unsafeSetFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter', arg2: bool):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,boolean)"""
        super(_GLTexture, self).unsafeSetFilter(arg0, arg1, _boolean.valueOf(arg2))

    @override
    @overload
    def getTextureObjectHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.GLTexture.getTextureObjectHandle()"""
        return int._wrap(super(GLTexture, self).getTextureObjectHandle())

    @overload
    def __init__(self, arg0: 'Texture3DData'):
        """public com.badlogic.gdx.graphics.Texture3D(com.badlogic.gdx.graphics.Texture3DData)"""
        val = _Texture3D(arg0)
        self.__wrapper = val

    @override
    @overload
    def unsafeSetWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap'):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        super(_GLTexture, self).unsafeSetWrap(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def unsafeSetAnisotropicFilter(self, arg0: float, arg1: bool) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.unsafeSetAnisotropicFilter(float,boolean)"""
        return float._wrap(super(_GLTexture, self).unsafeSetAnisotropicFilter(_float.valueOf(arg0), _boolean.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.Texture3D.isManaged()"""
        return bool._wrap(super(Texture3D, self).isManaged())

    @override
    @overload
    def setWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap'):
        """public void com.badlogic.gdx.graphics.GLTexture.setWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        super(_GLTexture, self).setWrap(arg0, arg1)

    @overload
    def unsafeSetWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap', arg2: 'TextureWrap'):
        """public void com.badlogic.gdx.graphics.Texture3D.unsafeSetWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        super(_Texture3D, self).unsafeSetWrap(arg0, arg1, arg2)

    @staticmethod
    @overload
    def clearAllTextureArrays(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.Texture3D.clearAllTextureArrays(com.badlogic.gdx.Application)"""
        _Texture3D.clearAllTextureArrays(arg0)

    @override
    @overload
    def getMinFilter(self) -> 'TextureFilter':
        """public com.badlogic.gdx.graphics.Texture$TextureFilter com.badlogic.gdx.graphics.GLTexture.getMinFilter()"""
        return 'TextureFilter'._wrap(super(GLTexture, self).getMinFilter())

    @overload
    def setWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap', arg2: 'TextureWrap'):
        """public void com.badlogic.gdx.graphics.Texture3D.setWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        super(_Texture3D, self).setWrap(arg0, arg1, arg2)

    @override
    @overload
    def setFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter'):
        """public void com.badlogic.gdx.graphics.GLTexture.setFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter)"""
        super(_GLTexture, self).setFilter(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getDepth(self) -> int:
        """public int com.badlogic.gdx.graphics.Texture3D.getDepth()"""
        return int._wrap(super(Texture3D, self).getDepth())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.GLTexture.dispose()"""
        super(GLTexture, self).dispose()

    @override
    @overload
    def bind(self, arg0: int):
        """public void com.badlogic.gdx.graphics.GLTexture.bind(int)"""
        super(_GLTexture, self).bind(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getMagFilter(self) -> 'TextureFilter':
        """public com.badlogic.gdx.graphics.Texture$TextureFilter com.badlogic.gdx.graphics.GLTexture.getMagFilter()"""
        return 'TextureFilter'._wrap(super(GLTexture, self).getMagFilter())

    @override
    @overload
    def getUWrap(self) -> 'TextureWrap':
        """public com.badlogic.gdx.graphics.Texture$TextureWrap com.badlogic.gdx.graphics.GLTexture.getUWrap()"""
        return 'TextureWrap'._wrap(super(GLTexture, self).getUWrap())

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.Texture3D.getHeight()"""
        return int._wrap(super(Texture3D, self).getHeight())

    @overload
    def getData(self) -> 'Texture3DData':
        """public com.badlogic.gdx.graphics.Texture3DData com.badlogic.gdx.graphics.Texture3D.getData()"""
        return 'Texture3DData'._wrap(super(Texture3D, self).getData())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def bind(self):
        """public void com.badlogic.gdx.graphics.GLTexture.bind()"""
        super(GLTexture, self).bind()

    @override
    @overload
    def getVWrap(self) -> 'TextureWrap':
        """public com.badlogic.gdx.graphics.Texture$TextureWrap com.badlogic.gdx.graphics.GLTexture.getVWrap()"""
        return 'TextureWrap'._wrap(super(GLTexture, self).getVWrap())

    @override
    @overload
    def unsafeSetFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter'):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter)"""
        super(_GLTexture, self).unsafeSetFilter(arg0, arg1)

    @staticmethod
    @overload
    def getMaxAnisotropicFilterLevel() -> float:
        """public static float com.badlogic.gdx.graphics.GLTexture.getMaxAnisotropicFilterLevel()"""
        return float._wrap(_GLTexture.getMaxAnisotropicFilterLevel())

    @override
    @overload
    def getAnisotropicFilter(self) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.getAnisotropicFilter()"""
        return float._wrap(super(GLTexture, self).getAnisotropicFilter())

    @staticmethod
    @overload
    def getNumManagedTextures3D() -> int:
        """public static int com.badlogic.gdx.graphics.Texture3D.getNumManagedTextures3D()"""
        return int._wrap(_Texture3D.getNumManagedTextures3D())

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

    @staticmethod
    @overload
    def uploadImageData(arg0: int, arg1: 'TextureData', arg2: int):
        """public static void com.badlogic.gdx.graphics.GLTexture.uploadImageData(int,com.badlogic.gdx.graphics.TextureData,int)"""
        _GLTexture.uploadImageData(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def unsafeSetWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap', arg2: bool):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap,boolean)"""
        super(_GLTexture, self).unsafeSetWrap(arg0, arg1, _boolean.valueOf(arg2))

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.Texture3D.getWidth()"""
        return int._wrap(super(Texture3D, self).getWidth())

    @overload
    def setAnisotropicFilter(self, arg0: float) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.setAnisotropicFilter(float)"""
        return float._wrap(super(_GLTexture, self).setAnisotropicFilter(_float.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.Texture$TextureFilter
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.graphics.Texture as _Texture_TextureFilter
_TextureFilter = _Texture_TextureFilter.TextureFilter
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
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextureFilter():
    """com.badlogic.gdx.graphics.Texture.TextureFilter"""
 
    @staticmethod
    def _wrap(java_value: _TextureFilter) -> 'TextureFilter':
        return TextureFilter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureFilter):
        """
        Dynamic initializer for TextureFilter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureFilter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureFilter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'TextureFilter':
        """public static com.badlogic.gdx.graphics.Texture$TextureFilter com.badlogic.gdx.graphics.Texture$TextureFilter.valueOf(java.lang.String)"""
        return TextureFilter._wrap(_TextureFilter.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getGLEnum(self) -> int:
        """public int com.badlogic.gdx.graphics.Texture$TextureFilter.getGLEnum()"""
        return int._wrap(super(TextureFilter, self).getGLEnum())

    @staticmethod
    @overload
    def values() -> List['TextureFilter']:
        """public static com.badlogic.gdx.graphics.Texture$TextureFilter[] com.badlogic.gdx.graphics.Texture$TextureFilter.values()"""
        return List[TextureFilter]._wrap(_TextureFilter.values())

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
    def isMipMap(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.Texture$TextureFilter.isMipMap()"""
        return bool._wrap(super(TextureFilter, self).isMipMap())

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
 
 
# CLASS: com.badlogic.gdx.graphics.Texture3DData
import com.badlogic.gdx.graphics.Texture3DData as _Texture3DData
_Texture3DData = _Texture3DData
from abc import abstractmethod, ABC
 
class Texture3DData():
    """com.badlogic.gdx.graphics.Texture3DData"""
 
    @staticmethod
    def _wrap(java_value: _Texture3DData) -> 'Texture3DData':
        return Texture3DData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Texture3DData):
        """
        Dynamic initializer for Texture3DData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Texture3DData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Texture3DData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def useMipMaps(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.Texture3DData.useMipMaps()"""
        pass

    @abstractmethod
    def isManaged(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.Texture3DData.isManaged()"""
        pass

    @abstractmethod
    def getWidth(self, ):
        """public abstract int com.badlogic.gdx.graphics.Texture3DData.getWidth()"""
        pass

    @abstractmethod
    def getHeight(self, ):
        """public abstract int com.badlogic.gdx.graphics.Texture3DData.getHeight()"""
        pass

    @abstractmethod
    def isPrepared(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.Texture3DData.isPrepared()"""
        pass

    @abstractmethod
    def getGLType(self, ):
        """public abstract int com.badlogic.gdx.graphics.Texture3DData.getGLType()"""
        pass

    @abstractmethod
    def consume3DData(self, ):
        """public abstract void com.badlogic.gdx.graphics.Texture3DData.consume3DData()"""
        pass

    @abstractmethod
    def prepare(self, ):
        """public abstract void com.badlogic.gdx.graphics.Texture3DData.prepare()"""
        pass

    @abstractmethod
    def getDepth(self, ):
        """public abstract int com.badlogic.gdx.graphics.Texture3DData.getDepth()"""
        pass

    @abstractmethod
    def getInternalFormat(self, ):
        """public abstract int com.badlogic.gdx.graphics.Texture3DData.getInternalFormat()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.GL20
import java.nio.IntBuffer as IntBuffer
import java.nio.Buffer as Buffer
from builtins import float
from abc import abstractmethod, ABC
import java.nio.FloatBuffer as FloatBuffer
import com.badlogic.gdx.graphics.GL20 as _GL20
_GL20 = _GL20
from builtins import int
 
class GL20():
    """com.badlogic.gdx.graphics.GL20"""
 
    @staticmethod
    def _wrap(java_value: _GL20) -> 'GL20':
        return GL20(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GL20):
        """
        Dynamic initializer for GL20.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GL20__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GL20__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def glGetProgramInfoLog(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetProgramInfoLog(int)"""
        pass

    @abstractmethod
    def glIsRenderbuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsRenderbuffer(int)"""
        pass

    @abstractmethod
    def glGetFloatv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetFloatv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glCreateShader(self, arg0: int):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCreateShader(int)"""
        pass

    @abstractmethod
    def glStencilOpSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilOpSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glStencilFunc(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilFunc(int,int,int)"""
        pass

    @abstractmethod
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttribPointer(int,int,int,boolean,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGetVertexAttribPointerv(self, arg0: int, arg1: int, arg2: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribPointerv(int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGetActiveAttrib(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetActiveAttrib(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glColorMask(self, arg0: bool, arg1: bool, arg2: bool, arg3: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glColorMask(boolean,boolean,boolean,boolean)"""
        pass

    @abstractmethod
    def glBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBufferSubData(int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glUniform4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4f(int,float,float,float,float)"""
        pass

    @abstractmethod
    def glBindFramebuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindFramebuffer(int,int)"""
        pass

    @abstractmethod
    def glDisable(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDisable(int)"""
        pass

    @abstractmethod
    def glBlendColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendColor(float,float,float,float)"""
        pass

    @abstractmethod
    def glGenBuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenBuffer()"""
        pass

    @abstractmethod
    def glDeleteShader(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteShader(int)"""
        pass

    @abstractmethod
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glRenderbufferStorage(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glRenderbufferStorage(int,int,int,int)"""
        pass

    @abstractmethod
    def glBlendEquationSeparate(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendEquationSeparate(int,int)"""
        pass

    @abstractmethod
    def glGetShaderPrecisionFormat(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetShaderPrecisionFormat(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glDeleteProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteProgram(int)"""
        pass

    @abstractmethod
    def glScissor(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glScissor(int,int,int,int)"""
        pass

    @abstractmethod
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glVertexAttrib2fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib2fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glCullFace(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCullFace(int)"""
        pass

    @abstractmethod
    def glIsProgram(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsProgram(int)"""
        pass

    @abstractmethod
    def glLineWidth(self, arg0: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glLineWidth(float)"""
        pass

    @abstractmethod
    def glStencilFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilFuncSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glVertexAttrib3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib3f(int,float,float,float)"""
        pass

    @abstractmethod
    def glCompressedTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompressedTexImage2D(int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glStencilMask(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilMask(int)"""
        pass

    @abstractmethod
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform2f(self, arg0: int, arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2f(int,float,float)"""
        pass

    @abstractmethod
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix3fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glDepthRangef(self, arg0: float, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthRangef(float,float)"""
        pass

    @abstractmethod
    def glUniform1f(self, arg0: int, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1f(int,float)"""
        pass

    @abstractmethod
    def glUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3i(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetError(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetError()"""
        pass

    @abstractmethod
    def glVertexAttrib1f(self, arg0: int, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib1f(int,float)"""
        pass

    @abstractmethod
    def glReadPixels(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glReadPixels(int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glDetachShader(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDetachShader(int,int)"""
        pass

    @abstractmethod
    def glClearColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearColor(float,float,float,float)"""
        pass

    @abstractmethod
    def glBlendFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendFuncSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glGenBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenBuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glShaderBinary(self, arg0: int, arg1: 'IntBuffer', arg2: int, arg3: 'Buffer', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glShaderBinary(int,java.nio.IntBuffer,int,java.nio.Buffer,int)"""
        pass

    @abstractmethod
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix2fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glGetUniformfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetUniformfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetFramebufferAttachmentParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetFramebufferAttachmentParameteriv(int,int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glCopyTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCopyTexImage2D(int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDeleteBuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteBuffer(int)"""
        pass

    @abstractmethod
    def glEnable(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glEnable(int)"""
        pass

    @abstractmethod
    def glVertexAttrib4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib4f(int,float,float,float,float)"""
        pass

    @abstractmethod
    def glGetAttribLocation(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetAttribLocation(int,java.lang.String)"""
        pass

    @abstractmethod
    def glVertexAttrib3fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib3fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glDeleteTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteTextures(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetShaderiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetShaderiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glLinkProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glLinkProgram(int)"""
        pass

    @abstractmethod
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glUniform2i(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2i(int,int,int)"""
        pass

    @abstractmethod
    def glUniform1i(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1i(int,int)"""
        pass

    @abstractmethod
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetIntegerv(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetIntegerv(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glClearStencil(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearStencil(int)"""
        pass

    @abstractmethod
    def glGetShaderInfoLog(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetShaderInfoLog(int)"""
        pass

    @abstractmethod
    def glPixelStorei(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glPixelStorei(int,int)"""
        pass

    @abstractmethod
    def glIsShader(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsShader(int)"""
        pass

    @abstractmethod
    def glVertexAttrib2f(self, arg0: int, arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib2f(int,float,float)"""
        pass

    @abstractmethod
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteRenderbuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteRenderbuffer(int)"""
        pass

    @abstractmethod
    def glGenFramebuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenFramebuffer()"""
        pass

    @abstractmethod
    def glGenRenderbuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenRenderbuffer()"""
        pass

    @abstractmethod
    def glUseProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUseProgram(int)"""
        pass

    @abstractmethod
    def glFinish(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFinish()"""
        pass

    @abstractmethod
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glReleaseShaderCompiler(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glReleaseShaderCompiler()"""
        pass

    @abstractmethod
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawElements(int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glSampleCoverage(self, arg0: float, arg1: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glSampleCoverage(float,boolean)"""
        pass

    @abstractmethod
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glCompileShader(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompileShader(int)"""
        pass

    @abstractmethod
    def glGetAttachedShaders(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetAttachedShaders(int,int,java.nio.Buffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix4fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glClearDepthf(self, arg0: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearDepthf(float)"""
        pass

    @abstractmethod
    def glStencilOp(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilOp(int,int,int)"""
        pass

    @abstractmethod
    def glGenTexture(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenTexture()"""
        pass

    @abstractmethod
    def glIsBuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsBuffer(int)"""
        pass

    @abstractmethod
    def glBlendEquation(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendEquation(int)"""
        pass

    @abstractmethod
    def glTexParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameteri(int,int,int)"""
        pass

    @abstractmethod
    def glDrawArrays(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawArrays(int,int,int)"""
        pass

    @abstractmethod
    def glCheckFramebufferStatus(self, arg0: int):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCheckFramebufferStatus(int)"""
        pass

    @abstractmethod
    def glBindTexture(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindTexture(int,int)"""
        pass

    @abstractmethod
    def glGetBufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetBufferParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawElements(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetProgramiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetProgramiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetRenderbufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetRenderbufferParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDepthFunc(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthFunc(int)"""
        pass

    @abstractmethod
    def glShaderSource(self, arg0: int, arg1: str):
        """public abstract void com.badlogic.gdx.graphics.GL20.glShaderSource(int,java.lang.String)"""
        pass

    @abstractmethod
    def glGetUniformLocation(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetUniformLocation(int,java.lang.String)"""
        pass

    @abstractmethod
    def glGetUniformiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetUniformiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glPolygonOffset(self, arg0: float, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glPolygonOffset(float,float)"""
        pass

    @abstractmethod
    def glGetActiveUniform(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetActiveUniform(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttribPointer(int,int,int,boolean,int,int)"""
        pass

    @abstractmethod
    def glGetBooleanv(self, arg0: int, arg1: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetBooleanv(int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glStencilMaskSeparate(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilMaskSeparate(int,int)"""
        pass

    @abstractmethod
    def glTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glCreateProgram(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCreateProgram()"""
        pass

    @abstractmethod
    def glGetString(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetString(int)"""
        pass

    @abstractmethod
    def glDeleteRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteRenderbuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glDeleteTexture(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteTexture(int)"""
        pass

    @abstractmethod
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glHint(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glHint(int,int)"""
        pass

    @abstractmethod
    def glDepthMask(self, arg0: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthMask(boolean)"""
        pass

    @abstractmethod
    def glUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4i(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGenFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenFramebuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteFramebuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteFramebuffer(int)"""
        pass

    @abstractmethod
    def glBufferData(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBufferData(int,int,java.nio.Buffer,int)"""
        pass

    @abstractmethod
    def glBindBuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindBuffer(int,int)"""
        pass

    @abstractmethod
    def glGenTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenTextures(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetVertexAttribiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFramebufferRenderbuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFramebufferRenderbuffer(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetTexParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glIsEnabled(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsEnabled(int)"""
        pass

    @abstractmethod
    def glViewport(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glViewport(int,int,int,int)"""
        pass

    @abstractmethod
    def glGenRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenRenderbuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glBindRenderbuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindRenderbuffer(int,int)"""
        pass

    @abstractmethod
    def glFlush(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFlush()"""
        pass

    @abstractmethod
    def glClear(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClear(int)"""
        pass

    @abstractmethod
    def glActiveTexture(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glActiveTexture(int)"""
        pass

    @abstractmethod
    def glEnableVertexAttribArray(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glEnableVertexAttribArray(int)"""
        pass

    @abstractmethod
    def glAttachShader(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glAttachShader(int,int)"""
        pass

    @abstractmethod
    def glIsTexture(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsTexture(int)"""
        pass

    @abstractmethod
    def glIsFramebuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsFramebuffer(int)"""
        pass

    @abstractmethod
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glVertexAttrib4fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib4fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlendFunc(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendFunc(int,int)"""
        pass

    @abstractmethod
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glDeleteBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteBuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetTexParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFramebufferTexture2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFramebufferTexture2D(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glTexParameterf(self, arg0: int, arg1: int, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameterf(int,int,float)"""
        pass

    @abstractmethod
    def glBindAttribLocation(self, arg0: int, arg1: int, arg2: str):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindAttribLocation(int,int,java.lang.String)"""
        pass

    @abstractmethod
    def glGenerateMipmap(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenerateMipmap(int)"""
        pass

    @abstractmethod
    def glUniform3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3f(int,float,float,float)"""
        pass

    @abstractmethod
    def glDeleteFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteFramebuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDisableVertexAttribArray(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDisableVertexAttribArray(int)"""
        pass

    @abstractmethod
    def glTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glCopyTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCopyTexSubImage2D(int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetVertexAttribfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glVertexAttrib1fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib1fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glCompressedTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompressedTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glValidateProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glValidateProgram(int)"""
        pass

    @abstractmethod
    def glFrontFace(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFrontFace(int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.VertexAttributes$Usage
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.VertexAttributes as _VertexAttributes_Usage
_Usage = _VertexAttributes_Usage.Usage
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Usage():
    """com.badlogic.gdx.graphics.VertexAttributes.Usage"""
 
    @staticmethod
    def _wrap(java_value: _Usage) -> 'Usage':
        return Usage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Usage):
        """
        Dynamic initializer for Usage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Usage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Usage__wrapper":
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.VertexAttributes$Usage()"""
        val = _Usage()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.VertexAttributes$Usage()"""
        val = _Usage()
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.graphics.Camera
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.Camera as _Camera
_Camera = _Camera
import com.badlogic.gdx.math.collision.Ray as _Ray
_Ray = _Ray
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Camera():
    """com.badlogic.gdx.graphics.Camera"""
 
    @staticmethod
    def _wrap(java_value: _Camera) -> 'Camera':
        return Camera(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Camera):
        """
        Dynamic initializer for Camera.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Camera__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Camera__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def update(self, ):
        """public abstract void com.badlogic.gdx.graphics.Camera.update()"""
        pass

    @abstractmethod
    def update(self, arg0: bool):
        """public abstract void com.badlogic.gdx.graphics.Camera.update(boolean)"""
        pass

    @overload
    def transform(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.Camera.transform(com.badlogic.gdx.math.Matrix4)"""
        super(_Camera, self).transform(arg0)

    @overload
    def rotate(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.Camera.rotate(com.badlogic.gdx.math.Vector3,float)"""
        super(_Camera, self).rotate(arg0, _float.valueOf(arg1))

    @overload
    def lookAt(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.Camera.lookAt(com.badlogic.gdx.math.Vector3)"""
        super(_Camera, self).lookAt(arg0)

    @overload
    def rotateAround(self, arg0: 'Vector3', arg1: 'Vector3', arg2: float):
        """public void com.badlogic.gdx.graphics.Camera.rotateAround(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float)"""
        super(_Camera, self).rotateAround(arg0, arg1, _float.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def rotate(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.Camera.rotate(com.badlogic.gdx.math.Matrix4)"""
        super(_Camera, self).rotate(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.Camera()"""
        val = _Camera()
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
    def lookAt(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.Camera.lookAt(float,float,float)"""
        super(_Camera, self).lookAt(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def unproject(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.unproject(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_Camera, self).unproject(arg0))

    @overload
    def getPickRay(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.graphics.Camera.getPickRay(float,float,float,float,float,float)"""
        return 'collision.Ray'._wrap(super(_Camera, self).getPickRay(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @overload
    def translate(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.Camera.translate(float,float,float)"""
        super(_Camera, self).translate(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def translate(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.Camera.translate(com.badlogic.gdx.math.Vector3)"""
        super(_Camera, self).translate(arg0)

    @overload
    def getPickRay(self, arg0: float, arg1: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.graphics.Camera.getPickRay(float,float)"""
        return 'collision.Ray'._wrap(super(_Camera, self).getPickRay(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def rotate(self, arg0: 'Quaternion'):
        """public void com.badlogic.gdx.graphics.Camera.rotate(com.badlogic.gdx.math.Quaternion)"""
        super(_Camera, self).rotate(arg0)

    @overload
    def rotate(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.Camera.rotate(float,float,float,float)"""
        super(_Camera, self).rotate(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.Camera()"""
        val = _Camera()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def project(self, arg0: 'Vector3', arg1: float, arg2: float, arg3: float, arg4: float) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.project(com.badlogic.gdx.math.Vector3,float,float,float,float)"""
        return 'math.Vector3'._wrap(super(_Camera, self).project(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @overload
    def project(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.project(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_Camera, self).project(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def unproject(self, arg0: 'Vector3', arg1: float, arg2: float, arg3: float, arg4: float) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.unproject(com.badlogic.gdx.math.Vector3,float,float,float,float)"""
        return 'math.Vector3'._wrap(super(_Camera, self).unproject(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def normalizeUp(self):
        """public void com.badlogic.gdx.graphics.Camera.normalizeUp()"""
        super(Camera, self).normalizeUp()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.GL31
from builtins import str
import com.badlogic.gdx.graphics.GL31 as _GL31
_GL31 = _GL31
import java.nio.IntBuffer as IntBuffer
import com.badlogic.gdx.graphics.GL30 as _GL30
_GL30 = _GL30
import java.nio.Buffer as Buffer
from builtins import float
import java.nio.LongBuffer as LongBuffer
from abc import abstractmethod, ABC
import java.nio.FloatBuffer as FloatBuffer
from builtins import int
import com.badlogic.gdx.graphics.GL20 as _GL20
_GL20 = _GL20
 
class GL31():
    """com.badlogic.gdx.graphics.GL31"""
 
    @staticmethod
    def _wrap(java_value: _GL31) -> 'GL31':
        return GL31(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GL31):
        """
        Dynamic initializer for GL31.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GL31__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GL31__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def glDrawElementsInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawElementsInstanced(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glIsRenderbuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsRenderbuffer(int)"""
        pass

    @abstractmethod
    def glCreateShader(self, arg0: int):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCreateShader(int)"""
        pass

    @abstractmethod
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetActiveUniformBlockName(int,int,java.nio.Buffer,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glFramebufferParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glFramebufferParameteri(int,int,int)"""
        pass

    @abstractmethod
    def glBindTransformFeedback(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindTransformFeedback(int,int)"""
        pass

    @abstractmethod
    def glGetActiveAttrib(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetActiveAttrib(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribI4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribI4i(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDeleteVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteVertexArrays(int,int[],int)"""
        pass

    @abstractmethod
    def glGetUniformuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetUniformuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glResumeTransformFeedback(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL30.glResumeTransformFeedback()"""
        pass

    @abstractmethod
    def glUniform4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4f(int,float,float,float,float)"""
        pass

    @abstractmethod
    def glBindFramebuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindFramebuffer(int,int)"""
        pass

    @abstractmethod
    def glDisable(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDisable(int)"""
        pass

    @abstractmethod
    def glBlendColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendColor(float,float,float,float)"""
        pass

    @abstractmethod
    def glGenBuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenBuffer()"""
        pass

    @abstractmethod
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glBlendEquationSeparate(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendEquationSeparate(int,int)"""
        pass

    @abstractmethod
    def glDeleteProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteProgram(int)"""
        pass

    @abstractmethod
    def glGenQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenQueries(int,int[],int)"""
        pass

    @abstractmethod
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glRenderbufferStorageMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glRenderbufferStorageMultisample(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glCullFace(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCullFace(int)"""
        pass

    @abstractmethod
    def glLineWidth(self, arg0: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glLineWidth(float)"""
        pass

    @abstractmethod
    def glProgramUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttrib3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib3f(int,float,float,float)"""
        pass

    @abstractmethod
    def glCompressedTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompressedTexImage2D(int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glStencilMask(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilMask(int)"""
        pass

    @abstractmethod
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix3fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glUniformMatrix3x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix3x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetActiveUniformBlockiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetActiveUniformBlockiv(int,int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDepthRangef(self, arg0: float, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthRangef(float,float)"""
        pass

    @abstractmethod
    def glUniform1f(self, arg0: int, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1f(int,float)"""
        pass

    @abstractmethod
    def glProgramUniform2ui(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2ui(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetError(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetError()"""
        pass

    @abstractmethod
    def glVertexAttrib1f(self, arg0: int, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib1f(int,float)"""
        pass

    @abstractmethod
    def glUniformMatrix4x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix4x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix2x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix2x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlitFramebuffer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBlitFramebuffer(int,int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glClearBufferuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetBufferParameteri64v(self, arg0: int, arg1: int, arg2: 'LongBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetBufferParameteri64v(int,int,java.nio.LongBuffer)"""
        pass

    @abstractmethod
    def glDetachShader(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDetachShader(int,int)"""
        pass

    @abstractmethod
    def glClearColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearColor(float,float,float,float)"""
        pass

    @abstractmethod
    def glDeleteSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteSamplers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glIsTransformFeedback(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsTransformFeedback(int)"""
        pass

    @abstractmethod
    def glDrawElementsIndirect(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glDrawElementsIndirect(int,int,long)"""
        pass

    @abstractmethod
    def glProgramUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix2fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glGetUniformfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetUniformfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glDrawArraysInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawArraysInstanced(int,int,int,int)"""
        pass

    @abstractmethod
    def glUniformBlockBinding(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformBlockBinding(int,int,int)"""
        pass

    @abstractmethod
    def glDeleteBuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteBuffer(int)"""
        pass

    @abstractmethod
    def glProgramUniform1i(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1i(int,int,int)"""
        pass

    @abstractmethod
    def glBeginTransformFeedback(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBeginTransformFeedback(int)"""
        pass

    @abstractmethod
    def glGetAttribLocation(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetAttribLocation(int,java.lang.String)"""
        pass

    @abstractmethod
    def glSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glVertexAttrib3fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib3fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetBooleani_v(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetBooleani_v(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteTextures(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexImage3D(int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glBindVertexArray(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindVertexArray(int)"""
        pass

    @abstractmethod
    def glUniform1i(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1i(int,int)"""
        pass

    @abstractmethod
    def glUniform3uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniform3uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glClearStencil(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearStencil(int)"""
        pass

    @abstractmethod
    def glGetShaderInfoLog(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetShaderInfoLog(int)"""
        pass

    @abstractmethod
    def glEndQuery(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glEndQuery(int)"""
        pass

    @abstractmethod
    def glIsShader(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsShader(int)"""
        pass

    @abstractmethod
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexImage3D(int,int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteTransformFeedbacks(int,int[],int)"""
        pass

    @abstractmethod
    def glDeleteRenderbuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteRenderbuffer(int)"""
        pass

    @abstractmethod
    def glGenFramebuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenFramebuffer()"""
        pass

    @abstractmethod
    def glBindSampler(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindSampler(int,int)"""
        pass

    @abstractmethod
    def glUseProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUseProgram(int)"""
        pass

    @abstractmethod
    def glFinish(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFinish()"""
        pass

    @abstractmethod
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBindBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindBufferRange(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glReleaseShaderCompiler(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glReleaseShaderCompiler()"""
        pass

    @abstractmethod
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawElements(int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL30.glGetActiveUniformBlockName(int,int)"""
        pass

    @abstractmethod
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform4f(self, arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4f(int,int,float,float,float,float)"""
        pass

    @abstractmethod
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glUniformMatrix2x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix2x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform3f(self, arg0: int, arg1: int, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3f(int,int,float,float,float)"""
        pass

    @abstractmethod
    def glClearDepthf(self, arg0: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearDepthf(float)"""
        pass

    @abstractmethod
    def glStencilOp(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilOp(int,int,int)"""
        pass

    @abstractmethod
    def glMapBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract java.nio.Buffer com.badlogic.gdx.graphics.GL30.glMapBufferRange(int,int,int,int)"""
        pass

    @abstractmethod
    def glBindProgramPipeline(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glBindProgramPipeline(int)"""
        pass

    @abstractmethod
    def glGetMultisamplefv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetMultisamplefv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlendEquation(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendEquation(int)"""
        pass

    @abstractmethod
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenTransformFeedbacks(int,int[],int)"""
        pass

    @abstractmethod
    def glCheckFramebufferStatus(self, arg0: int):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCheckFramebufferStatus(int)"""
        pass

    @abstractmethod
    def glBindTexture(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindTexture(int,int)"""
        pass

    @abstractmethod
    def glGetBufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetBufferParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetRenderbufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetRenderbufferParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glClearBufferfi(self, arg0: int, arg1: int, arg2: float, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferfi(int,int,float,int)"""
        pass

    @abstractmethod
    def glShaderSource(self, arg0: int, arg1: str):
        """public abstract void com.badlogic.gdx.graphics.GL20.glShaderSource(int,java.lang.String)"""
        pass

    @abstractmethod
    def glClearBufferfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetUniformLocation(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetUniformLocation(int,java.lang.String)"""
        pass

    @abstractmethod
    def glGetUniformiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetUniformiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGenVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenVertexArrays(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glPolygonOffset(self, arg0: float, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glPolygonOffset(float,float)"""
        pass

    @abstractmethod
    def glProgramParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glProgramParameteri(int,int,int)"""
        pass

    @abstractmethod
    def glGetBooleanv(self, arg0: int, arg1: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetBooleanv(int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glStencilMaskSeparate(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilMaskSeparate(int,int)"""
        pass

    @abstractmethod
    def glCreateProgram(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCreateProgram()"""
        pass

    @abstractmethod
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glHint(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glHint(int,int)"""
        pass

    @abstractmethod
    def glBindVertexBuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glBindVertexBuffer(int,int,long,int)"""
        pass

    @abstractmethod
    def glDrawArraysIndirect(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glDrawArraysIndirect(int,long)"""
        pass

    @abstractmethod
    def glSampleMaski(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glSampleMaski(int,int)"""
        pass

    @abstractmethod
    def glDeleteSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteSamplers(int,int[],int)"""
        pass

    @abstractmethod
    def glGenFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenFramebuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteTransformFeedbacks(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteFramebuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteFramebuffer(int)"""
        pass

    @abstractmethod
    def glIsSampler(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsSampler(int)"""
        pass

    @abstractmethod
    def glDeleteQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteQueries(int,int[],int)"""
        pass

    @abstractmethod
    def glBindBuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindBuffer(int,int)"""
        pass

    @abstractmethod
    def glGenTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenTextures(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform2uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUnmapBuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glUnmapBuffer(int)"""
        pass

    @abstractmethod
    def glGenVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenVertexArrays(int,int[],int)"""
        pass

    @abstractmethod
    def glViewport(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glViewport(int,int,int,int)"""
        pass

    @abstractmethod
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawRangeElements(int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetQueryiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetQueryiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetVertexAttribIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetVertexAttribIuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenTransformFeedbacks(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glDispatchComputeIndirect(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glDispatchComputeIndirect(long)"""
        pass

    @abstractmethod
    def glVertexAttribFormat(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glVertexAttribFormat(int,int,int,boolean,int)"""
        pass

    @abstractmethod
    def glFlush(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFlush()"""
        pass

    @abstractmethod
    def glClear(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClear(int)"""
        pass

    @abstractmethod
    def glActiveTexture(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glActiveTexture(int)"""
        pass

    @abstractmethod
    def glCopyTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glCopyTexSubImage3D(int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glAttachShader(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glAttachShader(int,int)"""
        pass

    @abstractmethod
    def glIsTexture(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsTexture(int)"""
        pass

    @abstractmethod
    def glProgramUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glVertexAttrib4fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib4fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTransformFeedbackVaryings(self, arg0: int, arg1: 'String', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTransformFeedbackVaryings(int,java.lang.String[],int)"""
        pass

    @abstractmethod
    def glUniformMatrix4x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix4x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGenProgramPipelines(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGenProgramPipelines(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteBuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glBindImageTexture(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int, arg6: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glBindImageTexture(int,int,int,boolean,int,int,int)"""
        pass

    @abstractmethod
    def glReadBuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glReadBuffer(int)"""
        pass

    @abstractmethod
    def glProgramUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glFramebufferTexture2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFramebufferTexture2D(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetTexLevelParameterfv(self, arg0: int, arg1: int, arg2: int, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetTexLevelParameterfv(int,int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGenerateMipmap(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenerateMipmap(int)"""
        pass

    @abstractmethod
    def glGetVertexAttribIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetVertexAttribIiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3f(int,float,float,float)"""
        pass

    @abstractmethod
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribPointer(int,int,int,boolean,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glDeleteFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteFramebuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glIsQuery(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsQuery(int)"""
        pass

    @abstractmethod
    def glGenSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenSamplers(int,int[],int)"""
        pass

    @abstractmethod
    def glProgramUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawRangeElements(int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glVertexAttrib1fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib1fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glCompressedTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompressedTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glValidateProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glValidateProgram(int)"""
        pass

    @abstractmethod
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexSubImage2D(int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniform2i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2i(int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix2x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix2x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetProgramInfoLog(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetProgramInfoLog(int)"""
        pass

    @abstractmethod
    def glGetFloatv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetFloatv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glTexStorage2DMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool):
        """public abstract void com.badlogic.gdx.graphics.GL31.glTexStorage2DMultisample(int,int,int,int,int,boolean)"""
        pass

    @abstractmethod
    def glGetSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glStencilOpSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilOpSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glStencilFunc(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilFunc(int,int,int)"""
        pass

    @abstractmethod
    def glGetVertexAttribPointerv(self, arg0: int, arg1: int, arg2: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribPointerv(int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glColorMask(self, arg0: bool, arg1: bool, arg2: bool, arg3: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glColorMask(boolean,boolean,boolean,boolean)"""
        pass

    @abstractmethod
    def glBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBufferSubData(int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGetProgramResourceName(self, arg0: int, arg1: int, arg2: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL31.glGetProgramResourceName(int,int,int)"""
        pass

    @abstractmethod
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glDeleteShader(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteShader(int)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix3x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix3x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glRenderbufferStorage(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glRenderbufferStorage(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetShaderPrecisionFormat(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetShaderPrecisionFormat(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glScissor(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glScissor(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetProgramPipelineiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetProgramPipelineiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetUniformIndices(self, arg0: int, arg1: 'String', arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetUniformIndices(int,java.lang.String[],java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttrib2fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib2fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glIsProgram(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsProgram(int)"""
        pass

    @abstractmethod
    def glGetProgramResourceIndex(self, arg0: int, arg1: int, arg2: str):
        """public abstract int com.badlogic.gdx.graphics.GL31.glGetProgramResourceIndex(int,int,java.lang.String)"""
        pass

    @abstractmethod
    def glProgramUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetUniformBlockIndex(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL30.glGetUniformBlockIndex(int,java.lang.String)"""
        pass

    @abstractmethod
    def glGetProgramResourceLocation(self, arg0: int, arg1: int, arg2: str):
        """public abstract int com.badlogic.gdx.graphics.GL31.glGetProgramResourceLocation(int,int,java.lang.String)"""
        pass

    @abstractmethod
    def glStencilFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilFuncSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform2f(self, arg0: int, arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2f(int,float,float)"""
        pass

    @abstractmethod
    def glGetFramebufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetFramebufferParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform3ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3ui(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3i(int,int,int,int)"""
        pass

    @abstractmethod
    def glUniform1uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniform1uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform4uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniform4uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteVertexArrays(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glReadPixels(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glReadPixels(int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlendFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendFuncSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glGenBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenBuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glShaderBinary(self, arg0: int, arg1: 'IntBuffer', arg2: int, arg3: 'Buffer', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glShaderBinary(int,java.nio.IntBuffer,int,java.nio.Buffer,int)"""
        pass

    @abstractmethod
    def glSamplerParameterf(self, arg0: int, arg1: int, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameterf(int,int,float)"""
        pass

    @abstractmethod
    def glVertexAttribIPointer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribIPointer(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glUniformMatrix2x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix2x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetFramebufferAttachmentParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetFramebufferAttachmentParameteriv(int,int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glCopyTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCopyTexImage2D(int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glEnable(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glEnable(int)"""
        pass

    @abstractmethod
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glVertexAttrib4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib4f(int,float,float,float,float)"""
        pass

    @abstractmethod
    def glGetActiveUniformsiv(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetActiveUniformsiv(int,int,java.nio.IntBuffer,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glBeginQuery(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBeginQuery(int,int)"""
        pass

    @abstractmethod
    def glProgramUniform1f(self, arg0: int, arg1: int, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1f(int,int,float)"""
        pass

    @abstractmethod
    def glProgramUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4i(int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3i(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetShaderiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetShaderiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glLinkProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glLinkProgram(int)"""
        pass

    @abstractmethod
    def glUniform2i(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2i(int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniform3uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetProgramPipelineInfoLog(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL31.glGetProgramPipelineInfoLog(int)"""
        pass

    @abstractmethod
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetIntegerv(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetIntegerv(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetProgramInterfaceiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetProgramInterfaceiv(int,int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glPixelStorei(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glPixelStorei(int,int)"""
        pass

    @abstractmethod
    def glVertexAttrib2f(self, arg0: int, arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib2f(int,float,float)"""
        pass

    @abstractmethod
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexImage2D(int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glInvalidateSubFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: int, arg5: int, arg6: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glInvalidateSubFramebuffer(int,int,java.nio.IntBuffer,int,int,int,int)"""
        pass

    @abstractmethod
    def glActiveShaderProgram(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glActiveShaderProgram(int,int)"""
        pass

    @abstractmethod
    def glProgramUniform4ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4ui(int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glVertexAttribI4ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribI4ui(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glIsProgramPipeline(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL31.glIsProgramPipeline(int)"""
        pass

    @abstractmethod
    def glGenRenderbuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenRenderbuffer()"""
        pass

    @abstractmethod
    def glUniformMatrix3x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix3x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetInteger64v(self, arg0: int, arg1: 'LongBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetInteger64v(int,java.nio.LongBuffer)"""
        pass

    @abstractmethod
    def glSampleCoverage(self, arg0: float, arg1: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glSampleCoverage(float,boolean)"""
        pass

    @abstractmethod
    def glCompileShader(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompileShader(int)"""
        pass

    @abstractmethod
    def glGetAttachedShaders(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetAttachedShaders(int,int,java.nio.Buffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetStringi(self, arg0: int, arg1: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL30.glGetStringi(int,int)"""
        pass

    @abstractmethod
    def glCopyBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glCopyBufferSubData(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix4x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix4x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix4fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glEndTransformFeedback(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL30.glEndTransformFeedback()"""
        pass

    @abstractmethod
    def glDrawBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawBuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix3x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix3x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetTexLevelParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetTexLevelParameteriv(int,int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetFragDataLocation(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL30.glGetFragDataLocation(int,java.lang.String)"""
        pass

    @abstractmethod
    def glGenTexture(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenTexture()"""
        pass

    @abstractmethod
    def glIsBuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsBuffer(int)"""
        pass

    @abstractmethod
    def glProgramUniform2f(self, arg0: int, arg1: int, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2f(int,int,float,float)"""
        pass

    @abstractmethod
    def glUseProgramStages(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glUseProgramStages(int,int,int)"""
        pass

    @abstractmethod
    def glTexParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameteri(int,int,int)"""
        pass

    @abstractmethod
    def glDrawArrays(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawArrays(int,int,int)"""
        pass

    @abstractmethod
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawElements(int,int,int,int)"""
        pass

    @abstractmethod
    def glGenQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenQueries(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribBinding(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glVertexAttribBinding(int,int)"""
        pass

    @abstractmethod
    def glGetProgramiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetProgramiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glIsVertexArray(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsVertexArray(int)"""
        pass

    @abstractmethod
    def glDepthFunc(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthFunc(int)"""
        pass

    @abstractmethod
    def glProgramUniform1ui(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1ui(int,int,int)"""
        pass

    @abstractmethod
    def glVertexBindingDivisor(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glVertexBindingDivisor(int,int)"""
        pass

    @abstractmethod
    def glGetActiveUniform(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetActiveUniform(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttribPointer(int,int,int,boolean,int,int)"""
        pass

    @abstractmethod
    def glTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetString(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetString(int)"""
        pass

    @abstractmethod
    def glCreateShaderProgramv(self, arg0: int, arg1: 'String'):
        """public abstract int com.badlogic.gdx.graphics.GL31.glCreateShaderProgramv(int,java.lang.String[])"""
        pass

    @abstractmethod
    def glGetProgramResourceiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetProgramResourceiv(int,int,int,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform4uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteRenderbuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteTexture(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteTexture(int)"""
        pass

    @abstractmethod
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glDepthMask(self, arg0: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthMask(boolean)"""
        pass

    @abstractmethod
    def glProgramUniform1uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4i(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glBufferData(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBufferData(int,int,java.nio.Buffer,int)"""
        pass

    @abstractmethod
    def glClearBufferiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDispatchCompute(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glDispatchCompute(int,int,int)"""
        pass

    @abstractmethod
    def glPauseTransformFeedback(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL30.glPauseTransformFeedback()"""
        pass

    @abstractmethod
    def glMemoryBarrier(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glMemoryBarrier(int)"""
        pass

    @abstractmethod
    def glGetVertexAttribiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFramebufferRenderbuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFramebufferRenderbuffer(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetQueryObjectuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetQueryObjectuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetTexParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glIsEnabled(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsEnabled(int)"""
        pass

    @abstractmethod
    def glGenRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenRenderbuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glMemoryBarrierByRegion(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glMemoryBarrierByRegion(int)"""
        pass

    @abstractmethod
    def glFlushMappedBufferRange(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glFlushMappedBufferRange(int,int,int)"""
        pass

    @abstractmethod
    def glInvalidateFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glInvalidateFramebuffer(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glBindRenderbuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindRenderbuffer(int,int)"""
        pass

    @abstractmethod
    def glEnableVertexAttribArray(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glEnableVertexAttribArray(int)"""
        pass

    @abstractmethod
    def glIsFramebuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsFramebuffer(int)"""
        pass

    @abstractmethod
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glValidateProgramPipeline(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glValidateProgramPipeline(int)"""
        pass

    @abstractmethod
    def glBlendFunc(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendFunc(int,int)"""
        pass

    @abstractmethod
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix4x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix4x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBindBufferBase(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindBufferBase(int,int,int)"""
        pass

    @abstractmethod
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGetTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetTexParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTexParameterf(self, arg0: int, arg1: int, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameterf(int,int,float)"""
        pass

    @abstractmethod
    def glBindAttribLocation(self, arg0: int, arg1: int, arg2: str):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindAttribLocation(int,int,java.lang.String)"""
        pass

    @abstractmethod
    def glGenSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenSamplers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFramebufferTextureLayer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glFramebufferTextureLayer(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDisableVertexAttribArray(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDisableVertexAttribArray(int)"""
        pass

    @abstractmethod
    def glTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glDeleteQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteQueries(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribDivisor(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribDivisor(int,int)"""
        pass

    @abstractmethod
    def glCopyTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCopyTexSubImage2D(int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetVertexAttribfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribIFormat(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glVertexAttribIFormat(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetBufferPointerv(self, arg0: int, arg1: int):
        """public abstract java.nio.Buffer com.badlogic.gdx.graphics.GL30.glGetBufferPointerv(int,int)"""
        pass

    @abstractmethod
    def glDeleteProgramPipelines(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glDeleteProgramPipelines(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFrontFace(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFrontFace(int)"""
        pass

    @abstractmethod
    def glSamplerParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameteri(int,int,int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.GL32
from builtins import str
import com.badlogic.gdx.graphics.GL31 as _GL31
_GL31 = _GL31
import java.nio.IntBuffer as IntBuffer
import com.badlogic.gdx.graphics.GL30 as _GL30
_GL30 = _GL30
from builtins import float
import java.nio.LongBuffer as LongBuffer
from abc import abstractmethod, ABC
import com.badlogic.gdx.graphics.GL32 as _GL32
_GL32 = _GL32
import java.nio.FloatBuffer as FloatBuffer
import java.nio.Buffer as Buffer
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
import com.badlogic.gdx.graphics.GL20 as _GL20
_GL20 = _GL20
 
class GL32():
    """com.badlogic.gdx.graphics.GL32"""
 
    @staticmethod
    def _wrap(java_value: _GL32) -> 'GL32':
        return GL32(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GL32):
        """
        Dynamic initializer for GL32.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GL32__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GL32__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def glDrawElementsInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawElementsInstanced(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glIsRenderbuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsRenderbuffer(int)"""
        pass

    @abstractmethod
    def glCreateShader(self, arg0: int):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCreateShader(int)"""
        pass

    @abstractmethod
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetActiveUniformBlockName(int,int,java.nio.Buffer,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glFramebufferParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glFramebufferParameteri(int,int,int)"""
        pass

    @abstractmethod
    def glBindTransformFeedback(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindTransformFeedback(int,int)"""
        pass

    @abstractmethod
    def glGetActiveAttrib(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetActiveAttrib(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribI4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribI4i(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDeleteVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteVertexArrays(int,int[],int)"""
        pass

    @abstractmethod
    def glGetUniformuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetUniformuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glResumeTransformFeedback(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL30.glResumeTransformFeedback()"""
        pass

    @abstractmethod
    def glUniform4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4f(int,float,float,float,float)"""
        pass

    @abstractmethod
    def glBindFramebuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindFramebuffer(int,int)"""
        pass

    @abstractmethod
    def glDisable(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDisable(int)"""
        pass

    @abstractmethod
    def glBlendColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendColor(float,float,float,float)"""
        pass

    @abstractmethod
    def glGenBuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenBuffer()"""
        pass

    @abstractmethod
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glBlendEquationSeparate(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendEquationSeparate(int,int)"""
        pass

    @abstractmethod
    def glGetPointerv(self, arg0: int):
        """public abstract long com.badlogic.gdx.graphics.GL32.glGetPointerv(int)"""
        pass

    @abstractmethod
    def glDeleteProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteProgram(int)"""
        pass

    @abstractmethod
    def glGenQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenQueries(int,int[],int)"""
        pass

    @abstractmethod
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glRenderbufferStorageMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glRenderbufferStorageMultisample(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glCullFace(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCullFace(int)"""
        pass

    @abstractmethod
    def glLineWidth(self, arg0: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glLineWidth(float)"""
        pass

    @abstractmethod
    def glProgramUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttrib3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib3f(int,float,float,float)"""
        pass

    @abstractmethod
    def glCompressedTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompressedTexImage2D(int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glStencilMask(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilMask(int)"""
        pass

    @abstractmethod
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix3fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glUniformMatrix3x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix3x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetActiveUniformBlockiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetActiveUniformBlockiv(int,int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDepthRangef(self, arg0: float, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthRangef(float,float)"""
        pass

    @abstractmethod
    def glUniform1f(self, arg0: int, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1f(int,float)"""
        pass

    @abstractmethod
    def glProgramUniform2ui(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2ui(int,int,int,int)"""
        pass

    @abstractmethod
    def glPopDebugGroup(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL32.glPopDebugGroup()"""
        pass

    @abstractmethod
    def glGetError(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetError()"""
        pass

    @abstractmethod
    def glVertexAttrib1f(self, arg0: int, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib1f(int,float)"""
        pass

    @abstractmethod
    def glUniformMatrix4x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix4x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix2x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix2x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlitFramebuffer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBlitFramebuffer(int,int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glMinSampleShading(self, arg0: float):
        """public abstract void com.badlogic.gdx.graphics.GL32.glMinSampleShading(float)"""
        pass

    @abstractmethod
    def glClearBufferuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetBufferParameteri64v(self, arg0: int, arg1: int, arg2: 'LongBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetBufferParameteri64v(int,int,java.nio.LongBuffer)"""
        pass

    @abstractmethod
    def glDetachShader(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDetachShader(int,int)"""
        pass

    @abstractmethod
    def glClearColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearColor(float,float,float,float)"""
        pass

    @abstractmethod
    def glDeleteSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteSamplers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glIsTransformFeedback(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsTransformFeedback(int)"""
        pass

    @abstractmethod
    def glDrawElementsIndirect(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glDrawElementsIndirect(int,int,long)"""
        pass

    @abstractmethod
    def glProgramUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix2fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glGetUniformfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetUniformfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glDrawArraysInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawArraysInstanced(int,int,int,int)"""
        pass

    @abstractmethod
    def glUniformBlockBinding(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformBlockBinding(int,int,int)"""
        pass

    @abstractmethod
    def glDeleteBuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteBuffer(int)"""
        pass

    @abstractmethod
    def glProgramUniform1i(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1i(int,int,int)"""
        pass

    @abstractmethod
    def glBeginTransformFeedback(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBeginTransformFeedback(int)"""
        pass

    @abstractmethod
    def glGetAttribLocation(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetAttribLocation(int,java.lang.String)"""
        pass

    @abstractmethod
    def glSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlendFuncSeparatei(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glBlendFuncSeparatei(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glVertexAttrib3fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib3fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetBooleani_v(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetBooleani_v(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteTextures(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetnUniformfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL32.glGetnUniformfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexImage3D(int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glTexBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glTexBufferRange(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDrawElementsInstancedBaseVertex(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glDrawElementsInstancedBaseVertex(int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glBindVertexArray(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindVertexArray(int)"""
        pass

    @abstractmethod
    def glUniform1i(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1i(int,int)"""
        pass

    @abstractmethod
    def glUniform3uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniform3uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glClearStencil(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearStencil(int)"""
        pass

    @abstractmethod
    def glGetShaderInfoLog(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetShaderInfoLog(int)"""
        pass

    @abstractmethod
    def glEndQuery(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glEndQuery(int)"""
        pass

    @abstractmethod
    def glIsShader(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsShader(int)"""
        pass

    @abstractmethod
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexImage3D(int,int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteTransformFeedbacks(int,int[],int)"""
        pass

    @abstractmethod
    def glDeleteRenderbuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteRenderbuffer(int)"""
        pass

    @abstractmethod
    def glGenFramebuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenFramebuffer()"""
        pass

    @abstractmethod
    def glBindSampler(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindSampler(int,int)"""
        pass

    @abstractmethod
    def glUseProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUseProgram(int)"""
        pass

    @abstractmethod
    def glFinish(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFinish()"""
        pass

    @abstractmethod
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBindBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindBufferRange(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glReleaseShaderCompiler(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glReleaseShaderCompiler()"""
        pass

    @abstractmethod
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawElements(int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL30.glGetActiveUniformBlockName(int,int)"""
        pass

    @abstractmethod
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform4f(self, arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4f(int,int,float,float,float,float)"""
        pass

    @abstractmethod
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glUniformMatrix2x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix2x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform3f(self, arg0: int, arg1: int, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3f(int,int,float,float,float)"""
        pass

    @abstractmethod
    def glClearDepthf(self, arg0: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearDepthf(float)"""
        pass

    @abstractmethod
    def glStencilOp(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilOp(int,int,int)"""
        pass

    @abstractmethod
    def glMapBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract java.nio.Buffer com.badlogic.gdx.graphics.GL30.glMapBufferRange(int,int,int,int)"""
        pass

    @abstractmethod
    def glBindProgramPipeline(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glBindProgramPipeline(int)"""
        pass

    @abstractmethod
    def glGetMultisamplefv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetMultisamplefv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlendEquation(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendEquation(int)"""
        pass

    @abstractmethod
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenTransformFeedbacks(int,int[],int)"""
        pass

    @abstractmethod
    def glCheckFramebufferStatus(self, arg0: int):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCheckFramebufferStatus(int)"""
        pass

    @abstractmethod
    def glBindTexture(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindTexture(int,int)"""
        pass

    @abstractmethod
    def glGetBufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetBufferParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glBlendFunci(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glBlendFunci(int,int,int)"""
        pass

    @abstractmethod
    def glGetRenderbufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetRenderbufferParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glClearBufferfi(self, arg0: int, arg1: int, arg2: float, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferfi(int,int,float,int)"""
        pass

    @abstractmethod
    def glShaderSource(self, arg0: int, arg1: str):
        """public abstract void com.badlogic.gdx.graphics.GL20.glShaderSource(int,java.lang.String)"""
        pass

    @abstractmethod
    def glPushDebugGroup(self, arg0: int, arg1: int, arg2: str):
        """public abstract void com.badlogic.gdx.graphics.GL32.glPushDebugGroup(int,int,java.lang.String)"""
        pass

    @abstractmethod
    def glClearBufferfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetUniformLocation(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetUniformLocation(int,java.lang.String)"""
        pass

    @abstractmethod
    def glGetUniformiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetUniformiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGenVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenVertexArrays(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glPolygonOffset(self, arg0: float, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glPolygonOffset(float,float)"""
        pass

    @abstractmethod
    def glProgramParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glProgramParameteri(int,int,int)"""
        pass

    @abstractmethod
    def glDebugMessageControl(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer', arg4: bool):
        """public abstract void com.badlogic.gdx.graphics.GL32.glDebugMessageControl(int,int,int,java.nio.IntBuffer,boolean)"""
        pass

    @abstractmethod
    def glGetBooleanv(self, arg0: int, arg1: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetBooleanv(int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glStencilMaskSeparate(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilMaskSeparate(int,int)"""
        pass

    @abstractmethod
    def glGetnUniformuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL32.glGetnUniformuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glCreateProgram(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCreateProgram()"""
        pass

    @abstractmethod
    def glTexParameterIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL32.glTexParameterIiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetSamplerParameterIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL32.glGetSamplerParameterIiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glHint(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glHint(int,int)"""
        pass

    @abstractmethod
    def glBindVertexBuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glBindVertexBuffer(int,int,long,int)"""
        pass

    @abstractmethod
    def glDrawArraysIndirect(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glDrawArraysIndirect(int,long)"""
        pass

    @abstractmethod
    def glSampleMaski(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glSampleMaski(int,int)"""
        pass

    @abstractmethod
    def glDeleteSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteSamplers(int,int[],int)"""
        pass

    @abstractmethod
    def glGenFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenFramebuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteTransformFeedbacks(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteFramebuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteFramebuffer(int)"""
        pass

    @abstractmethod
    def glIsSampler(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsSampler(int)"""
        pass

    @abstractmethod
    def glDeleteQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteQueries(int,int[],int)"""
        pass

    @abstractmethod
    def glBindBuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindBuffer(int,int)"""
        pass

    @abstractmethod
    def glGenTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenTextures(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform2uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUnmapBuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glUnmapBuffer(int)"""
        pass

    @abstractmethod
    def glDrawRangeElementsBaseVertex(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'Buffer', arg6: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glDrawRangeElementsBaseVertex(int,int,int,int,int,java.nio.Buffer,int)"""
        pass

    @abstractmethod
    def glGenVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenVertexArrays(int,int[],int)"""
        pass

    @abstractmethod
    def glViewport(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glViewport(int,int,int,int)"""
        pass

    @abstractmethod
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawRangeElements(int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetQueryiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetQueryiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetVertexAttribIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetVertexAttribIuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenTransformFeedbacks(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glDebugMessageInsert(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: str):
        """public abstract void com.badlogic.gdx.graphics.GL32.glDebugMessageInsert(int,int,int,int,java.lang.String)"""
        pass

    @abstractmethod
    def glDispatchComputeIndirect(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glDispatchComputeIndirect(long)"""
        pass

    @abstractmethod
    def glVertexAttribFormat(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glVertexAttribFormat(int,int,int,boolean,int)"""
        pass

    @abstractmethod
    def glFlush(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFlush()"""
        pass

    @abstractmethod
    def glClear(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClear(int)"""
        pass

    @abstractmethod
    def glActiveTexture(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glActiveTexture(int)"""
        pass

    @abstractmethod
    def glBlendEquationi(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glBlendEquationi(int,int)"""
        pass

    @abstractmethod
    def glCopyTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glCopyTexSubImage3D(int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glAttachShader(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glAttachShader(int,int)"""
        pass

    @abstractmethod
    def glIsTexture(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsTexture(int)"""
        pass

    @abstractmethod
    def glProgramUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glVertexAttrib4fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib4fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glObjectLabel(self, arg0: int, arg1: int, arg2: str):
        """public abstract void com.badlogic.gdx.graphics.GL32.glObjectLabel(int,int,java.lang.String)"""
        pass

    @abstractmethod
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTransformFeedbackVaryings(self, arg0: int, arg1: 'String', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTransformFeedbackVaryings(int,java.lang.String[],int)"""
        pass

    @abstractmethod
    def glUniformMatrix4x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix4x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGenProgramPipelines(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGenProgramPipelines(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteBuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glBindImageTexture(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int, arg6: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glBindImageTexture(int,int,int,boolean,int,int,int)"""
        pass

    @abstractmethod
    def glReadBuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glReadBuffer(int)"""
        pass

    @abstractmethod
    def glProgramUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glFramebufferTexture2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFramebufferTexture2D(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetTexLevelParameterfv(self, arg0: int, arg1: int, arg2: int, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetTexLevelParameterfv(int,int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGenerateMipmap(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenerateMipmap(int)"""
        pass

    @abstractmethod
    def glGetVertexAttribIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetVertexAttribIiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3f(int,float,float,float)"""
        pass

    @abstractmethod
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribPointer(int,int,int,boolean,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glDeleteFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteFramebuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glIsQuery(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsQuery(int)"""
        pass

    @abstractmethod
    def glGenSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenSamplers(int,int[],int)"""
        pass

    @abstractmethod
    def glProgramUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawRangeElements(int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glVertexAttrib1fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib1fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glCompressedTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompressedTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glValidateProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glValidateProgram(int)"""
        pass

    @abstractmethod
    def glIsEnabledi(self, arg0: int, arg1: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL32.glIsEnabledi(int,int)"""
        pass

    @abstractmethod
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexSubImage2D(int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniform2i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2i(int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix2x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix2x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetProgramInfoLog(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetProgramInfoLog(int)"""
        pass

    @abstractmethod
    def glGetFloatv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetFloatv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glTexStorage2DMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool):
        """public abstract void com.badlogic.gdx.graphics.GL31.glTexStorage2DMultisample(int,int,int,int,int,boolean)"""
        pass

    @abstractmethod
    def glGetSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glStencilOpSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilOpSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glStencilFunc(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilFunc(int,int,int)"""
        pass

    @abstractmethod
    def glGetVertexAttribPointerv(self, arg0: int, arg1: int, arg2: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribPointerv(int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glColorMask(self, arg0: bool, arg1: bool, arg2: bool, arg3: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glColorMask(boolean,boolean,boolean,boolean)"""
        pass

    @abstractmethod
    def glEnablei(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glEnablei(int,int)"""
        pass

    @abstractmethod
    def glBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBufferSubData(int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGetProgramResourceName(self, arg0: int, arg1: int, arg2: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL31.glGetProgramResourceName(int,int,int)"""
        pass

    @abstractmethod
    def glTexStorage3DMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: bool):
        """public abstract void com.badlogic.gdx.graphics.GL32.glTexStorage3DMultisample(int,int,int,int,int,int,boolean)"""
        pass

    @abstractmethod
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glDeleteShader(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteShader(int)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix3x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix3x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glRenderbufferStorage(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glRenderbufferStorage(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetShaderPrecisionFormat(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetShaderPrecisionFormat(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glScissor(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glScissor(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetnUniformiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL32.glGetnUniformiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetProgramPipelineiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetProgramPipelineiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetUniformIndices(self, arg0: int, arg1: 'String', arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetUniformIndices(int,java.lang.String[],java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttrib2fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib2fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glIsProgram(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsProgram(int)"""
        pass

    @abstractmethod
    def glGetProgramResourceIndex(self, arg0: int, arg1: int, arg2: str):
        """public abstract int com.badlogic.gdx.graphics.GL31.glGetProgramResourceIndex(int,int,java.lang.String)"""
        pass

    @abstractmethod
    def glProgramUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetUniformBlockIndex(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL30.glGetUniformBlockIndex(int,java.lang.String)"""
        pass

    @abstractmethod
    def glGetProgramResourceLocation(self, arg0: int, arg1: int, arg2: str):
        """public abstract int com.badlogic.gdx.graphics.GL31.glGetProgramResourceLocation(int,int,java.lang.String)"""
        pass

    @abstractmethod
    def glStencilFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilFuncSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform2f(self, arg0: int, arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2f(int,float,float)"""
        pass

    @abstractmethod
    def glDebugMessageCallback(self, arg0: 'DebugProc'):
        """public abstract void com.badlogic.gdx.graphics.GL32.glDebugMessageCallback(com.badlogic.gdx.graphics.GL32$DebugProc)"""
        pass

    @abstractmethod
    def glGetFramebufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetFramebufferParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform3ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3ui(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3i(int,int,int,int)"""
        pass

    @abstractmethod
    def glUniform1uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniform1uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform4uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniform4uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteVertexArrays(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDrawElementsInstancedBaseVertex(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer', arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glDrawElementsInstancedBaseVertex(int,int,int,java.nio.Buffer,int,int)"""
        pass

    @abstractmethod
    def glReadPixels(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glReadPixels(int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGetSamplerParameterIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL32.glGetSamplerParameterIuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlendFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendFuncSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glPatchParameteri(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glPatchParameteri(int,int)"""
        pass

    @abstractmethod
    def glGenBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenBuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glShaderBinary(self, arg0: int, arg1: 'IntBuffer', arg2: int, arg3: 'Buffer', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glShaderBinary(int,java.nio.IntBuffer,int,java.nio.Buffer,int)"""
        pass

    @abstractmethod
    def glSamplerParameterf(self, arg0: int, arg1: int, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameterf(int,int,float)"""
        pass

    @abstractmethod
    def glVertexAttribIPointer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribIPointer(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlendEquationSeparatei(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glBlendEquationSeparatei(int,int,int)"""
        pass

    @abstractmethod
    def glUniformMatrix2x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix2x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetFramebufferAttachmentParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetFramebufferAttachmentParameteriv(int,int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glCopyTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCopyTexImage2D(int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glEnable(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glEnable(int)"""
        pass

    @abstractmethod
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glVertexAttrib4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib4f(int,float,float,float,float)"""
        pass

    @abstractmethod
    def glGetActiveUniformsiv(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetActiveUniformsiv(int,int,java.nio.IntBuffer,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glBeginQuery(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBeginQuery(int,int)"""
        pass

    @abstractmethod
    def glGetObjectLabel(self, arg0: int, arg1: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL32.glGetObjectLabel(int,int)"""
        pass

    @abstractmethod
    def glGetTexParameterIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL32.glGetTexParameterIuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform1f(self, arg0: int, arg1: int, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1f(int,int,float)"""
        pass

    @abstractmethod
    def glProgramUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4i(int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3i(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetShaderiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetShaderiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glLinkProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glLinkProgram(int)"""
        pass

    @abstractmethod
    def glUniform2i(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2i(int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniform3uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetProgramPipelineInfoLog(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL31.glGetProgramPipelineInfoLog(int)"""
        pass

    @abstractmethod
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glTexBuffer(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glTexBuffer(int,int,int)"""
        pass

    @abstractmethod
    def glGetIntegerv(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetIntegerv(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetProgramInterfaceiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetProgramInterfaceiv(int,int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glPixelStorei(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glPixelStorei(int,int)"""
        pass

    @abstractmethod
    def glVertexAttrib2f(self, arg0: int, arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib2f(int,float,float)"""
        pass

    @abstractmethod
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexImage2D(int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glInvalidateSubFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: int, arg5: int, arg6: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glInvalidateSubFramebuffer(int,int,java.nio.IntBuffer,int,int,int,int)"""
        pass

    @abstractmethod
    def glActiveShaderProgram(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glActiveShaderProgram(int,int)"""
        pass

    @abstractmethod
    def glProgramUniform4ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4ui(int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDisablei(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glDisablei(int,int)"""
        pass

    @abstractmethod
    def glVertexAttribI4ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribI4ui(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glIsProgramPipeline(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL31.glIsProgramPipeline(int)"""
        pass

    @abstractmethod
    def glGenRenderbuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenRenderbuffer()"""
        pass

    @abstractmethod
    def glGetDebugMessageLog(self, arg0: int, arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: 'IntBuffer', arg6: 'ByteBuffer'):
        """public abstract int com.badlogic.gdx.graphics.GL32.glGetDebugMessageLog(int,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.ByteBuffer)"""
        pass

    @abstractmethod
    def glUniformMatrix3x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix3x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetInteger64v(self, arg0: int, arg1: 'LongBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetInteger64v(int,java.nio.LongBuffer)"""
        pass

    @abstractmethod
    def glSampleCoverage(self, arg0: float, arg1: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glSampleCoverage(float,boolean)"""
        pass

    @abstractmethod
    def glCompileShader(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompileShader(int)"""
        pass

    @abstractmethod
    def glGetAttachedShaders(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetAttachedShaders(int,int,java.nio.Buffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetStringi(self, arg0: int, arg1: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL30.glGetStringi(int,int)"""
        pass

    @abstractmethod
    def glCopyBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glCopyBufferSubData(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix4x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix4x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix4fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glEndTransformFeedback(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL30.glEndTransformFeedback()"""
        pass

    @abstractmethod
    def glDrawBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawBuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetTexParameterIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL32.glGetTexParameterIiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix3x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix3x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetTexLevelParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetTexLevelParameteriv(int,int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetFragDataLocation(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL30.glGetFragDataLocation(int,java.lang.String)"""
        pass

    @abstractmethod
    def glReadnPixels(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL32.glReadnPixels(int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGenTexture(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenTexture()"""
        pass

    @abstractmethod
    def glIsBuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsBuffer(int)"""
        pass

    @abstractmethod
    def glProgramUniform2f(self, arg0: int, arg1: int, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2f(int,int,float,float)"""
        pass

    @abstractmethod
    def glUseProgramStages(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glUseProgramStages(int,int,int)"""
        pass

    @abstractmethod
    def glTexParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameteri(int,int,int)"""
        pass

    @abstractmethod
    def glDrawArrays(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawArrays(int,int,int)"""
        pass

    @abstractmethod
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawElements(int,int,int,int)"""
        pass

    @abstractmethod
    def glGenQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenQueries(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribBinding(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glVertexAttribBinding(int,int)"""
        pass

    @abstractmethod
    def glGetProgramiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetProgramiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glIsVertexArray(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsVertexArray(int)"""
        pass

    @abstractmethod
    def glDepthFunc(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthFunc(int)"""
        pass

    @abstractmethod
    def glProgramUniform1ui(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1ui(int,int,int)"""
        pass

    @abstractmethod
    def glVertexBindingDivisor(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glVertexBindingDivisor(int,int)"""
        pass

    @abstractmethod
    def glGetActiveUniform(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetActiveUniform(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttribPointer(int,int,int,boolean,int,int)"""
        pass

    @abstractmethod
    def glTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetString(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetString(int)"""
        pass

    @abstractmethod
    def glCreateShaderProgramv(self, arg0: int, arg1: 'String'):
        """public abstract int com.badlogic.gdx.graphics.GL31.glCreateShaderProgramv(int,java.lang.String[])"""
        pass

    @abstractmethod
    def glGetProgramResourceiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetProgramResourceiv(int,int,int,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform4uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteRenderbuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteTexture(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteTexture(int)"""
        pass

    @abstractmethod
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glSamplerParameterIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL32.glSamplerParameterIuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDepthMask(self, arg0: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthMask(boolean)"""
        pass

    @abstractmethod
    def glProgramUniform1uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4i(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glBufferData(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBufferData(int,int,java.nio.Buffer,int)"""
        pass

    @abstractmethod
    def glBlendBarrier(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL32.glBlendBarrier()"""
        pass

    @abstractmethod
    def glClearBufferiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDispatchCompute(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glDispatchCompute(int,int,int)"""
        pass

    @abstractmethod
    def glPauseTransformFeedback(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL30.glPauseTransformFeedback()"""
        pass

    @abstractmethod
    def glMemoryBarrier(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glMemoryBarrier(int)"""
        pass

    @abstractmethod
    def glGetVertexAttribiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFramebufferRenderbuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFramebufferRenderbuffer(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetQueryObjectuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetQueryObjectuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetTexParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glDrawElementsBaseVertex(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glDrawElementsBaseVertex(int,int,int,java.nio.Buffer,int)"""
        pass

    @abstractmethod
    def glIsEnabled(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsEnabled(int)"""
        pass

    @abstractmethod
    def glColorMaski(self, arg0: int, arg1: bool, arg2: bool, arg3: bool, arg4: bool):
        """public abstract void com.badlogic.gdx.graphics.GL32.glColorMaski(int,boolean,boolean,boolean,boolean)"""
        pass

    @abstractmethod
    def glGenRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenRenderbuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glMemoryBarrierByRegion(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glMemoryBarrierByRegion(int)"""
        pass

    @abstractmethod
    def glFlushMappedBufferRange(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glFlushMappedBufferRange(int,int,int)"""
        pass

    @abstractmethod
    def glInvalidateFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glInvalidateFramebuffer(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glBindRenderbuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindRenderbuffer(int,int)"""
        pass

    @abstractmethod
    def glGetGraphicsResetStatus(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL32.glGetGraphicsResetStatus()"""
        pass

    @abstractmethod
    def glEnableVertexAttribArray(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glEnableVertexAttribArray(int)"""
        pass

    @abstractmethod
    def glIsFramebuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsFramebuffer(int)"""
        pass

    @abstractmethod
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glCopyImageSubData(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glCopyImageSubData(int,int,int,int,int,int,int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glValidateProgramPipeline(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glValidateProgramPipeline(int)"""
        pass

    @abstractmethod
    def glBlendFunc(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendFunc(int,int)"""
        pass

    @abstractmethod
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix4x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix4x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBindBufferBase(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindBufferBase(int,int,int)"""
        pass

    @abstractmethod
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGetTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetTexParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTexParameterf(self, arg0: int, arg1: int, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameterf(int,int,float)"""
        pass

    @abstractmethod
    def glBindAttribLocation(self, arg0: int, arg1: int, arg2: str):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindAttribLocation(int,int,java.lang.String)"""
        pass

    @abstractmethod
    def glSamplerParameterIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL32.glSamplerParameterIiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFramebufferTexture(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glFramebufferTexture(int,int,int,int)"""
        pass

    @abstractmethod
    def glGenSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenSamplers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFramebufferTextureLayer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glFramebufferTextureLayer(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDisableVertexAttribArray(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDisableVertexAttribArray(int)"""
        pass

    @abstractmethod
    def glTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glDeleteQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteQueries(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribDivisor(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribDivisor(int,int)"""
        pass

    @abstractmethod
    def glCopyTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCopyTexSubImage2D(int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetVertexAttribfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribIFormat(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glVertexAttribIFormat(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetBufferPointerv(self, arg0: int, arg1: int):
        """public abstract java.nio.Buffer com.badlogic.gdx.graphics.GL30.glGetBufferPointerv(int,int)"""
        pass

    @abstractmethod
    def glDeleteProgramPipelines(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glDeleteProgramPipelines(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTexParameterIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL32.glTexParameterIuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFrontFace(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFrontFace(int)"""
        pass

    @abstractmethod
    def glSamplerParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameteri(int,int,int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.FPSLogger
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.FPSLogger as _FPSLogger
_FPSLogger = _FPSLogger
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FPSLogger():
    """com.badlogic.gdx.graphics.FPSLogger"""
 
    @staticmethod
    def _wrap(java_value: _FPSLogger) -> 'FPSLogger':
        return FPSLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FPSLogger):
        """
        Dynamic initializer for FPSLogger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FPSLogger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FPSLogger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.FPSLogger()"""
        val = _FPSLogger()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.FPSLogger(int)"""
        val = _FPSLogger(_int.valueOf(arg0))
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
    def log(self):
        """public void com.badlogic.gdx.graphics.FPSLogger.log()"""
        super(FPSLogger, self).log()

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
    def __init__(self):
        """public com.badlogic.gdx.graphics.FPSLogger()"""
        val = _FPSLogger()
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.Mesh$VertexDataType
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
from builtins import bool
import com.badlogic.gdx.graphics.Mesh as _Mesh_VertexDataType
_VertexDataType = _Mesh_VertexDataType.VertexDataType
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class VertexDataType():
    """com.badlogic.gdx.graphics.Mesh.VertexDataType"""
 
    @staticmethod
    def _wrap(java_value: _VertexDataType) -> 'VertexDataType':
        return VertexDataType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _VertexDataType):
        """
        Dynamic initializer for VertexDataType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_VertexDataType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_VertexDataType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def values() -> List['VertexDataType']:
        """public static com.badlogic.gdx.graphics.Mesh$VertexDataType[] com.badlogic.gdx.graphics.Mesh$VertexDataType.values()"""
        return List[VertexDataType]._wrap(_VertexDataType.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'VertexDataType':
        """public static com.badlogic.gdx.graphics.Mesh$VertexDataType com.badlogic.gdx.graphics.Mesh$VertexDataType.valueOf(java.lang.String)"""
        return VertexDataType._wrap(_VertexDataType.valueOf(arg0))

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
 
 
# CLASS: com.badlogic.gdx.graphics.Texture$TextureWrap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.Texture as _Texture_TextureWrap
_TextureWrap = _Texture_TextureWrap.TextureWrap
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextureWrap():
    """com.badlogic.gdx.graphics.Texture.TextureWrap"""
 
    @staticmethod
    def _wrap(java_value: _TextureWrap) -> 'TextureWrap':
        return TextureWrap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureWrap):
        """
        Dynamic initializer for TextureWrap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureWrap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureWrap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'TextureWrap':
        """public static com.badlogic.gdx.graphics.Texture$TextureWrap com.badlogic.gdx.graphics.Texture$TextureWrap.valueOf(java.lang.String)"""
        return TextureWrap._wrap(_TextureWrap.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['TextureWrap']:
        """public static com.badlogic.gdx.graphics.Texture$TextureWrap[] com.badlogic.gdx.graphics.Texture$TextureWrap.values()"""
        return List[TextureWrap]._wrap(_TextureWrap.values())

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
    def getGLEnum(self) -> int:
        """public int com.badlogic.gdx.graphics.Texture$TextureWrap.getGLEnum()"""
        return int._wrap(super(TextureWrap, self).getGLEnum())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.GL30
from builtins import str
import com.badlogic.gdx.graphics.GL30 as _GL30
_GL30 = _GL30
import java.nio.IntBuffer as IntBuffer
import java.nio.Buffer as Buffer
from builtins import float
import java.nio.LongBuffer as LongBuffer
from abc import abstractmethod, ABC
import java.nio.FloatBuffer as FloatBuffer
from builtins import int
import com.badlogic.gdx.graphics.GL20 as _GL20
_GL20 = _GL20
 
class GL30():
    """com.badlogic.gdx.graphics.GL30"""
 
    @staticmethod
    def _wrap(java_value: _GL30) -> 'GL30':
        return GL30(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GL30):
        """
        Dynamic initializer for GL30.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GL30__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GL30__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def glDrawElementsInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawElementsInstanced(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glIsRenderbuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsRenderbuffer(int)"""
        pass

    @abstractmethod
    def glCreateShader(self, arg0: int):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCreateShader(int)"""
        pass

    @abstractmethod
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetActiveUniformBlockName(int,int,java.nio.Buffer,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glBindTransformFeedback(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindTransformFeedback(int,int)"""
        pass

    @abstractmethod
    def glGetActiveAttrib(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetActiveAttrib(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribI4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribI4i(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDeleteVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteVertexArrays(int,int[],int)"""
        pass

    @abstractmethod
    def glGetUniformuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetUniformuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glResumeTransformFeedback(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL30.glResumeTransformFeedback()"""
        pass

    @abstractmethod
    def glUniform4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4f(int,float,float,float,float)"""
        pass

    @abstractmethod
    def glBindFramebuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindFramebuffer(int,int)"""
        pass

    @abstractmethod
    def glDisable(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDisable(int)"""
        pass

    @abstractmethod
    def glBlendColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendColor(float,float,float,float)"""
        pass

    @abstractmethod
    def glGenBuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenBuffer()"""
        pass

    @abstractmethod
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glBlendEquationSeparate(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendEquationSeparate(int,int)"""
        pass

    @abstractmethod
    def glDeleteProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteProgram(int)"""
        pass

    @abstractmethod
    def glGenQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenQueries(int,int[],int)"""
        pass

    @abstractmethod
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glRenderbufferStorageMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glRenderbufferStorageMultisample(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glCullFace(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCullFace(int)"""
        pass

    @abstractmethod
    def glLineWidth(self, arg0: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glLineWidth(float)"""
        pass

    @abstractmethod
    def glVertexAttrib3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib3f(int,float,float,float)"""
        pass

    @abstractmethod
    def glCompressedTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompressedTexImage2D(int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glStencilMask(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilMask(int)"""
        pass

    @abstractmethod
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix3fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glUniformMatrix3x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix3x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetActiveUniformBlockiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetActiveUniformBlockiv(int,int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDepthRangef(self, arg0: float, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthRangef(float,float)"""
        pass

    @abstractmethod
    def glUniform1f(self, arg0: int, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1f(int,float)"""
        pass

    @abstractmethod
    def glGetError(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetError()"""
        pass

    @abstractmethod
    def glVertexAttrib1f(self, arg0: int, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib1f(int,float)"""
        pass

    @abstractmethod
    def glUniformMatrix4x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix4x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlitFramebuffer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBlitFramebuffer(int,int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glClearBufferuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetBufferParameteri64v(self, arg0: int, arg1: int, arg2: 'LongBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetBufferParameteri64v(int,int,java.nio.LongBuffer)"""
        pass

    @abstractmethod
    def glDetachShader(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDetachShader(int,int)"""
        pass

    @abstractmethod
    def glClearColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearColor(float,float,float,float)"""
        pass

    @abstractmethod
    def glDeleteSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteSamplers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glIsTransformFeedback(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsTransformFeedback(int)"""
        pass

    @abstractmethod
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix2fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glGetUniformfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetUniformfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glDrawArraysInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawArraysInstanced(int,int,int,int)"""
        pass

    @abstractmethod
    def glUniformBlockBinding(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformBlockBinding(int,int,int)"""
        pass

    @abstractmethod
    def glDeleteBuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteBuffer(int)"""
        pass

    @abstractmethod
    def glBeginTransformFeedback(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBeginTransformFeedback(int)"""
        pass

    @abstractmethod
    def glGetAttribLocation(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetAttribLocation(int,java.lang.String)"""
        pass

    @abstractmethod
    def glSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glVertexAttrib3fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib3fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glDeleteTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteTextures(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexImage3D(int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glBindVertexArray(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindVertexArray(int)"""
        pass

    @abstractmethod
    def glUniform1i(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1i(int,int)"""
        pass

    @abstractmethod
    def glUniform3uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniform3uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glClearStencil(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearStencil(int)"""
        pass

    @abstractmethod
    def glGetShaderInfoLog(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetShaderInfoLog(int)"""
        pass

    @abstractmethod
    def glEndQuery(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glEndQuery(int)"""
        pass

    @abstractmethod
    def glIsShader(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsShader(int)"""
        pass

    @abstractmethod
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexImage3D(int,int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteTransformFeedbacks(int,int[],int)"""
        pass

    @abstractmethod
    def glDeleteRenderbuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteRenderbuffer(int)"""
        pass

    @abstractmethod
    def glGenFramebuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenFramebuffer()"""
        pass

    @abstractmethod
    def glBindSampler(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindSampler(int,int)"""
        pass

    @abstractmethod
    def glUseProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUseProgram(int)"""
        pass

    @abstractmethod
    def glFinish(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFinish()"""
        pass

    @abstractmethod
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBindBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindBufferRange(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glReleaseShaderCompiler(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glReleaseShaderCompiler()"""
        pass

    @abstractmethod
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawElements(int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL30.glGetActiveUniformBlockName(int,int)"""
        pass

    @abstractmethod
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glUniformMatrix2x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix2x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glClearDepthf(self, arg0: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearDepthf(float)"""
        pass

    @abstractmethod
    def glStencilOp(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilOp(int,int,int)"""
        pass

    @abstractmethod
    def glMapBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract java.nio.Buffer com.badlogic.gdx.graphics.GL30.glMapBufferRange(int,int,int,int)"""
        pass

    @abstractmethod
    def glBlendEquation(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendEquation(int)"""
        pass

    @abstractmethod
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenTransformFeedbacks(int,int[],int)"""
        pass

    @abstractmethod
    def glCheckFramebufferStatus(self, arg0: int):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCheckFramebufferStatus(int)"""
        pass

    @abstractmethod
    def glBindTexture(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindTexture(int,int)"""
        pass

    @abstractmethod
    def glGetBufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetBufferParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetRenderbufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetRenderbufferParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glClearBufferfi(self, arg0: int, arg1: int, arg2: float, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferfi(int,int,float,int)"""
        pass

    @abstractmethod
    def glShaderSource(self, arg0: int, arg1: str):
        """public abstract void com.badlogic.gdx.graphics.GL20.glShaderSource(int,java.lang.String)"""
        pass

    @abstractmethod
    def glClearBufferfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetUniformLocation(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetUniformLocation(int,java.lang.String)"""
        pass

    @abstractmethod
    def glGetUniformiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetUniformiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGenVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenVertexArrays(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glPolygonOffset(self, arg0: float, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glPolygonOffset(float,float)"""
        pass

    @abstractmethod
    def glProgramParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glProgramParameteri(int,int,int)"""
        pass

    @abstractmethod
    def glGetBooleanv(self, arg0: int, arg1: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetBooleanv(int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glStencilMaskSeparate(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilMaskSeparate(int,int)"""
        pass

    @abstractmethod
    def glCreateProgram(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCreateProgram()"""
        pass

    @abstractmethod
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glHint(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glHint(int,int)"""
        pass

    @abstractmethod
    def glDeleteSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteSamplers(int,int[],int)"""
        pass

    @abstractmethod
    def glGenFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenFramebuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteTransformFeedbacks(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteFramebuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteFramebuffer(int)"""
        pass

    @abstractmethod
    def glIsSampler(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsSampler(int)"""
        pass

    @abstractmethod
    def glDeleteQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteQueries(int,int[],int)"""
        pass

    @abstractmethod
    def glBindBuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindBuffer(int,int)"""
        pass

    @abstractmethod
    def glGenTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenTextures(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUnmapBuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glUnmapBuffer(int)"""
        pass

    @abstractmethod
    def glGenVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenVertexArrays(int,int[],int)"""
        pass

    @abstractmethod
    def glViewport(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glViewport(int,int,int,int)"""
        pass

    @abstractmethod
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawRangeElements(int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetQueryiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetQueryiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetVertexAttribIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetVertexAttribIuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenTransformFeedbacks(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glFlush(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFlush()"""
        pass

    @abstractmethod
    def glClear(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClear(int)"""
        pass

    @abstractmethod
    def glActiveTexture(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glActiveTexture(int)"""
        pass

    @abstractmethod
    def glCopyTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glCopyTexSubImage3D(int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glAttachShader(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glAttachShader(int,int)"""
        pass

    @abstractmethod
    def glIsTexture(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsTexture(int)"""
        pass

    @abstractmethod
    def glVertexAttrib4fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib4fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTransformFeedbackVaryings(self, arg0: int, arg1: 'String', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTransformFeedbackVaryings(int,java.lang.String[],int)"""
        pass

    @abstractmethod
    def glUniformMatrix4x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix4x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glDeleteBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteBuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glReadBuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glReadBuffer(int)"""
        pass

    @abstractmethod
    def glFramebufferTexture2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFramebufferTexture2D(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGenerateMipmap(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenerateMipmap(int)"""
        pass

    @abstractmethod
    def glGetVertexAttribIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetVertexAttribIiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3f(int,float,float,float)"""
        pass

    @abstractmethod
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribPointer(int,int,int,boolean,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glDeleteFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteFramebuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glIsQuery(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsQuery(int)"""
        pass

    @abstractmethod
    def glGenSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenSamplers(int,int[],int)"""
        pass

    @abstractmethod
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawRangeElements(int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glVertexAttrib1fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib1fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glCompressedTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompressedTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glValidateProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glValidateProgram(int)"""
        pass

    @abstractmethod
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexSubImage2D(int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetProgramInfoLog(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetProgramInfoLog(int)"""
        pass

    @abstractmethod
    def glGetFloatv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetFloatv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glStencilOpSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilOpSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glStencilFunc(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilFunc(int,int,int)"""
        pass

    @abstractmethod
    def glGetVertexAttribPointerv(self, arg0: int, arg1: int, arg2: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribPointerv(int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glColorMask(self, arg0: bool, arg1: bool, arg2: bool, arg3: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glColorMask(boolean,boolean,boolean,boolean)"""
        pass

    @abstractmethod
    def glBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBufferSubData(int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glDeleteShader(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteShader(int)"""
        pass

    @abstractmethod
    def glRenderbufferStorage(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glRenderbufferStorage(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetShaderPrecisionFormat(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetShaderPrecisionFormat(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glScissor(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glScissor(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetUniformIndices(self, arg0: int, arg1: 'String', arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetUniformIndices(int,java.lang.String[],java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttrib2fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib2fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glIsProgram(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsProgram(int)"""
        pass

    @abstractmethod
    def glGetUniformBlockIndex(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL30.glGetUniformBlockIndex(int,java.lang.String)"""
        pass

    @abstractmethod
    def glStencilFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilFuncSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform2f(self, arg0: int, arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2f(int,float,float)"""
        pass

    @abstractmethod
    def glUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3i(int,int,int,int)"""
        pass

    @abstractmethod
    def glUniform1uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniform1uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform4uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniform4uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteVertexArrays(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glReadPixels(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glReadPixels(int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlendFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendFuncSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glGenBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenBuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glShaderBinary(self, arg0: int, arg1: 'IntBuffer', arg2: int, arg3: 'Buffer', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glShaderBinary(int,java.nio.IntBuffer,int,java.nio.Buffer,int)"""
        pass

    @abstractmethod
    def glSamplerParameterf(self, arg0: int, arg1: int, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameterf(int,int,float)"""
        pass

    @abstractmethod
    def glVertexAttribIPointer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribIPointer(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glUniformMatrix2x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix2x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetFramebufferAttachmentParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetFramebufferAttachmentParameteriv(int,int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glCopyTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCopyTexImage2D(int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glEnable(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glEnable(int)"""
        pass

    @abstractmethod
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glVertexAttrib4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib4f(int,float,float,float,float)"""
        pass

    @abstractmethod
    def glGetActiveUniformsiv(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetActiveUniformsiv(int,int,java.nio.IntBuffer,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glBeginQuery(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBeginQuery(int,int)"""
        pass

    @abstractmethod
    def glGetShaderiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetShaderiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glLinkProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glLinkProgram(int)"""
        pass

    @abstractmethod
    def glUniform2i(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2i(int,int,int)"""
        pass

    @abstractmethod
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetIntegerv(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetIntegerv(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glPixelStorei(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glPixelStorei(int,int)"""
        pass

    @abstractmethod
    def glVertexAttrib2f(self, arg0: int, arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib2f(int,float,float)"""
        pass

    @abstractmethod
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexImage2D(int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glInvalidateSubFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: int, arg5: int, arg6: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glInvalidateSubFramebuffer(int,int,java.nio.IntBuffer,int,int,int,int)"""
        pass

    @abstractmethod
    def glVertexAttribI4ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribI4ui(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGenRenderbuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenRenderbuffer()"""
        pass

    @abstractmethod
    def glUniformMatrix3x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix3x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetInteger64v(self, arg0: int, arg1: 'LongBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetInteger64v(int,java.nio.LongBuffer)"""
        pass

    @abstractmethod
    def glSampleCoverage(self, arg0: float, arg1: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glSampleCoverage(float,boolean)"""
        pass

    @abstractmethod
    def glCompileShader(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompileShader(int)"""
        pass

    @abstractmethod
    def glGetAttachedShaders(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetAttachedShaders(int,int,java.nio.Buffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetStringi(self, arg0: int, arg1: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL30.glGetStringi(int,int)"""
        pass

    @abstractmethod
    def glCopyBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glCopyBufferSubData(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix4fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glEndTransformFeedback(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL30.glEndTransformFeedback()"""
        pass

    @abstractmethod
    def glDrawBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawBuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetFragDataLocation(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL30.glGetFragDataLocation(int,java.lang.String)"""
        pass

    @abstractmethod
    def glGenTexture(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenTexture()"""
        pass

    @abstractmethod
    def glIsBuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsBuffer(int)"""
        pass

    @abstractmethod
    def glTexParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameteri(int,int,int)"""
        pass

    @abstractmethod
    def glDrawArrays(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawArrays(int,int,int)"""
        pass

    @abstractmethod
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawElements(int,int,int,int)"""
        pass

    @abstractmethod
    def glGenQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenQueries(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetProgramiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetProgramiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glIsVertexArray(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsVertexArray(int)"""
        pass

    @abstractmethod
    def glDepthFunc(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthFunc(int)"""
        pass

    @abstractmethod
    def glGetActiveUniform(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetActiveUniform(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttribPointer(int,int,int,boolean,int,int)"""
        pass

    @abstractmethod
    def glTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetString(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetString(int)"""
        pass

    @abstractmethod
    def glDeleteRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteRenderbuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteTexture(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteTexture(int)"""
        pass

    @abstractmethod
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glDepthMask(self, arg0: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthMask(boolean)"""
        pass

    @abstractmethod
    def glUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4i(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glBufferData(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBufferData(int,int,java.nio.Buffer,int)"""
        pass

    @abstractmethod
    def glClearBufferiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glPauseTransformFeedback(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL30.glPauseTransformFeedback()"""
        pass

    @abstractmethod
    def glGetVertexAttribiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFramebufferRenderbuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFramebufferRenderbuffer(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetQueryObjectuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetQueryObjectuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetTexParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glIsEnabled(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsEnabled(int)"""
        pass

    @abstractmethod
    def glGenRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenRenderbuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFlushMappedBufferRange(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glFlushMappedBufferRange(int,int,int)"""
        pass

    @abstractmethod
    def glInvalidateFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glInvalidateFramebuffer(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glBindRenderbuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindRenderbuffer(int,int)"""
        pass

    @abstractmethod
    def glEnableVertexAttribArray(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glEnableVertexAttribArray(int)"""
        pass

    @abstractmethod
    def glIsFramebuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsFramebuffer(int)"""
        pass

    @abstractmethod
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlendFunc(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendFunc(int,int)"""
        pass

    @abstractmethod
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBindBufferBase(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindBufferBase(int,int,int)"""
        pass

    @abstractmethod
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGetTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetTexParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTexParameterf(self, arg0: int, arg1: int, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameterf(int,int,float)"""
        pass

    @abstractmethod
    def glBindAttribLocation(self, arg0: int, arg1: int, arg2: str):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindAttribLocation(int,int,java.lang.String)"""
        pass

    @abstractmethod
    def glGenSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenSamplers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFramebufferTextureLayer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glFramebufferTextureLayer(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDisableVertexAttribArray(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDisableVertexAttribArray(int)"""
        pass

    @abstractmethod
    def glTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glDeleteQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteQueries(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribDivisor(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribDivisor(int,int)"""
        pass

    @abstractmethod
    def glCopyTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCopyTexSubImage2D(int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetVertexAttribfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetBufferPointerv(self, arg0: int, arg1: int):
        """public abstract java.nio.Buffer com.badlogic.gdx.graphics.GL30.glGetBufferPointerv(int,int)"""
        pass

    @abstractmethod
    def glFrontFace(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFrontFace(int)"""
        pass

    @abstractmethod
    def glSamplerParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameteri(int,int,int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.VertexAttribute
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.VertexAttribute as _VertexAttribute
_VertexAttribute = _VertexAttribute
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class VertexAttribute():
    """com.badlogic.gdx.graphics.VertexAttribute"""
 
    @staticmethod
    def _wrap(java_value: _VertexAttribute) -> 'VertexAttribute':
        return VertexAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _VertexAttribute):
        """
        Dynamic initializer for VertexAttribute.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_VertexAttribute__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_VertexAttribute__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def copy(self) -> 'VertexAttribute':
        """public com.badlogic.gdx.graphics.VertexAttribute com.badlogic.gdx.graphics.VertexAttribute.copy()"""
        return 'VertexAttribute'._wrap(super(VertexAttribute, self).copy())

    @staticmethod
    @overload
    def Normal() -> 'VertexAttribute':
        """public static com.badlogic.gdx.graphics.VertexAttribute com.badlogic.gdx.graphics.VertexAttribute.Normal()"""
        return VertexAttribute._wrap(_VertexAttribute.Normal())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: str, arg3: int):
        """public com.badlogic.gdx.graphics.VertexAttribute(int,int,java.lang.String,int)"""
        val = _VertexAttribute(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: str):
        """public com.badlogic.gdx.graphics.VertexAttribute(int,int,int,boolean,java.lang.String)"""
        val = _VertexAttribute(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), arg4)
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

    @staticmethod
    @overload
    def ColorUnpacked() -> 'VertexAttribute':
        """public static com.badlogic.gdx.graphics.VertexAttribute com.badlogic.gdx.graphics.VertexAttribute.ColorUnpacked()"""
        return VertexAttribute._wrap(_VertexAttribute.ColorUnpacked())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: str, arg5: int):
        """public com.badlogic.gdx.graphics.VertexAttribute(int,int,int,boolean,java.lang.String,int)"""
        val = _VertexAttribute(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), arg4, _int.valueOf(arg5))
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.VertexAttribute.hashCode()"""
        return int._wrap(super(VertexAttribute, self).hashCode())

    @staticmethod
    @overload
    def Binormal() -> 'VertexAttribute':
        """public static com.badlogic.gdx.graphics.VertexAttribute com.badlogic.gdx.graphics.VertexAttribute.Binormal()"""
        return VertexAttribute._wrap(_VertexAttribute.Binormal())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def ColorPacked() -> 'VertexAttribute':
        """public static com.badlogic.gdx.graphics.VertexAttribute com.badlogic.gdx.graphics.VertexAttribute.ColorPacked()"""
        return VertexAttribute._wrap(_VertexAttribute.ColorPacked())

    @overload
    def equals(self, arg0: 'VertexAttribute') -> bool:
        """public boolean com.badlogic.gdx.graphics.VertexAttribute.equals(com.badlogic.gdx.graphics.VertexAttribute)"""
        return bool._wrap(super(_VertexAttribute, self).equals(arg0))

    @staticmethod
    @overload
    def TexCoords(arg0: int) -> 'VertexAttribute':
        """public static com.badlogic.gdx.graphics.VertexAttribute com.badlogic.gdx.graphics.VertexAttribute.TexCoords(int)"""
        return VertexAttribute._wrap(_VertexAttribute.TexCoords(_int.valueOf(arg0)))

    @overload
    def getSizeInBytes(self) -> int:
        """public int com.badlogic.gdx.graphics.VertexAttribute.getSizeInBytes()"""
        return int._wrap(super(VertexAttribute, self).getSizeInBytes())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def Position() -> 'VertexAttribute':
        """public static com.badlogic.gdx.graphics.VertexAttribute com.badlogic.gdx.graphics.VertexAttribute.Position()"""
        return VertexAttribute._wrap(_VertexAttribute.Position())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.VertexAttribute.equals(java.lang.Object)"""
        return bool._wrap(super(_VertexAttribute, self).equals(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: str):
        """public com.badlogic.gdx.graphics.VertexAttribute(int,int,java.lang.String)"""
        val = _VertexAttribute(_int.valueOf(arg0), _int.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def BoneWeight(arg0: int) -> 'VertexAttribute':
        """public static com.badlogic.gdx.graphics.VertexAttribute com.badlogic.gdx.graphics.VertexAttribute.BoneWeight(int)"""
        return VertexAttribute._wrap(_VertexAttribute.BoneWeight(_int.valueOf(arg0)))

    @overload
    def getKey(self) -> int:
        """public int com.badlogic.gdx.graphics.VertexAttribute.getKey()"""
        return int._wrap(super(VertexAttribute, self).getKey())

    @staticmethod
    @overload
    def Tangent() -> 'VertexAttribute':
        """public static com.badlogic.gdx.graphics.VertexAttribute com.badlogic.gdx.graphics.VertexAttribute.Tangent()"""
        return VertexAttribute._wrap(_VertexAttribute.Tangent()) 
 
 
# CLASS: com.badlogic.gdx.graphics.Color
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Float as _float
import java.lang.String as _string
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Color():
    """com.badlogic.gdx.graphics.Color"""
 
    @staticmethod
    def _wrap(java_value: _Color) -> 'Color':
        return Color(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Color):
        """
        Dynamic initializer for Color.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Color__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Color__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def add(self, arg0: 'Color') -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.add(com.badlogic.gdx.graphics.Color)"""
        return 'Color'._wrap(super(_Color, self).add(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.Color()"""
        val = _Color()
        self.__wrapper = val

    @staticmethod
    @overload
    def toFloatBits(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.graphics.Color.toFloatBits(float,float,float,float)"""
        return float._wrap(_Color.toFloatBits(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Color':
        """public static com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.valueOf(java.lang.String)"""
        return Color._wrap(_Color.valueOf(arg0))

    @overload
    def toIntBits(self) -> int:
        """public int com.badlogic.gdx.graphics.Color.toIntBits()"""
        return int._wrap(super(Color, self).toIntBits())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def rgba8888ToColor(arg0: 'Color', arg1: int):
        """public static void com.badlogic.gdx.graphics.Color.rgba8888ToColor(com.badlogic.gdx.graphics.Color,int)"""
        _Color.rgba8888ToColor(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def rgb565(arg0: float, arg1: float, arg2: float) -> int:
        """public static int com.badlogic.gdx.graphics.Color.rgb565(float,float,float)"""
        return int._wrap(_Color.rgb565(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

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
    def mul(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.mul(float,float,float,float)"""
        return 'Color'._wrap(super(_Color, self).mul(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @staticmethod
    @overload
    def rgba4444(arg0: float, arg1: float, arg2: float, arg3: float) -> int:
        """public static int com.badlogic.gdx.graphics.Color.rgba4444(float,float,float,float)"""
        return int._wrap(_Color.rgba4444(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def mul(self, arg0: float) -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.mul(float)"""
        return 'Color'._wrap(super(_Color, self).mul(_float.valueOf(arg0)))

    @overload
    def set(self, arg0: 'Color') -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.set(com.badlogic.gdx.graphics.Color)"""
        return 'Color'._wrap(super(_Color, self).set(arg0))

    @staticmethod
    @overload
    def argb8888(arg0: float, arg1: float, arg2: float, arg3: float) -> int:
        """public static int com.badlogic.gdx.graphics.Color.argb8888(float,float,float,float)"""
        return int._wrap(_Color.argb8888(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.Color(int)"""
        val = _Color(_int.valueOf(arg0))
        self.__wrapper = val

    @staticmethod
    @overload
    def rgb888ToColor(arg0: 'Color', arg1: int):
        """public static void com.badlogic.gdx.graphics.Color.rgb888ToColor(com.badlogic.gdx.graphics.Color,int)"""
        _Color.rgb888ToColor(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def rgb888(arg0: float, arg1: float, arg2: float) -> int:
        """public static int com.badlogic.gdx.graphics.Color.rgb888(float,float,float)"""
        return int._wrap(_Color.rgb888(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @staticmethod
    @overload
    def abgr8888ToColor(arg0: 'Color', arg1: int):
        """public static void com.badlogic.gdx.graphics.Color.abgr8888ToColor(com.badlogic.gdx.graphics.Color,int)"""
        _Color.abgr8888ToColor(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def rgb565ToColor(arg0: 'Color', arg1: int):
        """public static void com.badlogic.gdx.graphics.Color.rgb565ToColor(com.badlogic.gdx.graphics.Color,int)"""
        _Color.rgb565ToColor(arg0, _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.Color.equals(java.lang.Object)"""
        return bool._wrap(super(_Color, self).equals(arg0))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.set(float,float,float,float)"""
        return 'Color'._wrap(super(_Color, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @staticmethod
    @overload
    def rgba4444ToColor(arg0: 'Color', arg1: int):
        """public static void com.badlogic.gdx.graphics.Color.rgba4444ToColor(com.badlogic.gdx.graphics.Color,int)"""
        _Color.rgba4444ToColor(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def rgba8888(arg0: 'Color') -> int:
        """public static int com.badlogic.gdx.graphics.Color.rgba8888(com.badlogic.gdx.graphics.Color)"""
        return int._wrap(_Color.rgba8888(arg0))

    @staticmethod
    @overload
    def rgb888(arg0: 'Color') -> int:
        """public static int com.badlogic.gdx.graphics.Color.rgb888(com.badlogic.gdx.graphics.Color)"""
        return int._wrap(_Color.rgb888(arg0))

    @staticmethod
    @overload
    def rgb565(arg0: 'Color') -> int:
        """public static int com.badlogic.gdx.graphics.Color.rgb565(com.badlogic.gdx.graphics.Color)"""
        return int._wrap(_Color.rgb565(arg0))

    @staticmethod
    @overload
    def luminanceAlpha(arg0: float, arg1: float) -> int:
        """public static int com.badlogic.gdx.graphics.Color.luminanceAlpha(float,float)"""
        return int._wrap(_Color.luminanceAlpha(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def alpha(arg0: float) -> int:
        """public static int com.badlogic.gdx.graphics.Color.alpha(float)"""
        return int._wrap(_Color.alpha(_float.valueOf(arg0)))

    @overload
    def add(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.add(float,float,float,float)"""
        return 'Color'._wrap(super(_Color, self).add(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def fromHsv(self, arg0: 'float') -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.fromHsv(float[])"""
        return 'Color'._wrap(super(_Color, self).fromHsv(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def rgba4444(arg0: 'Color') -> int:
        """public static int com.badlogic.gdx.graphics.Color.rgba4444(com.badlogic.gdx.graphics.Color)"""
        return int._wrap(_Color.rgba4444(arg0))

    @overload
    def cpy(self) -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.cpy()"""
        return 'Color'._wrap(super(Color, self).cpy())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.Color.hashCode()"""
        return int._wrap(super(Color, self).hashCode())

    @overload
    def premultiplyAlpha(self) -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.premultiplyAlpha()"""
        return 'Color'._wrap(super(Color, self).premultiplyAlpha())

    @staticmethod
    @overload
    def toIntBits(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static int com.badlogic.gdx.graphics.Color.toIntBits(int,int,int,int)"""
        return int._wrap(_Color.toIntBits(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def toFloatBits(self) -> float:
        """public float com.badlogic.gdx.graphics.Color.toFloatBits()"""
        return float._wrap(super(Color, self).toFloatBits())

    @staticmethod
    @overload
    def argb8888(arg0: 'Color') -> int:
        """public static int com.badlogic.gdx.graphics.Color.argb8888(com.badlogic.gdx.graphics.Color)"""
        return int._wrap(_Color.argb8888(arg0))

    @overload
    def sub(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.sub(float,float,float,float)"""
        return 'Color'._wrap(super(_Color, self).sub(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.Color.toString()"""
        return str._wrap(super(Color, self).toString())

    @overload
    def toHsv(self, arg0: 'float') -> List[float]:
        """public float[] com.badlogic.gdx.graphics.Color.toHsv(float[])"""
        return List[float]._wrap(super(_Color, self).toHsv(arg0))

    @overload
    def fromHsv(self, arg0: float, arg1: float, arg2: float) -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.fromHsv(float,float,float)"""
        return 'Color'._wrap(super(_Color, self).fromHsv(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @staticmethod
    @overload
    def toFloatBits(arg0: int, arg1: int, arg2: int, arg3: int) -> float:
        """public static float com.badlogic.gdx.graphics.Color.toFloatBits(int,int,int,int)"""
        return float._wrap(_Color.toFloatBits(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def argb8888ToColor(arg0: 'Color', arg1: int):
        """public static void com.badlogic.gdx.graphics.Color.argb8888ToColor(com.badlogic.gdx.graphics.Color,int)"""
        _Color.argb8888ToColor(arg0, _int.valueOf(arg1))

    @overload
    def set(self, arg0: int) -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.set(int)"""
        return 'Color'._wrap(super(_Color, self).set(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'Color'):
        """public com.badlogic.gdx.graphics.Color(com.badlogic.gdx.graphics.Color)"""
        val = _Color(arg0)
        self.__wrapper = val

    @overload
    def clamp(self) -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.clamp()"""
        return 'Color'._wrap(super(Color, self).clamp())

    @staticmethod
    @overload
    def valueOf(arg0: str, arg1: 'Color') -> 'Color':
        """public static com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.valueOf(java.lang.String,com.badlogic.gdx.graphics.Color)"""
        return Color._wrap(_Color.valueOf(arg0, arg1))

    @overload
    def lerp(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float) -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.lerp(float,float,float,float,float)"""
        return 'Color'._wrap(super(_Color, self).lerp(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.Color()"""
        val = _Color()
        self.__wrapper = val

    @staticmethod
    @overload
    def rgba8888(arg0: float, arg1: float, arg2: float, arg3: float) -> int:
        """public static int com.badlogic.gdx.graphics.Color.rgba8888(float,float,float,float)"""
        return int._wrap(_Color.rgba8888(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def mul(self, arg0: 'Color') -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.mul(com.badlogic.gdx.graphics.Color)"""
        return 'Color'._wrap(super(_Color, self).mul(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def sub(self, arg0: 'Color') -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.sub(com.badlogic.gdx.graphics.Color)"""
        return 'Color'._wrap(super(_Color, self).sub(arg0))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public com.badlogic.gdx.graphics.Color(float,float,float,float)"""
        val = _Color(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def lerp(self, arg0: 'Color', arg1: float) -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.lerp(com.badlogic.gdx.graphics.Color,float)"""
        return 'Color'._wrap(super(_Color, self).lerp(arg0, _float.valueOf(arg1)))

    @staticmethod
    @overload
    def abgr8888ToColor(arg0: 'Color', arg1: float):
        """public static void com.badlogic.gdx.graphics.Color.abgr8888ToColor(com.badlogic.gdx.graphics.Color,float)"""
        _Color.abgr8888ToColor(arg0, _float.valueOf(arg1)) 
 
 
# CLASS: com.badlogic.gdx.graphics.GL32$DebugProc
import com.badlogic.gdx.graphics.GL32 as _GL32_DebugProc
_DebugProc = _GL32_DebugProc.DebugProc
from abc import abstractmethod, ABC
 
class DebugProc():
    """com.badlogic.gdx.graphics.GL32.DebugProc"""
 
    @staticmethod
    def _wrap(java_value: _DebugProc) -> 'DebugProc':
        return DebugProc(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DebugProc):
        """
        Dynamic initializer for DebugProc.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DebugProc__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DebugProc__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onMessage(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: str):
        """public abstract void com.badlogic.gdx.graphics.GL32$DebugProc.onMessage(int,int,int,int,java.lang.String)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.Pixmap$Format
import com.badlogic.gdx.graphics.Pixmap as _Pixmap_Format
_Format = _Pixmap_Format.Format
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
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Format():
    """com.badlogic.gdx.graphics.Pixmap.Format"""
 
    @staticmethod
    def _wrap(java_value: _Format) -> 'Format':
        return Format(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Format):
        """
        Dynamic initializer for Format.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Format__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Format__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Format':
        """public static com.badlogic.gdx.graphics.Pixmap$Format com.badlogic.gdx.graphics.Pixmap$Format.valueOf(java.lang.String)"""
        return Format._wrap(_Format.valueOf(arg0))

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

    @staticmethod
    @overload
    def toGdx2DPixmapFormat(arg0: 'Format') -> int:
        """public static int com.badlogic.gdx.graphics.Pixmap$Format.toGdx2DPixmapFormat(com.badlogic.gdx.graphics.Pixmap$Format)"""
        return int._wrap(_Format.toGdx2DPixmapFormat(arg0))

    @staticmethod
    @overload
    def values() -> List['Format']:
        """public static com.badlogic.gdx.graphics.Pixmap$Format[] com.badlogic.gdx.graphics.Pixmap$Format.values()"""
        return List[Format]._wrap(_Format.values())

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

    @staticmethod
    @overload
    def toGlFormat(arg0: 'Format') -> int:
        """public static int com.badlogic.gdx.graphics.Pixmap$Format.toGlFormat(com.badlogic.gdx.graphics.Pixmap$Format)"""
        return int._wrap(_Format.toGlFormat(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def fromGdx2DPixmapFormat(arg0: int) -> 'Format':
        """public static com.badlogic.gdx.graphics.Pixmap$Format com.badlogic.gdx.graphics.Pixmap$Format.fromGdx2DPixmapFormat(int)"""
        return Format._wrap(_Format.fromGdx2DPixmapFormat(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def toGlType(arg0: 'Format') -> int:
        """public static int com.badlogic.gdx.graphics.Pixmap$Format.toGlType(com.badlogic.gdx.graphics.Pixmap$Format)"""
        return int._wrap(_Format.toGlType(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.PixmapIO
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.PixmapIO as _PixmapIO
_PixmapIO = _PixmapIO
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

import com.badlogic.gdx.graphics.Pixmap as _Pixmap
_Pixmap = _Pixmap
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PixmapIO():
    """com.badlogic.gdx.graphics.PixmapIO"""
 
    @staticmethod
    def _wrap(java_value: _PixmapIO) -> 'PixmapIO':
        return PixmapIO(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PixmapIO):
        """
        Dynamic initializer for PixmapIO.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PixmapIO__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PixmapIO__wrapper":
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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.PixmapIO()"""
        val = _PixmapIO()
        self.__wrapper = val

    @staticmethod
    @overload
    def writeCIM(arg0: 'FileHandle', arg1: 'Pixmap'):
        """public static void com.badlogic.gdx.graphics.PixmapIO.writeCIM(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.Pixmap)"""
        _PixmapIO.writeCIM(arg0, arg1)

    @staticmethod
    @overload
    def writePNG(arg0: 'FileHandle', arg1: 'Pixmap', arg2: int, arg3: bool):
        """public static void com.badlogic.gdx.graphics.PixmapIO.writePNG(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.Pixmap,int,boolean)"""
        _PixmapIO.writePNG(arg0, arg1, _int.valueOf(arg2), _boolean.valueOf(arg3))

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
    def __init__(self):
        """public com.badlogic.gdx.graphics.PixmapIO()"""
        val = _PixmapIO()
        self.__wrapper = val

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

    @staticmethod
    @overload
    def readCIM(arg0: 'FileHandle') -> 'Pixmap':
        """public static com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.graphics.PixmapIO.readCIM(com.badlogic.gdx.files.FileHandle)"""
        return Pixmap._wrap(_PixmapIO.readCIM(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def writePNG(arg0: 'FileHandle', arg1: 'Pixmap'):
        """public static void com.badlogic.gdx.graphics.PixmapIO.writePNG(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.Pixmap)"""
        _PixmapIO.writePNG(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.Cubemap
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

from pyquantum_helper import override
import com.badlogic.gdx.graphics.Texture as _Texture_TextureFilter
_TextureFilter = _Texture_TextureFilter.TextureFilter
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.Texture as _Texture_TextureWrap
_TextureWrap = _Texture_TextureWrap.TextureWrap
import java.lang.Float as _float
import com.badlogic.gdx.graphics.GLTexture as _GLTexture
_GLTexture = _GLTexture
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.Cubemap as _Cubemap
_Cubemap = _Cubemap
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import com.badlogic.gdx.graphics.CubemapData as _CubemapData
_CubemapData = _CubemapData
import java.lang.Class as _Class
_Class = _Class
 
class Cubemap():
    """com.badlogic.gdx.graphics.Cubemap"""
 
    @staticmethod
    def _wrap(java_value: _Cubemap) -> 'Cubemap':
        return Cubemap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Cubemap):
        """
        Dynamic initializer for Cubemap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Cubemap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Cubemap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getManagedStatus() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.Cubemap.getManagedStatus()"""
        return str._wrap(_Cubemap.getManagedStatus())

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.Cubemap.getHeight()"""
        return int._wrap(super(Cubemap, self).getHeight())

    @overload
    def unsafeSetAnisotropicFilter(self, arg0: float) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.unsafeSetAnisotropicFilter(float)"""
        return float._wrap(super(_GLTexture, self).unsafeSetAnisotropicFilter(_float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle', arg2: 'FileHandle', arg3: 'FileHandle', arg4: 'FileHandle', arg5: 'FileHandle', arg6: bool):
        """public com.badlogic.gdx.graphics.Cubemap(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,boolean)"""
        val = _Cubemap(arg0, arg1, arg2, arg3, arg4, arg5, _boolean.valueOf(arg6))
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.Cubemap.getWidth()"""
        return int._wrap(super(Cubemap, self).getWidth())

    @overload
    def __init__(self, arg0: 'TextureData', arg1: 'TextureData', arg2: 'TextureData', arg3: 'TextureData', arg4: 'TextureData', arg5: 'TextureData'):
        """public com.badlogic.gdx.graphics.Cubemap(com.badlogic.gdx.graphics.TextureData,com.badlogic.gdx.graphics.TextureData,com.badlogic.gdx.graphics.TextureData,com.badlogic.gdx.graphics.TextureData,com.badlogic.gdx.graphics.TextureData,com.badlogic.gdx.graphics.TextureData)"""
        val = _Cubemap(arg0, arg1, arg2, arg3, arg4, arg5)
        self.__wrapper = val

    @override
    @overload
    def unsafeSetFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter', arg2: bool):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,boolean)"""
        super(_GLTexture, self).unsafeSetFilter(arg0, arg1, _boolean.valueOf(arg2))

    @override
    @overload
    def getTextureObjectHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.GLTexture.getTextureObjectHandle()"""
        return int._wrap(super(GLTexture, self).getTextureObjectHandle())

    @overload
    def __init__(self, arg0: 'CubemapData'):
        """public com.badlogic.gdx.graphics.Cubemap(com.badlogic.gdx.graphics.CubemapData)"""
        val = _Cubemap(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def invalidateAllCubemaps(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.Cubemap.invalidateAllCubemaps(com.badlogic.gdx.Application)"""
        _Cubemap.invalidateAllCubemaps(arg0)

    @override
    @overload
    def unsafeSetWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap'):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        super(_GLTexture, self).unsafeSetWrap(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def unsafeSetAnisotropicFilter(self, arg0: float, arg1: bool) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.unsafeSetAnisotropicFilter(float,boolean)"""
        return float._wrap(super(_GLTexture, self).unsafeSetAnisotropicFilter(_float.valueOf(arg0), _boolean.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap'):
        """public void com.badlogic.gdx.graphics.GLTexture.setWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        super(_GLTexture, self).setWrap(arg0, arg1)

    @overload
    def __init__(self, arg0: 'Pixmap', arg1: 'Pixmap', arg2: 'Pixmap', arg3: 'Pixmap', arg4: 'Pixmap', arg5: 'Pixmap'):
        """public com.badlogic.gdx.graphics.Cubemap(com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap)"""
        val = _Cubemap(arg0, arg1, arg2, arg3, arg4, arg5)
        self.__wrapper = val

    @override
    @overload
    def getMinFilter(self) -> 'TextureFilter':
        """public com.badlogic.gdx.graphics.Texture$TextureFilter com.badlogic.gdx.graphics.GLTexture.getMinFilter()"""
        return 'TextureFilter'._wrap(super(GLTexture, self).getMinFilter())

    @override
    @overload
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.Cubemap.isManaged()"""
        return bool._wrap(super(Cubemap, self).isManaged())

    @override
    @overload
    def setFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter'):
        """public void com.badlogic.gdx.graphics.GLTexture.setFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter)"""
        super(_GLTexture, self).setFilter(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def load(self, arg0: 'CubemapData'):
        """public void com.badlogic.gdx.graphics.Cubemap.load(com.badlogic.gdx.graphics.CubemapData)"""
        super(_Cubemap, self).load(arg0)

    @staticmethod
    @overload
    def clearAllCubemaps(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.Cubemap.clearAllCubemaps(com.badlogic.gdx.Application)"""
        _Cubemap.clearAllCubemaps(arg0)

    @override
    @overload
    def getDepth(self) -> int:
        """public int com.badlogic.gdx.graphics.Cubemap.getDepth()"""
        return int._wrap(super(Cubemap, self).getDepth())

    @override
    @overload
    def bind(self, arg0: int):
        """public void com.badlogic.gdx.graphics.GLTexture.bind(int)"""
        super(_GLTexture, self).bind(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getMagFilter(self) -> 'TextureFilter':
        """public com.badlogic.gdx.graphics.Texture$TextureFilter com.badlogic.gdx.graphics.GLTexture.getMagFilter()"""
        return 'TextureFilter'._wrap(super(GLTexture, self).getMagFilter())

    @override
    @overload
    def getUWrap(self) -> 'TextureWrap':
        """public com.badlogic.gdx.graphics.Texture$TextureWrap com.badlogic.gdx.graphics.GLTexture.getUWrap()"""
        return 'TextureWrap'._wrap(super(GLTexture, self).getUWrap())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.Cubemap.dispose()"""
        super(Cubemap, self).dispose()

    @overload
    def __init__(self, arg0: 'Pixmap', arg1: 'Pixmap', arg2: 'Pixmap', arg3: 'Pixmap', arg4: 'Pixmap', arg5: 'Pixmap', arg6: bool):
        """public com.badlogic.gdx.graphics.Cubemap(com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,boolean)"""
        val = _Cubemap(arg0, arg1, arg2, arg3, arg4, arg5, _boolean.valueOf(arg6))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle', arg2: 'FileHandle', arg3: 'FileHandle', arg4: 'FileHandle', arg5: 'FileHandle'):
        """public com.badlogic.gdx.graphics.Cubemap(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        val = _Cubemap(arg0, arg1, arg2, arg3, arg4, arg5)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def bind(self):
        """public void com.badlogic.gdx.graphics.GLTexture.bind()"""
        super(GLTexture, self).bind()

    @override
    @overload
    def getVWrap(self) -> 'TextureWrap':
        """public com.badlogic.gdx.graphics.Texture$TextureWrap com.badlogic.gdx.graphics.GLTexture.getVWrap()"""
        return 'TextureWrap'._wrap(super(GLTexture, self).getVWrap())

    @override
    @overload
    def unsafeSetFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter'):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter)"""
        super(_GLTexture, self).unsafeSetFilter(arg0, arg1)

    @staticmethod
    @overload
    def getMaxAnisotropicFilterLevel() -> float:
        """public static float com.badlogic.gdx.graphics.GLTexture.getMaxAnisotropicFilterLevel()"""
        return float._wrap(_GLTexture.getMaxAnisotropicFilterLevel())

    @override
    @overload
    def getAnisotropicFilter(self) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.getAnisotropicFilter()"""
        return float._wrap(super(GLTexture, self).getAnisotropicFilter())

    @staticmethod
    @overload
    def getNumManagedCubemaps() -> int:
        """public static int com.badlogic.gdx.graphics.Cubemap.getNumManagedCubemaps()"""
        return int._wrap(_Cubemap.getNumManagedCubemaps())

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

    @staticmethod
    @overload
    def uploadImageData(arg0: int, arg1: 'TextureData', arg2: int):
        """public static void com.badlogic.gdx.graphics.GLTexture.uploadImageData(int,com.badlogic.gdx.graphics.TextureData,int)"""
        _GLTexture.uploadImageData(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def unsafeSetWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap', arg2: bool):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap,boolean)"""
        super(_GLTexture, self).unsafeSetWrap(arg0, arg1, _boolean.valueOf(arg2))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: 'Format'):
        """public com.badlogic.gdx.graphics.Cubemap(int,int,int,com.badlogic.gdx.graphics.Pixmap$Format)"""
        val = _Cubemap(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)
        self.__wrapper = val

    @staticmethod
    @overload
    def setAssetManager(arg0: 'AssetManager'):
        """public static void com.badlogic.gdx.graphics.Cubemap.setAssetManager(com.badlogic.gdx.assets.AssetManager)"""
        _Cubemap.setAssetManager(arg0)

    @overload
    def getCubemapData(self) -> 'CubemapData':
        """public com.badlogic.gdx.graphics.CubemapData com.badlogic.gdx.graphics.Cubemap.getCubemapData()"""
        return 'CubemapData'._wrap(super(Cubemap, self).getCubemapData())

    @overload
    def setAnisotropicFilter(self, arg0: float) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.setAnisotropicFilter(float)"""
        return float._wrap(super(_GLTexture, self).setAnisotropicFilter(_float.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.CubemapData
from abc import abstractmethod, ABC
import com.badlogic.gdx.graphics.CubemapData as _CubemapData
_CubemapData = _CubemapData
 
class CubemapData():
    """com.badlogic.gdx.graphics.CubemapData"""
 
    @staticmethod
    def _wrap(java_value: _CubemapData) -> 'CubemapData':
        return CubemapData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CubemapData):
        """
        Dynamic initializer for CubemapData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CubemapData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CubemapData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def isManaged(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.CubemapData.isManaged()"""
        pass

    @abstractmethod
    def isPrepared(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.CubemapData.isPrepared()"""
        pass

    @abstractmethod
    def getHeight(self, ):
        """public abstract int com.badlogic.gdx.graphics.CubemapData.getHeight()"""
        pass

    @abstractmethod
    def getWidth(self, ):
        """public abstract int com.badlogic.gdx.graphics.CubemapData.getWidth()"""
        pass

    @abstractmethod
    def prepare(self, ):
        """public abstract void com.badlogic.gdx.graphics.CubemapData.prepare()"""
        pass

    @abstractmethod
    def consumeCubemapData(self, ):
        """public abstract void com.badlogic.gdx.graphics.CubemapData.consumeCubemapData()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.Pixmap$Filter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.Pixmap as _Pixmap_Filter
_Filter = _Pixmap_Filter.Filter
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
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Filter():
    """com.badlogic.gdx.graphics.Pixmap.Filter"""
 
    @staticmethod
    def _wrap(java_value: _Filter) -> 'Filter':
        return Filter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Filter):
        """
        Dynamic initializer for Filter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Filter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Filter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Filter':
        """public static com.badlogic.gdx.graphics.Pixmap$Filter com.badlogic.gdx.graphics.Pixmap$Filter.valueOf(java.lang.String)"""
        return Filter._wrap(_Filter.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['Filter']:
        """public static com.badlogic.gdx.graphics.Pixmap$Filter[] com.badlogic.gdx.graphics.Pixmap$Filter.values()"""
        return List[Filter]._wrap(_Filter.values())

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
 
 
# CLASS: com.badlogic.gdx.graphics.Cubemap$CubemapSide
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
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
import com.badlogic.gdx.graphics.Cubemap as _Cubemap_CubemapSide
_CubemapSide = _Cubemap_CubemapSide.CubemapSide
import java.util.Optional as Optional
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CubemapSide():
    """com.badlogic.gdx.graphics.Cubemap.CubemapSide"""
 
    @staticmethod
    def _wrap(java_value: _CubemapSide) -> 'CubemapSide':
        return CubemapSide(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CubemapSide):
        """
        Dynamic initializer for CubemapSide.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CubemapSide__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CubemapSide__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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

    @staticmethod
    @overload
    def values() -> List['CubemapSide']:
        """public static com.badlogic.gdx.graphics.Cubemap$CubemapSide[] com.badlogic.gdx.graphics.Cubemap$CubemapSide.values()"""
        return List[CubemapSide]._wrap(_CubemapSide.values())

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

    @overload
    def getDirection(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Cubemap$CubemapSide.getDirection(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_CubemapSide, self).getDirection(arg0))

    @overload
    def getUp(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Cubemap$CubemapSide.getUp(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_CubemapSide, self).getUp(arg0))

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
    def getGLEnum(self) -> int:
        """public int com.badlogic.gdx.graphics.Cubemap$CubemapSide.getGLEnum()"""
        return int._wrap(super(CubemapSide, self).getGLEnum())

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'CubemapSide':
        """public static com.badlogic.gdx.graphics.Cubemap$CubemapSide com.badlogic.gdx.graphics.Cubemap$CubemapSide.valueOf(java.lang.String)"""
        return CubemapSide._wrap(_CubemapSide.valueOf(arg0))

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
 
 
# CLASS: com.badlogic.gdx.graphics.GLTexture
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.graphics.Texture as _Texture_TextureFilter
_TextureFilter = _Texture_TextureFilter.TextureFilter
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.Texture as _Texture_TextureWrap
_TextureWrap = _Texture_TextureWrap.TextureWrap
import java.lang.Float as _float
import com.badlogic.gdx.graphics.GLTexture as _GLTexture
_GLTexture = _GLTexture
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLTexture():
    """com.badlogic.gdx.graphics.GLTexture"""
 
    @staticmethod
    def _wrap(java_value: _GLTexture) -> 'GLTexture':
        return GLTexture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLTexture):
        """
        Dynamic initializer for GLTexture.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLTexture__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLTexture__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def unsafeSetWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap'):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        super(_GLTexture, self).unsafeSetWrap(arg0, arg1)

    @overload
    def unsafeSetAnisotropicFilter(self, arg0: float) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.unsafeSetAnisotropicFilter(float)"""
        return float._wrap(super(_GLTexture, self).unsafeSetAnisotropicFilter(_float.valueOf(arg0)))

    @overload
    def setFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter'):
        """public void com.badlogic.gdx.graphics.GLTexture.setFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter)"""
        super(_GLTexture, self).setFilter(arg0, arg1)

    @overload
    def unsafeSetFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter', arg2: bool):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,boolean)"""
        super(_GLTexture, self).unsafeSetFilter(arg0, arg1, _boolean.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getMinFilter(self) -> 'TextureFilter':
        """public com.badlogic.gdx.graphics.Texture$TextureFilter com.badlogic.gdx.graphics.GLTexture.getMinFilter()"""
        return 'TextureFilter'._wrap(super(GLTexture, self).getMinFilter())

    @overload
    def getVWrap(self) -> 'TextureWrap':
        """public com.badlogic.gdx.graphics.Texture$TextureWrap com.badlogic.gdx.graphics.GLTexture.getVWrap()"""
        return 'TextureWrap'._wrap(super(GLTexture, self).getVWrap())

    @overload
    def getTextureObjectHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.GLTexture.getTextureObjectHandle()"""
        return int._wrap(super(GLTexture, self).getTextureObjectHandle())

    @overload
    def setWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap'):
        """public void com.badlogic.gdx.graphics.GLTexture.setWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        super(_GLTexture, self).setWrap(arg0, arg1)

    @overload
    def getUWrap(self) -> 'TextureWrap':
        """public com.badlogic.gdx.graphics.Texture$TextureWrap com.badlogic.gdx.graphics.GLTexture.getUWrap()"""
        return 'TextureWrap'._wrap(super(GLTexture, self).getUWrap())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def unsafeSetAnisotropicFilter(self, arg0: float, arg1: bool) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.unsafeSetAnisotropicFilter(float,boolean)"""
        return float._wrap(super(_GLTexture, self).unsafeSetAnisotropicFilter(_float.valueOf(arg0), _boolean.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def bind(self):
        """public void com.badlogic.gdx.graphics.GLTexture.bind()"""
        super(GLTexture, self).bind()

    @overload
    def getMagFilter(self) -> 'TextureFilter':
        """public com.badlogic.gdx.graphics.Texture$TextureFilter com.badlogic.gdx.graphics.GLTexture.getMagFilter()"""
        return 'TextureFilter'._wrap(super(GLTexture, self).getMagFilter())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def bind(self, arg0: int):
        """public void com.badlogic.gdx.graphics.GLTexture.bind(int)"""
        super(_GLTexture, self).bind(_int.valueOf(arg0))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.GLTexture.dispose()"""
        super(GLTexture, self).dispose()

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.GLTexture(int)"""
        val = _GLTexture(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @abstractmethod
    def getDepth(self, ):
        """public abstract int com.badlogic.gdx.graphics.GLTexture.getDepth()"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @abstractmethod
    def getWidth(self, ):
        """public abstract int com.badlogic.gdx.graphics.GLTexture.getWidth()"""
        pass

    @overload
    def unsafeSetWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap', arg2: bool):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap,boolean)"""
        super(_GLTexture, self).unsafeSetWrap(arg0, arg1, _boolean.valueOf(arg2))

    @overload
    def getAnisotropicFilter(self) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.getAnisotropicFilter()"""
        return float._wrap(super(GLTexture, self).getAnisotropicFilter())

    @staticmethod
    @overload
    def getMaxAnisotropicFilterLevel() -> float:
        """public static float com.badlogic.gdx.graphics.GLTexture.getMaxAnisotropicFilterLevel()"""
        return float._wrap(_GLTexture.getMaxAnisotropicFilterLevel())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.graphics.GLTexture(int,int)"""
        val = _GLTexture(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @abstractmethod
    def isManaged(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.GLTexture.isManaged()"""
        pass

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def getHeight(self, ):
        """public abstract int com.badlogic.gdx.graphics.GLTexture.getHeight()"""
        pass

    @staticmethod
    @overload
    def uploadImageData(arg0: int, arg1: 'TextureData', arg2: int):
        """public static void com.badlogic.gdx.graphics.GLTexture.uploadImageData(int,com.badlogic.gdx.graphics.TextureData,int)"""
        _GLTexture.uploadImageData(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @overload
    def unsafeSetFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter'):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter)"""
        super(_GLTexture, self).unsafeSetFilter(arg0, arg1)

    @overload
    def setAnisotropicFilter(self, arg0: float) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.setAnisotropicFilter(float)"""
        return float._wrap(super(_GLTexture, self).setAnisotropicFilter(_float.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.TextureData$Factory
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.TextureData as _TextureData
_TextureData = _TextureData
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.TextureData as _TextureData_Factory
_Factory = _TextureData_Factory.Factory
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Factory():
    """com.badlogic.gdx.graphics.TextureData.Factory"""
 
    @staticmethod
    def _wrap(java_value: _Factory) -> 'Factory':
        return Factory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Factory):
        """
        Dynamic initializer for Factory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Factory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Factory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.TextureData$Factory()"""
        val = _Factory()
        self.__wrapper = val

    @staticmethod
    @overload
    def loadFromFile(arg0: 'FileHandle', arg1: 'Format', arg2: bool) -> 'TextureData':
        """public static com.badlogic.gdx.graphics.TextureData com.badlogic.gdx.graphics.TextureData$Factory.loadFromFile(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.Pixmap$Format,boolean)"""
        return TextureData._wrap(_Factory.loadFromFile(arg0, arg1, _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def loadFromFile(arg0: 'FileHandle', arg1: bool) -> 'TextureData':
        """public static com.badlogic.gdx.graphics.TextureData com.badlogic.gdx.graphics.TextureData$Factory.loadFromFile(com.badlogic.gdx.files.FileHandle,boolean)"""
        return TextureData._wrap(_Factory.loadFromFile(arg0, _boolean.valueOf(arg1)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.TextureData$Factory()"""
        val = _Factory()
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
 
 
# CLASS: com.badlogic.gdx.graphics.PixmapIO$PNG
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.graphics.PixmapIO as _PixmapIO_PNG
_PNG = _PixmapIO_PNG.PNG
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.io.OutputStream as OutputStream
import java.lang.Integer as _int
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PNG():
    """com.badlogic.gdx.graphics.PixmapIO.PNG"""
 
    @staticmethod
    def _wrap(java_value: _PNG) -> 'PNG':
        return PNG(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PNG):
        """
        Dynamic initializer for PNG.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PNG__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PNG__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.PixmapIO$PNG()"""
        val = _PNG()
        self.__wrapper = val

    @overload
    def setFlipY(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.PixmapIO$PNG.setFlipY(boolean)"""
        super(_PNG, self).setFlipY(_boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.PixmapIO$PNG(int)"""
        val = _PNG(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def write(self, arg0: 'OutputStream', arg1: 'Pixmap'):
        """public void com.badlogic.gdx.graphics.PixmapIO$PNG.write(java.io.OutputStream,com.badlogic.gdx.graphics.Pixmap) throws java.io.IOException"""
        super(_PNG, self).write(arg0, arg1)

    @overload
    def write(self, arg0: 'FileHandle', arg1: 'Pixmap'):
        """public void com.badlogic.gdx.graphics.PixmapIO$PNG.write(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.Pixmap) throws java.io.IOException"""
        super(_PNG, self).write(arg0, arg1)

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
    def dispose(self):
        """public void com.badlogic.gdx.graphics.PixmapIO$PNG.dispose()"""
        super(PNG, self).dispose()

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
    def setCompression(self, arg0: int):
        """public void com.badlogic.gdx.graphics.PixmapIO$PNG.setCompression(int)"""
        super(_PNG, self).setCompression(_int.valueOf(arg0))

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.PixmapIO$PNG()"""
        val = _PNG()
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
 
 
# CLASS: com.badlogic.gdx.graphics.Texture
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

from pyquantum_helper import override
import com.badlogic.gdx.graphics.Texture as _Texture_TextureFilter
_TextureFilter = _Texture_TextureFilter.TextureFilter
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.Texture as _Texture
_Texture = _Texture
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.TextureData as _TextureData
_TextureData = _TextureData
from builtins import float
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.Texture as _Texture_TextureWrap
_TextureWrap = _Texture_TextureWrap.TextureWrap
import java.lang.Float as _float
import java.lang.String as _string
import com.badlogic.gdx.graphics.GLTexture as _GLTexture
_GLTexture = _GLTexture
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Texture():
    """com.badlogic.gdx.graphics.Texture"""
 
    @staticmethod
    def _wrap(java_value: _Texture) -> 'Texture':
        return Texture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Texture):
        """
        Dynamic initializer for Texture.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Texture__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Texture__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'FileHandle'):
        """public com.badlogic.gdx.graphics.Texture(com.badlogic.gdx.files.FileHandle)"""
        val = _Texture(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def clearAllTextures(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.Texture.clearAllTextures(com.badlogic.gdx.Application)"""
        _Texture.clearAllTextures(arg0)

    @overload
    def unsafeSetAnisotropicFilter(self, arg0: float) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.unsafeSetAnisotropicFilter(float)"""
        return float._wrap(super(_GLTexture, self).unsafeSetAnisotropicFilter(_float.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def unsafeSetFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter', arg2: bool):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,boolean)"""
        super(_GLTexture, self).unsafeSetFilter(arg0, arg1, _boolean.valueOf(arg2))

    @overload
    def draw(self, arg0: 'Pixmap', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.Texture.draw(com.badlogic.gdx.graphics.Pixmap,int,int)"""
        super(_Texture, self).draw(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def load(self, arg0: 'TextureData'):
        """public void com.badlogic.gdx.graphics.Texture.load(com.badlogic.gdx.graphics.TextureData)"""
        super(_Texture, self).load(arg0)

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
    def __init__(self, arg0: 'FileHandle', arg1: bool):
        """public com.badlogic.gdx.graphics.Texture(com.badlogic.gdx.files.FileHandle,boolean)"""
        val = _Texture(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getMinFilter(self) -> 'TextureFilter':
        """public com.badlogic.gdx.graphics.Texture$TextureFilter com.badlogic.gdx.graphics.GLTexture.getMinFilter()"""
        return 'TextureFilter'._wrap(super(GLTexture, self).getMinFilter())

    @override
    @overload
    def setFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter'):
        """public void com.badlogic.gdx.graphics.GLTexture.setFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter)"""
        super(_GLTexture, self).setFilter(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.Texture.dispose()"""
        super(Texture, self).dispose()

    @overload
    def __init__(self, arg0: 'TextureData'):
        """public com.badlogic.gdx.graphics.Texture(com.badlogic.gdx.graphics.TextureData)"""
        val = _Texture(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Pixmap', arg1: 'Format', arg2: bool):
        """public com.badlogic.gdx.graphics.Texture(com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap$Format,boolean)"""
        val = _Texture(arg0, arg1, _boolean.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def getUWrap(self) -> 'TextureWrap':
        """public com.badlogic.gdx.graphics.Texture$TextureWrap com.badlogic.gdx.graphics.GLTexture.getUWrap()"""
        return 'TextureWrap'._wrap(super(GLTexture, self).getUWrap())

    @override
    @overload
    def getDepth(self) -> int:
        """public int com.badlogic.gdx.graphics.Texture.getDepth()"""
        return int._wrap(super(Texture, self).getDepth())

    @override
    @overload
    def bind(self):
        """public void com.badlogic.gdx.graphics.GLTexture.bind()"""
        super(GLTexture, self).bind()

    @override
    @overload
    def getAnisotropicFilter(self) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.getAnisotropicFilter()"""
        return float._wrap(super(GLTexture, self).getAnisotropicFilter())

    @staticmethod
    @overload
    def getManagedStatus() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.Texture.getManagedStatus()"""
        return str._wrap(_Texture.getManagedStatus())

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.graphics.Texture(java.lang.String)"""
        val = _Texture(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def uploadImageData(arg0: int, arg1: 'TextureData', arg2: int):
        """public static void com.badlogic.gdx.graphics.GLTexture.uploadImageData(int,com.badlogic.gdx.graphics.TextureData,int)"""
        _GLTexture.uploadImageData(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @staticmethod
    @overload
    def getNumManagedTextures() -> int:
        """public static int com.badlogic.gdx.graphics.Texture.getNumManagedTextures()"""
        return int._wrap(_Texture.getNumManagedTextures())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'Format', arg2: bool):
        """public com.badlogic.gdx.graphics.Texture(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.Pixmap$Format,boolean)"""
        val = _Texture(arg0, arg1, _boolean.valueOf(arg2))
        self.__wrapper = val

    @overload
    def getTextureData(self) -> 'TextureData':
        """public com.badlogic.gdx.graphics.TextureData com.badlogic.gdx.graphics.Texture.getTextureData()"""
        return 'TextureData'._wrap(super(Texture, self).getTextureData())

    @override
    @overload
    def getTextureObjectHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.GLTexture.getTextureObjectHandle()"""
        return int._wrap(super(GLTexture, self).getTextureObjectHandle())

    @override
    @overload
    def unsafeSetWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap'):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        super(_GLTexture, self).unsafeSetWrap(arg0, arg1)

    @staticmethod
    @overload
    def setAssetManager(arg0: 'AssetManager'):
        """public static void com.badlogic.gdx.graphics.Texture.setAssetManager(com.badlogic.gdx.assets.AssetManager)"""
        _Texture.setAssetManager(arg0)

    @overload
    def unsafeSetAnisotropicFilter(self, arg0: float, arg1: bool) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.unsafeSetAnisotropicFilter(float,boolean)"""
        return float._wrap(super(_GLTexture, self).unsafeSetAnisotropicFilter(_float.valueOf(arg0), _boolean.valueOf(arg1)))

    @override
    @overload
    def setWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap'):
        """public void com.badlogic.gdx.graphics.GLTexture.setWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        super(_GLTexture, self).setWrap(arg0, arg1)

    @overload
    def __init__(self, arg0: 'Pixmap', arg1: bool):
        """public com.badlogic.gdx.graphics.Texture(com.badlogic.gdx.graphics.Pixmap,boolean)"""
        val = _Texture(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

    @staticmethod
    @overload
    def invalidateAllTextures(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.Texture.invalidateAllTextures(com.badlogic.gdx.Application)"""
        _Texture.invalidateAllTextures(arg0)

    @overload
    def __init__(self, arg0: 'Pixmap'):
        """public com.badlogic.gdx.graphics.Texture(com.badlogic.gdx.graphics.Pixmap)"""
        val = _Texture(arg0)
        self.__wrapper = val

    @override
    @overload
    def bind(self, arg0: int):
        """public void com.badlogic.gdx.graphics.GLTexture.bind(int)"""
        super(_GLTexture, self).bind(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getMagFilter(self) -> 'TextureFilter':
        """public com.badlogic.gdx.graphics.Texture$TextureFilter com.badlogic.gdx.graphics.GLTexture.getMagFilter()"""
        return 'TextureFilter'._wrap(super(GLTexture, self).getMagFilter())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'Format'):
        """public com.badlogic.gdx.graphics.Texture(int,int,com.badlogic.gdx.graphics.Pixmap$Format)"""
        val = _Texture(_int.valueOf(arg0), _int.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.Texture.isManaged()"""
        return bool._wrap(super(Texture, self).isManaged())

    @override
    @overload
    def getVWrap(self) -> 'TextureWrap':
        """public com.badlogic.gdx.graphics.Texture$TextureWrap com.badlogic.gdx.graphics.GLTexture.getVWrap()"""
        return 'TextureWrap'._wrap(super(GLTexture, self).getVWrap())

    @override
    @overload
    def unsafeSetFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter'):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter)"""
        super(_GLTexture, self).unsafeSetFilter(arg0, arg1)

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.Texture.getHeight()"""
        return int._wrap(super(Texture, self).getHeight())

    @staticmethod
    @overload
    def getMaxAnisotropicFilterLevel() -> float:
        """public static float com.badlogic.gdx.graphics.GLTexture.getMaxAnisotropicFilterLevel()"""
        return float._wrap(_GLTexture.getMaxAnisotropicFilterLevel())

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.Texture.getWidth()"""
        return int._wrap(super(Texture, self).getWidth())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.Texture.toString()"""
        return str._wrap(super(Texture, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def unsafeSetWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap', arg2: bool):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap,boolean)"""
        super(_GLTexture, self).unsafeSetWrap(arg0, arg1, _boolean.valueOf(arg2))

    @overload
    def setAnisotropicFilter(self, arg0: float) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.setAnisotropicFilter(float)"""
        return float._wrap(super(_GLTexture, self).setAnisotropicFilter(_float.valueOf(arg0))) 
 
 
# CLASS: com.badlogic.gdx.graphics.OrthographicCamera
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.Camera as _Camera
_Camera = _Camera
import com.badlogic.gdx.math.collision.Ray as _Ray
_Ray = _Ray
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.OrthographicCamera as _OrthographicCamera
_OrthographicCamera = _OrthographicCamera
import java.lang.Float as _float
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class OrthographicCamera():
    """com.badlogic.gdx.graphics.OrthographicCamera"""
 
    @staticmethod
    def _wrap(java_value: _OrthographicCamera) -> 'OrthographicCamera':
        return OrthographicCamera(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OrthographicCamera):
        """
        Dynamic initializer for OrthographicCamera.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OrthographicCamera__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OrthographicCamera__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def update(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.OrthographicCamera.update(boolean)"""
        super(_OrthographicCamera, self).update(_boolean.valueOf(arg0))

    @overload
    def rotate(self, arg0: float):
        """public void com.badlogic.gdx.graphics.OrthographicCamera.rotate(float)"""
        super(_OrthographicCamera, self).rotate(_float.valueOf(arg0))

    @overload
    def translate(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.OrthographicCamera.translate(float,float)"""
        super(_OrthographicCamera, self).translate(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def translate(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.Camera.translate(com.badlogic.gdx.math.Vector3)"""
        super(_Camera, self).translate(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.OrthographicCamera()"""
        val = _OrthographicCamera()
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
    def translate(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.graphics.OrthographicCamera.translate(com.badlogic.gdx.math.Vector2)"""
        super(_OrthographicCamera, self).translate(arg0)

    @override
    @overload
    def rotate(self, arg0: 'Quaternion'):
        """public void com.badlogic.gdx.graphics.Camera.rotate(com.badlogic.gdx.math.Quaternion)"""
        super(_Camera, self).rotate(arg0)

    @override
    @overload
    def lookAt(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.Camera.lookAt(com.badlogic.gdx.math.Vector3)"""
        super(_Camera, self).lookAt(arg0)

    @overload
    def unproject(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.unproject(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_Camera, self).unproject(arg0))

    @overload
    def setToOrtho(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.OrthographicCamera.setToOrtho(boolean)"""
        super(_OrthographicCamera, self).setToOrtho(_boolean.valueOf(arg0))

    @overload
    def getPickRay(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.graphics.Camera.getPickRay(float,float,float,float,float,float)"""
        return 'collision.Ray'._wrap(super(_Camera, self).getPickRay(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getPickRay(self, arg0: float, arg1: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.graphics.Camera.getPickRay(float,float)"""
        return 'collision.Ray'._wrap(super(_Camera, self).getPickRay(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def setToOrtho(self, arg0: bool, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.OrthographicCamera.setToOrtho(boolean,float,float)"""
        super(_OrthographicCamera, self).setToOrtho(_boolean.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def transform(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.Camera.transform(com.badlogic.gdx.math.Matrix4)"""
        super(_Camera, self).transform(arg0)

    @override
    @overload
    def rotateAround(self, arg0: 'Vector3', arg1: 'Vector3', arg2: float):
        """public void com.badlogic.gdx.graphics.Camera.rotateAround(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float)"""
        super(_Camera, self).rotateAround(arg0, arg1, _float.valueOf(arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def normalizeUp(self):
        """public void com.badlogic.gdx.graphics.Camera.normalizeUp()"""
        super(Camera, self).normalizeUp()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.OrthographicCamera()"""
        val = _OrthographicCamera()
        self.__wrapper = val

    @override
    @overload
    def translate(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.Camera.translate(float,float,float)"""
        super(_Camera, self).translate(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def project(self, arg0: 'Vector3', arg1: float, arg2: float, arg3: float, arg4: float) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.project(com.badlogic.gdx.math.Vector3,float,float,float,float)"""
        return 'math.Vector3'._wrap(super(_Camera, self).project(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @override
    @overload
    def lookAt(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.Camera.lookAt(float,float,float)"""
        super(_Camera, self).lookAt(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def rotate(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.Camera.rotate(com.badlogic.gdx.math.Vector3,float)"""
        super(_Camera, self).rotate(arg0, _float.valueOf(arg1))

    @overload
    def project(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.project(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_Camera, self).project(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def rotate(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.Camera.rotate(com.badlogic.gdx.math.Matrix4)"""
        super(_Camera, self).rotate(arg0)

    @override
    @overload
    def rotate(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.Camera.rotate(float,float,float,float)"""
        super(_Camera, self).rotate(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def unproject(self, arg0: 'Vector3', arg1: float, arg2: float, arg3: float, arg4: float) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.unproject(com.badlogic.gdx.math.Vector3,float,float,float,float)"""
        return 'math.Vector3'._wrap(super(_Camera, self).unproject(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.OrthographicCamera.update()"""
        super(OrthographicCamera, self).update()

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

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.graphics.OrthographicCamera(float,float)"""
        val = _OrthographicCamera(_float.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.Cursor
import com.badlogic.gdx.graphics.Cursor as _Cursor
_Cursor = _Cursor
from abc import abstractmethod, ABC
import com.badlogic.gdx.utils.Disposable as _Disposable
_Disposable = _Disposable
 
class Cursor():
    """com.badlogic.gdx.graphics.Cursor"""
 
    @staticmethod
    def _wrap(java_value: _Cursor) -> 'Cursor':
        return Cursor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Cursor):
        """
        Dynamic initializer for Cursor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Cursor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Cursor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.utils.Disposable.dispose()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.VertexAttributes
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import com.badlogic.gdx.graphics.VertexAttributes as _VertexAttributes
_VertexAttributes = _VertexAttributes
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.VertexAttribute as _VertexAttribute
_VertexAttribute = _VertexAttribute
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class VertexAttributes():
    """com.badlogic.gdx.graphics.VertexAttributes"""
 
    @staticmethod
    def _wrap(java_value: _VertexAttributes) -> 'VertexAttributes':
        return VertexAttributes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _VertexAttributes):
        """
        Dynamic initializer for VertexAttributes.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_VertexAttributes__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_VertexAttributes__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getOffset(self, arg0: int, arg1: int) -> int:
        """public int com.badlogic.gdx.graphics.VertexAttributes.getOffset(int,int)"""
        return int._wrap(super(_VertexAttributes, self).getOffset(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.VertexAttributes.hashCode()"""
        return int._wrap(super(VertexAttributes, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, *arg0: 'VertexAttribute'):
        """public com.badlogic.gdx.graphics.VertexAttributes(com.badlogic.gdx.graphics.VertexAttribute...)"""
        val = _VertexAttributes(arg0)
        self.__wrapper = val

    @overload
    def get(self, arg0: int) -> 'VertexAttribute':
        """public com.badlogic.gdx.graphics.VertexAttribute com.badlogic.gdx.graphics.VertexAttributes.get(int)"""
        return 'VertexAttribute'._wrap(super(_VertexAttributes, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def compareTo(self, arg0: 'VertexAttributes') -> int:
        """public int com.badlogic.gdx.graphics.VertexAttributes.compareTo(com.badlogic.gdx.graphics.VertexAttributes)"""
        return int._wrap(super(_VertexAttributes, self).compareTo(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<com.badlogic.gdx.graphics.VertexAttribute> com.badlogic.gdx.graphics.VertexAttributes.iterator()"""
        return 'Iterator'._wrap(super(VertexAttributes, self).iterator())

    @overload
    def getMask(self) -> int:
        """public long com.badlogic.gdx.graphics.VertexAttributes.getMask()"""
        return int._wrap(super(VertexAttributes, self).getMask())

    @overload
    def findByUsage(self, arg0: int) -> 'VertexAttribute':
        """public com.badlogic.gdx.graphics.VertexAttribute com.badlogic.gdx.graphics.VertexAttributes.findByUsage(int)"""
        return 'VertexAttribute'._wrap(super(_VertexAttributes, self).findByUsage(_int.valueOf(arg0)))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

    @overload
    def getMaskWithSizePacked(self) -> int:
        """public long com.badlogic.gdx.graphics.VertexAttributes.getMaskWithSizePacked()"""
        return int._wrap(super(VertexAttributes, self).getMaskWithSizePacked())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getTextureCoordinates(self) -> int:
        """public int com.badlogic.gdx.graphics.VertexAttributes.getTextureCoordinates()"""
        return int._wrap(super(VertexAttributes, self).getTextureCoordinates())

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
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.VertexAttributes.equals(java.lang.Object)"""
        return bool._wrap(super(_VertexAttributes, self).equals(arg0))

    @overload
    def getBoneWeights(self) -> int:
        """public int com.badlogic.gdx.graphics.VertexAttributes.getBoneWeights()"""
        return int._wrap(super(VertexAttributes, self).getBoneWeights())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.graphics.VertexAttributes.size()"""
        return int._wrap(super(VertexAttributes, self).size())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.VertexAttributes.toString()"""
        return str._wrap(super(VertexAttributes, self).toString())

    @overload
    def getOffset(self, arg0: int) -> int:
        """public int com.badlogic.gdx.graphics.VertexAttributes.getOffset(int)"""
        return int._wrap(super(_VertexAttributes, self).getOffset(_int.valueOf(arg0))) 
 
 
# CLASS: com.badlogic.gdx.graphics.Mesh
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.nio.FloatBuffer as _FloatBuffer
_FloatBuffer = _FloatBuffer
import java.nio.ShortBuffer as ShortBuffer
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Boolean as _boolean
import com.badlogic.gdx.graphics.VertexAttribute as _VertexAttribute
_VertexAttribute = _VertexAttribute
import com.badlogic.gdx.graphics.Mesh as _Mesh
_Mesh = _Mesh
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import java.nio.ShortBuffer as _ShortBuffer
_ShortBuffer = _ShortBuffer
import com.badlogic.gdx.math.collision.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
from builtins import bool
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.VertexAttributes as _VertexAttributes
_VertexAttributes = _VertexAttributes
from typing import List
import java.lang.Float as _float
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

import java.lang.Integer as _int
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Mesh():
    """com.badlogic.gdx.graphics.Mesh"""
 
    @staticmethod
    def _wrap(java_value: _Mesh) -> 'Mesh':
        return Mesh(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Mesh):
        """
        Dynamic initializer for Mesh.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Mesh__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Mesh__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def updateVertices(self, arg0: int, arg1: 'float', arg2: int, arg3: int) -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.updateVertices(int,float[],int,int)"""
        return 'Mesh'._wrap(super(_Mesh, self).updateVertices(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def getVerticesBuffer(self) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.Mesh.getVerticesBuffer()"""
        return 'FloatBuffer'._wrap(super(Mesh, self).getVerticesBuffer())

    @overload
    def calculateRadius(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: 'Matrix4') -> float:
        """public float com.badlogic.gdx.graphics.Mesh.calculateRadius(float,float,float,int,int,com.badlogic.gdx.math.Matrix4)"""
        return float._wrap(super(_Mesh, self).calculateRadius(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5))

    @overload
    def __init__(self, arg0: 'VertexDataType', arg1: bool, arg2: int, arg3: int, arg4: 'VertexAttributes'):
        """public com.badlogic.gdx.graphics.Mesh(com.badlogic.gdx.graphics.Mesh$VertexDataType,boolean,int,int,com.badlogic.gdx.graphics.VertexAttributes)"""
        val = _Mesh(arg0, _boolean.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4)
        self.__wrapper = val

    @overload
    def scale(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.Mesh.scale(float,float,float)"""
        super(_Mesh, self).scale(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def getVertexAttribute(self, arg0: int) -> 'VertexAttribute':
        """public com.badlogic.gdx.graphics.VertexAttribute com.badlogic.gdx.graphics.Mesh.getVertexAttribute(int)"""
        return 'VertexAttribute'._wrap(super(_Mesh, self).getVertexAttribute(_int.valueOf(arg0)))

    @overload
    def setIndices(self, arg0: 'short') -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.setIndices(short[])"""
        return 'Mesh'._wrap(super(_Mesh, self).setIndices(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def render(self, arg0: 'ShaderProgram', arg1: int):
        """public void com.badlogic.gdx.graphics.Mesh.render(com.badlogic.gdx.graphics.glutils.ShaderProgram,int)"""
        super(_Mesh, self).render(arg0, _int.valueOf(arg1))

    @overload
    def calculateRadius(self, arg0: 'Vector3') -> float:
        """public float com.badlogic.gdx.graphics.Mesh.calculateRadius(com.badlogic.gdx.math.Vector3)"""
        return float._wrap(super(_Mesh, self).calculateRadius(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setInstanceData(self, arg0: 'FloatBuffer', arg1: int) -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.setInstanceData(java.nio.FloatBuffer,int)"""
        return 'Mesh'._wrap(super(_Mesh, self).setInstanceData(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def isInstanced(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.Mesh.isInstanced()"""
        return bool._wrap(super(Mesh, self).isInstanced())

    @staticmethod
    @overload
    def transformUV(arg0: 'Matrix3', arg1: 'float', arg2: int, arg3: int, arg4: int, arg5: int):
        """public static void com.badlogic.gdx.graphics.Mesh.transformUV(com.badlogic.gdx.math.Matrix3,float[],int,int,int,int)"""
        _Mesh.transformUV(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @overload
    def calculateBoundingBox(self, arg0: 'BoundingBox'):
        """public void com.badlogic.gdx.graphics.Mesh.calculateBoundingBox(com.badlogic.gdx.math.collision.BoundingBox)"""
        super(_Mesh, self).calculateBoundingBox(arg0)

    @overload
    def bind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.Mesh.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(_Mesh, self).bind(arg0)

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.Mesh.dispose()"""
        super(Mesh, self).dispose()

    @overload
    def disableInstancedRendering(self) -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.disableInstancedRendering()"""
        return 'Mesh'._wrap(super(Mesh, self).disableInstancedRendering())

    @overload
    def getNumIndices(self) -> int:
        """public int com.badlogic.gdx.graphics.Mesh.getNumIndices()"""
        return int._wrap(super(Mesh, self).getNumIndices())

    @overload
    def setVertices(self, arg0: 'float', arg1: int, arg2: int) -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.setVertices(float[],int,int)"""
        return 'Mesh'._wrap(super(_Mesh, self).setVertices(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def updateVertices(self, arg0: int, arg1: 'float') -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.updateVertices(int,float[])"""
        return 'Mesh'._wrap(super(_Mesh, self).updateVertices(_int.valueOf(arg0), arg1))

    @overload
    def setAutoBind(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.Mesh.setAutoBind(boolean)"""
        super(_Mesh, self).setAutoBind(_boolean.valueOf(arg0))

    @overload
    def calculateRadius(self, arg0: 'Vector3', arg1: int, arg2: int, arg3: 'Matrix4') -> float:
        """public float com.badlogic.gdx.graphics.Mesh.calculateRadius(com.badlogic.gdx.math.Vector3,int,int,com.badlogic.gdx.math.Matrix4)"""
        return float._wrap(super(_Mesh, self).calculateRadius(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def getVertexSize(self) -> int:
        """public int com.badlogic.gdx.graphics.Mesh.getVertexSize()"""
        return int._wrap(super(Mesh, self).getVertexSize())

    @overload
    def __init__(self, arg0: bool, arg1: int, arg2: int, *arg3: 'VertexAttribute'):
        """public com.badlogic.gdx.graphics.Mesh(boolean,int,int,com.badlogic.gdx.graphics.VertexAttribute...)"""
        val = _Mesh(_boolean.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)
        self.__wrapper = val

    @staticmethod
    @overload
    def clearAllMeshes(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.Mesh.clearAllMeshes(com.badlogic.gdx.Application)"""
        _Mesh.clearAllMeshes(arg0)

    @overload
    def calculateRadius(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int) -> float:
        """public float com.badlogic.gdx.graphics.Mesh.calculateRadius(float,float,float,int,int)"""
        return float._wrap(super(_Mesh, self).calculateRadius(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getIndices(self, arg0: int, arg1: 'short', arg2: int):
        """public void com.badlogic.gdx.graphics.Mesh.getIndices(int,short[],int)"""
        super(_Mesh, self).getIndices(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @overload
    def calculateRadius(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.graphics.Mesh.calculateRadius(float,float,float)"""
        return float._wrap(super(_Mesh, self).calculateRadius(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def updateInstanceData(self, arg0: int, arg1: 'float', arg2: int, arg3: int) -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.updateInstanceData(int,float[],int,int)"""
        return 'Mesh'._wrap(super(_Mesh, self).updateInstanceData(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def getMaxIndices(self) -> int:
        """public int com.badlogic.gdx.graphics.Mesh.getMaxIndices()"""
        return int._wrap(super(Mesh, self).getMaxIndices())

    @overload
    def setVertices(self, arg0: 'float') -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.setVertices(float[])"""
        return 'Mesh'._wrap(super(_Mesh, self).setVertices(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def unbind(self, arg0: 'ShaderProgram', arg1: 'int', arg2: 'int'):
        """public void com.badlogic.gdx.graphics.Mesh.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[],int[])"""
        super(_Mesh, self).unbind(arg0, arg1, arg2)

    @overload
    def getIndicesBuffer(self, arg0: bool) -> 'ShortBuffer':
        """public java.nio.ShortBuffer com.badlogic.gdx.graphics.Mesh.getIndicesBuffer(boolean)"""
        return 'ShortBuffer'._wrap(super(_Mesh, self).getIndicesBuffer(_boolean.valueOf(arg0)))

    @overload
    def getIndices(self, arg0: 'short', arg1: int):
        """public void com.badlogic.gdx.graphics.Mesh.getIndices(short[],int)"""
        super(_Mesh, self).getIndices(arg0, _int.valueOf(arg1))

    @overload
    def copy(self, arg0: bool) -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.copy(boolean)"""
        return 'Mesh'._wrap(super(_Mesh, self).copy(_boolean.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: bool, arg1: int, arg2: int, arg3: 'VertexAttributes'):
        """public com.badlogic.gdx.graphics.Mesh(boolean,int,int,com.badlogic.gdx.graphics.VertexAttributes)"""
        val = _Mesh(_boolean.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)
        self.__wrapper = val

    @overload
    def calculateBoundingBox(self) -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.Mesh.calculateBoundingBox()"""
        return 'collision.BoundingBox'._wrap(super(Mesh, self).calculateBoundingBox())

    @overload
    def getVerticesBuffer(self, arg0: bool) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.Mesh.getVerticesBuffer(boolean)"""
        return 'FloatBuffer'._wrap(super(_Mesh, self).getVerticesBuffer(_boolean.valueOf(arg0)))

    @overload
    def extendBoundingBox(self, arg0: 'BoundingBox', arg1: int, arg2: int) -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.Mesh.extendBoundingBox(com.badlogic.gdx.math.collision.BoundingBox,int,int)"""
        return 'collision.BoundingBox'._wrap(super(_Mesh, self).extendBoundingBox(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def calculateBoundingBox(self, arg0: 'BoundingBox', arg1: int, arg2: int, arg3: 'Matrix4') -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.Mesh.calculateBoundingBox(com.badlogic.gdx.math.collision.BoundingBox,int,int,com.badlogic.gdx.math.Matrix4)"""
        return 'collision.BoundingBox'._wrap(super(_Mesh, self).calculateBoundingBox(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def getVertices(self, arg0: int, arg1: int, arg2: 'float', arg3: int) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.Mesh.getVertices(int,int,float[],int)"""
        return List[float]._wrap(super(_Mesh, self).getVertices(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3)))

    @overload
    def getVertexAttributes(self) -> 'VertexAttributes':
        """public com.badlogic.gdx.graphics.VertexAttributes com.badlogic.gdx.graphics.Mesh.getVertexAttributes()"""
        return 'VertexAttributes'._wrap(super(Mesh, self).getVertexAttributes())

    @overload
    def render(self, arg0: 'ShaderProgram', arg1: int, arg2: int, arg3: int, arg4: bool):
        """public void com.badlogic.gdx.graphics.Mesh.render(com.badlogic.gdx.graphics.glutils.ShaderProgram,int,int,int,boolean)"""
        super(_Mesh, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _boolean.valueOf(arg4))

    @overload
    def updateInstanceData(self, arg0: int, arg1: 'FloatBuffer') -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.updateInstanceData(int,java.nio.FloatBuffer)"""
        return 'Mesh'._wrap(super(_Mesh, self).updateInstanceData(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def transform(arg0: 'Matrix4', arg1: 'float', arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static void com.badlogic.gdx.graphics.Mesh.transform(com.badlogic.gdx.math.Matrix4,float[],int,int,int,int,int)"""
        _Mesh.transform(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6))

    @overload
    def calculateBoundingBox(self, arg0: 'BoundingBox', arg1: int, arg2: int) -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.Mesh.calculateBoundingBox(com.badlogic.gdx.math.collision.BoundingBox,int,int)"""
        return 'collision.BoundingBox'._wrap(super(_Mesh, self).calculateBoundingBox(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def getVertices(self, arg0: 'float') -> List[float]:
        """public float[] com.badlogic.gdx.graphics.Mesh.getVertices(float[])"""
        return List[float]._wrap(super(_Mesh, self).getVertices(arg0))

    @overload
    def __init__(self, arg0: 'VertexDataType', arg1: bool, arg2: int, arg3: int, *arg4: 'VertexAttribute'):
        """public com.badlogic.gdx.graphics.Mesh(com.badlogic.gdx.graphics.Mesh$VertexDataType,boolean,int,int,com.badlogic.gdx.graphics.VertexAttribute...)"""
        val = _Mesh(arg0, _boolean.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4)
        self.__wrapper = val

    @staticmethod
    @overload
    def invalidateAllMeshes(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.Mesh.invalidateAllMeshes(com.badlogic.gdx.Application)"""
        _Mesh.invalidateAllMeshes(arg0)

    @staticmethod
    @overload
    def getManagedStatus() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.Mesh.getManagedStatus()"""
        return str._wrap(_Mesh.getManagedStatus())

    @overload
    def transform(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.Mesh.transform(com.badlogic.gdx.math.Matrix4)"""
        super(_Mesh, self).transform(arg0)

    @overload
    def calculateRadiusSquared(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: 'Matrix4') -> float:
        """public float com.badlogic.gdx.graphics.Mesh.calculateRadiusSquared(float,float,float,int,int,com.badlogic.gdx.math.Matrix4)"""
        return float._wrap(super(_Mesh, self).calculateRadiusSquared(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5))

    @overload
    def calculateRadius(self, arg0: 'Vector3', arg1: int, arg2: int) -> float:
        """public float com.badlogic.gdx.graphics.Mesh.calculateRadius(com.badlogic.gdx.math.Vector3,int,int)"""
        return float._wrap(super(_Mesh, self).calculateRadius(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def transform(self, arg0: 'Matrix4', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.Mesh.transform(com.badlogic.gdx.math.Matrix4,int,int)"""
        super(_Mesh, self).transform(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def getVertices(self, arg0: int, arg1: int, arg2: 'float') -> List[float]:
        """public float[] com.badlogic.gdx.graphics.Mesh.getVertices(int,int,float[])"""
        return List[float]._wrap(super(_Mesh, self).getVertices(_int.valueOf(arg0), _int.valueOf(arg1), arg2))

    @overload
    def getIndicesBuffer(self) -> 'ShortBuffer':
        """public java.nio.ShortBuffer com.badlogic.gdx.graphics.Mesh.getIndicesBuffer()"""
        return 'ShortBuffer'._wrap(super(Mesh, self).getIndicesBuffer())

    @overload
    def getMaxVertices(self) -> int:
        """public int com.badlogic.gdx.graphics.Mesh.getMaxVertices()"""
        return int._wrap(super(Mesh, self).getMaxVertices())

    @overload
    def getIndices(self, arg0: int, arg1: int, arg2: 'short', arg3: int):
        """public void com.badlogic.gdx.graphics.Mesh.getIndices(int,int,short[],int)"""
        super(_Mesh, self).getIndices(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @overload
    def render(self, arg0: 'ShaderProgram', arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.Mesh.render(com.badlogic.gdx.graphics.glutils.ShaderProgram,int,int,int)"""
        super(_Mesh, self).render(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def enableInstancedRendering(self, arg0: bool, arg1: int, *arg2: 'VertexAttribute') -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.enableInstancedRendering(boolean,int,com.badlogic.gdx.graphics.VertexAttribute...)"""
        return 'Mesh'._wrap(super(_Mesh, self).enableInstancedRendering(_boolean.valueOf(arg0), _int.valueOf(arg1), arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def unbind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.Mesh.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(_Mesh, self).unbind(arg0)

    @overload
    def bind(self, arg0: 'ShaderProgram', arg1: 'int', arg2: 'int'):
        """public void com.badlogic.gdx.graphics.Mesh.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[],int[])"""
        super(_Mesh, self).bind(arg0, arg1, arg2)

    @overload
    def setInstanceData(self, arg0: 'FloatBuffer') -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.setInstanceData(java.nio.FloatBuffer)"""
        return 'Mesh'._wrap(super(_Mesh, self).setInstanceData(arg0))

    @overload
    def updateInstanceData(self, arg0: int, arg1: 'FloatBuffer', arg2: int, arg3: int) -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.updateInstanceData(int,java.nio.FloatBuffer,int,int)"""
        return 'Mesh'._wrap(super(_Mesh, self).updateInstanceData(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def setIndices(self, arg0: 'short', arg1: int, arg2: int) -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.setIndices(short[],int,int)"""
        return 'Mesh'._wrap(super(_Mesh, self).setIndices(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def __init__(self, arg0: bool, arg1: bool, arg2: int, arg3: int, arg4: 'VertexAttributes'):
        """public com.badlogic.gdx.graphics.Mesh(boolean,boolean,int,int,com.badlogic.gdx.graphics.VertexAttributes)"""
        val = _Mesh(_boolean.valueOf(arg0), _boolean.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4)
        self.__wrapper = val

    @overload
    def extendBoundingBox(self, arg0: 'BoundingBox', arg1: int, arg2: int, arg3: 'Matrix4') -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.Mesh.extendBoundingBox(com.badlogic.gdx.math.collision.BoundingBox,int,int,com.badlogic.gdx.math.Matrix4)"""
        return 'collision.BoundingBox'._wrap(super(_Mesh, self).extendBoundingBox(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def getIndices(self, arg0: 'short'):
        """public void com.badlogic.gdx.graphics.Mesh.getIndices(short[])"""
        super(_Mesh, self).getIndices(arg0)

    @overload
    def updateInstanceData(self, arg0: int, arg1: 'float') -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.updateInstanceData(int,float[])"""
        return 'Mesh'._wrap(super(_Mesh, self).updateInstanceData(_int.valueOf(arg0), arg1))

    @overload
    def getInstancedAttributes(self) -> 'VertexAttributes':
        """public com.badlogic.gdx.graphics.VertexAttributes com.badlogic.gdx.graphics.Mesh.getInstancedAttributes()"""
        return 'VertexAttributes'._wrap(super(Mesh, self).getInstancedAttributes())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getNumVertices(self) -> int:
        """public int com.badlogic.gdx.graphics.Mesh.getNumVertices()"""
        return int._wrap(super(Mesh, self).getNumVertices())

    @overload
    def transformUV(self, arg0: 'Matrix3'):
        """public void com.badlogic.gdx.graphics.Mesh.transformUV(com.badlogic.gdx.math.Matrix3)"""
        super(_Mesh, self).transformUV(arg0)

    @overload
    def setInstanceData(self, arg0: 'float') -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.setInstanceData(float[])"""
        return 'Mesh'._wrap(super(_Mesh, self).setInstanceData(arg0))

    @overload
    def getVertices(self, arg0: int, arg1: 'float') -> List[float]:
        """public float[] com.badlogic.gdx.graphics.Mesh.getVertices(int,float[])"""
        return List[float]._wrap(super(_Mesh, self).getVertices(_int.valueOf(arg0), arg1))

    @overload
    def setInstanceData(self, arg0: 'float', arg1: int, arg2: int) -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.setInstanceData(float[],int,int)"""
        return 'Mesh'._wrap(super(_Mesh, self).setInstanceData(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def copy(self, arg0: bool, arg1: bool, arg2: 'int') -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.copy(boolean,boolean,int[])"""
        return 'Mesh'._wrap(super(_Mesh, self).copy(_boolean.valueOf(arg0), _boolean.valueOf(arg1), arg2))