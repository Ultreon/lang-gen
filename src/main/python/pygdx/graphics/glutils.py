from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.glutils.ShaderProgram as _ShaderProgram
_ShaderProgram = _ShaderProgram
from builtins import float
import java.lang.String as _String
_String = _String
import java.nio.FloatBuffer as FloatBuffer
from typing import List
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.nio.Buffer as Buffer
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ShaderProgram():
    """com.badlogic.gdx.graphics.glutils.ShaderProgram"""
 
    @staticmethod
    def _wrap(java_value: _ShaderProgram) -> 'ShaderProgram':
        return ShaderProgram(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShaderProgram):
        """
        Dynamic initializer for ShaderProgram.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShaderProgram__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShaderProgram__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getUniforms(self) -> List[str]:
        """public java.lang.String[] com.badlogic.gdx.graphics.glutils.ShaderProgram.getUniforms()"""
        return List[str]._wrap(super(ShaderProgram, self).getUniforms())

    @overload
    def setUniformf(self, arg0: int, arg1: 'Vector2'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(int,com.badlogic.gdx.math.Vector2)"""
        super(_ShaderProgram, self).setUniformf(_int.valueOf(arg0), arg1)

    @overload
    def setUniformMatrix(self, arg0: str, arg1: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix(java.lang.String,com.badlogic.gdx.math.Matrix4)"""
        super(_ShaderProgram, self).setUniformMatrix(arg0, arg1)

    @overload
    def setUniformi(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformi(int,int,int,int)"""
        super(_ShaderProgram, self).setUniformi(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def setUniformf(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(int,float)"""
        super(_ShaderProgram, self).setUniformf(_int.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def fetchUniformLocation(self, arg0: str, arg1: bool) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ShaderProgram.fetchUniformLocation(java.lang.String,boolean)"""
        return int._wrap(super(_ShaderProgram, self).fetchUniformLocation(arg0, _boolean.valueOf(arg1)))

    @overload
    def setUniform1fv(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniform1fv(int,float[],int,int)"""
        super(_ShaderProgram, self).setUniform1fv(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def getUniformType(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ShaderProgram.getUniformType(java.lang.String)"""
        return int._wrap(super(_ShaderProgram, self).getUniformType(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setUniform4fv(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniform4fv(int,float[],int,int)"""
        super(_ShaderProgram, self).setUniform4fv(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def clearAllShaderPrograms(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.glutils.ShaderProgram.clearAllShaderPrograms(com.badlogic.gdx.Application)"""
        _ShaderProgram.clearAllShaderPrograms(arg0)

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram(java.lang.String,java.lang.String)"""
        val = _ShaderProgram(arg0, arg1)
        self.__wrapper = val

    @overload
    def setUniformf(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(int,float,float,float,float)"""
        super(_ShaderProgram, self).setUniformf(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def disableVertexAttribute(self, arg0: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.disableVertexAttribute(int)"""
        super(_ShaderProgram, self).disableVertexAttribute(_int.valueOf(arg0))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.dispose()"""
        super(ShaderProgram, self).dispose()

    @overload
    def setUniformi(self, arg0: str, arg1: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformi(java.lang.String,int)"""
        super(_ShaderProgram, self).setUniformi(arg0, _int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def enableVertexAttribute(self, arg0: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.enableVertexAttribute(int)"""
        super(_ShaderProgram, self).enableVertexAttribute(_int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setUniformf(self, arg0: str, arg1: 'Vector3'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(java.lang.String,com.badlogic.gdx.math.Vector3)"""
        super(_ShaderProgram, self).setUniformf(arg0, arg1)

    @overload
    def setVertexAttribute(self, arg0: str, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'Buffer'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setVertexAttribute(java.lang.String,int,int,boolean,int,java.nio.Buffer)"""
        super(_ShaderProgram, self).setVertexAttribute(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), arg5)

    @overload
    def setUniformMatrix(self, arg0: str, arg1: 'Matrix4', arg2: bool):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix(java.lang.String,com.badlogic.gdx.math.Matrix4,boolean)"""
        super(_ShaderProgram, self).setUniformMatrix(arg0, arg1, _boolean.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setUniformi(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformi(int,int,int,int,int)"""
        super(_ShaderProgram, self).setUniformi(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle'):
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        val = _ShaderProgram(arg0, arg1)
        self.__wrapper = val

    @overload
    def setUniform1fv(self, arg0: str, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniform1fv(java.lang.String,float[],int,int)"""
        super(_ShaderProgram, self).setUniform1fv(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def getUniformSize(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ShaderProgram.getUniformSize(java.lang.String)"""
        return int._wrap(super(_ShaderProgram, self).getUniformSize(arg0))

    @overload
    def setUniformi(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformi(int,int)"""
        super(_ShaderProgram, self).setUniformi(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setVertexAttribute(self, arg0: str, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setVertexAttribute(java.lang.String,int,int,boolean,int,int)"""
        super(_ShaderProgram, self).setVertexAttribute(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @overload
    def setUniformf(self, arg0: str, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(java.lang.String,float,float)"""
        super(_ShaderProgram, self).setUniformf(arg0, _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def setUniformf(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(int,float,float)"""
        super(_ShaderProgram, self).setUniformf(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def isCompiled(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.ShaderProgram.isCompiled()"""
        return bool._wrap(super(ShaderProgram, self).isCompiled())

    @overload
    def setUniformMatrix(self, arg0: str, arg1: 'Matrix3', arg2: bool):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix(java.lang.String,com.badlogic.gdx.math.Matrix3,boolean)"""
        super(_ShaderProgram, self).setUniformMatrix(arg0, arg1, _boolean.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ShaderProgram.getHandle()"""
        return int._wrap(super(ShaderProgram, self).getHandle())

    @overload
    def getAttributeLocation(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ShaderProgram.getAttributeLocation(java.lang.String)"""
        return int._wrap(super(_ShaderProgram, self).getAttributeLocation(arg0))

    @overload
    def setUniformf(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(int,float,float,float)"""
        super(_ShaderProgram, self).setUniformf(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def setUniformMatrix4fv(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix4fv(int,float[],int,int)"""
        super(_ShaderProgram, self).setUniformMatrix4fv(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def setAttributef(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setAttributef(java.lang.String,float,float,float,float)"""
        super(_ShaderProgram, self).setAttributef(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def setUniform3fv(self, arg0: str, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniform3fv(java.lang.String,float[],int,int)"""
        super(_ShaderProgram, self).setUniform3fv(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def setUniformMatrix4fv(self, arg0: str, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix4fv(java.lang.String,float[],int,int)"""
        super(_ShaderProgram, self).setUniformMatrix4fv(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def setUniformi(self, arg0: str, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformi(java.lang.String,int,int,int,int)"""
        super(_ShaderProgram, self).setUniformi(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setUniformf(self, arg0: int, arg1: 'Color'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(int,com.badlogic.gdx.graphics.Color)"""
        super(_ShaderProgram, self).setUniformf(_int.valueOf(arg0), arg1)

    @overload
    def setUniformf(self, arg0: str, arg1: 'Vector4'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(java.lang.String,com.badlogic.gdx.math.Vector4)"""
        super(_ShaderProgram, self).setUniformf(arg0, arg1)

    @overload
    def setUniformMatrix(self, arg0: int, arg1: 'Matrix3', arg2: bool):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix(int,com.badlogic.gdx.math.Matrix3,boolean)"""
        super(_ShaderProgram, self).setUniformMatrix(_int.valueOf(arg0), arg1, _boolean.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def setUniformi(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformi(int,int,int)"""
        super(_ShaderProgram, self).setUniformi(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def setUniformi(self, arg0: str, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformi(java.lang.String,int,int)"""
        super(_ShaderProgram, self).setUniformi(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def bind(self):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.bind()"""
        super(ShaderProgram, self).bind()

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.end()"""
        super(ShaderProgram, self).end()

    @overload
    def hasAttribute(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.ShaderProgram.hasAttribute(java.lang.String)"""
        return bool._wrap(super(_ShaderProgram, self).hasAttribute(arg0))

    @overload
    def setUniformi(self, arg0: str, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformi(java.lang.String,int,int,int)"""
        super(_ShaderProgram, self).setUniformi(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def getAttributes(self) -> List[str]:
        """public java.lang.String[] com.badlogic.gdx.graphics.glutils.ShaderProgram.getAttributes()"""
        return List[str]._wrap(super(ShaderProgram, self).getAttributes())

    @overload
    def enableVertexAttribute(self, arg0: str):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.enableVertexAttribute(java.lang.String)"""
        super(_ShaderProgram, self).enableVertexAttribute(arg0)

    @overload
    def setUniformf(self, arg0: str, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(java.lang.String,float,float,float)"""
        super(_ShaderProgram, self).setUniformf(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def disableVertexAttribute(self, arg0: str):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.disableVertexAttribute(java.lang.String)"""
        super(_ShaderProgram, self).disableVertexAttribute(arg0)

    @staticmethod
    @overload
    def invalidateAllShaderPrograms(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.glutils.ShaderProgram.invalidateAllShaderPrograms(com.badlogic.gdx.Application)"""
        _ShaderProgram.invalidateAllShaderPrograms(arg0)

    @overload
    def getAttributeType(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ShaderProgram.getAttributeType(java.lang.String)"""
        return int._wrap(super(_ShaderProgram, self).getAttributeType(arg0))

    @overload
    def setUniformMatrix(self, arg0: int, arg1: 'Matrix4', arg2: bool):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix(int,com.badlogic.gdx.math.Matrix4,boolean)"""
        super(_ShaderProgram, self).setUniformMatrix(_int.valueOf(arg0), arg1, _boolean.valueOf(arg2))

    @overload
    def setUniform3fv(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniform3fv(int,float[],int,int)"""
        super(_ShaderProgram, self).setUniform3fv(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def getFragmentShaderSource(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.glutils.ShaderProgram.getFragmentShaderSource()"""
        return str._wrap(super(ShaderProgram, self).getFragmentShaderSource())

    @overload
    def setVertexAttribute(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setVertexAttribute(int,int,int,boolean,int,int)"""
        super(_ShaderProgram, self).setVertexAttribute(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @overload
    def setUniformMatrix(self, arg0: int, arg1: 'Matrix3'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix(int,com.badlogic.gdx.math.Matrix3)"""
        super(_ShaderProgram, self).setUniformMatrix(_int.valueOf(arg0), arg1)

    @overload
    def setUniformMatrix(self, arg0: str, arg1: 'Matrix3'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix(java.lang.String,com.badlogic.gdx.math.Matrix3)"""
        super(_ShaderProgram, self).setUniformMatrix(arg0, arg1)

    @overload
    def setUniformMatrix3fv(self, arg0: str, arg1: 'FloatBuffer', arg2: int, arg3: bool):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix3fv(java.lang.String,java.nio.FloatBuffer,int,boolean)"""
        super(_ShaderProgram, self).setUniformMatrix3fv(arg0, arg1, _int.valueOf(arg2), _boolean.valueOf(arg3))

    @overload
    def setUniformf(self, arg0: int, arg1: 'Vector4'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(int,com.badlogic.gdx.math.Vector4)"""
        super(_ShaderProgram, self).setUniformf(_int.valueOf(arg0), arg1)

    @overload
    def getVertexShaderSource(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.glutils.ShaderProgram.getVertexShaderSource()"""
        return str._wrap(super(ShaderProgram, self).getVertexShaderSource())

    @overload
    def setUniformf(self, arg0: str, arg1: 'Color'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(java.lang.String,com.badlogic.gdx.graphics.Color)"""
        super(_ShaderProgram, self).setUniformf(arg0, arg1)

    @staticmethod
    @overload
    def getNumManagedShaderPrograms() -> int:
        """public static int com.badlogic.gdx.graphics.glutils.ShaderProgram.getNumManagedShaderPrograms()"""
        return int._wrap(_ShaderProgram.getNumManagedShaderPrograms())

    @overload
    def setVertexAttribute(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'Buffer'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setVertexAttribute(int,int,int,boolean,int,java.nio.Buffer)"""
        super(_ShaderProgram, self).setVertexAttribute(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), arg5)

    @overload
    def setUniformMatrix4fv(self, arg0: str, arg1: 'FloatBuffer', arg2: int, arg3: bool):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix4fv(java.lang.String,java.nio.FloatBuffer,int,boolean)"""
        super(_ShaderProgram, self).setUniformMatrix4fv(arg0, arg1, _int.valueOf(arg2), _boolean.valueOf(arg3))

    @overload
    def getAttributeSize(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ShaderProgram.getAttributeSize(java.lang.String)"""
        return int._wrap(super(_ShaderProgram, self).getAttributeSize(arg0))

    @overload
    def getUniformLocation(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ShaderProgram.getUniformLocation(java.lang.String)"""
        return int._wrap(super(_ShaderProgram, self).getUniformLocation(arg0))

    @overload
    def setUniformf(self, arg0: int, arg1: 'Vector3'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(int,com.badlogic.gdx.math.Vector3)"""
        super(_ShaderProgram, self).setUniformf(_int.valueOf(arg0), arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getManagedStatus() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.glutils.ShaderProgram.getManagedStatus()"""
        return str._wrap(_ShaderProgram.getManagedStatus())

    @overload
    def setUniformf(self, arg0: str, arg1: 'Vector2'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(java.lang.String,com.badlogic.gdx.math.Vector2)"""
        super(_ShaderProgram, self).setUniformf(arg0, arg1)

    @overload
    def getLog(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.glutils.ShaderProgram.getLog()"""
        return str._wrap(super(ShaderProgram, self).getLog())

    @overload
    def setUniformMatrix(self, arg0: int, arg1: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix(int,com.badlogic.gdx.math.Matrix4)"""
        super(_ShaderProgram, self).setUniformMatrix(_int.valueOf(arg0), arg1)

    @overload
    def hasUniform(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.ShaderProgram.hasUniform(java.lang.String)"""
        return bool._wrap(super(_ShaderProgram, self).hasUniform(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setUniform2fv(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniform2fv(int,float[],int,int)"""
        super(_ShaderProgram, self).setUniform2fv(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def setUniform4fv(self, arg0: str, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniform4fv(java.lang.String,float[],int,int)"""
        super(_ShaderProgram, self).setUniform4fv(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def setUniform2fv(self, arg0: str, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniform2fv(java.lang.String,float[],int,int)"""
        super(_ShaderProgram, self).setUniform2fv(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def setUniformf(self, arg0: str, arg1: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(java.lang.String,float)"""
        super(_ShaderProgram, self).setUniformf(arg0, _float.valueOf(arg1))

    @overload
    def setUniformf(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(java.lang.String,float,float,float,float)"""
        super(_ShaderProgram, self).setUniformf(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.begin()"""
        super(ShaderProgram, self).begin()

 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.ShaderProgram
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.glutils.ShaderProgram as _ShaderProgram
_ShaderProgram = _ShaderProgram
from builtins import float
import java.lang.String as _String
_String = _String
import java.nio.FloatBuffer as FloatBuffer
from typing import List
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.nio.Buffer as Buffer
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ShaderProgram():
    """com.badlogic.gdx.graphics.glutils.ShaderProgram"""
 
    @staticmethod
    def _wrap(java_value: _ShaderProgram) -> 'ShaderProgram':
        return ShaderProgram(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShaderProgram):
        """
        Dynamic initializer for ShaderProgram.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShaderProgram__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShaderProgram__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getUniforms(self) -> List[str]:
        """public java.lang.String[] com.badlogic.gdx.graphics.glutils.ShaderProgram.getUniforms()"""
        return List[str]._wrap(super(ShaderProgram, self).getUniforms())

    @overload
    def setUniformf(self, arg0: int, arg1: 'Vector2'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(int,com.badlogic.gdx.math.Vector2)"""
        super(_ShaderProgram, self).setUniformf(_int.valueOf(arg0), arg1)

    @overload
    def setUniformMatrix(self, arg0: str, arg1: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix(java.lang.String,com.badlogic.gdx.math.Matrix4)"""
        super(_ShaderProgram, self).setUniformMatrix(arg0, arg1)

    @overload
    def setUniformi(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformi(int,int,int,int)"""
        super(_ShaderProgram, self).setUniformi(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def setUniformf(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(int,float)"""
        super(_ShaderProgram, self).setUniformf(_int.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def fetchUniformLocation(self, arg0: str, arg1: bool) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ShaderProgram.fetchUniformLocation(java.lang.String,boolean)"""
        return int._wrap(super(_ShaderProgram, self).fetchUniformLocation(arg0, _boolean.valueOf(arg1)))

    @overload
    def setUniform1fv(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniform1fv(int,float[],int,int)"""
        super(_ShaderProgram, self).setUniform1fv(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def getUniformType(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ShaderProgram.getUniformType(java.lang.String)"""
        return int._wrap(super(_ShaderProgram, self).getUniformType(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setUniform4fv(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniform4fv(int,float[],int,int)"""
        super(_ShaderProgram, self).setUniform4fv(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def clearAllShaderPrograms(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.glutils.ShaderProgram.clearAllShaderPrograms(com.badlogic.gdx.Application)"""
        _ShaderProgram.clearAllShaderPrograms(arg0)

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram(java.lang.String,java.lang.String)"""
        val = _ShaderProgram(arg0, arg1)
        self.__wrapper = val

    @overload
    def setUniformf(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(int,float,float,float,float)"""
        super(_ShaderProgram, self).setUniformf(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def disableVertexAttribute(self, arg0: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.disableVertexAttribute(int)"""
        super(_ShaderProgram, self).disableVertexAttribute(_int.valueOf(arg0))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.dispose()"""
        super(ShaderProgram, self).dispose()

    @overload
    def setUniformi(self, arg0: str, arg1: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformi(java.lang.String,int)"""
        super(_ShaderProgram, self).setUniformi(arg0, _int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def enableVertexAttribute(self, arg0: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.enableVertexAttribute(int)"""
        super(_ShaderProgram, self).enableVertexAttribute(_int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setUniformf(self, arg0: str, arg1: 'Vector3'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(java.lang.String,com.badlogic.gdx.math.Vector3)"""
        super(_ShaderProgram, self).setUniformf(arg0, arg1)

    @overload
    def setVertexAttribute(self, arg0: str, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'Buffer'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setVertexAttribute(java.lang.String,int,int,boolean,int,java.nio.Buffer)"""
        super(_ShaderProgram, self).setVertexAttribute(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), arg5)

    @overload
    def setUniformMatrix(self, arg0: str, arg1: 'Matrix4', arg2: bool):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix(java.lang.String,com.badlogic.gdx.math.Matrix4,boolean)"""
        super(_ShaderProgram, self).setUniformMatrix(arg0, arg1, _boolean.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setUniformi(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformi(int,int,int,int,int)"""
        super(_ShaderProgram, self).setUniformi(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle'):
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        val = _ShaderProgram(arg0, arg1)
        self.__wrapper = val

    @overload
    def setUniform1fv(self, arg0: str, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniform1fv(java.lang.String,float[],int,int)"""
        super(_ShaderProgram, self).setUniform1fv(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def getUniformSize(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ShaderProgram.getUniformSize(java.lang.String)"""
        return int._wrap(super(_ShaderProgram, self).getUniformSize(arg0))

    @overload
    def setUniformi(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformi(int,int)"""
        super(_ShaderProgram, self).setUniformi(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setVertexAttribute(self, arg0: str, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setVertexAttribute(java.lang.String,int,int,boolean,int,int)"""
        super(_ShaderProgram, self).setVertexAttribute(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @overload
    def setUniformf(self, arg0: str, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(java.lang.String,float,float)"""
        super(_ShaderProgram, self).setUniformf(arg0, _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def setUniformf(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(int,float,float)"""
        super(_ShaderProgram, self).setUniformf(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def isCompiled(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.ShaderProgram.isCompiled()"""
        return bool._wrap(super(ShaderProgram, self).isCompiled())

    @overload
    def setUniformMatrix(self, arg0: str, arg1: 'Matrix3', arg2: bool):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix(java.lang.String,com.badlogic.gdx.math.Matrix3,boolean)"""
        super(_ShaderProgram, self).setUniformMatrix(arg0, arg1, _boolean.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ShaderProgram.getHandle()"""
        return int._wrap(super(ShaderProgram, self).getHandle())

    @overload
    def getAttributeLocation(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ShaderProgram.getAttributeLocation(java.lang.String)"""
        return int._wrap(super(_ShaderProgram, self).getAttributeLocation(arg0))

    @overload
    def setUniformf(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(int,float,float,float)"""
        super(_ShaderProgram, self).setUniformf(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def setUniformMatrix4fv(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix4fv(int,float[],int,int)"""
        super(_ShaderProgram, self).setUniformMatrix4fv(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def setAttributef(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setAttributef(java.lang.String,float,float,float,float)"""
        super(_ShaderProgram, self).setAttributef(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def setUniform3fv(self, arg0: str, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniform3fv(java.lang.String,float[],int,int)"""
        super(_ShaderProgram, self).setUniform3fv(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def setUniformMatrix4fv(self, arg0: str, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix4fv(java.lang.String,float[],int,int)"""
        super(_ShaderProgram, self).setUniformMatrix4fv(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def setUniformi(self, arg0: str, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformi(java.lang.String,int,int,int,int)"""
        super(_ShaderProgram, self).setUniformi(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setUniformf(self, arg0: int, arg1: 'Color'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(int,com.badlogic.gdx.graphics.Color)"""
        super(_ShaderProgram, self).setUniformf(_int.valueOf(arg0), arg1)

    @overload
    def setUniformf(self, arg0: str, arg1: 'Vector4'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(java.lang.String,com.badlogic.gdx.math.Vector4)"""
        super(_ShaderProgram, self).setUniformf(arg0, arg1)

    @overload
    def setUniformMatrix(self, arg0: int, arg1: 'Matrix3', arg2: bool):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix(int,com.badlogic.gdx.math.Matrix3,boolean)"""
        super(_ShaderProgram, self).setUniformMatrix(_int.valueOf(arg0), arg1, _boolean.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def setUniformi(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformi(int,int,int)"""
        super(_ShaderProgram, self).setUniformi(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def setUniformi(self, arg0: str, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformi(java.lang.String,int,int)"""
        super(_ShaderProgram, self).setUniformi(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def bind(self):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.bind()"""
        super(ShaderProgram, self).bind()

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.end()"""
        super(ShaderProgram, self).end()

    @overload
    def hasAttribute(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.ShaderProgram.hasAttribute(java.lang.String)"""
        return bool._wrap(super(_ShaderProgram, self).hasAttribute(arg0))

    @overload
    def setUniformi(self, arg0: str, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformi(java.lang.String,int,int,int)"""
        super(_ShaderProgram, self).setUniformi(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def getAttributes(self) -> List[str]:
        """public java.lang.String[] com.badlogic.gdx.graphics.glutils.ShaderProgram.getAttributes()"""
        return List[str]._wrap(super(ShaderProgram, self).getAttributes())

    @overload
    def enableVertexAttribute(self, arg0: str):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.enableVertexAttribute(java.lang.String)"""
        super(_ShaderProgram, self).enableVertexAttribute(arg0)

    @overload
    def setUniformf(self, arg0: str, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(java.lang.String,float,float,float)"""
        super(_ShaderProgram, self).setUniformf(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def disableVertexAttribute(self, arg0: str):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.disableVertexAttribute(java.lang.String)"""
        super(_ShaderProgram, self).disableVertexAttribute(arg0)

    @staticmethod
    @overload
    def invalidateAllShaderPrograms(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.glutils.ShaderProgram.invalidateAllShaderPrograms(com.badlogic.gdx.Application)"""
        _ShaderProgram.invalidateAllShaderPrograms(arg0)

    @overload
    def getAttributeType(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ShaderProgram.getAttributeType(java.lang.String)"""
        return int._wrap(super(_ShaderProgram, self).getAttributeType(arg0))

    @overload
    def setUniformMatrix(self, arg0: int, arg1: 'Matrix4', arg2: bool):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix(int,com.badlogic.gdx.math.Matrix4,boolean)"""
        super(_ShaderProgram, self).setUniformMatrix(_int.valueOf(arg0), arg1, _boolean.valueOf(arg2))

    @overload
    def setUniform3fv(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniform3fv(int,float[],int,int)"""
        super(_ShaderProgram, self).setUniform3fv(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def getFragmentShaderSource(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.glutils.ShaderProgram.getFragmentShaderSource()"""
        return str._wrap(super(ShaderProgram, self).getFragmentShaderSource())

    @overload
    def setVertexAttribute(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setVertexAttribute(int,int,int,boolean,int,int)"""
        super(_ShaderProgram, self).setVertexAttribute(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @overload
    def setUniformMatrix(self, arg0: int, arg1: 'Matrix3'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix(int,com.badlogic.gdx.math.Matrix3)"""
        super(_ShaderProgram, self).setUniformMatrix(_int.valueOf(arg0), arg1)

    @overload
    def setUniformMatrix(self, arg0: str, arg1: 'Matrix3'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix(java.lang.String,com.badlogic.gdx.math.Matrix3)"""
        super(_ShaderProgram, self).setUniformMatrix(arg0, arg1)

    @overload
    def setUniformMatrix3fv(self, arg0: str, arg1: 'FloatBuffer', arg2: int, arg3: bool):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix3fv(java.lang.String,java.nio.FloatBuffer,int,boolean)"""
        super(_ShaderProgram, self).setUniformMatrix3fv(arg0, arg1, _int.valueOf(arg2), _boolean.valueOf(arg3))

    @overload
    def setUniformf(self, arg0: int, arg1: 'Vector4'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(int,com.badlogic.gdx.math.Vector4)"""
        super(_ShaderProgram, self).setUniformf(_int.valueOf(arg0), arg1)

    @overload
    def getVertexShaderSource(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.glutils.ShaderProgram.getVertexShaderSource()"""
        return str._wrap(super(ShaderProgram, self).getVertexShaderSource())

    @overload
    def setUniformf(self, arg0: str, arg1: 'Color'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(java.lang.String,com.badlogic.gdx.graphics.Color)"""
        super(_ShaderProgram, self).setUniformf(arg0, arg1)

    @staticmethod
    @overload
    def getNumManagedShaderPrograms() -> int:
        """public static int com.badlogic.gdx.graphics.glutils.ShaderProgram.getNumManagedShaderPrograms()"""
        return int._wrap(_ShaderProgram.getNumManagedShaderPrograms())

    @overload
    def setVertexAttribute(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'Buffer'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setVertexAttribute(int,int,int,boolean,int,java.nio.Buffer)"""
        super(_ShaderProgram, self).setVertexAttribute(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), arg5)

    @overload
    def setUniformMatrix4fv(self, arg0: str, arg1: 'FloatBuffer', arg2: int, arg3: bool):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix4fv(java.lang.String,java.nio.FloatBuffer,int,boolean)"""
        super(_ShaderProgram, self).setUniformMatrix4fv(arg0, arg1, _int.valueOf(arg2), _boolean.valueOf(arg3))

    @overload
    def getAttributeSize(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ShaderProgram.getAttributeSize(java.lang.String)"""
        return int._wrap(super(_ShaderProgram, self).getAttributeSize(arg0))

    @overload
    def getUniformLocation(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ShaderProgram.getUniformLocation(java.lang.String)"""
        return int._wrap(super(_ShaderProgram, self).getUniformLocation(arg0))

    @overload
    def setUniformf(self, arg0: int, arg1: 'Vector3'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(int,com.badlogic.gdx.math.Vector3)"""
        super(_ShaderProgram, self).setUniformf(_int.valueOf(arg0), arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getManagedStatus() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.glutils.ShaderProgram.getManagedStatus()"""
        return str._wrap(_ShaderProgram.getManagedStatus())

    @overload
    def setUniformf(self, arg0: str, arg1: 'Vector2'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(java.lang.String,com.badlogic.gdx.math.Vector2)"""
        super(_ShaderProgram, self).setUniformf(arg0, arg1)

    @overload
    def getLog(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.glutils.ShaderProgram.getLog()"""
        return str._wrap(super(ShaderProgram, self).getLog())

    @overload
    def setUniformMatrix(self, arg0: int, arg1: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformMatrix(int,com.badlogic.gdx.math.Matrix4)"""
        super(_ShaderProgram, self).setUniformMatrix(_int.valueOf(arg0), arg1)

    @overload
    def hasUniform(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.ShaderProgram.hasUniform(java.lang.String)"""
        return bool._wrap(super(_ShaderProgram, self).hasUniform(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setUniform2fv(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniform2fv(int,float[],int,int)"""
        super(_ShaderProgram, self).setUniform2fv(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def setUniform4fv(self, arg0: str, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniform4fv(java.lang.String,float[],int,int)"""
        super(_ShaderProgram, self).setUniform4fv(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def setUniform2fv(self, arg0: str, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniform2fv(java.lang.String,float[],int,int)"""
        super(_ShaderProgram, self).setUniform2fv(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def setUniformf(self, arg0: str, arg1: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(java.lang.String,float)"""
        super(_ShaderProgram, self).setUniformf(arg0, _float.valueOf(arg1))

    @overload
    def setUniformf(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.setUniformf(java.lang.String,float,float,float,float)"""
        super(_ShaderProgram, self).setUniformf(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.glutils.ShaderProgram.begin()"""
        super(ShaderProgram, self).begin()

 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.ShaderProgram 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.ShapeRenderer$ShapeType
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
import com.badlogic.gdx.graphics.glutils.ShapeRenderer as _ShapeRenderer_ShapeType
_ShapeType = _ShapeRenderer_ShapeType.ShapeType
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ShapeType():
    """com.badlogic.gdx.graphics.glutils.ShapeRenderer.ShapeType"""
 
    @staticmethod
    def _wrap(java_value: _ShapeType) -> 'ShapeType':
        return ShapeType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShapeType):
        """
        Dynamic initializer for ShapeType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShapeType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShapeType__wrapper":
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

    @overload
    def getGlType(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ShapeRenderer$ShapeType.getGlType()"""
        return int._wrap(super(ShapeType, self).getGlType())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ShapeType':
        """public static com.badlogic.gdx.graphics.glutils.ShapeRenderer$ShapeType com.badlogic.gdx.graphics.glutils.ShapeRenderer$ShapeType.valueOf(java.lang.String)"""
        return ShapeType._wrap(_ShapeType.valueOf(arg0))

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
    def values() -> List['ShapeType']:
        """public static com.badlogic.gdx.graphics.glutils.ShapeRenderer$ShapeType[] com.badlogic.gdx.graphics.glutils.ShapeRenderer$ShapeType.values()"""
        return List[ShapeType]._wrap(_ShapeType.values())

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
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.IndexArray
import com.badlogic.gdx.graphics.glutils.IndexArray as _IndexArray
_IndexArray = _IndexArray
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.nio.ShortBuffer as ShortBuffer
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.nio.ShortBuffer as _ShortBuffer
_ShortBuffer = _ShortBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IndexArray():
    """com.badlogic.gdx.graphics.glutils.IndexArray"""
 
    @staticmethod
    def _wrap(java_value: _IndexArray) -> 'IndexArray':
        return IndexArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IndexArray):
        """
        Dynamic initializer for IndexArray.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IndexArray__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IndexArray__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def bind(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexArray.bind()"""
        super(IndexArray, self).bind()

    @override
    @overload
    def getBuffer(self) -> 'ShortBuffer':
        """public java.nio.ShortBuffer com.badlogic.gdx.graphics.glutils.IndexArray.getBuffer()"""
        return 'ShortBuffer'._wrap(super(IndexArray, self).getBuffer())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setIndices(self, arg0: 'ShortBuffer'):
        """public void com.badlogic.gdx.graphics.glutils.IndexArray.setIndices(java.nio.ShortBuffer)"""
        super(_IndexArray, self).setIndices(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getNumMaxIndices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.IndexArray.getNumMaxIndices()"""
        return int._wrap(super(IndexArray, self).getNumMaxIndices())

    @override
    @overload
    def updateIndices(self, arg0: int, arg1: 'short', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.IndexArray.updateIndices(int,short[],int,int)"""
        super(_IndexArray, self).updateIndices(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def invalidate(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexArray.invalidate()"""
        super(IndexArray, self).invalidate()

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
    def setIndices(self, arg0: 'short', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.IndexArray.setIndices(short[],int,int)"""
        super(_IndexArray, self).setIndices(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.glutils.IndexArray(int)"""
        val = _IndexArray(_int.valueOf(arg0))
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

    @override
    @overload
    def getNumIndices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.IndexArray.getNumIndices()"""
        return int._wrap(super(IndexArray, self).getNumIndices())

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
    def getBuffer(self, arg0: bool) -> 'ShortBuffer':
        """public java.nio.ShortBuffer com.badlogic.gdx.graphics.glutils.IndexArray.getBuffer(boolean)"""
        return 'ShortBuffer'._wrap(super(_IndexArray, self).getBuffer(_boolean.valueOf(arg0)))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexArray.dispose()"""
        super(IndexArray, self).dispose()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.nio.FloatBuffer as _FloatBuffer
_FloatBuffer = _FloatBuffer
import java.lang.String as _String
_String = _String
import java.nio.FloatBuffer as FloatBuffer
import com.badlogic.gdx.graphics.VertexAttributes as _VertexAttributes
_VertexAttributes = _VertexAttributes
import com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData as _InstanceBufferObjectSubData
_InstanceBufferObjectSubData = _InstanceBufferObjectSubData
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InstanceBufferObjectSubData():
    """com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData"""
 
    @staticmethod
    def _wrap(java_value: _InstanceBufferObjectSubData) -> 'InstanceBufferObjectSubData':
        return InstanceBufferObjectSubData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InstanceBufferObjectSubData):
        """
        Dynamic initializer for InstanceBufferObjectSubData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InstanceBufferObjectSubData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InstanceBufferObjectSubData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getBuffer(self) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.getBuffer()"""
        return 'FloatBuffer'._wrap(super(InstanceBufferObjectSubData, self).getBuffer())

    @override
    @overload
    def setInstanceData(self, arg0: 'FloatBuffer', arg1: int):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.setInstanceData(java.nio.FloatBuffer,int)"""
        super(_InstanceBufferObjectSubData, self).setInstanceData(arg0, _int.valueOf(arg1))

    @override
    @overload
    def updateInstanceData(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.updateInstanceData(int,float[],int,int)"""
        super(_InstanceBufferObjectSubData, self).updateInstanceData(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def bind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(_InstanceBufferObjectSubData, self).bind(arg0)

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
    def updateInstanceData(self, arg0: int, arg1: 'FloatBuffer', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.updateInstanceData(int,java.nio.FloatBuffer,int,int)"""
        super(_InstanceBufferObjectSubData, self).updateInstanceData(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def __init__(self, arg0: bool, arg1: int, arg2: 'VertexAttributes'):
        """public com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData(boolean,int,com.badlogic.gdx.graphics.VertexAttributes)"""
        val = _InstanceBufferObjectSubData(_boolean.valueOf(arg0), _int.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def invalidate(self):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.invalidate()"""
        super(InstanceBufferObjectSubData, self).invalidate()

    @overload
    def getBufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.getBufferHandle()"""
        return int._wrap(super(InstanceBufferObjectSubData, self).getBufferHandle())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getNumMaxInstances(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.getNumMaxInstances()"""
        return int._wrap(super(InstanceBufferObjectSubData, self).getNumMaxInstances())

    @override
    @overload
    def getAttributes(self) -> 'graphics.VertexAttributes':
        """public com.badlogic.gdx.graphics.VertexAttributes com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.getAttributes()"""
        return 'graphics.VertexAttributes'._wrap(super(InstanceBufferObjectSubData, self).getAttributes())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def unbind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        super(_InstanceBufferObjectSubData, self).unbind(arg0, arg1)

    @override
    @overload
    def bind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        super(_InstanceBufferObjectSubData, self).bind(arg0, arg1)

    @overload
    def __init__(self, arg0: bool, arg1: int, *arg2: 'graphics.VertexAttribute'):
        """public com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData(boolean,int,com.badlogic.gdx.graphics.VertexAttribute...)"""
        val = _InstanceBufferObjectSubData(_boolean.valueOf(arg0), _int.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def getNumInstances(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.getNumInstances()"""
        return int._wrap(super(InstanceBufferObjectSubData, self).getNumInstances())

    @overload
    def getBuffer(self, arg0: bool) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.getBuffer(boolean)"""
        return 'FloatBuffer'._wrap(super(_InstanceBufferObjectSubData, self).getBuffer(_boolean.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setInstanceData(self, arg0: 'float', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.setInstanceData(float[],int,int)"""
        super(_InstanceBufferObjectSubData, self).setInstanceData(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def unbind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObjectSubData.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(_InstanceBufferObjectSubData, self).unbind(arg0)

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer as _ImmediateModeRenderer
_ImmediateModeRenderer = _ImmediateModeRenderer
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from abc import abstractmethod, ABC
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

 
class ImmediateModeRenderer():
    """com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer"""
 
    @staticmethod
    def _wrap(java_value: _ImmediateModeRenderer) -> 'ImmediateModeRenderer':
        return ImmediateModeRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ImmediateModeRenderer):
        """
        Dynamic initializer for ImmediateModeRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ImmediateModeRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ImmediateModeRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.nio.ShortBuffer as ShortBuffer
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData as _IndexBufferObjectSubData
_IndexBufferObjectSubData = _IndexBufferObjectSubData
import java.nio.ShortBuffer as _ShortBuffer
_ShortBuffer = _ShortBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IndexBufferObjectSubData():
    """com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData"""
 
    @staticmethod
    def _wrap(java_value: _IndexBufferObjectSubData) -> 'IndexBufferObjectSubData':
        return IndexBufferObjectSubData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IndexBufferObjectSubData):
        """
        Dynamic initializer for IndexBufferObjectSubData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IndexBufferObjectSubData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IndexBufferObjectSubData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def invalidate(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.invalidate()"""
        super(IndexBufferObjectSubData, self).invalidate()

    @override
    @overload
    def getNumMaxIndices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.getNumMaxIndices()"""
        return int._wrap(super(IndexBufferObjectSubData, self).getNumMaxIndices())

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
    def bind(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.bind()"""
        super(IndexBufferObjectSubData, self).bind()

    @override
    @overload
    def unbind(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.unbind()"""
        super(IndexBufferObjectSubData, self).unbind()

    @overload
    def __init__(self, arg0: bool, arg1: int):
        """public com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData(boolean,int)"""
        val = _IndexBufferObjectSubData(_boolean.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getBuffer(self, arg0: bool) -> 'ShortBuffer':
        """public java.nio.ShortBuffer com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.getBuffer(boolean)"""
        return 'ShortBuffer'._wrap(super(_IndexBufferObjectSubData, self).getBuffer(_boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def setIndices(self, arg0: 'ShortBuffer'):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.setIndices(java.nio.ShortBuffer)"""
        super(_IndexBufferObjectSubData, self).setIndices(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getBuffer(self) -> 'ShortBuffer':
        """public java.nio.ShortBuffer com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.getBuffer()"""
        return 'ShortBuffer'._wrap(super(IndexBufferObjectSubData, self).getBuffer())

    @override
    @overload
    def getNumIndices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.getNumIndices()"""
        return int._wrap(super(IndexBufferObjectSubData, self).getNumIndices())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.dispose()"""
        super(IndexBufferObjectSubData, self).dispose()

    @override
    @overload
    def setIndices(self, arg0: 'short', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.setIndices(short[],int,int)"""
        super(_IndexBufferObjectSubData, self).setIndices(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData(int)"""
        val = _IndexBufferObjectSubData(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def updateIndices(self, arg0: int, arg1: 'short', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObjectSubData.updateIndices(int,short[],int,int)"""
        super(_IndexBufferObjectSubData, self).updateIndices(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.HdpiUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.glutils.HdpiUtils as _HdpiUtils
_HdpiUtils = _HdpiUtils
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HdpiUtils():
    """com.badlogic.gdx.graphics.glutils.HdpiUtils"""
 
    @staticmethod
    def _wrap(java_value: _HdpiUtils) -> 'HdpiUtils':
        return HdpiUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HdpiUtils):
        """
        Dynamic initializer for HdpiUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HdpiUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HdpiUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def toBackBufferY(arg0: int) -> int:
        """public static int com.badlogic.gdx.graphics.glutils.HdpiUtils.toBackBufferY(int)"""
        return int._wrap(_HdpiUtils.toBackBufferY(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def setMode(arg0: 'HdpiMode'):
        """public static void com.badlogic.gdx.graphics.glutils.HdpiUtils.setMode(com.badlogic.gdx.graphics.glutils.HdpiMode)"""
        _HdpiUtils.setMode(arg0)

    @staticmethod
    @overload
    def glScissor(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static void com.badlogic.gdx.graphics.glutils.HdpiUtils.glScissor(int,int,int,int)"""
        _HdpiUtils.glScissor(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

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
    def toLogicalY(arg0: int) -> int:
        """public static int com.badlogic.gdx.graphics.glutils.HdpiUtils.toLogicalY(int)"""
        return int._wrap(_HdpiUtils.toLogicalY(_int.valueOf(arg0)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.glutils.HdpiUtils()"""
        val = _HdpiUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def glViewport(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static void com.badlogic.gdx.graphics.glutils.HdpiUtils.glViewport(int,int,int,int)"""
        _HdpiUtils.glViewport(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def toLogicalX(arg0: int) -> int:
        """public static int com.badlogic.gdx.graphics.glutils.HdpiUtils.toLogicalX(int)"""
        return int._wrap(_HdpiUtils.toLogicalX(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def toBackBufferX(arg0: int) -> int:
        """public static int com.badlogic.gdx.graphics.glutils.HdpiUtils.toBackBufferX(int)"""
        return int._wrap(_HdpiUtils.toBackBufferX(_int.valueOf(arg0)))

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.glutils.HdpiUtils()"""
        val = _HdpiUtils()
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
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.IndexData
import com.badlogic.gdx.graphics.glutils.IndexData as _IndexData
_IndexData = _IndexData
from abc import abstractmethod, ABC
import java.nio.ShortBuffer as ShortBuffer
from builtins import int
 
class IndexData():
    """com.badlogic.gdx.graphics.glutils.IndexData"""
 
    @staticmethod
    def _wrap(java_value: _IndexData) -> 'IndexData':
        return IndexData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IndexData):
        """
        Dynamic initializer for IndexData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IndexData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IndexData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
    def updateIndices(self, arg0: int, arg1: 'short', arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.glutils.IndexData.updateIndices(int,short[],int,int)"""
        pass

    @abstractmethod
    def setIndices(self, arg0: 'ShortBuffer'):
        """public abstract void com.badlogic.gdx.graphics.glutils.IndexData.setIndices(java.nio.ShortBuffer)"""
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
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FrameBufferBuilder
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.glutils.FrameBuffer as _FrameBuffer
_FrameBuffer = _FrameBuffer
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.glutils.GLFrameBuffer as _GLFrameBuffer_FrameBufferBuilder
_FrameBufferBuilder = _GLFrameBuffer_FrameBufferBuilder.FrameBufferBuilder
import com.badlogic.gdx.graphics.glutils.GLFrameBuffer as _GLFrameBuffer_GLFrameBufferBuilder
_GLFrameBufferBuilder = _GLFrameBuffer_GLFrameBufferBuilder.GLFrameBufferBuilder
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FrameBufferBuilder():
    """com.badlogic.gdx.graphics.glutils.GLFrameBuffer.FrameBufferBuilder"""
 
    @staticmethod
    def _wrap(java_value: _FrameBufferBuilder) -> 'FrameBufferBuilder':
        return FrameBufferBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FrameBufferBuilder):
        """
        Dynamic initializer for FrameBufferBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FrameBufferBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FrameBufferBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addStencilTextureAttachment(self, arg0: int, arg1: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addStencilTextureAttachment(int,int)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addStencilTextureAttachment(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def addColorTextureAttachment(self, arg0: int, arg1: int, arg2: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addColorTextureAttachment(int,int,int)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addColorTextureAttachment(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def addStencilDepthPackedRenderBuffer(self, arg0: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addStencilDepthPackedRenderBuffer(int)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addStencilDepthPackedRenderBuffer(_int.valueOf(arg0)))

    @override
    @overload
    def addBasicStencilDepthPackedRenderBuffer(self) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicStencilDepthPackedRenderBuffer()"""
        return 'GLFrameBufferBuilder'._wrap(super(GLFrameBufferBuilder, self).addBasicStencilDepthPackedRenderBuffer())

    @override
    @overload
    def addBasicDepthRenderBuffer(self) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicDepthRenderBuffer()"""
        return 'GLFrameBufferBuilder'._wrap(super(GLFrameBufferBuilder, self).addBasicDepthRenderBuffer())

    @override
    @overload
    def build(self) -> 'FrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FrameBufferBuilder.build()"""
        return 'FrameBuffer'._wrap(super(FrameBufferBuilder, self).build())

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

    @overload
    def addDepthTextureAttachment(self, arg0: int, arg1: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addDepthTextureAttachment(int,int)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addDepthTextureAttachment(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def addDepthRenderBuffer(self, arg0: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addDepthRenderBuffer(int)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addDepthRenderBuffer(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FrameBufferBuilder(int,int)"""
        val = _FrameBufferBuilder(_int.valueOf(arg0), _int.valueOf(arg1))
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
    def addStencilRenderBuffer(self, arg0: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addStencilRenderBuffer(int)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addStencilRenderBuffer(_int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def addFloatAttachment(self, arg0: int, arg1: int, arg2: int, arg3: bool) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addFloatAttachment(int,int,int,boolean)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addFloatAttachment(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def addBasicColorTextureAttachment(self, arg0: 'Format') -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicColorTextureAttachment(com.badlogic.gdx.graphics.Pixmap$Format)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addBasicColorTextureAttachment(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def addBasicStencilRenderBuffer(self) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicStencilRenderBuffer()"""
        return 'GLFrameBufferBuilder'._wrap(super(GLFrameBufferBuilder, self).addBasicStencilRenderBuffer())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.KTXTextureData
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.Pixmap as _Pixmap_Format
_Format = _Pixmap_Format.Format
import com.badlogic.gdx.graphics.TextureData as _TextureData_TextureDataType
_TextureDataType = _TextureData_TextureDataType.TextureDataType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import com.badlogic.gdx.graphics.glutils.KTXTextureData as _KTXTextureData
_KTXTextureData = _KTXTextureData
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.nio.ByteBuffer as ByteBuffer
import com.badlogic.gdx.graphics.Pixmap as _Pixmap
_Pixmap = _Pixmap
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class KTXTextureData():
    """com.badlogic.gdx.graphics.glutils.KTXTextureData"""
 
    @staticmethod
    def _wrap(java_value: _KTXTextureData) -> 'KTXTextureData':
        return KTXTextureData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _KTXTextureData):
        """
        Dynamic initializer for KTXTextureData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_KTXTextureData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_KTXTextureData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getFormat(self) -> 'graphics.Pixmap$Format':
        """public com.badlogic.gdx.graphics.Pixmap$Format com.badlogic.gdx.graphics.glutils.KTXTextureData.getFormat()"""
        return 'graphics.Pixmap$Format'._wrap(super(KTXTextureData, self).getFormat())

    @overload
    def disposePreparedData(self):
        """public void com.badlogic.gdx.graphics.glutils.KTXTextureData.disposePreparedData()"""
        super(KTXTextureData, self).disposePreparedData()

    @override
    @overload
    def consumeCustomData(self, arg0: int):
        """public void com.badlogic.gdx.graphics.glutils.KTXTextureData.consumeCustomData(int)"""
        super(_KTXTextureData, self).consumeCustomData(_int.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def consumePixmap(self) -> 'graphics.Pixmap':
        """public com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.graphics.glutils.KTXTextureData.consumePixmap()"""
        return 'graphics.Pixmap'._wrap(super(KTXTextureData, self).consumePixmap())

    @override
    @overload
    def disposePixmap(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.KTXTextureData.disposePixmap()"""
        return bool._wrap(super(KTXTextureData, self).disposePixmap())

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
    def useMipMaps(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.KTXTextureData.useMipMaps()"""
        return bool._wrap(super(KTXTextureData, self).useMipMaps())

    @overload
    def getNumberOfMipMapLevels(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.KTXTextureData.getNumberOfMipMapLevels()"""
        return int._wrap(super(KTXTextureData, self).getNumberOfMipMapLevels())

    @override
    @overload
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.KTXTextureData.isManaged()"""
        return bool._wrap(super(KTXTextureData, self).isManaged())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def prepare(self):
        """public void com.badlogic.gdx.graphics.glutils.KTXTextureData.prepare()"""
        super(KTXTextureData, self).prepare()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def consumeCubemapData(self):
        """public void com.badlogic.gdx.graphics.glutils.KTXTextureData.consumeCubemapData()"""
        super(KTXTextureData, self).consumeCubemapData()

    @overload
    def getData(self, arg0: int, arg1: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.graphics.glutils.KTXTextureData.getData(int,int)"""
        return 'ByteBuffer'._wrap(super(_KTXTextureData, self).getData(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getType(self) -> 'graphics.TextureData$TextureDataType':
        """public com.badlogic.gdx.graphics.TextureData$TextureDataType com.badlogic.gdx.graphics.glutils.KTXTextureData.getType()"""
        return 'graphics.TextureData$TextureDataType'._wrap(super(KTXTextureData, self).getType())

    @overload
    def getNumberOfFaces(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.KTXTextureData.getNumberOfFaces()"""
        return int._wrap(super(KTXTextureData, self).getNumberOfFaces())

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
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.KTXTextureData.getWidth()"""
        return int._wrap(super(KTXTextureData, self).getWidth())

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: bool):
        """public com.badlogic.gdx.graphics.glutils.KTXTextureData(com.badlogic.gdx.files.FileHandle,boolean)"""
        val = _KTXTextureData(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

    @overload
    def getGlInternalFormat(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.KTXTextureData.getGlInternalFormat()"""
        return int._wrap(super(KTXTextureData, self).getGlInternalFormat())

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.KTXTextureData.getHeight()"""
        return int._wrap(super(KTXTextureData, self).getHeight())

    @override
    @overload
    def isPrepared(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.KTXTextureData.isPrepared()"""
        return bool._wrap(super(KTXTextureData, self).isPrepared())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.ETC1$ETC1Data
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.graphics.glutils.ETC1 as _ETC1_ETC1Data
_ETC1Data = _ETC1_ETC1Data.ETC1Data
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ETC1Data():
    """com.badlogic.gdx.graphics.glutils.ETC1.ETC1Data"""
 
    @staticmethod
    def _wrap(java_value: _ETC1Data) -> 'ETC1Data':
        return ETC1Data(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ETC1Data):
        """
        Dynamic initializer for ETC1Data.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ETC1Data__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ETC1Data__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'ByteBuffer', arg3: int):
        """public com.badlogic.gdx.graphics.glutils.ETC1$ETC1Data(int,int,java.nio.ByteBuffer,int)"""
        val = _ETC1Data(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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
    def hasPKMHeader(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.ETC1$ETC1Data.hasPKMHeader()"""
        return bool._wrap(super(ETC1Data, self).hasPKMHeader())

    @overload
    def write(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.graphics.glutils.ETC1$ETC1Data.write(com.badlogic.gdx.files.FileHandle)"""
        super(_ETC1Data, self).write(arg0)

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
    def __init__(self, arg0: 'FileHandle'):
        """public com.badlogic.gdx.graphics.glutils.ETC1$ETC1Data(com.badlogic.gdx.files.FileHandle)"""
        val = _ETC1Data(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.glutils.ETC1$ETC1Data.toString()"""
        return str._wrap(super(ETC1Data, self).toString())

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
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.GLFrameBuffer
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.StringBuilder as _StringBuilder
_StringBuilder = _StringBuilder
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.glutils.GLFrameBuffer as _GLFrameBuffer
_GLFrameBuffer = _GLFrameBuffer
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.graphics.GLTexture as _GLTexture
_GLTexture = _GLTexture
import java.lang.Integer as _int
import java.lang.StringBuilder as StringBuilder
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFrameBuffer():
    """com.badlogic.gdx.graphics.glutils.GLFrameBuffer"""
 
    @staticmethod
    def _wrap(java_value: _GLFrameBuffer) -> 'GLFrameBuffer':
        return GLFrameBuffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFrameBuffer):
        """
        Dynamic initializer for GLFrameBuffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFrameBuffer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFrameBuffer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def bind(self):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.bind()"""
        super(GLFrameBuffer, self).bind()

    @overload
    def end(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.end(int,int,int,int)"""
        super(_GLFrameBuffer, self).end(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def getFramebufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getFramebufferHandle()"""
        return int._wrap(super(GLFrameBuffer, self).getFramebufferHandle())

    @overload
    def getStencilBufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getStencilBufferHandle()"""
        return int._wrap(super(GLFrameBuffer, self).getStencilBufferHandle())

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

    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.begin()"""
        super(GLFrameBuffer, self).begin()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getWidth()"""
        return int._wrap(super(GLFrameBuffer, self).getWidth())

    @staticmethod
    @overload
    def clearAllFrameBuffers(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.clearAllFrameBuffers(com.badlogic.gdx.Application)"""
        _GLFrameBuffer.clearAllFrameBuffers(arg0)

        @staticmethod
        @overload
        def unbind():
            """public static void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.unbind()"""
            _GLFrameBuffer.unbind()

    @overload
    def getTextureAttachments(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getTextureAttachments()"""
        return 'utils.Array'._wrap(super(GLFrameBuffer, self).getTextureAttachments())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getManagedStatus(arg0: 'StringBuilder') -> 'StringBuilder':
        """public static java.lang.StringBuilder com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getManagedStatus(java.lang.StringBuilder)"""
        return StringBuilder._wrap(_GLFrameBuffer.getManagedStatus(arg0))

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.end()"""
        super(GLFrameBuffer, self).end()

    @staticmethod
    @overload
    def getManagedStatus() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getManagedStatus()"""
        return str._wrap(_GLFrameBuffer.getManagedStatus())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getHeight()"""
        return int._wrap(super(GLFrameBuffer, self).getHeight())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

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
        return 'graphics.GLTexture'._wrap(super(GLFrameBuffer, self).getColorBufferTexture())

    @overload
    def getDepthBufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getDepthBufferHandle()"""
        return int._wrap(super(GLFrameBuffer, self).getDepthBufferHandle())

    @staticmethod
    @overload
    def invalidateAllFrameBuffers(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.invalidateAllFrameBuffers(com.badlogic.gdx.Application)"""
        _GLFrameBuffer.invalidateAllFrameBuffers(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FrameBufferRenderBufferAttachmentSpec
import com.badlogic.gdx.graphics.glutils.GLFrameBuffer as _GLFrameBuffer_FrameBufferRenderBufferAttachmentSpec
_FrameBufferRenderBufferAttachmentSpec = _GLFrameBuffer_FrameBufferRenderBufferAttachmentSpec.FrameBufferRenderBufferAttachmentSpec
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
 
class FrameBufferRenderBufferAttachmentSpec():
    """com.badlogic.gdx.graphics.glutils.GLFrameBuffer.FrameBufferRenderBufferAttachmentSpec"""
 
    @staticmethod
    def _wrap(java_value: _FrameBufferRenderBufferAttachmentSpec) -> 'FrameBufferRenderBufferAttachmentSpec':
        return FrameBufferRenderBufferAttachmentSpec(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FrameBufferRenderBufferAttachmentSpec):
        """
        Dynamic initializer for FrameBufferRenderBufferAttachmentSpec.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FrameBufferRenderBufferAttachmentSpec__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FrameBufferRenderBufferAttachmentSpec__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FrameBufferRenderBufferAttachmentSpec(int)"""
        val = _FrameBufferRenderBufferAttachmentSpec(_int.valueOf(arg0))
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
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.InstanceData
from builtins import float
from abc import abstractmethod, ABC
import com.badlogic.gdx.graphics.glutils.InstanceData as _InstanceData
_InstanceData = _InstanceData
import java.nio.FloatBuffer as FloatBuffer
from builtins import int
 
class InstanceData():
    """com.badlogic.gdx.graphics.glutils.InstanceData"""
 
    @staticmethod
    def _wrap(java_value: _InstanceData) -> 'InstanceData':
        return InstanceData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InstanceData):
        """
        Dynamic initializer for InstanceData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InstanceData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InstanceData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO as _VertexBufferObjectWithVAO
_VertexBufferObjectWithVAO = _VertexBufferObjectWithVAO
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.nio.FloatBuffer as _FloatBuffer
_FloatBuffer = _FloatBuffer
import java.lang.String as _String
_String = _String
import java.nio.FloatBuffer as FloatBuffer
import com.badlogic.gdx.graphics.VertexAttributes as _VertexAttributes
_VertexAttributes = _VertexAttributes
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.nio.ByteBuffer as ByteBuffer
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class VertexBufferObjectWithVAO():
    """com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO"""
 
    @staticmethod
    def _wrap(java_value: _VertexBufferObjectWithVAO) -> 'VertexBufferObjectWithVAO':
        return VertexBufferObjectWithVAO(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _VertexBufferObjectWithVAO):
        """
        Dynamic initializer for VertexBufferObjectWithVAO.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_VertexBufferObjectWithVAO__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_VertexBufferObjectWithVAO__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO.dispose()"""
        super(VertexBufferObjectWithVAO, self).dispose()

    @overload
    def __init__(self, arg0: bool, arg1: 'ByteBuffer', arg2: 'VertexAttributes'):
        """public com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO(boolean,java.nio.ByteBuffer,com.badlogic.gdx.graphics.VertexAttributes)"""
        val = _VertexBufferObjectWithVAO(_boolean.valueOf(arg0), arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def unbind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(_VertexBufferObjectWithVAO, self).unbind(arg0)

    @override
    @overload
    def getNumMaxVertices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO.getNumMaxVertices()"""
        return int._wrap(super(VertexBufferObjectWithVAO, self).getNumMaxVertices())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getAttributes(self) -> 'graphics.VertexAttributes':
        """public com.badlogic.gdx.graphics.VertexAttributes com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO.getAttributes()"""
        return 'graphics.VertexAttributes'._wrap(super(VertexBufferObjectWithVAO, self).getAttributes())

    @override
    @overload
    def updateVertices(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO.updateVertices(int,float[],int,int)"""
        super(_VertexBufferObjectWithVAO, self).updateVertices(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def unbind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        super(_VertexBufferObjectWithVAO, self).unbind(arg0, arg1)

    @override
    @overload
    def getNumVertices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO.getNumVertices()"""
        return int._wrap(super(VertexBufferObjectWithVAO, self).getNumVertices())

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
    def __init__(self, arg0: bool, arg1: int, *arg2: 'graphics.VertexAttribute'):
        """public com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO(boolean,int,com.badlogic.gdx.graphics.VertexAttribute...)"""
        val = _VertexBufferObjectWithVAO(_boolean.valueOf(arg0), _int.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def bind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        super(_VertexBufferObjectWithVAO, self).bind(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: bool, arg1: int, arg2: 'VertexAttributes'):
        """public com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO(boolean,int,com.badlogic.gdx.graphics.VertexAttributes)"""
        val = _VertexBufferObjectWithVAO(_boolean.valueOf(arg0), _int.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def bind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(_VertexBufferObjectWithVAO, self).bind(arg0)

    @override
    @overload
    def invalidate(self):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO.invalidate()"""
        super(VertexBufferObjectWithVAO, self).invalidate()

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
    def getBuffer(self, arg0: bool) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO.getBuffer(boolean)"""
        return 'FloatBuffer'._wrap(super(_VertexBufferObjectWithVAO, self).getBuffer(_boolean.valueOf(arg0)))

    @override
    @overload
    def setVertices(self, arg0: 'float', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO.setVertices(float[],int,int)"""
        super(_VertexBufferObjectWithVAO, self).setVertices(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def getBuffer(self) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.VertexBufferObjectWithVAO.getBuffer()"""
        return 'FloatBuffer'._wrap(super(VertexBufferObjectWithVAO, self).getBuffer())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.MipMapTextureData
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.glutils.MipMapTextureData as _MipMapTextureData
_MipMapTextureData = _MipMapTextureData
import com.badlogic.gdx.graphics.Pixmap as _Pixmap_Format
_Format = _Pixmap_Format.Format
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
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.Pixmap as _Pixmap
_Pixmap = _Pixmap
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MipMapTextureData():
    """com.badlogic.gdx.graphics.glutils.MipMapTextureData"""
 
    @staticmethod
    def _wrap(java_value: _MipMapTextureData) -> 'MipMapTextureData':
        return MipMapTextureData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MipMapTextureData):
        """
        Dynamic initializer for MipMapTextureData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MipMapTextureData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MipMapTextureData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.MipMapTextureData.getHeight()"""
        return int._wrap(super(MipMapTextureData, self).getHeight())

    @override
    @overload
    def consumeCustomData(self, arg0: int):
        """public void com.badlogic.gdx.graphics.glutils.MipMapTextureData.consumeCustomData(int)"""
        super(_MipMapTextureData, self).consumeCustomData(_int.valueOf(arg0))

    @override
    @overload
    def disposePixmap(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.MipMapTextureData.disposePixmap()"""
        return bool._wrap(super(MipMapTextureData, self).disposePixmap())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getFormat(self) -> 'graphics.Pixmap$Format':
        """public com.badlogic.gdx.graphics.Pixmap$Format com.badlogic.gdx.graphics.glutils.MipMapTextureData.getFormat()"""
        return 'graphics.Pixmap$Format'._wrap(super(MipMapTextureData, self).getFormat())

    @override
    @overload
    def isPrepared(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.MipMapTextureData.isPrepared()"""
        return bool._wrap(super(MipMapTextureData, self).isPrepared())

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

    @overload
    def __init__(self, *arg0: 'graphics.TextureData'):
        """public com.badlogic.gdx.graphics.glutils.MipMapTextureData(com.badlogic.gdx.graphics.TextureData...)"""
        val = _MipMapTextureData(arg0)
        self.__wrapper = val

    @override
    @overload
    def getType(self) -> 'graphics.TextureData$TextureDataType':
        """public com.badlogic.gdx.graphics.TextureData$TextureDataType com.badlogic.gdx.graphics.glutils.MipMapTextureData.getType()"""
        return 'graphics.TextureData$TextureDataType'._wrap(super(MipMapTextureData, self).getType())

    @override
    @overload
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.MipMapTextureData.isManaged()"""
        return bool._wrap(super(MipMapTextureData, self).isManaged())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def consumePixmap(self) -> 'graphics.Pixmap':
        """public com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.graphics.glutils.MipMapTextureData.consumePixmap()"""
        return 'graphics.Pixmap'._wrap(super(MipMapTextureData, self).consumePixmap())

    @override
    @overload
    def prepare(self):
        """public void com.badlogic.gdx.graphics.glutils.MipMapTextureData.prepare()"""
        super(MipMapTextureData, self).prepare()

    @override
    @overload
    def useMipMaps(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.MipMapTextureData.useMipMaps()"""
        return bool._wrap(super(MipMapTextureData, self).useMipMaps())

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.MipMapTextureData.getWidth()"""
        return int._wrap(super(MipMapTextureData, self).getWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20 as _ImmediateModeRenderer20
_ImmediateModeRenderer20 = _ImmediateModeRenderer20
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.glutils.ShaderProgram as _ShaderProgram
_ShaderProgram = _ShaderProgram
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ImmediateModeRenderer20():
    """com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20"""
 
    @staticmethod
    def _wrap(java_value: _ImmediateModeRenderer20) -> 'ImmediateModeRenderer20':
        return ImmediateModeRenderer20(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ImmediateModeRenderer20):
        """
        Dynamic initializer for ImmediateModeRenderer20.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ImmediateModeRenderer20__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ImmediateModeRenderer20__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def color(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.color(float,float,float,float)"""
        super(_ImmediateModeRenderer20, self).color(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def begin(self, arg0: 'Matrix4', arg1: int):
        """public void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.begin(com.badlogic.gdx.math.Matrix4,int)"""
        super(_ImmediateModeRenderer20, self).begin(arg0, _int.valueOf(arg1))

    @override
    @overload
    def normal(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.normal(float,float,float)"""
        super(_ImmediateModeRenderer20, self).normal(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def getShader(self) -> 'ShaderProgram':
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.getShader()"""
        return 'ShaderProgram'._wrap(super(ImmediateModeRenderer20, self).getShader())

    @override
    @overload
    def texCoord(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.texCoord(float,float)"""
        super(_ImmediateModeRenderer20, self).texCoord(_float.valueOf(arg0), _float.valueOf(arg1))

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
    def flush(self):
        """public void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.flush()"""
        super(ImmediateModeRenderer20, self).flush()

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.end()"""
        super(ImmediateModeRenderer20, self).end()

    @overload
    def __init__(self, arg0: bool, arg1: bool, arg2: int):
        """public com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20(boolean,boolean,int)"""
        val = _ImmediateModeRenderer20(_boolean.valueOf(arg0), _boolean.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def vertex(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.vertex(float,float,float)"""
        super(_ImmediateModeRenderer20, self).vertex(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def createDefaultShader(arg0: bool, arg1: bool, arg2: int) -> 'ShaderProgram':
        """public static com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.createDefaultShader(boolean,boolean,int)"""
        return ShaderProgram._wrap(_ImmediateModeRenderer20.createDefaultShader(_boolean.valueOf(arg0), _boolean.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def color(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.color(com.badlogic.gdx.graphics.Color)"""
        super(_ImmediateModeRenderer20, self).color(arg0)

    @override
    @overload
    def getNumVertices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.getNumVertices()"""
        return int._wrap(super(ImmediateModeRenderer20, self).getNumVertices())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.dispose()"""
        super(ImmediateModeRenderer20, self).dispose()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int, arg1: bool, arg2: bool, arg3: int, arg4: 'ShaderProgram'):
        """public com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20(int,boolean,boolean,int,com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        val = _ImmediateModeRenderer20(_int.valueOf(arg0), _boolean.valueOf(arg1), _boolean.valueOf(arg2), _int.valueOf(arg3), arg4)
        self.__wrapper = val

    @override
    @overload
    def color(self, arg0: float):
        """public void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.color(float)"""
        super(_ImmediateModeRenderer20, self).color(_float.valueOf(arg0))

    @override
    @overload
    def getMaxVertices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.getMaxVertices()"""
        return int._wrap(super(ImmediateModeRenderer20, self).getMaxVertices())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setShader(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20.setShader(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(_ImmediateModeRenderer20, self).setShader(arg0)

    @overload
    def __init__(self, arg0: int, arg1: bool, arg2: bool, arg3: int):
        """public com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer20(int,boolean,boolean,int)"""
        val = _ImmediateModeRenderer20(_int.valueOf(arg0), _boolean.valueOf(arg1), _boolean.valueOf(arg2), _int.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData as _VertexBufferObjectSubData
_VertexBufferObjectSubData = _VertexBufferObjectSubData
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.nio.FloatBuffer as _FloatBuffer
_FloatBuffer = _FloatBuffer
import java.lang.String as _String
_String = _String
import java.nio.FloatBuffer as FloatBuffer
import com.badlogic.gdx.graphics.VertexAttributes as _VertexAttributes
_VertexAttributes = _VertexAttributes
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class VertexBufferObjectSubData():
    """com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData"""
 
    @staticmethod
    def _wrap(java_value: _VertexBufferObjectSubData) -> 'VertexBufferObjectSubData':
        return VertexBufferObjectSubData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _VertexBufferObjectSubData):
        """
        Dynamic initializer for VertexBufferObjectSubData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_VertexBufferObjectSubData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_VertexBufferObjectSubData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getBuffer(self, arg0: bool) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.getBuffer(boolean)"""
        return 'FloatBuffer'._wrap(super(_VertexBufferObjectSubData, self).getBuffer(_boolean.valueOf(arg0)))

    @override
    @overload
    def bind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        super(_VertexBufferObjectSubData, self).bind(arg0, arg1)

    @override
    @overload
    def setVertices(self, arg0: 'float', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.setVertices(float[],int,int)"""
        super(_VertexBufferObjectSubData, self).setVertices(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

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
    def getBuffer(self) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.getBuffer()"""
        return 'FloatBuffer'._wrap(super(VertexBufferObjectSubData, self).getBuffer())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def invalidate(self):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.invalidate()"""
        super(VertexBufferObjectSubData, self).invalidate()

    @overload
    def getBufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.getBufferHandle()"""
        return int._wrap(super(VertexBufferObjectSubData, self).getBufferHandle())

    @override
    @overload
    def unbind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        super(_VertexBufferObjectSubData, self).unbind(arg0, arg1)

    @override
    @overload
    def bind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(_VertexBufferObjectSubData, self).bind(arg0)

    @override
    @overload
    def unbind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(_VertexBufferObjectSubData, self).unbind(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: bool, arg1: int, arg2: 'VertexAttributes'):
        """public com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData(boolean,int,com.badlogic.gdx.graphics.VertexAttributes)"""
        val = _VertexBufferObjectSubData(_boolean.valueOf(arg0), _int.valueOf(arg1), arg2)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: bool, arg1: int, *arg2: 'graphics.VertexAttribute'):
        """public com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData(boolean,int,com.badlogic.gdx.graphics.VertexAttribute...)"""
        val = _VertexBufferObjectSubData(_boolean.valueOf(arg0), _int.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.dispose()"""
        super(VertexBufferObjectSubData, self).dispose()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getNumMaxVertices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.getNumMaxVertices()"""
        return int._wrap(super(VertexBufferObjectSubData, self).getNumMaxVertices())

    @override
    @overload
    def getAttributes(self) -> 'graphics.VertexAttributes':
        """public com.badlogic.gdx.graphics.VertexAttributes com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.getAttributes()"""
        return 'graphics.VertexAttributes'._wrap(super(VertexBufferObjectSubData, self).getAttributes())

    @override
    @overload
    def updateVertices(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.updateVertices(int,float[],int,int)"""
        super(_VertexBufferObjectSubData, self).updateVertices(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3))

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
    def getNumVertices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.VertexBufferObjectSubData.getNumVertices()"""
        return int._wrap(super(VertexBufferObjectSubData, self).getNumVertices())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.GLVersion$Type
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.glutils.GLVersion as _GLVersion_Type
_Type = _GLVersion_Type.Type
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
 
class Type():
    """com.badlogic.gdx.graphics.glutils.GLVersion.Type"""
 
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
    def valueOf(arg0: str) -> 'Type':
        """public static com.badlogic.gdx.graphics.glutils.GLVersion$Type com.badlogic.gdx.graphics.glutils.GLVersion$Type.valueOf(java.lang.String)"""
        return Type._wrap(_Type.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['Type']:
        """public static com.badlogic.gdx.graphics.glutils.GLVersion$Type[] com.badlogic.gdx.graphics.glutils.GLVersion$Type.values()"""
        return List[Type]._wrap(_Type.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FrameBufferTextureAttachmentSpec
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.glutils.GLFrameBuffer as _GLFrameBuffer_FrameBufferTextureAttachmentSpec
_FrameBufferTextureAttachmentSpec = _GLFrameBuffer_FrameBufferTextureAttachmentSpec.FrameBufferTextureAttachmentSpec
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FrameBufferTextureAttachmentSpec():
    """com.badlogic.gdx.graphics.glutils.GLFrameBuffer.FrameBufferTextureAttachmentSpec"""
 
    @staticmethod
    def _wrap(java_value: _FrameBufferTextureAttachmentSpec) -> 'FrameBufferTextureAttachmentSpec':
        return FrameBufferTextureAttachmentSpec(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FrameBufferTextureAttachmentSpec):
        """
        Dynamic initializer for FrameBufferTextureAttachmentSpec.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FrameBufferTextureAttachmentSpec__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FrameBufferTextureAttachmentSpec__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def isColorTexture(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FrameBufferTextureAttachmentSpec.isColorTexture()"""
        return bool._wrap(super(FrameBufferTextureAttachmentSpec, self).isColorTexture())

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
    def __init__(self, arg0: int, arg1: int, arg2: int):
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FrameBufferTextureAttachmentSpec(int,int,int)"""
        val = _FrameBufferTextureAttachmentSpec(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))
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
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.VertexBufferObject
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.glutils.VertexBufferObject as _VertexBufferObject
_VertexBufferObject = _VertexBufferObject
from builtins import float
import java.nio.FloatBuffer as _FloatBuffer
_FloatBuffer = _FloatBuffer
import java.lang.String as _String
_String = _String
import java.nio.FloatBuffer as FloatBuffer
import com.badlogic.gdx.graphics.VertexAttributes as _VertexAttributes
_VertexAttributes = _VertexAttributes
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class VertexBufferObject():
    """com.badlogic.gdx.graphics.glutils.VertexBufferObject"""
 
    @staticmethod
    def _wrap(java_value: _VertexBufferObject) -> 'VertexBufferObject':
        return VertexBufferObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _VertexBufferObject):
        """
        Dynamic initializer for VertexBufferObject.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_VertexBufferObject__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_VertexBufferObject__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getBuffer(self) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.VertexBufferObject.getBuffer()"""
        return 'FloatBuffer'._wrap(super(VertexBufferObject, self).getBuffer())

    @override
    @overload
    def updateVertices(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObject.updateVertices(int,float[],int,int)"""
        super(_VertexBufferObject, self).updateVertices(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getNumVertices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.VertexBufferObject.getNumVertices()"""
        return int._wrap(super(VertexBufferObject, self).getNumVertices())

    @overload
    def getBuffer(self, arg0: bool) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.VertexBufferObject.getBuffer(boolean)"""
        return 'FloatBuffer'._wrap(super(_VertexBufferObject, self).getBuffer(_boolean.valueOf(arg0)))

    @override
    @overload
    def unbind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObject.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        super(_VertexBufferObject, self).unbind(arg0, arg1)

    @override
    @overload
    def setVertices(self, arg0: 'float', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObject.setVertices(float[],int,int)"""
        super(_VertexBufferObject, self).setVertices(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def unbind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObject.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(_VertexBufferObject, self).unbind(arg0)

    @override
    @overload
    def invalidate(self):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObject.invalidate()"""
        super(VertexBufferObject, self).invalidate()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObject.dispose()"""
        super(VertexBufferObject, self).dispose()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def bind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObject.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        super(_VertexBufferObject, self).bind(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def bind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.glutils.VertexBufferObject.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(_VertexBufferObject, self).bind(arg0)

    @overload
    def __init__(self, arg0: bool, arg1: int, arg2: 'VertexAttributes'):
        """public com.badlogic.gdx.graphics.glutils.VertexBufferObject(boolean,int,com.badlogic.gdx.graphics.VertexAttributes)"""
        val = _VertexBufferObject(_boolean.valueOf(arg0), _int.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: bool, arg1: int, *arg2: 'graphics.VertexAttribute'):
        """public com.badlogic.gdx.graphics.glutils.VertexBufferObject(boolean,int,com.badlogic.gdx.graphics.VertexAttribute...)"""
        val = _VertexBufferObject(_boolean.valueOf(arg0), _int.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def getNumMaxVertices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.VertexBufferObject.getNumMaxVertices()"""
        return int._wrap(super(VertexBufferObject, self).getNumMaxVertices())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getAttributes(self) -> 'graphics.VertexAttributes':
        """public com.badlogic.gdx.graphics.VertexAttributes com.badlogic.gdx.graphics.glutils.VertexBufferObject.getAttributes()"""
        return 'graphics.VertexAttributes'._wrap(super(VertexBufferObject, self).getAttributes())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.FrameBufferCubemap
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.glutils.FrameBufferCubemap as _FrameBufferCubemap
_FrameBufferCubemap = _FrameBufferCubemap
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.StringBuilder as _StringBuilder
_StringBuilder = _StringBuilder
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.glutils.GLFrameBuffer as _GLFrameBuffer
_GLFrameBuffer = _GLFrameBuffer
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.graphics.GLTexture as _GLTexture
_GLTexture = _GLTexture
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.Cubemap as _Cubemap_CubemapSide
_CubemapSide = _Cubemap_CubemapSide.CubemapSide
import java.lang.StringBuilder as StringBuilder
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FrameBufferCubemap():
    """com.badlogic.gdx.graphics.glutils.FrameBufferCubemap"""
 
    @staticmethod
    def _wrap(java_value: _FrameBufferCubemap) -> 'FrameBufferCubemap':
        return FrameBufferCubemap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FrameBufferCubemap):
        """
        Dynamic initializer for FrameBufferCubemap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FrameBufferCubemap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FrameBufferCubemap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def bind(self):
        """public void com.badlogic.gdx.graphics.glutils.FrameBufferCubemap.bind()"""
        super(FrameBufferCubemap, self).bind()

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getHeight()"""
        return int._wrap(super(GLFrameBuffer, self).getHeight())

    @override
    @overload
    def getStencilBufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getStencilBufferHandle()"""
        return int._wrap(super(GLFrameBuffer, self).getStencilBufferHandle())

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
    def getTextureAttachments(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getTextureAttachments()"""
        return 'utils.Array'._wrap(super(GLFrameBuffer, self).getTextureAttachments())

    @override
    @overload
    def getFramebufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getFramebufferHandle()"""
        return int._wrap(super(GLFrameBuffer, self).getFramebufferHandle())

    @override
    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.begin()"""
        super(GLFrameBuffer, self).begin()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def nextSide(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FrameBufferCubemap.nextSide()"""
        return bool._wrap(super(FrameBufferCubemap, self).nextSide())

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getWidth()"""
        return int._wrap(super(GLFrameBuffer, self).getWidth())

    @staticmethod
    @overload
    def clearAllFrameBuffers(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.clearAllFrameBuffers(com.badlogic.gdx.Application)"""
        _GLFrameBuffer.clearAllFrameBuffers(arg0)

    @override
    @overload
    def getDepthBufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getDepthBufferHandle()"""
        return int._wrap(super(GLFrameBuffer, self).getDepthBufferHandle())

        @staticmethod
        @overload
        def unbind():
            """public static void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.unbind()"""
            _GLFrameBuffer.unbind()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getManagedStatus(arg0: 'StringBuilder') -> 'StringBuilder':
        """public static java.lang.StringBuilder com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getManagedStatus(java.lang.StringBuilder)"""
        return StringBuilder._wrap(_GLFrameBuffer.getManagedStatus(arg0))

    @override
    @overload
    def end(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.end(int,int,int,int)"""
        super(_GLFrameBuffer, self).end(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def getManagedStatus() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getManagedStatus()"""
        return str._wrap(_GLFrameBuffer.getManagedStatus())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

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
        val = _FrameBufferCubemap(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3))
        self.__wrapper = val

    @overload
    def getSide(self) -> 'graphics.Cubemap$CubemapSide':
        """public com.badlogic.gdx.graphics.Cubemap$CubemapSide com.badlogic.gdx.graphics.glutils.FrameBufferCubemap.getSide()"""
        return 'graphics.Cubemap$CubemapSide'._wrap(super(FrameBufferCubemap, self).getSide())

    @overload
    def __init__(self, arg0: 'Format', arg1: int, arg2: int, arg3: bool, arg4: bool):
        """public com.badlogic.gdx.graphics.glutils.FrameBufferCubemap(com.badlogic.gdx.graphics.Pixmap$Format,int,int,boolean,boolean)"""
        val = _FrameBufferCubemap(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _boolean.valueOf(arg4))
        self.__wrapper = val

    @override
    @overload
    def getColorBufferTexture(self) -> 'graphics.GLTexture':
        """public T com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getColorBufferTexture()"""
        return 'graphics.GLTexture'._wrap(super(GLFrameBuffer, self).getColorBufferTexture())

    @staticmethod
    @overload
    def invalidateAllFrameBuffers(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.invalidateAllFrameBuffers(com.badlogic.gdx.Application)"""
        _GLFrameBuffer.invalidateAllFrameBuffers(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.glutils.GLFrameBuffer as _GLFrameBuffer_GLFrameBufferBuilder
_GLFrameBufferBuilder = _GLFrameBuffer_GLFrameBufferBuilder.GLFrameBufferBuilder
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFrameBufferBuilder():
    """com.badlogic.gdx.graphics.glutils.GLFrameBuffer.GLFrameBufferBuilder"""
 
    @staticmethod
    def _wrap(java_value: _GLFrameBufferBuilder) -> 'GLFrameBufferBuilder':
        return GLFrameBufferBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFrameBufferBuilder):
        """
        Dynamic initializer for GLFrameBufferBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFrameBufferBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFrameBufferBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addStencilTextureAttachment(self, arg0: int, arg1: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addStencilTextureAttachment(int,int)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addStencilTextureAttachment(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def addColorTextureAttachment(self, arg0: int, arg1: int, arg2: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addColorTextureAttachment(int,int,int)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addColorTextureAttachment(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def addStencilDepthPackedRenderBuffer(self, arg0: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addStencilDepthPackedRenderBuffer(int)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addStencilDepthPackedRenderBuffer(_int.valueOf(arg0)))

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
    def addBasicDepthRenderBuffer(self) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicDepthRenderBuffer()"""
        return 'GLFrameBufferBuilder'._wrap(super(GLFrameBufferBuilder, self).addBasicDepthRenderBuffer())

    @overload
    def addBasicStencilDepthPackedRenderBuffer(self) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicStencilDepthPackedRenderBuffer()"""
        return 'GLFrameBufferBuilder'._wrap(super(GLFrameBufferBuilder, self).addBasicStencilDepthPackedRenderBuffer())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def addDepthTextureAttachment(self, arg0: int, arg1: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addDepthTextureAttachment(int,int)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addDepthTextureAttachment(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def addDepthRenderBuffer(self, arg0: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addDepthRenderBuffer(int)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addDepthRenderBuffer(_int.valueOf(arg0)))

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

    @abstractmethod
    def build(self, ):
        """public abstract U com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.build()"""
        pass

    @overload
    def addStencilRenderBuffer(self, arg0: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addStencilRenderBuffer(int)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addStencilRenderBuffer(_int.valueOf(arg0)))

    @overload
    def addBasicStencilRenderBuffer(self) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicStencilRenderBuffer()"""
        return 'GLFrameBufferBuilder'._wrap(super(GLFrameBufferBuilder, self).addBasicStencilRenderBuffer())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def addFloatAttachment(self, arg0: int, arg1: int, arg2: int, arg3: bool) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addFloatAttachment(int,int,int,boolean)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addFloatAttachment(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder(int,int)"""
        val = _GLFrameBufferBuilder(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def addBasicColorTextureAttachment(self, arg0: 'Format') -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicColorTextureAttachment(com.badlogic.gdx.graphics.Pixmap$Format)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addBasicColorTextureAttachment(arg0))

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
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.PixmapTextureData
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.Pixmap as _Pixmap_Format
_Format = _Pixmap_Format.Format
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
import com.badlogic.gdx.graphics.glutils.PixmapTextureData as _PixmapTextureData
_PixmapTextureData = _PixmapTextureData
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.Pixmap as _Pixmap
_Pixmap = _Pixmap
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PixmapTextureData():
    """com.badlogic.gdx.graphics.glutils.PixmapTextureData"""
 
    @staticmethod
    def _wrap(java_value: _PixmapTextureData) -> 'PixmapTextureData':
        return PixmapTextureData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PixmapTextureData):
        """
        Dynamic initializer for PixmapTextureData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PixmapTextureData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PixmapTextureData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def consumeCustomData(self, arg0: int):
        """public void com.badlogic.gdx.graphics.glutils.PixmapTextureData.consumeCustomData(int)"""
        super(_PixmapTextureData, self).consumeCustomData(_int.valueOf(arg0))

    @override
    @overload
    def getType(self) -> 'graphics.TextureData$TextureDataType':
        """public com.badlogic.gdx.graphics.TextureData$TextureDataType com.badlogic.gdx.graphics.glutils.PixmapTextureData.getType()"""
        return 'graphics.TextureData$TextureDataType'._wrap(super(PixmapTextureData, self).getType())

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.PixmapTextureData.getHeight()"""
        return int._wrap(super(PixmapTextureData, self).getHeight())

    @override
    @overload
    def useMipMaps(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.PixmapTextureData.useMipMaps()"""
        return bool._wrap(super(PixmapTextureData, self).useMipMaps())

    @override
    @overload
    def getFormat(self) -> 'graphics.Pixmap$Format':
        """public com.badlogic.gdx.graphics.Pixmap$Format com.badlogic.gdx.graphics.glutils.PixmapTextureData.getFormat()"""
        return 'graphics.Pixmap$Format'._wrap(super(PixmapTextureData, self).getFormat())

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.PixmapTextureData.getWidth()"""
        return int._wrap(super(PixmapTextureData, self).getWidth())

    @override
    @overload
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.PixmapTextureData.isManaged()"""
        return bool._wrap(super(PixmapTextureData, self).isManaged())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isPrepared(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.PixmapTextureData.isPrepared()"""
        return bool._wrap(super(PixmapTextureData, self).isPrepared())

    @override
    @overload
    def consumePixmap(self) -> 'graphics.Pixmap':
        """public com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.graphics.glutils.PixmapTextureData.consumePixmap()"""
        return 'graphics.Pixmap'._wrap(super(PixmapTextureData, self).consumePixmap())

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
    def prepare(self):
        """public void com.badlogic.gdx.graphics.glutils.PixmapTextureData.prepare()"""
        super(PixmapTextureData, self).prepare()

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
    def __init__(self, arg0: 'Pixmap', arg1: 'Format', arg2: bool, arg3: bool):
        """public com.badlogic.gdx.graphics.glutils.PixmapTextureData(com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap$Format,boolean,boolean)"""
        val = _PixmapTextureData(arg0, arg1, _boolean.valueOf(arg2), _boolean.valueOf(arg3))
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
    def __init__(self, arg0: 'Pixmap', arg1: 'Format', arg2: bool, arg3: bool, arg4: bool):
        """public com.badlogic.gdx.graphics.glutils.PixmapTextureData(com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap$Format,boolean,boolean,boolean)"""
        val = _PixmapTextureData(arg0, arg1, _boolean.valueOf(arg2), _boolean.valueOf(arg3), _boolean.valueOf(arg4))
        self.__wrapper = val

    @override
    @overload
    def disposePixmap(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.PixmapTextureData.disposePixmap()"""
        return bool._wrap(super(PixmapTextureData, self).disposePixmap())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.GLVersion
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.glutils.GLVersion as _GLVersion_Type
_Type = _GLVersion_Type.Type
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.glutils.GLVersion as _GLVersion
_GLVersion = _GLVersion
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLVersion():
    """com.badlogic.gdx.graphics.glutils.GLVersion"""
 
    @staticmethod
    def _wrap(java_value: _GLVersion) -> 'GLVersion':
        return GLVersion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLVersion):
        """
        Dynamic initializer for GLVersion.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLVersion__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLVersion__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getMinorVersion(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLVersion.getMinorVersion()"""
        return int._wrap(super(GLVersion, self).getMinorVersion())

    @overload
    def getDebugVersionString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.glutils.GLVersion.getDebugVersionString()"""
        return str._wrap(super(GLVersion, self).getDebugVersionString())

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
    def getType(self) -> 'Type':
        """public com.badlogic.gdx.graphics.glutils.GLVersion$Type com.badlogic.gdx.graphics.glutils.GLVersion.getType()"""
        return 'Type'._wrap(super(GLVersion, self).getType())

    @overload
    def getMajorVersion(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLVersion.getMajorVersion()"""
        return int._wrap(super(GLVersion, self).getMajorVersion())

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
    def __init__(self, arg0: 'ApplicationType', arg1: str, arg2: str, arg3: str):
        """public com.badlogic.gdx.graphics.glutils.GLVersion(com.badlogic.gdx.Application$ApplicationType,java.lang.String,java.lang.String,java.lang.String)"""
        val = _GLVersion(arg0, arg1, arg2, arg3)
        self.__wrapper = val

    @overload
    def getVendorString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.glutils.GLVersion.getVendorString()"""
        return str._wrap(super(GLVersion, self).getVendorString())

    @overload
    def getRendererString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.glutils.GLVersion.getRendererString()"""
        return str._wrap(super(GLVersion, self).getRendererString())

    @overload
    def isVersionEqualToOrHigher(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.GLVersion.isVersionEqualToOrHigher(int,int)"""
        return bool._wrap(super(_GLVersion, self).isVersionEqualToOrHigher(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getReleaseVersion(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLVersion.getReleaseVersion()"""
        return int._wrap(super(GLVersion, self).getReleaseVersion())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.CustomTexture3DData
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.glutils.CustomTexture3DData as _CustomTexture3DData
_CustomTexture3DData = _CustomTexture3DData
import java.lang.Integer as _int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CustomTexture3DData():
    """com.badlogic.gdx.graphics.glutils.CustomTexture3DData"""
 
    @staticmethod
    def _wrap(java_value: _CustomTexture3DData) -> 'CustomTexture3DData':
        return CustomTexture3DData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CustomTexture3DData):
        """
        Dynamic initializer for CustomTexture3DData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CustomTexture3DData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CustomTexture3DData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.CustomTexture3DData.getWidth()"""
        return int._wrap(super(CustomTexture3DData, self).getWidth())

    @override
    @overload
    def useMipMaps(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.CustomTexture3DData.useMipMaps()"""
        return bool._wrap(super(CustomTexture3DData, self).useMipMaps())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getMipMapLevel(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.CustomTexture3DData.getMipMapLevel()"""
        return int._wrap(super(CustomTexture3DData, self).getMipMapLevel())

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
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.CustomTexture3DData.getHeight()"""
        return int._wrap(super(CustomTexture3DData, self).getHeight())

    @override
    @overload
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.CustomTexture3DData.isManaged()"""
        return bool._wrap(super(CustomTexture3DData, self).isManaged())

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
    def getDepth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.CustomTexture3DData.getDepth()"""
        return int._wrap(super(CustomTexture3DData, self).getDepth())

    @override
    @overload
    def getGLType(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.CustomTexture3DData.getGLType()"""
        return int._wrap(super(CustomTexture3DData, self).getGLType())

    @overload
    def getPixels(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.graphics.glutils.CustomTexture3DData.getPixels()"""
        return 'ByteBuffer'._wrap(super(CustomTexture3DData, self).getPixels())

    @overload
    def getGLFormat(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.CustomTexture3DData.getGLFormat()"""
        return int._wrap(super(CustomTexture3DData, self).getGLFormat())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getInternalFormat(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.CustomTexture3DData.getInternalFormat()"""
        return int._wrap(super(CustomTexture3DData, self).getInternalFormat())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def prepare(self):
        """public void com.badlogic.gdx.graphics.glutils.CustomTexture3DData.prepare()"""
        super(CustomTexture3DData, self).prepare()

    @override
    @overload
    def isPrepared(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.CustomTexture3DData.isPrepared()"""
        return bool._wrap(super(CustomTexture3DData, self).isPrepared())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public com.badlogic.gdx.graphics.glutils.CustomTexture3DData(int,int,int,int,int,int,int)"""
        val = _CustomTexture3DData(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6))
        self.__wrapper = val

    @override
    @overload
    def consume3DData(self):
        """public void com.badlogic.gdx.graphics.glutils.CustomTexture3DData.consume3DData()"""
        super(CustomTexture3DData, self).consume3DData()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.VertexArray
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.nio.FloatBuffer as _FloatBuffer
_FloatBuffer = _FloatBuffer
import java.lang.String as _String
_String = _String
import java.nio.FloatBuffer as FloatBuffer
import com.badlogic.gdx.graphics.VertexAttributes as _VertexAttributes
_VertexAttributes = _VertexAttributes
import com.badlogic.gdx.graphics.glutils.VertexArray as _VertexArray
_VertexArray = _VertexArray
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class VertexArray():
    """com.badlogic.gdx.graphics.glutils.VertexArray"""
 
    @staticmethod
    def _wrap(java_value: _VertexArray) -> 'VertexArray':
        return VertexArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _VertexArray):
        """
        Dynamic initializer for VertexArray.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_VertexArray__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_VertexArray__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def bind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public void com.badlogic.gdx.graphics.glutils.VertexArray.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        super(_VertexArray, self).bind(arg0, arg1)

    @override
    @overload
    def getBuffer(self) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.VertexArray.getBuffer()"""
        return 'FloatBuffer'._wrap(super(VertexArray, self).getBuffer())

    @override
    @overload
    def getAttributes(self) -> 'graphics.VertexAttributes':
        """public com.badlogic.gdx.graphics.VertexAttributes com.badlogic.gdx.graphics.glutils.VertexArray.getAttributes()"""
        return 'graphics.VertexAttributes'._wrap(super(VertexArray, self).getAttributes())

    @overload
    def __init__(self, arg0: int, arg1: 'VertexAttributes'):
        """public com.badlogic.gdx.graphics.glutils.VertexArray(int,com.badlogic.gdx.graphics.VertexAttributes)"""
        val = _VertexArray(_int.valueOf(arg0), arg1)
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

    @overload
    def __init__(self, arg0: int, *arg1: 'graphics.VertexAttribute'):
        """public com.badlogic.gdx.graphics.glutils.VertexArray(int,com.badlogic.gdx.graphics.VertexAttribute...)"""
        val = _VertexArray(_int.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def setVertices(self, arg0: 'float', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.VertexArray.setVertices(float[],int,int)"""
        super(_VertexArray, self).setVertices(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def getNumVertices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.VertexArray.getNumVertices()"""
        return int._wrap(super(VertexArray, self).getNumVertices())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getBuffer(self, arg0: bool) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.VertexArray.getBuffer(boolean)"""
        return 'FloatBuffer'._wrap(super(_VertexArray, self).getBuffer(_boolean.valueOf(arg0)))

    @override
    @overload
    def bind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.glutils.VertexArray.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(_VertexArray, self).bind(arg0)

    @override
    @overload
    def invalidate(self):
        """public void com.badlogic.gdx.graphics.glutils.VertexArray.invalidate()"""
        super(VertexArray, self).invalidate()

    @override
    @overload
    def updateVertices(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.VertexArray.updateVertices(int,float[],int,int)"""
        super(_VertexArray, self).updateVertices(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def unbind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public void com.badlogic.gdx.graphics.glutils.VertexArray.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        super(_VertexArray, self).unbind(arg0, arg1)

    @override
    @overload
    def getNumMaxVertices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.VertexArray.getNumMaxVertices()"""
        return int._wrap(super(VertexArray, self).getNumMaxVertices())

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
    def unbind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.glutils.VertexArray.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(_VertexArray, self).unbind(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.GLOnlyTextureData
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.Pixmap as _Pixmap_Format
_Format = _Pixmap_Format.Format
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
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.glutils.GLOnlyTextureData as _GLOnlyTextureData
_GLOnlyTextureData = _GLOnlyTextureData
import com.badlogic.gdx.graphics.Pixmap as _Pixmap
_Pixmap = _Pixmap
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLOnlyTextureData():
    """com.badlogic.gdx.graphics.glutils.GLOnlyTextureData"""
 
    @staticmethod
    def _wrap(java_value: _GLOnlyTextureData) -> 'GLOnlyTextureData':
        return GLOnlyTextureData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLOnlyTextureData):
        """
        Dynamic initializer for GLOnlyTextureData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLOnlyTextureData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLOnlyTextureData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def useMipMaps(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.GLOnlyTextureData.useMipMaps()"""
        return bool._wrap(super(GLOnlyTextureData, self).useMipMaps())

    @override
    @overload
    def consumeCustomData(self, arg0: int):
        """public void com.badlogic.gdx.graphics.glutils.GLOnlyTextureData.consumeCustomData(int)"""
        super(_GLOnlyTextureData, self).consumeCustomData(_int.valueOf(arg0))

    @override
    @overload
    def consumePixmap(self) -> 'graphics.Pixmap':
        """public com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.graphics.glutils.GLOnlyTextureData.consumePixmap()"""
        return 'graphics.Pixmap'._wrap(super(GLOnlyTextureData, self).consumePixmap())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public com.badlogic.gdx.graphics.glutils.GLOnlyTextureData(int,int,int,int,int,int)"""
        val = _GLOnlyTextureData(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))
        self.__wrapper = val

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLOnlyTextureData.getHeight()"""
        return int._wrap(super(GLOnlyTextureData, self).getHeight())

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
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.GLOnlyTextureData.isManaged()"""
        return bool._wrap(super(GLOnlyTextureData, self).isManaged())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getFormat(self) -> 'graphics.Pixmap$Format':
        """public com.badlogic.gdx.graphics.Pixmap$Format com.badlogic.gdx.graphics.glutils.GLOnlyTextureData.getFormat()"""
        return 'graphics.Pixmap$Format'._wrap(super(GLOnlyTextureData, self).getFormat())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def disposePixmap(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.GLOnlyTextureData.disposePixmap()"""
        return bool._wrap(super(GLOnlyTextureData, self).disposePixmap())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getType(self) -> 'graphics.TextureData$TextureDataType':
        """public com.badlogic.gdx.graphics.TextureData$TextureDataType com.badlogic.gdx.graphics.glutils.GLOnlyTextureData.getType()"""
        return 'graphics.TextureData$TextureDataType'._wrap(super(GLOnlyTextureData, self).getType())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isPrepared(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.GLOnlyTextureData.isPrepared()"""
        return bool._wrap(super(GLOnlyTextureData, self).isPrepared())

    @override
    @overload
    def prepare(self):
        """public void com.badlogic.gdx.graphics.glutils.GLOnlyTextureData.prepare()"""
        super(GLOnlyTextureData, self).prepare()

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLOnlyTextureData.getWidth()"""
        return int._wrap(super(GLOnlyTextureData, self).getWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.MipMapGenerator
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.glutils.MipMapGenerator as _MipMapGenerator
_MipMapGenerator = _MipMapGenerator
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MipMapGenerator():
    """com.badlogic.gdx.graphics.glutils.MipMapGenerator"""
 
    @staticmethod
    def _wrap(java_value: _MipMapGenerator) -> 'MipMapGenerator':
        return MipMapGenerator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MipMapGenerator):
        """
        Dynamic initializer for MipMapGenerator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MipMapGenerator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MipMapGenerator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def generateMipMap(arg0: 'Pixmap', arg1: int, arg2: int):
        """public static void com.badlogic.gdx.graphics.glutils.MipMapGenerator.generateMipMap(com.badlogic.gdx.graphics.Pixmap,int,int)"""
        _MipMapGenerator.generateMipMap(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def setUseHardwareMipMap(arg0: bool):
        """public static void com.badlogic.gdx.graphics.glutils.MipMapGenerator.setUseHardwareMipMap(boolean)"""
        _MipMapGenerator.setUseHardwareMipMap(_boolean.valueOf(arg0))

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

    @staticmethod
    @overload
    def generateMipMap(arg0: int, arg1: 'Pixmap', arg2: int, arg3: int):
        """public static void com.badlogic.gdx.graphics.glutils.MipMapGenerator.generateMipMap(int,com.badlogic.gdx.graphics.Pixmap,int,int)"""
        _MipMapGenerator.generateMipMap(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3))

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
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.InstanceBufferObject
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.nio.FloatBuffer as _FloatBuffer
_FloatBuffer = _FloatBuffer
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.glutils.InstanceBufferObject as _InstanceBufferObject
_InstanceBufferObject = _InstanceBufferObject
import java.nio.FloatBuffer as FloatBuffer
import com.badlogic.gdx.graphics.VertexAttributes as _VertexAttributes
_VertexAttributes = _VertexAttributes
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InstanceBufferObject():
    """com.badlogic.gdx.graphics.glutils.InstanceBufferObject"""
 
    @staticmethod
    def _wrap(java_value: _InstanceBufferObject) -> 'InstanceBufferObject':
        return InstanceBufferObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InstanceBufferObject):
        """
        Dynamic initializer for InstanceBufferObject.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InstanceBufferObject__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InstanceBufferObject__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def unbind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObject.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        super(_InstanceBufferObject, self).unbind(arg0, arg1)

    @override
    @overload
    def bind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObject.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(_InstanceBufferObject, self).bind(arg0)

    @override
    @overload
    def updateInstanceData(self, arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObject.updateInstanceData(int,float[],int,int)"""
        super(_InstanceBufferObject, self).updateInstanceData(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getNumMaxInstances(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.InstanceBufferObject.getNumMaxInstances()"""
        return int._wrap(super(InstanceBufferObject, self).getNumMaxInstances())

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
    def __init__(self, arg0: bool, arg1: int, *arg2: 'graphics.VertexAttribute'):
        """public com.badlogic.gdx.graphics.glutils.InstanceBufferObject(boolean,int,com.badlogic.gdx.graphics.VertexAttribute...)"""
        val = _InstanceBufferObject(_boolean.valueOf(arg0), _int.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def setInstanceData(self, arg0: 'float', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObject.setInstanceData(float[],int,int)"""
        super(_InstanceBufferObject, self).setInstanceData(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: bool, arg1: int, arg2: 'VertexAttributes'):
        """public com.badlogic.gdx.graphics.glutils.InstanceBufferObject(boolean,int,com.badlogic.gdx.graphics.VertexAttributes)"""
        val = _InstanceBufferObject(_boolean.valueOf(arg0), _int.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def updateInstanceData(self, arg0: int, arg1: 'FloatBuffer', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObject.updateInstanceData(int,java.nio.FloatBuffer,int,int)"""
        super(_InstanceBufferObject, self).updateInstanceData(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObject.dispose()"""
        super(InstanceBufferObject, self).dispose()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getBuffer(self) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.InstanceBufferObject.getBuffer()"""
        return 'FloatBuffer'._wrap(super(InstanceBufferObject, self).getBuffer())

    @override
    @overload
    def getAttributes(self) -> 'graphics.VertexAttributes':
        """public com.badlogic.gdx.graphics.VertexAttributes com.badlogic.gdx.graphics.glutils.InstanceBufferObject.getAttributes()"""
        return 'graphics.VertexAttributes'._wrap(super(InstanceBufferObject, self).getAttributes())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def bind(self, arg0: 'ShaderProgram', arg1: 'int'):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObject.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[])"""
        super(_InstanceBufferObject, self).bind(arg0, arg1)

    @overload
    def getBuffer(self, arg0: bool) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.InstanceBufferObject.getBuffer(boolean)"""
        return 'FloatBuffer'._wrap(super(_InstanceBufferObject, self).getBuffer(_boolean.valueOf(arg0)))

    @override
    @overload
    def invalidate(self):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObject.invalidate()"""
        super(InstanceBufferObject, self).invalidate()

    @override
    @overload
    def unbind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObject.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(_InstanceBufferObject, self).unbind(arg0)

    @override
    @overload
    def getNumInstances(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.InstanceBufferObject.getNumInstances()"""
        return int._wrap(super(InstanceBufferObject, self).getNumInstances())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setInstanceData(self, arg0: 'FloatBuffer', arg1: int):
        """public void com.badlogic.gdx.graphics.glutils.InstanceBufferObject.setInstanceData(java.nio.FloatBuffer,int)"""
        super(_InstanceBufferObject, self).setInstanceData(arg0, _int.valueOf(arg1))

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
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.ETC1
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.glutils.ETC1 as _ETC1
_ETC1 = _ETC1
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.Pixmap as _Pixmap
_Pixmap = _Pixmap
import java.nio.ByteBuffer as ByteBuffer
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.graphics.glutils.ETC1 as _ETC1_ETC1Data
_ETC1Data = _ETC1_ETC1Data.ETC1Data
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ETC1():
    """com.badlogic.gdx.graphics.glutils.ETC1"""
 
    @staticmethod
    def _wrap(java_value: _ETC1) -> 'ETC1':
        return ETC1(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ETC1):
        """
        Dynamic initializer for ETC1.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ETC1__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ETC1__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.glutils.ETC1()"""
        val = _ETC1()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.glutils.ETC1()"""
        val = _ETC1()
        self.__wrapper = val

    @staticmethod
    @overload
    def decodeImage(arg0: 'ETC1Data', arg1: 'Format') -> 'graphics.Pixmap':
        """public static com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.graphics.glutils.ETC1.decodeImage(com.badlogic.gdx.graphics.glutils.ETC1$ETC1Data,com.badlogic.gdx.graphics.Pixmap$Format)"""
        return graphics.Pixmap._wrap(_ETC1.decodeImage(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def formatHeader(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int):
        """public static native void com.badlogic.gdx.graphics.glutils.ETC1.formatHeader(java.nio.ByteBuffer,int,int,int)"""
        _ETC1.formatHeader(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

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

    @staticmethod
    @overload
    def encodeImagePKM(arg0: 'Pixmap') -> 'ETC1Data':
        """public static com.badlogic.gdx.graphics.glutils.ETC1$ETC1Data com.badlogic.gdx.graphics.glutils.ETC1.encodeImagePKM(com.badlogic.gdx.graphics.Pixmap)"""
        return ETC1Data._wrap(_ETC1.encodeImagePKM(arg0))

    @staticmethod
    @overload
    def getCompressedDataSize(arg0: int, arg1: int) -> int:
        """public static native int com.badlogic.gdx.graphics.glutils.ETC1.getCompressedDataSize(int,int)"""
        return int._wrap(_ETC1.getCompressedDataSize(_int.valueOf(arg0), _int.valueOf(arg1)))

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
    def encodeImage(arg0: 'Pixmap') -> 'ETC1Data':
        """public static com.badlogic.gdx.graphics.glutils.ETC1$ETC1Data com.badlogic.gdx.graphics.glutils.ETC1.encodeImage(com.badlogic.gdx.graphics.Pixmap)"""
        return ETC1Data._wrap(_ETC1.encodeImage(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.ETC1TextureData
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.Pixmap as _Pixmap_Format
_Format = _Pixmap_Format.Format
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
import java.lang.Boolean as _boolean
import com.badlogic.gdx.graphics.glutils.ETC1TextureData as _ETC1TextureData
_ETC1TextureData = _ETC1TextureData
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.Pixmap as _Pixmap
_Pixmap = _Pixmap
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ETC1TextureData():
    """com.badlogic.gdx.graphics.glutils.ETC1TextureData"""
 
    @staticmethod
    def _wrap(java_value: _ETC1TextureData) -> 'ETC1TextureData':
        return ETC1TextureData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ETC1TextureData):
        """
        Dynamic initializer for ETC1TextureData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ETC1TextureData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ETC1TextureData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def prepare(self):
        """public void com.badlogic.gdx.graphics.glutils.ETC1TextureData.prepare()"""
        super(ETC1TextureData, self).prepare()

    @override
    @overload
    def isPrepared(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.ETC1TextureData.isPrepared()"""
        return bool._wrap(super(ETC1TextureData, self).isPrepared())

    @override
    @overload
    def useMipMaps(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.ETC1TextureData.useMipMaps()"""
        return bool._wrap(super(ETC1TextureData, self).useMipMaps())

    @override
    @overload
    def consumePixmap(self) -> 'graphics.Pixmap':
        """public com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.graphics.glutils.ETC1TextureData.consumePixmap()"""
        return 'graphics.Pixmap'._wrap(super(ETC1TextureData, self).consumePixmap())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getType(self) -> 'graphics.TextureData$TextureDataType':
        """public com.badlogic.gdx.graphics.TextureData$TextureDataType com.badlogic.gdx.graphics.glutils.ETC1TextureData.getType()"""
        return 'graphics.TextureData$TextureDataType'._wrap(super(ETC1TextureData, self).getType())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ETC1TextureData.getWidth()"""
        return int._wrap(super(ETC1TextureData, self).getWidth())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'ETC1Data', arg1: bool):
        """public com.badlogic.gdx.graphics.glutils.ETC1TextureData(com.badlogic.gdx.graphics.glutils.ETC1$ETC1Data,boolean)"""
        val = _ETC1TextureData(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'FileHandle'):
        """public com.badlogic.gdx.graphics.glutils.ETC1TextureData(com.badlogic.gdx.files.FileHandle)"""
        val = _ETC1TextureData(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def consumeCustomData(self, arg0: int):
        """public void com.badlogic.gdx.graphics.glutils.ETC1TextureData.consumeCustomData(int)"""
        super(_ETC1TextureData, self).consumeCustomData(_int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def disposePixmap(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.ETC1TextureData.disposePixmap()"""
        return bool._wrap(super(ETC1TextureData, self).disposePixmap())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.ETC1TextureData.isManaged()"""
        return bool._wrap(super(ETC1TextureData, self).isManaged())

    @override
    @overload
    def getFormat(self) -> 'graphics.Pixmap$Format':
        """public com.badlogic.gdx.graphics.Pixmap$Format com.badlogic.gdx.graphics.glutils.ETC1TextureData.getFormat()"""
        return 'graphics.Pixmap$Format'._wrap(super(ETC1TextureData, self).getFormat())

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.ETC1TextureData.getHeight()"""
        return int._wrap(super(ETC1TextureData, self).getHeight())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: bool):
        """public com.badlogic.gdx.graphics.glutils.ETC1TextureData(com.badlogic.gdx.files.FileHandle,boolean)"""
        val = _ETC1TextureData(arg0, _boolean.valueOf(arg1))
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
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.FloatFrameBuffer
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.StringBuilder as _StringBuilder
_StringBuilder = _StringBuilder
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.glutils.FrameBuffer as _FrameBuffer
_FrameBuffer = _FrameBuffer
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.glutils.GLFrameBuffer as _GLFrameBuffer
_GLFrameBuffer = _GLFrameBuffer
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.graphics.GLTexture as _GLTexture
_GLTexture = _GLTexture
import java.lang.Boolean as _boolean
import com.badlogic.gdx.graphics.glutils.FloatFrameBuffer as _FloatFrameBuffer
_FloatFrameBuffer = _FloatFrameBuffer
import java.lang.Integer as _int
import java.lang.StringBuilder as StringBuilder
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FloatFrameBuffer():
    """com.badlogic.gdx.graphics.glutils.FloatFrameBuffer"""
 
    @staticmethod
    def _wrap(java_value: _FloatFrameBuffer) -> 'FloatFrameBuffer':
        return FloatFrameBuffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FloatFrameBuffer):
        """
        Dynamic initializer for FloatFrameBuffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FloatFrameBuffer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FloatFrameBuffer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
        @staticmethod
        @overload
        def unbind():
            """public static void com.badlogic.gdx.graphics.glutils.FrameBuffer.unbind()"""
            _FrameBuffer.unbind()

    @override
    @overload
    def bind(self):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.bind()"""
        super(GLFrameBuffer, self).bind()

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getHeight()"""
        return int._wrap(super(GLFrameBuffer, self).getHeight())

    @override
    @overload
    def getStencilBufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getStencilBufferHandle()"""
        return int._wrap(super(GLFrameBuffer, self).getStencilBufferHandle())

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
    def getTextureAttachments(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getTextureAttachments()"""
        return 'utils.Array'._wrap(super(GLFrameBuffer, self).getTextureAttachments())

    @override
    @overload
    def getFramebufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getFramebufferHandle()"""
        return int._wrap(super(GLFrameBuffer, self).getFramebufferHandle())

    @override
    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.begin()"""
        super(GLFrameBuffer, self).begin()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getWidth()"""
        return int._wrap(super(GLFrameBuffer, self).getWidth())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: bool):
        """public com.badlogic.gdx.graphics.glutils.FloatFrameBuffer(int,int,boolean)"""
        val = _FloatFrameBuffer(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2))
        self.__wrapper = val

    @staticmethod
    @overload
    def clearAllFrameBuffers(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.clearAllFrameBuffers(com.badlogic.gdx.Application)"""
        _GLFrameBuffer.clearAllFrameBuffers(arg0)

    @override
    @overload
    def getDepthBufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getDepthBufferHandle()"""
        return int._wrap(super(GLFrameBuffer, self).getDepthBufferHandle())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getManagedStatus(arg0: 'StringBuilder') -> 'StringBuilder':
        """public static java.lang.StringBuilder com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getManagedStatus(java.lang.StringBuilder)"""
        return StringBuilder._wrap(_GLFrameBuffer.getManagedStatus(arg0))

    @override
    @overload
    def end(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.end(int,int,int,int)"""
        super(_GLFrameBuffer, self).end(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def getManagedStatus() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getManagedStatus()"""
        return str._wrap(_GLFrameBuffer.getManagedStatus())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

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

    @override
    @overload
    def getColorBufferTexture(self) -> 'graphics.GLTexture':
        """public T com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getColorBufferTexture()"""
        return 'graphics.GLTexture'._wrap(super(GLFrameBuffer, self).getColorBufferTexture())

    @staticmethod
    @overload
    def invalidateAllFrameBuffers(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.invalidateAllFrameBuffers(com.badlogic.gdx.Application)"""
        _GLFrameBuffer.invalidateAllFrameBuffers(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.FloatTextureData
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.Pixmap as _Pixmap_Format
_Format = _Pixmap_Format.Format
import com.badlogic.gdx.graphics.TextureData as _TextureData_TextureDataType
_TextureDataType = _TextureData_TextureDataType.TextureDataType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.nio.FloatBuffer as _FloatBuffer
_FloatBuffer = _FloatBuffer
import java.lang.String as _String
_String = _String
import java.nio.FloatBuffer as FloatBuffer
import com.badlogic.gdx.graphics.glutils.FloatTextureData as _FloatTextureData
_FloatTextureData = _FloatTextureData
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.Pixmap as _Pixmap
_Pixmap = _Pixmap
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FloatTextureData():
    """com.badlogic.gdx.graphics.glutils.FloatTextureData"""
 
    @staticmethod
    def _wrap(java_value: _FloatTextureData) -> 'FloatTextureData':
        return FloatTextureData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FloatTextureData):
        """
        Dynamic initializer for FloatTextureData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FloatTextureData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FloatTextureData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FloatTextureData.isManaged()"""
        return bool._wrap(super(FloatTextureData, self).isManaged())

    @override
    @overload
    def disposePixmap(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FloatTextureData.disposePixmap()"""
        return bool._wrap(super(FloatTextureData, self).disposePixmap())

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
    def getBuffer(self) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.glutils.FloatTextureData.getBuffer()"""
        return 'FloatBuffer'._wrap(super(FloatTextureData, self).getBuffer())

    @override
    @overload
    def getType(self) -> 'graphics.TextureData$TextureDataType':
        """public com.badlogic.gdx.graphics.TextureData$TextureDataType com.badlogic.gdx.graphics.glutils.FloatTextureData.getType()"""
        return 'graphics.TextureData$TextureDataType'._wrap(super(FloatTextureData, self).getType())

    @override
    @overload
    def prepare(self):
        """public void com.badlogic.gdx.graphics.glutils.FloatTextureData.prepare()"""
        super(FloatTextureData, self).prepare()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def consumeCustomData(self, arg0: int):
        """public void com.badlogic.gdx.graphics.glutils.FloatTextureData.consumeCustomData(int)"""
        super(_FloatTextureData, self).consumeCustomData(_int.valueOf(arg0))

    @override
    @overload
    def isPrepared(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FloatTextureData.isPrepared()"""
        return bool._wrap(super(FloatTextureData, self).isPrepared())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool):
        """public com.badlogic.gdx.graphics.glutils.FloatTextureData(int,int,int,int,int,boolean)"""
        val = _FloatTextureData(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _boolean.valueOf(arg5))
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

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.FloatTextureData.getWidth()"""
        return int._wrap(super(FloatTextureData, self).getWidth())

    @override
    @overload
    def useMipMaps(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FloatTextureData.useMipMaps()"""
        return bool._wrap(super(FloatTextureData, self).useMipMaps())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def consumePixmap(self) -> 'graphics.Pixmap':
        """public com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.graphics.glutils.FloatTextureData.consumePixmap()"""
        return 'graphics.Pixmap'._wrap(super(FloatTextureData, self).consumePixmap())

    @override
    @overload
    def getFormat(self) -> 'graphics.Pixmap$Format':
        """public com.badlogic.gdx.graphics.Pixmap$Format com.badlogic.gdx.graphics.glutils.FloatTextureData.getFormat()"""
        return 'graphics.Pixmap$Format'._wrap(super(FloatTextureData, self).getFormat())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.FloatTextureData.getHeight()"""
        return int._wrap(super(FloatTextureData, self).getHeight())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.FrameBuffer
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.StringBuilder as _StringBuilder
_StringBuilder = _StringBuilder
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.glutils.FrameBuffer as _FrameBuffer
_FrameBuffer = _FrameBuffer
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.glutils.GLFrameBuffer as _GLFrameBuffer
_GLFrameBuffer = _GLFrameBuffer
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.graphics.GLTexture as _GLTexture
_GLTexture = _GLTexture
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.lang.StringBuilder as StringBuilder
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FrameBuffer():
    """com.badlogic.gdx.graphics.glutils.FrameBuffer"""
 
    @staticmethod
    def _wrap(java_value: _FrameBuffer) -> 'FrameBuffer':
        return FrameBuffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FrameBuffer):
        """
        Dynamic initializer for FrameBuffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FrameBuffer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FrameBuffer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
        @staticmethod
        @overload
        def unbind():
            """public static void com.badlogic.gdx.graphics.glutils.FrameBuffer.unbind()"""
            _FrameBuffer.unbind()

    @override
    @overload
    def bind(self):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.bind()"""
        super(GLFrameBuffer, self).bind()

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getHeight()"""
        return int._wrap(super(GLFrameBuffer, self).getHeight())

    @override
    @overload
    def getStencilBufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getStencilBufferHandle()"""
        return int._wrap(super(GLFrameBuffer, self).getStencilBufferHandle())

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
    def getTextureAttachments(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getTextureAttachments()"""
        return 'utils.Array'._wrap(super(GLFrameBuffer, self).getTextureAttachments())

    @override
    @overload
    def getFramebufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getFramebufferHandle()"""
        return int._wrap(super(GLFrameBuffer, self).getFramebufferHandle())

    @override
    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.begin()"""
        super(GLFrameBuffer, self).begin()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getWidth()"""
        return int._wrap(super(GLFrameBuffer, self).getWidth())

    @overload
    def __init__(self, arg0: 'Format', arg1: int, arg2: int, arg3: bool):
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer(com.badlogic.gdx.graphics.Pixmap$Format,int,int,boolean)"""
        val = _FrameBuffer(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3))
        self.__wrapper = val

    @staticmethod
    @overload
    def clearAllFrameBuffers(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.clearAllFrameBuffers(com.badlogic.gdx.Application)"""
        _GLFrameBuffer.clearAllFrameBuffers(arg0)

    @override
    @overload
    def getDepthBufferHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getDepthBufferHandle()"""
        return int._wrap(super(GLFrameBuffer, self).getDepthBufferHandle())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Format', arg1: int, arg2: int, arg3: bool, arg4: bool):
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer(com.badlogic.gdx.graphics.Pixmap$Format,int,int,boolean,boolean)"""
        val = _FrameBuffer(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _boolean.valueOf(arg4))
        self.__wrapper = val

    @staticmethod
    @overload
    def getManagedStatus(arg0: 'StringBuilder') -> 'StringBuilder':
        """public static java.lang.StringBuilder com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getManagedStatus(java.lang.StringBuilder)"""
        return StringBuilder._wrap(_GLFrameBuffer.getManagedStatus(arg0))

    @override
    @overload
    def end(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.end(int,int,int,int)"""
        super(_GLFrameBuffer, self).end(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def getManagedStatus() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getManagedStatus()"""
        return str._wrap(_GLFrameBuffer.getManagedStatus())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

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

    @override
    @overload
    def getColorBufferTexture(self) -> 'graphics.GLTexture':
        """public T com.badlogic.gdx.graphics.glutils.GLFrameBuffer.getColorBufferTexture()"""
        return 'graphics.GLTexture'._wrap(super(GLFrameBuffer, self).getColorBufferTexture())

    @staticmethod
    @overload
    def invalidateAllFrameBuffers(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.glutils.GLFrameBuffer.invalidateAllFrameBuffers(com.badlogic.gdx.Application)"""
        _GLFrameBuffer.invalidateAllFrameBuffers(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FrameBufferCubemapBuilder
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.glutils.FrameBufferCubemap as _FrameBufferCubemap
_FrameBufferCubemap = _FrameBufferCubemap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.glutils.GLFrameBuffer as _GLFrameBuffer_FrameBufferCubemapBuilder
_FrameBufferCubemapBuilder = _GLFrameBuffer_FrameBufferCubemapBuilder.FrameBufferCubemapBuilder
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.glutils.GLFrameBuffer as _GLFrameBuffer_GLFrameBufferBuilder
_GLFrameBufferBuilder = _GLFrameBuffer_GLFrameBufferBuilder.GLFrameBufferBuilder
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FrameBufferCubemapBuilder():
    """com.badlogic.gdx.graphics.glutils.GLFrameBuffer.FrameBufferCubemapBuilder"""
 
    @staticmethod
    def _wrap(java_value: _FrameBufferCubemapBuilder) -> 'FrameBufferCubemapBuilder':
        return FrameBufferCubemapBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FrameBufferCubemapBuilder):
        """
        Dynamic initializer for FrameBufferCubemapBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FrameBufferCubemapBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FrameBufferCubemapBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addStencilTextureAttachment(self, arg0: int, arg1: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addStencilTextureAttachment(int,int)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addStencilTextureAttachment(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def addColorTextureAttachment(self, arg0: int, arg1: int, arg2: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addColorTextureAttachment(int,int,int)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addColorTextureAttachment(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def build(self) -> 'FrameBufferCubemap':
        """public com.badlogic.gdx.graphics.glutils.FrameBufferCubemap com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FrameBufferCubemapBuilder.build()"""
        return 'FrameBufferCubemap'._wrap(super(FrameBufferCubemapBuilder, self).build())

    @overload
    def addStencilDepthPackedRenderBuffer(self, arg0: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addStencilDepthPackedRenderBuffer(int)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addStencilDepthPackedRenderBuffer(_int.valueOf(arg0)))

    @override
    @overload
    def addBasicStencilDepthPackedRenderBuffer(self) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicStencilDepthPackedRenderBuffer()"""
        return 'GLFrameBufferBuilder'._wrap(super(GLFrameBufferBuilder, self).addBasicStencilDepthPackedRenderBuffer())

    @override
    @overload
    def addBasicDepthRenderBuffer(self) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicDepthRenderBuffer()"""
        return 'GLFrameBufferBuilder'._wrap(super(GLFrameBufferBuilder, self).addBasicDepthRenderBuffer())

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

    @overload
    def addDepthTextureAttachment(self, arg0: int, arg1: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addDepthTextureAttachment(int,int)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addDepthTextureAttachment(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def addDepthRenderBuffer(self, arg0: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addDepthRenderBuffer(int)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addDepthRenderBuffer(_int.valueOf(arg0)))

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
    def addStencilRenderBuffer(self, arg0: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addStencilRenderBuffer(int)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addStencilRenderBuffer(_int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def addFloatAttachment(self, arg0: int, arg1: int, arg2: int, arg3: bool) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addFloatAttachment(int,int,int,boolean)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addFloatAttachment(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def addBasicColorTextureAttachment(self, arg0: 'Format') -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicColorTextureAttachment(com.badlogic.gdx.graphics.Pixmap$Format)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addBasicColorTextureAttachment(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def addBasicStencilRenderBuffer(self) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicStencilRenderBuffer()"""
        return 'GLFrameBufferBuilder'._wrap(super(GLFrameBufferBuilder, self).addBasicStencilRenderBuffer())

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
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FrameBufferCubemapBuilder(int,int)"""
        val = _FrameBufferCubemapBuilder(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.HdpiMode
from builtins import str
import com.badlogic.gdx.graphics.glutils.HdpiMode as _HdpiMode
_HdpiMode = _HdpiMode
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
 
class HdpiMode():
    """com.badlogic.gdx.graphics.glutils.HdpiMode"""
 
    @staticmethod
    def _wrap(java_value: _HdpiMode) -> 'HdpiMode':
        return HdpiMode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HdpiMode):
        """
        Dynamic initializer for HdpiMode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HdpiMode__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HdpiMode__wrapper":
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

    @staticmethod
    @overload
    def values() -> List['HdpiMode']:
        """public static com.badlogic.gdx.graphics.glutils.HdpiMode[] com.badlogic.gdx.graphics.glutils.HdpiMode.values()"""
        return List[HdpiMode]._wrap(_HdpiMode.values())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'HdpiMode':
        """public static com.badlogic.gdx.graphics.glutils.HdpiMode com.badlogic.gdx.graphics.glutils.HdpiMode.valueOf(java.lang.String)"""
        return HdpiMode._wrap(_HdpiMode.valueOf(arg0))

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
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.VertexData
import com.badlogic.gdx.graphics.glutils.VertexData as _VertexData
_VertexData = _VertexData
from builtins import float
from abc import abstractmethod, ABC
from builtins import int
 
class VertexData():
    """com.badlogic.gdx.graphics.glutils.VertexData"""
 
    @staticmethod
    def _wrap(java_value: _VertexData) -> 'VertexData':
        return VertexData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _VertexData):
        """
        Dynamic initializer for VertexData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_VertexData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_VertexData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
    def invalidate(self, ):
        """public abstract void com.badlogic.gdx.graphics.glutils.VertexData.invalidate()"""
        pass

    @abstractmethod
    def getNumVertices(self, ):
        """public abstract int com.badlogic.gdx.graphics.glutils.VertexData.getNumVertices()"""
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
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.FacedCubemapData
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
import com.badlogic.gdx.graphics.glutils.FacedCubemapData as _FacedCubemapData
_FacedCubemapData = _FacedCubemapData
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FacedCubemapData():
    """com.badlogic.gdx.graphics.glutils.FacedCubemapData"""
 
    @staticmethod
    def _wrap(java_value: _FacedCubemapData) -> 'FacedCubemapData':
        return FacedCubemapData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FacedCubemapData):
        """
        Dynamic initializer for FacedCubemapData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FacedCubemapData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FacedCubemapData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def consumeCubemapData(self):
        """public void com.badlogic.gdx.graphics.glutils.FacedCubemapData.consumeCubemapData()"""
        super(FacedCubemapData, self).consumeCubemapData()

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle', arg2: 'FileHandle', arg3: 'FileHandle', arg4: 'FileHandle', arg5: 'FileHandle'):
        """public com.badlogic.gdx.graphics.glutils.FacedCubemapData(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        val = _FacedCubemapData(arg0, arg1, arg2, arg3, arg4, arg5)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Pixmap', arg1: 'Pixmap', arg2: 'Pixmap', arg3: 'Pixmap', arg4: 'Pixmap', arg5: 'Pixmap', arg6: bool):
        """public com.badlogic.gdx.graphics.glutils.FacedCubemapData(com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,boolean)"""
        val = _FacedCubemapData(arg0, arg1, arg2, arg3, arg4, arg5, _boolean.valueOf(arg6))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: 'Format'):
        """public com.badlogic.gdx.graphics.glutils.FacedCubemapData(int,int,int,com.badlogic.gdx.graphics.Pixmap$Format)"""
        val = _FacedCubemapData(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.glutils.FacedCubemapData()"""
        val = _FacedCubemapData()
        self.__wrapper = val

    @overload
    def load(self, arg0: 'CubemapSide', arg1: 'Pixmap'):
        """public void com.badlogic.gdx.graphics.glutils.FacedCubemapData.load(com.badlogic.gdx.graphics.Cubemap$CubemapSide,com.badlogic.gdx.graphics.Pixmap)"""
        super(_FacedCubemapData, self).load(arg0, arg1)

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
    def prepare(self):
        """public void com.badlogic.gdx.graphics.glutils.FacedCubemapData.prepare()"""
        super(FacedCubemapData, self).prepare()

    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FacedCubemapData.isComplete()"""
        return bool._wrap(super(FacedCubemapData, self).isComplete())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getTextureData(self, arg0: 'CubemapSide') -> 'graphics.TextureData':
        """public com.badlogic.gdx.graphics.TextureData com.badlogic.gdx.graphics.glutils.FacedCubemapData.getTextureData(com.badlogic.gdx.graphics.Cubemap$CubemapSide)"""
        return 'graphics.TextureData'._wrap(super(_FacedCubemapData, self).getTextureData(arg0))

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle', arg2: 'FileHandle', arg3: 'FileHandle', arg4: 'FileHandle', arg5: 'FileHandle', arg6: bool):
        """public com.badlogic.gdx.graphics.glutils.FacedCubemapData(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,boolean)"""
        val = _FacedCubemapData(arg0, arg1, arg2, arg3, arg4, arg5, _boolean.valueOf(arg6))
        self.__wrapper = val

    @overload
    def load(self, arg0: 'CubemapSide', arg1: 'FileHandle'):
        """public void com.badlogic.gdx.graphics.glutils.FacedCubemapData.load(com.badlogic.gdx.graphics.Cubemap$CubemapSide,com.badlogic.gdx.files.FileHandle)"""
        super(_FacedCubemapData, self).load(arg0, arg1)

    @override
    @overload
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FacedCubemapData.isManaged()"""
        return bool._wrap(super(FacedCubemapData, self).isManaged())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.FacedCubemapData.getHeight()"""
        return int._wrap(super(FacedCubemapData, self).getHeight())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def isPrepared(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FacedCubemapData.isPrepared()"""
        return bool._wrap(super(FacedCubemapData, self).isPrepared())

    @overload
    def __init__(self, arg0: 'TextureData', arg1: 'TextureData', arg2: 'TextureData', arg3: 'TextureData', arg4: 'TextureData', arg5: 'TextureData'):
        """public com.badlogic.gdx.graphics.glutils.FacedCubemapData(com.badlogic.gdx.graphics.TextureData,com.badlogic.gdx.graphics.TextureData,com.badlogic.gdx.graphics.TextureData,com.badlogic.gdx.graphics.TextureData,com.badlogic.gdx.graphics.TextureData,com.badlogic.gdx.graphics.TextureData)"""
        val = _FacedCubemapData(arg0, arg1, arg2, arg3, arg4, arg5)
        self.__wrapper = val

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.FacedCubemapData.getWidth()"""
        return int._wrap(super(FacedCubemapData, self).getWidth())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.glutils.FacedCubemapData()"""
        val = _FacedCubemapData()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Pixmap', arg1: 'Pixmap', arg2: 'Pixmap', arg3: 'Pixmap', arg4: 'Pixmap', arg5: 'Pixmap'):
        """public com.badlogic.gdx.graphics.glutils.FacedCubemapData(com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap)"""
        val = _FacedCubemapData(arg0, arg1, arg2, arg3, arg4, arg5)
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.FileTextureArrayData
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.glutils.FileTextureArrayData as _FileTextureArrayData
_FileTextureArrayData = _FileTextureArrayData
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FileTextureArrayData():
    """com.badlogic.gdx.graphics.glutils.FileTextureArrayData"""
 
    @staticmethod
    def _wrap(java_value: _FileTextureArrayData) -> 'FileTextureArrayData':
        return FileTextureArrayData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FileTextureArrayData):
        """
        Dynamic initializer for FileTextureArrayData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FileTextureArrayData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FileTextureArrayData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getInternalFormat(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.FileTextureArrayData.getInternalFormat()"""
        return int._wrap(super(FileTextureArrayData, self).getInternalFormat())

    @override
    @overload
    def isPrepared(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FileTextureArrayData.isPrepared()"""
        return bool._wrap(super(FileTextureArrayData, self).isPrepared())

    @override
    @overload
    def getGLType(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.FileTextureArrayData.getGLType()"""
        return int._wrap(super(FileTextureArrayData, self).getGLType())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def prepare(self):
        """public void com.badlogic.gdx.graphics.glutils.FileTextureArrayData.prepare()"""
        super(FileTextureArrayData, self).prepare()

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.FileTextureArrayData.getHeight()"""
        return int._wrap(super(FileTextureArrayData, self).getHeight())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.FileTextureArrayData.getWidth()"""
        return int._wrap(super(FileTextureArrayData, self).getWidth())

    @overload
    def __init__(self, arg0: 'Format', arg1: bool, arg2: 'FileHandle'):
        """public com.badlogic.gdx.graphics.glutils.FileTextureArrayData(com.badlogic.gdx.graphics.Pixmap$Format,boolean,com.badlogic.gdx.files.FileHandle[])"""
        val = _FileTextureArrayData(arg0, _boolean.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getDepth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.FileTextureArrayData.getDepth()"""
        return int._wrap(super(FileTextureArrayData, self).getDepth())

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

    @override
    @overload
    def consumeTextureArrayData(self):
        """public void com.badlogic.gdx.graphics.glutils.FileTextureArrayData.consumeTextureArrayData()"""
        super(FileTextureArrayData, self).consumeTextureArrayData()

    @override
    @overload
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FileTextureArrayData.isManaged()"""
        return bool._wrap(super(FileTextureArrayData, self).isManaged())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FloatFrameBufferBuilder
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.glutils.GLFrameBuffer as _GLFrameBuffer_FloatFrameBufferBuilder
_FloatFrameBufferBuilder = _GLFrameBuffer_FloatFrameBufferBuilder.FloatFrameBufferBuilder
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import com.badlogic.gdx.graphics.glutils.FloatFrameBuffer as _FloatFrameBuffer
_FloatFrameBuffer = _FloatFrameBuffer
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.glutils.GLFrameBuffer as _GLFrameBuffer_GLFrameBufferBuilder
_GLFrameBufferBuilder = _GLFrameBuffer_GLFrameBufferBuilder.GLFrameBufferBuilder
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FloatFrameBufferBuilder():
    """com.badlogic.gdx.graphics.glutils.GLFrameBuffer.FloatFrameBufferBuilder"""
 
    @staticmethod
    def _wrap(java_value: _FloatFrameBufferBuilder) -> 'FloatFrameBufferBuilder':
        return FloatFrameBufferBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FloatFrameBufferBuilder):
        """
        Dynamic initializer for FloatFrameBufferBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FloatFrameBufferBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FloatFrameBufferBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addStencilTextureAttachment(self, arg0: int, arg1: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addStencilTextureAttachment(int,int)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addStencilTextureAttachment(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def addColorTextureAttachment(self, arg0: int, arg1: int, arg2: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addColorTextureAttachment(int,int,int)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addColorTextureAttachment(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def addStencilDepthPackedRenderBuffer(self, arg0: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addStencilDepthPackedRenderBuffer(int)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addStencilDepthPackedRenderBuffer(_int.valueOf(arg0)))

    @override
    @overload
    def addBasicStencilDepthPackedRenderBuffer(self) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicStencilDepthPackedRenderBuffer()"""
        return 'GLFrameBufferBuilder'._wrap(super(GLFrameBufferBuilder, self).addBasicStencilDepthPackedRenderBuffer())

    @override
    @overload
    def addBasicDepthRenderBuffer(self) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicDepthRenderBuffer()"""
        return 'GLFrameBufferBuilder'._wrap(super(GLFrameBufferBuilder, self).addBasicDepthRenderBuffer())

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
    def build(self) -> 'FloatFrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FloatFrameBuffer com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FloatFrameBufferBuilder.build()"""
        return 'FloatFrameBuffer'._wrap(super(FloatFrameBufferBuilder, self).build())

    @overload
    def addDepthTextureAttachment(self, arg0: int, arg1: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addDepthTextureAttachment(int,int)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addDepthTextureAttachment(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def addDepthRenderBuffer(self, arg0: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addDepthRenderBuffer(int)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addDepthRenderBuffer(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$FloatFrameBufferBuilder(int,int)"""
        val = _FloatFrameBufferBuilder(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def addStencilRenderBuffer(self, arg0: int) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addStencilRenderBuffer(int)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addStencilRenderBuffer(_int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def addFloatAttachment(self, arg0: int, arg1: int, arg2: int, arg3: bool) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addFloatAttachment(int,int,int,boolean)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addFloatAttachment(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def addBasicColorTextureAttachment(self, arg0: 'Format') -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicColorTextureAttachment(com.badlogic.gdx.graphics.Pixmap$Format)"""
        return 'GLFrameBufferBuilder'._wrap(super(_GLFrameBufferBuilder, self).addBasicColorTextureAttachment(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def addBasicStencilRenderBuffer(self) -> 'GLFrameBufferBuilder':
        """public com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder<U> com.badlogic.gdx.graphics.glutils.GLFrameBuffer$GLFrameBufferBuilder.addBasicStencilRenderBuffer()"""
        return 'GLFrameBufferBuilder'._wrap(super(GLFrameBufferBuilder, self).addBasicStencilRenderBuffer())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.IndexBufferObject
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.nio.ShortBuffer as ShortBuffer
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.glutils.IndexBufferObject as _IndexBufferObject
_IndexBufferObject = _IndexBufferObject
import java.nio.ShortBuffer as _ShortBuffer
_ShortBuffer = _ShortBuffer
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IndexBufferObject():
    """com.badlogic.gdx.graphics.glutils.IndexBufferObject"""
 
    @staticmethod
    def _wrap(java_value: _IndexBufferObject) -> 'IndexBufferObject':
        return IndexBufferObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IndexBufferObject):
        """
        Dynamic initializer for IndexBufferObject.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IndexBufferObject__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IndexBufferObject__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def unbind(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObject.unbind()"""
        super(IndexBufferObject, self).unbind()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def updateIndices(self, arg0: int, arg1: 'short', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObject.updateIndices(int,short[],int,int)"""
        super(_IndexBufferObject, self).updateIndices(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def setIndices(self, arg0: 'short', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObject.setIndices(short[],int,int)"""
        super(_IndexBufferObject, self).setIndices(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def getBuffer(self) -> 'ShortBuffer':
        """public java.nio.ShortBuffer com.badlogic.gdx.graphics.glutils.IndexBufferObject.getBuffer()"""
        return 'ShortBuffer'._wrap(super(IndexBufferObject, self).getBuffer())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: bool, arg1: 'ByteBuffer'):
        """public com.badlogic.gdx.graphics.glutils.IndexBufferObject(boolean,java.nio.ByteBuffer)"""
        val = _IndexBufferObject(_boolean.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def setIndices(self, arg0: 'ShortBuffer'):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObject.setIndices(java.nio.ShortBuffer)"""
        super(_IndexBufferObject, self).setIndices(arg0)

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObject.dispose()"""
        super(IndexBufferObject, self).dispose()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: bool, arg1: int):
        """public com.badlogic.gdx.graphics.glutils.IndexBufferObject(boolean,int)"""
        val = _IndexBufferObject(_boolean.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def getBuffer(self, arg0: bool) -> 'ShortBuffer':
        """public java.nio.ShortBuffer com.badlogic.gdx.graphics.glutils.IndexBufferObject.getBuffer(boolean)"""
        return 'ShortBuffer'._wrap(super(_IndexBufferObject, self).getBuffer(_boolean.valueOf(arg0)))

    @override
    @overload
    def getNumMaxIndices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.IndexBufferObject.getNumMaxIndices()"""
        return int._wrap(super(IndexBufferObject, self).getNumMaxIndices())

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
    def getNumIndices(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.IndexBufferObject.getNumIndices()"""
        return int._wrap(super(IndexBufferObject, self).getNumIndices())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def bind(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObject.bind()"""
        super(IndexBufferObject, self).bind()

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.glutils.IndexBufferObject(int)"""
        val = _IndexBufferObject(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def invalidate(self):
        """public void com.badlogic.gdx.graphics.glutils.IndexBufferObject.invalidate()"""
        super(IndexBufferObject, self).invalidate()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.FileTextureData
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.Pixmap as _Pixmap_Format
_Format = _Pixmap_Format.Format
from builtins import str
import com.badlogic.gdx.graphics.TextureData as _TextureData_TextureDataType
_TextureDataType = _TextureData_TextureDataType.TextureDataType
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.glutils.FileTextureData as _FileTextureData
_FileTextureData = _FileTextureData
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.Pixmap as _Pixmap
_Pixmap = _Pixmap
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FileTextureData():
    """com.badlogic.gdx.graphics.glutils.FileTextureData"""
 
    @staticmethod
    def _wrap(java_value: _FileTextureData) -> 'FileTextureData':
        return FileTextureData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FileTextureData):
        """
        Dynamic initializer for FileTextureData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FileTextureData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FileTextureData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def disposePixmap(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FileTextureData.disposePixmap()"""
        return bool._wrap(super(FileTextureData, self).disposePixmap())

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.FileTextureData.getWidth()"""
        return int._wrap(super(FileTextureData, self).getWidth())

    @override
    @overload
    def useMipMaps(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FileTextureData.useMipMaps()"""
        return bool._wrap(super(FileTextureData, self).useMipMaps())

    @override
    @overload
    def getFormat(self) -> 'graphics.Pixmap$Format':
        """public com.badlogic.gdx.graphics.Pixmap$Format com.badlogic.gdx.graphics.glutils.FileTextureData.getFormat()"""
        return 'graphics.Pixmap$Format'._wrap(super(FileTextureData, self).getFormat())

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'Pixmap', arg2: 'Format', arg3: bool):
        """public com.badlogic.gdx.graphics.glutils.FileTextureData(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap$Format,boolean)"""
        val = _FileTextureData(arg0, arg1, arg2, _boolean.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def consumePixmap(self) -> 'graphics.Pixmap':
        """public com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.graphics.glutils.FileTextureData.consumePixmap()"""
        return 'graphics.Pixmap'._wrap(super(FileTextureData, self).consumePixmap())

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
    def prepare(self):
        """public void com.badlogic.gdx.graphics.glutils.FileTextureData.prepare()"""
        super(FileTextureData, self).prepare()

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.glutils.FileTextureData.getHeight()"""
        return int._wrap(super(FileTextureData, self).getHeight())

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
    def getType(self) -> 'graphics.TextureData$TextureDataType':
        """public com.badlogic.gdx.graphics.TextureData$TextureDataType com.badlogic.gdx.graphics.glutils.FileTextureData.getType()"""
        return 'graphics.TextureData$TextureDataType'._wrap(super(FileTextureData, self).getType())

    @override
    @overload
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FileTextureData.isManaged()"""
        return bool._wrap(super(FileTextureData, self).isManaged())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getFileHandle(self) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.graphics.glutils.FileTextureData.getFileHandle()"""
        return 'files.FileHandle'._wrap(super(FileTextureData, self).getFileHandle())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.glutils.FileTextureData.toString()"""
        return str._wrap(super(FileTextureData, self).toString())

    @override
    @overload
    def consumeCustomData(self, arg0: int):
        """public void com.badlogic.gdx.graphics.glutils.FileTextureData.consumeCustomData(int)"""
        super(_FileTextureData, self).consumeCustomData(_int.valueOf(arg0))

    @override
    @overload
    def isPrepared(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.FileTextureData.isPrepared()"""
        return bool._wrap(super(FileTextureData, self).isPrepared())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.glutils.ShapeRenderer
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Matrix4 as _Matrix4
_Matrix4 = _Matrix4
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.graphics.glutils.ShapeRenderer as _ShapeRenderer
_ShapeRenderer = _ShapeRenderer
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.glutils.ShapeRenderer as _ShapeRenderer_ShapeType
_ShapeType = _ShapeRenderer_ShapeType.ShapeType
import com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer as _ImmediateModeRenderer
_ImmediateModeRenderer = _ImmediateModeRenderer
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ShapeRenderer():
    """com.badlogic.gdx.graphics.glutils.ShapeRenderer"""
 
    @staticmethod
    def _wrap(java_value: _ShapeRenderer) -> 'ShapeRenderer':
        return ShapeRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShapeRenderer):
        """
        Dynamic initializer for ShapeRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShapeRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShapeRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def triangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.triangle(float,float,float,float,float,float)"""
        super(_ShapeRenderer, self).triangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))

    @overload
    def rectLine(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.rectLine(float,float,float,float,float)"""
        super(_ShapeRenderer, self).rectLine(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def point(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.point(float,float,float)"""
        super(_ShapeRenderer, self).point(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def circle(self, arg0: float, arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.circle(float,float,float,int)"""
        super(_ShapeRenderer, self).circle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def arc(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.arc(float,float,float,float,float,int)"""
        super(_ShapeRenderer, self).arc(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isDrawing(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.glutils.ShapeRenderer.isDrawing()"""
        return bool._wrap(super(ShapeRenderer, self).isDrawing())

    @overload
    def getProjectionMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.glutils.ShapeRenderer.getProjectionMatrix()"""
        return 'math.Matrix4'._wrap(super(ShapeRenderer, self).getProjectionMatrix())

    @overload
    def identity(self):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.identity()"""
        super(ShapeRenderer, self).identity()

    @overload
    def getCurrentType(self) -> 'ShapeType':
        """public com.badlogic.gdx.graphics.glutils.ShapeRenderer$ShapeType com.badlogic.gdx.graphics.glutils.ShapeRenderer.getCurrentType()"""
        return 'ShapeType'._wrap(super(ShapeRenderer, self).getCurrentType())

    @overload
    def setAutoShapeType(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.setAutoShapeType(boolean)"""
        super(_ShapeRenderer, self).setAutoShapeType(_boolean.valueOf(arg0))

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
    def polyline(self, arg0: 'float', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.polyline(float[],int,int)"""
        super(_ShapeRenderer, self).polyline(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def __init__(self, arg0: int, arg1: 'ShaderProgram'):
        """public com.badlogic.gdx.graphics.glutils.ShapeRenderer(int,com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        val = _ShapeRenderer(_int.valueOf(arg0), arg1)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.glutils.ShapeRenderer()"""
        val = _ShapeRenderer()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.glutils.ShapeRenderer(int)"""
        val = _ShapeRenderer(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.setColor(float,float,float,float)"""
        super(_ShapeRenderer, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def rectLine(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'Color', arg6: 'Color'):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.rectLine(float,float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeRenderer, self).rectLine(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), arg5, arg6)

    @overload
    def rect(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: 'Color', arg10: 'Color', arg11: 'Color', arg12: 'Color'):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.rect(float,float,float,float,float,float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeRenderer, self).rect(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), arg9, arg10, arg11, arg12)

    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.ellipse(float,float,float,float)"""
        super(_ShapeRenderer, self).ellipse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def updateMatrices(self):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.updateMatrices()"""
        super(ShapeRenderer, self).updateMatrices()

    @overload
    def getTransformMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.glutils.ShapeRenderer.getTransformMatrix()"""
        return 'math.Matrix4'._wrap(super(ShapeRenderer, self).getTransformMatrix())

    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: int):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.ellipse(float,float,float,float,int)"""
        super(_ShapeRenderer, self).ellipse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4))

    @overload
    def triangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'Color', arg7: 'Color', arg8: 'Color'):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.triangle(float,float,float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeRenderer, self).triangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8)

    @overload
    def line(self, arg0: 'Vector2', arg1: 'Vector2'):
        """public final void com.badlogic.gdx.graphics.glutils.ShapeRenderer.line(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(_ShapeRenderer, self).line(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def polyline(self, arg0: 'float'):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.polyline(float[])"""
        super(_ShapeRenderer, self).polyline(arg0)

    @overload
    def rect(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: 'Color', arg6: 'Color', arg7: 'Color'):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.rect(float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeRenderer, self).rect(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4, arg5, arg6, arg7)

    @overload
    def polygon(self, arg0: 'float'):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.polygon(float[])"""
        super(_ShapeRenderer, self).polygon(arg0)

    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.ellipse(float,float,float,float,float,int)"""
        super(_ShapeRenderer, self).ellipse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5))

    @overload
    def translate(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.translate(float,float,float)"""
        super(_ShapeRenderer, self).translate(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'Color', arg7: 'Color'):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.line(float,float,float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeRenderer, self).line(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6, arg7)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.glutils.ShapeRenderer()"""
        val = _ShapeRenderer()
        self.__wrapper = val

    @overload
    def setProjectionMatrix(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.setProjectionMatrix(com.badlogic.gdx.math.Matrix4)"""
        super(_ShapeRenderer, self).setProjectionMatrix(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def rect(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.rect(float,float,float,float,float,float,float,float,float)"""
        super(_ShapeRenderer, self).rect(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8))

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public final void com.badlogic.gdx.graphics.glutils.ShapeRenderer.line(float,float,float,float,float,float)"""
        super(_ShapeRenderer, self).line(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))

    @overload
    def cone(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.cone(float,float,float,float,float)"""
        super(_ShapeRenderer, self).cone(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def rotate(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.rotate(float,float,float,float)"""
        super(_ShapeRenderer, self).rotate(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.ellipse(float,float,float,float,float)"""
        super(_ShapeRenderer, self).ellipse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def x(self, arg0: 'Vector2', arg1: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.x(com.badlogic.gdx.math.Vector2,float)"""
        super(_ShapeRenderer, self).x(arg0, _float.valueOf(arg1))

    @overload
    def set(self, arg0: 'ShapeType'):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.set(com.badlogic.gdx.graphics.glutils.ShapeRenderer$ShapeType)"""
        super(_ShapeRenderer, self).set(arg0)

    @overload
    def rectLine(self, arg0: 'Vector2', arg1: 'Vector2', arg2: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.rectLine(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,float)"""
        super(_ShapeRenderer, self).rectLine(arg0, arg1, _float.valueOf(arg2))

    @overload
    def arc(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.arc(float,float,float,float,float)"""
        super(_ShapeRenderer, self).arc(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.begin()"""
        super(ShapeRenderer, self).begin()

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public final void com.badlogic.gdx.graphics.glutils.ShapeRenderer.line(float,float,float,float)"""
        super(_ShapeRenderer, self).line(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def setTransformMatrix(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.setTransformMatrix(com.badlogic.gdx.math.Matrix4)"""
        super(_ShapeRenderer, self).setTransformMatrix(arg0)

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: 'Color'):
        """public final void com.badlogic.gdx.graphics.glutils.ShapeRenderer.line(float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeRenderer, self).line(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4, arg5)

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.dispose()"""
        super(ShapeRenderer, self).dispose()

    @overload
    def begin(self, arg0: 'ShapeType'):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.begin(com.badlogic.gdx.graphics.glutils.ShapeRenderer$ShapeType)"""
        super(_ShapeRenderer, self).begin(arg0)

    @overload
    def circle(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.circle(float,float,float)"""
        super(_ShapeRenderer, self).circle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def polygon(self, arg0: 'float', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.polygon(float[],int,int)"""
        super(_ShapeRenderer, self).polygon(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.glutils.ShapeRenderer.getColor()"""
        return 'graphics.Color'._wrap(super(ShapeRenderer, self).getColor())

    @overload
    def scale(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.scale(float,float,float)"""
        super(_ShapeRenderer, self).scale(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def getRenderer(self) -> 'ImmediateModeRenderer':
        """public com.badlogic.gdx.graphics.glutils.ImmediateModeRenderer com.badlogic.gdx.graphics.glutils.ShapeRenderer.getRenderer()"""
        return 'ImmediateModeRenderer'._wrap(super(ShapeRenderer, self).getRenderer())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def line(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public final void com.badlogic.gdx.graphics.glutils.ShapeRenderer.line(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(_ShapeRenderer, self).line(arg0, arg1)

    @overload
    def x(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.x(float,float,float)"""
        super(_ShapeRenderer, self).x(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_ShapeRenderer, self).setColor(arg0)

    @overload
    def curve(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: int):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.curve(float,float,float,float,float,float,float,float,int)"""
        super(_ShapeRenderer, self).curve(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _int.valueOf(arg8))

    @overload
    def rect(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.rect(float,float,float,float)"""
        super(_ShapeRenderer, self).rect(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def cone(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.cone(float,float,float,float,float,int)"""
        super(_ShapeRenderer, self).cone(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5))

    @overload
    def box(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void com.badlogic.gdx.graphics.glutils.ShapeRenderer.box(float,float,float,float,float,float)"""
        super(_ShapeRenderer, self).box(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))