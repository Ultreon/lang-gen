from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.math.FloatCounter as _FloatCounter
_FloatCounter = _FloatCounter
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.nio.IntBuffer as IntBuffer
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.profiling.GLInterceptor as _GLInterceptor
_GLInterceptor = _GLInterceptor
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.nio.Buffer as Buffer
import com.badlogic.gdx.graphics.profiling.GL20Interceptor as _GL20Interceptor
_GL20Interceptor = _GL20Interceptor
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GL20Interceptor():
    """com.badlogic.gdx.graphics.profiling.GL20Interceptor"""
 
    @staticmethod
    def _wrap(java_value: _GL20Interceptor) -> 'GL20Interceptor':
        return GL20Interceptor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GL20Interceptor):
        """
        Dynamic initializer for GL20Interceptor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GL20Interceptor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GL20Interceptor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getVertexCount(self) -> 'math.FloatCounter':
        """public com.badlogic.gdx.math.FloatCounter com.badlogic.gdx.graphics.profiling.GLInterceptor.getVertexCount()"""
        return 'math.FloatCounter'._wrap(super(GLInterceptor, self).getVertexCount())

    @override
    @overload
    def glVertexAttrib3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttrib3f(int,float,float,float)"""
        super(_GL20Interceptor, self).glVertexAttrib3f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def glGetProgramInfoLog(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetProgramInfoLog(int)"""
        return str._wrap(super(_GL20Interceptor, self).glGetProgramInfoLog(_int.valueOf(arg0)))

    @overload
    def glIsRenderbuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL20Interceptor.glIsRenderbuffer(int)"""
        return bool._wrap(super(_GL20Interceptor, self).glIsRenderbuffer(_int.valueOf(arg0)))

    @override
    @overload
    def glBindAttribLocation(self, arg0: int, arg1: int, arg2: str):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBindAttribLocation(int,int,java.lang.String)"""
        super(_GL20Interceptor, self).glBindAttribLocation(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glCompileShader(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCompileShader(int)"""
        super(_GL20Interceptor, self).glCompileShader(_int.valueOf(arg0))

    @override
    @overload
    def glStencilOpSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glStencilOpSeparate(int,int,int,int)"""
        super(_GL20Interceptor, self).glStencilOpSeparate(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glUseProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUseProgram(int)"""
        super(_GL20Interceptor, self).glUseProgram(_int.valueOf(arg0))

    @override
    @overload
    def glAttachShader(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glAttachShader(int,int)"""
        super(_GL20Interceptor, self).glAttachShader(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glBlendEquationSeparate(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBlendEquationSeparate(int,int)"""
        super(_GL20Interceptor, self).glBlendEquationSeparate(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glDeleteProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteProgram(int)"""
        super(_GL20Interceptor, self).glDeleteProgram(_int.valueOf(arg0))

    @override
    @overload
    def glFramebufferRenderbuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glFramebufferRenderbuffer(int,int,int,int)"""
        super(_GL20Interceptor, self).glFramebufferRenderbuffer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform4fv(int,int,float[],int)"""
        super(_GL20Interceptor, self).glUniform4fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glDeleteRenderbuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteRenderbuffer(int)"""
        super(_GL20Interceptor, self).glDeleteRenderbuffer(_int.valueOf(arg0))

    @override
    @overload
    def glGetVertexAttribPointerv(self, arg0: int, arg1: int, arg2: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetVertexAttribPointerv(int,int,java.nio.Buffer)"""
        super(_GL20Interceptor, self).glGetVertexAttribPointerv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glStencilFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glStencilFuncSeparate(int,int,int,int)"""
        super(_GL20Interceptor, self).glStencilFuncSeparate(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glVertexAttrib4fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttrib4fv(int,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glVertexAttrib4fv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glUniformMatrix2fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glVertexAttrib1f(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttrib1f(int,float)"""
        super(_GL20Interceptor, self).glVertexAttrib1f(_int.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def glDepthRangef(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDepthRangef(float,float)"""
        super(_GL20Interceptor, self).glDepthRangef(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def glClearStencil(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glClearStencil(int)"""
        super(_GL20Interceptor, self).glClearStencil(_int.valueOf(arg0))

    @override
    @overload
    def glBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBufferSubData(int,int,int,java.nio.Buffer)"""
        super(_GL20Interceptor, self).glBufferSubData(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def glGetError(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetError()"""
        return int._wrap(super(GL20Interceptor, self).glGetError())

    @override
    @overload
    def glGetIntegerv(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetIntegerv(int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGetIntegerv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glVertexAttrib2fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttrib2fv(int,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glVertexAttrib2fv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glGenRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenRenderbuffers(int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGenRenderbuffers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glEnableVertexAttribArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glEnableVertexAttribArray(int)"""
        super(_GL20Interceptor, self).glEnableVertexAttribArray(_int.valueOf(arg0))

    @override
    @overload
    def glDepthFunc(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDepthFunc(int)"""
        super(_GL20Interceptor, self).glDepthFunc(_int.valueOf(arg0))

    @override
    @overload
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttribPointer(int,int,int,boolean,int,int)"""
        super(_GL20Interceptor, self).glVertexAttribPointer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @override
    @overload
    def glSampleCoverage(self, arg0: float, arg1: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glSampleCoverage(float,boolean)"""
        super(_GL20Interceptor, self).glSampleCoverage(_float.valueOf(arg0), _boolean.valueOf(arg1))

    @override
    @overload
    def glGetAttachedShaders(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetAttachedShaders(int,int,java.nio.Buffer,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGetAttachedShaders(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform4iv(int,int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glUniform4iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def glBindTexture(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBindTexture(int,int)"""
        super(_GL20Interceptor, self).glBindTexture(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glActiveTexture(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glActiveTexture(int)"""
        super(_GL20Interceptor, self).glActiveTexture(_int.valueOf(arg0))

    @overload
    def glIsFramebuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL20Interceptor.glIsFramebuffer(int)"""
        return bool._wrap(super(_GL20Interceptor, self).glIsFramebuffer(_int.valueOf(arg0)))

    @override
    @overload
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform3fv(int,int,float[],int)"""
        super(_GL20Interceptor, self).glUniform3fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glTexParameterf(self, arg0: int, arg1: int, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glTexParameterf(int,int,float)"""
        super(_GL20Interceptor, self).glTexParameterf(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def glFlush(self):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glFlush()"""
        super(GL20Interceptor, self).glFlush()

    @override
    @overload
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform1iv(int,int,int[],int)"""
        super(_GL20Interceptor, self).glUniform1iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glBlendEquation(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBlendEquation(int)"""
        super(_GL20Interceptor, self).glBlendEquation(_int.valueOf(arg0))

    @override
    @overload
    def glShaderBinary(self, arg0: int, arg1: 'IntBuffer', arg2: int, arg3: 'Buffer', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glShaderBinary(int,java.nio.IntBuffer,int,java.nio.Buffer,int)"""
        super(_GL20Interceptor, self).glShaderBinary(_int.valueOf(arg0), arg1, _int.valueOf(arg2), arg3, _int.valueOf(arg4))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def glBlendFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBlendFuncSeparate(int,int,int,int)"""
        super(_GL20Interceptor, self).glBlendFuncSeparate(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glDeleteShader(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteShader(int)"""
        super(_GL20Interceptor, self).glDeleteShader(_int.valueOf(arg0))

    @override
    @overload
    def glGenerateMipmap(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenerateMipmap(int)"""
        super(_GL20Interceptor, self).glGenerateMipmap(_int.valueOf(arg0))

    @override
    @overload
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform2iv(int,int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glUniform2iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glBindRenderbuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBindRenderbuffer(int,int)"""
        super(_GL20Interceptor, self).glBindRenderbuffer(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glGenTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenTextures(int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGenTextures(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniform4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform4f(int,float,float,float,float)"""
        super(_GL20Interceptor, self).glUniform4f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def glGenFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenFramebuffers(int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGenFramebuffers(_int.valueOf(arg0), arg1)

    @overload
    def glIsProgram(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL20Interceptor.glIsProgram(int)"""
        return bool._wrap(super(_GL20Interceptor, self).glIsProgram(_int.valueOf(arg0)))

    @override
    @overload
    def glTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glTexParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glTexParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @overload
    def glGetActiveAttrib(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer') -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetActiveAttrib(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return str._wrap(super(_GL20Interceptor, self).glGetActiveAttrib(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3))

    @override
    @overload
    def glGetBufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetBufferParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGetBufferParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glRenderbufferStorage(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glRenderbufferStorage(int,int,int,int)"""
        super(_GL20Interceptor, self).glRenderbufferStorage(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glStencilMaskSeparate(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glStencilMaskSeparate(int,int)"""
        super(_GL20Interceptor, self).glStencilMaskSeparate(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glDisableVertexAttribArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDisableVertexAttribArray(int)"""
        super(_GL20Interceptor, self).glDisableVertexAttribArray(_int.valueOf(arg0))

    @override
    @overload
    def glLineWidth(self, arg0: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glLineWidth(float)"""
        super(_GL20Interceptor, self).glLineWidth(_float.valueOf(arg0))

    @override
    @overload
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform3iv(int,int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glUniform3iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGenBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenBuffers(int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGenBuffers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniformMatrix4fv(int,int,boolean,float[],int)"""
        super(_GL20Interceptor, self).glUniformMatrix4fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3, _int.valueOf(arg4))

    @override
    @overload
    def glValidateProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glValidateProgram(int)"""
        super(_GL20Interceptor, self).glValidateProgram(_int.valueOf(arg0))

    @overload
    def glGetUniformLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetUniformLocation(int,java.lang.String)"""
        return int._wrap(super(_GL20Interceptor, self).glGetUniformLocation(_int.valueOf(arg0), arg1))

    @override
    @overload
    def getDrawCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getDrawCalls()"""
        return int._wrap(super(GLInterceptor, self).getDrawCalls())

    @override
    @overload
    def glGetProgramiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetProgramiv(int,int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGetProgramiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def glGetString(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetString(int)"""
        return str._wrap(super(_GL20Interceptor, self).glGetString(_int.valueOf(arg0)))

    @override
    @overload
    def glGenRenderbuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenRenderbuffer()"""
        return int._wrap(super(GL20Interceptor, self).glGenRenderbuffer())

    @override
    @overload
    def glGetTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetTexParameterfv(int,int,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glGetTexParameterfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glCompressedTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCompressedTexImage2D(int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL20Interceptor, self).glCompressedTexImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), arg7)

    @override
    @overload
    def glCopyTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCopyTexImage2D(int,int,int,int,int,int,int,int)"""
        super(_GL20Interceptor, self).glCopyTexImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7))

    @override
    @overload
    def glStencilFunc(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glStencilFunc(int,int,int)"""
        super(_GL20Interceptor, self).glStencilFunc(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glReadPixels(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glReadPixels(int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL20Interceptor, self).glReadPixels(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), arg6)

    @override
    @overload
    def glVertexAttrib4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttrib4f(int,float,float,float,float)"""
        super(_GL20Interceptor, self).glVertexAttrib4f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def glDeleteFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteFramebuffers(int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glDeleteFramebuffers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glDisable(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDisable(int)"""
        super(_GL20Interceptor, self).glDisable(_int.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def glDeleteTexture(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteTexture(int)"""
        super(_GL20Interceptor, self).glDeleteTexture(_int.valueOf(arg0))

    @override
    @overload
    def glDeleteTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteTextures(int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glDeleteTextures(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glColorMask(self, arg0: bool, arg1: bool, arg2: bool, arg3: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glColorMask(boolean,boolean,boolean,boolean)"""
        super(_GL20Interceptor, self).glColorMask(_boolean.valueOf(arg0), _boolean.valueOf(arg1), _boolean.valueOf(arg2), _boolean.valueOf(arg3))

    @override
    @overload
    def glTexParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glTexParameteri(int,int,int)"""
        super(_GL20Interceptor, self).glTexParameteri(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glGetBooleanv(self, arg0: int, arg1: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetBooleanv(int,java.nio.Buffer)"""
        super(_GL20Interceptor, self).glGetBooleanv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glFrontFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glFrontFace(int)"""
        super(_GL20Interceptor, self).glFrontFace(_int.valueOf(arg0))

    @override
    @overload
    def glLinkProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glLinkProgram(int)"""
        super(_GL20Interceptor, self).glLinkProgram(_int.valueOf(arg0))

    @override
    @overload
    def glVertexAttrib1fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttrib1fv(int,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glVertexAttrib1fv(_int.valueOf(arg0), arg1)

    @overload
    def glCheckFramebufferStatus(self, arg0: int) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCheckFramebufferStatus(int)"""
        return int._wrap(super(_GL20Interceptor, self).glCheckFramebufferStatus(_int.valueOf(arg0)))

    @override
    @overload
    def glPixelStorei(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glPixelStorei(int,int)"""
        super(_GL20Interceptor, self).glPixelStorei(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glUniform2f(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform2f(int,float,float)"""
        super(_GL20Interceptor, self).glUniform2f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def glIsShader(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL20Interceptor.glIsShader(int)"""
        return bool._wrap(super(_GL20Interceptor, self).glIsShader(_int.valueOf(arg0)))

    @overload
    def glIsEnabled(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL20Interceptor.glIsEnabled(int)"""
        return bool._wrap(super(_GL20Interceptor, self).glIsEnabled(_int.valueOf(arg0)))

    @override
    @overload
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform1fv(int,int,float[],int)"""
        super(_GL20Interceptor, self).glUniform1fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def getCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getCalls()"""
        return int._wrap(super(GLInterceptor, self).getCalls())

    @override
    @overload
    def glReleaseShaderCompiler(self):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glReleaseShaderCompiler()"""
        super(GL20Interceptor, self).glReleaseShaderCompiler()

    @override
    @overload
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniformMatrix2fv(int,int,boolean,float[],int)"""
        super(_GL20Interceptor, self).glUniformMatrix2fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3, _int.valueOf(arg4))

    @overload
    def glIsTexture(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL20Interceptor.glIsTexture(int)"""
        return bool._wrap(super(_GL20Interceptor, self).glIsTexture(_int.valueOf(arg0)))

    @override
    @overload
    def glDepthMask(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDepthMask(boolean)"""
        super(_GL20Interceptor, self).glDepthMask(_boolean.valueOf(arg0))

    @override
    @overload
    def glViewport(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glViewport(int,int,int,int)"""
        super(_GL20Interceptor, self).glViewport(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glBlendColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBlendColor(float,float,float,float)"""
        super(_GL20Interceptor, self).glBlendColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform4fv(int,int,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glUniform4fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def getShaderSwitches(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getShaderSwitches()"""
        return int._wrap(super(GLInterceptor, self).getShaderSwitches())

    @override
    @overload
    def glStencilMask(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glStencilMask(int)"""
        super(_GL20Interceptor, self).glStencilMask(_int.valueOf(arg0))

    @override
    @overload
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glUniformMatrix4fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

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
    def glGenFramebuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenFramebuffer()"""
        return int._wrap(super(GL20Interceptor, self).glGenFramebuffer())

    @override
    @overload
    def glPolygonOffset(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glPolygonOffset(float,float)"""
        super(_GL20Interceptor, self).glPolygonOffset(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform1fv(int,int,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glUniform1fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glVertexAttrib2f(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttrib2f(int,float,float)"""
        super(_GL20Interceptor, self).glVertexAttrib2f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def glGetActiveUniform(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer') -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetActiveUniform(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return str._wrap(super(_GL20Interceptor, self).glGetActiveUniform(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3))

    @override
    @overload
    def glDeleteRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteRenderbuffers(int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glDeleteRenderbuffers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetVertexAttribfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetVertexAttribfv(int,int,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glGetVertexAttribfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteBuffers(int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glDeleteBuffers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniform3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform3f(int,float,float,float)"""
        super(_GL20Interceptor, self).glUniform3f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def glHint(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glHint(int,int)"""
        super(_GL20Interceptor, self).glHint(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDrawElements(int,int,int,int)"""
        super(_GL20Interceptor, self).glDrawElements(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glShaderSource(self, arg0: int, arg1: str):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glShaderSource(int,java.lang.String)"""
        super(_GL20Interceptor, self).glShaderSource(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform3i(int,int,int,int)"""
        super(_GL20Interceptor, self).glUniform3i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniformMatrix3fv(int,int,boolean,float[],int)"""
        super(_GL20Interceptor, self).glUniformMatrix3fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3, _int.valueOf(arg4))

    @override
    @overload
    def getTextureBindings(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getTextureBindings()"""
        return int._wrap(super(GLInterceptor, self).getTextureBindings())

    @override
    @overload
    def glDrawArrays(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDrawArrays(int,int,int)"""
        super(_GL20Interceptor, self).glDrawArrays(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glTexImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL20Interceptor, self).glTexImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), arg8)

    @override
    @overload
    def glGetTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetTexParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGetTexParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glCreateProgram(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCreateProgram()"""
        return int._wrap(super(GL20Interceptor, self).glCreateProgram())

    @override
    @overload
    def glFinish(self):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glFinish()"""
        super(GL20Interceptor, self).glFinish()

    @override
    @overload
    def glGetRenderbufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetRenderbufferParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGetRenderbufferParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDrawElements(int,int,int,java.nio.Buffer)"""
        super(_GL20Interceptor, self).glDrawElements(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def glTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glTexParameterfv(int,int,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glTexParameterfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteBuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteBuffer(int)"""
        super(_GL20Interceptor, self).glDeleteBuffer(_int.valueOf(arg0))

    @override
    @overload
    def glBindFramebuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBindFramebuffer(int,int)"""
        super(_GL20Interceptor, self).glBindFramebuffer(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glDeleteFramebuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteFramebuffer(int)"""
        super(_GL20Interceptor, self).glDeleteFramebuffer(_int.valueOf(arg0))

    @overload
    def glGetShaderInfoLog(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetShaderInfoLog(int)"""
        return str._wrap(super(_GL20Interceptor, self).glGetShaderInfoLog(_int.valueOf(arg0)))

    @overload
    def glCreateShader(self, arg0: int) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCreateShader(int)"""
        return int._wrap(super(_GL20Interceptor, self).glCreateShader(_int.valueOf(arg0)))

    @override
    @overload
    def glFramebufferTexture2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glFramebufferTexture2D(int,int,int,int,int)"""
        super(_GL20Interceptor, self).glFramebufferTexture2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform1iv(int,int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glUniform1iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glClear(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glClear(int)"""
        super(_GL20Interceptor, self).glClear(_int.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.profiling.GLInterceptor.reset()"""
        super(GLInterceptor, self).reset()

    @override
    @overload
    def glDetachShader(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDetachShader(int,int)"""
        super(_GL20Interceptor, self).glDetachShader(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glGetUniformiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetUniformiv(int,int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGetUniformiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glCullFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCullFace(int)"""
        super(_GL20Interceptor, self).glCullFace(_int.valueOf(arg0))

    @override
    @overload
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL20Interceptor, self).glTexSubImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), arg8)

    @override
    @overload
    def glUniform2i(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform2i(int,int,int)"""
        super(_GL20Interceptor, self).glUniform2i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform2iv(int,int,int[],int)"""
        super(_GL20Interceptor, self).glUniform2iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glClearColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glClearColor(float,float,float,float)"""
        super(_GL20Interceptor, self).glClearColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def glGetUniformfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetUniformfv(int,int,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glGetUniformfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glBlendFunc(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBlendFunc(int,int)"""
        super(_GL20Interceptor, self).glBlendFunc(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform2fv(int,int,float[],int)"""
        super(_GL20Interceptor, self).glUniform2fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glCompressedTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCompressedTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL20Interceptor, self).glCompressedTexSubImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), arg8)

    @override
    @overload
    def glUniform1i(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform1i(int,int)"""
        super(_GL20Interceptor, self).glUniform1i(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glGenTexture(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenTexture()"""
        return int._wrap(super(GL20Interceptor, self).glGenTexture())

    @override
    @overload
    def glEnable(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glEnable(int)"""
        super(_GL20Interceptor, self).glEnable(_int.valueOf(arg0))

    @override
    @overload
    def glGetVertexAttribiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetVertexAttribiv(int,int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGetVertexAttribiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform4i(int,int,int,int,int)"""
        super(_GL20Interceptor, self).glUniform4i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glGetFramebufferAttachmentParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetFramebufferAttachmentParameteriv(int,int,int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGetFramebufferAttachmentParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @overload
    def glGetAttribLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetAttribLocation(int,java.lang.String)"""
        return int._wrap(super(_GL20Interceptor, self).glGetAttribLocation(_int.valueOf(arg0), arg1))

    @override
    @overload
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform2fv(int,int,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glUniform2fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glBufferData(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBufferData(int,int,java.nio.Buffer,int)"""
        super(_GL20Interceptor, self).glBufferData(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform3iv(int,int,int[],int)"""
        super(_GL20Interceptor, self).glUniform3iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glGetFloatv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetFloatv(int,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glGetFloatv(_int.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def resolveErrorNumber(arg0: int) -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.profiling.GLInterceptor.resolveErrorNumber(int)"""
        return str._wrap(_GLInterceptor.resolveErrorNumber(_int.valueOf(arg0)))

    @override
    @overload
    def glScissor(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glScissor(int,int,int,int)"""
        super(_GL20Interceptor, self).glScissor(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glStencilOp(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glStencilOp(int,int,int)"""
        super(_GL20Interceptor, self).glStencilOp(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glGenBuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenBuffer()"""
        return int._wrap(super(GL20Interceptor, self).glGenBuffer())

    @overload
    def glIsBuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL20Interceptor.glIsBuffer(int)"""
        return bool._wrap(super(_GL20Interceptor, self).glIsBuffer(_int.valueOf(arg0)))

    @override
    @overload
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttribPointer(int,int,int,boolean,int,java.nio.Buffer)"""
        super(_GL20Interceptor, self).glVertexAttribPointer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), arg5)

    @override
    @overload
    def glClearDepthf(self, arg0: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glClearDepthf(float)"""
        super(_GL20Interceptor, self).glClearDepthf(_float.valueOf(arg0))

    @override
    @overload
    def glVertexAttrib3fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttrib3fv(int,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glVertexAttrib3fv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniform1f(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform1f(int,float)"""
        super(_GL20Interceptor, self).glUniform1f(_int.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform4iv(int,int,int[],int)"""
        super(_GL20Interceptor, self).glUniform4iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glGetShaderPrecisionFormat(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetShaderPrecisionFormat(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGetShaderPrecisionFormat(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform3fv(int,int,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glUniform3fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetShaderiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetShaderiv(int,int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGetShaderiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glUniformMatrix3fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glBindBuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBindBuffer(int,int)"""
        super(_GL20Interceptor, self).glBindBuffer(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glCopyTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCopyTexSubImage2D(int,int,int,int,int,int,int,int)"""
        super(_GL20Interceptor, self).glCopyTexSubImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7))

 
 
 
# CLASS: com.badlogic.gdx.graphics.profiling.GL20Interceptor
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.math.FloatCounter as _FloatCounter
_FloatCounter = _FloatCounter
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.nio.IntBuffer as IntBuffer
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.profiling.GLInterceptor as _GLInterceptor
_GLInterceptor = _GLInterceptor
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.nio.Buffer as Buffer
import com.badlogic.gdx.graphics.profiling.GL20Interceptor as _GL20Interceptor
_GL20Interceptor = _GL20Interceptor
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GL20Interceptor():
    """com.badlogic.gdx.graphics.profiling.GL20Interceptor"""
 
    @staticmethod
    def _wrap(java_value: _GL20Interceptor) -> 'GL20Interceptor':
        return GL20Interceptor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GL20Interceptor):
        """
        Dynamic initializer for GL20Interceptor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GL20Interceptor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GL20Interceptor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getVertexCount(self) -> 'math.FloatCounter':
        """public com.badlogic.gdx.math.FloatCounter com.badlogic.gdx.graphics.profiling.GLInterceptor.getVertexCount()"""
        return 'math.FloatCounter'._wrap(super(GLInterceptor, self).getVertexCount())

    @override
    @overload
    def glVertexAttrib3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttrib3f(int,float,float,float)"""
        super(_GL20Interceptor, self).glVertexAttrib3f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def glGetProgramInfoLog(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetProgramInfoLog(int)"""
        return str._wrap(super(_GL20Interceptor, self).glGetProgramInfoLog(_int.valueOf(arg0)))

    @overload
    def glIsRenderbuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL20Interceptor.glIsRenderbuffer(int)"""
        return bool._wrap(super(_GL20Interceptor, self).glIsRenderbuffer(_int.valueOf(arg0)))

    @override
    @overload
    def glBindAttribLocation(self, arg0: int, arg1: int, arg2: str):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBindAttribLocation(int,int,java.lang.String)"""
        super(_GL20Interceptor, self).glBindAttribLocation(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glCompileShader(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCompileShader(int)"""
        super(_GL20Interceptor, self).glCompileShader(_int.valueOf(arg0))

    @override
    @overload
    def glStencilOpSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glStencilOpSeparate(int,int,int,int)"""
        super(_GL20Interceptor, self).glStencilOpSeparate(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glUseProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUseProgram(int)"""
        super(_GL20Interceptor, self).glUseProgram(_int.valueOf(arg0))

    @override
    @overload
    def glAttachShader(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glAttachShader(int,int)"""
        super(_GL20Interceptor, self).glAttachShader(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glBlendEquationSeparate(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBlendEquationSeparate(int,int)"""
        super(_GL20Interceptor, self).glBlendEquationSeparate(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glDeleteProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteProgram(int)"""
        super(_GL20Interceptor, self).glDeleteProgram(_int.valueOf(arg0))

    @override
    @overload
    def glFramebufferRenderbuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glFramebufferRenderbuffer(int,int,int,int)"""
        super(_GL20Interceptor, self).glFramebufferRenderbuffer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform4fv(int,int,float[],int)"""
        super(_GL20Interceptor, self).glUniform4fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glDeleteRenderbuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteRenderbuffer(int)"""
        super(_GL20Interceptor, self).glDeleteRenderbuffer(_int.valueOf(arg0))

    @override
    @overload
    def glGetVertexAttribPointerv(self, arg0: int, arg1: int, arg2: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetVertexAttribPointerv(int,int,java.nio.Buffer)"""
        super(_GL20Interceptor, self).glGetVertexAttribPointerv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glStencilFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glStencilFuncSeparate(int,int,int,int)"""
        super(_GL20Interceptor, self).glStencilFuncSeparate(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glVertexAttrib4fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttrib4fv(int,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glVertexAttrib4fv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glUniformMatrix2fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glVertexAttrib1f(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttrib1f(int,float)"""
        super(_GL20Interceptor, self).glVertexAttrib1f(_int.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def glDepthRangef(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDepthRangef(float,float)"""
        super(_GL20Interceptor, self).glDepthRangef(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def glClearStencil(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glClearStencil(int)"""
        super(_GL20Interceptor, self).glClearStencil(_int.valueOf(arg0))

    @override
    @overload
    def glBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBufferSubData(int,int,int,java.nio.Buffer)"""
        super(_GL20Interceptor, self).glBufferSubData(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def glGetError(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetError()"""
        return int._wrap(super(GL20Interceptor, self).glGetError())

    @override
    @overload
    def glGetIntegerv(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetIntegerv(int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGetIntegerv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glVertexAttrib2fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttrib2fv(int,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glVertexAttrib2fv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glGenRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenRenderbuffers(int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGenRenderbuffers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glEnableVertexAttribArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glEnableVertexAttribArray(int)"""
        super(_GL20Interceptor, self).glEnableVertexAttribArray(_int.valueOf(arg0))

    @override
    @overload
    def glDepthFunc(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDepthFunc(int)"""
        super(_GL20Interceptor, self).glDepthFunc(_int.valueOf(arg0))

    @override
    @overload
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttribPointer(int,int,int,boolean,int,int)"""
        super(_GL20Interceptor, self).glVertexAttribPointer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @override
    @overload
    def glSampleCoverage(self, arg0: float, arg1: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glSampleCoverage(float,boolean)"""
        super(_GL20Interceptor, self).glSampleCoverage(_float.valueOf(arg0), _boolean.valueOf(arg1))

    @override
    @overload
    def glGetAttachedShaders(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetAttachedShaders(int,int,java.nio.Buffer,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGetAttachedShaders(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform4iv(int,int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glUniform4iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def glBindTexture(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBindTexture(int,int)"""
        super(_GL20Interceptor, self).glBindTexture(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glActiveTexture(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glActiveTexture(int)"""
        super(_GL20Interceptor, self).glActiveTexture(_int.valueOf(arg0))

    @overload
    def glIsFramebuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL20Interceptor.glIsFramebuffer(int)"""
        return bool._wrap(super(_GL20Interceptor, self).glIsFramebuffer(_int.valueOf(arg0)))

    @override
    @overload
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform3fv(int,int,float[],int)"""
        super(_GL20Interceptor, self).glUniform3fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glTexParameterf(self, arg0: int, arg1: int, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glTexParameterf(int,int,float)"""
        super(_GL20Interceptor, self).glTexParameterf(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def glFlush(self):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glFlush()"""
        super(GL20Interceptor, self).glFlush()

    @override
    @overload
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform1iv(int,int,int[],int)"""
        super(_GL20Interceptor, self).glUniform1iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glBlendEquation(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBlendEquation(int)"""
        super(_GL20Interceptor, self).glBlendEquation(_int.valueOf(arg0))

    @override
    @overload
    def glShaderBinary(self, arg0: int, arg1: 'IntBuffer', arg2: int, arg3: 'Buffer', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glShaderBinary(int,java.nio.IntBuffer,int,java.nio.Buffer,int)"""
        super(_GL20Interceptor, self).glShaderBinary(_int.valueOf(arg0), arg1, _int.valueOf(arg2), arg3, _int.valueOf(arg4))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def glBlendFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBlendFuncSeparate(int,int,int,int)"""
        super(_GL20Interceptor, self).glBlendFuncSeparate(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glDeleteShader(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteShader(int)"""
        super(_GL20Interceptor, self).glDeleteShader(_int.valueOf(arg0))

    @override
    @overload
    def glGenerateMipmap(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenerateMipmap(int)"""
        super(_GL20Interceptor, self).glGenerateMipmap(_int.valueOf(arg0))

    @override
    @overload
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform2iv(int,int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glUniform2iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glBindRenderbuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBindRenderbuffer(int,int)"""
        super(_GL20Interceptor, self).glBindRenderbuffer(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glGenTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenTextures(int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGenTextures(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniform4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform4f(int,float,float,float,float)"""
        super(_GL20Interceptor, self).glUniform4f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def glGenFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenFramebuffers(int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGenFramebuffers(_int.valueOf(arg0), arg1)

    @overload
    def glIsProgram(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL20Interceptor.glIsProgram(int)"""
        return bool._wrap(super(_GL20Interceptor, self).glIsProgram(_int.valueOf(arg0)))

    @override
    @overload
    def glTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glTexParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glTexParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @overload
    def glGetActiveAttrib(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer') -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetActiveAttrib(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return str._wrap(super(_GL20Interceptor, self).glGetActiveAttrib(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3))

    @override
    @overload
    def glGetBufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetBufferParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGetBufferParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glRenderbufferStorage(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glRenderbufferStorage(int,int,int,int)"""
        super(_GL20Interceptor, self).glRenderbufferStorage(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glStencilMaskSeparate(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glStencilMaskSeparate(int,int)"""
        super(_GL20Interceptor, self).glStencilMaskSeparate(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glDisableVertexAttribArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDisableVertexAttribArray(int)"""
        super(_GL20Interceptor, self).glDisableVertexAttribArray(_int.valueOf(arg0))

    @override
    @overload
    def glLineWidth(self, arg0: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glLineWidth(float)"""
        super(_GL20Interceptor, self).glLineWidth(_float.valueOf(arg0))

    @override
    @overload
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform3iv(int,int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glUniform3iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGenBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenBuffers(int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGenBuffers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniformMatrix4fv(int,int,boolean,float[],int)"""
        super(_GL20Interceptor, self).glUniformMatrix4fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3, _int.valueOf(arg4))

    @override
    @overload
    def glValidateProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glValidateProgram(int)"""
        super(_GL20Interceptor, self).glValidateProgram(_int.valueOf(arg0))

    @overload
    def glGetUniformLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetUniformLocation(int,java.lang.String)"""
        return int._wrap(super(_GL20Interceptor, self).glGetUniformLocation(_int.valueOf(arg0), arg1))

    @override
    @overload
    def getDrawCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getDrawCalls()"""
        return int._wrap(super(GLInterceptor, self).getDrawCalls())

    @override
    @overload
    def glGetProgramiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetProgramiv(int,int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGetProgramiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def glGetString(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetString(int)"""
        return str._wrap(super(_GL20Interceptor, self).glGetString(_int.valueOf(arg0)))

    @override
    @overload
    def glGenRenderbuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenRenderbuffer()"""
        return int._wrap(super(GL20Interceptor, self).glGenRenderbuffer())

    @override
    @overload
    def glGetTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetTexParameterfv(int,int,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glGetTexParameterfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glCompressedTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCompressedTexImage2D(int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL20Interceptor, self).glCompressedTexImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), arg7)

    @override
    @overload
    def glCopyTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCopyTexImage2D(int,int,int,int,int,int,int,int)"""
        super(_GL20Interceptor, self).glCopyTexImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7))

    @override
    @overload
    def glStencilFunc(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glStencilFunc(int,int,int)"""
        super(_GL20Interceptor, self).glStencilFunc(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glReadPixels(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glReadPixels(int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL20Interceptor, self).glReadPixels(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), arg6)

    @override
    @overload
    def glVertexAttrib4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttrib4f(int,float,float,float,float)"""
        super(_GL20Interceptor, self).glVertexAttrib4f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def glDeleteFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteFramebuffers(int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glDeleteFramebuffers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glDisable(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDisable(int)"""
        super(_GL20Interceptor, self).glDisable(_int.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def glDeleteTexture(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteTexture(int)"""
        super(_GL20Interceptor, self).glDeleteTexture(_int.valueOf(arg0))

    @override
    @overload
    def glDeleteTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteTextures(int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glDeleteTextures(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glColorMask(self, arg0: bool, arg1: bool, arg2: bool, arg3: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glColorMask(boolean,boolean,boolean,boolean)"""
        super(_GL20Interceptor, self).glColorMask(_boolean.valueOf(arg0), _boolean.valueOf(arg1), _boolean.valueOf(arg2), _boolean.valueOf(arg3))

    @override
    @overload
    def glTexParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glTexParameteri(int,int,int)"""
        super(_GL20Interceptor, self).glTexParameteri(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glGetBooleanv(self, arg0: int, arg1: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetBooleanv(int,java.nio.Buffer)"""
        super(_GL20Interceptor, self).glGetBooleanv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glFrontFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glFrontFace(int)"""
        super(_GL20Interceptor, self).glFrontFace(_int.valueOf(arg0))

    @override
    @overload
    def glLinkProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glLinkProgram(int)"""
        super(_GL20Interceptor, self).glLinkProgram(_int.valueOf(arg0))

    @override
    @overload
    def glVertexAttrib1fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttrib1fv(int,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glVertexAttrib1fv(_int.valueOf(arg0), arg1)

    @overload
    def glCheckFramebufferStatus(self, arg0: int) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCheckFramebufferStatus(int)"""
        return int._wrap(super(_GL20Interceptor, self).glCheckFramebufferStatus(_int.valueOf(arg0)))

    @override
    @overload
    def glPixelStorei(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glPixelStorei(int,int)"""
        super(_GL20Interceptor, self).glPixelStorei(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glUniform2f(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform2f(int,float,float)"""
        super(_GL20Interceptor, self).glUniform2f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def glIsShader(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL20Interceptor.glIsShader(int)"""
        return bool._wrap(super(_GL20Interceptor, self).glIsShader(_int.valueOf(arg0)))

    @overload
    def glIsEnabled(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL20Interceptor.glIsEnabled(int)"""
        return bool._wrap(super(_GL20Interceptor, self).glIsEnabled(_int.valueOf(arg0)))

    @override
    @overload
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform1fv(int,int,float[],int)"""
        super(_GL20Interceptor, self).glUniform1fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def getCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getCalls()"""
        return int._wrap(super(GLInterceptor, self).getCalls())

    @override
    @overload
    def glReleaseShaderCompiler(self):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glReleaseShaderCompiler()"""
        super(GL20Interceptor, self).glReleaseShaderCompiler()

    @override
    @overload
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniformMatrix2fv(int,int,boolean,float[],int)"""
        super(_GL20Interceptor, self).glUniformMatrix2fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3, _int.valueOf(arg4))

    @overload
    def glIsTexture(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL20Interceptor.glIsTexture(int)"""
        return bool._wrap(super(_GL20Interceptor, self).glIsTexture(_int.valueOf(arg0)))

    @override
    @overload
    def glDepthMask(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDepthMask(boolean)"""
        super(_GL20Interceptor, self).glDepthMask(_boolean.valueOf(arg0))

    @override
    @overload
    def glViewport(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glViewport(int,int,int,int)"""
        super(_GL20Interceptor, self).glViewport(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glBlendColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBlendColor(float,float,float,float)"""
        super(_GL20Interceptor, self).glBlendColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform4fv(int,int,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glUniform4fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def getShaderSwitches(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getShaderSwitches()"""
        return int._wrap(super(GLInterceptor, self).getShaderSwitches())

    @override
    @overload
    def glStencilMask(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glStencilMask(int)"""
        super(_GL20Interceptor, self).glStencilMask(_int.valueOf(arg0))

    @override
    @overload
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glUniformMatrix4fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

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
    def glGenFramebuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenFramebuffer()"""
        return int._wrap(super(GL20Interceptor, self).glGenFramebuffer())

    @override
    @overload
    def glPolygonOffset(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glPolygonOffset(float,float)"""
        super(_GL20Interceptor, self).glPolygonOffset(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform1fv(int,int,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glUniform1fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glVertexAttrib2f(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttrib2f(int,float,float)"""
        super(_GL20Interceptor, self).glVertexAttrib2f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def glGetActiveUniform(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer') -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetActiveUniform(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return str._wrap(super(_GL20Interceptor, self).glGetActiveUniform(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3))

    @override
    @overload
    def glDeleteRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteRenderbuffers(int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glDeleteRenderbuffers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetVertexAttribfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetVertexAttribfv(int,int,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glGetVertexAttribfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteBuffers(int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glDeleteBuffers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniform3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform3f(int,float,float,float)"""
        super(_GL20Interceptor, self).glUniform3f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def glHint(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glHint(int,int)"""
        super(_GL20Interceptor, self).glHint(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDrawElements(int,int,int,int)"""
        super(_GL20Interceptor, self).glDrawElements(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glShaderSource(self, arg0: int, arg1: str):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glShaderSource(int,java.lang.String)"""
        super(_GL20Interceptor, self).glShaderSource(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform3i(int,int,int,int)"""
        super(_GL20Interceptor, self).glUniform3i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniformMatrix3fv(int,int,boolean,float[],int)"""
        super(_GL20Interceptor, self).glUniformMatrix3fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3, _int.valueOf(arg4))

    @override
    @overload
    def getTextureBindings(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getTextureBindings()"""
        return int._wrap(super(GLInterceptor, self).getTextureBindings())

    @override
    @overload
    def glDrawArrays(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDrawArrays(int,int,int)"""
        super(_GL20Interceptor, self).glDrawArrays(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glTexImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL20Interceptor, self).glTexImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), arg8)

    @override
    @overload
    def glGetTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetTexParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGetTexParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glCreateProgram(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCreateProgram()"""
        return int._wrap(super(GL20Interceptor, self).glCreateProgram())

    @override
    @overload
    def glFinish(self):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glFinish()"""
        super(GL20Interceptor, self).glFinish()

    @override
    @overload
    def glGetRenderbufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetRenderbufferParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGetRenderbufferParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDrawElements(int,int,int,java.nio.Buffer)"""
        super(_GL20Interceptor, self).glDrawElements(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def glTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glTexParameterfv(int,int,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glTexParameterfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteBuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteBuffer(int)"""
        super(_GL20Interceptor, self).glDeleteBuffer(_int.valueOf(arg0))

    @override
    @overload
    def glBindFramebuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBindFramebuffer(int,int)"""
        super(_GL20Interceptor, self).glBindFramebuffer(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glDeleteFramebuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteFramebuffer(int)"""
        super(_GL20Interceptor, self).glDeleteFramebuffer(_int.valueOf(arg0))

    @overload
    def glGetShaderInfoLog(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetShaderInfoLog(int)"""
        return str._wrap(super(_GL20Interceptor, self).glGetShaderInfoLog(_int.valueOf(arg0)))

    @overload
    def glCreateShader(self, arg0: int) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCreateShader(int)"""
        return int._wrap(super(_GL20Interceptor, self).glCreateShader(_int.valueOf(arg0)))

    @override
    @overload
    def glFramebufferTexture2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glFramebufferTexture2D(int,int,int,int,int)"""
        super(_GL20Interceptor, self).glFramebufferTexture2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform1iv(int,int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glUniform1iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glClear(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glClear(int)"""
        super(_GL20Interceptor, self).glClear(_int.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.profiling.GLInterceptor.reset()"""
        super(GLInterceptor, self).reset()

    @override
    @overload
    def glDetachShader(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDetachShader(int,int)"""
        super(_GL20Interceptor, self).glDetachShader(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glGetUniformiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetUniformiv(int,int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGetUniformiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glCullFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCullFace(int)"""
        super(_GL20Interceptor, self).glCullFace(_int.valueOf(arg0))

    @override
    @overload
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL20Interceptor, self).glTexSubImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), arg8)

    @override
    @overload
    def glUniform2i(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform2i(int,int,int)"""
        super(_GL20Interceptor, self).glUniform2i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform2iv(int,int,int[],int)"""
        super(_GL20Interceptor, self).glUniform2iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glClearColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glClearColor(float,float,float,float)"""
        super(_GL20Interceptor, self).glClearColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def glGetUniformfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetUniformfv(int,int,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glGetUniformfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glBlendFunc(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBlendFunc(int,int)"""
        super(_GL20Interceptor, self).glBlendFunc(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform2fv(int,int,float[],int)"""
        super(_GL20Interceptor, self).glUniform2fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glCompressedTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCompressedTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL20Interceptor, self).glCompressedTexSubImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), arg8)

    @override
    @overload
    def glUniform1i(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform1i(int,int)"""
        super(_GL20Interceptor, self).glUniform1i(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glGenTexture(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenTexture()"""
        return int._wrap(super(GL20Interceptor, self).glGenTexture())

    @override
    @overload
    def glEnable(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glEnable(int)"""
        super(_GL20Interceptor, self).glEnable(_int.valueOf(arg0))

    @override
    @overload
    def glGetVertexAttribiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetVertexAttribiv(int,int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGetVertexAttribiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform4i(int,int,int,int,int)"""
        super(_GL20Interceptor, self).glUniform4i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glGetFramebufferAttachmentParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetFramebufferAttachmentParameteriv(int,int,int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGetFramebufferAttachmentParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @overload
    def glGetAttribLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetAttribLocation(int,java.lang.String)"""
        return int._wrap(super(_GL20Interceptor, self).glGetAttribLocation(_int.valueOf(arg0), arg1))

    @override
    @overload
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform2fv(int,int,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glUniform2fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glBufferData(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBufferData(int,int,java.nio.Buffer,int)"""
        super(_GL20Interceptor, self).glBufferData(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform3iv(int,int,int[],int)"""
        super(_GL20Interceptor, self).glUniform3iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glGetFloatv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetFloatv(int,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glGetFloatv(_int.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def resolveErrorNumber(arg0: int) -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.profiling.GLInterceptor.resolveErrorNumber(int)"""
        return str._wrap(_GLInterceptor.resolveErrorNumber(_int.valueOf(arg0)))

    @override
    @overload
    def glScissor(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glScissor(int,int,int,int)"""
        super(_GL20Interceptor, self).glScissor(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glStencilOp(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glStencilOp(int,int,int)"""
        super(_GL20Interceptor, self).glStencilOp(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glGenBuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenBuffer()"""
        return int._wrap(super(GL20Interceptor, self).glGenBuffer())

    @overload
    def glIsBuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL20Interceptor.glIsBuffer(int)"""
        return bool._wrap(super(_GL20Interceptor, self).glIsBuffer(_int.valueOf(arg0)))

    @override
    @overload
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttribPointer(int,int,int,boolean,int,java.nio.Buffer)"""
        super(_GL20Interceptor, self).glVertexAttribPointer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), arg5)

    @override
    @overload
    def glClearDepthf(self, arg0: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glClearDepthf(float)"""
        super(_GL20Interceptor, self).glClearDepthf(_float.valueOf(arg0))

    @override
    @overload
    def glVertexAttrib3fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttrib3fv(int,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glVertexAttrib3fv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniform1f(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform1f(int,float)"""
        super(_GL20Interceptor, self).glUniform1f(_int.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform4iv(int,int,int[],int)"""
        super(_GL20Interceptor, self).glUniform4iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glGetShaderPrecisionFormat(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetShaderPrecisionFormat(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGetShaderPrecisionFormat(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform3fv(int,int,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glUniform3fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetShaderiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetShaderiv(int,int,java.nio.IntBuffer)"""
        super(_GL20Interceptor, self).glGetShaderiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL20Interceptor, self).glUniformMatrix3fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glBindBuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBindBuffer(int,int)"""
        super(_GL20Interceptor, self).glBindBuffer(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glCopyTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCopyTexSubImage2D(int,int,int,int,int,int,int,int)"""
        super(_GL20Interceptor, self).glCopyTexSubImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7))

 
 
 
# CLASS: com.badlogic.gdx.graphics.profiling.GL20Interceptor 
 
 
# CLASS: com.badlogic.gdx.graphics.profiling.GL31Interceptor
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.FloatCounter as _FloatCounter
_FloatCounter = _FloatCounter
import java.lang.Object as _Object
_Object = _Object
import java.nio.IntBuffer as IntBuffer
from builtins import type
import com.badlogic.gdx.graphics.profiling.GL30Interceptor as _GL30Interceptor
_GL30Interceptor = _GL30Interceptor
import com.badlogic.gdx.graphics.profiling.GLInterceptor as _GLInterceptor
_GLInterceptor = _GLInterceptor
import java.nio.FloatBuffer as FloatBuffer
import java.lang.String as _string
import java.lang.Boolean as _boolean
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.nio.Buffer as _Buffer
_Buffer = _Buffer
from builtins import float
import java.nio.LongBuffer as LongBuffer
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import java.nio.Buffer as Buffer
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
import com.badlogic.gdx.graphics.profiling.GL31Interceptor as _GL31Interceptor
_GL31Interceptor = _GL31Interceptor
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GL31Interceptor():
    """com.badlogic.gdx.graphics.profiling.GL31Interceptor"""
 
    @staticmethod
    def _wrap(java_value: _GL31Interceptor) -> 'GL31Interceptor':
        return GL31Interceptor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GL31Interceptor):
        """
        Dynamic initializer for GL31Interceptor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GL31Interceptor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GL31Interceptor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def glIsBuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsBuffer(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsBuffer(_int.valueOf(arg0)))

    @override
    @overload
    def glCopyBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyBufferSubData(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glCopyBufferSubData(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glPauseTransformFeedback(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glPauseTransformFeedback()"""
        super(GL30Interceptor, self).glPauseTransformFeedback()

    @override
    @overload
    def getVertexCount(self) -> 'math.FloatCounter':
        """public com.badlogic.gdx.math.FloatCounter com.badlogic.gdx.graphics.profiling.GLInterceptor.getVertexCount()"""
        return 'math.FloatCounter'._wrap(super(GLInterceptor, self).getVertexCount())

    @override
    @overload
    def glDeleteSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteSamplers(int,int[],int)"""
        super(_GL30Interceptor, self).glDeleteSamplers(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def glUniform3uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3uiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glUniform3uiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDetachShader(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDetachShader(int,int)"""
        super(_GL30Interceptor, self).glDetachShader(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3fv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniform3fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGenSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenSamplers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGenSamplers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glDeleteVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteVertexArrays(int,int[],int)"""
        super(_GL30Interceptor, self).glDeleteVertexArrays(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def glGenVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenVertexArrays(int,int[],int)"""
        super(_GL30Interceptor, self).glGenVertexArrays(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def glClear(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClear(int)"""
        super(_GL30Interceptor, self).glClear(_int.valueOf(arg0))

    @override
    @overload
    def glUniform4uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4uiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glUniform4uiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteTexture(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTexture(int)"""
        super(_GL30Interceptor, self).glDeleteTexture(_int.valueOf(arg0))

    @override
    @overload
    def glDepthMask(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDepthMask(boolean)"""
        super(_GL30Interceptor, self).glDepthMask(_boolean.valueOf(arg0))

    @override
    @overload
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1fv(int,int,float[],int)"""
        super(_GL30Interceptor, self).glUniform1fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3i(int,int,int,int)"""
        super(_GL30Interceptor, self).glUniform3i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glDrawArraysIndirect(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glDrawArraysIndirect(int,long)"""
        super(_GL31Interceptor, self).glDrawArraysIndirect(_int.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def glGetQueryObjectuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetQueryObjectuiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetQueryObjectuiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glSamplerParameterfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glBindRenderbuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindRenderbuffer(int,int)"""
        super(_GL30Interceptor, self).glBindRenderbuffer(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glGetShaderiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetShaderiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetShaderiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glPixelStorei(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glPixelStorei(int,int)"""
        super(_GL30Interceptor, self).glPixelStorei(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glGetTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetTexParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetTexParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetVertexAttribIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribIuiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetVertexAttribIuiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glSamplerParameterf(self, arg0: int, arg1: int, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameterf(int,int,float)"""
        super(_GL30Interceptor, self).glSamplerParameterf(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glTexSubImage3D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), arg10)

    @override
    @overload
    def glProgramUniform2i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform2i(int,int,int,int)"""
        super(_GL31Interceptor, self).glProgramUniform2i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glDisable(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDisable(int)"""
        super(_GL30Interceptor, self).glDisable(_int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def glSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glSamplerParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glUseProgramStages(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glUseProgramStages(int,int,int)"""
        super(_GL31Interceptor, self).glUseProgramStages(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glUniform1uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1uiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glUniform1uiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDispatchComputeIndirect(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glDispatchComputeIndirect(long)"""
        super(_GL31Interceptor, self).glDispatchComputeIndirect(_long.valueOf(arg0))

    @override
    @overload
    def glDrawArraysInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawArraysInstanced(int,int,int,int)"""
        super(_GL30Interceptor, self).glDrawArraysInstanced(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glProgramUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform1iv(int,int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glProgramUniform1iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glProgramUniform3uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform3uiv(int,int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glProgramUniform3uiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glProgramUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform3fv(int,int,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glProgramUniform3fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @overload
    def glIsVertexArray(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsVertexArray(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsVertexArray(_int.valueOf(arg0)))

    @override
    @overload
    def glUniformMatrix4x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix4x2fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glColorMask(self, arg0: bool, arg1: bool, arg2: bool, arg3: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glColorMask(boolean,boolean,boolean,boolean)"""
        super(_GL30Interceptor, self).glColorMask(_boolean.valueOf(arg0), _boolean.valueOf(arg1), _boolean.valueOf(arg2), _boolean.valueOf(arg3))

    @override
    @overload
    def glPolygonOffset(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glPolygonOffset(float,float)"""
        super(_GL30Interceptor, self).glPolygonOffset(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def glProgramUniform1f(self, arg0: int, arg1: int, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform1f(int,int,float)"""
        super(_GL31Interceptor, self).glProgramUniform1f(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def glBlendFunc(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendFunc(int,int)"""
        super(_GL30Interceptor, self).glBlendFunc(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glShaderSource(self, arg0: int, arg1: str):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glShaderSource(int,java.lang.String)"""
        super(_GL30Interceptor, self).glShaderSource(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetUniformfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformfv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glGetUniformfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteSamplers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDeleteSamplers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def glUniformMatrix3x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix3x4fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @overload
    def glGetFragDataLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetFragDataLocation(int,java.lang.String)"""
        return int._wrap(super(_GL30Interceptor, self).glGetFragDataLocation(_int.valueOf(arg0), arg1))

    @override
    @overload
    def glClearBufferfi(self, arg0: int, arg1: int, arg2: float, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferfi(int,int,float,int)"""
        super(_GL30Interceptor, self).glClearBufferfi(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glUseProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUseProgram(int)"""
        super(_GL30Interceptor, self).glUseProgram(_int.valueOf(arg0))

    @override
    @overload
    def glUniformBlockBinding(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformBlockBinding(int,int,int)"""
        super(_GL30Interceptor, self).glUniformBlockBinding(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glCopyTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyTexImage2D(int,int,int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glCopyTexImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7))

    @override
    @overload
    def glViewport(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glViewport(int,int,int,int)"""
        super(_GL30Interceptor, self).glViewport(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glClearColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearColor(float,float,float,float)"""
        super(_GL30Interceptor, self).glClearColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def glGetProgramiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetProgramiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetProgramiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glProgramUniform2f(self, arg0: int, arg1: int, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform2f(int,int,float,float)"""
        super(_GL31Interceptor, self).glProgramUniform2f(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def glCreateProgram(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCreateProgram()"""
        return int._wrap(super(GL30Interceptor, self).glCreateProgram())

    @override
    @overload
    def glDeleteQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteQueries(int,int[],int)"""
        super(_GL30Interceptor, self).glDeleteQueries(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def glGetMultisamplefv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetMultisamplefv(int,int,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glGetMultisamplefv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glBindTexture(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindTexture(int,int)"""
        super(_GL30Interceptor, self).glBindTexture(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glGenVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenVertexArrays(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGenVertexArrays(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glVertexBindingDivisor(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glVertexBindingDivisor(int,int)"""
        super(_GL31Interceptor, self).glVertexBindingDivisor(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glProgramUniform4f(self, arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform4f(int,int,float,float,float,float)"""
        super(_GL31Interceptor, self).glProgramUniform4f(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))

    @override
    @overload
    def glValidateProgramPipeline(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glValidateProgramPipeline(int)"""
        super(_GL31Interceptor, self).glValidateProgramPipeline(_int.valueOf(arg0))

    @override
    @overload
    def glGetTexLevelParameterfv(self, arg0: int, arg1: int, arg2: int, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetTexLevelParameterfv(int,int,int,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glGetTexLevelParameterfv(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def glUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4i(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glUniform4i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage3D(int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glTexImage3D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), arg9)

    @override
    @overload
    def glGetError(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetError()"""
        return int._wrap(super(GL30Interceptor, self).glGetError())

    @override
    @overload
    def glDeleteProgramPipelines(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glDeleteProgramPipelines(int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glDeleteProgramPipelines(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glScissor(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glScissor(int,int,int,int)"""
        super(_GL30Interceptor, self).glScissor(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glGetShaderPrecisionFormat(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetShaderPrecisionFormat(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetShaderPrecisionFormat(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3)

    @overload
    def glGetActiveUniform(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer') -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniform(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return str._wrap(super(_GL30Interceptor, self).glGetActiveUniform(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3))

    @override
    @overload
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4fv(int,int,boolean,float[],int)"""
        super(_GL30Interceptor, self).glUniformMatrix4fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3, _int.valueOf(arg4))

    @override
    @overload
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix4fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glStencilMaskSeparate(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilMaskSeparate(int,int)"""
        super(_GL30Interceptor, self).glStencilMaskSeparate(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glVertexAttrib2f(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib2f(int,float,float)"""
        super(_GL30Interceptor, self).glVertexAttrib2f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def glBindVertexBuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glBindVertexBuffer(int,int,long,int)"""
        super(_GL31Interceptor, self).glBindVertexBuffer(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glSamplerParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameteri(int,int,int)"""
        super(_GL30Interceptor, self).glSamplerParameteri(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def __init__(self, arg0: 'GLProfiler', arg1: 'GL31'):
        """public com.badlogic.gdx.graphics.profiling.GL31Interceptor(com.badlogic.gdx.graphics.profiling.GLProfiler,com.badlogic.gdx.graphics.GL31)"""
        val = _GL31Interceptor(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def glGetBufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBufferParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetBufferParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glBlitFramebuffer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlitFramebuffer(int,int,int,int,int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glBlitFramebuffer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9))

    @override
    @overload
    def glBlendFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendFuncSeparate(int,int,int,int)"""
        super(_GL30Interceptor, self).glBlendFuncSeparate(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glTransformFeedbackVaryings(self, arg0: int, arg1: 'String', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTransformFeedbackVaryings(int,java.lang.String[],int)"""
        super(_GL30Interceptor, self).glTransformFeedbackVaryings(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def glGenRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenRenderbuffers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGenRenderbuffers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glBindVertexArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindVertexArray(int)"""
        super(_GL30Interceptor, self).glBindVertexArray(_int.valueOf(arg0))

    @override
    @overload
    def glProgramUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform2iv(int,int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glProgramUniform2iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glProgramUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform4fv(int,int,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glProgramUniform4fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glStencilFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilFuncSeparate(int,int,int,int)"""
        super(_GL30Interceptor, self).glStencilFuncSeparate(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glGenQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenQueries(int,int[],int)"""
        super(_GL30Interceptor, self).glGenQueries(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def glBindBufferBase(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindBufferBase(int,int,int)"""
        super(_GL30Interceptor, self).glBindBufferBase(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glProgramUniform3ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform3ui(int,int,int,int,int)"""
        super(_GL31Interceptor, self).glProgramUniform3ui(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def getCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getCalls()"""
        return int._wrap(super(GLInterceptor, self).getCalls())

    @overload
    def glIsTexture(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsTexture(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsTexture(_int.valueOf(arg0)))

    @override
    @overload
    def glGetActiveUniformBlockiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformBlockiv(int,int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetActiveUniformBlockiv(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def glEnable(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEnable(int)"""
        super(_GL30Interceptor, self).glEnable(_int.valueOf(arg0))

    @override
    @overload
    def glGenFramebuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenFramebuffer()"""
        return int._wrap(super(GL30Interceptor, self).glGenFramebuffer())

    @override
    @overload
    def glProgramUniform1i(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform1i(int,int,int)"""
        super(_GL31Interceptor, self).glProgramUniform1i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glTexParameterf(self, arg0: int, arg1: int, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameterf(int,int,float)"""
        super(_GL30Interceptor, self).glTexParameterf(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def glGetRenderbufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetRenderbufferParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetRenderbufferParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @overload
    def glIsEnabled(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsEnabled(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsEnabled(_int.valueOf(arg0)))

    @override
    @overload
    def getShaderSwitches(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getShaderSwitches()"""
        return int._wrap(super(GLInterceptor, self).getShaderSwitches())

    @override
    @overload
    def glBindProgramPipeline(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glBindProgramPipeline(int)"""
        super(_GL31Interceptor, self).glBindProgramPipeline(_int.valueOf(arg0))

    @override
    @overload
    def glCopyTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyTexSubImage3D(int,int,int,int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glCopyTexSubImage3D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def glGetIntegerv(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetIntegerv(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetIntegerv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glEnableVertexAttribArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEnableVertexAttribArray(int)"""
        super(_GL30Interceptor, self).glEnableVertexAttribArray(_int.valueOf(arg0))

    @override
    @overload
    def glReleaseShaderCompiler(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glReleaseShaderCompiler()"""
        super(GL30Interceptor, self).glReleaseShaderCompiler()

    @override
    @overload
    def glBlendEquation(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendEquation(int)"""
        super(_GL30Interceptor, self).glBlendEquation(_int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2fv(int,int,boolean,float[],int)"""
        super(_GL30Interceptor, self).glUniformMatrix2fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3, _int.valueOf(arg4))

    @override
    @overload
    def glVertexAttribIFormat(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glVertexAttribIFormat(int,int,int,int)"""
        super(_GL31Interceptor, self).glVertexAttribIFormat(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def glMapBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Buffer':
        """public java.nio.Buffer com.badlogic.gdx.graphics.profiling.GL30Interceptor.glMapBufferRange(int,int,int,int)"""
        return 'Buffer'._wrap(super(_GL30Interceptor, self).glMapBufferRange(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def glGetFramebufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetFramebufferParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glGetFramebufferParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDepthRangef(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDepthRangef(float,float)"""
        super(_GL30Interceptor, self).glDepthRangef(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def glBindTransformFeedback(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindTransformFeedback(int,int)"""
        super(_GL30Interceptor, self).glBindTransformFeedback(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glProgramUniform2ui(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform2ui(int,int,int,int)"""
        super(_GL31Interceptor, self).glProgramUniform2ui(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glActiveShaderProgram(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glActiveShaderProgram(int,int)"""
        super(_GL31Interceptor, self).glActiveShaderProgram(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glGetFloatv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetFloatv(int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glGetFloatv(_int.valueOf(arg0), arg1)

    @overload
    def glIsShader(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsShader(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsShader(_int.valueOf(arg0)))

    @override
    @overload
    def glResumeTransformFeedback(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glResumeTransformFeedback()"""
        super(GL30Interceptor, self).glResumeTransformFeedback()

    @override
    @overload
    def glProgramUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform2fv(int,int,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glProgramUniform2fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glProgramUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glProgramUniformMatrix3fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTransformFeedbacks(int,int[],int)"""
        super(_GL30Interceptor, self).glDeleteTransformFeedbacks(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def glEndTransformFeedback(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEndTransformFeedback()"""
        super(GL30Interceptor, self).glEndTransformFeedback()

    @override
    @overload
    def glBindBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindBufferRange(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glBindBufferRange(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glAttachShader(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glAttachShader(int,int)"""
        super(_GL30Interceptor, self).glAttachShader(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glCompileShader(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCompileShader(int)"""
        super(_GL30Interceptor, self).glCompileShader(_int.valueOf(arg0))

    @overload
    def glGetShaderInfoLog(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetShaderInfoLog(int)"""
        return str._wrap(super(_GL30Interceptor, self).glGetShaderInfoLog(_int.valueOf(arg0)))

    @overload
    def glGetAttribLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetAttribLocation(int,java.lang.String)"""
        return int._wrap(super(_GL30Interceptor, self).glGetAttribLocation(_int.valueOf(arg0), arg1))

    @overload
    def glIsRenderbuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsRenderbuffer(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsRenderbuffer(_int.valueOf(arg0)))

    @override
    @overload
    def glUniformMatrix2x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix2x3fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glTexStorage2DMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glTexStorage2DMultisample(int,int,int,int,int,boolean)"""
        super(_GL31Interceptor, self).glTexStorage2DMultisample(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _boolean.valueOf(arg5))

    @override
    @overload
    def glGetProgramInterfaceiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramInterfaceiv(int,int,int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glGetProgramInterfaceiv(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawElements(int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glDrawElements(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def glUniform4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4f(int,float,float,float,float)"""
        super(_GL30Interceptor, self).glUniform4f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def glGetProgramPipelineiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramPipelineiv(int,int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glGetProgramPipelineiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawElements(int,int,int,int)"""
        super(_GL30Interceptor, self).glDrawElements(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glDeleteFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteFramebuffers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDeleteFramebuffers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glRenderbufferStorage(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glRenderbufferStorage(int,int,int,int)"""
        super(_GL30Interceptor, self).glRenderbufferStorage(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.profiling.GLInterceptor.reset()"""
        super(GLInterceptor, self).reset()

    @override
    @overload
    def glDrawElementsInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawElementsInstanced(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glDrawElementsInstanced(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glFramebufferParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glFramebufferParameteri(int,int,int)"""
        super(_GL31Interceptor, self).glFramebufferParameteri(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage2D(int,int,int,int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glTexImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8))

    @override
    @overload
    def glDeleteFramebuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteFramebuffer(int)"""
        super(_GL30Interceptor, self).glDeleteFramebuffer(_int.valueOf(arg0))

    @override
    @overload
    def glGetActiveUniformsiv(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformsiv(int,int,java.nio.IntBuffer,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetActiveUniformsiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), arg4)

    @override
    @overload
    def glTexParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameteri(int,int,int)"""
        super(_GL30Interceptor, self).glTexParameteri(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix3fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glReadPixels(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glReadPixels(int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glReadPixels(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), arg6)

    @override
    @overload
    def glUniform2i(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2i(int,int,int)"""
        super(_GL30Interceptor, self).glUniform2i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2iv(int,int,int[],int)"""
        super(_GL30Interceptor, self).glUniform2iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glVertexAttribBinding(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glVertexAttribBinding(int,int)"""
        super(_GL31Interceptor, self).glVertexAttribBinding(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3fv(int,int,boolean,float[],int)"""
        super(_GL30Interceptor, self).glUniformMatrix3fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3, _int.valueOf(arg4))

    @override
    @overload
    def glUniform1f(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1f(int,float)"""
        super(_GL30Interceptor, self).glUniform1f(_int.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def glVertexAttrib3fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib3fv(int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glVertexAttrib3fv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTransformFeedbacks(int,int[],int)"""
        super(_GL30Interceptor, self).glGenTransformFeedbacks(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def glGetQueryiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetQueryiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetQueryiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetVertexAttribiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetVertexAttribiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4fv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniform4fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @overload
    def glIsFramebuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsFramebuffer(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsFramebuffer(_int.valueOf(arg0)))

    @override
    @overload
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribPointer(int,int,int,boolean,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glVertexAttribPointer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), arg5)

    @overload
    def glGetString(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetString(int)"""
        return str._wrap(super(_GL30Interceptor, self).glGetString(_int.valueOf(arg0)))

    @override
    @overload
    def glDeleteShader(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteShader(int)"""
        super(_GL30Interceptor, self).glDeleteShader(_int.valueOf(arg0))

    @override
    @overload
    def glSampleMaski(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glSampleMaski(int,int)"""
        super(_GL31Interceptor, self).glSampleMaski(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glClearBufferiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glClearBufferiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glVertexAttrib2fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib2fv(int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glVertexAttrib2fv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1iv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glUniform1iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4iv(int,int,int[],int)"""
        super(_GL30Interceptor, self).glUniform4iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @overload
    def glGetProgramResourceIndex(self, arg0: int, arg1: int, arg2: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramResourceIndex(int,int,java.lang.String)"""
        return int._wrap(super(_GL31Interceptor, self).glGetProgramResourceIndex(_int.valueOf(arg0), _int.valueOf(arg1), arg2))

    @overload
    def glGetUniformBlockIndex(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformBlockIndex(int,java.lang.String)"""
        return int._wrap(super(_GL30Interceptor, self).glGetUniformBlockIndex(_int.valueOf(arg0), arg1))

    @override
    @overload
    def glStencilOpSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilOpSeparate(int,int,int,int)"""
        super(_GL30Interceptor, self).glStencilOpSeparate(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glTexSubImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), arg8)

    @override
    @overload
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2fv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniform2fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribPointer(int,int,int,boolean,int,int)"""
        super(_GL30Interceptor, self).glVertexAttribPointer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @override
    @overload
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawRangeElements(int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glDrawRangeElements(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @override
    @overload
    def glVertexAttribI4ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribI4ui(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glVertexAttribI4ui(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glBindAttribLocation(self, arg0: int, arg1: int, arg2: str):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindAttribLocation(int,int,java.lang.String)"""
        super(_GL30Interceptor, self).glBindAttribLocation(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glMemoryBarrierByRegion(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glMemoryBarrierByRegion(int)"""
        super(_GL31Interceptor, self).glMemoryBarrierByRegion(_int.valueOf(arg0))

    @override
    @overload
    def glProgramUniformMatrix4x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix4x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glProgramUniformMatrix4x2fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glGetFramebufferAttachmentParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetFramebufferAttachmentParameteriv(int,int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetFramebufferAttachmentParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def glGetTexLevelParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetTexLevelParameteriv(int,int,int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glGetTexLevelParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def glFrontFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFrontFace(int)"""
        super(_GL30Interceptor, self).glFrontFace(_int.valueOf(arg0))

    @override
    @overload
    def glVertexAttribI4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribI4i(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glVertexAttribI4i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glCompressedTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCompressedTexImage2D(int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glCompressedTexImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), arg7)

    @override
    @overload
    def glGetBufferParameteri64v(self, arg0: int, arg1: int, arg2: 'LongBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBufferParameteri64v(int,int,java.nio.LongBuffer)"""
        super(_GL30Interceptor, self).glGetBufferParameteri64v(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteBuffers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDeleteBuffers(_int.valueOf(arg0), arg1)

    @overload
    def glIsTransformFeedback(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsTransformFeedback(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsTransformFeedback(_int.valueOf(arg0)))

    @override
    @overload
    def glDeleteTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTextures(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDeleteTextures(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glProgramUniform4ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform4ui(int,int,int,int,int,int)"""
        super(_GL31Interceptor, self).glProgramUniform4ui(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @override
    @overload
    def glFlush(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFlush()"""
        super(GL30Interceptor, self).glFlush()

    @override
    @overload
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix2fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glProgramUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform3iv(int,int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glProgramUniform3iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glTexSubImage3D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10))

    @override
    @overload
    def glCompressedTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCompressedTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glCompressedTexSubImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), arg8)

    @override
    @overload
    def glGetSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glGetSamplerParameterfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetBooleani_v(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetBooleani_v(int,int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glGetBooleani_v(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteRenderbuffers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDeleteRenderbuffers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glGenFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenFramebuffers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGenFramebuffers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glVertexAttrib1fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib1fv(int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glVertexAttrib1fv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glGenProgramPipelines(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGenProgramPipelines(int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glGenProgramPipelines(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glGenerateMipmap(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenerateMipmap(int)"""
        super(_GL30Interceptor, self).glGenerateMipmap(_int.valueOf(arg0))

    @override
    @overload
    def glGenBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenBuffers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGenBuffers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glFlushMappedBufferRange(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFlushMappedBufferRange(int,int,int)"""
        super(_GL30Interceptor, self).glFlushMappedBufferRange(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glClearDepthf(self, arg0: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearDepthf(float)"""
        super(_GL30Interceptor, self).glClearDepthf(_float.valueOf(arg0))

    @override
    @overload
    def glProgramUniformMatrix3x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix3x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glProgramUniformMatrix3x4fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def glRenderbufferStorageMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glRenderbufferStorageMultisample(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glRenderbufferStorageMultisample(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glUniform1i(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1i(int,int)"""
        super(_GL30Interceptor, self).glUniform1i(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glValidateProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glValidateProgram(int)"""
        super(_GL30Interceptor, self).glValidateProgram(_int.valueOf(arg0))

    @override
    @overload
    def glStencilOp(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilOp(int,int,int)"""
        super(_GL30Interceptor, self).glStencilOp(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glUniformMatrix2x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix2x4fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glCopyTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyTexSubImage2D(int,int,int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glCopyTexSubImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7))

    @override
    @overload
    def glLinkProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glLinkProgram(int)"""
        super(_GL30Interceptor, self).glLinkProgram(_int.valueOf(arg0))

    @override
    @overload
    def glDrawBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawBuffers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDrawBuffers(_int.valueOf(arg0), arg1)

    @overload
    def glUnmapBuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUnmapBuffer(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glUnmapBuffer(_int.valueOf(arg0)))

    @override
    @overload
    def glVertexAttribDivisor(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribDivisor(int,int)"""
        super(_GL30Interceptor, self).glVertexAttribDivisor(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glStencilFunc(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilFunc(int,int,int)"""
        super(_GL30Interceptor, self).glStencilFunc(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glProgramUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glProgramUniformMatrix2fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glGetUniformuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformuiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetUniformuiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glCullFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCullFace(int)"""
        super(_GL30Interceptor, self).glCullFace(_int.valueOf(arg0))

    @override
    @overload
    def glHint(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glHint(int,int)"""
        super(_GL30Interceptor, self).glHint(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glProgramParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glProgramParameteri(int,int,int)"""
        super(_GL30Interceptor, self).glProgramParameteri(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3iv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glUniform3iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glProgramUniform3f(self, arg0: int, arg1: int, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform3f(int,int,float,float,float)"""
        super(_GL31Interceptor, self).glProgramUniform3f(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def glCreateShader(self, arg0: int) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCreateShader(int)"""
        return int._wrap(super(_GL30Interceptor, self).glCreateShader(_int.valueOf(arg0)))

    @override
    @overload
    def glDeleteBuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteBuffer(int)"""
        super(_GL30Interceptor, self).glDeleteBuffer(_int.valueOf(arg0))

    @override
    @overload
    def glGetProgramResourceiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramResourceiv(int,int,int,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glGetProgramResourceiv(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, arg4, arg5)

    @override
    @overload
    def glBeginTransformFeedback(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBeginTransformFeedback(int)"""
        super(_GL30Interceptor, self).glBeginTransformFeedback(_int.valueOf(arg0))

    @override
    @overload
    def glClearBufferfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferfv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glClearBufferfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glProgramUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform1fv(int,int,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glProgramUniform1fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glActiveTexture(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glActiveTexture(int)"""
        super(_GL30Interceptor, self).glActiveTexture(_int.valueOf(arg0))

    @override
    @overload
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4iv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glUniform4iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteVertexArrays(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDeleteVertexArrays(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glVertexAttrib4fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib4fv(int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glVertexAttrib4fv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glBindBuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindBuffer(int,int)"""
        super(_GL30Interceptor, self).glBindBuffer(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def glGetProgramPipelineInfoLog(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramPipelineInfoLog(int)"""
        return str._wrap(super(_GL31Interceptor, self).glGetProgramPipelineInfoLog(_int.valueOf(arg0)))

    @override
    @overload
    def glVertexAttribIPointer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribIPointer(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glVertexAttribIPointer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @overload
    def glIsQuery(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsQuery(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsQuery(_int.valueOf(arg0)))

    @overload
    def glGetProgramResourceName(self, arg0: int, arg1: int, arg2: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramResourceName(int,int,int)"""
        return str._wrap(super(_GL31Interceptor, self).glGetProgramResourceName(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def glGenTexture(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTexture()"""
        return int._wrap(super(GL30Interceptor, self).glGenTexture())

    @overload
    def glGetProgramResourceLocation(self, arg0: int, arg1: int, arg2: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramResourceLocation(int,int,java.lang.String)"""
        return int._wrap(super(_GL31Interceptor, self).glGetProgramResourceLocation(_int.valueOf(arg0), _int.valueOf(arg1), arg2))

    @override
    @overload
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawRangeElements(int,int,int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glDrawRangeElements(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5)

    @override
    @overload
    def glBufferData(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBufferData(int,int,java.nio.Buffer,int)"""
        super(_GL30Interceptor, self).glBufferData(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def getDrawCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getDrawCalls()"""
        return int._wrap(super(GLInterceptor, self).getDrawCalls())

    @override
    @overload
    def glFinish(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFinish()"""
        super(GL30Interceptor, self).glFinish()

    @override
    @overload
    def glDeleteRenderbuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteRenderbuffer(int)"""
        super(_GL30Interceptor, self).glDeleteRenderbuffer(_int.valueOf(arg0))

    @override
    @overload
    def glVertexAttrib1f(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib1f(int,float)"""
        super(_GL30Interceptor, self).glVertexAttrib1f(_int.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def glBindImageTexture(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glBindImageTexture(int,int,int,boolean,int,int,int)"""
        super(_GL31Interceptor, self).glBindImageTexture(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6))

    @overload
    def glIsSampler(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsSampler(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsSampler(_int.valueOf(arg0)))

    @override
    @overload
    def glDrawElementsIndirect(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glDrawElementsIndirect(int,int,long)"""
        super(_GL31Interceptor, self).glDrawElementsIndirect(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2))

    @override
    @overload
    def glInvalidateFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glInvalidateFramebuffer(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glInvalidateFramebuffer(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glLineWidth(self, arg0: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glLineWidth(float)"""
        super(_GL30Interceptor, self).glLineWidth(_float.valueOf(arg0))

    @override
    @overload
    def glStencilMask(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilMask(int)"""
        super(_GL30Interceptor, self).glStencilMask(_int.valueOf(arg0))

    @override
    @overload
    def glBindFramebuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindFramebuffer(int,int)"""
        super(_GL30Interceptor, self).glBindFramebuffer(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def glProgramUniform2uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform2uiv(int,int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glProgramUniform2uiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniformMatrix3x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix3x2fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glProgramUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform4i(int,int,int,int,int,int)"""
        super(_GL31Interceptor, self).glProgramUniform4i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @overload
    def glGetProgramInfoLog(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetProgramInfoLog(int)"""
        return str._wrap(super(_GL30Interceptor, self).glGetProgramInfoLog(_int.valueOf(arg0)))

    @override
    @overload
    def glVertexAttribFormat(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glVertexAttribFormat(int,int,int,boolean,int)"""
        super(_GL31Interceptor, self).glVertexAttribFormat(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glProgramUniform1ui(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform1ui(int,int,int)"""
        super(_GL31Interceptor, self).glProgramUniform1ui(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glClearStencil(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearStencil(int)"""
        super(_GL30Interceptor, self).glClearStencil(_int.valueOf(arg0))

    @override
    @overload
    def glReadBuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glReadBuffer(int)"""
        super(_GL30Interceptor, self).glReadBuffer(_int.valueOf(arg0))

    @override
    @overload
    def glProgramUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform3i(int,int,int,int,int)"""
        super(_GL31Interceptor, self).glProgramUniform3i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glTexImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), arg8)

    @override
    @overload
    def glDispatchCompute(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glDispatchCompute(int,int,int)"""
        super(_GL31Interceptor, self).glDispatchCompute(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glUniform3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3f(int,float,float,float)"""
        super(_GL30Interceptor, self).glUniform3f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformBlockName(int,int)"""
        return str._wrap(super(_GL30Interceptor, self).glGetActiveUniformBlockName(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def glVertexAttrib3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib3f(int,float,float,float)"""
        super(_GL30Interceptor, self).glVertexAttrib3f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def glBeginQuery(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBeginQuery(int,int)"""
        super(_GL30Interceptor, self).glBeginQuery(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glProgramUniformMatrix4x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix4x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glProgramUniformMatrix4x3fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glGetVertexAttribfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribfv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glGetVertexAttribfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @overload
    def glGetBufferPointerv(self, arg0: int, arg1: int) -> 'Buffer':
        """public java.nio.Buffer com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBufferPointerv(int,int)"""
        return 'Buffer'._wrap(super(_GL30Interceptor, self).glGetBufferPointerv(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def glProgramUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glProgramUniformMatrix4fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glTexParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @overload
    def glGetUniformLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformLocation(int,java.lang.String)"""
        return int._wrap(super(_GL30Interceptor, self).glGetUniformLocation(_int.valueOf(arg0), arg1))

    @override
    @overload
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformBlockName(int,int,java.nio.Buffer,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glGetActiveUniformBlockName(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def glGetInteger64v(self, arg0: int, arg1: 'LongBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetInteger64v(int,java.nio.LongBuffer)"""
        super(_GL30Interceptor, self).glGetInteger64v(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniformMatrix4x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix4x3fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glGetAttachedShaders(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetAttachedShaders(int,int,java.nio.Buffer,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetAttachedShaders(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def glGetSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetSamplerParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGenRenderbuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenRenderbuffer()"""
        return int._wrap(super(GL30Interceptor, self).glGenRenderbuffer())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def glEndQuery(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEndQuery(int)"""
        super(_GL30Interceptor, self).glEndQuery(_int.valueOf(arg0))

    @override
    @overload
    def glProgramUniform1uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform1uiv(int,int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glProgramUniform1uiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glBlendColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendColor(float,float,float,float)"""
        super(_GL30Interceptor, self).glBlendColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getTextureBindings(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getTextureBindings()"""
        return int._wrap(super(GLInterceptor, self).getTextureBindings())

    @overload
    def glCreateShaderProgramv(self, arg0: int, arg1: 'String') -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL31Interceptor.glCreateShaderProgramv(int,java.lang.String[])"""
        return int._wrap(super(_GL31Interceptor, self).glCreateShaderProgramv(_int.valueOf(arg0), arg1))

    @override
    @overload
    def glGenTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTextures(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGenTextures(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetTexParameterfv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glGetTexParameterfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glShaderBinary(self, arg0: int, arg1: 'IntBuffer', arg2: int, arg3: 'Buffer', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glShaderBinary(int,java.nio.IntBuffer,int,java.nio.Buffer,int)"""
        super(_GL30Interceptor, self).glShaderBinary(_int.valueOf(arg0), arg1, _int.valueOf(arg2), arg3, _int.valueOf(arg4))

    @overload
    def glGetActiveAttrib(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer') -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveAttrib(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return str._wrap(super(_GL30Interceptor, self).glGetActiveAttrib(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3))

    @override
    @overload
    def glDisableVertexAttribArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDisableVertexAttribArray(int)"""
        super(_GL30Interceptor, self).glDisableVertexAttribArray(_int.valueOf(arg0))

    @override
    @overload
    def glInvalidateSubFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: int, arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glInvalidateSubFramebuffer(int,int,java.nio.IntBuffer,int,int,int,int)"""
        super(_GL30Interceptor, self).glInvalidateSubFramebuffer(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6))

    @override
    @overload
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2iv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glUniform2iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTransformFeedbacks(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGenTransformFeedbacks(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1iv(int,int,int[],int)"""
        super(_GL30Interceptor, self).glUniform1iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glGetBooleanv(self, arg0: int, arg1: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBooleanv(int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glGetBooleanv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glDrawArrays(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawArrays(int,int,int)"""
        super(_GL30Interceptor, self).glDrawArrays(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4fv(int,int,float[],int)"""
        super(_GL30Interceptor, self).glUniform4fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glDepthFunc(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDepthFunc(int)"""
        super(_GL30Interceptor, self).glDepthFunc(_int.valueOf(arg0))

    @overload
    def glGetStringi(self, arg0: int, arg1: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetStringi(int,int)"""
        return str._wrap(super(_GL30Interceptor, self).glGetStringi(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def glFramebufferTexture2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFramebufferTexture2D(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glFramebufferTexture2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @overload
    def glCheckFramebufferStatus(self, arg0: int) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCheckFramebufferStatus(int)"""
        return int._wrap(super(_GL30Interceptor, self).glCheckFramebufferStatus(_int.valueOf(arg0)))

    @overload
    def glIsProgram(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsProgram(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsProgram(_int.valueOf(arg0)))

    @override
    @overload
    def glProgramUniformMatrix3x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix3x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glProgramUniformMatrix3x2fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glDeleteQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteQueries(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDeleteQueries(_int.valueOf(arg0), arg1)

    @overload
    def glIsProgramPipeline(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL31Interceptor.glIsProgramPipeline(int)"""
        return bool._wrap(super(_GL31Interceptor, self).glIsProgramPipeline(_int.valueOf(arg0)))

    @override
    @overload
    def glGetUniformIndices(self, arg0: int, arg1: 'String', arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformIndices(int,java.lang.String[],java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetUniformIndices(_int.valueOf(arg0), arg1, arg2)

    @override
    @overload
    def glGenQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenQueries(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGenQueries(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetUniformiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetUniformiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGenSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenSamplers(int,int[],int)"""
        super(_GL30Interceptor, self).glGenSamplers(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def glTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameterfv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glTexParameterfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glMemoryBarrier(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glMemoryBarrier(int)"""
        super(_GL31Interceptor, self).glMemoryBarrier(_int.valueOf(arg0))

    @override
    @overload
    def glGetVertexAttribPointerv(self, arg0: int, arg1: int, arg2: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribPointerv(int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glGetVertexAttribPointerv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3fv(int,int,float[],int)"""
        super(_GL30Interceptor, self).glUniform3fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTransformFeedbacks(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDeleteTransformFeedbacks(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glSampleCoverage(self, arg0: float, arg1: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSampleCoverage(float,boolean)"""
        super(_GL30Interceptor, self).glSampleCoverage(_float.valueOf(arg0), _boolean.valueOf(arg1))

    @override
    @overload
    def glFramebufferRenderbuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFramebufferRenderbuffer(int,int,int,int)"""
        super(_GL30Interceptor, self).glFramebufferRenderbuffer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3iv(int,int,int[],int)"""
        super(_GL30Interceptor, self).glUniform3iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1fv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniform1fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGenBuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenBuffer()"""
        return int._wrap(super(GL30Interceptor, self).glGenBuffer())

    @override
    @overload
    def glProgramUniformMatrix2x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix2x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glProgramUniformMatrix2x4fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glVertexAttrib4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib4f(int,float,float,float,float)"""
        super(_GL30Interceptor, self).glVertexAttrib4f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @staticmethod
    @overload
    def resolveErrorNumber(arg0: int) -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.profiling.GLInterceptor.resolveErrorNumber(int)"""
        return str._wrap(_GLInterceptor.resolveErrorNumber(_int.valueOf(arg0)))

    @override
    @overload
    def glBlendEquationSeparate(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendEquationSeparate(int,int)"""
        super(_GL30Interceptor, self).glBlendEquationSeparate(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage3D(int,int,int,int,int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glTexImage3D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9))

    @override
    @overload
    def glProgramUniform4uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform4uiv(int,int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glProgramUniform4uiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform2f(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2f(int,float,float)"""
        super(_GL30Interceptor, self).glUniform2f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def glDeleteProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteProgram(int)"""
        super(_GL30Interceptor, self).glDeleteProgram(_int.valueOf(arg0))

    @override
    @overload
    def glBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBufferSubData(int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glBufferSubData(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def glBindSampler(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindSampler(int,int)"""
        super(_GL30Interceptor, self).glBindSampler(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glGetVertexAttribIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribIiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetVertexAttribIiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glFramebufferTextureLayer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFramebufferTextureLayer(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glFramebufferTextureLayer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glClearBufferuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferuiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glClearBufferuiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glProgramUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform4iv(int,int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glProgramUniform4iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2fv(int,int,float[],int)"""
        super(_GL30Interceptor, self).glUniform2fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glProgramUniformMatrix2x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix2x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glProgramUniformMatrix2x3fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage2D(int,int,int,int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glTexSubImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8)) 
 
 
# CLASS: com.badlogic.gdx.graphics.profiling.GLInterceptor
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.math.FloatCounter as _FloatCounter
_FloatCounter = _FloatCounter
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.nio.IntBuffer as IntBuffer
from builtins import float
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import com.badlogic.gdx.graphics.profiling.GLInterceptor as _GLInterceptor
_GLInterceptor = _GLInterceptor
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Integer as _int
import java.nio.Buffer as Buffer
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import com.badlogic.gdx.graphics.GL20 as _GL20
_GL20 = _GL20
 
class GLInterceptor():
    """com.badlogic.gdx.graphics.profiling.GLInterceptor"""
 
    @staticmethod
    def _wrap(java_value: _GLInterceptor) -> 'GLInterceptor':
        return GLInterceptor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLInterceptor):
        """
        Dynamic initializer for GLInterceptor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLInterceptor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLInterceptor__wrapper":
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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

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

    @overload
    def getCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getCalls()"""
        return int._wrap(super(GLInterceptor, self).getCalls())

    @abstractmethod
    def glLinkProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glLinkProgram(int)"""
        pass

    @abstractmethod
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4fv(int,int,float[],int)"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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

    @overload
    def getDrawCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getDrawCalls()"""
        return int._wrap(super(GLInterceptor, self).getDrawCalls())

    @abstractmethod
    def glDeleteRenderbuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteRenderbuffer(int)"""
        pass

    @abstractmethod
    def glGenFramebuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenFramebuffer()"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

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

    @overload
    def getVertexCount(self) -> 'math.FloatCounter':
        """public com.badlogic.gdx.math.FloatCounter com.badlogic.gdx.graphics.profiling.GLInterceptor.getVertexCount()"""
        return 'math.FloatCounter'._wrap(super(GLInterceptor, self).getVertexCount())

    @abstractmethod
    def glGenTexture(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenTexture()"""
        pass

    @abstractmethod
    def glIsBuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsBuffer(int)"""
        pass

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

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

    @overload
    def getShaderSwitches(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getShaderSwitches()"""
        return int._wrap(super(GLInterceptor, self).getShaderSwitches())

    @abstractmethod
    def glDepthFunc(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthFunc(int)"""
        pass

    @abstractmethod
    def glShaderSource(self, arg0: int, arg1: str):
        """public abstract void com.badlogic.gdx.graphics.GL20.glShaderSource(int,java.lang.String)"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

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

    @overload
    def getTextureBindings(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getTextureBindings()"""
        return int._wrap(super(GLInterceptor, self).getTextureBindings())

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

    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.profiling.GLInterceptor.reset()"""
        super(GLInterceptor, self).reset()

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

    @staticmethod
    @overload
    def resolveErrorNumber(arg0: int) -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.profiling.GLInterceptor.resolveErrorNumber(int)"""
        return str._wrap(_GLInterceptor.resolveErrorNumber(_int.valueOf(arg0)))

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
 
 
# CLASS: com.badlogic.gdx.graphics.profiling.GL32Interceptor
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.FloatCounter as _FloatCounter
_FloatCounter = _FloatCounter
import java.lang.Object as _Object
_Object = _Object
import java.nio.IntBuffer as IntBuffer
from builtins import type
import com.badlogic.gdx.graphics.profiling.GL30Interceptor as _GL30Interceptor
_GL30Interceptor = _GL30Interceptor
import com.badlogic.gdx.graphics.profiling.GLInterceptor as _GLInterceptor
_GLInterceptor = _GLInterceptor
import com.badlogic.gdx.graphics.profiling.GL32Interceptor as _GL32Interceptor
_GL32Interceptor = _GL32Interceptor
import java.nio.FloatBuffer as FloatBuffer
import java.lang.String as _string
import java.lang.Boolean as _boolean
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.nio.Buffer as _Buffer
_Buffer = _Buffer
from builtins import float
import java.nio.LongBuffer as LongBuffer
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import java.nio.Buffer as Buffer
import java.nio.ByteBuffer as ByteBuffer
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import com.badlogic.gdx.graphics.profiling.GL31Interceptor as _GL31Interceptor
_GL31Interceptor = _GL31Interceptor
import java.lang.Class as _Class
_Class = _Class
 
class GL32Interceptor():
    """com.badlogic.gdx.graphics.profiling.GL32Interceptor"""
 
    @staticmethod
    def _wrap(java_value: _GL32Interceptor) -> 'GL32Interceptor':
        return GL32Interceptor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GL32Interceptor):
        """
        Dynamic initializer for GL32Interceptor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GL32Interceptor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GL32Interceptor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def glIsBuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsBuffer(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsBuffer(_int.valueOf(arg0)))

    @override
    @overload
    def glCopyBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyBufferSubData(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glCopyBufferSubData(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glPauseTransformFeedback(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glPauseTransformFeedback()"""
        super(GL30Interceptor, self).glPauseTransformFeedback()

    @override
    @overload
    def getVertexCount(self) -> 'math.FloatCounter':
        """public com.badlogic.gdx.math.FloatCounter com.badlogic.gdx.graphics.profiling.GLInterceptor.getVertexCount()"""
        return 'math.FloatCounter'._wrap(super(GLInterceptor, self).getVertexCount())

    @override
    @overload
    def glDeleteSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteSamplers(int,int[],int)"""
        super(_GL30Interceptor, self).glDeleteSamplers(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def glTexParameterIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glTexParameterIiv(int,int,java.nio.IntBuffer)"""
        super(_GL32Interceptor, self).glTexParameterIiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform3uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3uiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glUniform3uiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetTexParameterIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glGetTexParameterIuiv(int,int,java.nio.IntBuffer)"""
        super(_GL32Interceptor, self).glGetTexParameterIuiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDetachShader(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDetachShader(int,int)"""
        super(_GL30Interceptor, self).glDetachShader(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3fv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniform3fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glEnablei(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glEnablei(int,int)"""
        super(_GL32Interceptor, self).glEnablei(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glGenSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenSamplers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGenSamplers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glDeleteVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteVertexArrays(int,int[],int)"""
        super(_GL30Interceptor, self).glDeleteVertexArrays(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def glGenVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenVertexArrays(int,int[],int)"""
        super(_GL30Interceptor, self).glGenVertexArrays(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def glClear(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClear(int)"""
        super(_GL30Interceptor, self).glClear(_int.valueOf(arg0))

    @override
    @overload
    def glUniform4uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4uiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glUniform4uiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteTexture(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTexture(int)"""
        super(_GL30Interceptor, self).glDeleteTexture(_int.valueOf(arg0))

    @override
    @overload
    def glDepthMask(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDepthMask(boolean)"""
        super(_GL30Interceptor, self).glDepthMask(_boolean.valueOf(arg0))

    @override
    @overload
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1fv(int,int,float[],int)"""
        super(_GL30Interceptor, self).glUniform1fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3i(int,int,int,int)"""
        super(_GL30Interceptor, self).glUniform3i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glDrawArraysIndirect(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glDrawArraysIndirect(int,long)"""
        super(_GL31Interceptor, self).glDrawArraysIndirect(_int.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def glGetQueryObjectuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetQueryObjectuiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetQueryObjectuiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glSamplerParameterfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glBindRenderbuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindRenderbuffer(int,int)"""
        super(_GL30Interceptor, self).glBindRenderbuffer(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glGetShaderiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetShaderiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetShaderiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glPixelStorei(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glPixelStorei(int,int)"""
        super(_GL30Interceptor, self).glPixelStorei(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glGetTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetTexParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetTexParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetVertexAttribIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribIuiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetVertexAttribIuiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glSamplerParameterf(self, arg0: int, arg1: int, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameterf(int,int,float)"""
        super(_GL30Interceptor, self).glSamplerParameterf(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glTexSubImage3D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), arg10)

    @override
    @overload
    def glProgramUniform2i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform2i(int,int,int,int)"""
        super(_GL31Interceptor, self).glProgramUniform2i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glDisable(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDisable(int)"""
        super(_GL30Interceptor, self).glDisable(_int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def glSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glSamplerParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glUseProgramStages(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glUseProgramStages(int,int,int)"""
        super(_GL31Interceptor, self).glUseProgramStages(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glUniform1uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1uiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glUniform1uiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glObjectLabel(self, arg0: int, arg1: int, arg2: str):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glObjectLabel(int,int,java.lang.String)"""
        super(_GL32Interceptor, self).glObjectLabel(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDispatchComputeIndirect(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glDispatchComputeIndirect(long)"""
        super(_GL31Interceptor, self).glDispatchComputeIndirect(_long.valueOf(arg0))

    @override
    @overload
    def glDrawArraysInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawArraysInstanced(int,int,int,int)"""
        super(_GL30Interceptor, self).glDrawArraysInstanced(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glProgramUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform1iv(int,int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glProgramUniform1iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glTexBuffer(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glTexBuffer(int,int,int)"""
        super(_GL32Interceptor, self).glTexBuffer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glProgramUniform3uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform3uiv(int,int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glProgramUniform3uiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glProgramUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform3fv(int,int,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glProgramUniform3fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @overload
    def glIsVertexArray(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsVertexArray(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsVertexArray(_int.valueOf(arg0)))

    @override
    @overload
    def glPatchParameteri(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glPatchParameteri(int,int)"""
        super(_GL32Interceptor, self).glPatchParameteri(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glUniformMatrix4x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix4x2fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glColorMask(self, arg0: bool, arg1: bool, arg2: bool, arg3: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glColorMask(boolean,boolean,boolean,boolean)"""
        super(_GL30Interceptor, self).glColorMask(_boolean.valueOf(arg0), _boolean.valueOf(arg1), _boolean.valueOf(arg2), _boolean.valueOf(arg3))

    @override
    @overload
    def glPolygonOffset(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glPolygonOffset(float,float)"""
        super(_GL30Interceptor, self).glPolygonOffset(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def glProgramUniform1f(self, arg0: int, arg1: int, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform1f(int,int,float)"""
        super(_GL31Interceptor, self).glProgramUniform1f(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def glBlendFunc(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendFunc(int,int)"""
        super(_GL30Interceptor, self).glBlendFunc(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glShaderSource(self, arg0: int, arg1: str):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glShaderSource(int,java.lang.String)"""
        super(_GL30Interceptor, self).glShaderSource(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetUniformfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformfv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glGetUniformfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteSamplers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDeleteSamplers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def glUniformMatrix3x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix3x4fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @overload
    def glGetFragDataLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetFragDataLocation(int,java.lang.String)"""
        return int._wrap(super(_GL30Interceptor, self).glGetFragDataLocation(_int.valueOf(arg0), arg1))

    @override
    @overload
    def glClearBufferfi(self, arg0: int, arg1: int, arg2: float, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferfi(int,int,float,int)"""
        super(_GL30Interceptor, self).glClearBufferfi(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glUseProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUseProgram(int)"""
        super(_GL30Interceptor, self).glUseProgram(_int.valueOf(arg0))

    @override
    @overload
    def glUniformBlockBinding(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformBlockBinding(int,int,int)"""
        super(_GL30Interceptor, self).glUniformBlockBinding(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def __init__(self, arg0: 'GLProfiler', arg1: 'GL32'):
        """public com.badlogic.gdx.graphics.profiling.GL32Interceptor(com.badlogic.gdx.graphics.profiling.GLProfiler,com.badlogic.gdx.graphics.GL32)"""
        val = _GL32Interceptor(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def glGetnUniformiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glGetnUniformiv(int,int,java.nio.IntBuffer)"""
        super(_GL32Interceptor, self).glGetnUniformiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glCopyTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyTexImage2D(int,int,int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glCopyTexImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7))

    @override
    @overload
    def glViewport(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glViewport(int,int,int,int)"""
        super(_GL30Interceptor, self).glViewport(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glClearColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearColor(float,float,float,float)"""
        super(_GL30Interceptor, self).glClearColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def glGetProgramiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetProgramiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetProgramiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glProgramUniform2f(self, arg0: int, arg1: int, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform2f(int,int,float,float)"""
        super(_GL31Interceptor, self).glProgramUniform2f(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def glCreateProgram(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCreateProgram()"""
        return int._wrap(super(GL30Interceptor, self).glCreateProgram())

    @override
    @overload
    def glDeleteQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteQueries(int,int[],int)"""
        super(_GL30Interceptor, self).glDeleteQueries(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def glGetMultisamplefv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetMultisamplefv(int,int,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glGetMultisamplefv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glBindTexture(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindTexture(int,int)"""
        super(_GL30Interceptor, self).glBindTexture(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glGenVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenVertexArrays(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGenVertexArrays(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glVertexBindingDivisor(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glVertexBindingDivisor(int,int)"""
        super(_GL31Interceptor, self).glVertexBindingDivisor(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glProgramUniform4f(self, arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform4f(int,int,float,float,float,float)"""
        super(_GL31Interceptor, self).glProgramUniform4f(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))

    @override
    @overload
    def glValidateProgramPipeline(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glValidateProgramPipeline(int)"""
        super(_GL31Interceptor, self).glValidateProgramPipeline(_int.valueOf(arg0))

    @override
    @overload
    def glGetTexLevelParameterfv(self, arg0: int, arg1: int, arg2: int, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetTexLevelParameterfv(int,int,int,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glGetTexLevelParameterfv(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def glUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4i(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glUniform4i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage3D(int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glTexImage3D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), arg9)

    @override
    @overload
    def glGetError(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetError()"""
        return int._wrap(super(GL30Interceptor, self).glGetError())

    @override
    @overload
    def glDeleteProgramPipelines(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glDeleteProgramPipelines(int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glDeleteProgramPipelines(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glScissor(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glScissor(int,int,int,int)"""
        super(_GL30Interceptor, self).glScissor(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glGetShaderPrecisionFormat(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetShaderPrecisionFormat(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetShaderPrecisionFormat(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3)

    @overload
    def glGetActiveUniform(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer') -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniform(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return str._wrap(super(_GL30Interceptor, self).glGetActiveUniform(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3))

    @override
    @overload
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4fv(int,int,boolean,float[],int)"""
        super(_GL30Interceptor, self).glUniformMatrix4fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3, _int.valueOf(arg4))

    @override
    @overload
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix4fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glStencilMaskSeparate(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilMaskSeparate(int,int)"""
        super(_GL30Interceptor, self).glStencilMaskSeparate(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glVertexAttrib2f(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib2f(int,float,float)"""
        super(_GL30Interceptor, self).glVertexAttrib2f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def glBindVertexBuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glBindVertexBuffer(int,int,long,int)"""
        super(_GL31Interceptor, self).glBindVertexBuffer(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glSamplerParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameteri(int,int,int)"""
        super(_GL30Interceptor, self).glSamplerParameteri(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glGetBufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBufferParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetBufferParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glBlitFramebuffer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlitFramebuffer(int,int,int,int,int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glBlitFramebuffer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9))

    @override
    @overload
    def glBlendFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendFuncSeparate(int,int,int,int)"""
        super(_GL30Interceptor, self).glBlendFuncSeparate(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glTransformFeedbackVaryings(self, arg0: int, arg1: 'String', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTransformFeedbackVaryings(int,java.lang.String[],int)"""
        super(_GL30Interceptor, self).glTransformFeedbackVaryings(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def glGenRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenRenderbuffers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGenRenderbuffers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glBindVertexArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindVertexArray(int)"""
        super(_GL30Interceptor, self).glBindVertexArray(_int.valueOf(arg0))

    @override
    @overload
    def glBlendFunci(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glBlendFunci(int,int,int)"""
        super(_GL32Interceptor, self).glBlendFunci(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glProgramUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform2iv(int,int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glProgramUniform2iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glProgramUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform4fv(int,int,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glProgramUniform4fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glStencilFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilFuncSeparate(int,int,int,int)"""
        super(_GL30Interceptor, self).glStencilFuncSeparate(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glGenQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenQueries(int,int[],int)"""
        super(_GL30Interceptor, self).glGenQueries(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def glBindBufferBase(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindBufferBase(int,int,int)"""
        super(_GL30Interceptor, self).glBindBufferBase(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glProgramUniform3ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform3ui(int,int,int,int,int)"""
        super(_GL31Interceptor, self).glProgramUniform3ui(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def getCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getCalls()"""
        return int._wrap(super(GLInterceptor, self).getCalls())

    @overload
    def glIsTexture(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsTexture(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsTexture(_int.valueOf(arg0)))

    @override
    @overload
    def glGetActiveUniformBlockiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformBlockiv(int,int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetActiveUniformBlockiv(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def glEnable(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEnable(int)"""
        super(_GL30Interceptor, self).glEnable(_int.valueOf(arg0))

    @override
    @overload
    def glGenFramebuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenFramebuffer()"""
        return int._wrap(super(GL30Interceptor, self).glGenFramebuffer())

    @override
    @overload
    def glProgramUniform1i(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform1i(int,int,int)"""
        super(_GL31Interceptor, self).glProgramUniform1i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glTexParameterf(self, arg0: int, arg1: int, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameterf(int,int,float)"""
        super(_GL30Interceptor, self).glTexParameterf(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def glGetRenderbufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetRenderbufferParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetRenderbufferParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @overload
    def glIsEnabled(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsEnabled(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsEnabled(_int.valueOf(arg0)))

    @override
    @overload
    def getShaderSwitches(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getShaderSwitches()"""
        return int._wrap(super(GLInterceptor, self).getShaderSwitches())

    @override
    @overload
    def glBindProgramPipeline(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glBindProgramPipeline(int)"""
        super(_GL31Interceptor, self).glBindProgramPipeline(_int.valueOf(arg0))

    @override
    @overload
    def glCopyTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyTexSubImage3D(int,int,int,int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glCopyTexSubImage3D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8))

    @override
    @overload
    def glDisablei(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glDisablei(int,int)"""
        super(_GL32Interceptor, self).glDisablei(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glPopDebugGroup(self):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glPopDebugGroup()"""
        super(GL32Interceptor, self).glPopDebugGroup()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def glGetIntegerv(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetIntegerv(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetIntegerv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glEnableVertexAttribArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEnableVertexAttribArray(int)"""
        super(_GL30Interceptor, self).glEnableVertexAttribArray(_int.valueOf(arg0))

    @override
    @overload
    def glReleaseShaderCompiler(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glReleaseShaderCompiler()"""
        super(GL30Interceptor, self).glReleaseShaderCompiler()

    @override
    @overload
    def glBlendEquation(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendEquation(int)"""
        super(_GL30Interceptor, self).glBlendEquation(_int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2fv(int,int,boolean,float[],int)"""
        super(_GL30Interceptor, self).glUniformMatrix2fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3, _int.valueOf(arg4))

    @override
    @overload
    def glVertexAttribIFormat(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glVertexAttribIFormat(int,int,int,int)"""
        super(_GL31Interceptor, self).glVertexAttribIFormat(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def glMapBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Buffer':
        """public java.nio.Buffer com.badlogic.gdx.graphics.profiling.GL30Interceptor.glMapBufferRange(int,int,int,int)"""
        return 'Buffer'._wrap(super(_GL30Interceptor, self).glMapBufferRange(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def glGetFramebufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetFramebufferParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glGetFramebufferParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDepthRangef(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDepthRangef(float,float)"""
        super(_GL30Interceptor, self).glDepthRangef(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def glBindTransformFeedback(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindTransformFeedback(int,int)"""
        super(_GL30Interceptor, self).glBindTransformFeedback(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glProgramUniform2ui(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform2ui(int,int,int,int)"""
        super(_GL31Interceptor, self).glProgramUniform2ui(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glActiveShaderProgram(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glActiveShaderProgram(int,int)"""
        super(_GL31Interceptor, self).glActiveShaderProgram(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glGetFloatv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetFloatv(int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glGetFloatv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetnUniformuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glGetnUniformuiv(int,int,java.nio.IntBuffer)"""
        super(_GL32Interceptor, self).glGetnUniformuiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @overload
    def glIsShader(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsShader(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsShader(_int.valueOf(arg0)))

    @override
    @overload
    def glResumeTransformFeedback(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glResumeTransformFeedback()"""
        super(GL30Interceptor, self).glResumeTransformFeedback()

    @override
    @overload
    def glProgramUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform2fv(int,int,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glProgramUniform2fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glProgramUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glProgramUniformMatrix3fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTransformFeedbacks(int,int[],int)"""
        super(_GL30Interceptor, self).glDeleteTransformFeedbacks(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def glEndTransformFeedback(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEndTransformFeedback()"""
        super(GL30Interceptor, self).glEndTransformFeedback()

    @override
    @overload
    def glBindBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindBufferRange(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glBindBufferRange(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glAttachShader(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glAttachShader(int,int)"""
        super(_GL30Interceptor, self).glAttachShader(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glCompileShader(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCompileShader(int)"""
        super(_GL30Interceptor, self).glCompileShader(_int.valueOf(arg0))

    @overload
    def glGetShaderInfoLog(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetShaderInfoLog(int)"""
        return str._wrap(super(_GL30Interceptor, self).glGetShaderInfoLog(_int.valueOf(arg0)))

    @overload
    def glGetAttribLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetAttribLocation(int,java.lang.String)"""
        return int._wrap(super(_GL30Interceptor, self).glGetAttribLocation(_int.valueOf(arg0), arg1))

    @override
    @overload
    def glCopyImageSubData(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glCopyImageSubData(int,int,int,int,int,int,int,int,int,int,int,int,int,int,int)"""
        super(_GL32Interceptor, self).glCopyImageSubData(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _int.valueOf(arg14))

    @overload
    def glIsRenderbuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsRenderbuffer(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsRenderbuffer(_int.valueOf(arg0)))

    @override
    @overload
    def glUniformMatrix2x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix2x3fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glTexStorage2DMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glTexStorage2DMultisample(int,int,int,int,int,boolean)"""
        super(_GL31Interceptor, self).glTexStorage2DMultisample(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _boolean.valueOf(arg5))

    @override
    @overload
    def glGetProgramInterfaceiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramInterfaceiv(int,int,int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glGetProgramInterfaceiv(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawElements(int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glDrawElements(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def glUniform4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4f(int,float,float,float,float)"""
        super(_GL30Interceptor, self).glUniform4f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def glGetPointerv(self, arg0: int) -> int:
        """public long com.badlogic.gdx.graphics.profiling.GL32Interceptor.glGetPointerv(int)"""
        return int._wrap(super(_GL32Interceptor, self).glGetPointerv(_int.valueOf(arg0)))

    @override
    @overload
    def glGetProgramPipelineiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramPipelineiv(int,int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glGetProgramPipelineiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawElements(int,int,int,int)"""
        super(_GL30Interceptor, self).glDrawElements(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glDeleteFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteFramebuffers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDeleteFramebuffers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glRenderbufferStorage(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glRenderbufferStorage(int,int,int,int)"""
        super(_GL30Interceptor, self).glRenderbufferStorage(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.profiling.GLInterceptor.reset()"""
        super(GLInterceptor, self).reset()

    @override
    @overload
    def glDrawElementsInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawElementsInstanced(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glDrawElementsInstanced(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glFramebufferParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glFramebufferParameteri(int,int,int)"""
        super(_GL31Interceptor, self).glFramebufferParameteri(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage2D(int,int,int,int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glTexImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8))

    @override
    @overload
    def glDeleteFramebuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteFramebuffer(int)"""
        super(_GL30Interceptor, self).glDeleteFramebuffer(_int.valueOf(arg0))

    @override
    @overload
    def glGetActiveUniformsiv(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformsiv(int,int,java.nio.IntBuffer,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetActiveUniformsiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), arg4)

    @override
    @overload
    def glTexParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameteri(int,int,int)"""
        super(_GL30Interceptor, self).glTexParameteri(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix3fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glReadPixels(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glReadPixels(int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glReadPixels(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), arg6)

    @override
    @overload
    def glUniform2i(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2i(int,int,int)"""
        super(_GL30Interceptor, self).glUniform2i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2iv(int,int,int[],int)"""
        super(_GL30Interceptor, self).glUniform2iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glVertexAttribBinding(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glVertexAttribBinding(int,int)"""
        super(_GL31Interceptor, self).glVertexAttribBinding(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3fv(int,int,boolean,float[],int)"""
        super(_GL30Interceptor, self).glUniformMatrix3fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3, _int.valueOf(arg4))

    @override
    @overload
    def glUniform1f(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1f(int,float)"""
        super(_GL30Interceptor, self).glUniform1f(_int.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def glVertexAttrib3fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib3fv(int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glVertexAttrib3fv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTransformFeedbacks(int,int[],int)"""
        super(_GL30Interceptor, self).glGenTransformFeedbacks(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def glGetQueryiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetQueryiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetQueryiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDrawElementsInstancedBaseVertex(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer', arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glDrawElementsInstancedBaseVertex(int,int,int,java.nio.Buffer,int,int)"""
        super(_GL32Interceptor, self).glDrawElementsInstancedBaseVertex(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, _int.valueOf(arg4), _int.valueOf(arg5))

    @override
    @overload
    def glTexParameterIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glTexParameterIuiv(int,int,java.nio.IntBuffer)"""
        super(_GL32Interceptor, self).glTexParameterIuiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetVertexAttribiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetVertexAttribiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4fv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniform4fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @overload
    def glIsFramebuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsFramebuffer(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsFramebuffer(_int.valueOf(arg0)))

    @override
    @overload
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribPointer(int,int,int,boolean,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glVertexAttribPointer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), arg5)

    @overload
    def glGetString(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetString(int)"""
        return str._wrap(super(_GL30Interceptor, self).glGetString(_int.valueOf(arg0)))

    @override
    @overload
    def glDeleteShader(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteShader(int)"""
        super(_GL30Interceptor, self).glDeleteShader(_int.valueOf(arg0))

    @override
    @overload
    def glSampleMaski(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glSampleMaski(int,int)"""
        super(_GL31Interceptor, self).glSampleMaski(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glClearBufferiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glClearBufferiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glVertexAttrib2fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib2fv(int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glVertexAttrib2fv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1iv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glUniform1iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4iv(int,int,int[],int)"""
        super(_GL30Interceptor, self).glUniform4iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glReadnPixels(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glReadnPixels(int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL32Interceptor, self).glReadnPixels(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), arg7)

    @overload
    def glGetProgramResourceIndex(self, arg0: int, arg1: int, arg2: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramResourceIndex(int,int,java.lang.String)"""
        return int._wrap(super(_GL31Interceptor, self).glGetProgramResourceIndex(_int.valueOf(arg0), _int.valueOf(arg1), arg2))

    @overload
    def glGetUniformBlockIndex(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformBlockIndex(int,java.lang.String)"""
        return int._wrap(super(_GL30Interceptor, self).glGetUniformBlockIndex(_int.valueOf(arg0), arg1))

    @override
    @overload
    def glStencilOpSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilOpSeparate(int,int,int,int)"""
        super(_GL30Interceptor, self).glStencilOpSeparate(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glSamplerParameterIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glSamplerParameterIiv(int,int,java.nio.IntBuffer)"""
        super(_GL32Interceptor, self).glSamplerParameterIiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glTexSubImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), arg8)

    @override
    @overload
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2fv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniform2fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribPointer(int,int,int,boolean,int,int)"""
        super(_GL30Interceptor, self).glVertexAttribPointer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @override
    @overload
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawRangeElements(int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glDrawRangeElements(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @override
    @overload
    def glVertexAttribI4ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribI4ui(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glVertexAttribI4ui(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glBindAttribLocation(self, arg0: int, arg1: int, arg2: str):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindAttribLocation(int,int,java.lang.String)"""
        super(_GL30Interceptor, self).glBindAttribLocation(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDebugMessageInsert(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: str):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glDebugMessageInsert(int,int,int,int,java.lang.String)"""
        super(_GL32Interceptor, self).glDebugMessageInsert(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4)

    @override
    @overload
    def glMemoryBarrierByRegion(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glMemoryBarrierByRegion(int)"""
        super(_GL31Interceptor, self).glMemoryBarrierByRegion(_int.valueOf(arg0))

    @override
    @overload
    def glProgramUniformMatrix4x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix4x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glProgramUniformMatrix4x2fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glGetFramebufferAttachmentParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetFramebufferAttachmentParameteriv(int,int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetFramebufferAttachmentParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def glGetTexLevelParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetTexLevelParameteriv(int,int,int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glGetTexLevelParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def glFrontFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFrontFace(int)"""
        super(_GL30Interceptor, self).glFrontFace(_int.valueOf(arg0))

    @override
    @overload
    def glVertexAttribI4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribI4i(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glVertexAttribI4i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glCompressedTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCompressedTexImage2D(int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glCompressedTexImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), arg7)

    @override
    @overload
    def glGetBufferParameteri64v(self, arg0: int, arg1: int, arg2: 'LongBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBufferParameteri64v(int,int,java.nio.LongBuffer)"""
        super(_GL30Interceptor, self).glGetBufferParameteri64v(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteBuffers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDeleteBuffers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glBlendBarrier(self):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glBlendBarrier()"""
        super(GL32Interceptor, self).glBlendBarrier()

    @overload
    def glIsTransformFeedback(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsTransformFeedback(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsTransformFeedback(_int.valueOf(arg0)))

    @override
    @overload
    def glDeleteTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTextures(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDeleteTextures(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glProgramUniform4ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform4ui(int,int,int,int,int,int)"""
        super(_GL31Interceptor, self).glProgramUniform4ui(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @override
    @overload
    def glFlush(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFlush()"""
        super(GL30Interceptor, self).glFlush()

    @override
    @overload
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix2fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @overload
    def glGetObjectLabel(self, arg0: int, arg1: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL32Interceptor.glGetObjectLabel(int,int)"""
        return str._wrap(super(_GL32Interceptor, self).glGetObjectLabel(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def glProgramUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform3iv(int,int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glProgramUniform3iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glBlendEquationi(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glBlendEquationi(int,int)"""
        super(_GL32Interceptor, self).glBlendEquationi(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glTexStorage3DMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glTexStorage3DMultisample(int,int,int,int,int,int,boolean)"""
        super(_GL32Interceptor, self).glTexStorage3DMultisample(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _boolean.valueOf(arg6))

    @override
    @overload
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glTexSubImage3D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10))

    @override
    @overload
    def glCompressedTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCompressedTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glCompressedTexSubImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), arg8)

    @override
    @overload
    def glGetSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glGetSamplerParameterfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetBooleani_v(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetBooleani_v(int,int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glGetBooleani_v(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteRenderbuffers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDeleteRenderbuffers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glGenFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenFramebuffers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGenFramebuffers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glColorMaski(self, arg0: int, arg1: bool, arg2: bool, arg3: bool, arg4: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glColorMaski(int,boolean,boolean,boolean,boolean)"""
        super(_GL32Interceptor, self).glColorMaski(_int.valueOf(arg0), _boolean.valueOf(arg1), _boolean.valueOf(arg2), _boolean.valueOf(arg3), _boolean.valueOf(arg4))

    @override
    @overload
    def glVertexAttrib1fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib1fv(int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glVertexAttrib1fv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glGenProgramPipelines(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGenProgramPipelines(int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glGenProgramPipelines(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glGenerateMipmap(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenerateMipmap(int)"""
        super(_GL30Interceptor, self).glGenerateMipmap(_int.valueOf(arg0))

    @override
    @overload
    def glGenBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenBuffers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGenBuffers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glFlushMappedBufferRange(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFlushMappedBufferRange(int,int,int)"""
        super(_GL30Interceptor, self).glFlushMappedBufferRange(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glClearDepthf(self, arg0: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearDepthf(float)"""
        super(_GL30Interceptor, self).glClearDepthf(_float.valueOf(arg0))

    @override
    @overload
    def glProgramUniformMatrix3x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix3x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glProgramUniformMatrix3x4fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def glRenderbufferStorageMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glRenderbufferStorageMultisample(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glRenderbufferStorageMultisample(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glUniform1i(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1i(int,int)"""
        super(_GL30Interceptor, self).glUniform1i(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glValidateProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glValidateProgram(int)"""
        super(_GL30Interceptor, self).glValidateProgram(_int.valueOf(arg0))

    @override
    @overload
    def glStencilOp(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilOp(int,int,int)"""
        super(_GL30Interceptor, self).glStencilOp(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glUniformMatrix2x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix2x4fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glCopyTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyTexSubImage2D(int,int,int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glCopyTexSubImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7))

    @override
    @overload
    def glLinkProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glLinkProgram(int)"""
        super(_GL30Interceptor, self).glLinkProgram(_int.valueOf(arg0))

    @override
    @overload
    def glDrawBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawBuffers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDrawBuffers(_int.valueOf(arg0), arg1)

    @overload
    def glUnmapBuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUnmapBuffer(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glUnmapBuffer(_int.valueOf(arg0)))

    @override
    @overload
    def glVertexAttribDivisor(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribDivisor(int,int)"""
        super(_GL30Interceptor, self).glVertexAttribDivisor(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glStencilFunc(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilFunc(int,int,int)"""
        super(_GL30Interceptor, self).glStencilFunc(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glProgramUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glProgramUniformMatrix2fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glGetSamplerParameterIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glGetSamplerParameterIiv(int,int,java.nio.IntBuffer)"""
        super(_GL32Interceptor, self).glGetSamplerParameterIiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetUniformuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformuiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetUniformuiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glTexBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glTexBufferRange(int,int,int,int,int)"""
        super(_GL32Interceptor, self).glTexBufferRange(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glCullFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCullFace(int)"""
        super(_GL30Interceptor, self).glCullFace(_int.valueOf(arg0))

    @override
    @overload
    def glHint(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glHint(int,int)"""
        super(_GL30Interceptor, self).glHint(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glProgramParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glProgramParameteri(int,int,int)"""
        super(_GL30Interceptor, self).glProgramParameteri(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3iv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glUniform3iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glProgramUniform3f(self, arg0: int, arg1: int, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform3f(int,int,float,float,float)"""
        super(_GL31Interceptor, self).glProgramUniform3f(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def glCreateShader(self, arg0: int) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCreateShader(int)"""
        return int._wrap(super(_GL30Interceptor, self).glCreateShader(_int.valueOf(arg0)))

    @override
    @overload
    def glDeleteBuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteBuffer(int)"""
        super(_GL30Interceptor, self).glDeleteBuffer(_int.valueOf(arg0))

    @override
    @overload
    def glGetProgramResourceiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramResourceiv(int,int,int,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glGetProgramResourceiv(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, arg4, arg5)

    @override
    @overload
    def glBeginTransformFeedback(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBeginTransformFeedback(int)"""
        super(_GL30Interceptor, self).glBeginTransformFeedback(_int.valueOf(arg0))

    @override
    @overload
    def glClearBufferfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferfv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glClearBufferfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glProgramUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform1fv(int,int,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glProgramUniform1fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glActiveTexture(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glActiveTexture(int)"""
        super(_GL30Interceptor, self).glActiveTexture(_int.valueOf(arg0))

    @override
    @overload
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4iv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glUniform4iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteVertexArrays(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDeleteVertexArrays(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glDebugMessageControl(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer', arg4: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glDebugMessageControl(int,int,int,java.nio.IntBuffer,boolean)"""
        super(_GL32Interceptor, self).glDebugMessageControl(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, _boolean.valueOf(arg4))

    @override
    @overload
    def glVertexAttrib4fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib4fv(int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glVertexAttrib4fv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glBindBuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindBuffer(int,int)"""
        super(_GL30Interceptor, self).glBindBuffer(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def glGetProgramPipelineInfoLog(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramPipelineInfoLog(int)"""
        return str._wrap(super(_GL31Interceptor, self).glGetProgramPipelineInfoLog(_int.valueOf(arg0)))

    @override
    @overload
    def glVertexAttribIPointer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribIPointer(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glVertexAttribIPointer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @overload
    def glIsQuery(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsQuery(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsQuery(_int.valueOf(arg0)))

    @overload
    def glGetProgramResourceName(self, arg0: int, arg1: int, arg2: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramResourceName(int,int,int)"""
        return str._wrap(super(_GL31Interceptor, self).glGetProgramResourceName(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def glGenTexture(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTexture()"""
        return int._wrap(super(GL30Interceptor, self).glGenTexture())

    @overload
    def glGetProgramResourceLocation(self, arg0: int, arg1: int, arg2: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramResourceLocation(int,int,java.lang.String)"""
        return int._wrap(super(_GL31Interceptor, self).glGetProgramResourceLocation(_int.valueOf(arg0), _int.valueOf(arg1), arg2))

    @override
    @overload
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawRangeElements(int,int,int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glDrawRangeElements(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5)

    @override
    @overload
    def glPushDebugGroup(self, arg0: int, arg1: int, arg2: str):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glPushDebugGroup(int,int,java.lang.String)"""
        super(_GL32Interceptor, self).glPushDebugGroup(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glBufferData(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBufferData(int,int,java.nio.Buffer,int)"""
        super(_GL30Interceptor, self).glBufferData(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def getDrawCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getDrawCalls()"""
        return int._wrap(super(GLInterceptor, self).getDrawCalls())

    @override
    @overload
    def glFinish(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFinish()"""
        super(GL30Interceptor, self).glFinish()

    @override
    @overload
    def glDeleteRenderbuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteRenderbuffer(int)"""
        super(_GL30Interceptor, self).glDeleteRenderbuffer(_int.valueOf(arg0))

    @override
    @overload
    def glGetGraphicsResetStatus(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL32Interceptor.glGetGraphicsResetStatus()"""
        return int._wrap(super(GL32Interceptor, self).glGetGraphicsResetStatus())

    @override
    @overload
    def glVertexAttrib1f(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib1f(int,float)"""
        super(_GL30Interceptor, self).glVertexAttrib1f(_int.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def glBindImageTexture(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glBindImageTexture(int,int,int,boolean,int,int,int)"""
        super(_GL31Interceptor, self).glBindImageTexture(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6))

    @overload
    def glIsSampler(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsSampler(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsSampler(_int.valueOf(arg0)))

    @override
    @overload
    def glDrawElementsIndirect(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glDrawElementsIndirect(int,int,long)"""
        super(_GL31Interceptor, self).glDrawElementsIndirect(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2))

    @override
    @overload
    def glInvalidateFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glInvalidateFramebuffer(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glInvalidateFramebuffer(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glLineWidth(self, arg0: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glLineWidth(float)"""
        super(_GL30Interceptor, self).glLineWidth(_float.valueOf(arg0))

    @override
    @overload
    def glStencilMask(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilMask(int)"""
        super(_GL30Interceptor, self).glStencilMask(_int.valueOf(arg0))

    @override
    @overload
    def glBindFramebuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindFramebuffer(int,int)"""
        super(_GL30Interceptor, self).glBindFramebuffer(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def glProgramUniform2uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform2uiv(int,int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glProgramUniform2uiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniformMatrix3x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix3x2fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glGetSamplerParameterIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glGetSamplerParameterIuiv(int,int,java.nio.IntBuffer)"""
        super(_GL32Interceptor, self).glGetSamplerParameterIuiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glProgramUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform4i(int,int,int,int,int,int)"""
        super(_GL31Interceptor, self).glProgramUniform4i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @overload
    def glGetProgramInfoLog(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetProgramInfoLog(int)"""
        return str._wrap(super(_GL30Interceptor, self).glGetProgramInfoLog(_int.valueOf(arg0)))

    @override
    @overload
    def glVertexAttribFormat(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glVertexAttribFormat(int,int,int,boolean,int)"""
        super(_GL31Interceptor, self).glVertexAttribFormat(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glProgramUniform1ui(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform1ui(int,int,int)"""
        super(_GL31Interceptor, self).glProgramUniform1ui(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glClearStencil(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearStencil(int)"""
        super(_GL30Interceptor, self).glClearStencil(_int.valueOf(arg0))

    @override
    @overload
    def glReadBuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glReadBuffer(int)"""
        super(_GL30Interceptor, self).glReadBuffer(_int.valueOf(arg0))

    @override
    @overload
    def glProgramUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform3i(int,int,int,int,int)"""
        super(_GL31Interceptor, self).glProgramUniform3i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glGetTexParameterIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glGetTexParameterIiv(int,int,java.nio.IntBuffer)"""
        super(_GL32Interceptor, self).glGetTexParameterIiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glTexImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), arg8)

    @override
    @overload
    def glDispatchCompute(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glDispatchCompute(int,int,int)"""
        super(_GL31Interceptor, self).glDispatchCompute(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glUniform3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3f(int,float,float,float)"""
        super(_GL30Interceptor, self).glUniform3f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformBlockName(int,int)"""
        return str._wrap(super(_GL30Interceptor, self).glGetActiveUniformBlockName(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def glVertexAttrib3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib3f(int,float,float,float)"""
        super(_GL30Interceptor, self).glVertexAttrib3f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def glBeginQuery(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBeginQuery(int,int)"""
        super(_GL30Interceptor, self).glBeginQuery(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glProgramUniformMatrix4x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix4x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glProgramUniformMatrix4x3fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glGetVertexAttribfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribfv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glGetVertexAttribfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @overload
    def glGetBufferPointerv(self, arg0: int, arg1: int) -> 'Buffer':
        """public java.nio.Buffer com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBufferPointerv(int,int)"""
        return 'Buffer'._wrap(super(_GL30Interceptor, self).glGetBufferPointerv(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def glProgramUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glProgramUniformMatrix4fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glTexParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @overload
    def glGetUniformLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformLocation(int,java.lang.String)"""
        return int._wrap(super(_GL30Interceptor, self).glGetUniformLocation(_int.valueOf(arg0), arg1))

    @override
    @overload
    def glDebugMessageCallback(self, arg0: 'DebugProc'):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glDebugMessageCallback(com.badlogic.gdx.graphics.GL32$DebugProc)"""
        super(_GL32Interceptor, self).glDebugMessageCallback(arg0)

    @override
    @overload
    def glMinSampleShading(self, arg0: float):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glMinSampleShading(float)"""
        super(_GL32Interceptor, self).glMinSampleShading(_float.valueOf(arg0))

    @override
    @overload
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformBlockName(int,int,java.nio.Buffer,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glGetActiveUniformBlockName(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def glGetInteger64v(self, arg0: int, arg1: 'LongBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetInteger64v(int,java.nio.LongBuffer)"""
        super(_GL30Interceptor, self).glGetInteger64v(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniformMatrix4x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix4x3fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glGetAttachedShaders(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetAttachedShaders(int,int,java.nio.Buffer,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetAttachedShaders(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def glGetSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetSamplerParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGenRenderbuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenRenderbuffer()"""
        return int._wrap(super(GL30Interceptor, self).glGenRenderbuffer())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def glEndQuery(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEndQuery(int)"""
        super(_GL30Interceptor, self).glEndQuery(_int.valueOf(arg0))

    @override
    @overload
    def glProgramUniform1uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform1uiv(int,int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glProgramUniform1uiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glBlendColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendColor(float,float,float,float)"""
        super(_GL30Interceptor, self).glBlendColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getTextureBindings(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getTextureBindings()"""
        return int._wrap(super(GLInterceptor, self).getTextureBindings())

    @overload
    def glIsEnabledi(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL32Interceptor.glIsEnabledi(int,int)"""
        return bool._wrap(super(_GL32Interceptor, self).glIsEnabledi(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def glCreateShaderProgramv(self, arg0: int, arg1: 'String') -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL31Interceptor.glCreateShaderProgramv(int,java.lang.String[])"""
        return int._wrap(super(_GL31Interceptor, self).glCreateShaderProgramv(_int.valueOf(arg0), arg1))

    @override
    @overload
    def glGenTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTextures(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGenTextures(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetTexParameterfv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glGetTexParameterfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glShaderBinary(self, arg0: int, arg1: 'IntBuffer', arg2: int, arg3: 'Buffer', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glShaderBinary(int,java.nio.IntBuffer,int,java.nio.Buffer,int)"""
        super(_GL30Interceptor, self).glShaderBinary(_int.valueOf(arg0), arg1, _int.valueOf(arg2), arg3, _int.valueOf(arg4))

    @overload
    def glGetActiveAttrib(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer') -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveAttrib(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return str._wrap(super(_GL30Interceptor, self).glGetActiveAttrib(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3))

    @override
    @overload
    def glDrawElementsBaseVertex(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glDrawElementsBaseVertex(int,int,int,java.nio.Buffer,int)"""
        super(_GL32Interceptor, self).glDrawElementsBaseVertex(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, _int.valueOf(arg4))

    @override
    @overload
    def glDisableVertexAttribArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDisableVertexAttribArray(int)"""
        super(_GL30Interceptor, self).glDisableVertexAttribArray(_int.valueOf(arg0))

    @override
    @overload
    def glInvalidateSubFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: int, arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glInvalidateSubFramebuffer(int,int,java.nio.IntBuffer,int,int,int,int)"""
        super(_GL30Interceptor, self).glInvalidateSubFramebuffer(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6))

    @override
    @overload
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2iv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glUniform2iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTransformFeedbacks(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGenTransformFeedbacks(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glDrawRangeElementsBaseVertex(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'Buffer', arg6: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glDrawRangeElementsBaseVertex(int,int,int,int,int,java.nio.Buffer,int)"""
        super(_GL32Interceptor, self).glDrawRangeElementsBaseVertex(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _int.valueOf(arg6))

    @override
    @overload
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1iv(int,int,int[],int)"""
        super(_GL30Interceptor, self).glUniform1iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glGetBooleanv(self, arg0: int, arg1: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBooleanv(int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glGetBooleanv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glDrawArrays(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawArrays(int,int,int)"""
        super(_GL30Interceptor, self).glDrawArrays(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4fv(int,int,float[],int)"""
        super(_GL30Interceptor, self).glUniform4fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glDepthFunc(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDepthFunc(int)"""
        super(_GL30Interceptor, self).glDepthFunc(_int.valueOf(arg0))

    @overload
    def glGetStringi(self, arg0: int, arg1: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetStringi(int,int)"""
        return str._wrap(super(_GL30Interceptor, self).glGetStringi(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def glFramebufferTexture2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFramebufferTexture2D(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glFramebufferTexture2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @overload
    def glCheckFramebufferStatus(self, arg0: int) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCheckFramebufferStatus(int)"""
        return int._wrap(super(_GL30Interceptor, self).glCheckFramebufferStatus(_int.valueOf(arg0)))

    @overload
    def glIsProgram(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsProgram(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsProgram(_int.valueOf(arg0)))

    @override
    @overload
    def glFramebufferTexture(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glFramebufferTexture(int,int,int,int)"""
        super(_GL32Interceptor, self).glFramebufferTexture(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glProgramUniformMatrix3x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix3x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glProgramUniformMatrix3x2fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glDeleteQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteQueries(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDeleteQueries(_int.valueOf(arg0), arg1)

    @overload
    def glIsProgramPipeline(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL31Interceptor.glIsProgramPipeline(int)"""
        return bool._wrap(super(_GL31Interceptor, self).glIsProgramPipeline(_int.valueOf(arg0)))

    @overload
    def glGetDebugMessageLog(self, arg0: int, arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: 'IntBuffer', arg6: 'ByteBuffer') -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL32Interceptor.glGetDebugMessageLog(int,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.ByteBuffer)"""
        return int._wrap(super(_GL32Interceptor, self).glGetDebugMessageLog(_int.valueOf(arg0), arg1, arg2, arg3, arg4, arg5, arg6))

    @override
    @overload
    def glBlendFuncSeparatei(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glBlendFuncSeparatei(int,int,int,int,int)"""
        super(_GL32Interceptor, self).glBlendFuncSeparatei(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glGetUniformIndices(self, arg0: int, arg1: 'String', arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformIndices(int,java.lang.String[],java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetUniformIndices(_int.valueOf(arg0), arg1, arg2)

    @override
    @overload
    def glGenQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenQueries(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGenQueries(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetUniformiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetUniformiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGenSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenSamplers(int,int[],int)"""
        super(_GL30Interceptor, self).glGenSamplers(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def glTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameterfv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glTexParameterfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glMemoryBarrier(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glMemoryBarrier(int)"""
        super(_GL31Interceptor, self).glMemoryBarrier(_int.valueOf(arg0))

    @override
    @overload
    def glGetVertexAttribPointerv(self, arg0: int, arg1: int, arg2: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribPointerv(int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glGetVertexAttribPointerv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3fv(int,int,float[],int)"""
        super(_GL30Interceptor, self).glUniform3fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTransformFeedbacks(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDeleteTransformFeedbacks(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glSampleCoverage(self, arg0: float, arg1: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSampleCoverage(float,boolean)"""
        super(_GL30Interceptor, self).glSampleCoverage(_float.valueOf(arg0), _boolean.valueOf(arg1))

    @override
    @overload
    def glFramebufferRenderbuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFramebufferRenderbuffer(int,int,int,int)"""
        super(_GL30Interceptor, self).glFramebufferRenderbuffer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3iv(int,int,int[],int)"""
        super(_GL30Interceptor, self).glUniform3iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1fv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniform1fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGenBuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenBuffer()"""
        return int._wrap(super(GL30Interceptor, self).glGenBuffer())

    @override
    @overload
    def glProgramUniformMatrix2x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix2x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glProgramUniformMatrix2x4fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glVertexAttrib4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib4f(int,float,float,float,float)"""
        super(_GL30Interceptor, self).glVertexAttrib4f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @staticmethod
    @overload
    def resolveErrorNumber(arg0: int) -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.profiling.GLInterceptor.resolveErrorNumber(int)"""
        return str._wrap(_GLInterceptor.resolveErrorNumber(_int.valueOf(arg0)))

    @override
    @overload
    def glBlendEquationSeparate(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendEquationSeparate(int,int)"""
        super(_GL30Interceptor, self).glBlendEquationSeparate(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage3D(int,int,int,int,int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glTexImage3D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9))

    @override
    @overload
    def glProgramUniform4uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform4uiv(int,int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glProgramUniform4uiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform2f(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2f(int,float,float)"""
        super(_GL30Interceptor, self).glUniform2f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def glDeleteProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteProgram(int)"""
        super(_GL30Interceptor, self).glDeleteProgram(_int.valueOf(arg0))

    @override
    @overload
    def glBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBufferSubData(int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glBufferSubData(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def glBindSampler(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindSampler(int,int)"""
        super(_GL30Interceptor, self).glBindSampler(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glGetnUniformfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glGetnUniformfv(int,int,java.nio.FloatBuffer)"""
        super(_GL32Interceptor, self).glGetnUniformfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDrawElementsInstancedBaseVertex(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glDrawElementsInstancedBaseVertex(int,int,int,int,int,int)"""
        super(_GL32Interceptor, self).glDrawElementsInstancedBaseVertex(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @override
    @overload
    def glGetVertexAttribIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribIiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetVertexAttribIiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glBlendEquationSeparatei(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glBlendEquationSeparatei(int,int,int)"""
        super(_GL32Interceptor, self).glBlendEquationSeparatei(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glFramebufferTextureLayer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFramebufferTextureLayer(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glFramebufferTextureLayer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glClearBufferuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferuiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glClearBufferuiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glProgramUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform4iv(int,int,java.nio.IntBuffer)"""
        super(_GL31Interceptor, self).glProgramUniform4iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2fv(int,int,float[],int)"""
        super(_GL30Interceptor, self).glUniform2fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glProgramUniformMatrix2x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix2x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL31Interceptor, self).glProgramUniformMatrix2x3fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glSamplerParameterIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glSamplerParameterIuiv(int,int,java.nio.IntBuffer)"""
        super(_GL32Interceptor, self).glSamplerParameterIuiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage2D(int,int,int,int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glTexSubImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8)) 
 
 
# CLASS: com.badlogic.gdx.graphics.profiling.GL30Interceptor
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.math.FloatCounter as _FloatCounter
_FloatCounter = _FloatCounter
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.nio.IntBuffer as IntBuffer
import java.lang.Object as _object
from builtins import type
import java.nio.Buffer as _Buffer
_Buffer = _Buffer
import com.badlogic.gdx.graphics.profiling.GL30Interceptor as _GL30Interceptor
_GL30Interceptor = _GL30Interceptor
from builtins import float
import java.nio.LongBuffer as LongBuffer
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.profiling.GLInterceptor as _GLInterceptor
_GLInterceptor = _GLInterceptor
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.nio.Buffer as Buffer
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GL30Interceptor():
    """com.badlogic.gdx.graphics.profiling.GL30Interceptor"""
 
    @staticmethod
    def _wrap(java_value: _GL30Interceptor) -> 'GL30Interceptor':
        return GL30Interceptor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GL30Interceptor):
        """
        Dynamic initializer for GL30Interceptor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GL30Interceptor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GL30Interceptor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def glIsBuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsBuffer(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsBuffer(_int.valueOf(arg0)))

    @override
    @overload
    def glCopyBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyBufferSubData(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glCopyBufferSubData(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glPauseTransformFeedback(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glPauseTransformFeedback()"""
        super(GL30Interceptor, self).glPauseTransformFeedback()

    @override
    @overload
    def getVertexCount(self) -> 'math.FloatCounter':
        """public com.badlogic.gdx.math.FloatCounter com.badlogic.gdx.graphics.profiling.GLInterceptor.getVertexCount()"""
        return 'math.FloatCounter'._wrap(super(GLInterceptor, self).getVertexCount())

    @override
    @overload
    def glDeleteSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteSamplers(int,int[],int)"""
        super(_GL30Interceptor, self).glDeleteSamplers(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def glUniform3uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3uiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glUniform3uiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDetachShader(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDetachShader(int,int)"""
        super(_GL30Interceptor, self).glDetachShader(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3fv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniform3fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGenSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenSamplers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGenSamplers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glDeleteVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteVertexArrays(int,int[],int)"""
        super(_GL30Interceptor, self).glDeleteVertexArrays(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def glGenVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenVertexArrays(int,int[],int)"""
        super(_GL30Interceptor, self).glGenVertexArrays(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def glClear(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClear(int)"""
        super(_GL30Interceptor, self).glClear(_int.valueOf(arg0))

    @override
    @overload
    def glUniform4uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4uiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glUniform4uiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteTexture(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTexture(int)"""
        super(_GL30Interceptor, self).glDeleteTexture(_int.valueOf(arg0))

    @override
    @overload
    def glDepthMask(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDepthMask(boolean)"""
        super(_GL30Interceptor, self).glDepthMask(_boolean.valueOf(arg0))

    @override
    @overload
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1fv(int,int,float[],int)"""
        super(_GL30Interceptor, self).glUniform1fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3i(int,int,int,int)"""
        super(_GL30Interceptor, self).glUniform3i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glGetQueryObjectuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetQueryObjectuiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetQueryObjectuiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glSamplerParameterfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glBindRenderbuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindRenderbuffer(int,int)"""
        super(_GL30Interceptor, self).glBindRenderbuffer(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glGetShaderiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetShaderiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetShaderiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glPixelStorei(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glPixelStorei(int,int)"""
        super(_GL30Interceptor, self).glPixelStorei(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glGetTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetTexParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetTexParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetVertexAttribIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribIuiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetVertexAttribIuiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glSamplerParameterf(self, arg0: int, arg1: int, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameterf(int,int,float)"""
        super(_GL30Interceptor, self).glSamplerParameterf(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glTexSubImage3D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), arg10)

    @override
    @overload
    def glDisable(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDisable(int)"""
        super(_GL30Interceptor, self).glDisable(_int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def glSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glSamplerParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform1uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1uiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glUniform1uiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDrawArraysInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawArraysInstanced(int,int,int,int)"""
        super(_GL30Interceptor, self).glDrawArraysInstanced(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def glIsVertexArray(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsVertexArray(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsVertexArray(_int.valueOf(arg0)))

    @override
    @overload
    def glUniformMatrix4x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix4x2fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glColorMask(self, arg0: bool, arg1: bool, arg2: bool, arg3: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glColorMask(boolean,boolean,boolean,boolean)"""
        super(_GL30Interceptor, self).glColorMask(_boolean.valueOf(arg0), _boolean.valueOf(arg1), _boolean.valueOf(arg2), _boolean.valueOf(arg3))

    @override
    @overload
    def glPolygonOffset(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glPolygonOffset(float,float)"""
        super(_GL30Interceptor, self).glPolygonOffset(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def glBlendFunc(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendFunc(int,int)"""
        super(_GL30Interceptor, self).glBlendFunc(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glShaderSource(self, arg0: int, arg1: str):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glShaderSource(int,java.lang.String)"""
        super(_GL30Interceptor, self).glShaderSource(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetUniformfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformfv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glGetUniformfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteSamplers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDeleteSamplers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def glUniformMatrix3x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix3x4fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @overload
    def glGetFragDataLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetFragDataLocation(int,java.lang.String)"""
        return int._wrap(super(_GL30Interceptor, self).glGetFragDataLocation(_int.valueOf(arg0), arg1))

    @override
    @overload
    def glClearBufferfi(self, arg0: int, arg1: int, arg2: float, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferfi(int,int,float,int)"""
        super(_GL30Interceptor, self).glClearBufferfi(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glUseProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUseProgram(int)"""
        super(_GL30Interceptor, self).glUseProgram(_int.valueOf(arg0))

    @override
    @overload
    def glUniformBlockBinding(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformBlockBinding(int,int,int)"""
        super(_GL30Interceptor, self).glUniformBlockBinding(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glCopyTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyTexImage2D(int,int,int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glCopyTexImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7))

    @override
    @overload
    def glViewport(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glViewport(int,int,int,int)"""
        super(_GL30Interceptor, self).glViewport(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glClearColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearColor(float,float,float,float)"""
        super(_GL30Interceptor, self).glClearColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def glGetProgramiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetProgramiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetProgramiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glCreateProgram(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCreateProgram()"""
        return int._wrap(super(GL30Interceptor, self).glCreateProgram())

    @override
    @overload
    def glDeleteQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteQueries(int,int[],int)"""
        super(_GL30Interceptor, self).glDeleteQueries(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def glBindTexture(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindTexture(int,int)"""
        super(_GL30Interceptor, self).glBindTexture(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glGenVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenVertexArrays(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGenVertexArrays(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4i(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glUniform4i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage3D(int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glTexImage3D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), arg9)

    @override
    @overload
    def glGetError(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetError()"""
        return int._wrap(super(GL30Interceptor, self).glGetError())

    @override
    @overload
    def glScissor(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glScissor(int,int,int,int)"""
        super(_GL30Interceptor, self).glScissor(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glGetShaderPrecisionFormat(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetShaderPrecisionFormat(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetShaderPrecisionFormat(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3)

    @overload
    def glGetActiveUniform(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer') -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniform(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return str._wrap(super(_GL30Interceptor, self).glGetActiveUniform(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3))

    @override
    @overload
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4fv(int,int,boolean,float[],int)"""
        super(_GL30Interceptor, self).glUniformMatrix4fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3, _int.valueOf(arg4))

    @override
    @overload
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix4fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glStencilMaskSeparate(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilMaskSeparate(int,int)"""
        super(_GL30Interceptor, self).glStencilMaskSeparate(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glVertexAttrib2f(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib2f(int,float,float)"""
        super(_GL30Interceptor, self).glVertexAttrib2f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def glSamplerParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameteri(int,int,int)"""
        super(_GL30Interceptor, self).glSamplerParameteri(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glGetBufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBufferParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetBufferParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glBlitFramebuffer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlitFramebuffer(int,int,int,int,int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glBlitFramebuffer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9))

    @override
    @overload
    def glBlendFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendFuncSeparate(int,int,int,int)"""
        super(_GL30Interceptor, self).glBlendFuncSeparate(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glTransformFeedbackVaryings(self, arg0: int, arg1: 'String', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTransformFeedbackVaryings(int,java.lang.String[],int)"""
        super(_GL30Interceptor, self).glTransformFeedbackVaryings(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def glGenRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenRenderbuffers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGenRenderbuffers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glBindVertexArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindVertexArray(int)"""
        super(_GL30Interceptor, self).glBindVertexArray(_int.valueOf(arg0))

    @override
    @overload
    def glStencilFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilFuncSeparate(int,int,int,int)"""
        super(_GL30Interceptor, self).glStencilFuncSeparate(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glGenQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenQueries(int,int[],int)"""
        super(_GL30Interceptor, self).glGenQueries(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def glBindBufferBase(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindBufferBase(int,int,int)"""
        super(_GL30Interceptor, self).glBindBufferBase(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def getCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getCalls()"""
        return int._wrap(super(GLInterceptor, self).getCalls())

    @overload
    def glIsTexture(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsTexture(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsTexture(_int.valueOf(arg0)))

    @override
    @overload
    def glGetActiveUniformBlockiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformBlockiv(int,int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetActiveUniformBlockiv(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def glEnable(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEnable(int)"""
        super(_GL30Interceptor, self).glEnable(_int.valueOf(arg0))

    @override
    @overload
    def glGenFramebuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenFramebuffer()"""
        return int._wrap(super(GL30Interceptor, self).glGenFramebuffer())

    @override
    @overload
    def glTexParameterf(self, arg0: int, arg1: int, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameterf(int,int,float)"""
        super(_GL30Interceptor, self).glTexParameterf(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def glGetRenderbufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetRenderbufferParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetRenderbufferParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @overload
    def glIsEnabled(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsEnabled(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsEnabled(_int.valueOf(arg0)))

    @override
    @overload
    def getShaderSwitches(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getShaderSwitches()"""
        return int._wrap(super(GLInterceptor, self).getShaderSwitches())

    @override
    @overload
    def glCopyTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyTexSubImage3D(int,int,int,int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glCopyTexSubImage3D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def glGetIntegerv(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetIntegerv(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetIntegerv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glEnableVertexAttribArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEnableVertexAttribArray(int)"""
        super(_GL30Interceptor, self).glEnableVertexAttribArray(_int.valueOf(arg0))

    @override
    @overload
    def glReleaseShaderCompiler(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glReleaseShaderCompiler()"""
        super(GL30Interceptor, self).glReleaseShaderCompiler()

    @override
    @overload
    def glBlendEquation(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendEquation(int)"""
        super(_GL30Interceptor, self).glBlendEquation(_int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2fv(int,int,boolean,float[],int)"""
        super(_GL30Interceptor, self).glUniformMatrix2fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3, _int.valueOf(arg4))

    @overload
    def glMapBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Buffer':
        """public java.nio.Buffer com.badlogic.gdx.graphics.profiling.GL30Interceptor.glMapBufferRange(int,int,int,int)"""
        return 'Buffer'._wrap(super(_GL30Interceptor, self).glMapBufferRange(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def glDepthRangef(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDepthRangef(float,float)"""
        super(_GL30Interceptor, self).glDepthRangef(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def glBindTransformFeedback(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindTransformFeedback(int,int)"""
        super(_GL30Interceptor, self).glBindTransformFeedback(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glGetFloatv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetFloatv(int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glGetFloatv(_int.valueOf(arg0), arg1)

    @overload
    def glIsShader(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsShader(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsShader(_int.valueOf(arg0)))

    @override
    @overload
    def glResumeTransformFeedback(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glResumeTransformFeedback()"""
        super(GL30Interceptor, self).glResumeTransformFeedback()

    @override
    @overload
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTransformFeedbacks(int,int[],int)"""
        super(_GL30Interceptor, self).glDeleteTransformFeedbacks(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def glEndTransformFeedback(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEndTransformFeedback()"""
        super(GL30Interceptor, self).glEndTransformFeedback()

    @override
    @overload
    def glBindBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindBufferRange(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glBindBufferRange(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glAttachShader(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glAttachShader(int,int)"""
        super(_GL30Interceptor, self).glAttachShader(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glCompileShader(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCompileShader(int)"""
        super(_GL30Interceptor, self).glCompileShader(_int.valueOf(arg0))

    @overload
    def glGetShaderInfoLog(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetShaderInfoLog(int)"""
        return str._wrap(super(_GL30Interceptor, self).glGetShaderInfoLog(_int.valueOf(arg0)))

    @overload
    def glGetAttribLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetAttribLocation(int,java.lang.String)"""
        return int._wrap(super(_GL30Interceptor, self).glGetAttribLocation(_int.valueOf(arg0), arg1))

    @overload
    def glIsRenderbuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsRenderbuffer(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsRenderbuffer(_int.valueOf(arg0)))

    @override
    @overload
    def glUniformMatrix2x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix2x3fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawElements(int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glDrawElements(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def glUniform4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4f(int,float,float,float,float)"""
        super(_GL30Interceptor, self).glUniform4f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawElements(int,int,int,int)"""
        super(_GL30Interceptor, self).glDrawElements(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glDeleteFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteFramebuffers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDeleteFramebuffers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glRenderbufferStorage(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glRenderbufferStorage(int,int,int,int)"""
        super(_GL30Interceptor, self).glRenderbufferStorage(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.profiling.GLInterceptor.reset()"""
        super(GLInterceptor, self).reset()

    @override
    @overload
    def glDrawElementsInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawElementsInstanced(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glDrawElementsInstanced(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage2D(int,int,int,int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glTexImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8))

    @override
    @overload
    def glDeleteFramebuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteFramebuffer(int)"""
        super(_GL30Interceptor, self).glDeleteFramebuffer(_int.valueOf(arg0))

    @override
    @overload
    def glGetActiveUniformsiv(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformsiv(int,int,java.nio.IntBuffer,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetActiveUniformsiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), arg4)

    @override
    @overload
    def glTexParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameteri(int,int,int)"""
        super(_GL30Interceptor, self).glTexParameteri(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix3fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glReadPixels(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glReadPixels(int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glReadPixels(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), arg6)

    @override
    @overload
    def glUniform2i(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2i(int,int,int)"""
        super(_GL30Interceptor, self).glUniform2i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2iv(int,int,int[],int)"""
        super(_GL30Interceptor, self).glUniform2iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3fv(int,int,boolean,float[],int)"""
        super(_GL30Interceptor, self).glUniformMatrix3fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3, _int.valueOf(arg4))

    @override
    @overload
    def glUniform1f(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1f(int,float)"""
        super(_GL30Interceptor, self).glUniform1f(_int.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def glVertexAttrib3fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib3fv(int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glVertexAttrib3fv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTransformFeedbacks(int,int[],int)"""
        super(_GL30Interceptor, self).glGenTransformFeedbacks(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def glGetQueryiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetQueryiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetQueryiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetVertexAttribiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetVertexAttribiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4fv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniform4fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @overload
    def glIsFramebuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsFramebuffer(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsFramebuffer(_int.valueOf(arg0)))

    @override
    @overload
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribPointer(int,int,int,boolean,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glVertexAttribPointer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), arg5)

    @overload
    def glGetString(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetString(int)"""
        return str._wrap(super(_GL30Interceptor, self).glGetString(_int.valueOf(arg0)))

    @override
    @overload
    def glDeleteShader(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteShader(int)"""
        super(_GL30Interceptor, self).glDeleteShader(_int.valueOf(arg0))

    @override
    @overload
    def glClearBufferiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glClearBufferiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glVertexAttrib2fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib2fv(int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glVertexAttrib2fv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1iv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glUniform1iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4iv(int,int,int[],int)"""
        super(_GL30Interceptor, self).glUniform4iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @overload
    def glGetUniformBlockIndex(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformBlockIndex(int,java.lang.String)"""
        return int._wrap(super(_GL30Interceptor, self).glGetUniformBlockIndex(_int.valueOf(arg0), arg1))

    @override
    @overload
    def glStencilOpSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilOpSeparate(int,int,int,int)"""
        super(_GL30Interceptor, self).glStencilOpSeparate(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glTexSubImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), arg8)

    @override
    @overload
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2fv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniform2fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribPointer(int,int,int,boolean,int,int)"""
        super(_GL30Interceptor, self).glVertexAttribPointer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @override
    @overload
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawRangeElements(int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glDrawRangeElements(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @override
    @overload
    def glVertexAttribI4ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribI4ui(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glVertexAttribI4ui(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glBindAttribLocation(self, arg0: int, arg1: int, arg2: str):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindAttribLocation(int,int,java.lang.String)"""
        super(_GL30Interceptor, self).glBindAttribLocation(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetFramebufferAttachmentParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetFramebufferAttachmentParameteriv(int,int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetFramebufferAttachmentParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def glFrontFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFrontFace(int)"""
        super(_GL30Interceptor, self).glFrontFace(_int.valueOf(arg0))

    @override
    @overload
    def glVertexAttribI4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribI4i(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glVertexAttribI4i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glCompressedTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCompressedTexImage2D(int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glCompressedTexImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), arg7)

    @override
    @overload
    def glGetBufferParameteri64v(self, arg0: int, arg1: int, arg2: 'LongBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBufferParameteri64v(int,int,java.nio.LongBuffer)"""
        super(_GL30Interceptor, self).glGetBufferParameteri64v(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteBuffers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDeleteBuffers(_int.valueOf(arg0), arg1)

    @overload
    def glIsTransformFeedback(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsTransformFeedback(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsTransformFeedback(_int.valueOf(arg0)))

    @override
    @overload
    def glDeleteTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTextures(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDeleteTextures(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glFlush(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFlush()"""
        super(GL30Interceptor, self).glFlush()

    @override
    @overload
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix2fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glTexSubImage3D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10))

    @override
    @overload
    def glCompressedTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCompressedTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glCompressedTexSubImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), arg8)

    @override
    @overload
    def glGetSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glGetSamplerParameterfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteRenderbuffers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDeleteRenderbuffers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glGenFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenFramebuffers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGenFramebuffers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glVertexAttrib1fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib1fv(int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glVertexAttrib1fv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glGenerateMipmap(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenerateMipmap(int)"""
        super(_GL30Interceptor, self).glGenerateMipmap(_int.valueOf(arg0))

    @override
    @overload
    def glGenBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenBuffers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGenBuffers(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glFlushMappedBufferRange(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFlushMappedBufferRange(int,int,int)"""
        super(_GL30Interceptor, self).glFlushMappedBufferRange(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glClearDepthf(self, arg0: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearDepthf(float)"""
        super(_GL30Interceptor, self).glClearDepthf(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def glRenderbufferStorageMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glRenderbufferStorageMultisample(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glRenderbufferStorageMultisample(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glUniform1i(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1i(int,int)"""
        super(_GL30Interceptor, self).glUniform1i(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glValidateProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glValidateProgram(int)"""
        super(_GL30Interceptor, self).glValidateProgram(_int.valueOf(arg0))

    @override
    @overload
    def glStencilOp(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilOp(int,int,int)"""
        super(_GL30Interceptor, self).glStencilOp(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glUniformMatrix2x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix2x4fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glCopyTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyTexSubImage2D(int,int,int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glCopyTexSubImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7))

    @override
    @overload
    def glLinkProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glLinkProgram(int)"""
        super(_GL30Interceptor, self).glLinkProgram(_int.valueOf(arg0))

    @override
    @overload
    def glDrawBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawBuffers(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDrawBuffers(_int.valueOf(arg0), arg1)

    @overload
    def glUnmapBuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUnmapBuffer(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glUnmapBuffer(_int.valueOf(arg0)))

    @override
    @overload
    def glVertexAttribDivisor(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribDivisor(int,int)"""
        super(_GL30Interceptor, self).glVertexAttribDivisor(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glStencilFunc(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilFunc(int,int,int)"""
        super(_GL30Interceptor, self).glStencilFunc(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glGetUniformuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformuiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetUniformuiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glCullFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCullFace(int)"""
        super(_GL30Interceptor, self).glCullFace(_int.valueOf(arg0))

    @override
    @overload
    def glHint(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glHint(int,int)"""
        super(_GL30Interceptor, self).glHint(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glProgramParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glProgramParameteri(int,int,int)"""
        super(_GL30Interceptor, self).glProgramParameteri(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3iv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glUniform3iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @overload
    def glCreateShader(self, arg0: int) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCreateShader(int)"""
        return int._wrap(super(_GL30Interceptor, self).glCreateShader(_int.valueOf(arg0)))

    @override
    @overload
    def glDeleteBuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteBuffer(int)"""
        super(_GL30Interceptor, self).glDeleteBuffer(_int.valueOf(arg0))

    @override
    @overload
    def glBeginTransformFeedback(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBeginTransformFeedback(int)"""
        super(_GL30Interceptor, self).glBeginTransformFeedback(_int.valueOf(arg0))

    @override
    @overload
    def glClearBufferfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferfv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glClearBufferfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glActiveTexture(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glActiveTexture(int)"""
        super(_GL30Interceptor, self).glActiveTexture(_int.valueOf(arg0))

    @override
    @overload
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4iv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glUniform4iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteVertexArrays(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDeleteVertexArrays(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glVertexAttrib4fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib4fv(int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glVertexAttrib4fv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glBindBuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindBuffer(int,int)"""
        super(_GL30Interceptor, self).glBindBuffer(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glVertexAttribIPointer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribIPointer(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glVertexAttribIPointer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @overload
    def glIsQuery(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsQuery(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsQuery(_int.valueOf(arg0)))

    @override
    @overload
    def glGenTexture(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTexture()"""
        return int._wrap(super(GL30Interceptor, self).glGenTexture())

    @override
    @overload
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawRangeElements(int,int,int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glDrawRangeElements(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5)

    @override
    @overload
    def glBufferData(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBufferData(int,int,java.nio.Buffer,int)"""
        super(_GL30Interceptor, self).glBufferData(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def getDrawCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getDrawCalls()"""
        return int._wrap(super(GLInterceptor, self).getDrawCalls())

    @override
    @overload
    def glFinish(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFinish()"""
        super(GL30Interceptor, self).glFinish()

    @override
    @overload
    def glDeleteRenderbuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteRenderbuffer(int)"""
        super(_GL30Interceptor, self).glDeleteRenderbuffer(_int.valueOf(arg0))

    @override
    @overload
    def glVertexAttrib1f(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib1f(int,float)"""
        super(_GL30Interceptor, self).glVertexAttrib1f(_int.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def glIsSampler(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsSampler(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsSampler(_int.valueOf(arg0)))

    @override
    @overload
    def glInvalidateFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glInvalidateFramebuffer(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glInvalidateFramebuffer(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glLineWidth(self, arg0: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glLineWidth(float)"""
        super(_GL30Interceptor, self).glLineWidth(_float.valueOf(arg0))

    @override
    @overload
    def glStencilMask(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilMask(int)"""
        super(_GL30Interceptor, self).glStencilMask(_int.valueOf(arg0))

    @override
    @overload
    def glBindFramebuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindFramebuffer(int,int)"""
        super(_GL30Interceptor, self).glBindFramebuffer(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def glUniformMatrix3x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix3x2fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @overload
    def glGetProgramInfoLog(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetProgramInfoLog(int)"""
        return str._wrap(super(_GL30Interceptor, self).glGetProgramInfoLog(_int.valueOf(arg0)))

    @override
    @overload
    def glClearStencil(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearStencil(int)"""
        super(_GL30Interceptor, self).glClearStencil(_int.valueOf(arg0))

    @override
    @overload
    def glReadBuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glReadBuffer(int)"""
        super(_GL30Interceptor, self).glReadBuffer(_int.valueOf(arg0))

    @override
    @overload
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glTexImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), arg8)

    @override
    @overload
    def glUniform3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3f(int,float,float,float)"""
        super(_GL30Interceptor, self).glUniform3f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformBlockName(int,int)"""
        return str._wrap(super(_GL30Interceptor, self).glGetActiveUniformBlockName(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def glVertexAttrib3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib3f(int,float,float,float)"""
        super(_GL30Interceptor, self).glVertexAttrib3f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def glBeginQuery(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBeginQuery(int,int)"""
        super(_GL30Interceptor, self).glBeginQuery(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glGetVertexAttribfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribfv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glGetVertexAttribfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @overload
    def glGetBufferPointerv(self, arg0: int, arg1: int) -> 'Buffer':
        """public java.nio.Buffer com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBufferPointerv(int,int)"""
        return 'Buffer'._wrap(super(_GL30Interceptor, self).glGetBufferPointerv(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def glTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glTexParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @overload
    def glGetUniformLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformLocation(int,java.lang.String)"""
        return int._wrap(super(_GL30Interceptor, self).glGetUniformLocation(_int.valueOf(arg0), arg1))

    @override
    @overload
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformBlockName(int,int,java.nio.Buffer,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glGetActiveUniformBlockName(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def glGetInteger64v(self, arg0: int, arg1: 'LongBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetInteger64v(int,java.nio.LongBuffer)"""
        super(_GL30Interceptor, self).glGetInteger64v(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniformMatrix4x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniformMatrix4x3fv(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glGetAttachedShaders(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetAttachedShaders(int,int,java.nio.Buffer,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetAttachedShaders(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def glGetSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetSamplerParameteriv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGenRenderbuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenRenderbuffer()"""
        return int._wrap(super(GL30Interceptor, self).glGenRenderbuffer())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def glEndQuery(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEndQuery(int)"""
        super(_GL30Interceptor, self).glEndQuery(_int.valueOf(arg0))

    @override
    @overload
    def glBlendColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendColor(float,float,float,float)"""
        super(_GL30Interceptor, self).glBlendColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getTextureBindings(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getTextureBindings()"""
        return int._wrap(super(GLInterceptor, self).getTextureBindings())

    @override
    @overload
    def glGenTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTextures(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGenTextures(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetTexParameterfv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glGetTexParameterfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glShaderBinary(self, arg0: int, arg1: 'IntBuffer', arg2: int, arg3: 'Buffer', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glShaderBinary(int,java.nio.IntBuffer,int,java.nio.Buffer,int)"""
        super(_GL30Interceptor, self).glShaderBinary(_int.valueOf(arg0), arg1, _int.valueOf(arg2), arg3, _int.valueOf(arg4))

    @overload
    def glGetActiveAttrib(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer') -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveAttrib(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return str._wrap(super(_GL30Interceptor, self).glGetActiveAttrib(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3))

    @override
    @overload
    def glDisableVertexAttribArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDisableVertexAttribArray(int)"""
        super(_GL30Interceptor, self).glDisableVertexAttribArray(_int.valueOf(arg0))

    @override
    @overload
    def glInvalidateSubFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: int, arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glInvalidateSubFramebuffer(int,int,java.nio.IntBuffer,int,int,int,int)"""
        super(_GL30Interceptor, self).glInvalidateSubFramebuffer(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6))

    @override
    @overload
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2iv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glUniform2iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTransformFeedbacks(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGenTransformFeedbacks(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1iv(int,int,int[],int)"""
        super(_GL30Interceptor, self).glUniform1iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glGetBooleanv(self, arg0: int, arg1: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBooleanv(int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glGetBooleanv(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glDrawArrays(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawArrays(int,int,int)"""
        super(_GL30Interceptor, self).glDrawArrays(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4fv(int,int,float[],int)"""
        super(_GL30Interceptor, self).glUniform4fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glDepthFunc(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDepthFunc(int)"""
        super(_GL30Interceptor, self).glDepthFunc(_int.valueOf(arg0))

    @overload
    def glGetStringi(self, arg0: int, arg1: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetStringi(int,int)"""
        return str._wrap(super(_GL30Interceptor, self).glGetStringi(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def glFramebufferTexture2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFramebufferTexture2D(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glFramebufferTexture2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @overload
    def glCheckFramebufferStatus(self, arg0: int) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCheckFramebufferStatus(int)"""
        return int._wrap(super(_GL30Interceptor, self).glCheckFramebufferStatus(_int.valueOf(arg0)))

    @overload
    def glIsProgram(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsProgram(int)"""
        return bool._wrap(super(_GL30Interceptor, self).glIsProgram(_int.valueOf(arg0)))

    @override
    @overload
    def glDeleteQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteQueries(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDeleteQueries(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetUniformIndices(self, arg0: int, arg1: 'String', arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformIndices(int,java.lang.String[],java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetUniformIndices(_int.valueOf(arg0), arg1, arg2)

    @override
    @overload
    def glGenQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenQueries(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGenQueries(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetUniformiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetUniformiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGenSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenSamplers(int,int[],int)"""
        super(_GL30Interceptor, self).glGenSamplers(_int.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def glTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameterfv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glTexParameterfv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetVertexAttribPointerv(self, arg0: int, arg1: int, arg2: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribPointerv(int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glGetVertexAttribPointerv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3fv(int,int,float[],int)"""
        super(_GL30Interceptor, self).glUniform3fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTransformFeedbacks(int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glDeleteTransformFeedbacks(_int.valueOf(arg0), arg1)

    @override
    @overload
    def glSampleCoverage(self, arg0: float, arg1: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSampleCoverage(float,boolean)"""
        super(_GL30Interceptor, self).glSampleCoverage(_float.valueOf(arg0), _boolean.valueOf(arg1))

    @override
    @overload
    def glFramebufferRenderbuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFramebufferRenderbuffer(int,int,int,int)"""
        super(_GL30Interceptor, self).glFramebufferRenderbuffer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3iv(int,int,int[],int)"""
        super(_GL30Interceptor, self).glUniform3iv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1fv(int,int,java.nio.FloatBuffer)"""
        super(_GL30Interceptor, self).glUniform1fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glGenBuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenBuffer()"""
        return int._wrap(super(GL30Interceptor, self).glGenBuffer())

    @override
    @overload
    def glVertexAttrib4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib4f(int,float,float,float,float)"""
        super(_GL30Interceptor, self).glVertexAttrib4f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @staticmethod
    @overload
    def resolveErrorNumber(arg0: int) -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.profiling.GLInterceptor.resolveErrorNumber(int)"""
        return str._wrap(_GLInterceptor.resolveErrorNumber(_int.valueOf(arg0)))

    @override
    @overload
    def glBlendEquationSeparate(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendEquationSeparate(int,int)"""
        super(_GL30Interceptor, self).glBlendEquationSeparate(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage3D(int,int,int,int,int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glTexImage3D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9))

    @override
    @overload
    def glUniform2f(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2f(int,float,float)"""
        super(_GL30Interceptor, self).glUniform2f(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def glDeleteProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteProgram(int)"""
        super(_GL30Interceptor, self).glDeleteProgram(_int.valueOf(arg0))

    @override
    @overload
    def glBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBufferSubData(int,int,int,java.nio.Buffer)"""
        super(_GL30Interceptor, self).glBufferSubData(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def glBindSampler(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindSampler(int,int)"""
        super(_GL30Interceptor, self).glBindSampler(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def glGetVertexAttribIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribIiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glGetVertexAttribIiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glFramebufferTextureLayer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFramebufferTextureLayer(int,int,int,int,int)"""
        super(_GL30Interceptor, self).glFramebufferTextureLayer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def glClearBufferuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferuiv(int,int,java.nio.IntBuffer)"""
        super(_GL30Interceptor, self).glClearBufferuiv(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2fv(int,int,float[],int)"""
        super(_GL30Interceptor, self).glUniform2fv(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage2D(int,int,int,int,int,int,int,int,int)"""
        super(_GL30Interceptor, self).glTexSubImage2D(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8)) 
 
 
# CLASS: com.badlogic.gdx.graphics.profiling.GLErrorListener
import com.badlogic.gdx.graphics.profiling.GLErrorListener as _GLErrorListener
_GLErrorListener = _GLErrorListener
from abc import abstractmethod, ABC
 
class GLErrorListener():
    """com.badlogic.gdx.graphics.profiling.GLErrorListener"""
 
    @staticmethod
    def _wrap(java_value: _GLErrorListener) -> 'GLErrorListener':
        return GLErrorListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLErrorListener):
        """
        Dynamic initializer for GLErrorListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLErrorListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLErrorListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onError(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.profiling.GLErrorListener.onError(int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.profiling.GLProfiler
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

import com.badlogic.gdx.math.FloatCounter as _FloatCounter
_FloatCounter = _FloatCounter
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.profiling.GLProfiler as _GLProfiler
_GLProfiler = _GLProfiler
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.profiling.GLErrorListener as _GLErrorListener
_GLErrorListener = _GLErrorListener
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
 
class GLProfiler():
    """com.badlogic.gdx.graphics.profiling.GLProfiler"""
 
    @staticmethod
    def _wrap(java_value: _GLProfiler) -> 'GLProfiler':
        return GLProfiler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLProfiler):
        """
        Dynamic initializer for GLProfiler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLProfiler__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLProfiler__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getShaderSwitches(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLProfiler.getShaderSwitches()"""
        return int._wrap(super(GLProfiler, self).getShaderSwitches())

    @overload
    def getCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLProfiler.getCalls()"""
        return int._wrap(super(GLProfiler, self).getCalls())

    @overload
    def getDrawCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLProfiler.getDrawCalls()"""
        return int._wrap(super(GLProfiler, self).getDrawCalls())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setListener(self, arg0: 'GLErrorListener'):
        """public void com.badlogic.gdx.graphics.profiling.GLProfiler.setListener(com.badlogic.gdx.graphics.profiling.GLErrorListener)"""
        super(_GLProfiler, self).setListener(arg0)

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
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GLProfiler.isEnabled()"""
        return bool._wrap(super(GLProfiler, self).isEnabled())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getVertexCount(self) -> 'math.FloatCounter':
        """public com.badlogic.gdx.math.FloatCounter com.badlogic.gdx.graphics.profiling.GLProfiler.getVertexCount()"""
        return 'math.FloatCounter'._wrap(super(GLProfiler, self).getVertexCount())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getListener(self) -> 'GLErrorListener':
        """public com.badlogic.gdx.graphics.profiling.GLErrorListener com.badlogic.gdx.graphics.profiling.GLProfiler.getListener()"""
        return 'GLErrorListener'._wrap(super(GLProfiler, self).getListener())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def enable(self):
        """public void com.badlogic.gdx.graphics.profiling.GLProfiler.enable()"""
        super(GLProfiler, self).enable()

    @overload
    def disable(self):
        """public void com.badlogic.gdx.graphics.profiling.GLProfiler.disable()"""
        super(GLProfiler, self).disable()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Graphics'):
        """public com.badlogic.gdx.graphics.profiling.GLProfiler(com.badlogic.gdx.Graphics)"""
        val = _GLProfiler(arg0)
        self.__wrapper = val

    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.profiling.GLProfiler.reset()"""
        super(GLProfiler, self).reset()

    @overload
    def getTextureBindings(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLProfiler.getTextureBindings()"""
        return int._wrap(super(GLProfiler, self).getTextureBindings())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())