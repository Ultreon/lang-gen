from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.nio.ShortBuffer as __ShortBuffer
__ShortBuffer = __ShortBuffer
import java.lang.Object as __object
from builtins import type
import java.nio.ShortBuffer as ShortBuffer
import java.lang.Long as __long
import com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData as __IndexBufferObjectSubData
__IndexBufferObjectSubData = __IndexBufferObjectSubData
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class IndexBufferObjectSubData():
    """com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData"""
 
    @staticmethod
    def __wrap(java_value: __IndexBufferObjectSubData) -> 'IndexBufferObjectSubData':
        return IndexBufferObjectSubData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IndexBufferObjectSubData):
        """
        Dynamic initializer for IndexBufferObjectSubData.
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
    def invalidate(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.invalidate()"""
        super(IndexBufferObjectSubData, self).invalidate()

    @override
    @overload
    def getBuffer(self) -> 'ShortBuffer':
        """public java.nio.ShortBuffer com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.getBuffer()"""
        return 'ShortBuffer'.__wrap(super(IndexBufferObjectSubData, self).getBuffer())

    @override
    @overload
    def setIndices(self, arg0: 'short', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.setIndices(short[],int,int)"""
        super(__IndexBufferObjectSubData, self).setIndices(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getBuffer(self, arg0: bool) -> 'ShortBuffer':
        """public java.nio.ShortBuffer com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.getBuffer(boolean)"""
        return 'ShortBuffer'.__wrap(super(__IndexBufferObjectSubData, self).getBuffer(__boolean.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def bind(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.bind()"""
        super(IndexBufferObjectSubData, self).bind()

    @override
    @overload
    def unbind(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.unbind()"""
        super(IndexBufferObjectSubData, self).unbind()

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
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData(int)"""
        val = __IndexBufferObjectSubData(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setIndices(self, arg0: 'ShortBuffer'):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.setIndices(java.nio.ShortBuffer)"""
        super(__IndexBufferObjectSubData, self).setIndices(arg0)

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.dispose()"""
        super(IndexBufferObjectSubData, self).dispose()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getNumIndices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.getNumIndices()"""
        return int.__wrap(super(IndexBufferObjectSubData, self).getNumIndices())

    @override
    @overload
    def updateIndices(self, arg0: int, arg1: 'short', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.updateIndices(int,short[],int,int)"""
        super(__IndexBufferObjectSubData, self).updateIndices(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: bool, arg1: int):
        """public com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData(boolean,int)"""
        val = __IndexBufferObjectSubData(__boolean.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getNumMaxIndices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.getNumMaxIndices()"""
        return int.__wrap(super(IndexBufferObjectSubData, self).getNumMaxIndices())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.nio.ShortBuffer as __ShortBuffer
__ShortBuffer = __ShortBuffer
import java.lang.Object as __object
from builtins import type
import java.nio.ShortBuffer as ShortBuffer
import java.lang.Long as __long
import com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData as __IndexBufferObjectSubData
__IndexBufferObjectSubData = __IndexBufferObjectSubData
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class IndexBufferObjectSubData():
    """com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData"""
 
    @staticmethod
    def __wrap(java_value: __IndexBufferObjectSubData) -> 'IndexBufferObjectSubData':
        return IndexBufferObjectSubData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IndexBufferObjectSubData):
        """
        Dynamic initializer for IndexBufferObjectSubData.
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
    def invalidate(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.invalidate()"""
        super(IndexBufferObjectSubData, self).invalidate()

    @override
    @overload
    def getBuffer(self) -> 'ShortBuffer':
        """public java.nio.ShortBuffer com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.getBuffer()"""
        return 'ShortBuffer'.__wrap(super(IndexBufferObjectSubData, self).getBuffer())

    @override
    @overload
    def setIndices(self, arg0: 'short', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.setIndices(short[],int,int)"""
        super(__IndexBufferObjectSubData, self).setIndices(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getBuffer(self, arg0: bool) -> 'ShortBuffer':
        """public java.nio.ShortBuffer com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.getBuffer(boolean)"""
        return 'ShortBuffer'.__wrap(super(__IndexBufferObjectSubData, self).getBuffer(__boolean.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def bind(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.bind()"""
        super(IndexBufferObjectSubData, self).bind()

    @override
    @overload
    def unbind(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.unbind()"""
        super(IndexBufferObjectSubData, self).unbind()

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
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData(int)"""
        val = __IndexBufferObjectSubData(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setIndices(self, arg0: 'ShortBuffer'):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.setIndices(java.nio.ShortBuffer)"""
        super(__IndexBufferObjectSubData, self).setIndices(arg0)

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.dispose()"""
        super(IndexBufferObjectSubData, self).dispose()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getNumIndices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.getNumIndices()"""
        return int.__wrap(super(IndexBufferObjectSubData, self).getNumIndices())

    @override
    @overload
    def updateIndices(self, arg0: int, arg1: 'short', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.updateIndices(int,short[],int,int)"""
        super(__IndexBufferObjectSubData, self).updateIndices(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: bool, arg1: int):
        """public com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData(boolean,int)"""
        val = __IndexBufferObjectSubData(__boolean.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getNumMaxIndices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.getNumMaxIndices()"""
        return int.__wrap(super(IndexBufferObjectSubData, self).getNumMaxIndices())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.ShaderProgram
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

import com.badlogic.gdx.graphics.glutils.ShaderProgram as __ShaderProgram
__ShaderProgram = __ShaderProgram
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.nio.FloatBuffer as FloatBuffer
from typing import List
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.nio.Buffer as Buffer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class ShaderProgram():
    """com.badlogic.gdx.graphics.glutils.ShaderProgram"""
 
    @staticmethod
    def __wrap(java_value: __ShaderProgram) -> 'ShaderProgram':
        return ShaderProgram(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ShaderProgram):
        """
        Dynamic initializer for ShaderProgram.
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
    def getUniformType(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ShaderProgram.getUniformType(java.lang.String)"""
        return int.__wrap(super(__ShaderProgram, self).getUniformType(arg0))

    @overload
    def getUniformLocation(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ShaderProgram.getUniformLocation(java.lang.String)"""
        return int.__wrap(super(__ShaderProgram, self).getUniformLocation(arg0))

    @overload
    def getUniforms(self) -> List[str]:
        """public java.lang.String[] com.badlogic.gdx.graphics.glutils.ShaderProgram.getUniforms()"""
        return List[str].__wrap(super(ShaderProgram, self).getUniforms())

    @overload
    def setUniformf(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(java.lang.String,float,float,float,float)"""
        super(__ShaderProgram, self).setUniformf(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def setUniform2fv(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniform2fv(int,float[],int,int)"""
        super(__ShaderProgram, self).setUniform2fv(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def setUniformMatrix3fv(self, arg0: str, arg1: 'FloatBuffer', arg2: int, arg3: bool):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix3fv(java.lang.String,java.nio.FloatBuffer,int,boolean)"""
        super(__ShaderProgram, self).setUniformMatrix3fv(arg0, arg1, __int.valueOf(arg2), __boolean.valueOf(arg3))

    @overload
    def getFragmentShaderSource(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.glutils.ShaderProgram.getFragmentShaderSource()"""
        return str.__wrap(super(ShaderProgram, self).getFragmentShaderSource())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setUniformMatrix(self, arg0: str, arg1: 'Matrix4', arg2: bool):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix(java.lang.String,com.badlogic.gdx.math.Matrix4,boolean)"""
        super(__ShaderProgram, self).setUniformMatrix(arg0, arg1, __boolean.valueOf(arg2))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.dispose()"""
        super(ShaderProgram, self).dispose()

    @overload
    def enableVertexAttribute(self, arg0: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.enableVertexAttribute(int)"""
        super(__ShaderProgram, self).enableVertexAttribute(__int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setUniform1fv(self, arg0: str, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniform1fv(java.lang.String,float[],int,int)"""
        super(__ShaderProgram, self).setUniform1fv(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def setUniformi(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformi(int,int,int,int,int)"""
        super(__ShaderProgram, self).setUniformi(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @overload
    def setAttributef(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setAttributef(java.lang.String,float,float,float,float)"""
        super(__ShaderProgram, self).setAttributef(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def disableVertexAttribute(self, arg0: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.disableVertexAttribute(int)"""
        super(__ShaderProgram, self).disableVertexAttribute(__int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setUniform3fv(self, arg0: str, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniform3fv(java.lang.String,float[],int,int)"""
        super(__ShaderProgram, self).setUniform3fv(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def setUniformf(self, arg0: int, arg1: 'Vector4'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(int,com.badlogic.gdx.math.Vector4)"""
        super(__ShaderProgram, self).setUniformf(__int.valueOf(arg0), arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setUniformMatrix(self, arg0: int, arg1: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix(int,com.badlogic.gdx.math.Matrix4)"""
        super(__ShaderProgram, self).setUniformMatrix(__int.valueOf(arg0), arg1)

    @overload
    def isCompiled(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.ShaderProgram.isCompiled()"""
        return bool.__wrap(super(ShaderProgram, self).isCompiled())

    @overload
    def setUniformi(self, arg0: str, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformi(java.lang.String,int,int,int,int)"""
        super(__ShaderProgram, self).setUniformi(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @overload
    def setUniformMatrix4fv(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix4fv(int,float[],int,int)"""
        super(__ShaderProgram, self).setUniformMatrix4fv(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def getAttributes(self) -> List[str]:
        """public java.lang.String[] com.badlogic.gdx.graphics.glutils.ShaderProgram.getAttributes()"""
        return List[str].__wrap(super(ShaderProgram, self).getAttributes())

    @overload
    def setUniformi(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformi(int,int,int,int)"""
        super(__ShaderProgram, self).setUniformi(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def setUniformf(self, arg0: str, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(java.lang.String,float,float,float)"""
        super(__ShaderProgram, self).setUniformf(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def setUniformi(self, arg0: str, arg1: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformi(java.lang.String,int)"""
        super(__ShaderProgram, self).setUniformi(arg0, __int.valueOf(arg1))

    @overload
    def getHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ShaderProgram.getHandle()"""
        return int.__wrap(super(ShaderProgram, self).getHandle())

    @overload
    def setUniformf(self, arg0: str, arg1: 'Color'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(java.lang.String,com.badlogic.gdx.graphics.Color)"""
        super(__ShaderProgram, self).setUniformf(arg0, arg1)

    @overload
    def setUniformMatrix(self, arg0: int, arg1: 'Matrix4', arg2: bool):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix(int,com.badlogic.gdx.math.Matrix4,boolean)"""
        super(__ShaderProgram, self).setUniformMatrix(__int.valueOf(arg0), arg1, __boolean.valueOf(arg2))

    @staticmethod
    @overload
    def clearAllShaderPrograms(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.glutils.ShaderProgram.clearAllShaderPrograms(com.badlogic.gdx.Application)"""
        __ShaderProgram.clearAllShaderPrograms(arg0)

    @overload
    def setUniformi(self, arg0: str, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformi(java.lang.String,int,int,int)"""
        super(__ShaderProgram, self).setUniformi(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def setUniform2fv(self, arg0: str, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniform2fv(java.lang.String,float[],int,int)"""
        super(__ShaderProgram, self).setUniform2fv(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def enableVertexAttribute(self, arg0: str):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.enableVertexAttribute(java.lang.String)"""
        super(__ShaderProgram, self).enableVertexAttribute(arg0)

    @overload
    def setUniform4fv(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniform4fv(int,float[],int,int)"""
        super(__ShaderProgram, self).setUniform4fv(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setVertexAttribute(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setVertexAttribute(int,int,int,boolean,int,int)"""
        super(__ShaderProgram, self).setVertexAttribute(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram(java.lang.String,java.lang.String)"""
        val = __ShaderProgram(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getVertexShaderSource(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.glutils.ShaderProgram.getVertexShaderSource()"""
        return str.__wrap(super(ShaderProgram, self).getVertexShaderSource())

    @overload
    def setUniformf(self, arg0: str, arg1: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(java.lang.String,float)"""
        super(__ShaderProgram, self).setUniformf(arg0, __float.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def bind(self):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.bind()"""
        super(ShaderProgram, self).bind()

    @overload
    def setUniformMatrix(self, arg0: str, arg1: 'Matrix3', arg2: bool):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix(java.lang.String,com.badlogic.gdx.math.Matrix3,boolean)"""
        super(__ShaderProgram, self).setUniformMatrix(arg0, arg1, __boolean.valueOf(arg2))

    @overload
    def setUniformf(self, arg0: int, arg1: 'Color'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(int,com.badlogic.gdx.graphics.Color)"""
        super(__ShaderProgram, self).setUniformf(__int.valueOf(arg0), arg1)

    @overload
    def getAttributeLocation(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ShaderProgram.getAttributeLocation(java.lang.String)"""
        return int.__wrap(super(__ShaderProgram, self).getAttributeLocation(arg0))

    @overload
    def setUniformf(self, arg0: str, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(java.lang.String,float,float)"""
        super(__ShaderProgram, self).setUniformf(arg0, __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def setUniformf(self, arg0: str, arg1: 'Vector3'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(java.lang.String,com.badlogic.gdx.math.Vector3)"""
        super(__ShaderProgram, self).setUniformf(arg0, arg1)

    @overload
    def setUniformf(self, arg0: int, arg1: 'Vector2'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(int,com.badlogic.gdx.math.Vector2)"""
        super(__ShaderProgram, self).setUniformf(__int.valueOf(arg0), arg1)

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.end()"""
        super(ShaderProgram, self).end()

    @overload
    def setUniformf(self, arg0: str, arg1: 'Vector2'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(java.lang.String,com.badlogic.gdx.math.Vector2)"""
        super(__ShaderProgram, self).setUniformf(arg0, arg1)

    @staticmethod
    @overload
    def getManagedStatus() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.glutils.ShaderProgram.getManagedStatus()"""
        return str.__wrap(__ShaderProgram.getManagedStatus())

    @overload
    def getLog(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.glutils.ShaderProgram.getLog()"""
        return str.__wrap(super(ShaderProgram, self).getLog())

    @overload
    def setUniform1fv(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniform1fv(int,float[],int,int)"""
        super(__ShaderProgram, self).setUniform1fv(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def setUniformf(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(int,float)"""
        super(__ShaderProgram, self).setUniformf(__int.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def setUniformf(self, arg0: int, arg1: 'Vector3'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(int,com.badlogic.gdx.math.Vector3)"""
        super(__ShaderProgram, self).setUniformf(__int.valueOf(arg0), arg1)

    @overload
    def setUniformf(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(int,float,float,float)"""
        super(__ShaderProgram, self).setUniformf(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def getAttributeSize(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ShaderProgram.getAttributeSize(java.lang.String)"""
        return int.__wrap(super(__ShaderProgram, self).getAttributeSize(arg0))

    @overload
    def setUniformf(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(int,float,float,float,float)"""
        super(__ShaderProgram, self).setUniformf(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle'):
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        val = __ShaderProgram(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setUniformMatrix(self, arg0: str, arg1: 'Matrix3'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix(java.lang.String,com.badlogic.gdx.math.Matrix3)"""
        super(__ShaderProgram, self).setUniformMatrix(arg0, arg1)

    @overload
    def setUniformi(self, arg0: str, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformi(java.lang.String,int,int)"""
        super(__ShaderProgram, self).setUniformi(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def setVertexAttribute(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'Buffer'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setVertexAttribute(int,int,int,boolean,int,java.nio.Buffer)"""
        super(__ShaderProgram, self).setVertexAttribute(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __int.valueOf(arg4), arg5)

    @overload
    def setVertexAttribute(self, arg0: str, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setVertexAttribute(java.lang.String,int,int,boolean,int,int)"""
        super(__ShaderProgram, self).setVertexAttribute(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @overload
    def setUniformMatrix(self, arg0: int, arg1: 'Matrix3', arg2: bool):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix(int,com.badlogic.gdx.math.Matrix3,boolean)"""
        super(__ShaderProgram, self).setUniformMatrix(__int.valueOf(arg0), arg1, __boolean.valueOf(arg2))

    @overload
    def setUniformi(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformi(int,int)"""
        super(__ShaderProgram, self).setUniformi(__int.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def getNumManagedShaderPrograms() -> int:
        """public static int com.badlogic.gdx.graphics.glutils.ShaderProgram.getNumManagedShaderPrograms()"""
        return int.__wrap(__ShaderProgram.getNumManagedShaderPrograms())

    @overload
    def hasUniform(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.ShaderProgram.hasUniform(java.lang.String)"""
        return bool.__wrap(super(__ShaderProgram, self).hasUniform(arg0))

    @overload
    def getUniformSize(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ShaderProgram.getUniformSize(java.lang.String)"""
        return int.__wrap(super(__ShaderProgram, self).getUniformSize(arg0))

    @overload
    def setUniformMatrix(self, arg0: int, arg1: 'Matrix3'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix(int,com.badlogic.gdx.math.Matrix3)"""
        super(__ShaderProgram, self).setUniformMatrix(__int.valueOf(arg0), arg1)

    @overload
    def setVertexAttribute(self, arg0: str, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'Buffer'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setVertexAttribute(java.lang.String,int,int,boolean,int,java.nio.Buffer)"""
        super(__ShaderProgram, self).setVertexAttribute(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __int.valueOf(arg4), arg5)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def fetchUniformLocation(self, arg0: str, arg1: bool) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ShaderProgram.fetchUniformLocation(java.lang.String,boolean)"""
        return int.__wrap(super(__ShaderProgram, self).fetchUniformLocation(arg0, __boolean.valueOf(arg1)))

    @overload
    def disableVertexAttribute(self, arg0: str):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.disableVertexAttribute(java.lang.String)"""
        super(__ShaderProgram, self).disableVertexAttribute(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setUniformf(self, arg0: str, arg1: 'Vector4'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(java.lang.String,com.badlogic.gdx.math.Vector4)"""
        super(__ShaderProgram, self).setUniformf(arg0, arg1)

    @overload
    def setUniformi(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformi(int,int,int)"""
        super(__ShaderProgram, self).setUniformi(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def getAttributeType(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ShaderProgram.getAttributeType(java.lang.String)"""
        return int.__wrap(super(__ShaderProgram, self).getAttributeType(arg0))

    @overload
    def setUniformMatrix4fv(self, arg0: str, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix4fv(java.lang.String,float[],int,int)"""
        super(__ShaderProgram, self).setUniformMatrix4fv(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def setUniformMatrix(self, arg0: str, arg1: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix(java.lang.String,com.badlogic.gdx.math.Matrix4)"""
        super(__ShaderProgram, self).setUniformMatrix(arg0, arg1)

    @overload
    def setUniformf(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(int,float,float)"""
        super(__ShaderProgram, self).setUniformf(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def setUniform4fv(self, arg0: str, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniform4fv(java.lang.String,float[],int,int)"""
        super(__ShaderProgram, self).setUniform4fv(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def setUniform3fv(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniform3fv(int,float[],int,int)"""
        super(__ShaderProgram, self).setUniform3fv(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def hasAttribute(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.ShaderProgram.hasAttribute(java.lang.String)"""
        return bool.__wrap(super(__ShaderProgram, self).hasAttribute(arg0))

    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.begin()"""
        super(ShaderProgram, self).begin()

    @overload
    def setUniformMatrix4fv(self, arg0: str, arg1: 'FloatBuffer', arg2: int, arg3: bool):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix4fv(java.lang.String,java.nio.FloatBuffer,int,boolean)"""
        super(__ShaderProgram, self).setUniformMatrix4fv(arg0, arg1, __int.valueOf(arg2), __boolean.valueOf(arg3))

    @staticmethod
    @overload
    def invalidateAllShaderPrograms(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.glutils.ShaderProgram.invalidateAllShaderPrograms(com.badlogic.gdx.Application)"""
        __ShaderProgram.invalidateAllShaderPrograms(arg0) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FrameBufferCubemapBuilder
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.graphics.glutils.FrameBufferCubemap as __FrameBufferCubemap
__FrameBufferCubemap = __FrameBufferCubemap
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.glutils.GLFrameBuffer as __GLFrameBuffer_FrameBufferCubemapBuilder
__FrameBufferCubemapBuilder = __GLFrameBuffer_FrameBufferCubemapBuilder.FrameBufferCubemapBuilder
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.graphics.glutils.GLFrameBuffer as __GLFrameBuffer_GLFrameBufferBuilder
__GLFrameBufferBuilder = __GLFrameBuffer_GLFrameBufferBuilder.GLFrameBufferBuilder
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class FrameBufferCubemapBuilder():
    """com.badlogic.gdx.graphics.glutils.GLFrameBuffer.FrameBufferCubemapBuilder"""
 
    @staticmethod
    def __wrap(java_value: __FrameBufferCubemapBuilder) -> 'FrameBufferCubemapBuilder':
        return FrameBufferCubemapBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FrameBufferCubemapBuilder):
        """
        Dynamic initializer for FrameBufferCubemapBuilder.
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
    def addFloatAttachment(self, arg0: int, arg1: int, arg2: int, arg3: bool) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addFloatAttachment(int,int,int,boolean)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addFloatAttachment(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def addStencilDepthPackedRenderBuffer(self, arg0: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addStencilDepthPackedRenderBuffer(int)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addStencilDepthPackedRenderBuffer(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FrameBufferCubemapBuilder(int,int)"""
        val = __FrameBufferCubemapBuilder(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addStencilRenderBuffer(self, arg0: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addStencilRenderBuffer(int)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addStencilRenderBuffer(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def addBasicDepthRenderBuffer(self) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicDepthRenderBuffer()"""
        return 'GLFrameBufferBuilder'.__wrap(super(GLFrameBufferBuilder, self).addBasicDepthRenderBuffer())

    @overload
    def addBasicColorTextureAttachment(self, arg0: 'Format') -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicColorTextureAttachment(com.badlogic.gdx.graphics.Pixmap$Format)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addBasicColorTextureAttachment(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def addStencilTextureAttachment(self, arg0: int, arg1: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addStencilTextureAttachment(int,int)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addStencilTextureAttachment(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def build(self) -> 'FrameBufferCubemap':
        """public com.badlogic.gdx.graphics.glutils.FrameBufferCubemap com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FrameBufferCubemapBuilder.build()"""
        return 'FrameBufferCubemap'.__wrap(super(FrameBufferCubemapBuilder, self).build())

    @override
    @overload
    def addBasicStencilDepthPackedRenderBuffer(self) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicStencilDepthPackedRenderBuffer()"""
        return 'GLFrameBufferBuilder'.__wrap(super(GLFrameBufferBuilder, self).addBasicStencilDepthPackedRenderBuffer())

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
    def addColorTextureAttachment(self, arg0: int, arg1: int, arg2: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addColorTextureAttachment(int,int,int)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addColorTextureAttachment(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def addBasicStencilRenderBuffer(self) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicStencilRenderBuffer()"""
        return 'GLFrameBufferBuilder'.__wrap(super(GLFrameBufferBuilder, self).addBasicStencilRenderBuffer())

    @overload
    def addDepthTextureAttachment(self, arg0: int, arg1: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addDepthTextureAttachment(int,int)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addDepthTextureAttachment(__int.valueOf(arg0), __int.valueOf(arg1)))

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
    def addDepthRenderBuffer(self, arg0: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addDepthRenderBuffer(int)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addDepthRenderBuffer(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.IndexArray
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.nio.ShortBuffer as __ShortBuffer
__ShortBuffer = __ShortBuffer
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.glutils.IndexArray as __IndexArray
__IndexArray = __IndexArray
import java.nio.ShortBuffer as ShortBuffer
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
 
class IndexArray():
    """com.badlogic.gdx.graphics.glutils.IndexArray"""
 
    @staticmethod
    def __wrap(java_value: __IndexArray) -> 'IndexArray':
        return IndexArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IndexArray):
        """
        Dynamic initializer for IndexArray.
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
    def bind(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexArray.bind()"""
        super(IndexArray, self).bind()

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
    def getBuffer(self, arg0: bool) -> 'ShortBuffer':
        """public java.nio.ShortBuffer com.badlogic.gdx.graphics.glutils.IndexArray.getBuffer(boolean)"""
        return 'ShortBuffer'.__wrap(super(__IndexArray, self).getBuffer(__boolean.valueOf(arg0)))

    @override
    @overload
    def getNumIndices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.IndexArray.getNumIndices()"""
        return int.__wrap(super(IndexArray, self).getNumIndices())

    @override
    @overload
    def setIndices(self, arg0: 'short', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.IndexArray.setIndices(short[],int,int)"""
        super(__IndexArray, self).setIndices(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def updateIndices(self, arg0: int, arg1: 'short', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.IndexArray.updateIndices(int,short[],int,int)"""
        super(__IndexArray, self).updateIndices(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def invalidate(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexArray.invalidate()"""
        super(IndexArray, self).invalidate()

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
    def getNumMaxIndices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.IndexArray.getNumMaxIndices()"""
        return int.__wrap(super(IndexArray, self).getNumMaxIndices())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setIndices(self, arg0: 'ShortBuffer'):
        """public void com.badlogic.gdx.graphics.glutils.IndexArray.setIndices(java.nio.ShortBuffer)"""
        super(__IndexArray, self).setIndices(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getBuffer(self) -> 'ShortBuffer':
        """public java.nio.ShortBuffer com.badlogic.gdx.graphics.glutils.IndexArray.getBuffer()"""
        return 'ShortBuffer'.__wrap(super(IndexArray, self).getBuffer())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def unbind(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexArray.unbind()"""
        super(IndexArray, self).unbind()

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.glutils.IndexArray(int)"""
        val = __IndexArray(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexArray.dispose()"""
        super(IndexArray, self).dispose() 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.MipMapGenerator
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.glutils.MipMapGenerator as __MipMapGenerator
__MipMapGenerator = __MipMapGenerator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class MipMapGenerator():
    """com.badlogic.gdx.graphics.glutils.MipMapGenerator"""
 
    @staticmethod
    def __wrap(java_value: __MipMapGenerator) -> 'MipMapGenerator':
        return MipMapGenerator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MipMapGenerator):
        """
        Dynamic initializer for MipMapGenerator.
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

    @staticmethod
    @overload
    def generateMipMap(arg0: int, arg1: 'Pixmap', arg2: int, arg3: int):
        """public static void com.badlogic.gdx.graphics.glutils.MipMapGenerator.generateMipMap(int,com.badlogic.gdx.graphics.Pixmap,int,int)"""
        __MipMapGenerator.generateMipMap(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def setUseHardwareMipMap(arg0: bool):
        """public static void com.badlogic.gdx.graphics.glutils.MipMapGenerator.setUseHardwareMipMap(boolean)"""
        __MipMapGenerator.setUseHardwareMipMap(__boolean.valueOf(arg0))

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

    @staticmethod
    @overload
    def generateMipMap(arg0: 'Pixmap', arg1: int, arg2: int):
        """public static void com.badlogic.gdx.graphics.glutils.MipMapGenerator.generateMipMap(com.badlogic.gdx.graphics.Pixmap,int,int)"""
        __MipMapGenerator.generateMipMap(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

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
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20 as __ImmediateModeRenderer20
__ImmediateModeRenderer20 = __ImmediateModeRenderer20
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.graphics.glutils.ShaderProgram as __ShaderProgram
__ShaderProgram = __ShaderProgram
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class ImmediateModeRenderer20():
    """com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20"""
 
    @staticmethod
    def __wrap(java_value: __ImmediateModeRenderer20) -> 'ImmediateModeRenderer20':
        return ImmediateModeRenderer20(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ImmediateModeRenderer20):
        """
        Dynamic initializer for ImmediateModeRenderer20.
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
    def begin(self, arg0: 'Matrix4', arg1: int):
        """public void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.begin(com.badlogic.gdx.math.Matrix4,int)"""
        super(__ImmediateModeRenderer20, self).begin(arg0, __int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def color(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.color(com.badlogic.gdx.graphics.Color)"""
        super(__ImmediateModeRenderer20, self).color(arg0)

    @overload
    def __init__(self, arg0: bool, arg1: bool, arg2: int):
        """public com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20(boolean,boolean,int)"""
        val = __ImmediateModeRenderer20(__boolean.valueOf(arg0), __boolean.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def color(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.color(float,float,float,float)"""
        super(__ImmediateModeRenderer20, self).color(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getMaxVertices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.getMaxVertices()"""
        return int.__wrap(super(ImmediateModeRenderer20, self).getMaxVertices())

    @override
    @overload
    def vertex(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.vertex(float,float,float)"""
        super(__ImmediateModeRenderer20, self).vertex(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def normal(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.normal(float,float,float)"""
        super(__ImmediateModeRenderer20, self).normal(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def flush(self):
        """public void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.flush()"""
        super(ImmediateModeRenderer20, self).flush()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.end()"""
        super(ImmediateModeRenderer20, self).end()

    @overload
    def __init__(self, arg0: int, arg1: bool, arg2: bool, arg3: int, arg4: 'ShaderProgram'):
        """public com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20(int,boolean,boolean,int,com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        val = __ImmediateModeRenderer20(__int.valueOf(arg0), __boolean.valueOf(arg1), __boolean.valueOf(arg2), __int.valueOf(arg3), arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def color(self, arg0: float):
        """public void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.color(float)"""
        super(__ImmediateModeRenderer20, self).color(__float.valueOf(arg0))

    @overload
    def getShader(self) -> 'ShaderProgram':
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.getShader()"""
        return 'ShaderProgram'.__wrap(super(ImmediateModeRenderer20, self).getShader())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getNumVertices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.getNumVertices()"""
        return int.__wrap(super(ImmediateModeRenderer20, self).getNumVertices())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def texCoord(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.texCoord(float,float)"""
        super(__ImmediateModeRenderer20, self).texCoord(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.dispose()"""
        super(ImmediateModeRenderer20, self).dispose()

    @overload
    def setShader(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.setShader(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(__ImmediateModeRenderer20, self).setShader(arg0)

    @staticmethod
    @overload
    def createDefaultShader(arg0: bool, arg1: bool, arg2: int) -> 'ShaderProgram':
        """public static com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.createDefaultShader(boolean,boolean,int)"""
        return ShaderProgram.__wrap(__ImmediateModeRenderer20.createDefaultShader(__boolean.valueOf(arg0), __boolean.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def __init__(self, arg0: int, arg1: bool, arg2: bool, arg3: int):
        """public com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20(int,boolean,boolean,int)"""
        val = __ImmediateModeRenderer20(__int.valueOf(arg0), __boolean.valueOf(arg1), __boolean.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.FileTextureArrayData
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.graphics.glutils.FileTextureArrayData as __FileTextureArrayData
__FileTextureArrayData = __FileTextureArrayData
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class FileTextureArrayData():
    """com.badlogic.gdx.graphics.glutils.FileTextureArrayData"""
 
    @staticmethod
    def __wrap(java_value: __FileTextureArrayData) -> 'FileTextureArrayData':
        return FileTextureArrayData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FileTextureArrayData):
        """
        Dynamic initializer for FileTextureArrayData.
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
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.FileTextureArrayData.getHeight()"""
        return int.__wrap(super(FileTextureArrayData, self).getHeight())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FileTextureArrayData.isManaged()"""
        return bool.__wrap(super(FileTextureArrayData, self).isManaged())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Format', arg1: bool, arg2: 'FileHandle'):
        """public com.badlogic.gdx.graphics.glutils.FileTextureArrayData(com.badlogic.gdx.graphics.Pixmap$Format,boolean,com.badlogic.gdx.files.FileHandle[])"""
        val = __FileTextureArrayData(arg0, __boolean.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def prepare(self):
        """public void com.badlogic.gdx.graphics.glutils.FileTextureArrayData.prepare()"""
        super(FileTextureArrayData, self).prepare()

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
    def getInternalFormat(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.FileTextureArrayData.getInternalFormat()"""
        return int.__wrap(super(FileTextureArrayData, self).getInternalFormat())

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
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.FileTextureArrayData.getWidth()"""
        return int.__wrap(super(FileTextureArrayData, self).getWidth())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def isPrepared(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FileTextureArrayData.isPrepared()"""
        return bool.__wrap(super(FileTextureArrayData, self).isPrepared())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getDepth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.FileTextureArrayData.getDepth()"""
        return int.__wrap(super(FileTextureArrayData, self).getDepth())

    @override
    @overload
    def consumeTextureArrayData(self):
        """public void com.badlogic.gdx.graphics.glutils.FileTextureArrayData.consumeTextureArrayData()"""
        super(FileTextureArrayData, self).consumeTextureArrayData()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getGLType(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.FileTextureArrayData.getGLType()"""
        return int.__wrap(super(FileTextureArrayData, self).getGLType()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.KTXTextureData
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import com.badlogic.gdx.graphics.TextureData as __TextureData_TextureDataType
__TextureDataType = __TextureData_TextureDataType.TextureDataType
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Pixmap as __Pixmap_Format
__Format = __Pixmap_Format.Format
import com.badlogic.gdx.graphics.glutils.KTXTextureData as __KTXTextureData
__KTXTextureData = __KTXTextureData
import com.badlogic.gdx.graphics.Pixmap as __Pixmap
__Pixmap = __Pixmap
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class KTXTextureData():
    """com.badlogic.gdx.graphics.glutils.KTXTextureData"""
 
    @staticmethod
    def __wrap(java_value: __KTXTextureData) -> 'KTXTextureData':
        return KTXTextureData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __KTXTextureData):
        """
        Dynamic initializer for KTXTextureData.
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
    def disposePreparedData(self):
        """public void com.badlogic.gdx.graphics.glutils.KTXTextureData.disposePreparedData()"""
        super(KTXTextureData, self).disposePreparedData()

    @override
    @overload
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.KTXTextureData.isManaged()"""
        return bool.__wrap(super(KTXTextureData, self).isManaged())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getNumberOfMipMapLevels(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.KTXTextureData.getNumberOfMipMapLevels()"""
        return int.__wrap(super(KTXTextureData, self).getNumberOfMipMapLevels())

    @overload
    def getGlInternalFormat(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.KTXTextureData.getGlInternalFormat()"""
        return int.__wrap(super(KTXTextureData, self).getGlInternalFormat())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getType(self) -> 'graphics.TextureData$TextureDataType':
        """public com.badlogic.gdx.graphics.TextureData$TextureDataType com.badlogic.gdx.graphics.glutils.KTXTextureData.getType()"""
        return 'graphics.TextureData$TextureDataType'.__wrap(super(KTXTextureData, self).getType())

    @override
    @overload
    def getFormat(self) -> 'graphics.Pixmap$Format':
        """public com.badlogic.gdx.graphics.Pixmap$Format com.badlogic.gdx.graphics.glutils.KTXTextureData.getFormat()"""
        return 'graphics.Pixmap$Format'.__wrap(super(KTXTextureData, self).getFormat())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getNumberOfFaces(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.KTXTextureData.getNumberOfFaces()"""
        return int.__wrap(super(KTXTextureData, self).getNumberOfFaces())

    @override
    @overload
    def consumePixmap(self) -> 'graphics.Pixmap':
        """public com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.graphics.glutils.KTXTextureData.consumePixmap()"""
        return 'graphics.Pixmap'.__wrap(super(KTXTextureData, self).consumePixmap())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def prepare(self):
        """public void com.badlogic.gdx.graphics.glutils.KTXTextureData.prepare()"""
        super(KTXTextureData, self).prepare()

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.KTXTextureData.getHeight()"""
        return int.__wrap(super(KTXTextureData, self).getHeight())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.KTXTextureData.getWidth()"""
        return int.__wrap(super(KTXTextureData, self).getWidth())

    @override
    @overload
    def disposePixmap(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.KTXTextureData.disposePixmap()"""
        return bool.__wrap(super(KTXTextureData, self).disposePixmap())

    @override
    @overload
    def consumeCubemapData(self):
        """public void com.badlogic.gdx.graphics.glutils.KTXTextureData.consumeCubemapData()"""
        super(KTXTextureData, self).consumeCubemapData()

    @override
    @overload
    def useMipMaps(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.KTXTextureData.useMipMaps()"""
        return bool.__wrap(super(KTXTextureData, self).useMipMaps())

    @override
    @overload
    def isPrepared(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.KTXTextureData.isPrepared()"""
        return bool.__wrap(super(KTXTextureData, self).isPrepared())

    @overload
    def getData(self, arg0: int, arg1: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.graphics.glutils.KTXTextureData.getData(int,int)"""
        return 'ByteBuffer'.__wrap(super(__KTXTextureData, self).getData(__int.valueOf(arg0), __int.valueOf(arg1)))

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
    def consumeCustomData(self, arg0: int):
        """public void com.badlogic.gdx.graphics.glutils.KTXTextureData.consumeCustomData(int)"""
        super(__KTXTextureData, self).consumeCustomData(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: bool):
        """public com.badlogic.gdx.graphics.glutils.KTXTextureData(com.badlogic.gdx.files.FileHandle,boolean)"""
        val = __KTXTextureData(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.ETC1$ETC1Data
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.glutils.ETC1 as __ETC1_ETC1Data
__ETC1Data = __ETC1_ETC1Data.ETC1Data
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class ETC1Data():
    """com.badlogic.gdx.graphics.glutils.ETC1.ETC1Data"""
 
    @staticmethod
    def __wrap(java_value: __ETC1Data) -> 'ETC1Data':
        return ETC1Data(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ETC1Data):
        """
        Dynamic initializer for ETC1Data.
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
    def write(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.graphics.glutils.ETC1$ETC1Data.write(com.badlogic.gdx.files.FileHandle)"""
        super(__ETC1Data, self).write(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.ETC1$ETC1Data.dispose()"""
        super(ETC1Data, self).dispose()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'ByteBuffer', arg3: int):
        """public com.badlogic.gdx.graphics.glutils.ETC1$ETC1Data(int,int,java.nio.ByteBuffer,int)"""
        val = __ETC1Data(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.glutils.ETC1$ETC1Data.toString()"""
        return str.__wrap(super(ETC1Data, self).toString())

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
    def hasPKMHeader(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.ETC1$ETC1Data.hasPKMHeader()"""
        return bool.__wrap(super(ETC1Data, self).hasPKMHeader())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'FileHandle'):
        """public com.badlogic.gdx.graphics.glutils.ETC1$ETC1Data(com.badlogic.gdx.files.FileHandle)"""
        val = __ETC1Data(arg0)
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
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer as __ImmediateModeRenderer
__ImmediateModeRenderer = __ImmediateModeRenderer
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from abc import abstractmethod, ABC
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

 
class ImmediateModeRenderer(ABC):
    """com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer"""
 
    @staticmethod
    def __wrap(java_value: __ImmediateModeRenderer) -> 'ImmediateModeRenderer':
        return ImmediateModeRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ImmediateModeRenderer):
        """
        Dynamic initializer for ImmediateModeRenderer.
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
    def begin(self, arg0: 'Matrix4', arg1: int):
        """public abstract void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer.begin(com.badlogic.gdx.math.Matrix4,int)"""
        pass

    @abstractmethod
    def texCoord(self, arg0: float, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer.texCoord(float,float)"""
        pass

    @abstractmethod
    def normal(self, arg0: float, arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer.normal(float,float,float)"""
        pass

    @abstractmethod
    def vertex(self, arg0: float, arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer.vertex(float,float,float)"""
        pass

    @abstractmethod
    def color(self, arg0: float):
        """public abstract void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer.color(float)"""
        pass

    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer.dispose()"""
        pass

    @abstractmethod
    def getNumVertices(self, ):
        """public abstract int com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer.getNumVertices()"""
        pass

    @abstractmethod
    def getMaxVertices(self, ):
        """public abstract int com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer.getMaxVertices()"""
        pass

    @abstractmethod
    def color(self, arg0: 'Color'):
        """public abstract void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer.color(com.badlogic.gdx.graphics.Color)"""
        pass

    @abstractmethod
    def flush(self, ):
        """public abstract void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer.flush()"""
        pass

    @abstractmethod
    def color(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer.color(float,float,float,float)"""
        pass

    @abstractmethod
    def end(self, ):
        """public abstract void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer.end()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.VertexData
import com.badlogic.gdx.graphics.glutils.VertexData as __VertexData
__VertexData = __VertexData
from builtins import float
from abc import abstractmethod, ABC
from builtins import int
 
class VertexData(ABC):
    """com.badlogic.gdx.graphics.glutils.VertexData"""
 
    @staticmethod
    def __wrap(java_value: __VertexData) -> 'VertexData':
        return VertexData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __VertexData):
        """
        Dynamic initializer for VertexData.
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
    def getAttributes(self, ):
        """public abstract com.badlogic.gdx.graphics.VertexAttributes com.badlogic.gdx.graphics.glutils.VertexData.getAttributes()"""
        pass

    @abstractmethod
    def getBuffer(self, arg0: bool):
        """public abstract java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.VertexData.getBuffer(boolean)"""
        pass

    @abstractmethod
    def getNumVertices(self, ):
        """public abstract int com.badlogic.gdx.graphics.glutils.VertexData.getNumVertices()"""
        pass

    @abstractmethod
    def invalidate(self, ):
        """public abstract void com.badlogic.gdx.graphics.glutils.VertexData.invalidate()"""
        pass

    @abstractmethod
    def unbind(self, arg0: 'ShaderProgram'):
        """public abstract void com.badlogic.gdx.graphics.glutils.VertexData.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        pass

    @abstractmethod
    def bind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public abstract void com.badlogic.gdx.graphics.glutils.VertexData.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        pass

    @abstractmethod
    def getNumMaxVertices(self, ):
        """public abstract int com.badlogic.gdx.graphics.glutils.VertexData.getNumMaxVertices()"""
        pass

    @abstractmethod
    def setVertices(self, arg0: 'float', arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.glutils.VertexData.setVertices(float[],int,int)"""
        pass

    @abstractmethod
    def bind(self, arg0: 'ShaderProgram'):
        """public abstract void com.badlogic.gdx.graphics.glutils.VertexData.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        pass

    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.graphics.glutils.VertexData.dispose()"""
        pass

    @abstractmethod
    def updateVertices(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.glutils.VertexData.updateVertices(int,float[],int,int)"""
        pass

    @abstractmethod
    def getBuffer(self, ):
        """public abstract java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.VertexData.getBuffer()"""
        pass

    @abstractmethod
    def unbind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public abstract void com.badlogic.gdx.graphics.glutils.VertexData.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.VertexArray
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.glutils.VertexArray as __VertexArray
__VertexArray = __VertexArray
from builtins import float
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.VertexAttributes as __VertexAttributes
__VertexAttributes = __VertexAttributes
import java.nio.FloatBuffer as __FloatBuffer
__FloatBuffer = __FloatBuffer
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class VertexArray():
    """com.badlogic.gdx.graphics.glutils.VertexArray"""
 
    @staticmethod
    def __wrap(java_value: __VertexArray) -> 'VertexArray':
        return VertexArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __VertexArray):
        """
        Dynamic initializer for VertexArray.
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
    def unbind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.glutils.VertexArray.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(__VertexArray, self).unbind(arg0)

    @override
    @overload
    def bind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.glutils.VertexArray.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(__VertexArray, self).bind(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setVertices(self, arg0: 'float', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.VertexArray.setVertices(float[],int,int)"""
        super(__VertexArray, self).setVertices(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def getNumMaxVertices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.VertexArray.getNumMaxVertices()"""
        return int.__wrap(super(VertexArray, self).getNumMaxVertices())

    @override
    @overload
    def getAttributes(self) -> 'graphics.VertexAttributes':
        """public com.badlogic.gdx.graphics.VertexAttributes com.badlogic.gdx.graphics.glutils.VertexArray.getAttributes()"""
        return 'graphics.VertexAttributes'.__wrap(super(VertexArray, self).getAttributes())

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
    def getBuffer(self) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.VertexArray.getBuffer()"""
        return 'FloatBuffer'.__wrap(super(VertexArray, self).getBuffer())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int, arg1: 'VertexAttributes'):
        """public com.badlogic.gdx.graphics.glutils.VertexArray(int,com.badlogic.gdx.graphics.VertexAttributes)"""
        val = __VertexArray(__int.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def invalidate(self):
        """public void com.badlogic.gdx.graphics.glutils.VertexArray.invalidate()"""
        super(VertexArray, self).invalidate()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getBuffer(self, arg0: bool) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.VertexArray.getBuffer(boolean)"""
        return 'FloatBuffer'.__wrap(super(__VertexArray, self).getBuffer(__boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.VertexArray.dispose()"""
        super(VertexArray, self).dispose()

    @override
    @overload
    def bind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public void com.badlogic.gdx.graphics.glutils.VertexArray.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        super(__VertexArray, self).bind(arg0, arg1)

    @override
    @overload
    def unbind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public void com.badlogic.gdx.graphics.glutils.VertexArray.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        super(__VertexArray, self).unbind(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: int, *arg1: 'graphics.VertexAttribute'):
        """public com.badlogic.gdx.graphics.glutils.VertexArray(int,com.badlogic.gdx.graphics.VertexAttribute...)"""
        val = __VertexArray(__int.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def updateVertices(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.VertexArray.updateVertices(int,float[],int,int)"""
        super(__VertexArray, self).updateVertices(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def getNumVertices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.VertexArray.getNumVertices()"""
        return int.__wrap(super(VertexArray, self).getNumVertices()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.FileTextureData
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.files.FileHandle as __FileHandle
__FileHandle = __FileHandle
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.TextureData as __TextureData_TextureDataType
__TextureDataType = __TextureData_TextureDataType.TextureDataType
import com.badlogic.gdx.graphics.glutils.FileTextureData as __FileTextureData
__FileTextureData = __FileTextureData
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Pixmap as __Pixmap_Format
__Format = __Pixmap_Format.Format
import com.badlogic.gdx.graphics.Pixmap as __Pixmap
__Pixmap = __Pixmap
import java.lang.Integer as __int
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class FileTextureData():
    """com.badlogic.gdx.graphics.glutils.FileTextureData"""
 
    @staticmethod
    def __wrap(java_value: __FileTextureData) -> 'FileTextureData':
        return FileTextureData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FileTextureData):
        """
        Dynamic initializer for FileTextureData.
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
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FileTextureData.isManaged()"""
        return bool.__wrap(super(FileTextureData, self).isManaged())

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.FileTextureData.getWidth()"""
        return int.__wrap(super(FileTextureData, self).getWidth())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.glutils.FileTextureData.toString()"""
        return str.__wrap(super(FileTextureData, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def prepare(self):
        """public void com.badlogic.gdx.graphics.glutils.FileTextureData.prepare()"""
        super(FileTextureData, self).prepare()

    @override
    @overload
    def consumePixmap(self) -> 'graphics.Pixmap':
        """public com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.graphics.glutils.FileTextureData.consumePixmap()"""
        return 'graphics.Pixmap'.__wrap(super(FileTextureData, self).consumePixmap())

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
    def getType(self) -> 'graphics.TextureData$TextureDataType':
        """public com.badlogic.gdx.graphics.TextureData$TextureDataType com.badlogic.gdx.graphics.glutils.FileTextureData.getType()"""
        return 'graphics.TextureData$TextureDataType'.__wrap(super(FileTextureData, self).getType())

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.FileTextureData.getHeight()"""
        return int.__wrap(super(FileTextureData, self).getHeight())

    @override
    @overload
    def useMipMaps(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FileTextureData.useMipMaps()"""
        return bool.__wrap(super(FileTextureData, self).useMipMaps())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isPrepared(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FileTextureData.isPrepared()"""
        return bool.__wrap(super(FileTextureData, self).isPrepared())

    @override
    @overload
    def disposePixmap(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FileTextureData.disposePixmap()"""
        return bool.__wrap(super(FileTextureData, self).disposePixmap())

    @overload
    def getFileHandle(self) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.graphics.glutils.FileTextureData.getFileHandle()"""
        return 'files.FileHandle'.__wrap(super(FileTextureData, self).getFileHandle())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getFormat(self) -> 'graphics.Pixmap$Format':
        """public com.badlogic.gdx.graphics.Pixmap$Format com.badlogic.gdx.graphics.glutils.FileTextureData.getFormat()"""
        return 'graphics.Pixmap$Format'.__wrap(super(FileTextureData, self).getFormat())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def consumeCustomData(self, arg0: int):
        """public void com.badlogic.gdx.graphics.glutils.FileTextureData.consumeCustomData(int)"""
        super(__FileTextureData, self).consumeCustomData(__int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'Pixmap', arg2: 'Format', arg3: bool):
        """public com.badlogic.gdx.graphics.glutils.FileTextureData(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap$Format,boolean)"""
        val = __FileTextureData(arg0, arg1, arg2, __boolean.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.InstanceData
from builtins import float
import com.badlogic.gdx.graphics.glutils.InstanceData as __InstanceData
__InstanceData = __InstanceData
from abc import abstractmethod, ABC
import java.nio.FloatBuffer as FloatBuffer
from builtins import int
 
class InstanceData(ABC):
    """com.badlogic.gdx.graphics.glutils.InstanceData"""
 
    @staticmethod
    def __wrap(java_value: __InstanceData) -> 'InstanceData':
        return InstanceData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InstanceData):
        """
        Dynamic initializer for InstanceData.
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
    def getNumInstances(self, ):
        """public abstract int com.badlogic.gdx.graphics.glutils.InstanceData.getNumInstances()"""
        pass

    @abstractmethod
    def invalidate(self, ):
        """public abstract void com.badlogic.gdx.graphics.glutils.InstanceData.invalidate()"""
        pass

    @abstractmethod
    def bind(self, arg0: 'ShaderProgram'):
        """public abstract void com.badlogic.gdx.graphics.glutils.InstanceData.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        pass

    @abstractmethod
    def getBuffer(self, ):
        """public abstract java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.InstanceData.getBuffer()"""
        pass

    @abstractmethod
    def unbind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public abstract void com.badlogic.gdx.graphics.glutils.InstanceData.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        pass

    @abstractmethod
    def getNumMaxInstances(self, ):
        """public abstract int com.badlogic.gdx.graphics.glutils.InstanceData.getNumMaxInstances()"""
        pass

    @abstractmethod
    def setInstanceData(self, arg0: 'float', arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.glutils.InstanceData.setInstanceData(float[],int,int)"""
        pass

    @abstractmethod
    def unbind(self, arg0: 'ShaderProgram'):
        """public abstract void com.badlogic.gdx.graphics.glutils.InstanceData.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        pass

    @abstractmethod
    def bind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public abstract void com.badlogic.gdx.graphics.glutils.InstanceData.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        pass

    @abstractmethod
    def getBuffer(self, arg0: bool):
        """public abstract java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.InstanceData.getBuffer(boolean)"""
        pass

    @abstractmethod
    def getAttributes(self, ):
        """public abstract com.badlogic.gdx.graphics.VertexAttributes com.badlogic.gdx.graphics.glutils.InstanceData.getAttributes()"""
        pass

    @abstractmethod
    def updateInstanceData(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.glutils.InstanceData.updateInstanceData(int,float[],int,int)"""
        pass

    @abstractmethod
    def setInstanceData(self, arg0: 'FloatBuffer', arg1: int):
        """public abstract void com.badlogic.gdx.graphics.glutils.InstanceData.setInstanceData(java.nio.FloatBuffer,int)"""
        pass

    @abstractmethod
    def updateInstanceData(self, arg0: int, arg1: 'FloatBuffer', arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.glutils.InstanceData.updateInstanceData(int,java.nio.FloatBuffer,int,int)"""
        pass

    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.graphics.glutils.InstanceData.dispose()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.GLVersion
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.glutils.GLVersion as __GLVersion
__GLVersion = __GLVersion
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
import com.badlogic.gdx.graphics.glutils.GLVersion as __GLVersion_Type
__Type = __GLVersion_Type.Type
from builtins import int
 
class GLVersion():
    """com.badlogic.gdx.graphics.glutils.GLVersion"""
 
    @staticmethod
    def __wrap(java_value: __GLVersion) -> 'GLVersion':
        return GLVersion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLVersion):
        """
        Dynamic initializer for GLVersion.
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
    def getType(self) -> 'Type':
        """public com.badlogic.gdx.graphics.glutils.GLVersion$Type com.badlogic.gdx.graphics.glutils.GLVersion.getType()"""
        return 'Type'.__wrap(super(GLVersion, self).getType())

    @overload
    def getReleaseVersion(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLVersion.getReleaseVersion()"""
        return int.__wrap(super(GLVersion, self).getReleaseVersion())

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
    def __init__(self, arg0: 'ApplicationType', arg1: str, arg2: str, arg3: str):
        """public com.badlogic.gdx.graphics.glutils.GLVersion(com.badlogic.gdx.Application$ApplicationType,java.lang.String,java.lang.String,java.lang.String)"""
        val = __GLVersion(arg0, arg1, arg2, arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getRendererString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.glutils.GLVersion.getRendererString()"""
        return str.__wrap(super(GLVersion, self).getRendererString())

    @overload
    def isVersionEqualToOrHigher(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.GLVersion.isVersionEqualToOrHigher(int,int)"""
        return bool.__wrap(super(__GLVersion, self).isVersionEqualToOrHigher(__int.valueOf(arg0), __int.valueOf(arg1)))

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
    def getDebugVersionString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.glutils.GLVersion.getDebugVersionString()"""
        return str.__wrap(super(GLVersion, self).getDebugVersionString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getMajorVersion(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLVersion.getMajorVersion()"""
        return int.__wrap(super(GLVersion, self).getMajorVersion())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getMinorVersion(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLVersion.getMinorVersion()"""
        return int.__wrap(super(GLVersion, self).getMinorVersion())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getVendorString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.glutils.GLVersion.getVendorString()"""
        return str.__wrap(super(GLVersion, self).getVendorString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.ETC1TextureData
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.TextureData as __TextureData_TextureDataType
__TextureDataType = __TextureData_TextureDataType.TextureDataType
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Pixmap as __Pixmap_Format
__Format = __Pixmap_Format.Format
import com.badlogic.gdx.graphics.Pixmap as __Pixmap
__Pixmap = __Pixmap
import java.lang.Integer as __int
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
import com.badlogic.gdx.graphics.glutils.ETC1TextureData as __ETC1TextureData
__ETC1TextureData = __ETC1TextureData
from builtins import int
 
class ETC1TextureData():
    """com.badlogic.gdx.graphics.glutils.ETC1TextureData"""
 
    @staticmethod
    def __wrap(java_value: __ETC1TextureData) -> 'ETC1TextureData':
        return ETC1TextureData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ETC1TextureData):
        """
        Dynamic initializer for ETC1TextureData.
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
    def __init__(self, arg0: 'ETC1Data', arg1: bool):
        """public com.badlogic.gdx.graphics.glutils.ETC1TextureData(com.badlogic.gdx.graphics.glutils.ETC1$ETC1Data,boolean)"""
        val = __ETC1TextureData(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def consumePixmap(self) -> 'graphics.Pixmap':
        """public com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.graphics.glutils.ETC1TextureData.consumePixmap()"""
        return 'graphics.Pixmap'.__wrap(super(ETC1TextureData, self).consumePixmap())

    @override
    @overload
    def prepare(self):
        """public void com.badlogic.gdx.graphics.glutils.ETC1TextureData.prepare()"""
        super(ETC1TextureData, self).prepare()

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ETC1TextureData.getWidth()"""
        return int.__wrap(super(ETC1TextureData, self).getWidth())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getFormat(self) -> 'graphics.Pixmap$Format':
        """public com.badlogic.gdx.graphics.Pixmap$Format com.badlogic.gdx.graphics.glutils.ETC1TextureData.getFormat()"""
        return 'graphics.Pixmap$Format'.__wrap(super(ETC1TextureData, self).getFormat())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def useMipMaps(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.ETC1TextureData.useMipMaps()"""
        return bool.__wrap(super(ETC1TextureData, self).useMipMaps())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'FileHandle'):
        """public com.badlogic.gdx.graphics.glutils.ETC1TextureData(com.badlogic.gdx.files.FileHandle)"""
        val = __ETC1TextureData(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def isPrepared(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.ETC1TextureData.isPrepared()"""
        return bool.__wrap(super(ETC1TextureData, self).isPrepared())

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ETC1TextureData.getHeight()"""
        return int.__wrap(super(ETC1TextureData, self).getHeight())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.ETC1TextureData.isManaged()"""
        return bool.__wrap(super(ETC1TextureData, self).isManaged())

    @override
    @overload
    def consumeCustomData(self, arg0: int):
        """public void com.badlogic.gdx.graphics.glutils.ETC1TextureData.consumeCustomData(int)"""
        super(__ETC1TextureData, self).consumeCustomData(__int.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def disposePixmap(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.ETC1TextureData.disposePixmap()"""
        return bool.__wrap(super(ETC1TextureData, self).disposePixmap())

    @override
    @overload
    def getType(self) -> 'graphics.TextureData$TextureDataType':
        """public com.badlogic.gdx.graphics.TextureData$TextureDataType com.badlogic.gdx.graphics.glutils.ETC1TextureData.getType()"""
        return 'graphics.TextureData$TextureDataType'.__wrap(super(ETC1TextureData, self).getType())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: bool):
        """public com.badlogic.gdx.graphics.glutils.ETC1TextureData(com.badlogic.gdx.files.FileHandle,boolean)"""
        val = __ETC1TextureData(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.GLOnlyTextureData
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.TextureData as __TextureData_TextureDataType
__TextureDataType = __TextureData_TextureDataType.TextureDataType
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.graphics.glutils.GLOnlyTextureData as __GLOnlyTextureData
__GLOnlyTextureData = __GLOnlyTextureData
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Pixmap as __Pixmap_Format
__Format = __Pixmap_Format.Format
import com.badlogic.gdx.graphics.Pixmap as __Pixmap
__Pixmap = __Pixmap
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class GLOnlyTextureData():
    """com.badlogic.gdx.graphics.glutils.GLOnlyTextureData"""
 
    @staticmethod
    def __wrap(java_value: __GLOnlyTextureData) -> 'GLOnlyTextureData':
        return GLOnlyTextureData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLOnlyTextureData):
        """
        Dynamic initializer for GLOnlyTextureData.
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
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public com.badlogic.gdx.graphics.glutils.GLOnlyTextureData(int,int,int,int,int,int)"""
        val = __GLOnlyTextureData(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.GLOnlyTextureData.isManaged()"""
        return bool.__wrap(super(GLOnlyTextureData, self).isManaged())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getType(self) -> 'graphics.TextureData$TextureDataType':
        """public com.badlogic.gdx.graphics.TextureData$TextureDataType com.badlogic.gdx.graphics.glutils.GLOnlyTextureData.getType()"""
        return 'graphics.TextureData$TextureDataType'.__wrap(super(GLOnlyTextureData, self).getType())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def consumeCustomData(self, arg0: int):
        """public void com.badlogic.gdx.graphics.glutils.GLOnlyTextureData.consumeCustomData(int)"""
        super(__GLOnlyTextureData, self).consumeCustomData(__int.valueOf(arg0))

    @override
    @overload
    def useMipMaps(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.GLOnlyTextureData.useMipMaps()"""
        return bool.__wrap(super(GLOnlyTextureData, self).useMipMaps())

    @override
    @overload
    def disposePixmap(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.GLOnlyTextureData.disposePixmap()"""
        return bool.__wrap(super(GLOnlyTextureData, self).disposePixmap())

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
    def getFormat(self) -> 'graphics.Pixmap$Format':
        """public com.badlogic.gdx.graphics.Pixmap$Format com.badlogic.gdx.graphics.glutils.GLOnlyTextureData.getFormat()"""
        return 'graphics.Pixmap$Format'.__wrap(super(GLOnlyTextureData, self).getFormat())

    @override
    @overload
    def isPrepared(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.GLOnlyTextureData.isPrepared()"""
        return bool.__wrap(super(GLOnlyTextureData, self).isPrepared())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLOnlyTextureData.getWidth()"""
        return int.__wrap(super(GLOnlyTextureData, self).getWidth())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLOnlyTextureData.getHeight()"""
        return int.__wrap(super(GLOnlyTextureData, self).getHeight())

    @override
    @overload
    def prepare(self):
        """public void com.badlogic.gdx.graphics.glutils.GLOnlyTextureData.prepare()"""
        super(GLOnlyTextureData, self).prepare()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def consumePixmap(self) -> 'graphics.Pixmap':
        """public com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.graphics.glutils.GLOnlyTextureData.consumePixmap()"""
        return 'graphics.Pixmap'.__wrap(super(GLOnlyTextureData, self).consumePixmap()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.PixmapTextureData
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.TextureData as __TextureData_TextureDataType
__TextureDataType = __TextureData_TextureDataType.TextureDataType
import com.badlogic.gdx.graphics.glutils.PixmapTextureData as __PixmapTextureData
__PixmapTextureData = __PixmapTextureData
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Pixmap as __Pixmap_Format
__Format = __Pixmap_Format.Format
import com.badlogic.gdx.graphics.Pixmap as __Pixmap
__Pixmap = __Pixmap
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class PixmapTextureData():
    """com.badlogic.gdx.graphics.glutils.PixmapTextureData"""
 
    @staticmethod
    def __wrap(java_value: __PixmapTextureData) -> 'PixmapTextureData':
        return PixmapTextureData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PixmapTextureData):
        """
        Dynamic initializer for PixmapTextureData.
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
    def consumeCustomData(self, arg0: int):
        """public void com.badlogic.gdx.graphics.glutils.PixmapTextureData.consumeCustomData(int)"""
        super(__PixmapTextureData, self).consumeCustomData(__int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.PixmapTextureData.isManaged()"""
        return bool.__wrap(super(PixmapTextureData, self).isManaged())

    @override
    @overload
    def disposePixmap(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.PixmapTextureData.disposePixmap()"""
        return bool.__wrap(super(PixmapTextureData, self).disposePixmap())

    @override
    @overload
    def consumePixmap(self) -> 'graphics.Pixmap':
        """public com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.graphics.glutils.PixmapTextureData.consumePixmap()"""
        return 'graphics.Pixmap'.__wrap(super(PixmapTextureData, self).consumePixmap())

    @override
    @overload
    def isPrepared(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.PixmapTextureData.isPrepared()"""
        return bool.__wrap(super(PixmapTextureData, self).isPrepared())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Pixmap', arg1: 'Format', arg2: bool, arg3: bool):
        """public com.badlogic.gdx.graphics.glutils.PixmapTextureData(com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap$Format,boolean,boolean)"""
        val = __PixmapTextureData(arg0, arg1, __boolean.valueOf(arg2), __boolean.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def prepare(self):
        """public void com.badlogic.gdx.graphics.glutils.PixmapTextureData.prepare()"""
        super(PixmapTextureData, self).prepare()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getFormat(self) -> 'graphics.Pixmap$Format':
        """public com.badlogic.gdx.graphics.Pixmap$Format com.badlogic.gdx.graphics.glutils.PixmapTextureData.getFormat()"""
        return 'graphics.Pixmap$Format'.__wrap(super(PixmapTextureData, self).getFormat())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getType(self) -> 'graphics.TextureData$TextureDataType':
        """public com.badlogic.gdx.graphics.TextureData$TextureDataType com.badlogic.gdx.graphics.glutils.PixmapTextureData.getType()"""
        return 'graphics.TextureData$TextureDataType'.__wrap(super(PixmapTextureData, self).getType())

    @override
    @overload
    def useMipMaps(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.PixmapTextureData.useMipMaps()"""
        return bool.__wrap(super(PixmapTextureData, self).useMipMaps())

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.PixmapTextureData.getHeight()"""
        return int.__wrap(super(PixmapTextureData, self).getHeight())

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
    def __init__(self, arg0: 'Pixmap', arg1: 'Format', arg2: bool, arg3: bool, arg4: bool):
        """public com.badlogic.gdx.graphics.glutils.PixmapTextureData(com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap$Format,boolean,boolean,boolean)"""
        val = __PixmapTextureData(arg0, arg1, __boolean.valueOf(arg2), __boolean.valueOf(arg3), __boolean.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.PixmapTextureData.getWidth()"""
        return int.__wrap(super(PixmapTextureData, self).getWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.FacedCubemapData
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.glutils.FacedCubemapData as __FacedCubemapData
__FacedCubemapData = __FacedCubemapData
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.graphics.TextureData as __TextureData
__TextureData = __TextureData
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class FacedCubemapData():
    """com.badlogic.gdx.graphics.glutils.FacedCubemapData"""
 
    @staticmethod
    def __wrap(java_value: __FacedCubemapData) -> 'FacedCubemapData':
        return FacedCubemapData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FacedCubemapData):
        """
        Dynamic initializer for FacedCubemapData.
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
    def consumeCubemapData(self):
        """public void com.badlogic.gdx.graphics.glutils.FacedCubemapData.consumeCubemapData()"""
        super(FacedCubemapData, self).consumeCubemapData()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def load(self, arg0: 'CubemapSide', arg1: 'Pixmap'):
        """public void com.badlogic.gdx.graphics.glutils.FacedCubemapData.load(com.badlogic.gdx.graphics.Cubemap$CubemapSide,com.badlogic.gdx.graphics.Pixmap)"""
        super(__FacedCubemapData, self).load(arg0, arg1)

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: 'Format'):
        """public com.badlogic.gdx.graphics.glutils.FacedCubemapData(int,int,int,com.badlogic.gdx.graphics.Pixmap$Format)"""
        val = __FacedCubemapData(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.FacedCubemapData.getHeight()"""
        return int.__wrap(super(FacedCubemapData, self).getHeight())

    @overload
    def getTextureData(self, arg0: 'CubemapSide') -> 'graphics.TextureData':
        """public com.badlogic.gdx.graphics.TextureData com.badlogic.gdx.graphics.glutils.FacedCubemapData.getTextureData(com.badlogic.gdx.graphics.Cubemap$CubemapSide)"""
        return 'graphics.TextureData'.__wrap(super(__FacedCubemapData, self).getTextureData(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.glutils.FacedCubemapData()"""
        val = __FacedCubemapData()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.FacedCubemapData.getWidth()"""
        return int.__wrap(super(FacedCubemapData, self).getWidth())

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle', arg2: 'FileHandle', arg3: 'FileHandle', arg4: 'FileHandle', arg5: 'FileHandle'):
        """public com.badlogic.gdx.graphics.glutils.FacedCubemapData(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        val = __FacedCubemapData(arg0, arg1, arg2, arg3, arg4, arg5)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Pixmap', arg1: 'Pixmap', arg2: 'Pixmap', arg3: 'Pixmap', arg4: 'Pixmap', arg5: 'Pixmap', arg6: bool):
        """public com.badlogic.gdx.graphics.glutils.FacedCubemapData(com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,boolean)"""
        val = __FacedCubemapData(arg0, arg1, arg2, arg3, arg4, arg5, __boolean.valueOf(arg6))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def prepare(self):
        """public void com.badlogic.gdx.graphics.glutils.FacedCubemapData.prepare()"""
        super(FacedCubemapData, self).prepare()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def load(self, arg0: 'CubemapSide', arg1: 'FileHandle'):
        """public void com.badlogic.gdx.graphics.glutils.FacedCubemapData.load(com.badlogic.gdx.graphics.Cubemap$CubemapSide,com.badlogic.gdx.files.FileHandle)"""
        super(__FacedCubemapData, self).load(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.glutils.FacedCubemapData()"""
        val = __FacedCubemapData()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle', arg2: 'FileHandle', arg3: 'FileHandle', arg4: 'FileHandle', arg5: 'FileHandle', arg6: bool):
        """public com.badlogic.gdx.graphics.glutils.FacedCubemapData(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,boolean)"""
        val = __FacedCubemapData(arg0, arg1, arg2, arg3, arg4, arg5, __boolean.valueOf(arg6))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isPrepared(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FacedCubemapData.isPrepared()"""
        return bool.__wrap(super(FacedCubemapData, self).isPrepared())

    @overload
    def __init__(self, arg0: 'Pixmap', arg1: 'Pixmap', arg2: 'Pixmap', arg3: 'Pixmap', arg4: 'Pixmap', arg5: 'Pixmap'):
        """public com.badlogic.gdx.graphics.glutils.FacedCubemapData(com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap)"""
        val = __FacedCubemapData(arg0, arg1, arg2, arg3, arg4, arg5)
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'TextureData', arg1: 'TextureData', arg2: 'TextureData', arg3: 'TextureData', arg4: 'TextureData', arg5: 'TextureData'):
        """public com.badlogic.gdx.graphics.glutils.FacedCubemapData(com.badlogic.gdx.graphics.TextureData,com.badlogic.gdx.graphics.TextureData,com.badlogic.gdx.graphics.TextureData,com.badlogic.gdx.graphics.TextureData,com.badlogic.gdx.graphics.TextureData,com.badlogic.gdx.graphics.TextureData)"""
        val = __FacedCubemapData(arg0, arg1, arg2, arg3, arg4, arg5)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FacedCubemapData.isManaged()"""
        return bool.__wrap(super(FacedCubemapData, self).isManaged())

    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FacedCubemapData.isComplete()"""
        return bool.__wrap(super(FacedCubemapData, self).isComplete()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.InstanceBufferObject
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.glutils.InstanceBufferObject as __InstanceBufferObject
__InstanceBufferObject = __InstanceBufferObject
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.VertexAttributes as __VertexAttributes
__VertexAttributes = __VertexAttributes
import java.nio.FloatBuffer as __FloatBuffer
__FloatBuffer = __FloatBuffer
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class InstanceBufferObject():
    """com.badlogic.gdx.graphics.glutils.InstanceBufferObject"""
 
    @staticmethod
    def __wrap(java_value: __InstanceBufferObject) -> 'InstanceBufferObject':
        return InstanceBufferObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InstanceBufferObject):
        """
        Dynamic initializer for InstanceBufferObject.
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
    def unbind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObject.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        super(__InstanceBufferObject, self).unbind(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getBuffer(self, arg0: bool) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.InstanceBufferObject.getBuffer(boolean)"""
        return 'FloatBuffer'.__wrap(super(__InstanceBufferObject, self).getBuffer(__boolean.valueOf(arg0)))

    @override
    @overload
    def getBuffer(self) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.InstanceBufferObject.getBuffer()"""
        return 'FloatBuffer'.__wrap(super(InstanceBufferObject, self).getBuffer())

    @override
    @overload
    def unbind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObject.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(__InstanceBufferObject, self).unbind(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: bool, arg1: int, *arg2: 'graphics.VertexAttribute'):
        """public com.badlogic.gdx.graphics.glutils.InstanceBufferObject(boolean,int,com.badlogic.gdx.graphics.VertexAttribute...)"""
        val = __InstanceBufferObject(__boolean.valueOf(arg0), __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: bool, arg1: int, arg2: 'VertexAttributes'):
        """public com.badlogic.gdx.graphics.glutils.InstanceBufferObject(boolean,int,com.badlogic.gdx.graphics.VertexAttributes)"""
        val = __InstanceBufferObject(__boolean.valueOf(arg0), __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setInstanceData(self, arg0: 'FloatBuffer', arg1: int):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObject.setInstanceData(java.nio.FloatBuffer,int)"""
        super(__InstanceBufferObject, self).setInstanceData(arg0, __int.valueOf(arg1))

    @override
    @overload
    def setInstanceData(self, arg0: 'float', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObject.setInstanceData(float[],int,int)"""
        super(__InstanceBufferObject, self).setInstanceData(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def updateInstanceData(self, arg0: int, arg1: 'FloatBuffer', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObject.updateInstanceData(int,java.nio.FloatBuffer,int,int)"""
        super(__InstanceBufferObject, self).updateInstanceData(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObject.dispose()"""
        super(InstanceBufferObject, self).dispose()

    @override
    @overload
    def updateInstanceData(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObject.updateInstanceData(int,float[],int,int)"""
        super(__InstanceBufferObject, self).updateInstanceData(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def getNumInstances(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.InstanceBufferObject.getNumInstances()"""
        return int.__wrap(super(InstanceBufferObject, self).getNumInstances())

    @override
    @overload
    def bind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObject.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        super(__InstanceBufferObject, self).bind(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def invalidate(self):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObject.invalidate()"""
        super(InstanceBufferObject, self).invalidate()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def bind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObject.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(__InstanceBufferObject, self).bind(arg0)

    @override
    @overload
    def getAttributes(self) -> 'graphics.VertexAttributes':
        """public com.badlogic.gdx.graphics.VertexAttributes com.badlogic.gdx.graphics.glutils.InstanceBufferObject.getAttributes()"""
        return 'graphics.VertexAttributes'.__wrap(super(InstanceBufferObject, self).getAttributes())

    @override
    @overload
    def getNumMaxInstances(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.InstanceBufferObject.getNumMaxInstances()"""
        return int.__wrap(super(InstanceBufferObject, self).getNumMaxInstances())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FrameBufferBuilder
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.glutils.GLFrameBuffer as __GLFrameBuffer_FrameBufferBuilder
__FrameBufferBuilder = __GLFrameBuffer_FrameBufferBuilder.FrameBufferBuilder
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.graphics.glutils.GLFrameBuffer as __GLFrameBuffer_GLFrameBufferBuilder
__GLFrameBufferBuilder = __GLFrameBuffer_GLFrameBufferBuilder.GLFrameBufferBuilder
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.graphics.glutils.FrameBuffer as __FrameBuffer
__FrameBuffer = __FrameBuffer
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class FrameBufferBuilder():
    """com.badlogic.gdx.graphics.glutils.GLFrameBuffer.FrameBufferBuilder"""
 
    @staticmethod
    def __wrap(java_value: __FrameBufferBuilder) -> 'FrameBufferBuilder':
        return FrameBufferBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FrameBufferBuilder):
        """
        Dynamic initializer for FrameBufferBuilder.
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
    def addFloatAttachment(self, arg0: int, arg1: int, arg2: int, arg3: bool) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addFloatAttachment(int,int,int,boolean)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addFloatAttachment(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def addStencilDepthPackedRenderBuffer(self, arg0: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addStencilDepthPackedRenderBuffer(int)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addStencilDepthPackedRenderBuffer(__int.valueOf(arg0)))

    @overload
    def addStencilRenderBuffer(self, arg0: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addStencilRenderBuffer(int)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addStencilRenderBuffer(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def addBasicDepthRenderBuffer(self) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicDepthRenderBuffer()"""
        return 'GLFrameBufferBuilder'.__wrap(super(GLFrameBufferBuilder, self).addBasicDepthRenderBuffer())

    @overload
    def addBasicColorTextureAttachment(self, arg0: 'Format') -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicColorTextureAttachment(com.badlogic.gdx.graphics.Pixmap$Format)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addBasicColorTextureAttachment(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def addStencilTextureAttachment(self, arg0: int, arg1: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addStencilTextureAttachment(int,int)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addStencilTextureAttachment(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def addBasicStencilDepthPackedRenderBuffer(self) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicStencilDepthPackedRenderBuffer()"""
        return 'GLFrameBufferBuilder'.__wrap(super(GLFrameBufferBuilder, self).addBasicStencilDepthPackedRenderBuffer())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FrameBufferBuilder(int,int)"""
        val = __FrameBufferBuilder(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def addColorTextureAttachment(self, arg0: int, arg1: int, arg2: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addColorTextureAttachment(int,int,int)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addColorTextureAttachment(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def addBasicStencilRenderBuffer(self) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicStencilRenderBuffer()"""
        return 'GLFrameBufferBuilder'.__wrap(super(GLFrameBufferBuilder, self).addBasicStencilRenderBuffer())

    @overload
    def addDepthTextureAttachment(self, arg0: int, arg1: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addDepthTextureAttachment(int,int)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addDepthTextureAttachment(__int.valueOf(arg0), __int.valueOf(arg1)))

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
    def addDepthRenderBuffer(self, arg0: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addDepthRenderBuffer(int)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addDepthRenderBuffer(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def build(self) -> 'FrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FrameBufferBuilder.build()"""
        return 'FrameBuffer'.__wrap(super(FrameBufferBuilder, self).build()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.ETC1
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.glutils.ETC1 as __ETC1
__ETC1 = __ETC1
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.glutils.ETC1 as __ETC1_ETC1Data
__ETC1Data = __ETC1_ETC1Data.ETC1Data
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Pixmap as __Pixmap
__Pixmap = __Pixmap
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class ETC1():
    """com.badlogic.gdx.graphics.glutils.ETC1"""
 
    @staticmethod
    def __wrap(java_value: __ETC1) -> 'ETC1':
        return ETC1(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ETC1):
        """
        Dynamic initializer for ETC1.
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
    def encodeImagePKM(arg0: 'Pixmap') -> 'ETC1Data':
        """public static com.badlogic.gdx.graphics.glutils.ETC1$ETC1Data com.badlogic.gdx.graphics.glutils.ETC1.encodeImagePKM(com.badlogic.gdx.graphics.Pixmap)"""
        return ETC1Data.__wrap(__ETC1.encodeImagePKM(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.glutils.ETC1()"""
        val = __ETC1()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def formatHeader(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int):
        """public static native void com.badlogic.gdx.graphics.glutils.ETC1.formatHeader(java.nio.ByteBuffer,int,int,int)"""
        __ETC1.formatHeader(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getCompressedDataSize(arg0: int, arg1: int) -> int:
        """public static native int com.badlogic.gdx.graphics.glutils.ETC1.getCompressedDataSize(int,int)"""
        return int.__wrap(__ETC1.getCompressedDataSize(__int.valueOf(arg0), __int.valueOf(arg1)))

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.glutils.ETC1()"""
        val = __ETC1()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def decodeImage(arg0: 'ETC1Data', arg1: 'Format') -> 'graphics.Pixmap':
        """public static com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.graphics.glutils.ETC1.decodeImage(com.badlogic.gdx.graphics.glutils.ETC1$ETC1Data,com.badlogic.gdx.graphics.Pixmap$Format)"""
        return graphics.Pixmap.__wrap(__ETC1.decodeImage(arg0, arg1))

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
    def encodeImage(arg0: 'Pixmap') -> 'ETC1Data':
        """public static com.badlogic.gdx.graphics.glutils.ETC1$ETC1Data com.badlogic.gdx.graphics.glutils.ETC1.encodeImage(com.badlogic.gdx.graphics.Pixmap)"""
        return ETC1Data.__wrap(__ETC1.encodeImage(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.FrameBufferCubemap
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import com.badlogic.gdx.graphics.glutils.FrameBufferCubemap as __FrameBufferCubemap
__FrameBufferCubemap = __FrameBufferCubemap
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.glutils.GLFrameBuffer as __GLFrameBuffer
__GLFrameBuffer = __GLFrameBuffer
import com.badlogic.gdx.graphics.GLTexture as __GLTexture
__GLTexture = __GLTexture
import java.lang.Long as __long
import java.lang.StringBuilder as __StringBuilder
__StringBuilder = __StringBuilder
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

import com.badlogic.gdx.graphics.Cubemap as __Cubemap_CubemapSide
__CubemapSide = __Cubemap_CubemapSide.CubemapSide
from builtins import int
 
class FrameBufferCubemap():
    """com.badlogic.gdx.graphics.glutils.FrameBufferCubemap"""
 
    @staticmethod
    def __wrap(java_value: __FrameBufferCubemap) -> 'FrameBufferCubemap':
        return FrameBufferCubemap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FrameBufferCubemap):
        """
        Dynamic initializer for FrameBufferCubemap.
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
    def bind(self):
        """public void com.badlogic.gdx.graphics.glutils.FrameBufferCubemap.bind()"""
        super(FrameBufferCubemap, self).bind()

    @override
    @overload
    def getDepthBufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getDepthBufferHandle()"""
        return int.__wrap(super(GLFrameBuffer, self).getDepthBufferHandle())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Format', arg1: int, arg2: int, arg3: bool, arg4: bool):
        """public com.badlogic.gdx.graphics.glutils.FrameBufferCubemap(com.badlogic.gdx.graphics.Pixmap$Format,int,int,boolean,boolean)"""
        val = __FrameBufferCubemap(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __boolean.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getColorBufferTexture(self) -> 'graphics.GLTexture':
        """public T com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getColorBufferTexture()"""
        return 'graphics.GLTexture'.__wrap(super(GLFrameBuffer, self).getColorBufferTexture())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getWidth()"""
        return int.__wrap(super(GLFrameBuffer, self).getWidth())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.begin()"""
        super(GLFrameBuffer, self).begin()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def clearAllFrameBuffers(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.clearAllFrameBuffers(com.badlogic.gdx.Application)"""
        __GLFrameBuffer.clearAllFrameBuffers(arg0)

    @override
    @overload
    def getTextureAttachments(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getTextureAttachments()"""
        return 'utils.Array'.__wrap(super(GLFrameBuffer, self).getTextureAttachments())

        @staticmethod
        @overload
        def unbind():
            """public static void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.unbind()"""
            __GLFrameBuffer.unbind()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getSide(self) -> 'graphics.Cubemap$CubemapSide':
        """public com.badlogic.gdx.graphics.Cubemap$CubemapSide com.badlogic.gdx.graphics.glutils.FrameBufferCubemap.getSide()"""
        return 'graphics.Cubemap$CubemapSide'.__wrap(super(FrameBufferCubemap, self).getSide())

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getHeight()"""
        return int.__wrap(super(GLFrameBuffer, self).getHeight())

    @override
    @overload
    def getFramebufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getFramebufferHandle()"""
        return int.__wrap(super(GLFrameBuffer, self).getFramebufferHandle())

    @staticmethod
    @overload
    def invalidateAllFrameBuffers(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.invalidateAllFrameBuffers(com.badlogic.gdx.Application)"""
        __GLFrameBuffer.invalidateAllFrameBuffers(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def nextSide(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FrameBufferCubemap.nextSide()"""
        return bool.__wrap(super(FrameBufferCubemap, self).nextSide())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def end(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.end(int,int,int,int)"""
        super(__GLFrameBuffer, self).end(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def getManagedStatus(arg0: 'StringBuilder') -> 'StringBuilder':
        """public static java.lang.StringBuilder com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getManagedStatus(java.lang.StringBuilder)"""
        return StringBuilder.__wrap(__GLFrameBuffer.getManagedStatus(arg0))

    @staticmethod
    @overload
    def getManagedStatus() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getManagedStatus()"""
        return str.__wrap(__GLFrameBuffer.getManagedStatus())

    @override
    @overload
    def getStencilBufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getStencilBufferHandle()"""
        return int.__wrap(super(GLFrameBuffer, self).getStencilBufferHandle())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.dispose()"""
        super(GLFrameBuffer, self).dispose()

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.end()"""
        super(GLFrameBuffer, self).end()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Format', arg1: int, arg2: int, arg3: bool):
        """public com.badlogic.gdx.graphics.glutils.FrameBufferCubemap(com.badlogic.gdx.graphics.Pixmap$Format,int,int,boolean)"""
        val = __FrameBufferCubemap(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.GLVersion$Type
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
import com.badlogic.gdx.graphics.glutils.GLVersion as __GLVersion_Type
__Type = __GLVersion_Type.Type
from builtins import int
 
class Type():
    """com.badlogic.gdx.graphics.glutils.GLVersion.Type"""
 
    @staticmethod
    def __wrap(java_value: __Type) -> 'Type':
        return Type(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Type):
        """
        Dynamic initializer for Type.
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Type':
        """public static com.badlogic.gdx.graphics.glutils.GLVersion$Type com.badlogic.gdx.graphics.glutils.GLVersion$Type.valueOf(java.lang.String)"""
        return Type.__wrap(__Type.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['Type']:
        """public static com.badlogic.gdx.graphics.glutils.GLVersion$Type[] com.badlogic.gdx.graphics.glutils.GLVersion$Type.values()"""
        return List[Type].__wrap(__Type.values()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.FloatTextureData
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.glutils.FloatTextureData as __FloatTextureData
__FloatTextureData = __FloatTextureData
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.TextureData as __TextureData_TextureDataType
__TextureDataType = __TextureData_TextureDataType.TextureDataType
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Pixmap as __Pixmap_Format
__Format = __Pixmap_Format.Format
import java.nio.FloatBuffer as __FloatBuffer
__FloatBuffer = __FloatBuffer
import com.badlogic.gdx.graphics.Pixmap as __Pixmap
__Pixmap = __Pixmap
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class FloatTextureData():
    """com.badlogic.gdx.graphics.glutils.FloatTextureData"""
 
    @staticmethod
    def __wrap(java_value: __FloatTextureData) -> 'FloatTextureData':
        return FloatTextureData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FloatTextureData):
        """
        Dynamic initializer for FloatTextureData.
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
    def isPrepared(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FloatTextureData.isPrepared()"""
        return bool.__wrap(super(FloatTextureData, self).isPrepared())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getType(self) -> 'graphics.TextureData$TextureDataType':
        """public com.badlogic.gdx.graphics.TextureData$TextureDataType com.badlogic.gdx.graphics.glutils.FloatTextureData.getType()"""
        return 'graphics.TextureData$TextureDataType'.__wrap(super(FloatTextureData, self).getType())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def useMipMaps(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FloatTextureData.useMipMaps()"""
        return bool.__wrap(super(FloatTextureData, self).useMipMaps())

    @override
    @overload
    def consumeCustomData(self, arg0: int):
        """public void com.badlogic.gdx.graphics.glutils.FloatTextureData.consumeCustomData(int)"""
        super(__FloatTextureData, self).consumeCustomData(__int.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def consumePixmap(self) -> 'graphics.Pixmap':
        """public com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.graphics.glutils.FloatTextureData.consumePixmap()"""
        return 'graphics.Pixmap'.__wrap(super(FloatTextureData, self).consumePixmap())

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.FloatTextureData.getWidth()"""
        return int.__wrap(super(FloatTextureData, self).getWidth())

    @override
    @overload
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FloatTextureData.isManaged()"""
        return bool.__wrap(super(FloatTextureData, self).isManaged())

    @override
    @overload
    def prepare(self):
        """public void com.badlogic.gdx.graphics.glutils.FloatTextureData.prepare()"""
        super(FloatTextureData, self).prepare()

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
    def disposePixmap(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FloatTextureData.disposePixmap()"""
        return bool.__wrap(super(FloatTextureData, self).disposePixmap())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool):
        """public com.badlogic.gdx.graphics.glutils.FloatTextureData(int,int,int,int,int,boolean)"""
        val = __FloatTextureData(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __boolean.valueOf(arg5))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getBuffer(self) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.FloatTextureData.getBuffer()"""
        return 'FloatBuffer'.__wrap(super(FloatTextureData, self).getBuffer())

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

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.FloatTextureData.getHeight()"""
        return int.__wrap(super(FloatTextureData, self).getHeight())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getFormat(self) -> 'graphics.Pixmap$Format':
        """public com.badlogic.gdx.graphics.Pixmap$Format com.badlogic.gdx.graphics.glutils.FloatTextureData.getFormat()"""
        return 'graphics.Pixmap$Format'.__wrap(super(FloatTextureData, self).getFormat()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.VertexBufferObject
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.nio.FloatBuffer as FloatBuffer
import com.badlogic.gdx.graphics.glutils.VertexBufferObject as __VertexBufferObject
__VertexBufferObject = __VertexBufferObject
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.VertexAttributes as __VertexAttributes
__VertexAttributes = __VertexAttributes
import java.nio.FloatBuffer as __FloatBuffer
__FloatBuffer = __FloatBuffer
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class VertexBufferObject():
    """com.badlogic.gdx.graphics.glutils.VertexBufferObject"""
 
    @staticmethod
    def __wrap(java_value: __VertexBufferObject) -> 'VertexBufferObject':
        return VertexBufferObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __VertexBufferObject):
        """
        Dynamic initializer for VertexBufferObject.
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
    def getBuffer(self, arg0: bool) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.VertexBufferObject.getBuffer(boolean)"""
        return 'FloatBuffer'.__wrap(super(__VertexBufferObject, self).getBuffer(__boolean.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: bool, arg1: int, arg2: 'VertexAttributes'):
        """public com.badlogic.gdx.graphics.glutils.VertexBufferObject(boolean,int,com.badlogic.gdx.graphics.VertexAttributes)"""
        val = __VertexBufferObject(__boolean.valueOf(arg0), __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def unbind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObject.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(__VertexBufferObject, self).unbind(arg0)

    @override
    @overload
    def unbind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObject.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        super(__VertexBufferObject, self).unbind(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: bool, arg1: int, *arg2: 'graphics.VertexAttribute'):
        """public com.badlogic.gdx.graphics.glutils.VertexBufferObject(boolean,int,com.badlogic.gdx.graphics.VertexAttribute...)"""
        val = __VertexBufferObject(__boolean.valueOf(arg0), __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def invalidate(self):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObject.invalidate()"""
        super(VertexBufferObject, self).invalidate()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObject.dispose()"""
        super(VertexBufferObject, self).dispose()

    @override
    @overload
    def getNumMaxVertices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.VertexBufferObject.getNumMaxVertices()"""
        return int.__wrap(super(VertexBufferObject, self).getNumMaxVertices())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def updateVertices(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObject.updateVertices(int,float[],int,int)"""
        super(__VertexBufferObject, self).updateVertices(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def getAttributes(self) -> 'graphics.VertexAttributes':
        """public com.badlogic.gdx.graphics.VertexAttributes com.badlogic.gdx.graphics.glutils.VertexBufferObject.getAttributes()"""
        return 'graphics.VertexAttributes'.__wrap(super(VertexBufferObject, self).getAttributes())

    @override
    @overload
    def setVertices(self, arg0: 'float', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObject.setVertices(float[],int,int)"""
        super(__VertexBufferObject, self).setVertices(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def getNumVertices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.VertexBufferObject.getNumVertices()"""
        return int.__wrap(super(VertexBufferObject, self).getNumVertices())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getBuffer(self) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.VertexBufferObject.getBuffer()"""
        return 'FloatBuffer'.__wrap(super(VertexBufferObject, self).getBuffer())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def bind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObject.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        super(__VertexBufferObject, self).bind(arg0, arg1)

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
    def bind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObject.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(__VertexBufferObject, self).bind(arg0) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.ShapeRenderer$ShapeType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.glutils.ShapeRenderer as __ShapeRenderer_ShapeType
__ShapeType = __ShapeRenderer_ShapeType.ShapeType
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
from builtins import int
 
class ShapeType():
    """com.badlogic.gdx.graphics.glutils.ShapeRenderer.ShapeType"""
 
    @staticmethod
    def __wrap(java_value: __ShapeType) -> 'ShapeType':
        return ShapeType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ShapeType):
        """
        Dynamic initializer for ShapeType.
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

    @overload
    def getGlType(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ShapeRenderer$ShapeType.getGlType()"""
        return int.__wrap(super(ShapeType, self).getGlType())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ShapeType':
        """public static com.badlogic.gdx.graphics.glutils.ShapeRenderer$ShapeType com.badlogic.gdx.graphics.glutils.ShapeRenderer$ShapeType.valueOf(java.lang.String)"""
        return ShapeType.__wrap(__ShapeType.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['ShapeType']:
        """public static com.badlogic.gdx.graphics.glutils.ShapeRenderer$ShapeType[] com.badlogic.gdx.graphics.glutils.ShapeRenderer$ShapeType.values()"""
        return List[ShapeType].__wrap(__ShapeType.values()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.graphics.glutils.GLFrameBuffer as __GLFrameBuffer_GLFrameBufferBuilder
__GLFrameBufferBuilder = __GLFrameBuffer_GLFrameBufferBuilder.GLFrameBufferBuilder
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class GLFrameBufferBuilder(ABC):
    """com.badlogic.gdx.graphics.glutils.GLFrameBuffer.GLFrameBufferBuilder"""
 
    @staticmethod
    def __wrap(java_value: __GLFrameBufferBuilder) -> 'GLFrameBufferBuilder':
        return GLFrameBufferBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFrameBufferBuilder):
        """
        Dynamic initializer for GLFrameBufferBuilder.
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
    def addFloatAttachment(self, arg0: int, arg1: int, arg2: int, arg3: bool) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addFloatAttachment(int,int,int,boolean)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addFloatAttachment(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def addBasicStencilDepthPackedRenderBuffer(self) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicStencilDepthPackedRenderBuffer()"""
        return 'GLFrameBufferBuilder'.__wrap(super(GLFrameBufferBuilder, self).addBasicStencilDepthPackedRenderBuffer())

    @overload
    def addStencilDepthPackedRenderBuffer(self, arg0: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addStencilDepthPackedRenderBuffer(int)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addStencilDepthPackedRenderBuffer(__int.valueOf(arg0)))

    @overload
    def addStencilRenderBuffer(self, arg0: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addStencilRenderBuffer(int)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addStencilRenderBuffer(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def addBasicStencilRenderBuffer(self) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicStencilRenderBuffer()"""
        return 'GLFrameBufferBuilder'.__wrap(super(GLFrameBufferBuilder, self).addBasicStencilRenderBuffer())

    @overload
    def addBasicColorTextureAttachment(self, arg0: 'Format') -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicColorTextureAttachment(com.badlogic.gdx.graphics.Pixmap$Format)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addBasicColorTextureAttachment(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def addBasicDepthRenderBuffer(self) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicDepthRenderBuffer()"""
        return 'GLFrameBufferBuilder'.__wrap(super(GLFrameBufferBuilder, self).addBasicDepthRenderBuffer())

    @overload
    def addStencilTextureAttachment(self, arg0: int, arg1: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addStencilTextureAttachment(int,int)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addStencilTextureAttachment(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder(int,int)"""
        val = __GLFrameBufferBuilder(__int.valueOf(arg0), __int.valueOf(arg1))
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

    @abstractmethod
    def build(self, ):
        """public abstract U com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.build()"""
        pass

    @overload
    def addColorTextureAttachment(self, arg0: int, arg1: int, arg2: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addColorTextureAttachment(int,int,int)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addColorTextureAttachment(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def addDepthTextureAttachment(self, arg0: int, arg1: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addDepthTextureAttachment(int,int)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addDepthTextureAttachment(__int.valueOf(arg0), __int.valueOf(arg1)))

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
    def addDepthRenderBuffer(self, arg0: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addDepthRenderBuffer(int)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addDepthRenderBuffer(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.MipMapTextureData
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.TextureData as __TextureData_TextureDataType
__TextureDataType = __TextureData_TextureDataType.TextureDataType
import com.badlogic.gdx.graphics.glutils.MipMapTextureData as __MipMapTextureData
__MipMapTextureData = __MipMapTextureData
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Pixmap as __Pixmap_Format
__Format = __Pixmap_Format.Format
import com.badlogic.gdx.graphics.Pixmap as __Pixmap
__Pixmap = __Pixmap
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class MipMapTextureData():
    """com.badlogic.gdx.graphics.glutils.MipMapTextureData"""
 
    @staticmethod
    def __wrap(java_value: __MipMapTextureData) -> 'MipMapTextureData':
        return MipMapTextureData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MipMapTextureData):
        """
        Dynamic initializer for MipMapTextureData.
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
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.MipMapTextureData.getHeight()"""
        return int.__wrap(super(MipMapTextureData, self).getHeight())

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.MipMapTextureData.getWidth()"""
        return int.__wrap(super(MipMapTextureData, self).getWidth())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getFormat(self) -> 'graphics.Pixmap$Format':
        """public com.badlogic.gdx.graphics.Pixmap$Format com.badlogic.gdx.graphics.glutils.MipMapTextureData.getFormat()"""
        return 'graphics.Pixmap$Format'.__wrap(super(MipMapTextureData, self).getFormat())

    @override
    @overload
    def useMipMaps(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.MipMapTextureData.useMipMaps()"""
        return bool.__wrap(super(MipMapTextureData, self).useMipMaps())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, *arg0: 'graphics.TextureData'):
        """public com.badlogic.gdx.graphics.glutils.MipMapTextureData(com.badlogic.gdx.graphics.TextureData...)"""
        val = __MipMapTextureData(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def disposePixmap(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.MipMapTextureData.disposePixmap()"""
        return bool.__wrap(super(MipMapTextureData, self).disposePixmap())

    @override
    @overload
    def consumeCustomData(self, arg0: int):
        """public void com.badlogic.gdx.graphics.glutils.MipMapTextureData.consumeCustomData(int)"""
        super(__MipMapTextureData, self).consumeCustomData(__int.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getType(self) -> 'graphics.TextureData$TextureDataType':
        """public com.badlogic.gdx.graphics.TextureData$TextureDataType com.badlogic.gdx.graphics.glutils.MipMapTextureData.getType()"""
        return 'graphics.TextureData$TextureDataType'.__wrap(super(MipMapTextureData, self).getType())

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
    def consumePixmap(self) -> 'graphics.Pixmap':
        """public com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.graphics.glutils.MipMapTextureData.consumePixmap()"""
        return 'graphics.Pixmap'.__wrap(super(MipMapTextureData, self).consumePixmap())

    @override
    @overload
    def isPrepared(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.MipMapTextureData.isPrepared()"""
        return bool.__wrap(super(MipMapTextureData, self).isPrepared())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.MipMapTextureData.isManaged()"""
        return bool.__wrap(super(MipMapTextureData, self).isManaged())

    @override
    @overload
    def prepare(self):
        """public void com.badlogic.gdx.graphics.glutils.MipMapTextureData.prepare()"""
        super(MipMapTextureData, self).prepare()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.HdpiUtils
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import com.badlogic.gdx.graphics.glutils.HdpiUtils as __HdpiUtils
__HdpiUtils = __HdpiUtils
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class HdpiUtils():
    """com.badlogic.gdx.graphics.glutils.HdpiUtils"""
 
    @staticmethod
    def __wrap(java_value: __HdpiUtils) -> 'HdpiUtils':
        return HdpiUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HdpiUtils):
        """
        Dynamic initializer for HdpiUtils.
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
    def toLogicalX(arg0: int) -> int:
        """public static int com.badlogic.gdx.graphics.glutils.HdpiUtils.toLogicalX(int)"""
        return int.__wrap(__HdpiUtils.toLogicalX(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def toBackBufferY(arg0: int) -> int:
        """public static int com.badlogic.gdx.graphics.glutils.HdpiUtils.toBackBufferY(int)"""
        return int.__wrap(__HdpiUtils.toBackBufferY(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def setMode(arg0: 'HdpiMode'):
        """public static void com.badlogic.gdx.graphics.glutils.HdpiUtils.setMode(com.badlogic.gdx.graphics.glutils.HdpiMode)"""
        __HdpiUtils.setMode(arg0)

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.glutils.HdpiUtils()"""
        val = __HdpiUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.glutils.HdpiUtils()"""
        val = __HdpiUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def glScissor(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static void com.badlogic.gdx.graphics.glutils.HdpiUtils.glScissor(int,int,int,int)"""
        __HdpiUtils.glScissor(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def toBackBufferX(arg0: int) -> int:
        """public static int com.badlogic.gdx.graphics.glutils.HdpiUtils.toBackBufferX(int)"""
        return int.__wrap(__HdpiUtils.toBackBufferX(__int.valueOf(arg0)))

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
    def toLogicalY(arg0: int) -> int:
        """public static int com.badlogic.gdx.graphics.glutils.HdpiUtils.toLogicalY(int)"""
        return int.__wrap(__HdpiUtils.toLogicalY(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def glViewport(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static void com.badlogic.gdx.graphics.glutils.HdpiUtils.glViewport(int,int,int,int)"""
        __HdpiUtils.glViewport(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FrameBufferRenderBufferAttachmentSpec
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
import com.badlogic.gdx.graphics.glutils.GLFrameBuffer as __GLFrameBuffer_FrameBufferRenderBufferAttachmentSpec
__FrameBufferRenderBufferAttachmentSpec = __GLFrameBuffer_FrameBufferRenderBufferAttachmentSpec.FrameBufferRenderBufferAttachmentSpec
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FrameBufferRenderBufferAttachmentSpec():
    """com.badlogic.gdx.graphics.glutils.GLFrameBuffer.FrameBufferRenderBufferAttachmentSpec"""
 
    @staticmethod
    def __wrap(java_value: __FrameBufferRenderBufferAttachmentSpec) -> 'FrameBufferRenderBufferAttachmentSpec':
        return FrameBufferRenderBufferAttachmentSpec(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FrameBufferRenderBufferAttachmentSpec):
        """
        Dynamic initializer for FrameBufferRenderBufferAttachmentSpec.
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

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FrameBufferRenderBufferAttachmentSpec(int)"""
        val = __FrameBufferRenderBufferAttachmentSpec(__int.valueOf(arg0))
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
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.IndexBufferObject
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.nio.ShortBuffer as __ShortBuffer
__ShortBuffer = __ShortBuffer
import java.lang.Object as __object
from builtins import type
import java.nio.ShortBuffer as ShortBuffer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.graphics.glutils.IndexBufferObject as __IndexBufferObject
__IndexBufferObject = __IndexBufferObject
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class IndexBufferObject():
    """com.badlogic.gdx.graphics.glutils.IndexBufferObject"""
 
    @staticmethod
    def __wrap(java_value: __IndexBufferObject) -> 'IndexBufferObject':
        return IndexBufferObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IndexBufferObject):
        """
        Dynamic initializer for IndexBufferObject.
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
    def getBuffer(self, arg0: bool) -> 'ShortBuffer':
        """public java.nio.ShortBuffer com.badlogic.gdx.graphics.glutils.IndexBufferObject.getBuffer(boolean)"""
        return 'ShortBuffer'.__wrap(super(__IndexBufferObject, self).getBuffer(__boolean.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def unbind(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObject.unbind()"""
        super(IndexBufferObject, self).unbind()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getNumIndices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.IndexBufferObject.getNumIndices()"""
        return int.__wrap(super(IndexBufferObject, self).getNumIndices())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObject.dispose()"""
        super(IndexBufferObject, self).dispose()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getBuffer(self) -> 'ShortBuffer':
        """public java.nio.ShortBuffer com.badlogic.gdx.graphics.glutils.IndexBufferObject.getBuffer()"""
        return 'ShortBuffer'.__wrap(super(IndexBufferObject, self).getBuffer())

    @overload
    def __init__(self, arg0: bool, arg1: int):
        """public com.badlogic.gdx.graphics.glutils.IndexBufferObject(boolean,int)"""
        val = __IndexBufferObject(__boolean.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.glutils.IndexBufferObject(int)"""
        val = __IndexBufferObject(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def setIndices(self, arg0: 'ShortBuffer'):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObject.setIndices(java.nio.ShortBuffer)"""
        super(__IndexBufferObject, self).setIndices(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def updateIndices(self, arg0: int, arg1: 'short', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObject.updateIndices(int,short[],int,int)"""
        super(__IndexBufferObject, self).updateIndices(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def setIndices(self, arg0: 'short', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObject.setIndices(short[],int,int)"""
        super(__IndexBufferObject, self).setIndices(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getNumMaxIndices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.IndexBufferObject.getNumMaxIndices()"""
        return int.__wrap(super(IndexBufferObject, self).getNumMaxIndices())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: bool, arg1: 'ByteBuffer'):
        """public com.badlogic.gdx.graphics.glutils.IndexBufferObject(boolean,java.nio.ByteBuffer)"""
        val = __IndexBufferObject(__boolean.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def bind(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObject.bind()"""
        super(IndexBufferObject, self).bind()

    @override
    @overload
    def invalidate(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObject.invalidate()"""
        super(IndexBufferObject, self).invalidate()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.FrameBuffer
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.glutils.GLFrameBuffer as __GLFrameBuffer
__GLFrameBuffer = __GLFrameBuffer
import com.badlogic.gdx.graphics.GLTexture as __GLTexture
__GLTexture = __GLTexture
import java.lang.Long as __long
import java.lang.StringBuilder as __StringBuilder
__StringBuilder = __StringBuilder
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
import com.badlogic.gdx.graphics.glutils.FrameBuffer as __FrameBuffer
__FrameBuffer = __FrameBuffer
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class FrameBuffer():
    """com.badlogic.gdx.graphics.glutils.FrameBuffer"""
 
    @staticmethod
    def __wrap(java_value: __FrameBuffer) -> 'FrameBuffer':
        return FrameBuffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FrameBuffer):
        """
        Dynamic initializer for FrameBuffer.
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
    def bind(self):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.bind()"""
        super(GLFrameBuffer, self).bind()

    @override
    @overload
    def getDepthBufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getDepthBufferHandle()"""
        return int.__wrap(super(GLFrameBuffer, self).getDepthBufferHandle())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getColorBufferTexture(self) -> 'graphics.GLTexture':
        """public T com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getColorBufferTexture()"""
        return 'graphics.GLTexture'.__wrap(super(GLFrameBuffer, self).getColorBufferTexture())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getWidth()"""
        return int.__wrap(super(GLFrameBuffer, self).getWidth())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Format', arg1: int, arg2: int, arg3: bool, arg4: bool):
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer(com.badlogic.gdx.graphics.Pixmap$Format,int,int,boolean,boolean)"""
        val = __FrameBuffer(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __boolean.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.begin()"""
        super(GLFrameBuffer, self).begin()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def clearAllFrameBuffers(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.clearAllFrameBuffers(com.badlogic.gdx.Application)"""
        __GLFrameBuffer.clearAllFrameBuffers(arg0)

    @override
    @overload
    def getTextureAttachments(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getTextureAttachments()"""
        return 'utils.Array'.__wrap(super(GLFrameBuffer, self).getTextureAttachments())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getHeight()"""
        return int.__wrap(super(GLFrameBuffer, self).getHeight())

    @override
    @overload
    def getFramebufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getFramebufferHandle()"""
        return int.__wrap(super(GLFrameBuffer, self).getFramebufferHandle())

    @staticmethod
    @overload
    def invalidateAllFrameBuffers(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.invalidateAllFrameBuffers(com.badlogic.gdx.Application)"""
        __GLFrameBuffer.invalidateAllFrameBuffers(arg0)

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
    def end(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.end(int,int,int,int)"""
        super(__GLFrameBuffer, self).end(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def getManagedStatus(arg0: 'StringBuilder') -> 'StringBuilder':
        """public static java.lang.StringBuilder com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getManagedStatus(java.lang.StringBuilder)"""
        return StringBuilder.__wrap(__GLFrameBuffer.getManagedStatus(arg0))

    @staticmethod
    @overload
    def getManagedStatus() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getManagedStatus()"""
        return str.__wrap(__GLFrameBuffer.getManagedStatus())

    @override
    @overload
    def getStencilBufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getStencilBufferHandle()"""
        return int.__wrap(super(GLFrameBuffer, self).getStencilBufferHandle())

    @overload
    def __init__(self, arg0: 'Format', arg1: int, arg2: int, arg3: bool):
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer(com.badlogic.gdx.graphics.Pixmap$Format,int,int,boolean)"""
        val = __FrameBuffer(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

        @staticmethod
        @overload
        def unbind():
            """public static void com.badlogic.gdx.graphics.glutils.FrameBuffer.unbind()"""
            __FrameBuffer.unbind()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.dispose()"""
        super(GLFrameBuffer, self).dispose()

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.end()"""
        super(GLFrameBuffer, self).end()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.ShapeRenderer
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer as __ImmediateModeRenderer
__ImmediateModeRenderer = __ImmediateModeRenderer
import com.badlogic.gdx.graphics.glutils.ShapeRenderer as __ShapeRenderer_ShapeType
__ShapeType = __ShapeRenderer_ShapeType.ShapeType
from builtins import float
import com.badlogic.gdx.math.Matrix4 as __Matrix4
__Matrix4 = __Matrix4
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
import com.badlogic.gdx.graphics.glutils.ShapeRenderer as __ShapeRenderer
__ShapeRenderer = __ShapeRenderer
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class ShapeRenderer():
    """com.badlogic.gdx.graphics.glutils.ShapeRenderer"""
 
    @staticmethod
    def __wrap(java_value: __ShapeRenderer) -> 'ShapeRenderer':
        return ShapeRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ShapeRenderer):
        """
        Dynamic initializer for ShapeRenderer.
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
    def rectLine(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.rectLine(float,float,float,float,float)"""
        super(__ShapeRenderer, self).rectLine(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: int):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.ellipse(float,float,float,float,int)"""
        super(__ShapeRenderer, self).ellipse(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4))

    @overload
    def rect(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: 'Color', arg6: 'Color', arg7: 'Color'):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.rect(float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeRenderer, self).rect(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4, arg5, arg6, arg7)

    @overload
    def rotate(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.rotate(float,float,float,float)"""
        super(__ShapeRenderer, self).rotate(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def polygon(self, arg0: 'float', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.polygon(float[],int,int)"""
        super(__ShapeRenderer, self).polygon(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def getCurrentType(self) -> 'ShapeType':
        """public com.badlogic.gdx.graphics.glutils.ShapeRenderer$ShapeType com.badlogic.gdx.graphics.glutils.ShapeRenderer.getCurrentType()"""
        return 'ShapeType'.__wrap(super(ShapeRenderer, self).getCurrentType())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def x(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.x(float,float,float)"""
        super(__ShapeRenderer, self).x(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def identity(self):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.identity()"""
        super(ShapeRenderer, self).identity()

    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.ellipse(float,float,float,float,float)"""
        super(__ShapeRenderer, self).ellipse(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.ellipse(float,float,float,float)"""
        super(__ShapeRenderer, self).ellipse(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def line(self, arg0: 'Vector2', arg1: 'Vector2'):
        """public final void com.badlogic.gdx.graphics.glutils.ShapeRenderer.line(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(__ShapeRenderer, self).line(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.ellipse(float,float,float,float,float,int)"""
        super(__ShapeRenderer, self).ellipse(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def point(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.point(float,float,float)"""
        super(__ShapeRenderer, self).point(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def set(self, arg0: 'ShapeType'):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.set(com.badlogic.gdx.graphics.glutils.ShapeRenderer$ShapeType)"""
        super(__ShapeRenderer, self).set(arg0)

    @overload
    def triangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.triangle(float,float,float,float,float,float)"""
        super(__ShapeRenderer, self).triangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5))

    @overload
    def rectLine(self, arg0: 'Vector2', arg1: 'Vector2', arg2: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.rectLine(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,float)"""
        super(__ShapeRenderer, self).rectLine(arg0, arg1, __float.valueOf(arg2))

    @overload
    def updateMatrices(self):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.updateMatrices()"""
        super(ShapeRenderer, self).updateMatrices()

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.glutils.ShapeRenderer.getColor()"""
        return 'graphics.Color'.__wrap(super(ShapeRenderer, self).getColor())

    @overload
    def polyline(self, arg0: 'float', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.polyline(float[],int,int)"""
        super(__ShapeRenderer, self).polyline(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public final void com.badlogic.gdx.graphics.glutils.ShapeRenderer.line(float,float,float,float,float,float)"""
        super(__ShapeRenderer, self).line(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5))

    @overload
    def cone(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.cone(float,float,float,float,float)"""
        super(__ShapeRenderer, self).cone(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def setTransformMatrix(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.setTransformMatrix(com.badlogic.gdx.math.Matrix4)"""
        super(__ShapeRenderer, self).setTransformMatrix(arg0)

    @overload
    def arc(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.arc(float,float,float,float,float)"""
        super(__ShapeRenderer, self).arc(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def line(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public final void com.badlogic.gdx.graphics.glutils.ShapeRenderer.line(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(__ShapeRenderer, self).line(arg0, arg1)

    @overload
    def rectLine(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'Color', arg6: 'Color'):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.rectLine(float,float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeRenderer, self).rectLine(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), arg5, arg6)

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public final void com.badlogic.gdx.graphics.glutils.ShapeRenderer.line(float,float,float,float)"""
        super(__ShapeRenderer, self).line(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def polygon(self, arg0: 'float'):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.polygon(float[])"""
        super(__ShapeRenderer, self).polygon(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def begin(self, arg0: 'ShapeType'):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.begin(com.badlogic.gdx.graphics.glutils.ShapeRenderer$ShapeType)"""
        super(__ShapeRenderer, self).begin(arg0)

    @overload
    def translate(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.translate(float,float,float)"""
        super(__ShapeRenderer, self).translate(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.end()"""
        super(ShapeRenderer, self).end()

    @overload
    def flush(self):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.flush()"""
        super(ShapeRenderer, self).flush()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.setColor(float,float,float,float)"""
        super(__ShapeRenderer, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'Color', arg7: 'Color'):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.line(float,float,float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeRenderer, self).line(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6, arg7)

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__ShapeRenderer, self).setColor(arg0)

    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.begin()"""
        super(ShapeRenderer, self).begin()

    @overload
    def isDrawing(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.ShapeRenderer.isDrawing()"""
        return bool.__wrap(super(ShapeRenderer, self).isDrawing())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.glutils.ShapeRenderer()"""
        val = __ShapeRenderer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def scale(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.scale(float,float,float)"""
        super(__ShapeRenderer, self).scale(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def arc(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.arc(float,float,float,float,float,int)"""
        super(__ShapeRenderer, self).arc(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5))

    @overload
    def rect(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.rect(float,float,float,float,float,float,float,float,float)"""
        super(__ShapeRenderer, self).rect(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.dispose()"""
        super(ShapeRenderer, self).dispose()

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: 'Color'):
        """public final void com.badlogic.gdx.graphics.glutils.ShapeRenderer.line(float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeRenderer, self).line(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4, arg5)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def triangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'Color', arg7: 'Color', arg8: 'Color'):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.triangle(float,float,float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeRenderer, self).triangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6, arg7, arg8)

    @overload
    def getTransformMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.glutils.ShapeRenderer.getTransformMatrix()"""
        return 'math.Matrix4'.__wrap(super(ShapeRenderer, self).getTransformMatrix())

    @overload
    def polyline(self, arg0: 'float'):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.polyline(float[])"""
        super(__ShapeRenderer, self).polyline(arg0)

    @overload
    def rect(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.rect(float,float,float,float)"""
        super(__ShapeRenderer, self).rect(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.glutils.ShapeRenderer(int)"""
        val = __ShapeRenderer(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def cone(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.cone(float,float,float,float,float,int)"""
        super(__ShapeRenderer, self).cone(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5))

    @overload
    def __init__(self, arg0: int, arg1: 'ShaderProgram'):
        """public com.badlogic.gdx.graphics.glutils.ShapeRenderer(int,com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        val = __ShapeRenderer(__int.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.glutils.ShapeRenderer()"""
        val = __ShapeRenderer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getProjectionMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.glutils.ShapeRenderer.getProjectionMatrix()"""
        return 'math.Matrix4'.__wrap(super(ShapeRenderer, self).getProjectionMatrix())

    @overload
    def circle(self, arg0: float, arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.circle(float,float,float,int)"""
        super(__ShapeRenderer, self).circle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def circle(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.circle(float,float,float)"""
        super(__ShapeRenderer, self).circle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def curve(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: int):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.curve(float,float,float,float,float,float,float,float,int)"""
        super(__ShapeRenderer, self).curve(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __int.valueOf(arg8))

    @overload
    def box(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.box(float,float,float,float,float,float)"""
        super(__ShapeRenderer, self).box(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5))

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
    def setProjectionMatrix(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.setProjectionMatrix(com.badlogic.gdx.math.Matrix4)"""
        super(__ShapeRenderer, self).setProjectionMatrix(arg0)

    @overload
    def getRenderer(self) -> 'ImmediateModeRenderer':
        """public com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer com.badlogic.gdx.graphics.glutils.ShapeRenderer.getRenderer()"""
        return 'ImmediateModeRenderer'.__wrap(super(ShapeRenderer, self).getRenderer())

    @overload
    def x(self, arg0: 'Vector2', arg1: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.x(com.badlogic.gdx.math.Vector2,float)"""
        super(__ShapeRenderer, self).x(arg0, __float.valueOf(arg1))

    @overload
    def setAutoShapeType(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.setAutoShapeType(boolean)"""
        super(__ShapeRenderer, self).setAutoShapeType(__boolean.valueOf(arg0))

    @overload
    def rect(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: 'Color', arg10: 'Color', arg11: 'Color', arg12: 'Color'):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.rect(float,float,float,float,float,float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeRenderer, self).rect(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), arg9, arg10, arg11, arg12) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO as __VertexBufferObjectWithVAO
__VertexBufferObjectWithVAO = __VertexBufferObjectWithVAO
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.VertexAttributes as __VertexAttributes
__VertexAttributes = __VertexAttributes
import java.nio.FloatBuffer as __FloatBuffer
__FloatBuffer = __FloatBuffer
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class VertexBufferObjectWithVAO():
    """com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO"""
 
    @staticmethod
    def __wrap(java_value: __VertexBufferObjectWithVAO) -> 'VertexBufferObjectWithVAO':
        return VertexBufferObjectWithVAO(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __VertexBufferObjectWithVAO):
        """
        Dynamic initializer for VertexBufferObjectWithVAO.
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
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO.dispose()"""
        super(VertexBufferObjectWithVAO, self).dispose()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getBuffer(self) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO.getBuffer()"""
        return 'FloatBuffer'.__wrap(super(VertexBufferObjectWithVAO, self).getBuffer())

    @override
    @overload
    def unbind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        super(__VertexBufferObjectWithVAO, self).unbind(arg0, arg1)

    @overload
    def __init__(self, arg0: bool, arg1: 'ByteBuffer', arg2: 'VertexAttributes'):
        """public com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO(boolean,java.nio.ByteBuffer,com.badlogic.gdx.graphics.VertexAttributes)"""
        val = __VertexBufferObjectWithVAO(__boolean.valueOf(arg0), arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def unbind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(__VertexBufferObjectWithVAO, self).unbind(arg0)

    @override
    @overload
    def updateVertices(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO.updateVertices(int,float[],int,int)"""
        super(__VertexBufferObjectWithVAO, self).updateVertices(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: bool, arg1: int, *arg2: 'graphics.VertexAttribute'):
        """public com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO(boolean,int,com.badlogic.gdx.graphics.VertexAttribute...)"""
        val = __VertexBufferObjectWithVAO(__boolean.valueOf(arg0), __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getNumMaxVertices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO.getNumMaxVertices()"""
        return int.__wrap(super(VertexBufferObjectWithVAO, self).getNumMaxVertices())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: bool, arg1: int, arg2: 'VertexAttributes'):
        """public com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO(boolean,int,com.badlogic.gdx.graphics.VertexAttributes)"""
        val = __VertexBufferObjectWithVAO(__boolean.valueOf(arg0), __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def bind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        super(__VertexBufferObjectWithVAO, self).bind(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def bind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(__VertexBufferObjectWithVAO, self).bind(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getNumVertices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO.getNumVertices()"""
        return int.__wrap(super(VertexBufferObjectWithVAO, self).getNumVertices())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def invalidate(self):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO.invalidate()"""
        super(VertexBufferObjectWithVAO, self).invalidate()

    @overload
    def getBuffer(self, arg0: bool) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO.getBuffer(boolean)"""
        return 'FloatBuffer'.__wrap(super(__VertexBufferObjectWithVAO, self).getBuffer(__boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setVertices(self, arg0: 'float', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO.setVertices(float[],int,int)"""
        super(__VertexBufferObjectWithVAO, self).setVertices(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def getAttributes(self) -> 'graphics.VertexAttributes':
        """public com.badlogic.gdx.graphics.VertexAttributes com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO.getAttributes()"""
        return 'graphics.VertexAttributes'.__wrap(super(VertexBufferObjectWithVAO, self).getAttributes()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData as __VertexBufferObjectSubData
__VertexBufferObjectSubData = __VertexBufferObjectSubData
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.VertexAttributes as __VertexAttributes
__VertexAttributes = __VertexAttributes
import java.nio.FloatBuffer as __FloatBuffer
__FloatBuffer = __FloatBuffer
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class VertexBufferObjectSubData():
    """com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData"""
 
    @staticmethod
    def __wrap(java_value: __VertexBufferObjectSubData) -> 'VertexBufferObjectSubData':
        return VertexBufferObjectSubData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __VertexBufferObjectSubData):
        """
        Dynamic initializer for VertexBufferObjectSubData.
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
    def bind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        super(__VertexBufferObjectSubData, self).bind(arg0, arg1)

    @overload
    def getBuffer(self, arg0: bool) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.getBuffer(boolean)"""
        return 'FloatBuffer'.__wrap(super(__VertexBufferObjectSubData, self).getBuffer(__boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def unbind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(__VertexBufferObjectSubData, self).unbind(arg0)

    @override
    @overload
    def updateVertices(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.updateVertices(int,float[],int,int)"""
        super(__VertexBufferObjectSubData, self).updateVertices(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def getNumVertices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.getNumVertices()"""
        return int.__wrap(super(VertexBufferObjectSubData, self).getNumVertices())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getNumMaxVertices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.getNumMaxVertices()"""
        return int.__wrap(super(VertexBufferObjectSubData, self).getNumMaxVertices())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getBufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.getBufferHandle()"""
        return int.__wrap(super(VertexBufferObjectSubData, self).getBufferHandle())

    @override
    @overload
    def invalidate(self):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.invalidate()"""
        super(VertexBufferObjectSubData, self).invalidate()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: bool, arg1: int, *arg2: 'graphics.VertexAttribute'):
        """public com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData(boolean,int,com.badlogic.gdx.graphics.VertexAttribute...)"""
        val = __VertexBufferObjectSubData(__boolean.valueOf(arg0), __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setVertices(self, arg0: 'float', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.setVertices(float[],int,int)"""
        super(__VertexBufferObjectSubData, self).setVertices(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getBuffer(self) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.getBuffer()"""
        return 'FloatBuffer'.__wrap(super(VertexBufferObjectSubData, self).getBuffer())

    @override
    @overload
    def unbind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        super(__VertexBufferObjectSubData, self).unbind(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.dispose()"""
        super(VertexBufferObjectSubData, self).dispose()

    @overload
    def __init__(self, arg0: bool, arg1: int, arg2: 'VertexAttributes'):
        """public com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData(boolean,int,com.badlogic.gdx.graphics.VertexAttributes)"""
        val = __VertexBufferObjectSubData(__boolean.valueOf(arg0), __int.valueOf(arg1), arg2)
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
    def bind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(__VertexBufferObjectSubData, self).bind(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getAttributes(self) -> 'graphics.VertexAttributes':
        """public com.badlogic.gdx.graphics.VertexAttributes com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.getAttributes()"""
        return 'graphics.VertexAttributes'.__wrap(super(VertexBufferObjectSubData, self).getAttributes()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.FloatFrameBuffer
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.glutils.GLFrameBuffer as __GLFrameBuffer
__GLFrameBuffer = __GLFrameBuffer
import com.badlogic.gdx.graphics.GLTexture as __GLTexture
__GLTexture = __GLTexture
import java.lang.Long as __long
import com.badlogic.gdx.graphics.glutils.FloatFrameBuffer as __FloatFrameBuffer
__FloatFrameBuffer = __FloatFrameBuffer
import java.lang.StringBuilder as __StringBuilder
__StringBuilder = __StringBuilder
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
import com.badlogic.gdx.graphics.glutils.FrameBuffer as __FrameBuffer
__FrameBuffer = __FrameBuffer
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class FloatFrameBuffer():
    """com.badlogic.gdx.graphics.glutils.FloatFrameBuffer"""
 
    @staticmethod
    def __wrap(java_value: __FloatFrameBuffer) -> 'FloatFrameBuffer':
        return FloatFrameBuffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FloatFrameBuffer):
        """
        Dynamic initializer for FloatFrameBuffer.
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
    def bind(self):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.bind()"""
        super(GLFrameBuffer, self).bind()

    @override
    @overload
    def getDepthBufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getDepthBufferHandle()"""
        return int.__wrap(super(GLFrameBuffer, self).getDepthBufferHandle())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: bool):
        """public com.badlogic.gdx.graphics.glutils.FloatFrameBuffer(int,int,boolean)"""
        val = __FloatFrameBuffer(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getColorBufferTexture(self) -> 'graphics.GLTexture':
        """public T com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getColorBufferTexture()"""
        return 'graphics.GLTexture'.__wrap(super(GLFrameBuffer, self).getColorBufferTexture())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getWidth()"""
        return int.__wrap(super(GLFrameBuffer, self).getWidth())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.begin()"""
        super(GLFrameBuffer, self).begin()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def clearAllFrameBuffers(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.clearAllFrameBuffers(com.badlogic.gdx.Application)"""
        __GLFrameBuffer.clearAllFrameBuffers(arg0)

    @override
    @overload
    def getTextureAttachments(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getTextureAttachments()"""
        return 'utils.Array'.__wrap(super(GLFrameBuffer, self).getTextureAttachments())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getHeight()"""
        return int.__wrap(super(GLFrameBuffer, self).getHeight())

    @override
    @overload
    def getFramebufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getFramebufferHandle()"""
        return int.__wrap(super(GLFrameBuffer, self).getFramebufferHandle())

    @staticmethod
    @overload
    def invalidateAllFrameBuffers(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.invalidateAllFrameBuffers(com.badlogic.gdx.Application)"""
        __GLFrameBuffer.invalidateAllFrameBuffers(arg0)

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
    def end(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.end(int,int,int,int)"""
        super(__GLFrameBuffer, self).end(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def getManagedStatus(arg0: 'StringBuilder') -> 'StringBuilder':
        """public static java.lang.StringBuilder com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getManagedStatus(java.lang.StringBuilder)"""
        return StringBuilder.__wrap(__GLFrameBuffer.getManagedStatus(arg0))

    @staticmethod
    @overload
    def getManagedStatus() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getManagedStatus()"""
        return str.__wrap(__GLFrameBuffer.getManagedStatus())

    @override
    @overload
    def getStencilBufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getStencilBufferHandle()"""
        return int.__wrap(super(GLFrameBuffer, self).getStencilBufferHandle())

        @staticmethod
        @overload
        def unbind():
            """public static void com.badlogic.gdx.graphics.glutils.FrameBuffer.unbind()"""
            __FrameBuffer.unbind()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.dispose()"""
        super(GLFrameBuffer, self).dispose()

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.end()"""
        super(GLFrameBuffer, self).end()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.VertexAttributes as __VertexAttributes
__VertexAttributes = __VertexAttributes
import java.nio.FloatBuffer as __FloatBuffer
__FloatBuffer = __FloatBuffer
import com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData as __InstanceBufferObjectSubData
__InstanceBufferObjectSubData = __InstanceBufferObjectSubData
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class InstanceBufferObjectSubData():
    """com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData"""
 
    @staticmethod
    def __wrap(java_value: __InstanceBufferObjectSubData) -> 'InstanceBufferObjectSubData':
        return InstanceBufferObjectSubData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InstanceBufferObjectSubData):
        """
        Dynamic initializer for InstanceBufferObjectSubData.
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
    def __init__(self, arg0: bool, arg1: int, arg2: 'VertexAttributes'):
        """public com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData(boolean,int,com.badlogic.gdx.graphics.VertexAttributes)"""
        val = __InstanceBufferObjectSubData(__boolean.valueOf(arg0), __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getBuffer(self) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.getBuffer()"""
        return 'FloatBuffer'.__wrap(super(InstanceBufferObjectSubData, self).getBuffer())

    @override
    @overload
    def setInstanceData(self, arg0: 'FloatBuffer', arg1: int):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.setInstanceData(java.nio.FloatBuffer,int)"""
        super(__InstanceBufferObjectSubData, self).setInstanceData(arg0, __int.valueOf(arg1))

    @override
    @overload
    def setInstanceData(self, arg0: 'float', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.setInstanceData(float[],int,int)"""
        super(__InstanceBufferObjectSubData, self).setInstanceData(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def getBufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.getBufferHandle()"""
        return int.__wrap(super(InstanceBufferObjectSubData, self).getBufferHandle())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getBuffer(self, arg0: bool) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.getBuffer(boolean)"""
        return 'FloatBuffer'.__wrap(super(__InstanceBufferObjectSubData, self).getBuffer(__boolean.valueOf(arg0)))

    @override
    @overload
    def updateInstanceData(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.updateInstanceData(int,float[],int,int)"""
        super(__InstanceBufferObjectSubData, self).updateInstanceData(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def unbind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(__InstanceBufferObjectSubData, self).unbind(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getAttributes(self) -> 'graphics.VertexAttributes':
        """public com.badlogic.gdx.graphics.VertexAttributes com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.getAttributes()"""
        return 'graphics.VertexAttributes'.__wrap(super(InstanceBufferObjectSubData, self).getAttributes())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def invalidate(self):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.invalidate()"""
        super(InstanceBufferObjectSubData, self).invalidate()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: bool, arg1: int, *arg2: 'graphics.VertexAttribute'):
        """public com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData(boolean,int,com.badlogic.gdx.graphics.VertexAttribute...)"""
        val = __InstanceBufferObjectSubData(__boolean.valueOf(arg0), __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getNumMaxInstances(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.getNumMaxInstances()"""
        return int.__wrap(super(InstanceBufferObjectSubData, self).getNumMaxInstances())

    @override
    @overload
    def bind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(__InstanceBufferObjectSubData, self).bind(arg0)

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
    def unbind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        super(__InstanceBufferObjectSubData, self).unbind(arg0, arg1)

    @override
    @overload
    def updateInstanceData(self, arg0: int, arg1: 'FloatBuffer', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.updateInstanceData(int,java.nio.FloatBuffer,int,int)"""
        super(__InstanceBufferObjectSubData, self).updateInstanceData(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def bind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        super(__InstanceBufferObjectSubData, self).bind(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.dispose()"""
        super(InstanceBufferObjectSubData, self).dispose()

    @override
    @overload
    def getNumInstances(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.getNumInstances()"""
        return int.__wrap(super(InstanceBufferObjectSubData, self).getNumInstances()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.HdpiMode
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.graphics.glutils.HdpiMode as __HdpiMode
__HdpiMode = __HdpiMode
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
from builtins import int
 
class HdpiMode():
    """com.badlogic.gdx.graphics.glutils.HdpiMode"""
 
    @staticmethod
    def __wrap(java_value: __HdpiMode) -> 'HdpiMode':
        return HdpiMode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HdpiMode):
        """
        Dynamic initializer for HdpiMode.
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'HdpiMode':
        """public static com.badlogic.gdx.graphics.glutils.HdpiMode com.badlogic.gdx.graphics.glutils.HdpiMode.valueOf(java.lang.String)"""
        return HdpiMode.__wrap(__HdpiMode.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['HdpiMode']:
        """public static com.badlogic.gdx.graphics.glutils.HdpiMode[] com.badlogic.gdx.graphics.glutils.HdpiMode.values()"""
        return List[HdpiMode].__wrap(__HdpiMode.values()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FrameBufferTextureAttachmentSpec
import com.badlogic.gdx.graphics.glutils.GLFrameBuffer as __GLFrameBuffer_FrameBufferTextureAttachmentSpec
__FrameBufferTextureAttachmentSpec = __GLFrameBuffer_FrameBufferTextureAttachmentSpec.FrameBufferTextureAttachmentSpec
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
 
class FrameBufferTextureAttachmentSpec():
    """com.badlogic.gdx.graphics.glutils.GLFrameBuffer.FrameBufferTextureAttachmentSpec"""
 
    @staticmethod
    def __wrap(java_value: __FrameBufferTextureAttachmentSpec) -> 'FrameBufferTextureAttachmentSpec':
        return FrameBufferTextureAttachmentSpec(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FrameBufferTextureAttachmentSpec):
        """
        Dynamic initializer for FrameBufferTextureAttachmentSpec.
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
    def isColorTexture(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FrameBufferTextureAttachmentSpec.isColorTexture()"""
        return bool.__wrap(super(FrameBufferTextureAttachmentSpec, self).isColorTexture())

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
    def __init__(self, arg0: int, arg1: int, arg2: int):
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FrameBufferTextureAttachmentSpec(int,int,int)"""
        val = __FrameBufferTextureAttachmentSpec(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))
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
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.GLFrameBuffer
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.glutils.GLFrameBuffer as __GLFrameBuffer
__GLFrameBuffer = __GLFrameBuffer
import com.badlogic.gdx.graphics.GLTexture as __GLTexture
__GLTexture = __GLTexture
import java.lang.Long as __long
import java.lang.StringBuilder as __StringBuilder
__StringBuilder = __StringBuilder
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class GLFrameBuffer(ABC):
    """com.badlogic.gdx.graphics.glutils.GLFrameBuffer"""
 
    @staticmethod
    def __wrap(java_value: __GLFrameBuffer) -> 'GLFrameBuffer':
        return GLFrameBuffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFrameBuffer):
        """
        Dynamic initializer for GLFrameBuffer.
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
    def bind(self):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.bind()"""
        super(GLFrameBuffer, self).bind()

    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getWidth()"""
        return int.__wrap(super(GLFrameBuffer, self).getWidth())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getHeight()"""
        return int.__wrap(super(GLFrameBuffer, self).getHeight())

    @overload
    def getTextureAttachments(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getTextureAttachments()"""
        return 'utils.Array'.__wrap(super(GLFrameBuffer, self).getTextureAttachments())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getFramebufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getFramebufferHandle()"""
        return int.__wrap(super(GLFrameBuffer, self).getFramebufferHandle())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getDepthBufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getDepthBufferHandle()"""
        return int.__wrap(super(GLFrameBuffer, self).getDepthBufferHandle())

    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.begin()"""
        super(GLFrameBuffer, self).begin()

    @overload
    def getStencilBufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getStencilBufferHandle()"""
        return int.__wrap(super(GLFrameBuffer, self).getStencilBufferHandle())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def clearAllFrameBuffers(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.clearAllFrameBuffers(com.badlogic.gdx.Application)"""
        __GLFrameBuffer.clearAllFrameBuffers(arg0)

    @overload
    def end(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.end(int,int,int,int)"""
        super(__GLFrameBuffer, self).end(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

        @staticmethod
        @overload
        def unbind():
            """public static void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.unbind()"""
            __GLFrameBuffer.unbind()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def invalidateAllFrameBuffers(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.invalidateAllFrameBuffers(com.badlogic.gdx.Application)"""
        __GLFrameBuffer.invalidateAllFrameBuffers(arg0)

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.end()"""
        super(GLFrameBuffer, self).end()

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
    def getManagedStatus(arg0: 'StringBuilder') -> 'StringBuilder':
        """public static java.lang.StringBuilder com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getManagedStatus(java.lang.StringBuilder)"""
        return StringBuilder.__wrap(__GLFrameBuffer.getManagedStatus(arg0))

    @staticmethod
    @overload
    def getManagedStatus() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getManagedStatus()"""
        return str.__wrap(__GLFrameBuffer.getManagedStatus())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.dispose()"""
        super(GLFrameBuffer, self).dispose()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getColorBufferTexture(self) -> 'graphics.GLTexture':
        """public T com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getColorBufferTexture()"""
        return 'graphics.GLTexture'.__wrap(super(GLFrameBuffer, self).getColorBufferTexture()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.CustomTexture3DData
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import com.badlogic.gdx.graphics.glutils.CustomTexture3DData as __CustomTexture3DData
__CustomTexture3DData = __CustomTexture3DData
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CustomTexture3DData():
    """com.badlogic.gdx.graphics.glutils.CustomTexture3DData"""
 
    @staticmethod
    def __wrap(java_value: __CustomTexture3DData) -> 'CustomTexture3DData':
        return CustomTexture3DData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CustomTexture3DData):
        """
        Dynamic initializer for CustomTexture3DData.
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
    def getGLType(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.CustomTexture3DData.getGLType()"""
        return int.__wrap(super(CustomTexture3DData, self).getGLType())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getPixels(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.graphics.glutils.CustomTexture3DData.getPixels()"""
        return 'ByteBuffer'.__wrap(super(CustomTexture3DData, self).getPixels())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.CustomTexture3DData.getHeight()"""
        return int.__wrap(super(CustomTexture3DData, self).getHeight())

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
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.CustomTexture3DData.isManaged()"""
        return bool.__wrap(super(CustomTexture3DData, self).isManaged())

    @override
    @overload
    def getDepth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.CustomTexture3DData.getDepth()"""
        return int.__wrap(super(CustomTexture3DData, self).getDepth())

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
    def getInternalFormat(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.CustomTexture3DData.getInternalFormat()"""
        return int.__wrap(super(CustomTexture3DData, self).getInternalFormat())

    @overload
    def getMipMapLevel(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.CustomTexture3DData.getMipMapLevel()"""
        return int.__wrap(super(CustomTexture3DData, self).getMipMapLevel())

    @override
    @overload
    def isPrepared(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.CustomTexture3DData.isPrepared()"""
        return bool.__wrap(super(CustomTexture3DData, self).isPrepared())

    @overload
    def getGLFormat(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.CustomTexture3DData.getGLFormat()"""
        return int.__wrap(super(CustomTexture3DData, self).getGLFormat())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public com.badlogic.gdx.graphics.glutils.CustomTexture3DData(int,int,int,int,int,int,int)"""
        val = __CustomTexture3DData(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def prepare(self):
        """public void com.badlogic.gdx.graphics.glutils.CustomTexture3DData.prepare()"""
        super(CustomTexture3DData, self).prepare()

    @override
    @overload
    def useMipMaps(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.CustomTexture3DData.useMipMaps()"""
        return bool.__wrap(super(CustomTexture3DData, self).useMipMaps())

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.CustomTexture3DData.getWidth()"""
        return int.__wrap(super(CustomTexture3DData, self).getWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def consume3DData(self):
        """public void com.badlogic.gdx.graphics.glutils.CustomTexture3DData.consume3DData()"""
        super(CustomTexture3DData, self).consume3DData() 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FloatFrameBufferBuilder
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.glutils.GLFrameBuffer as __GLFrameBuffer_FloatFrameBufferBuilder
__FloatFrameBufferBuilder = __GLFrameBuffer_FloatFrameBufferBuilder.FloatFrameBufferBuilder
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import com.badlogic.gdx.graphics.glutils.FloatFrameBuffer as __FloatFrameBuffer
__FloatFrameBuffer = __FloatFrameBuffer
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.graphics.glutils.GLFrameBuffer as __GLFrameBuffer_GLFrameBufferBuilder
__GLFrameBufferBuilder = __GLFrameBuffer_GLFrameBufferBuilder.GLFrameBufferBuilder
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class FloatFrameBufferBuilder():
    """com.badlogic.gdx.graphics.glutils.GLFrameBuffer.FloatFrameBufferBuilder"""
 
    @staticmethod
    def __wrap(java_value: __FloatFrameBufferBuilder) -> 'FloatFrameBufferBuilder':
        return FloatFrameBufferBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FloatFrameBufferBuilder):
        """
        Dynamic initializer for FloatFrameBufferBuilder.
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
    def addFloatAttachment(self, arg0: int, arg1: int, arg2: int, arg3: bool) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addFloatAttachment(int,int,int,boolean)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addFloatAttachment(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def addStencilDepthPackedRenderBuffer(self, arg0: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addStencilDepthPackedRenderBuffer(int)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addStencilDepthPackedRenderBuffer(__int.valueOf(arg0)))

    @overload
    def addStencilRenderBuffer(self, arg0: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addStencilRenderBuffer(int)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addStencilRenderBuffer(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def addBasicDepthRenderBuffer(self) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicDepthRenderBuffer()"""
        return 'GLFrameBufferBuilder'.__wrap(super(GLFrameBufferBuilder, self).addBasicDepthRenderBuffer())

    @overload
    def addBasicColorTextureAttachment(self, arg0: 'Format') -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicColorTextureAttachment(com.badlogic.gdx.graphics.Pixmap$Format)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addBasicColorTextureAttachment(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def addStencilTextureAttachment(self, arg0: int, arg1: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addStencilTextureAttachment(int,int)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addStencilTextureAttachment(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def addBasicStencilDepthPackedRenderBuffer(self) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicStencilDepthPackedRenderBuffer()"""
        return 'GLFrameBufferBuilder'.__wrap(super(GLFrameBufferBuilder, self).addBasicStencilDepthPackedRenderBuffer())

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
    def addColorTextureAttachment(self, arg0: int, arg1: int, arg2: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addColorTextureAttachment(int,int,int)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addColorTextureAttachment(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def addBasicStencilRenderBuffer(self) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicStencilRenderBuffer()"""
        return 'GLFrameBufferBuilder'.__wrap(super(GLFrameBufferBuilder, self).addBasicStencilRenderBuffer())

    @overload
    def addDepthTextureAttachment(self, arg0: int, arg1: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addDepthTextureAttachment(int,int)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addDepthTextureAttachment(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FloatFrameBufferBuilder(int,int)"""
        val = __FloatFrameBufferBuilder(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def addDepthRenderBuffer(self, arg0: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addDepthRenderBuffer(int)"""
        return 'GLFrameBufferBuilder'.__wrap(super(__GLFrameBufferBuilder, self).addDepthRenderBuffer(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def build(self) -> 'FloatFrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FloatFrameBuffer com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FloatFrameBufferBuilder.build()"""
        return 'FloatFrameBuffer'.__wrap(super(FloatFrameBufferBuilder, self).build()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.IndexData
from abc import abstractmethod, ABC
import java.nio.ShortBuffer as ShortBuffer
import com.badlogic.gdx.graphics.glutils.IndexData as __IndexData
__IndexData = __IndexData
from builtins import int
 
class IndexData(ABC):
    """com.badlogic.gdx.graphics.glutils.IndexData"""
 
    @staticmethod
    def __wrap(java_value: __IndexData) -> 'IndexData':
        return IndexData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IndexData):
        """
        Dynamic initializer for IndexData.
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
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.graphics.glutils.IndexData.dispose()"""
        pass

    @abstractmethod
    def unbind(self, ):
        """public abstract void com.badlogic.gdx.graphics.glutils.IndexData.unbind()"""
        pass

    @abstractmethod
    def getBuffer(self, arg0: bool):
        """public abstract java.nio.ShortBuffer com.badlogic.gdx.graphics.glutils.IndexData.getBuffer(boolean)"""
        pass

    @abstractmethod
    def bind(self, ):
        """public abstract void com.badlogic.gdx.graphics.glutils.IndexData.bind()"""
        pass

    @abstractmethod
    def invalidate(self, ):
        """public abstract void com.badlogic.gdx.graphics.glutils.IndexData.invalidate()"""
        pass

    @abstractmethod
    def getNumIndices(self, ):
        """public abstract int com.badlogic.gdx.graphics.glutils.IndexData.getNumIndices()"""
        pass

    @abstractmethod
    def setIndices(self, arg0: 'ShortBuffer'):
        """public abstract void com.badlogic.gdx.graphics.glutils.IndexData.setIndices(java.nio.ShortBuffer)"""
        pass

    @abstractmethod
    def updateIndices(self, arg0: int, arg1: 'short', arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.glutils.IndexData.updateIndices(int,short[],int,int)"""
        pass

    @abstractmethod
    def getBuffer(self, ):
        """public abstract java.nio.ShortBuffer com.badlogic.gdx.graphics.glutils.IndexData.getBuffer()"""
        pass

    @abstractmethod
    def setIndices(self, arg0: 'short', arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.glutils.IndexData.setIndices(short[],int,int)"""
        pass

    @abstractmethod
    def getNumMaxIndices(self, ):
        """public abstract int com.badlogic.gdx.graphics.glutils.IndexData.getNumMaxIndices()"""
        pass