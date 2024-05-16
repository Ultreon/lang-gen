from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.graphics.profiling.GLInterceptor as __GLInterceptor
__GLInterceptor = __GLInterceptor
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import com.badlogic.gdx.graphics.profiling.GL30Interceptor as __GL30Interceptor
__GL30Interceptor = __GL30Interceptor
import java.lang.Object as __object
import java.nio.IntBuffer as IntBuffer
from builtins import type
from builtins import float
import java.nio.LongBuffer as LongBuffer
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Long as __long
import java.lang.Float as __float
import com.badlogic.gdx.math.FloatCounter as __FloatCounter
__FloatCounter = __FloatCounter
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

from builtins import bool
import java.nio.Buffer as __Buffer
__Buffer = __Buffer
from builtins import int
 
class GL30Interceptor():
    """com.badlogic.gdx.graphics.profiling.GL30Interceptor"""
 
    @staticmethod
    def __wrap(java_value: __GL30Interceptor) -> 'GL30Interceptor':
        return GL30Interceptor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GL30Interceptor):
        """
        Dynamic initializer for GL30Interceptor.
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
    def glUniform3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3f(int,float,float,float)"""
        super(__GL30Interceptor, self).glUniform3f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def glPauseTransformFeedback(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glPauseTransformFeedback()"""
        super(GL30Interceptor, self).glPauseTransformFeedback()

    @overload
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformBlockName(int,int)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetActiveUniformBlockName(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def glGetAttribLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetAttribLocation(int,java.lang.String)"""
        return int.__wrap(super(__GL30Interceptor, self).glGetAttribLocation(__int.valueOf(arg0), arg1))

    @override
    @overload
    def glCullFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCullFace(int)"""
        super(__GL30Interceptor, self).glCullFace(__int.valueOf(arg0))

    @override
    @overload
    def glGetSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glGetSamplerParameterfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3iv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform3iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glBindBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindBufferRange(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glBindBufferRange(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glGenBuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenBuffer()"""
        return int.__wrap(super(GL30Interceptor, self).glGenBuffer())

    @override
    @overload
    def glGetTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetTexParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetTexParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteTexture(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTexture(int)"""
        super(__GL30Interceptor, self).glDeleteTexture(__int.valueOf(arg0))

    @override
    @overload
    def glCopyTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyTexSubImage2D(int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glCopyTexSubImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7))

    @override
    @overload
    def glVertexAttribI4ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribI4ui(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glVertexAttribI4ui(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glBindTexture(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindTexture(int,int)"""
        super(__GL30Interceptor, self).glBindTexture(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawRangeElements(int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glDrawRangeElements(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5)

    @override
    @overload
    def glGetIntegerv(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetIntegerv(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetIntegerv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawElements(int,int,int,int)"""
        super(__GL30Interceptor, self).glDrawElements(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def glGetStringi(self, arg0: int, arg1: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetStringi(int,int)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetStringi(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def glLinkProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glLinkProgram(int)"""
        super(__GL30Interceptor, self).glLinkProgram(__int.valueOf(arg0))

    @overload
    def glIsBuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsBuffer(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsBuffer(__int.valueOf(arg0)))

    @override
    @overload
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glTexSubImage3D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), arg10)

    @override
    @overload
    def glClearBufferuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferuiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glClearBufferuiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetQueryiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetQueryiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetQueryiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glClearDepthf(self, arg0: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearDepthf(float)"""
        super(__GL30Interceptor, self).glClearDepthf(__float.valueOf(arg0))

    @override
    @overload
    def glEndQuery(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEndQuery(int)"""
        super(__GL30Interceptor, self).glEndQuery(__int.valueOf(arg0))

    @override
    @overload
    def glCompressedTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCompressedTexImage2D(int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glCompressedTexImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), arg7)

    @override
    @overload
    def glAttachShader(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glAttachShader(int,int)"""
        super(__GL30Interceptor, self).glAttachShader(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glDeleteProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteProgram(int)"""
        super(__GL30Interceptor, self).glDeleteProgram(__int.valueOf(arg0))

    @override
    @overload
    def glTransformFeedbackVaryings(self, arg0: int, arg1: 'String', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTransformFeedbackVaryings(int,java.lang.String[],int)"""
        super(__GL30Interceptor, self).glTransformFeedbackVaryings(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glFlushMappedBufferRange(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFlushMappedBufferRange(int,int,int)"""
        super(__GL30Interceptor, self).glFlushMappedBufferRange(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glTexParameterf(self, arg0: int, arg1: int, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameterf(int,int,float)"""
        super(__GL30Interceptor, self).glTexParameterf(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def glUniform3uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3uiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform3uiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDepthMask(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDepthMask(boolean)"""
        super(__GL30Interceptor, self).glDepthMask(__boolean.valueOf(arg0))

    @override
    @overload
    def glVertexAttrib1f(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib1f(int,float)"""
        super(__GL30Interceptor, self).glVertexAttrib1f(__int.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def glGetBooleanv(self, arg0: int, arg1: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBooleanv(int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glGetBooleanv(__int.valueOf(arg0), arg1)

    @overload
    def glGetActiveAttrib(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer') -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveAttrib(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetActiveAttrib(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3))

    @overload
    def glIsFramebuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsFramebuffer(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsFramebuffer(__int.valueOf(arg0)))

    @override
    @overload
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformBlockName(int,int,java.nio.Buffer,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glGetActiveUniformBlockName(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def glVertexAttribI4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribI4i(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glVertexAttribI4i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glVertexAttrib1fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib1fv(int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glVertexAttrib1fv(__int.valueOf(arg0), arg1)

    @overload
    def glUnmapBuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUnmapBuffer(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glUnmapBuffer(__int.valueOf(arg0)))

    @overload
    def glIsRenderbuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsRenderbuffer(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsRenderbuffer(__int.valueOf(arg0)))

    @override
    @overload
    def glGenTexture(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTexture()"""
        return int.__wrap(super(GL30Interceptor, self).glGenTexture())

    @override
    @overload
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage3D(int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glTexImage3D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), arg9)

    @overload
    def glIsProgram(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsProgram(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsProgram(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def glBindVertexArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindVertexArray(int)"""
        super(__GL30Interceptor, self).glBindVertexArray(__int.valueOf(arg0))

    @override
    @overload
    def glGetQueryObjectuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetQueryObjectuiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetQueryObjectuiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def getTextureBindings(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getTextureBindings()"""
        return int.__wrap(super(GLInterceptor, self).getTextureBindings())

    @override
    @overload
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawRangeElements(int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glDrawRangeElements(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @override
    @overload
    def getDrawCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getDrawCalls()"""
        return int.__wrap(super(GLInterceptor, self).getDrawCalls())

    @override
    @overload
    def glClearBufferfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glClearBufferfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @overload
    def glCreateShader(self, arg0: int) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCreateShader(int)"""
        return int.__wrap(super(__GL30Interceptor, self).glCreateShader(__int.valueOf(arg0)))

    @override
    @overload
    def glGetActiveUniformBlockiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformBlockiv(int,int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetActiveUniformBlockiv(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def glBindBuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindBuffer(int,int)"""
        super(__GL30Interceptor, self).glBindBuffer(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBufferSubData(int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glBufferSubData(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @overload
    def glGetBufferPointerv(self, arg0: int, arg1: int) -> 'Buffer':
        """public java.nio.Buffer com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBufferPointerv(int,int)"""
        return 'Buffer'.__wrap(super(__GL30Interceptor, self).glGetBufferPointerv(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def glDeleteBuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteBuffer(int)"""
        super(__GL30Interceptor, self).glDeleteBuffer(__int.valueOf(arg0))

    @override
    @overload
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTransformFeedbacks(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenTransformFeedbacks(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glClear(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClear(int)"""
        super(__GL30Interceptor, self).glClear(__int.valueOf(arg0))

    @override
    @overload
    def glStencilMask(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilMask(int)"""
        super(__GL30Interceptor, self).glStencilMask(__int.valueOf(arg0))

    @override
    @overload
    def glUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3i(int,int,int,int)"""
        super(__GL30Interceptor, self).glUniform3i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2fv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniform2fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix4fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glGenVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenVertexArrays(int,int[],int)"""
        super(__GL30Interceptor, self).glGenVertexArrays(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glGenQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenQueries(int,int[],int)"""
        super(__GL30Interceptor, self).glGenQueries(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1fv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniform1fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def glBindBufferBase(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindBufferBase(int,int,int)"""
        super(__GL30Interceptor, self).glBindBufferBase(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glDepthFunc(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDepthFunc(int)"""
        super(__GL30Interceptor, self).glDepthFunc(__int.valueOf(arg0))

    @override
    @overload
    def glGenRenderbuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenRenderbuffer()"""
        return int.__wrap(super(GL30Interceptor, self).glGenRenderbuffer())

    @override
    @overload
    def glUniformMatrix3x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix3x2fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glBindAttribLocation(self, arg0: int, arg1: int, arg2: str):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindAttribLocation(int,int,java.lang.String)"""
        super(__GL30Interceptor, self).glBindAttribLocation(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetActiveUniformsiv(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformsiv(int,int,java.nio.IntBuffer,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetActiveUniformsiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), arg4)

    @override
    @overload
    def glClearStencil(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearStencil(int)"""
        super(__GL30Interceptor, self).glClearStencil(__int.valueOf(arg0))

    @override
    @overload
    def glGetVertexAttribPointerv(self, arg0: int, arg1: int, arg2: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribPointerv(int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glGetVertexAttribPointerv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform2i(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2i(int,int,int)"""
        super(__GL30Interceptor, self).glUniform2i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glCompressedTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCompressedTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glCompressedTexSubImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), arg8)

    @override
    @overload
    def glStencilOpSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilOpSeparate(int,int,int,int)"""
        super(__GL30Interceptor, self).glStencilOpSeparate(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glGetAttachedShaders(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetAttachedShaders(int,int,java.nio.Buffer,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetAttachedShaders(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def glReadBuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glReadBuffer(int)"""
        super(__GL30Interceptor, self).glReadBuffer(__int.valueOf(arg0))

    @override
    @overload
    def glGetRenderbufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetRenderbufferParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetRenderbufferParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glClearBufferiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glClearBufferiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glVertexAttrib2fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib2fv(int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glVertexAttrib2fv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glDeleteVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteVertexArrays(int,int[],int)"""
        super(__GL30Interceptor, self).glDeleteVertexArrays(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glColorMask(self, arg0: bool, arg1: bool, arg2: bool, arg3: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glColorMask(boolean,boolean,boolean,boolean)"""
        super(__GL30Interceptor, self).glColorMask(__boolean.valueOf(arg0), __boolean.valueOf(arg1), __boolean.valueOf(arg2), __boolean.valueOf(arg3))

    @overload
    def glIsEnabled(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsEnabled(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsEnabled(__int.valueOf(arg0)))

    @override
    @overload
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glTexImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), arg8)

    @override
    @overload
    def glDrawArrays(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawArrays(int,int,int)"""
        super(__GL30Interceptor, self).glDrawArrays(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glGenTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTextures(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenTextures(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glPolygonOffset(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glPolygonOffset(float,float)"""
        super(__GL30Interceptor, self).glPolygonOffset(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def glUniformMatrix4x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix4x3fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1iv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform1iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteBuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteBuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetSamplerParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glEnableVertexAttribArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEnableVertexAttribArray(int)"""
        super(__GL30Interceptor, self).glEnableVertexAttribArray(__int.valueOf(arg0))

    @override
    @overload
    def glUniform4uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4uiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform4uiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glInvalidateSubFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: int, arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glInvalidateSubFramebuffer(int,int,java.nio.IntBuffer,int,int,int,int)"""
        super(__GL30Interceptor, self).glInvalidateSubFramebuffer(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6))

    @override
    @overload
    def glReleaseShaderCompiler(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glReleaseShaderCompiler()"""
        super(GL30Interceptor, self).glReleaseShaderCompiler()

    @override
    @overload
    def glVertexAttrib3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib3f(int,float,float,float)"""
        super(__GL30Interceptor, self).glVertexAttrib3f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def glDeleteFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteFramebuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteFramebuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetBufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBufferParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetBufferParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDisable(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDisable(int)"""
        super(__GL30Interceptor, self).glDisable(__int.valueOf(arg0))

    @overload
    def glIsTexture(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsTexture(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsTexture(__int.valueOf(arg0)))

    @override
    @overload
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glTexSubImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), arg8)

    @override
    @overload
    def glVertexAttrib4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib4f(int,float,float,float,float)"""
        super(__GL30Interceptor, self).glVertexAttrib4f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def glGetFramebufferAttachmentParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetFramebufferAttachmentParameteriv(int,int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetFramebufferAttachmentParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def glResumeTransformFeedback(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glResumeTransformFeedback()"""
        super(GL30Interceptor, self).glResumeTransformFeedback()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def glGetFloatv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetFloatv(int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glGetFloatv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetVertexAttribIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribIiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetVertexAttribIiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glGenRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenRenderbuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenRenderbuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glEndTransformFeedback(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEndTransformFeedback()"""
        super(GL30Interceptor, self).glEndTransformFeedback()

    @overload
    def glIsVertexArray(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsVertexArray(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsVertexArray(__int.valueOf(arg0)))

    @overload
    def glGetUniformBlockIndex(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformBlockIndex(int,java.lang.String)"""
        return int.__wrap(super(__GL30Interceptor, self).glGetUniformBlockIndex(__int.valueOf(arg0), arg1))

    @override
    @overload
    def glPixelStorei(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glPixelStorei(int,int)"""
        super(__GL30Interceptor, self).glPixelStorei(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glLineWidth(self, arg0: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glLineWidth(float)"""
        super(__GL30Interceptor, self).glLineWidth(__float.valueOf(arg0))

    @override
    @overload
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribPointer(int,int,int,boolean,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glVertexAttribPointer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __int.valueOf(arg4), arg5)

    @override
    @overload
    def glBindTransformFeedback(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindTransformFeedback(int,int)"""
        super(__GL30Interceptor, self).glBindTransformFeedback(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glBlendEquation(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendEquation(int)"""
        super(__GL30Interceptor, self).glBlendEquation(__int.valueOf(arg0))

    @override
    @overload
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4fv(int,int,boolean,float[],int)"""
        super(__GL30Interceptor, self).glUniformMatrix4fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3, __int.valueOf(arg4))

    @override
    @overload
    def glGenerateMipmap(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenerateMipmap(int)"""
        super(__GL30Interceptor, self).glGenerateMipmap(__int.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.profiling.GLInterceptor.reset()"""
        super(GLInterceptor, self).reset()

    @override
    @overload
    def glGenBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenBuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenBuffers(__int.valueOf(arg0), arg1)

    @overload
    def glIsQuery(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsQuery(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsQuery(__int.valueOf(arg0)))

    @override
    @overload
    def glGetTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetTexParameterfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glGetTexParameterfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2iv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform2iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteFramebuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteFramebuffer(int)"""
        super(__GL30Interceptor, self).glDeleteFramebuffer(__int.valueOf(arg0))

    @override
    @overload
    def glSamplerParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameteri(int,int,int)"""
        super(__GL30Interceptor, self).glSamplerParameteri(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glEnable(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEnable(int)"""
        super(__GL30Interceptor, self).glEnable(__int.valueOf(arg0))

    @overload
    def glGetShaderInfoLog(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetShaderInfoLog(int)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetShaderInfoLog(__int.valueOf(arg0)))

    @override
    @overload
    def glUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4i(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glUniform4i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glStencilFunc(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilFunc(int,int,int)"""
        super(__GL30Interceptor, self).glStencilFunc(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glDeleteTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTextures(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteTextures(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2fv(int,int,boolean,float[],int)"""
        super(__GL30Interceptor, self).glUniformMatrix2fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3, __int.valueOf(arg4))

    @override
    @overload
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage2D(int,int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glTexSubImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8))

    @overload
    def glGetProgramInfoLog(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetProgramInfoLog(int)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetProgramInfoLog(__int.valueOf(arg0)))

    @override
    @overload
    def glFrontFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFrontFace(int)"""
        super(__GL30Interceptor, self).glFrontFace(__int.valueOf(arg0))

    @override
    @overload
    def glSamplerParameterf(self, arg0: int, arg1: int, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameterf(int,int,float)"""
        super(__GL30Interceptor, self).glSamplerParameterf(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def glGetUniformiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetUniformiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetBufferParameteri64v(self, arg0: int, arg1: int, arg2: 'LongBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBufferParameteri64v(int,int,java.nio.LongBuffer)"""
        super(__GL30Interceptor, self).glGetBufferParameteri64v(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @overload
    def glGetString(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetString(int)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetString(__int.valueOf(arg0)))

    @overload
    def glGetFragDataLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetFragDataLocation(int,java.lang.String)"""
        return int.__wrap(super(__GL30Interceptor, self).glGetFragDataLocation(__int.valueOf(arg0), arg1))

    @override
    @overload
    def glTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameterfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glTexParameterfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glGenSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenSamplers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenSamplers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glClearBufferfi(self, arg0: int, arg1: int, arg2: float, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferfi(int,int,float,int)"""
        super(__GL30Interceptor, self).glClearBufferfi(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glUniformMatrix2x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix2x3fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def getShaderSwitches(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getShaderSwitches()"""
        return int.__wrap(super(GLInterceptor, self).getShaderSwitches())

    @override
    @overload
    def glGenSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenSamplers(int,int[],int)"""
        super(__GL30Interceptor, self).glGenSamplers(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glRenderbufferStorageMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glRenderbufferStorageMultisample(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glRenderbufferStorageMultisample(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glSamplerParameterfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def getCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getCalls()"""
        return int.__wrap(super(GLInterceptor, self).getCalls())

    @override
    @overload
    def glShaderBinary(self, arg0: int, arg1: 'IntBuffer', arg2: int, arg3: 'Buffer', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glShaderBinary(int,java.nio.IntBuffer,int,java.nio.Buffer,int)"""
        super(__GL30Interceptor, self).glShaderBinary(__int.valueOf(arg0), arg1, __int.valueOf(arg2), arg3, __int.valueOf(arg4))

    @override
    @overload
    def glDisableVertexAttribArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDisableVertexAttribArray(int)"""
        super(__GL30Interceptor, self).glDisableVertexAttribArray(__int.valueOf(arg0))

    @overload
    def glIsShader(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsShader(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsShader(__int.valueOf(arg0)))

    @override
    @overload
    def glDeleteVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteVertexArrays(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteVertexArrays(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glFlush(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFlush()"""
        super(GL30Interceptor, self).glFlush()

    @override
    @overload
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTransformFeedbacks(int,int[],int)"""
        super(__GL30Interceptor, self).glGenTransformFeedbacks(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glVertexAttrib4fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib4fv(int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glVertexAttrib4fv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glDeleteRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteRenderbuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteRenderbuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glGenVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenVertexArrays(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenVertexArrays(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glDrawArraysInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawArraysInstanced(int,int,int,int)"""
        super(__GL30Interceptor, self).glDrawArraysInstanced(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3fv(int,int,float[],int)"""
        super(__GL30Interceptor, self).glUniform3fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @overload
    def glGetUniformLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformLocation(int,java.lang.String)"""
        return int.__wrap(super(__GL30Interceptor, self).glGetUniformLocation(__int.valueOf(arg0), arg1))

    @override
    @overload
    def glShaderSource(self, arg0: int, arg1: str):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glShaderSource(int,java.lang.String)"""
        super(__GL30Interceptor, self).glShaderSource(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glBindFramebuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindFramebuffer(int,int)"""
        super(__GL30Interceptor, self).glBindFramebuffer(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def glDrawElementsInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawElementsInstanced(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glDrawElementsInstanced(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def resolveErrorNumber(arg0: int) -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.profiling.GLInterceptor.resolveErrorNumber(int)"""
        return str.__wrap(__GLInterceptor.resolveErrorNumber(__int.valueOf(arg0)))

    @override
    @overload
    def glTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glTexParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetUniformfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glGetUniformfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform2f(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2f(int,float,float)"""
        super(__GL30Interceptor, self).glUniform2f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def glBeginQuery(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBeginQuery(int,int)"""
        super(__GL30Interceptor, self).glBeginQuery(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glBlitFramebuffer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlitFramebuffer(int,int,int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glBlitFramebuffer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9))

    @override
    @overload
    def glDeleteQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteQueries(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteQueries(__int.valueOf(arg0), arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def glUseProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUseProgram(int)"""
        super(__GL30Interceptor, self).glUseProgram(__int.valueOf(arg0))

    @override
    @overload
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2fv(int,int,float[],int)"""
        super(__GL30Interceptor, self).glUniform2fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix2fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1fv(int,int,float[],int)"""
        super(__GL30Interceptor, self).glUniform1fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3fv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniform3fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def getVertexCount(self) -> 'math.FloatCounter':
        """public com.badlogic.gdx.math.FloatCounter com.badlogic.gdx.graphics.profiling.GLInterceptor.getVertexCount()"""
        return 'math.FloatCounter'.__wrap(super(GLInterceptor, self).getVertexCount())

    @override
    @overload
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawElements(int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glDrawElements(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def glReadPixels(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glReadPixels(int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glReadPixels(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), arg6)

    @override
    @overload
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage3D(int,int,int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glTexImage3D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9))

    @override
    @overload
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1iv(int,int,int[],int)"""
        super(__GL30Interceptor, self).glUniform1iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glDeleteRenderbuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteRenderbuffer(int)"""
        super(__GL30Interceptor, self).glDeleteRenderbuffer(__int.valueOf(arg0))

    @override
    @overload
    def glCreateProgram(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCreateProgram()"""
        return int.__wrap(super(GL30Interceptor, self).glCreateProgram())

    @override
    @overload
    def glDeleteShader(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteShader(int)"""
        super(__GL30Interceptor, self).glDeleteShader(__int.valueOf(arg0))

    @overload
    def glIsTransformFeedback(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsTransformFeedback(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsTransformFeedback(__int.valueOf(arg0)))

    @override
    @overload
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix3fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glHint(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glHint(int,int)"""
        super(__GL30Interceptor, self).glHint(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glGetVertexAttribIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribIuiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetVertexAttribIuiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glProgramParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glProgramParameteri(int,int,int)"""
        super(__GL30Interceptor, self).glProgramParameteri(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glCompileShader(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCompileShader(int)"""
        super(__GL30Interceptor, self).glCompileShader(__int.valueOf(arg0))

    @override
    @overload
    def glBindSampler(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindSampler(int,int)"""
        super(__GL30Interceptor, self).glBindSampler(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glFinish(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFinish()"""
        super(GL30Interceptor, self).glFinish()

    @overload
    def glCheckFramebufferStatus(self, arg0: int) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCheckFramebufferStatus(int)"""
        return int.__wrap(super(__GL30Interceptor, self).glCheckFramebufferStatus(__int.valueOf(arg0)))

    @override
    @overload
    def glUniformMatrix2x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix2x4fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glGenFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenFramebuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenFramebuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniform4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4f(int,float,float,float,float)"""
        super(__GL30Interceptor, self).glUniform4f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4fv(int,int,float[],int)"""
        super(__GL30Interceptor, self).glUniform4fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glGetVertexAttribfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glGetVertexAttribfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribPointer(int,int,int,boolean,int,int)"""
        super(__GL30Interceptor, self).glVertexAttribPointer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @override
    @overload
    def glRenderbufferStorage(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glRenderbufferStorage(int,int,int,int)"""
        super(__GL30Interceptor, self).glRenderbufferStorage(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glStencilMaskSeparate(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilMaskSeparate(int,int)"""
        super(__GL30Interceptor, self).glStencilMaskSeparate(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glGetInteger64v(self, arg0: int, arg1: 'LongBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetInteger64v(int,java.nio.LongBuffer)"""
        super(__GL30Interceptor, self).glGetInteger64v(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniformMatrix4x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix4x2fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glDepthRangef(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDepthRangef(float,float)"""
        super(__GL30Interceptor, self).glDepthRangef(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def glDeleteSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteSamplers(int,int[],int)"""
        super(__GL30Interceptor, self).glDeleteSamplers(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glCopyTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyTexImage2D(int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glCopyTexImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7))

    @override
    @overload
    def glValidateProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glValidateProgram(int)"""
        super(__GL30Interceptor, self).glValidateProgram(__int.valueOf(arg0))

    @override
    @overload
    def glBlendFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendFuncSeparate(int,int,int,int)"""
        super(__GL30Interceptor, self).glBlendFuncSeparate(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3fv(int,int,boolean,float[],int)"""
        super(__GL30Interceptor, self).glUniformMatrix3fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3, __int.valueOf(arg4))

    @override
    @overload
    def glCopyBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyBufferSubData(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glCopyBufferSubData(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glClearColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearColor(float,float,float,float)"""
        super(__GL30Interceptor, self).glClearColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def glVertexAttribDivisor(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribDivisor(int,int)"""
        super(__GL30Interceptor, self).glVertexAttribDivisor(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glGetUniformuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformuiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetUniformuiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniformMatrix3x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix3x4fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glGenFramebuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenFramebuffer()"""
        return int.__wrap(super(GL30Interceptor, self).glGenFramebuffer())

    @override
    @overload
    def glDrawBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawBuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDrawBuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glViewport(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glViewport(int,int,int,int)"""
        super(__GL30Interceptor, self).glViewport(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glBeginTransformFeedback(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBeginTransformFeedback(int)"""
        super(__GL30Interceptor, self).glBeginTransformFeedback(__int.valueOf(arg0))

    @override
    @overload
    def glGenQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenQueries(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenQueries(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glActiveTexture(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glActiveTexture(int)"""
        super(__GL30Interceptor, self).glActiveTexture(__int.valueOf(arg0))

    @override
    @overload
    def glDetachShader(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDetachShader(int,int)"""
        super(__GL30Interceptor, self).glDetachShader(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glSamplerParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTransformFeedbacks(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteTransformFeedbacks(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glBlendColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendColor(float,float,float,float)"""
        super(__GL30Interceptor, self).glBlendColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def glUniform1i(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1i(int,int)"""
        super(__GL30Interceptor, self).glUniform1i(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage2D(int,int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glTexImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8))

    @override
    @overload
    def glBlendEquationSeparate(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendEquationSeparate(int,int)"""
        super(__GL30Interceptor, self).glBlendEquationSeparate(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def glGetActiveUniform(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer') -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniform(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetActiveUniform(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3))

    @override
    @overload
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4iv(int,int,int[],int)"""
        super(__GL30Interceptor, self).glUniform4iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glBindRenderbuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindRenderbuffer(int,int)"""
        super(__GL30Interceptor, self).glBindRenderbuffer(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glUniform1f(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1f(int,float)"""
        super(__GL30Interceptor, self).glUniform1f(__int.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def glCopyTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyTexSubImage3D(int,int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glCopyTexSubImage3D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8))

    @override
    @overload
    def glScissor(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glScissor(int,int,int,int)"""
        super(__GL30Interceptor, self).glScissor(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glStencilFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilFuncSeparate(int,int,int,int)"""
        super(__GL30Interceptor, self).glStencilFuncSeparate(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glVertexAttrib3fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib3fv(int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glVertexAttrib3fv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glVertexAttrib2f(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib2f(int,float,float)"""
        super(__GL30Interceptor, self).glVertexAttrib2f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glTexSubImage3D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10))

    @overload
    def glMapBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Buffer':
        """public java.nio.Buffer com.badlogic.gdx.graphics.profiling.GL30Interceptor.glMapBufferRange(int,int,int,int)"""
        return 'Buffer'.__wrap(super(__GL30Interceptor, self).glMapBufferRange(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def glGetError(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetError()"""
        return int.__wrap(super(GL30Interceptor, self).glGetError())

    @override
    @overload
    def glGetShaderPrecisionFormat(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetShaderPrecisionFormat(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetShaderPrecisionFormat(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3iv(int,int,int[],int)"""
        super(__GL30Interceptor, self).glUniform3iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glBlendFunc(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendFunc(int,int)"""
        super(__GL30Interceptor, self).glBlendFunc(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glFramebufferRenderbuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFramebufferRenderbuffer(int,int,int,int)"""
        super(__GL30Interceptor, self).glFramebufferRenderbuffer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glGetUniformIndices(self, arg0: int, arg1: 'String', arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformIndices(int,java.lang.String[],java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetUniformIndices(__int.valueOf(arg0), arg1, arg2)

    @override
    @overload
    def glGetProgramiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetProgramiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetProgramiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4fv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniform4fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glFramebufferTextureLayer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFramebufferTextureLayer(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glFramebufferTextureLayer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4iv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform4iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2iv(int,int,int[],int)"""
        super(__GL30Interceptor, self).glUniform2iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glDeleteQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteQueries(int,int[],int)"""
        super(__GL30Interceptor, self).glDeleteQueries(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glTexParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameteri(int,int,int)"""
        super(__GL30Interceptor, self).glTexParameteri(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glUniformBlockBinding(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformBlockBinding(int,int,int)"""
        super(__GL30Interceptor, self).glUniformBlockBinding(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glGetVertexAttribiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetVertexAttribiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glInvalidateFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glInvalidateFramebuffer(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glInvalidateFramebuffer(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glVertexAttribIPointer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribIPointer(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glVertexAttribIPointer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glStencilOp(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilOp(int,int,int)"""
        super(__GL30Interceptor, self).glStencilOp(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glBufferData(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBufferData(int,int,java.nio.Buffer,int)"""
        super(__GL30Interceptor, self).glBufferData(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def glUniform1uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1uiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform1uiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glSampleCoverage(self, arg0: float, arg1: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSampleCoverage(float,boolean)"""
        super(__GL30Interceptor, self).glSampleCoverage(__float.valueOf(arg0), __boolean.valueOf(arg1))

    @override
    @overload
    def glFramebufferTexture2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFramebufferTexture2D(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glFramebufferTexture2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glDeleteSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteSamplers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteSamplers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetShaderiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetShaderiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetShaderiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @overload
    def glIsSampler(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsSampler(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsSampler(__int.valueOf(arg0)))

    @override
    @overload
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTransformFeedbacks(int,int[],int)"""
        super(__GL30Interceptor, self).glDeleteTransformFeedbacks(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

 
 
 
# CLASS: com.badlogic.gdx.graphics.profiling.GL30Interceptor
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.graphics.profiling.GLInterceptor as __GLInterceptor
__GLInterceptor = __GLInterceptor
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import com.badlogic.gdx.graphics.profiling.GL30Interceptor as __GL30Interceptor
__GL30Interceptor = __GL30Interceptor
import java.lang.Object as __object
import java.nio.IntBuffer as IntBuffer
from builtins import type
from builtins import float
import java.nio.LongBuffer as LongBuffer
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Long as __long
import java.lang.Float as __float
import com.badlogic.gdx.math.FloatCounter as __FloatCounter
__FloatCounter = __FloatCounter
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

from builtins import bool
import java.nio.Buffer as __Buffer
__Buffer = __Buffer
from builtins import int
 
class GL30Interceptor():
    """com.badlogic.gdx.graphics.profiling.GL30Interceptor"""
 
    @staticmethod
    def __wrap(java_value: __GL30Interceptor) -> 'GL30Interceptor':
        return GL30Interceptor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GL30Interceptor):
        """
        Dynamic initializer for GL30Interceptor.
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
    def glUniform3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3f(int,float,float,float)"""
        super(__GL30Interceptor, self).glUniform3f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def glPauseTransformFeedback(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glPauseTransformFeedback()"""
        super(GL30Interceptor, self).glPauseTransformFeedback()

    @overload
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformBlockName(int,int)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetActiveUniformBlockName(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def glGetAttribLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetAttribLocation(int,java.lang.String)"""
        return int.__wrap(super(__GL30Interceptor, self).glGetAttribLocation(__int.valueOf(arg0), arg1))

    @override
    @overload
    def glCullFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCullFace(int)"""
        super(__GL30Interceptor, self).glCullFace(__int.valueOf(arg0))

    @override
    @overload
    def glGetSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glGetSamplerParameterfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3iv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform3iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glBindBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindBufferRange(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glBindBufferRange(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glGenBuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenBuffer()"""
        return int.__wrap(super(GL30Interceptor, self).glGenBuffer())

    @override
    @overload
    def glGetTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetTexParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetTexParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteTexture(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTexture(int)"""
        super(__GL30Interceptor, self).glDeleteTexture(__int.valueOf(arg0))

    @override
    @overload
    def glCopyTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyTexSubImage2D(int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glCopyTexSubImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7))

    @override
    @overload
    def glVertexAttribI4ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribI4ui(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glVertexAttribI4ui(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glBindTexture(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindTexture(int,int)"""
        super(__GL30Interceptor, self).glBindTexture(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawRangeElements(int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glDrawRangeElements(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5)

    @override
    @overload
    def glGetIntegerv(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetIntegerv(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetIntegerv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawElements(int,int,int,int)"""
        super(__GL30Interceptor, self).glDrawElements(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def glGetStringi(self, arg0: int, arg1: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetStringi(int,int)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetStringi(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def glLinkProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glLinkProgram(int)"""
        super(__GL30Interceptor, self).glLinkProgram(__int.valueOf(arg0))

    @overload
    def glIsBuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsBuffer(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsBuffer(__int.valueOf(arg0)))

    @override
    @overload
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glTexSubImage3D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), arg10)

    @override
    @overload
    def glClearBufferuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferuiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glClearBufferuiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetQueryiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetQueryiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetQueryiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glClearDepthf(self, arg0: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearDepthf(float)"""
        super(__GL30Interceptor, self).glClearDepthf(__float.valueOf(arg0))

    @override
    @overload
    def glEndQuery(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEndQuery(int)"""
        super(__GL30Interceptor, self).glEndQuery(__int.valueOf(arg0))

    @override
    @overload
    def glCompressedTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCompressedTexImage2D(int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glCompressedTexImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), arg7)

    @override
    @overload
    def glAttachShader(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glAttachShader(int,int)"""
        super(__GL30Interceptor, self).glAttachShader(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glDeleteProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteProgram(int)"""
        super(__GL30Interceptor, self).glDeleteProgram(__int.valueOf(arg0))

    @override
    @overload
    def glTransformFeedbackVaryings(self, arg0: int, arg1: 'String', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTransformFeedbackVaryings(int,java.lang.String[],int)"""
        super(__GL30Interceptor, self).glTransformFeedbackVaryings(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glFlushMappedBufferRange(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFlushMappedBufferRange(int,int,int)"""
        super(__GL30Interceptor, self).glFlushMappedBufferRange(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glTexParameterf(self, arg0: int, arg1: int, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameterf(int,int,float)"""
        super(__GL30Interceptor, self).glTexParameterf(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def glUniform3uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3uiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform3uiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDepthMask(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDepthMask(boolean)"""
        super(__GL30Interceptor, self).glDepthMask(__boolean.valueOf(arg0))

    @override
    @overload
    def glVertexAttrib1f(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib1f(int,float)"""
        super(__GL30Interceptor, self).glVertexAttrib1f(__int.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def glGetBooleanv(self, arg0: int, arg1: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBooleanv(int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glGetBooleanv(__int.valueOf(arg0), arg1)

    @overload
    def glGetActiveAttrib(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer') -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveAttrib(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetActiveAttrib(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3))

    @overload
    def glIsFramebuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsFramebuffer(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsFramebuffer(__int.valueOf(arg0)))

    @override
    @overload
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformBlockName(int,int,java.nio.Buffer,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glGetActiveUniformBlockName(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def glVertexAttribI4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribI4i(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glVertexAttribI4i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glVertexAttrib1fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib1fv(int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glVertexAttrib1fv(__int.valueOf(arg0), arg1)

    @overload
    def glUnmapBuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUnmapBuffer(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glUnmapBuffer(__int.valueOf(arg0)))

    @overload
    def glIsRenderbuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsRenderbuffer(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsRenderbuffer(__int.valueOf(arg0)))

    @override
    @overload
    def glGenTexture(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTexture()"""
        return int.__wrap(super(GL30Interceptor, self).glGenTexture())

    @override
    @overload
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage3D(int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glTexImage3D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), arg9)

    @overload
    def glIsProgram(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsProgram(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsProgram(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def glBindVertexArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindVertexArray(int)"""
        super(__GL30Interceptor, self).glBindVertexArray(__int.valueOf(arg0))

    @override
    @overload
    def glGetQueryObjectuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetQueryObjectuiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetQueryObjectuiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def getTextureBindings(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getTextureBindings()"""
        return int.__wrap(super(GLInterceptor, self).getTextureBindings())

    @override
    @overload
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawRangeElements(int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glDrawRangeElements(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @override
    @overload
    def getDrawCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getDrawCalls()"""
        return int.__wrap(super(GLInterceptor, self).getDrawCalls())

    @override
    @overload
    def glClearBufferfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glClearBufferfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @overload
    def glCreateShader(self, arg0: int) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCreateShader(int)"""
        return int.__wrap(super(__GL30Interceptor, self).glCreateShader(__int.valueOf(arg0)))

    @override
    @overload
    def glGetActiveUniformBlockiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformBlockiv(int,int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetActiveUniformBlockiv(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def glBindBuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindBuffer(int,int)"""
        super(__GL30Interceptor, self).glBindBuffer(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBufferSubData(int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glBufferSubData(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @overload
    def glGetBufferPointerv(self, arg0: int, arg1: int) -> 'Buffer':
        """public java.nio.Buffer com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBufferPointerv(int,int)"""
        return 'Buffer'.__wrap(super(__GL30Interceptor, self).glGetBufferPointerv(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def glDeleteBuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteBuffer(int)"""
        super(__GL30Interceptor, self).glDeleteBuffer(__int.valueOf(arg0))

    @override
    @overload
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTransformFeedbacks(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenTransformFeedbacks(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glClear(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClear(int)"""
        super(__GL30Interceptor, self).glClear(__int.valueOf(arg0))

    @override
    @overload
    def glStencilMask(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilMask(int)"""
        super(__GL30Interceptor, self).glStencilMask(__int.valueOf(arg0))

    @override
    @overload
    def glUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3i(int,int,int,int)"""
        super(__GL30Interceptor, self).glUniform3i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2fv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniform2fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix4fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glGenVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenVertexArrays(int,int[],int)"""
        super(__GL30Interceptor, self).glGenVertexArrays(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glGenQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenQueries(int,int[],int)"""
        super(__GL30Interceptor, self).glGenQueries(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1fv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniform1fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def glBindBufferBase(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindBufferBase(int,int,int)"""
        super(__GL30Interceptor, self).glBindBufferBase(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glDepthFunc(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDepthFunc(int)"""
        super(__GL30Interceptor, self).glDepthFunc(__int.valueOf(arg0))

    @override
    @overload
    def glGenRenderbuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenRenderbuffer()"""
        return int.__wrap(super(GL30Interceptor, self).glGenRenderbuffer())

    @override
    @overload
    def glUniformMatrix3x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix3x2fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glBindAttribLocation(self, arg0: int, arg1: int, arg2: str):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindAttribLocation(int,int,java.lang.String)"""
        super(__GL30Interceptor, self).glBindAttribLocation(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetActiveUniformsiv(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformsiv(int,int,java.nio.IntBuffer,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetActiveUniformsiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), arg4)

    @override
    @overload
    def glClearStencil(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearStencil(int)"""
        super(__GL30Interceptor, self).glClearStencil(__int.valueOf(arg0))

    @override
    @overload
    def glGetVertexAttribPointerv(self, arg0: int, arg1: int, arg2: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribPointerv(int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glGetVertexAttribPointerv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform2i(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2i(int,int,int)"""
        super(__GL30Interceptor, self).glUniform2i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glCompressedTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCompressedTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glCompressedTexSubImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), arg8)

    @override
    @overload
    def glStencilOpSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilOpSeparate(int,int,int,int)"""
        super(__GL30Interceptor, self).glStencilOpSeparate(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glGetAttachedShaders(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetAttachedShaders(int,int,java.nio.Buffer,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetAttachedShaders(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def glReadBuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glReadBuffer(int)"""
        super(__GL30Interceptor, self).glReadBuffer(__int.valueOf(arg0))

    @override
    @overload
    def glGetRenderbufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetRenderbufferParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetRenderbufferParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glClearBufferiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glClearBufferiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glVertexAttrib2fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib2fv(int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glVertexAttrib2fv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glDeleteVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteVertexArrays(int,int[],int)"""
        super(__GL30Interceptor, self).glDeleteVertexArrays(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glColorMask(self, arg0: bool, arg1: bool, arg2: bool, arg3: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glColorMask(boolean,boolean,boolean,boolean)"""
        super(__GL30Interceptor, self).glColorMask(__boolean.valueOf(arg0), __boolean.valueOf(arg1), __boolean.valueOf(arg2), __boolean.valueOf(arg3))

    @overload
    def glIsEnabled(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsEnabled(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsEnabled(__int.valueOf(arg0)))

    @override
    @overload
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glTexImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), arg8)

    @override
    @overload
    def glDrawArrays(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawArrays(int,int,int)"""
        super(__GL30Interceptor, self).glDrawArrays(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glGenTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTextures(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenTextures(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glPolygonOffset(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glPolygonOffset(float,float)"""
        super(__GL30Interceptor, self).glPolygonOffset(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def glUniformMatrix4x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix4x3fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1iv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform1iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteBuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteBuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetSamplerParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glEnableVertexAttribArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEnableVertexAttribArray(int)"""
        super(__GL30Interceptor, self).glEnableVertexAttribArray(__int.valueOf(arg0))

    @override
    @overload
    def glUniform4uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4uiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform4uiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glInvalidateSubFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: int, arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glInvalidateSubFramebuffer(int,int,java.nio.IntBuffer,int,int,int,int)"""
        super(__GL30Interceptor, self).glInvalidateSubFramebuffer(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6))

    @override
    @overload
    def glReleaseShaderCompiler(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glReleaseShaderCompiler()"""
        super(GL30Interceptor, self).glReleaseShaderCompiler()

    @override
    @overload
    def glVertexAttrib3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib3f(int,float,float,float)"""
        super(__GL30Interceptor, self).glVertexAttrib3f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def glDeleteFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteFramebuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteFramebuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetBufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBufferParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetBufferParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDisable(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDisable(int)"""
        super(__GL30Interceptor, self).glDisable(__int.valueOf(arg0))

    @overload
    def glIsTexture(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsTexture(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsTexture(__int.valueOf(arg0)))

    @override
    @overload
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glTexSubImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), arg8)

    @override
    @overload
    def glVertexAttrib4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib4f(int,float,float,float,float)"""
        super(__GL30Interceptor, self).glVertexAttrib4f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def glGetFramebufferAttachmentParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetFramebufferAttachmentParameteriv(int,int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetFramebufferAttachmentParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def glResumeTransformFeedback(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glResumeTransformFeedback()"""
        super(GL30Interceptor, self).glResumeTransformFeedback()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def glGetFloatv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetFloatv(int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glGetFloatv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetVertexAttribIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribIiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetVertexAttribIiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glGenRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenRenderbuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenRenderbuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glEndTransformFeedback(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEndTransformFeedback()"""
        super(GL30Interceptor, self).glEndTransformFeedback()

    @overload
    def glIsVertexArray(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsVertexArray(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsVertexArray(__int.valueOf(arg0)))

    @overload
    def glGetUniformBlockIndex(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformBlockIndex(int,java.lang.String)"""
        return int.__wrap(super(__GL30Interceptor, self).glGetUniformBlockIndex(__int.valueOf(arg0), arg1))

    @override
    @overload
    def glPixelStorei(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glPixelStorei(int,int)"""
        super(__GL30Interceptor, self).glPixelStorei(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glLineWidth(self, arg0: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glLineWidth(float)"""
        super(__GL30Interceptor, self).glLineWidth(__float.valueOf(arg0))

    @override
    @overload
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribPointer(int,int,int,boolean,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glVertexAttribPointer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __int.valueOf(arg4), arg5)

    @override
    @overload
    def glBindTransformFeedback(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindTransformFeedback(int,int)"""
        super(__GL30Interceptor, self).glBindTransformFeedback(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glBlendEquation(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendEquation(int)"""
        super(__GL30Interceptor, self).glBlendEquation(__int.valueOf(arg0))

    @override
    @overload
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4fv(int,int,boolean,float[],int)"""
        super(__GL30Interceptor, self).glUniformMatrix4fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3, __int.valueOf(arg4))

    @override
    @overload
    def glGenerateMipmap(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenerateMipmap(int)"""
        super(__GL30Interceptor, self).glGenerateMipmap(__int.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.profiling.GLInterceptor.reset()"""
        super(GLInterceptor, self).reset()

    @override
    @overload
    def glGenBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenBuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenBuffers(__int.valueOf(arg0), arg1)

    @overload
    def glIsQuery(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsQuery(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsQuery(__int.valueOf(arg0)))

    @override
    @overload
    def glGetTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetTexParameterfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glGetTexParameterfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2iv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform2iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteFramebuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteFramebuffer(int)"""
        super(__GL30Interceptor, self).glDeleteFramebuffer(__int.valueOf(arg0))

    @override
    @overload
    def glSamplerParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameteri(int,int,int)"""
        super(__GL30Interceptor, self).glSamplerParameteri(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glEnable(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEnable(int)"""
        super(__GL30Interceptor, self).glEnable(__int.valueOf(arg0))

    @overload
    def glGetShaderInfoLog(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetShaderInfoLog(int)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetShaderInfoLog(__int.valueOf(arg0)))

    @override
    @overload
    def glUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4i(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glUniform4i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glStencilFunc(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilFunc(int,int,int)"""
        super(__GL30Interceptor, self).glStencilFunc(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glDeleteTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTextures(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteTextures(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2fv(int,int,boolean,float[],int)"""
        super(__GL30Interceptor, self).glUniformMatrix2fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3, __int.valueOf(arg4))

    @override
    @overload
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage2D(int,int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glTexSubImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8))

    @overload
    def glGetProgramInfoLog(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetProgramInfoLog(int)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetProgramInfoLog(__int.valueOf(arg0)))

    @override
    @overload
    def glFrontFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFrontFace(int)"""
        super(__GL30Interceptor, self).glFrontFace(__int.valueOf(arg0))

    @override
    @overload
    def glSamplerParameterf(self, arg0: int, arg1: int, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameterf(int,int,float)"""
        super(__GL30Interceptor, self).glSamplerParameterf(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def glGetUniformiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetUniformiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetBufferParameteri64v(self, arg0: int, arg1: int, arg2: 'LongBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBufferParameteri64v(int,int,java.nio.LongBuffer)"""
        super(__GL30Interceptor, self).glGetBufferParameteri64v(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @overload
    def glGetString(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetString(int)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetString(__int.valueOf(arg0)))

    @overload
    def glGetFragDataLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetFragDataLocation(int,java.lang.String)"""
        return int.__wrap(super(__GL30Interceptor, self).glGetFragDataLocation(__int.valueOf(arg0), arg1))

    @override
    @overload
    def glTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameterfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glTexParameterfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glGenSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenSamplers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenSamplers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glClearBufferfi(self, arg0: int, arg1: int, arg2: float, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferfi(int,int,float,int)"""
        super(__GL30Interceptor, self).glClearBufferfi(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glUniformMatrix2x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix2x3fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def getShaderSwitches(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getShaderSwitches()"""
        return int.__wrap(super(GLInterceptor, self).getShaderSwitches())

    @override
    @overload
    def glGenSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenSamplers(int,int[],int)"""
        super(__GL30Interceptor, self).glGenSamplers(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glRenderbufferStorageMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glRenderbufferStorageMultisample(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glRenderbufferStorageMultisample(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glSamplerParameterfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def getCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getCalls()"""
        return int.__wrap(super(GLInterceptor, self).getCalls())

    @override
    @overload
    def glShaderBinary(self, arg0: int, arg1: 'IntBuffer', arg2: int, arg3: 'Buffer', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glShaderBinary(int,java.nio.IntBuffer,int,java.nio.Buffer,int)"""
        super(__GL30Interceptor, self).glShaderBinary(__int.valueOf(arg0), arg1, __int.valueOf(arg2), arg3, __int.valueOf(arg4))

    @override
    @overload
    def glDisableVertexAttribArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDisableVertexAttribArray(int)"""
        super(__GL30Interceptor, self).glDisableVertexAttribArray(__int.valueOf(arg0))

    @overload
    def glIsShader(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsShader(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsShader(__int.valueOf(arg0)))

    @override
    @overload
    def glDeleteVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteVertexArrays(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteVertexArrays(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glFlush(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFlush()"""
        super(GL30Interceptor, self).glFlush()

    @override
    @overload
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTransformFeedbacks(int,int[],int)"""
        super(__GL30Interceptor, self).glGenTransformFeedbacks(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glVertexAttrib4fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib4fv(int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glVertexAttrib4fv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glDeleteRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteRenderbuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteRenderbuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glGenVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenVertexArrays(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenVertexArrays(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glDrawArraysInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawArraysInstanced(int,int,int,int)"""
        super(__GL30Interceptor, self).glDrawArraysInstanced(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3fv(int,int,float[],int)"""
        super(__GL30Interceptor, self).glUniform3fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @overload
    def glGetUniformLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformLocation(int,java.lang.String)"""
        return int.__wrap(super(__GL30Interceptor, self).glGetUniformLocation(__int.valueOf(arg0), arg1))

    @override
    @overload
    def glShaderSource(self, arg0: int, arg1: str):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glShaderSource(int,java.lang.String)"""
        super(__GL30Interceptor, self).glShaderSource(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glBindFramebuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindFramebuffer(int,int)"""
        super(__GL30Interceptor, self).glBindFramebuffer(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def glDrawElementsInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawElementsInstanced(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glDrawElementsInstanced(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def resolveErrorNumber(arg0: int) -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.profiling.GLInterceptor.resolveErrorNumber(int)"""
        return str.__wrap(__GLInterceptor.resolveErrorNumber(__int.valueOf(arg0)))

    @override
    @overload
    def glTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glTexParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetUniformfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glGetUniformfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform2f(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2f(int,float,float)"""
        super(__GL30Interceptor, self).glUniform2f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def glBeginQuery(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBeginQuery(int,int)"""
        super(__GL30Interceptor, self).glBeginQuery(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glBlitFramebuffer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlitFramebuffer(int,int,int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glBlitFramebuffer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9))

    @override
    @overload
    def glDeleteQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteQueries(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteQueries(__int.valueOf(arg0), arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def glUseProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUseProgram(int)"""
        super(__GL30Interceptor, self).glUseProgram(__int.valueOf(arg0))

    @override
    @overload
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2fv(int,int,float[],int)"""
        super(__GL30Interceptor, self).glUniform2fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix2fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1fv(int,int,float[],int)"""
        super(__GL30Interceptor, self).glUniform1fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3fv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniform3fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def getVertexCount(self) -> 'math.FloatCounter':
        """public com.badlogic.gdx.math.FloatCounter com.badlogic.gdx.graphics.profiling.GLInterceptor.getVertexCount()"""
        return 'math.FloatCounter'.__wrap(super(GLInterceptor, self).getVertexCount())

    @override
    @overload
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawElements(int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glDrawElements(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def glReadPixels(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glReadPixels(int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glReadPixels(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), arg6)

    @override
    @overload
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage3D(int,int,int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glTexImage3D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9))

    @override
    @overload
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1iv(int,int,int[],int)"""
        super(__GL30Interceptor, self).glUniform1iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glDeleteRenderbuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteRenderbuffer(int)"""
        super(__GL30Interceptor, self).glDeleteRenderbuffer(__int.valueOf(arg0))

    @override
    @overload
    def glCreateProgram(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCreateProgram()"""
        return int.__wrap(super(GL30Interceptor, self).glCreateProgram())

    @override
    @overload
    def glDeleteShader(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteShader(int)"""
        super(__GL30Interceptor, self).glDeleteShader(__int.valueOf(arg0))

    @overload
    def glIsTransformFeedback(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsTransformFeedback(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsTransformFeedback(__int.valueOf(arg0)))

    @override
    @overload
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix3fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glHint(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glHint(int,int)"""
        super(__GL30Interceptor, self).glHint(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glGetVertexAttribIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribIuiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetVertexAttribIuiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glProgramParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glProgramParameteri(int,int,int)"""
        super(__GL30Interceptor, self).glProgramParameteri(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glCompileShader(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCompileShader(int)"""
        super(__GL30Interceptor, self).glCompileShader(__int.valueOf(arg0))

    @override
    @overload
    def glBindSampler(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindSampler(int,int)"""
        super(__GL30Interceptor, self).glBindSampler(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glFinish(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFinish()"""
        super(GL30Interceptor, self).glFinish()

    @overload
    def glCheckFramebufferStatus(self, arg0: int) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCheckFramebufferStatus(int)"""
        return int.__wrap(super(__GL30Interceptor, self).glCheckFramebufferStatus(__int.valueOf(arg0)))

    @override
    @overload
    def glUniformMatrix2x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix2x4fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glGenFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenFramebuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenFramebuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniform4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4f(int,float,float,float,float)"""
        super(__GL30Interceptor, self).glUniform4f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4fv(int,int,float[],int)"""
        super(__GL30Interceptor, self).glUniform4fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glGetVertexAttribfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glGetVertexAttribfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribPointer(int,int,int,boolean,int,int)"""
        super(__GL30Interceptor, self).glVertexAttribPointer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @override
    @overload
    def glRenderbufferStorage(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glRenderbufferStorage(int,int,int,int)"""
        super(__GL30Interceptor, self).glRenderbufferStorage(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glStencilMaskSeparate(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilMaskSeparate(int,int)"""
        super(__GL30Interceptor, self).glStencilMaskSeparate(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glGetInteger64v(self, arg0: int, arg1: 'LongBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetInteger64v(int,java.nio.LongBuffer)"""
        super(__GL30Interceptor, self).glGetInteger64v(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniformMatrix4x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix4x2fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glDepthRangef(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDepthRangef(float,float)"""
        super(__GL30Interceptor, self).glDepthRangef(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def glDeleteSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteSamplers(int,int[],int)"""
        super(__GL30Interceptor, self).glDeleteSamplers(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glCopyTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyTexImage2D(int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glCopyTexImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7))

    @override
    @overload
    def glValidateProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glValidateProgram(int)"""
        super(__GL30Interceptor, self).glValidateProgram(__int.valueOf(arg0))

    @override
    @overload
    def glBlendFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendFuncSeparate(int,int,int,int)"""
        super(__GL30Interceptor, self).glBlendFuncSeparate(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3fv(int,int,boolean,float[],int)"""
        super(__GL30Interceptor, self).glUniformMatrix3fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3, __int.valueOf(arg4))

    @override
    @overload
    def glCopyBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyBufferSubData(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glCopyBufferSubData(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glClearColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearColor(float,float,float,float)"""
        super(__GL30Interceptor, self).glClearColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def glVertexAttribDivisor(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribDivisor(int,int)"""
        super(__GL30Interceptor, self).glVertexAttribDivisor(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glGetUniformuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformuiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetUniformuiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniformMatrix3x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix3x4fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glGenFramebuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenFramebuffer()"""
        return int.__wrap(super(GL30Interceptor, self).glGenFramebuffer())

    @override
    @overload
    def glDrawBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawBuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDrawBuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glViewport(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glViewport(int,int,int,int)"""
        super(__GL30Interceptor, self).glViewport(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glBeginTransformFeedback(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBeginTransformFeedback(int)"""
        super(__GL30Interceptor, self).glBeginTransformFeedback(__int.valueOf(arg0))

    @override
    @overload
    def glGenQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenQueries(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenQueries(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glActiveTexture(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glActiveTexture(int)"""
        super(__GL30Interceptor, self).glActiveTexture(__int.valueOf(arg0))

    @override
    @overload
    def glDetachShader(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDetachShader(int,int)"""
        super(__GL30Interceptor, self).glDetachShader(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glSamplerParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTransformFeedbacks(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteTransformFeedbacks(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glBlendColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendColor(float,float,float,float)"""
        super(__GL30Interceptor, self).glBlendColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def glUniform1i(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1i(int,int)"""
        super(__GL30Interceptor, self).glUniform1i(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage2D(int,int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glTexImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8))

    @override
    @overload
    def glBlendEquationSeparate(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendEquationSeparate(int,int)"""
        super(__GL30Interceptor, self).glBlendEquationSeparate(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def glGetActiveUniform(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer') -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniform(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetActiveUniform(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3))

    @override
    @overload
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4iv(int,int,int[],int)"""
        super(__GL30Interceptor, self).glUniform4iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glBindRenderbuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindRenderbuffer(int,int)"""
        super(__GL30Interceptor, self).glBindRenderbuffer(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glUniform1f(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1f(int,float)"""
        super(__GL30Interceptor, self).glUniform1f(__int.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def glCopyTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyTexSubImage3D(int,int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glCopyTexSubImage3D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8))

    @override
    @overload
    def glScissor(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glScissor(int,int,int,int)"""
        super(__GL30Interceptor, self).glScissor(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glStencilFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilFuncSeparate(int,int,int,int)"""
        super(__GL30Interceptor, self).glStencilFuncSeparate(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glVertexAttrib3fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib3fv(int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glVertexAttrib3fv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glVertexAttrib2f(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib2f(int,float,float)"""
        super(__GL30Interceptor, self).glVertexAttrib2f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glTexSubImage3D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10))

    @overload
    def glMapBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Buffer':
        """public java.nio.Buffer com.badlogic.gdx.graphics.profiling.GL30Interceptor.glMapBufferRange(int,int,int,int)"""
        return 'Buffer'.__wrap(super(__GL30Interceptor, self).glMapBufferRange(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def glGetError(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetError()"""
        return int.__wrap(super(GL30Interceptor, self).glGetError())

    @override
    @overload
    def glGetShaderPrecisionFormat(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetShaderPrecisionFormat(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetShaderPrecisionFormat(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3iv(int,int,int[],int)"""
        super(__GL30Interceptor, self).glUniform3iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glBlendFunc(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendFunc(int,int)"""
        super(__GL30Interceptor, self).glBlendFunc(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glFramebufferRenderbuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFramebufferRenderbuffer(int,int,int,int)"""
        super(__GL30Interceptor, self).glFramebufferRenderbuffer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glGetUniformIndices(self, arg0: int, arg1: 'String', arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformIndices(int,java.lang.String[],java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetUniformIndices(__int.valueOf(arg0), arg1, arg2)

    @override
    @overload
    def glGetProgramiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetProgramiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetProgramiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4fv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniform4fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glFramebufferTextureLayer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFramebufferTextureLayer(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glFramebufferTextureLayer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4iv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform4iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2iv(int,int,int[],int)"""
        super(__GL30Interceptor, self).glUniform2iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glDeleteQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteQueries(int,int[],int)"""
        super(__GL30Interceptor, self).glDeleteQueries(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glTexParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameteri(int,int,int)"""
        super(__GL30Interceptor, self).glTexParameteri(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glUniformBlockBinding(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformBlockBinding(int,int,int)"""
        super(__GL30Interceptor, self).glUniformBlockBinding(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glGetVertexAttribiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetVertexAttribiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glInvalidateFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glInvalidateFramebuffer(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glInvalidateFramebuffer(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glVertexAttribIPointer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribIPointer(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glVertexAttribIPointer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glStencilOp(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilOp(int,int,int)"""
        super(__GL30Interceptor, self).glStencilOp(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glBufferData(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBufferData(int,int,java.nio.Buffer,int)"""
        super(__GL30Interceptor, self).glBufferData(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def glUniform1uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1uiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform1uiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glSampleCoverage(self, arg0: float, arg1: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSampleCoverage(float,boolean)"""
        super(__GL30Interceptor, self).glSampleCoverage(__float.valueOf(arg0), __boolean.valueOf(arg1))

    @override
    @overload
    def glFramebufferTexture2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFramebufferTexture2D(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glFramebufferTexture2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glDeleteSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteSamplers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteSamplers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetShaderiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetShaderiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetShaderiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @overload
    def glIsSampler(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsSampler(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsSampler(__int.valueOf(arg0)))

    @override
    @overload
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTransformFeedbacks(int,int[],int)"""
        super(__GL30Interceptor, self).glDeleteTransformFeedbacks(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

 
 
 
# CLASS: com.badlogic.gdx.graphics.profiling.GL30Interceptor 
 
 
# CLASS: com.badlogic.gdx.graphics.profiling.GL32Interceptor
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
import com.badlogic.gdx.graphics.profiling.GL30Interceptor as __GL30Interceptor
__GL30Interceptor = __GL30Interceptor
import java.nio.IntBuffer as IntBuffer
from builtins import type
import java.nio.FloatBuffer as FloatBuffer
import com.badlogic.gdx.graphics.profiling.GL32Interceptor as __GL32Interceptor
__GL32Interceptor = __GL32Interceptor
import com.badlogic.gdx.math.FloatCounter as __FloatCounter
__FloatCounter = __FloatCounter
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import str
import com.badlogic.gdx.graphics.profiling.GLInterceptor as __GLInterceptor
__GLInterceptor = __GLInterceptor
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
import java.nio.LongBuffer as LongBuffer
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.nio.Buffer as Buffer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

import com.badlogic.gdx.graphics.profiling.GL31Interceptor as __GL31Interceptor
__GL31Interceptor = __GL31Interceptor
import java.nio.Buffer as __Buffer
__Buffer = __Buffer
from builtins import int
 
class GL32Interceptor():
    """com.badlogic.gdx.graphics.profiling.GL32Interceptor"""
 
    @staticmethod
    def __wrap(java_value: __GL32Interceptor) -> 'GL32Interceptor':
        return GL32Interceptor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GL32Interceptor):
        """
        Dynamic initializer for GL32Interceptor.
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
    def glUniform3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3f(int,float,float,float)"""
        super(__GL30Interceptor, self).glUniform3f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def glPauseTransformFeedback(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glPauseTransformFeedback()"""
        super(GL30Interceptor, self).glPauseTransformFeedback()

    @overload
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformBlockName(int,int)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetActiveUniformBlockName(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def glGetnUniformfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glGetnUniformfv(int,int,java.nio.FloatBuffer)"""
        super(__GL32Interceptor, self).glGetnUniformfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glBlendFunci(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glBlendFunci(int,int,int)"""
        super(__GL32Interceptor, self).glBlendFunci(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def glGetAttribLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetAttribLocation(int,java.lang.String)"""
        return int.__wrap(super(__GL30Interceptor, self).glGetAttribLocation(__int.valueOf(arg0), arg1))

    @override
    @overload
    def glProgramUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glProgramUniformMatrix3fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glCullFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCullFace(int)"""
        super(__GL30Interceptor, self).glCullFace(__int.valueOf(arg0))

    @override
    @overload
    def glMinSampleShading(self, arg0: float):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glMinSampleShading(float)"""
        super(__GL32Interceptor, self).glMinSampleShading(__float.valueOf(arg0))

    @override
    @overload
    def glGetSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glGetSamplerParameterfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDebugMessageCallback(self, arg0: 'DebugProc'):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glDebugMessageCallback(com.badlogic.gdx.graphics.GL32$DebugProc)"""
        super(__GL32Interceptor, self).glDebugMessageCallback(arg0)

    @override
    @overload
    def glProgramUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform3fv(int,int,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glProgramUniform3fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3iv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform3iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glBindBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindBufferRange(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glBindBufferRange(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glGenBuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenBuffer()"""
        return int.__wrap(super(GL30Interceptor, self).glGenBuffer())

    @override
    @overload
    def glGetTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetTexParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetTexParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteTexture(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTexture(int)"""
        super(__GL30Interceptor, self).glDeleteTexture(__int.valueOf(arg0))

    @override
    @overload
    def glCopyTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyTexSubImage2D(int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glCopyTexSubImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7))

    @override
    @overload
    def glVertexAttribI4ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribI4ui(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glVertexAttribI4ui(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glBindTexture(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindTexture(int,int)"""
        super(__GL30Interceptor, self).glBindTexture(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glProgramUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform3i(int,int,int,int,int)"""
        super(__GL31Interceptor, self).glProgramUniform3i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawRangeElements(int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glDrawRangeElements(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5)

    @override
    @overload
    def glGetIntegerv(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetIntegerv(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetIntegerv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glBindVertexBuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glBindVertexBuffer(int,int,long,int)"""
        super(__GL31Interceptor, self).glBindVertexBuffer(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glGetProgramPipelineiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramPipelineiv(int,int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glGetProgramPipelineiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawElements(int,int,int,int)"""
        super(__GL30Interceptor, self).glDrawElements(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def glGetStringi(self, arg0: int, arg1: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetStringi(int,int)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetStringi(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def glGenProgramPipelines(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGenProgramPipelines(int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glGenProgramPipelines(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glLinkProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glLinkProgram(int)"""
        super(__GL30Interceptor, self).glLinkProgram(__int.valueOf(arg0))

    @overload
    def glIsBuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsBuffer(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsBuffer(__int.valueOf(arg0)))

    @override
    @overload
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glTexSubImage3D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), arg10)

    @override
    @overload
    def glBlendEquationi(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glBlendEquationi(int,int)"""
        super(__GL32Interceptor, self).glBlendEquationi(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glDrawArraysIndirect(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glDrawArraysIndirect(int,long)"""
        super(__GL31Interceptor, self).glDrawArraysIndirect(__int.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def glMemoryBarrierByRegion(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glMemoryBarrierByRegion(int)"""
        super(__GL31Interceptor, self).glMemoryBarrierByRegion(__int.valueOf(arg0))

    @override
    @overload
    def glClearBufferuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferuiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glClearBufferuiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDrawElementsIndirect(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glDrawElementsIndirect(int,int,long)"""
        super(__GL31Interceptor, self).glDrawElementsIndirect(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2))

    @override
    @overload
    def glGetQueryiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetQueryiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetQueryiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glClearDepthf(self, arg0: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearDepthf(float)"""
        super(__GL30Interceptor, self).glClearDepthf(__float.valueOf(arg0))

    @override
    @overload
    def glEndQuery(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEndQuery(int)"""
        super(__GL30Interceptor, self).glEndQuery(__int.valueOf(arg0))

    @override
    @overload
    def glCompressedTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCompressedTexImage2D(int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glCompressedTexImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), arg7)

    @override
    @overload
    def glAttachShader(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glAttachShader(int,int)"""
        super(__GL30Interceptor, self).glAttachShader(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glActiveShaderProgram(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glActiveShaderProgram(int,int)"""
        super(__GL31Interceptor, self).glActiveShaderProgram(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glDeleteProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteProgram(int)"""
        super(__GL30Interceptor, self).glDeleteProgram(__int.valueOf(arg0))

    @override
    @overload
    def glTransformFeedbackVaryings(self, arg0: int, arg1: 'String', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTransformFeedbackVaryings(int,java.lang.String[],int)"""
        super(__GL30Interceptor, self).glTransformFeedbackVaryings(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glFlushMappedBufferRange(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFlushMappedBufferRange(int,int,int)"""
        super(__GL30Interceptor, self).glFlushMappedBufferRange(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glTexParameterf(self, arg0: int, arg1: int, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameterf(int,int,float)"""
        super(__GL30Interceptor, self).glTexParameterf(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def glUniform3uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3uiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform3uiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDepthMask(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDepthMask(boolean)"""
        super(__GL30Interceptor, self).glDepthMask(__boolean.valueOf(arg0))

    @override
    @overload
    def glVertexAttrib1f(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib1f(int,float)"""
        super(__GL30Interceptor, self).glVertexAttrib1f(__int.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def glEnablei(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glEnablei(int,int)"""
        super(__GL32Interceptor, self).glEnablei(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glGetBooleanv(self, arg0: int, arg1: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBooleanv(int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glGetBooleanv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glDrawElementsInstancedBaseVertex(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer', arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glDrawElementsInstancedBaseVertex(int,int,int,java.nio.Buffer,int,int)"""
        super(__GL32Interceptor, self).glDrawElementsInstancedBaseVertex(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, __int.valueOf(arg4), __int.valueOf(arg5))

    @override
    @overload
    def glGetBooleani_v(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetBooleani_v(int,int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glGetBooleani_v(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @overload
    def glGetActiveAttrib(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer') -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveAttrib(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetActiveAttrib(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3))

    @overload
    def glIsFramebuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsFramebuffer(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsFramebuffer(__int.valueOf(arg0)))

    @override
    @overload
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformBlockName(int,int,java.nio.Buffer,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glGetActiveUniformBlockName(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def glVertexAttribI4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribI4i(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glVertexAttribI4i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @overload
    def glGetProgramResourceLocation(self, arg0: int, arg1: int, arg2: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramResourceLocation(int,int,java.lang.String)"""
        return int.__wrap(super(__GL31Interceptor, self).glGetProgramResourceLocation(__int.valueOf(arg0), __int.valueOf(arg1), arg2))

    @override
    @overload
    def glProgramUniform4ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform4ui(int,int,int,int,int,int)"""
        super(__GL31Interceptor, self).glProgramUniform4ui(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @override
    @overload
    def glVertexAttrib1fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib1fv(int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glVertexAttrib1fv(__int.valueOf(arg0), arg1)

    @overload
    def glUnmapBuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUnmapBuffer(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glUnmapBuffer(__int.valueOf(arg0)))

    @overload
    def glIsRenderbuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsRenderbuffer(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsRenderbuffer(__int.valueOf(arg0)))

    @override
    @overload
    def glGenTexture(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTexture()"""
        return int.__wrap(super(GL30Interceptor, self).glGenTexture())

    @override
    @overload
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage3D(int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glTexImage3D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), arg9)

    @overload
    def glIsProgram(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsProgram(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsProgram(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def glBindVertexArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindVertexArray(int)"""
        super(__GL30Interceptor, self).glBindVertexArray(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'GLProfiler', arg1: 'GL32'):
        """public com.badlogic.gdx.graphics.profiling.GL32Interceptor(com.badlogic.gdx.graphics.profiling.GLProfiler,com.badlogic.gdx.graphics.GL32)"""
        val = __GL32Interceptor(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def glGetQueryObjectuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetQueryObjectuiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetQueryObjectuiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def getTextureBindings(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getTextureBindings()"""
        return int.__wrap(super(GLInterceptor, self).getTextureBindings())

    @override
    @overload
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawRangeElements(int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glDrawRangeElements(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @override
    @overload
    def getDrawCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getDrawCalls()"""
        return int.__wrap(super(GLInterceptor, self).getDrawCalls())

    @override
    @overload
    def glClearBufferfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glClearBufferfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @overload
    def glGetObjectLabel(self, arg0: int, arg1: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL32Interceptor.glGetObjectLabel(int,int)"""
        return str.__wrap(super(__GL32Interceptor, self).glGetObjectLabel(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def glCreateShader(self, arg0: int) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCreateShader(int)"""
        return int.__wrap(super(__GL30Interceptor, self).glCreateShader(__int.valueOf(arg0)))

    @override
    @overload
    def glGetActiveUniformBlockiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformBlockiv(int,int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetActiveUniformBlockiv(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def glGetTexLevelParameterfv(self, arg0: int, arg1: int, arg2: int, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetTexLevelParameterfv(int,int,int,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glGetTexLevelParameterfv(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def glBindBuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindBuffer(int,int)"""
        super(__GL30Interceptor, self).glBindBuffer(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBufferSubData(int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glBufferSubData(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @overload
    def glGetBufferPointerv(self, arg0: int, arg1: int) -> 'Buffer':
        """public java.nio.Buffer com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBufferPointerv(int,int)"""
        return 'Buffer'.__wrap(super(__GL30Interceptor, self).glGetBufferPointerv(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def glDeleteBuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteBuffer(int)"""
        super(__GL30Interceptor, self).glDeleteBuffer(__int.valueOf(arg0))

    @override
    @overload
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTransformFeedbacks(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenTransformFeedbacks(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glClear(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClear(int)"""
        super(__GL30Interceptor, self).glClear(__int.valueOf(arg0))

    @override
    @overload
    def glStencilMask(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilMask(int)"""
        super(__GL30Interceptor, self).glStencilMask(__int.valueOf(arg0))

    @override
    @overload
    def glUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3i(int,int,int,int)"""
        super(__GL30Interceptor, self).glUniform3i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glProgramUniformMatrix2x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix2x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glProgramUniformMatrix2x4fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2fv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniform2fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix4fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glGenVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenVertexArrays(int,int[],int)"""
        super(__GL30Interceptor, self).glGenVertexArrays(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glGenQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenQueries(int,int[],int)"""
        super(__GL30Interceptor, self).glGenQueries(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @overload
    def glCreateShaderProgramv(self, arg0: int, arg1: 'String') -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL31Interceptor.glCreateShaderProgramv(int,java.lang.String[])"""
        return int.__wrap(super(__GL31Interceptor, self).glCreateShaderProgramv(__int.valueOf(arg0), arg1))

    @override
    @overload
    def glSamplerParameterIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glSamplerParameterIiv(int,int,java.nio.IntBuffer)"""
        super(__GL32Interceptor, self).glSamplerParameterIiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1fv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniform1fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def glBindBufferBase(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindBufferBase(int,int,int)"""
        super(__GL30Interceptor, self).glBindBufferBase(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glDepthFunc(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDepthFunc(int)"""
        super(__GL30Interceptor, self).glDepthFunc(__int.valueOf(arg0))

    @override
    @overload
    def glGenRenderbuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenRenderbuffer()"""
        return int.__wrap(super(GL30Interceptor, self).glGenRenderbuffer())

    @override
    @overload
    def glUniformMatrix3x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix3x2fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glSamplerParameterIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glSamplerParameterIuiv(int,int,java.nio.IntBuffer)"""
        super(__GL32Interceptor, self).glSamplerParameterIuiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glBindAttribLocation(self, arg0: int, arg1: int, arg2: str):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindAttribLocation(int,int,java.lang.String)"""
        super(__GL30Interceptor, self).glBindAttribLocation(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glProgramUniform1ui(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform1ui(int,int,int)"""
        super(__GL31Interceptor, self).glProgramUniform1ui(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glGetActiveUniformsiv(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformsiv(int,int,java.nio.IntBuffer,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetActiveUniformsiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), arg4)

    @override
    @overload
    def glClearStencil(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearStencil(int)"""
        super(__GL30Interceptor, self).glClearStencil(__int.valueOf(arg0))

    @override
    @overload
    def glGetVertexAttribPointerv(self, arg0: int, arg1: int, arg2: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribPointerv(int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glGetVertexAttribPointerv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform2i(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2i(int,int,int)"""
        super(__GL30Interceptor, self).glUniform2i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glProgramUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform4iv(int,int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glProgramUniform4iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glCompressedTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCompressedTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glCompressedTexSubImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), arg8)

    @override
    @overload
    def glStencilOpSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilOpSeparate(int,int,int,int)"""
        super(__GL30Interceptor, self).glStencilOpSeparate(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glMemoryBarrier(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glMemoryBarrier(int)"""
        super(__GL31Interceptor, self).glMemoryBarrier(__int.valueOf(arg0))

    @override
    @overload
    def glGetAttachedShaders(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetAttachedShaders(int,int,java.nio.Buffer,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetAttachedShaders(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def glReadBuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glReadBuffer(int)"""
        super(__GL30Interceptor, self).glReadBuffer(__int.valueOf(arg0))

    @overload
    def glGetProgramResourceIndex(self, arg0: int, arg1: int, arg2: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramResourceIndex(int,int,java.lang.String)"""
        return int.__wrap(super(__GL31Interceptor, self).glGetProgramResourceIndex(__int.valueOf(arg0), __int.valueOf(arg1), arg2))

    @override
    @overload
    def glGetRenderbufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetRenderbufferParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetRenderbufferParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glClearBufferiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glClearBufferiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glVertexAttribBinding(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glVertexAttribBinding(int,int)"""
        super(__GL31Interceptor, self).glVertexAttribBinding(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glVertexAttrib2fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib2fv(int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glVertexAttrib2fv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glDeleteVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteVertexArrays(int,int[],int)"""
        super(__GL30Interceptor, self).glDeleteVertexArrays(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glColorMask(self, arg0: bool, arg1: bool, arg2: bool, arg3: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glColorMask(boolean,boolean,boolean,boolean)"""
        super(__GL30Interceptor, self).glColorMask(__boolean.valueOf(arg0), __boolean.valueOf(arg1), __boolean.valueOf(arg2), __boolean.valueOf(arg3))

    @overload
    def glIsEnabled(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsEnabled(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsEnabled(__int.valueOf(arg0)))

    @override
    @overload
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glTexImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), arg8)

    @override
    @overload
    def glDrawArrays(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawArrays(int,int,int)"""
        super(__GL30Interceptor, self).glDrawArrays(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glGenTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTextures(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenTextures(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glPolygonOffset(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glPolygonOffset(float,float)"""
        super(__GL30Interceptor, self).glPolygonOffset(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def glUniformMatrix4x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix4x3fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1iv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform1iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteBuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteBuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetSamplerParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glEnableVertexAttribArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEnableVertexAttribArray(int)"""
        super(__GL30Interceptor, self).glEnableVertexAttribArray(__int.valueOf(arg0))

    @override
    @overload
    def glPopDebugGroup(self):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glPopDebugGroup()"""
        super(GL32Interceptor, self).glPopDebugGroup()

    @override
    @overload
    def glUniform4uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4uiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform4uiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glInvalidateSubFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: int, arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glInvalidateSubFramebuffer(int,int,java.nio.IntBuffer,int,int,int,int)"""
        super(__GL30Interceptor, self).glInvalidateSubFramebuffer(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6))

    @override
    @overload
    def glReleaseShaderCompiler(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glReleaseShaderCompiler()"""
        super(GL30Interceptor, self).glReleaseShaderCompiler()

    @override
    @overload
    def glVertexAttrib3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib3f(int,float,float,float)"""
        super(__GL30Interceptor, self).glVertexAttrib3f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def glDeleteFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteFramebuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteFramebuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glDisablei(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glDisablei(int,int)"""
        super(__GL32Interceptor, self).glDisablei(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glGetBufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBufferParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetBufferParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDisable(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDisable(int)"""
        super(__GL30Interceptor, self).glDisable(__int.valueOf(arg0))

    @overload
    def glIsTexture(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsTexture(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsTexture(__int.valueOf(arg0)))

    @override
    @overload
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glTexSubImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), arg8)

    @override
    @overload
    def glVertexAttrib4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib4f(int,float,float,float,float)"""
        super(__GL30Interceptor, self).glVertexAttrib4f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def glGetFramebufferAttachmentParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetFramebufferAttachmentParameteriv(int,int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetFramebufferAttachmentParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def glResumeTransformFeedback(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glResumeTransformFeedback()"""
        super(GL30Interceptor, self).glResumeTransformFeedback()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def glGetFloatv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetFloatv(int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glGetFloatv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetVertexAttribIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribIiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetVertexAttribIiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glGenRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenRenderbuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenRenderbuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glEndTransformFeedback(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEndTransformFeedback()"""
        super(GL30Interceptor, self).glEndTransformFeedback()

    @override
    @overload
    def glGetTexParameterIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glGetTexParameterIuiv(int,int,java.nio.IntBuffer)"""
        super(__GL32Interceptor, self).glGetTexParameterIuiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glTexBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glTexBufferRange(int,int,int,int,int)"""
        super(__GL32Interceptor, self).glTexBufferRange(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @overload
    def glIsVertexArray(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsVertexArray(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsVertexArray(__int.valueOf(arg0)))

    @overload
    def glGetUniformBlockIndex(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformBlockIndex(int,java.lang.String)"""
        return int.__wrap(super(__GL30Interceptor, self).glGetUniformBlockIndex(__int.valueOf(arg0), arg1))

    @override
    @overload
    def glPixelStorei(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glPixelStorei(int,int)"""
        super(__GL30Interceptor, self).glPixelStorei(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glLineWidth(self, arg0: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glLineWidth(float)"""
        super(__GL30Interceptor, self).glLineWidth(__float.valueOf(arg0))

    @override
    @overload
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribPointer(int,int,int,boolean,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glVertexAttribPointer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __int.valueOf(arg4), arg5)

    @override
    @overload
    def glProgramUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform1iv(int,int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glProgramUniform1iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glBindTransformFeedback(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindTransformFeedback(int,int)"""
        super(__GL30Interceptor, self).glBindTransformFeedback(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glBlendEquation(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendEquation(int)"""
        super(__GL30Interceptor, self).glBlendEquation(__int.valueOf(arg0))

    @override
    @overload
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4fv(int,int,boolean,float[],int)"""
        super(__GL30Interceptor, self).glUniformMatrix4fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3, __int.valueOf(arg4))

    @override
    @overload
    def glGetGraphicsResetStatus(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL32Interceptor.glGetGraphicsResetStatus()"""
        return int.__wrap(super(GL32Interceptor, self).glGetGraphicsResetStatus())

    @override
    @overload
    def glProgramUniformMatrix4x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix4x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glProgramUniformMatrix4x3fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glGenerateMipmap(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenerateMipmap(int)"""
        super(__GL30Interceptor, self).glGenerateMipmap(__int.valueOf(arg0))

    @override
    @overload
    def glDispatchCompute(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glDispatchCompute(int,int,int)"""
        super(__GL31Interceptor, self).glDispatchCompute(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.profiling.GLInterceptor.reset()"""
        super(GLInterceptor, self).reset()

    @override
    @overload
    def glProgramUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glProgramUniformMatrix2fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glGenBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenBuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenBuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glProgramUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform4i(int,int,int,int,int,int)"""
        super(__GL31Interceptor, self).glProgramUniform4i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @overload
    def glIsQuery(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsQuery(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsQuery(__int.valueOf(arg0)))

    @override
    @overload
    def glGetTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetTexParameterfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glGetTexParameterfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2iv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform2iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetnUniformuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glGetnUniformuiv(int,int,java.nio.IntBuffer)"""
        super(__GL32Interceptor, self).glGetnUniformuiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteFramebuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteFramebuffer(int)"""
        super(__GL30Interceptor, self).glDeleteFramebuffer(__int.valueOf(arg0))

    @override
    @overload
    def glSamplerParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameteri(int,int,int)"""
        super(__GL30Interceptor, self).glSamplerParameteri(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glEnable(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEnable(int)"""
        super(__GL30Interceptor, self).glEnable(__int.valueOf(arg0))

    @overload
    def glGetShaderInfoLog(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetShaderInfoLog(int)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetShaderInfoLog(__int.valueOf(arg0)))

    @override
    @overload
    def glUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4i(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glUniform4i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glProgramUniform2f(self, arg0: int, arg1: int, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform2f(int,int,float,float)"""
        super(__GL31Interceptor, self).glProgramUniform2f(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def glStencilFunc(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilFunc(int,int,int)"""
        super(__GL30Interceptor, self).glStencilFunc(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glDeleteTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTextures(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteTextures(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2fv(int,int,boolean,float[],int)"""
        super(__GL30Interceptor, self).glUniformMatrix2fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3, __int.valueOf(arg4))

    @override
    @overload
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage2D(int,int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glTexSubImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8))

    @overload
    def glGetProgramInfoLog(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetProgramInfoLog(int)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetProgramInfoLog(__int.valueOf(arg0)))

    @override
    @overload
    def glFrontFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFrontFace(int)"""
        super(__GL30Interceptor, self).glFrontFace(__int.valueOf(arg0))

    @override
    @overload
    def glSamplerParameterf(self, arg0: int, arg1: int, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameterf(int,int,float)"""
        super(__GL30Interceptor, self).glSamplerParameterf(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def glGetUniformiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetUniformiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetBufferParameteri64v(self, arg0: int, arg1: int, arg2: 'LongBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBufferParameteri64v(int,int,java.nio.LongBuffer)"""
        super(__GL30Interceptor, self).glGetBufferParameteri64v(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @overload
    def glGetDebugMessageLog(self, arg0: int, arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: 'IntBuffer', arg6: 'ByteBuffer') -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL32Interceptor.glGetDebugMessageLog(int,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.ByteBuffer)"""
        return int.__wrap(super(__GL32Interceptor, self).glGetDebugMessageLog(__int.valueOf(arg0), arg1, arg2, arg3, arg4, arg5, arg6))

    @overload
    def glGetString(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetString(int)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetString(__int.valueOf(arg0)))

    @override
    @overload
    def glPatchParameteri(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glPatchParameteri(int,int)"""
        super(__GL32Interceptor, self).glPatchParameteri(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def glGetFragDataLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetFragDataLocation(int,java.lang.String)"""
        return int.__wrap(super(__GL30Interceptor, self).glGetFragDataLocation(__int.valueOf(arg0), arg1))

    @override
    @overload
    def glProgramUniform3ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform3ui(int,int,int,int,int)"""
        super(__GL31Interceptor, self).glProgramUniform3ui(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glProgramUniform4f(self, arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform4f(int,int,float,float,float,float)"""
        super(__GL31Interceptor, self).glProgramUniform4f(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5))

    @override
    @overload
    def glTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameterfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glTexParameterfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glGenSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenSamplers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenSamplers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glPushDebugGroup(self, arg0: int, arg1: int, arg2: str):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glPushDebugGroup(int,int,java.lang.String)"""
        super(__GL32Interceptor, self).glPushDebugGroup(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glClearBufferfi(self, arg0: int, arg1: int, arg2: float, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferfi(int,int,float,int)"""
        super(__GL30Interceptor, self).glClearBufferfi(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glUniformMatrix2x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix2x3fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def getShaderSwitches(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getShaderSwitches()"""
        return int.__wrap(super(GLInterceptor, self).getShaderSwitches())

    @override
    @overload
    def glUseProgramStages(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glUseProgramStages(int,int,int)"""
        super(__GL31Interceptor, self).glUseProgramStages(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glTexBuffer(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glTexBuffer(int,int,int)"""
        super(__GL32Interceptor, self).glTexBuffer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glGenSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenSamplers(int,int[],int)"""
        super(__GL30Interceptor, self).glGenSamplers(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glRenderbufferStorageMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glRenderbufferStorageMultisample(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glRenderbufferStorageMultisample(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glTexStorage2DMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glTexStorage2DMultisample(int,int,int,int,int,boolean)"""
        super(__GL31Interceptor, self).glTexStorage2DMultisample(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __boolean.valueOf(arg5))

    @override
    @overload
    def glSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glSamplerParameterfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def getCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getCalls()"""
        return int.__wrap(super(GLInterceptor, self).getCalls())

    @override
    @overload
    def glShaderBinary(self, arg0: int, arg1: 'IntBuffer', arg2: int, arg3: 'Buffer', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glShaderBinary(int,java.nio.IntBuffer,int,java.nio.Buffer,int)"""
        super(__GL30Interceptor, self).glShaderBinary(__int.valueOf(arg0), arg1, __int.valueOf(arg2), arg3, __int.valueOf(arg4))

    @override
    @overload
    def glProgramUniform1uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform1uiv(int,int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glProgramUniform1uiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDisableVertexAttribArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDisableVertexAttribArray(int)"""
        super(__GL30Interceptor, self).glDisableVertexAttribArray(__int.valueOf(arg0))

    @overload
    def glIsShader(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsShader(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsShader(__int.valueOf(arg0)))

    @override
    @overload
    def glProgramUniform2ui(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform2ui(int,int,int,int)"""
        super(__GL31Interceptor, self).glProgramUniform2ui(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glBlendBarrier(self):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glBlendBarrier()"""
        super(GL32Interceptor, self).glBlendBarrier()

    @override
    @overload
    def glGetSamplerParameterIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glGetSamplerParameterIuiv(int,int,java.nio.IntBuffer)"""
        super(__GL32Interceptor, self).glGetSamplerParameterIuiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteVertexArrays(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteVertexArrays(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glFlush(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFlush()"""
        super(GL30Interceptor, self).glFlush()

    @override
    @overload
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTransformFeedbacks(int,int[],int)"""
        super(__GL30Interceptor, self).glGenTransformFeedbacks(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glVertexAttrib4fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib4fv(int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glVertexAttrib4fv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glDrawElementsInstancedBaseVertex(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glDrawElementsInstancedBaseVertex(int,int,int,int,int,int)"""
        super(__GL32Interceptor, self).glDrawElementsInstancedBaseVertex(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @override
    @overload
    def glBindProgramPipeline(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glBindProgramPipeline(int)"""
        super(__GL31Interceptor, self).glBindProgramPipeline(__int.valueOf(arg0))

    @override
    @overload
    def glDeleteRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteRenderbuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteRenderbuffers(__int.valueOf(arg0), arg1)

    @overload
    def glGetProgramResourceName(self, arg0: int, arg1: int, arg2: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramResourceName(int,int,int)"""
        return str.__wrap(super(__GL31Interceptor, self).glGetProgramResourceName(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def glGenVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenVertexArrays(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenVertexArrays(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glDrawArraysInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawArraysInstanced(int,int,int,int)"""
        super(__GL30Interceptor, self).glDrawArraysInstanced(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3fv(int,int,float[],int)"""
        super(__GL30Interceptor, self).glUniform3fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @overload
    def glGetUniformLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformLocation(int,java.lang.String)"""
        return int.__wrap(super(__GL30Interceptor, self).glGetUniformLocation(__int.valueOf(arg0), arg1))

    @override
    @overload
    def glShaderSource(self, arg0: int, arg1: str):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glShaderSource(int,java.lang.String)"""
        super(__GL30Interceptor, self).glShaderSource(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glProgramUniformMatrix3x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix3x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glProgramUniformMatrix3x4fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glBindFramebuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindFramebuffer(int,int)"""
        super(__GL30Interceptor, self).glBindFramebuffer(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glGetProgramResourceiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramResourceiv(int,int,int,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glGetProgramResourceiv(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, arg4, arg5)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def glValidateProgramPipeline(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glValidateProgramPipeline(int)"""
        super(__GL31Interceptor, self).glValidateProgramPipeline(__int.valueOf(arg0))

    @override
    @overload
    def glProgramUniform3uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform3uiv(int,int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glProgramUniform3uiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glVertexAttribFormat(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glVertexAttribFormat(int,int,int,boolean,int)"""
        super(__GL31Interceptor, self).glVertexAttribFormat(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glTexParameterIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glTexParameterIuiv(int,int,java.nio.IntBuffer)"""
        super(__GL32Interceptor, self).glTexParameterIuiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDrawElementsInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawElementsInstanced(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glDrawElementsInstanced(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def resolveErrorNumber(arg0: int) -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.profiling.GLInterceptor.resolveErrorNumber(int)"""
        return str.__wrap(__GLInterceptor.resolveErrorNumber(__int.valueOf(arg0)))

    @override
    @overload
    def glTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glTexParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glProgramUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform2iv(int,int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glProgramUniform2iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetUniformfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glGetUniformfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform2f(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2f(int,float,float)"""
        super(__GL30Interceptor, self).glUniform2f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def glBeginQuery(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBeginQuery(int,int)"""
        super(__GL30Interceptor, self).glBeginQuery(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glProgramUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform1fv(int,int,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glProgramUniform1fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glBlitFramebuffer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlitFramebuffer(int,int,int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glBlitFramebuffer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9))

    @override
    @overload
    def glProgramUniform1i(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform1i(int,int,int)"""
        super(__GL31Interceptor, self).glProgramUniform1i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glBlendEquationSeparatei(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glBlendEquationSeparatei(int,int,int)"""
        super(__GL32Interceptor, self).glBlendEquationSeparatei(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glReadnPixels(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glReadnPixels(int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL32Interceptor, self).glReadnPixels(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), arg7)

    @override
    @overload
    def glDeleteQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteQueries(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteQueries(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glBindImageTexture(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glBindImageTexture(int,int,int,boolean,int,int,int)"""
        super(__GL31Interceptor, self).glBindImageTexture(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def glUseProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUseProgram(int)"""
        super(__GL30Interceptor, self).glUseProgram(__int.valueOf(arg0))

    @override
    @overload
    def glGetTexParameterIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glGetTexParameterIiv(int,int,java.nio.IntBuffer)"""
        super(__GL32Interceptor, self).glGetTexParameterIiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2fv(int,int,float[],int)"""
        super(__GL30Interceptor, self).glUniform2fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glProgramUniform3f(self, arg0: int, arg1: int, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform3f(int,int,float,float,float)"""
        super(__GL31Interceptor, self).glProgramUniform3f(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix2fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1fv(int,int,float[],int)"""
        super(__GL30Interceptor, self).glUniform1fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3fv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniform3fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def getVertexCount(self) -> 'math.FloatCounter':
        """public com.badlogic.gdx.math.FloatCounter com.badlogic.gdx.graphics.profiling.GLInterceptor.getVertexCount()"""
        return 'math.FloatCounter'.__wrap(super(GLInterceptor, self).getVertexCount())

    @override
    @overload
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawElements(int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glDrawElements(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def glReadPixels(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glReadPixels(int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glReadPixels(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), arg6)

    @override
    @overload
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage3D(int,int,int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glTexImage3D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9))

    @override
    @overload
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1iv(int,int,int[],int)"""
        super(__GL30Interceptor, self).glUniform1iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glDeleteRenderbuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteRenderbuffer(int)"""
        super(__GL30Interceptor, self).glDeleteRenderbuffer(__int.valueOf(arg0))

    @override
    @overload
    def glCreateProgram(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCreateProgram()"""
        return int.__wrap(super(GL30Interceptor, self).glCreateProgram())

    @override
    @overload
    def glProgramUniformMatrix4x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix4x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glProgramUniformMatrix4x2fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glDrawElementsBaseVertex(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glDrawElementsBaseVertex(int,int,int,java.nio.Buffer,int)"""
        super(__GL32Interceptor, self).glDrawElementsBaseVertex(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, __int.valueOf(arg4))

    @override
    @overload
    def glDeleteShader(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteShader(int)"""
        super(__GL30Interceptor, self).glDeleteShader(__int.valueOf(arg0))

    @overload
    def glIsTransformFeedback(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsTransformFeedback(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsTransformFeedback(__int.valueOf(arg0)))

    @override
    @overload
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix3fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glHint(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glHint(int,int)"""
        super(__GL30Interceptor, self).glHint(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glGetVertexAttribIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribIuiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetVertexAttribIuiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDispatchComputeIndirect(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glDispatchComputeIndirect(long)"""
        super(__GL31Interceptor, self).glDispatchComputeIndirect(__long.valueOf(arg0))

    @override
    @overload
    def glProgramParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glProgramParameteri(int,int,int)"""
        super(__GL30Interceptor, self).glProgramParameteri(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glCompileShader(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCompileShader(int)"""
        super(__GL30Interceptor, self).glCompileShader(__int.valueOf(arg0))

    @override
    @overload
    def glBindSampler(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindSampler(int,int)"""
        super(__GL30Interceptor, self).glBindSampler(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glFinish(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFinish()"""
        super(GL30Interceptor, self).glFinish()

    @overload
    def glCheckFramebufferStatus(self, arg0: int) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCheckFramebufferStatus(int)"""
        return int.__wrap(super(__GL30Interceptor, self).glCheckFramebufferStatus(__int.valueOf(arg0)))

    @override
    @overload
    def glUniformMatrix2x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix2x4fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glSampleMaski(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glSampleMaski(int,int)"""
        super(__GL31Interceptor, self).glSampleMaski(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def glGetProgramPipelineInfoLog(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramPipelineInfoLog(int)"""
        return str.__wrap(super(__GL31Interceptor, self).glGetProgramPipelineInfoLog(__int.valueOf(arg0)))

    @override
    @overload
    def glGenFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenFramebuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenFramebuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniform4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4f(int,float,float,float,float)"""
        super(__GL30Interceptor, self).glUniform4f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4fv(int,int,float[],int)"""
        super(__GL30Interceptor, self).glUniform4fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glGetVertexAttribfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glGetVertexAttribfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribPointer(int,int,int,boolean,int,int)"""
        super(__GL30Interceptor, self).glVertexAttribPointer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @override
    @overload
    def glRenderbufferStorage(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glRenderbufferStorage(int,int,int,int)"""
        super(__GL30Interceptor, self).glRenderbufferStorage(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glStencilMaskSeparate(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilMaskSeparate(int,int)"""
        super(__GL30Interceptor, self).glStencilMaskSeparate(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glGetInteger64v(self, arg0: int, arg1: 'LongBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetInteger64v(int,java.nio.LongBuffer)"""
        super(__GL30Interceptor, self).glGetInteger64v(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniformMatrix4x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix4x2fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glFramebufferParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glFramebufferParameteri(int,int,int)"""
        super(__GL31Interceptor, self).glFramebufferParameteri(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glGetnUniformiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glGetnUniformiv(int,int,java.nio.IntBuffer)"""
        super(__GL32Interceptor, self).glGetnUniformiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDepthRangef(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDepthRangef(float,float)"""
        super(__GL30Interceptor, self).glDepthRangef(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def glColorMaski(self, arg0: int, arg1: bool, arg2: bool, arg3: bool, arg4: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glColorMaski(int,boolean,boolean,boolean,boolean)"""
        super(__GL32Interceptor, self).glColorMaski(__int.valueOf(arg0), __boolean.valueOf(arg1), __boolean.valueOf(arg2), __boolean.valueOf(arg3), __boolean.valueOf(arg4))

    @override
    @overload
    def glGetTexLevelParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetTexLevelParameteriv(int,int,int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glGetTexLevelParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def glDeleteSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteSamplers(int,int[],int)"""
        super(__GL30Interceptor, self).glDeleteSamplers(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glCopyTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyTexImage2D(int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glCopyTexImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7))

    @override
    @overload
    def glValidateProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glValidateProgram(int)"""
        super(__GL30Interceptor, self).glValidateProgram(__int.valueOf(arg0))

    @override
    @overload
    def glProgramUniform4uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform4uiv(int,int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glProgramUniform4uiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glBlendFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendFuncSeparate(int,int,int,int)"""
        super(__GL30Interceptor, self).glBlendFuncSeparate(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3fv(int,int,boolean,float[],int)"""
        super(__GL30Interceptor, self).glUniformMatrix3fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3, __int.valueOf(arg4))

    @override
    @overload
    def glCopyBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyBufferSubData(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glCopyBufferSubData(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glClearColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearColor(float,float,float,float)"""
        super(__GL30Interceptor, self).glClearColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def glDebugMessageControl(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer', arg4: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glDebugMessageControl(int,int,int,java.nio.IntBuffer,boolean)"""
        super(__GL32Interceptor, self).glDebugMessageControl(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, __boolean.valueOf(arg4))

    @override
    @overload
    def glDebugMessageInsert(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: str):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glDebugMessageInsert(int,int,int,int,java.lang.String)"""
        super(__GL32Interceptor, self).glDebugMessageInsert(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4)

    @override
    @overload
    def glVertexAttribDivisor(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribDivisor(int,int)"""
        super(__GL30Interceptor, self).glVertexAttribDivisor(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glGetUniformuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformuiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetUniformuiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniformMatrix3x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix3x4fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glGetProgramInterfaceiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramInterfaceiv(int,int,int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glGetProgramInterfaceiv(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def glGenFramebuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenFramebuffer()"""
        return int.__wrap(super(GL30Interceptor, self).glGenFramebuffer())

    @override
    @overload
    def glVertexBindingDivisor(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glVertexBindingDivisor(int,int)"""
        super(__GL31Interceptor, self).glVertexBindingDivisor(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glObjectLabel(self, arg0: int, arg1: int, arg2: str):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glObjectLabel(int,int,java.lang.String)"""
        super(__GL32Interceptor, self).glObjectLabel(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glCopyImageSubData(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glCopyImageSubData(int,int,int,int,int,int,int,int,int,int,int,int,int,int,int)"""
        super(__GL32Interceptor, self).glCopyImageSubData(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13), __int.valueOf(arg14))

    @override
    @overload
    def glDrawBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawBuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDrawBuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glDeleteProgramPipelines(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glDeleteProgramPipelines(int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glDeleteProgramPipelines(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glViewport(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glViewport(int,int,int,int)"""
        super(__GL30Interceptor, self).glViewport(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glBeginTransformFeedback(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBeginTransformFeedback(int)"""
        super(__GL30Interceptor, self).glBeginTransformFeedback(__int.valueOf(arg0))

    @override
    @overload
    def glGenQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenQueries(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenQueries(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetMultisamplefv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetMultisamplefv(int,int,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glGetMultisamplefv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glActiveTexture(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glActiveTexture(int)"""
        super(__GL30Interceptor, self).glActiveTexture(__int.valueOf(arg0))

    @override
    @overload
    def glDetachShader(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDetachShader(int,int)"""
        super(__GL30Interceptor, self).glDetachShader(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glSamplerParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glFramebufferTexture(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glFramebufferTexture(int,int,int,int)"""
        super(__GL32Interceptor, self).glFramebufferTexture(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glBlendFuncSeparatei(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glBlendFuncSeparatei(int,int,int,int,int)"""
        super(__GL32Interceptor, self).glBlendFuncSeparatei(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTransformFeedbacks(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteTransformFeedbacks(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glProgramUniform2i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform2i(int,int,int,int)"""
        super(__GL31Interceptor, self).glProgramUniform2i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glBlendColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendColor(float,float,float,float)"""
        super(__GL30Interceptor, self).glBlendColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def glTexParameterIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glTexParameterIiv(int,int,java.nio.IntBuffer)"""
        super(__GL32Interceptor, self).glTexParameterIiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform1i(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1i(int,int)"""
        super(__GL30Interceptor, self).glUniform1i(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage2D(int,int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glTexImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8))

    @override
    @overload
    def glBlendEquationSeparate(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendEquationSeparate(int,int)"""
        super(__GL30Interceptor, self).glBlendEquationSeparate(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def glGetActiveUniform(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer') -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniform(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetActiveUniform(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3))

    @override
    @overload
    def glProgramUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform2fv(int,int,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glProgramUniform2fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4iv(int,int,int[],int)"""
        super(__GL30Interceptor, self).glUniform4iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glBindRenderbuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindRenderbuffer(int,int)"""
        super(__GL30Interceptor, self).glBindRenderbuffer(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glUniform1f(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1f(int,float)"""
        super(__GL30Interceptor, self).glUniform1f(__int.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def glCopyTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyTexSubImage3D(int,int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glCopyTexSubImage3D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8))

    @override
    @overload
    def glVertexAttribIFormat(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glVertexAttribIFormat(int,int,int,int)"""
        super(__GL31Interceptor, self).glVertexAttribIFormat(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glScissor(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glScissor(int,int,int,int)"""
        super(__GL30Interceptor, self).glScissor(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glStencilFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilFuncSeparate(int,int,int,int)"""
        super(__GL30Interceptor, self).glStencilFuncSeparate(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glProgramUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform3iv(int,int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glProgramUniform3iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glVertexAttrib3fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib3fv(int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glVertexAttrib3fv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glTexStorage3DMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glTexStorage3DMultisample(int,int,int,int,int,int,boolean)"""
        super(__GL32Interceptor, self).glTexStorage3DMultisample(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __boolean.valueOf(arg6))

    @override
    @overload
    def glVertexAttrib2f(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib2f(int,float,float)"""
        super(__GL30Interceptor, self).glVertexAttrib2f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glTexSubImage3D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10))

    @override
    @overload
    def glProgramUniformMatrix2x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix2x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glProgramUniformMatrix2x3fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @overload
    def glMapBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Buffer':
        """public java.nio.Buffer com.badlogic.gdx.graphics.profiling.GL30Interceptor.glMapBufferRange(int,int,int,int)"""
        return 'Buffer'.__wrap(super(__GL30Interceptor, self).glMapBufferRange(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def glGetError(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetError()"""
        return int.__wrap(super(GL30Interceptor, self).glGetError())

    @override
    @overload
    def glGetShaderPrecisionFormat(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetShaderPrecisionFormat(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetShaderPrecisionFormat(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3iv(int,int,int[],int)"""
        super(__GL30Interceptor, self).glUniform3iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glBlendFunc(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendFunc(int,int)"""
        super(__GL30Interceptor, self).glBlendFunc(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glFramebufferRenderbuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFramebufferRenderbuffer(int,int,int,int)"""
        super(__GL30Interceptor, self).glFramebufferRenderbuffer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glGetUniformIndices(self, arg0: int, arg1: 'String', arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformIndices(int,java.lang.String[],java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetUniformIndices(__int.valueOf(arg0), arg1, arg2)

    @override
    @overload
    def glGetProgramiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetProgramiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetProgramiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4fv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniform4fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @overload
    def glGetPointerv(self, arg0: int) -> int:
        """public long com.badlogic.gdx.graphics.profiling.GL32Interceptor.glGetPointerv(int)"""
        return int.__wrap(super(__GL32Interceptor, self).glGetPointerv(__int.valueOf(arg0)))

    @override
    @overload
    def glGetFramebufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetFramebufferParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glGetFramebufferParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glFramebufferTextureLayer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFramebufferTextureLayer(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glFramebufferTextureLayer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glProgramUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glProgramUniformMatrix4fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glProgramUniformMatrix3x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix3x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glProgramUniformMatrix3x2fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4iv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform4iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2iv(int,int,int[],int)"""
        super(__GL30Interceptor, self).glUniform2iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glProgramUniform2uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform2uiv(int,int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glProgramUniform2uiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteQueries(int,int[],int)"""
        super(__GL30Interceptor, self).glDeleteQueries(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glTexParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameteri(int,int,int)"""
        super(__GL30Interceptor, self).glTexParameteri(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glGetSamplerParameterIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glGetSamplerParameterIiv(int,int,java.nio.IntBuffer)"""
        super(__GL32Interceptor, self).glGetSamplerParameterIiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniformBlockBinding(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformBlockBinding(int,int,int)"""
        super(__GL30Interceptor, self).glUniformBlockBinding(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glGetVertexAttribiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetVertexAttribiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glInvalidateFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glInvalidateFramebuffer(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glInvalidateFramebuffer(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @overload
    def glIsProgramPipeline(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL31Interceptor.glIsProgramPipeline(int)"""
        return bool.__wrap(super(__GL31Interceptor, self).glIsProgramPipeline(__int.valueOf(arg0)))

    @override
    @overload
    def glVertexAttribIPointer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribIPointer(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glVertexAttribIPointer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glStencilOp(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilOp(int,int,int)"""
        super(__GL30Interceptor, self).glStencilOp(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glBufferData(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBufferData(int,int,java.nio.Buffer,int)"""
        super(__GL30Interceptor, self).glBufferData(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @overload
    def glIsEnabledi(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL32Interceptor.glIsEnabledi(int,int)"""
        return bool.__wrap(super(__GL32Interceptor, self).glIsEnabledi(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def glProgramUniform1f(self, arg0: int, arg1: int, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform1f(int,int,float)"""
        super(__GL31Interceptor, self).glProgramUniform1f(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def glUniform1uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1uiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform1uiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glSampleCoverage(self, arg0: float, arg1: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSampleCoverage(float,boolean)"""
        super(__GL30Interceptor, self).glSampleCoverage(__float.valueOf(arg0), __boolean.valueOf(arg1))

    @override
    @overload
    def glFramebufferTexture2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFramebufferTexture2D(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glFramebufferTexture2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glDeleteSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteSamplers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteSamplers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetShaderiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetShaderiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetShaderiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glProgramUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform4fv(int,int,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glProgramUniform4fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @overload
    def glIsSampler(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsSampler(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsSampler(__int.valueOf(arg0)))

    @override
    @overload
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTransformFeedbacks(int,int[],int)"""
        super(__GL30Interceptor, self).glDeleteTransformFeedbacks(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glDrawRangeElementsBaseVertex(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'Buffer', arg6: int):
        """public void com.badlogic.gdx.graphics.profiling.GL32Interceptor.glDrawRangeElementsBaseVertex(int,int,int,int,int,java.nio.Buffer,int)"""
        super(__GL32Interceptor, self).glDrawRangeElementsBaseVertex(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __int.valueOf(arg6)) 
 
 
# CLASS: com.badlogic.gdx.graphics.profiling.GLInterceptor
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.graphics.profiling.GLInterceptor as __GLInterceptor
__GLInterceptor = __GLInterceptor
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.nio.IntBuffer as IntBuffer
from builtins import float
from abc import abstractmethod, ABC
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Long as __long
import com.badlogic.gdx.math.FloatCounter as __FloatCounter
__FloatCounter = __FloatCounter
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.GL20 as __GL20
__GL20 = __GL20
import java.nio.Buffer as Buffer
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GLInterceptor(ABC):
    """com.badlogic.gdx.graphics.profiling.GLInterceptor"""
 
    @staticmethod
    def __wrap(java_value: __GLInterceptor) -> 'GLInterceptor':
        return GLInterceptor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLInterceptor):
        """
        Dynamic initializer for GLInterceptor.
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

    @overload
    def getShaderSwitches(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getShaderSwitches()"""
        return int.__wrap(super(GLInterceptor, self).getShaderSwitches())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

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

    @staticmethod
    @overload
    def resolveErrorNumber(arg0: int) -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.profiling.GLInterceptor.resolveErrorNumber(int)"""
        return str.__wrap(__GLInterceptor.resolveErrorNumber(__int.valueOf(arg0)))

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

    @overload
    def getCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getCalls()"""
        return int.__wrap(super(GLInterceptor, self).getCalls())

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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

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

    @overload
    def getVertexCount(self) -> 'math.FloatCounter':
        """public com.badlogic.gdx.math.FloatCounter com.badlogic.gdx.graphics.profiling.GLInterceptor.getVertexCount()"""
        return 'math.FloatCounter'.__wrap(super(GLInterceptor, self).getVertexCount())

    @abstractmethod
    def glIsEnabled(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsEnabled(int)"""
        pass

    @overload
    def getTextureBindings(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getTextureBindings()"""
        return int.__wrap(super(GLInterceptor, self).getTextureBindings())

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

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

    @overload
    def getDrawCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getDrawCalls()"""
        return int.__wrap(super(GLInterceptor, self).getDrawCalls())

    @abstractmethod
    def glFrontFace(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFrontFace(int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.profiling.GL20Interceptor
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.graphics.profiling.GLInterceptor as __GLInterceptor
__GLInterceptor = __GLInterceptor
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
import java.nio.IntBuffer as IntBuffer
from builtins import type
from builtins import float
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Long as __long
import java.lang.Float as __float
import com.badlogic.gdx.math.FloatCounter as __FloatCounter
__FloatCounter = __FloatCounter
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import com.badlogic.gdx.graphics.profiling.GL20Interceptor as __GL20Interceptor
__GL20Interceptor = __GL20Interceptor
import java.nio.Buffer as Buffer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import int
 
class GL20Interceptor():
    """com.badlogic.gdx.graphics.profiling.GL20Interceptor"""
 
    @staticmethod
    def __wrap(java_value: __GL20Interceptor) -> 'GL20Interceptor':
        return GL20Interceptor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GL20Interceptor):
        """
        Dynamic initializer for GL20Interceptor.
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
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform1iv(int,int,int[],int)"""
        super(__GL20Interceptor, self).glUniform1iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glDeleteBuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteBuffer(int)"""
        super(__GL20Interceptor, self).glDeleteBuffer(__int.valueOf(arg0))

    @override
    @overload
    def glTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glTexParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL20Interceptor, self).glTexParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glBindRenderbuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBindRenderbuffer(int,int)"""
        super(__GL20Interceptor, self).glBindRenderbuffer(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glBlendEquation(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBlendEquation(int)"""
        super(__GL20Interceptor, self).glBlendEquation(__int.valueOf(arg0))

    @override
    @overload
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform2iv(int,int,java.nio.IntBuffer)"""
        super(__GL20Interceptor, self).glUniform2iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteRenderbuffers(int,java.nio.IntBuffer)"""
        super(__GL20Interceptor, self).glDeleteRenderbuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glStencilMask(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glStencilMask(int)"""
        super(__GL20Interceptor, self).glStencilMask(__int.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def glGetFloatv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetFloatv(int,java.nio.FloatBuffer)"""
        super(__GL20Interceptor, self).glGetFloatv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetShaderiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetShaderiv(int,int,java.nio.IntBuffer)"""
        super(__GL20Interceptor, self).glGetShaderiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @overload
    def glIsShader(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL20Interceptor.glIsShader(int)"""
        return bool.__wrap(super(__GL20Interceptor, self).glIsShader(__int.valueOf(arg0)))

    @override
    @overload
    def glGetRenderbufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetRenderbufferParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL20Interceptor, self).glGetRenderbufferParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDisable(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDisable(int)"""
        super(__GL20Interceptor, self).glDisable(__int.valueOf(arg0))

    @override
    @overload
    def glGenBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenBuffers(int,java.nio.IntBuffer)"""
        super(__GL20Interceptor, self).glGenBuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glBlendFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBlendFuncSeparate(int,int,int,int)"""
        super(__GL20Interceptor, self).glBlendFuncSeparate(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glVertexAttrib4fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttrib4fv(int,java.nio.FloatBuffer)"""
        super(__GL20Interceptor, self).glVertexAttrib4fv(__int.valueOf(arg0), arg1)

    @overload
    def glIsBuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL20Interceptor.glIsBuffer(int)"""
        return bool.__wrap(super(__GL20Interceptor, self).glIsBuffer(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def glStencilOp(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glStencilOp(int,int,int)"""
        super(__GL20Interceptor, self).glStencilOp(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glStencilFunc(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glStencilFunc(int,int,int)"""
        super(__GL20Interceptor, self).glStencilFunc(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glTexParameterf(self, arg0: int, arg1: int, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glTexParameterf(int,int,float)"""
        super(__GL20Interceptor, self).glTexParameterf(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2))

    @staticmethod
    @overload
    def resolveErrorNumber(arg0: int) -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.profiling.GLInterceptor.resolveErrorNumber(int)"""
        return str.__wrap(__GLInterceptor.resolveErrorNumber(__int.valueOf(arg0)))

    @override
    @overload
    def glUniform3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform3f(int,float,float,float)"""
        super(__GL20Interceptor, self).glUniform3f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def glShaderBinary(self, arg0: int, arg1: 'IntBuffer', arg2: int, arg3: 'Buffer', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glShaderBinary(int,java.nio.IntBuffer,int,java.nio.Buffer,int)"""
        super(__GL20Interceptor, self).glShaderBinary(__int.valueOf(arg0), arg1, __int.valueOf(arg2), arg3, __int.valueOf(arg4))

    @override
    @overload
    def glDrawArrays(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDrawArrays(int,int,int)"""
        super(__GL20Interceptor, self).glDrawArrays(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL20Interceptor, self).glUniformMatrix3fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glDetachShader(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDetachShader(int,int)"""
        super(__GL20Interceptor, self).glDetachShader(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glGetFramebufferAttachmentParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetFramebufferAttachmentParameteriv(int,int,int,java.nio.IntBuffer)"""
        super(__GL20Interceptor, self).glGetFramebufferAttachmentParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def glDeleteRenderbuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteRenderbuffer(int)"""
        super(__GL20Interceptor, self).glDeleteRenderbuffer(__int.valueOf(arg0))

    @override
    @overload
    def glGetProgramiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetProgramiv(int,int,java.nio.IntBuffer)"""
        super(__GL20Interceptor, self).glGetProgramiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform2i(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform2i(int,int,int)"""
        super(__GL20Interceptor, self).glUniform2i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttribPointer(int,int,int,boolean,int,int)"""
        super(__GL20Interceptor, self).glVertexAttribPointer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @override
    @overload
    def glCullFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCullFace(int)"""
        super(__GL20Interceptor, self).glCullFace(__int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def glDepthFunc(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDepthFunc(int)"""
        super(__GL20Interceptor, self).glDepthFunc(__int.valueOf(arg0))

    @override
    @overload
    def glFlush(self):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glFlush()"""
        super(GL20Interceptor, self).glFlush()

    @override
    @overload
    def glUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform3i(int,int,int,int)"""
        super(__GL20Interceptor, self).glUniform3i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDrawElements(int,int,int,int)"""
        super(__GL20Interceptor, self).glDrawElements(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttribPointer(int,int,int,boolean,int,java.nio.Buffer)"""
        super(__GL20Interceptor, self).glVertexAttribPointer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __int.valueOf(arg4), arg5)

    @override
    @overload
    def glGenRenderbuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenRenderbuffer()"""
        return int.__wrap(super(GL20Interceptor, self).glGenRenderbuffer())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glBlendColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBlendColor(float,float,float,float)"""
        super(__GL20Interceptor, self).glBlendColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def glUniform4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform4f(int,float,float,float,float)"""
        super(__GL20Interceptor, self).glUniform4f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def getVertexCount(self) -> 'math.FloatCounter':
        """public com.badlogic.gdx.math.FloatCounter com.badlogic.gdx.graphics.profiling.GLInterceptor.getVertexCount()"""
        return 'math.FloatCounter'.__wrap(super(GLInterceptor, self).getVertexCount())

    @override
    @overload
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL20Interceptor, self).glUniformMatrix4fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glShaderSource(self, arg0: int, arg1: str):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glShaderSource(int,java.lang.String)"""
        super(__GL20Interceptor, self).glShaderSource(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glHint(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glHint(int,int)"""
        super(__GL20Interceptor, self).glHint(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glGetVertexAttribiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetVertexAttribiv(int,int,java.nio.IntBuffer)"""
        super(__GL20Interceptor, self).glGetVertexAttribiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glClear(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glClear(int)"""
        super(__GL20Interceptor, self).glClear(__int.valueOf(arg0))

    @override
    @overload
    def glVertexAttrib2f(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttrib2f(int,float,float)"""
        super(__GL20Interceptor, self).glVertexAttrib2f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def glBindBuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBindBuffer(int,int)"""
        super(__GL20Interceptor, self).glBindBuffer(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getTextureBindings(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getTextureBindings()"""
        return int.__wrap(super(GLInterceptor, self).getTextureBindings())

    @override
    @overload
    def getDrawCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getDrawCalls()"""
        return int.__wrap(super(GLInterceptor, self).getDrawCalls())

    @override
    @overload
    def glClearStencil(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glClearStencil(int)"""
        super(__GL20Interceptor, self).glClearStencil(__int.valueOf(arg0))

    @override
    @overload
    def glGetTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetTexParameterfv(int,int,java.nio.FloatBuffer)"""
        super(__GL20Interceptor, self).glGetTexParameterfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glGenBuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenBuffer()"""
        return int.__wrap(super(GL20Interceptor, self).glGenBuffer())

    @override
    @overload
    def glUniform1i(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform1i(int,int)"""
        super(__GL20Interceptor, self).glUniform1i(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glColorMask(self, arg0: bool, arg1: bool, arg2: bool, arg3: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glColorMask(boolean,boolean,boolean,boolean)"""
        super(__GL20Interceptor, self).glColorMask(__boolean.valueOf(arg0), __boolean.valueOf(arg1), __boolean.valueOf(arg2), __boolean.valueOf(arg3))

    @override
    @overload
    def glBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBufferSubData(int,int,int,java.nio.Buffer)"""
        super(__GL20Interceptor, self).glBufferSubData(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def glStencilFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glStencilFuncSeparate(int,int,int,int)"""
        super(__GL20Interceptor, self).glStencilFuncSeparate(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def glDepthRangef(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDepthRangef(float,float)"""
        super(__GL20Interceptor, self).glDepthRangef(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def glGenTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenTextures(int,java.nio.IntBuffer)"""
        super(__GL20Interceptor, self).glGenTextures(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glVertexAttrib1fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttrib1fv(int,java.nio.FloatBuffer)"""
        super(__GL20Interceptor, self).glVertexAttrib1fv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glClearColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glClearColor(float,float,float,float)"""
        super(__GL20Interceptor, self).glClearColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def glGetIntegerv(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetIntegerv(int,java.nio.IntBuffer)"""
        super(__GL20Interceptor, self).glGetIntegerv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform4i(int,int,int,int,int)"""
        super(__GL20Interceptor, self).glUniform4i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glGetUniformiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetUniformiv(int,int,java.nio.IntBuffer)"""
        super(__GL20Interceptor, self).glGetUniformiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniformMatrix4fv(int,int,boolean,float[],int)"""
        super(__GL20Interceptor, self).glUniformMatrix4fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3, __int.valueOf(arg4))

    @override
    @overload
    def glEnable(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glEnable(int)"""
        super(__GL20Interceptor, self).glEnable(__int.valueOf(arg0))

    @override
    @overload
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform4fv(int,int,float[],int)"""
        super(__GL20Interceptor, self).glUniform4fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform3iv(int,int,int[],int)"""
        super(__GL20Interceptor, self).glUniform3iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glDeleteFramebuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteFramebuffer(int)"""
        super(__GL20Interceptor, self).glDeleteFramebuffer(__int.valueOf(arg0))

    @override
    @overload
    def glGenRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenRenderbuffers(int,java.nio.IntBuffer)"""
        super(__GL20Interceptor, self).glGenRenderbuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glDeleteTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteTextures(int,java.nio.IntBuffer)"""
        super(__GL20Interceptor, self).glDeleteTextures(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glLinkProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glLinkProgram(int)"""
        super(__GL20Interceptor, self).glLinkProgram(__int.valueOf(arg0))

    @override
    @overload
    def glTexParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glTexParameteri(int,int,int)"""
        super(__GL20Interceptor, self).glTexParameteri(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glViewport(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glViewport(int,int,int,int)"""
        super(__GL20Interceptor, self).glViewport(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glEnableVertexAttribArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glEnableVertexAttribArray(int)"""
        super(__GL20Interceptor, self).glEnableVertexAttribArray(__int.valueOf(arg0))

    @overload
    def glGetAttribLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetAttribLocation(int,java.lang.String)"""
        return int.__wrap(super(__GL20Interceptor, self).glGetAttribLocation(__int.valueOf(arg0), arg1))

    @override
    @overload
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniformMatrix3fv(int,int,boolean,float[],int)"""
        super(__GL20Interceptor, self).glUniformMatrix3fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3, __int.valueOf(arg4))

    @override
    @overload
    def glVertexAttrib4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttrib4f(int,float,float,float,float)"""
        super(__GL20Interceptor, self).glVertexAttrib4f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def glFramebufferRenderbuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glFramebufferRenderbuffer(int,int,int,int)"""
        super(__GL20Interceptor, self).glFramebufferRenderbuffer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glReleaseShaderCompiler(self):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glReleaseShaderCompiler()"""
        super(GL20Interceptor, self).glReleaseShaderCompiler()

    @override
    @overload
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform1fv(int,int,float[],int)"""
        super(__GL20Interceptor, self).glUniform1fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform2iv(int,int,int[],int)"""
        super(__GL20Interceptor, self).glUniform2iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDrawElements(int,int,int,java.nio.Buffer)"""
        super(__GL20Interceptor, self).glDrawElements(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def glAttachShader(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glAttachShader(int,int)"""
        super(__GL20Interceptor, self).glAttachShader(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def glCheckFramebufferStatus(self, arg0: int) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCheckFramebufferStatus(int)"""
        return int.__wrap(super(__GL20Interceptor, self).glCheckFramebufferStatus(__int.valueOf(arg0)))

    @override
    @overload
    def glBindFramebuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBindFramebuffer(int,int)"""
        super(__GL20Interceptor, self).glBindFramebuffer(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glCreateProgram(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCreateProgram()"""
        return int.__wrap(super(GL20Interceptor, self).glCreateProgram())

    @override
    @overload
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform4iv(int,int,java.nio.IntBuffer)"""
        super(__GL20Interceptor, self).glUniform4iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL20Interceptor, self).glUniformMatrix2fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def glGetUniformfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetUniformfv(int,int,java.nio.FloatBuffer)"""
        super(__GL20Interceptor, self).glGetUniformfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glBlendEquationSeparate(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBlendEquationSeparate(int,int)"""
        super(__GL20Interceptor, self).glBlendEquationSeparate(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glGetBooleanv(self, arg0: int, arg1: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetBooleanv(int,java.nio.Buffer)"""
        super(__GL20Interceptor, self).glGetBooleanv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glGenerateMipmap(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenerateMipmap(int)"""
        super(__GL20Interceptor, self).glGenerateMipmap(__int.valueOf(arg0))

    @overload
    def glGetActiveUniform(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer') -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetActiveUniform(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return str.__wrap(super(__GL20Interceptor, self).glGetActiveUniform(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3))

    @override
    @overload
    def glBlendFunc(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBlendFunc(int,int)"""
        super(__GL20Interceptor, self).glBlendFunc(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glFrontFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glFrontFace(int)"""
        super(__GL20Interceptor, self).glFrontFace(__int.valueOf(arg0))

    @override
    @overload
    def glDeleteBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteBuffers(int,java.nio.IntBuffer)"""
        super(__GL20Interceptor, self).glDeleteBuffers(__int.valueOf(arg0), arg1)

    @overload
    def glGetActiveAttrib(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer') -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetActiveAttrib(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return str.__wrap(super(__GL20Interceptor, self).glGetActiveAttrib(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3))

    @override
    @overload
    def glReadPixels(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glReadPixels(int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL20Interceptor, self).glReadPixels(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), arg6)

    @override
    @overload
    def glBufferData(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBufferData(int,int,java.nio.Buffer,int)"""
        super(__GL20Interceptor, self).glBufferData(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL20Interceptor, self).glTexSubImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), arg8)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def glGetVertexAttribPointerv(self, arg0: int, arg1: int, arg2: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetVertexAttribPointerv(int,int,java.nio.Buffer)"""
        super(__GL20Interceptor, self).glGetVertexAttribPointerv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glStencilMaskSeparate(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glStencilMaskSeparate(int,int)"""
        super(__GL20Interceptor, self).glStencilMaskSeparate(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform1fv(int,int,java.nio.FloatBuffer)"""
        super(__GL20Interceptor, self).glUniform1fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform2fv(int,int,float[],int)"""
        super(__GL20Interceptor, self).glUniform2fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform4iv(int,int,int[],int)"""
        super(__GL20Interceptor, self).glUniform4iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glVertexAttrib3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttrib3f(int,float,float,float)"""
        super(__GL20Interceptor, self).glVertexAttrib3f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def glCopyTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCopyTexImage2D(int,int,int,int,int,int,int,int)"""
        super(__GL20Interceptor, self).glCopyTexImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7))

    @override
    @overload
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform4fv(int,int,java.nio.FloatBuffer)"""
        super(__GL20Interceptor, self).glUniform4fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glBindAttribLocation(self, arg0: int, arg1: int, arg2: str):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBindAttribLocation(int,int,java.lang.String)"""
        super(__GL20Interceptor, self).glBindAttribLocation(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glGenFramebuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenFramebuffer()"""
        return int.__wrap(super(GL20Interceptor, self).glGenFramebuffer())

    @override
    @overload
    def glFinish(self):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glFinish()"""
        super(GL20Interceptor, self).glFinish()

    @override
    @overload
    def glVertexAttrib2fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttrib2fv(int,java.nio.FloatBuffer)"""
        super(__GL20Interceptor, self).glVertexAttrib2fv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetTexParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL20Interceptor, self).glGetTexParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glTexParameterfv(int,int,java.nio.FloatBuffer)"""
        super(__GL20Interceptor, self).glTexParameterfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteShader(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteShader(int)"""
        super(__GL20Interceptor, self).glDeleteShader(__int.valueOf(arg0))

    @overload
    def glIsEnabled(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL20Interceptor.glIsEnabled(int)"""
        return bool.__wrap(super(__GL20Interceptor, self).glIsEnabled(__int.valueOf(arg0)))

    @override
    @overload
    def glSampleCoverage(self, arg0: float, arg1: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glSampleCoverage(float,boolean)"""
        super(__GL20Interceptor, self).glSampleCoverage(__float.valueOf(arg0), __boolean.valueOf(arg1))

    @override
    @overload
    def glValidateProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glValidateProgram(int)"""
        super(__GL20Interceptor, self).glValidateProgram(__int.valueOf(arg0))

    @override
    @overload
    def glFramebufferTexture2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glFramebufferTexture2D(int,int,int,int,int)"""
        super(__GL20Interceptor, self).glFramebufferTexture2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glActiveTexture(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glActiveTexture(int)"""
        super(__GL20Interceptor, self).glActiveTexture(__int.valueOf(arg0))

    @overload
    def glIsRenderbuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL20Interceptor.glIsRenderbuffer(int)"""
        return bool.__wrap(super(__GL20Interceptor, self).glIsRenderbuffer(__int.valueOf(arg0)))

    @override
    @overload
    def glScissor(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glScissor(int,int,int,int)"""
        super(__GL20Interceptor, self).glScissor(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glPolygonOffset(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glPolygonOffset(float,float)"""
        super(__GL20Interceptor, self).glPolygonOffset(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def glGenFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenFramebuffers(int,java.nio.IntBuffer)"""
        super(__GL20Interceptor, self).glGenFramebuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glCompileShader(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCompileShader(int)"""
        super(__GL20Interceptor, self).glCompileShader(__int.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.profiling.GLInterceptor.reset()"""
        super(GLInterceptor, self).reset()

    @override
    @overload
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform3fv(int,int,float[],int)"""
        super(__GL20Interceptor, self).glUniform3fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glBindTexture(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glBindTexture(int,int)"""
        super(__GL20Interceptor, self).glBindTexture(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glVertexAttrib1f(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttrib1f(int,float)"""
        super(__GL20Interceptor, self).glVertexAttrib1f(__int.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def glPixelStorei(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glPixelStorei(int,int)"""
        super(__GL20Interceptor, self).glPixelStorei(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glClearDepthf(self, arg0: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glClearDepthf(float)"""
        super(__GL20Interceptor, self).glClearDepthf(__float.valueOf(arg0))

    @override
    @overload
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform3iv(int,int,java.nio.IntBuffer)"""
        super(__GL20Interceptor, self).glUniform3iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetShaderPrecisionFormat(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetShaderPrecisionFormat(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        super(__GL20Interceptor, self).glGetShaderPrecisionFormat(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def glDisableVertexAttribArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDisableVertexAttribArray(int)"""
        super(__GL20Interceptor, self).glDisableVertexAttribArray(__int.valueOf(arg0))

    @overload
    def glCreateShader(self, arg0: int) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCreateShader(int)"""
        return int.__wrap(super(__GL20Interceptor, self).glCreateShader(__int.valueOf(arg0)))

    @override
    @overload
    def glUniform2f(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform2f(int,float,float)"""
        super(__GL20Interceptor, self).glUniform2f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def glCompressedTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCompressedTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL20Interceptor, self).glCompressedTexSubImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), arg8)

    @override
    @overload
    def glRenderbufferStorage(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glRenderbufferStorage(int,int,int,int)"""
        super(__GL20Interceptor, self).glRenderbufferStorage(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniformMatrix2fv(int,int,boolean,float[],int)"""
        super(__GL20Interceptor, self).glUniformMatrix2fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3, __int.valueOf(arg4))

    @overload
    def glIsFramebuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL20Interceptor.glIsFramebuffer(int)"""
        return bool.__wrap(super(__GL20Interceptor, self).glIsFramebuffer(__int.valueOf(arg0)))

    @override
    @overload
    def glVertexAttrib3fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glVertexAttrib3fv(int,java.nio.FloatBuffer)"""
        super(__GL20Interceptor, self).glVertexAttrib3fv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glDeleteProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteProgram(int)"""
        super(__GL20Interceptor, self).glDeleteProgram(__int.valueOf(arg0))

    @override
    @overload
    def glDepthMask(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDepthMask(boolean)"""
        super(__GL20Interceptor, self).glDepthMask(__boolean.valueOf(arg0))

    @override
    @overload
    def glGetVertexAttribfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetVertexAttribfv(int,int,java.nio.FloatBuffer)"""
        super(__GL20Interceptor, self).glGetVertexAttribfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform3fv(int,int,java.nio.FloatBuffer)"""
        super(__GL20Interceptor, self).glUniform3fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetAttachedShaders(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetAttachedShaders(int,int,java.nio.Buffer,java.nio.IntBuffer)"""
        super(__GL20Interceptor, self).glGetAttachedShaders(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3)

    @overload
    def glGetShaderInfoLog(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetShaderInfoLog(int)"""
        return str.__wrap(super(__GL20Interceptor, self).glGetShaderInfoLog(__int.valueOf(arg0)))

    @override
    @overload
    def glLineWidth(self, arg0: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glLineWidth(float)"""
        super(__GL20Interceptor, self).glLineWidth(__float.valueOf(arg0))

    @override
    @overload
    def glUseProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUseProgram(int)"""
        super(__GL20Interceptor, self).glUseProgram(__int.valueOf(arg0))

    @override
    @overload
    def glUniform1f(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform1f(int,float)"""
        super(__GL20Interceptor, self).glUniform1f(__int.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def glCopyTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCopyTexSubImage2D(int,int,int,int,int,int,int,int)"""
        super(__GL20Interceptor, self).glCopyTexSubImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7))

    @override
    @overload
    def glGetError(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetError()"""
        return int.__wrap(super(GL20Interceptor, self).glGetError())

    @override
    @overload
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glTexImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL20Interceptor, self).glTexImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), arg8)

    @overload
    def glIsTexture(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL20Interceptor.glIsTexture(int)"""
        return bool.__wrap(super(__GL20Interceptor, self).glIsTexture(__int.valueOf(arg0)))

    @override
    @overload
    def glStencilOpSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glStencilOpSeparate(int,int,int,int)"""
        super(__GL20Interceptor, self).glStencilOpSeparate(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def getShaderSwitches(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getShaderSwitches()"""
        return int.__wrap(super(GLInterceptor, self).getShaderSwitches())

    @overload
    def glIsProgram(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL20Interceptor.glIsProgram(int)"""
        return bool.__wrap(super(__GL20Interceptor, self).glIsProgram(__int.valueOf(arg0)))

    @overload
    def glGetString(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetString(int)"""
        return str.__wrap(super(__GL20Interceptor, self).glGetString(__int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def glGenTexture(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGenTexture()"""
        return int.__wrap(super(GL20Interceptor, self).glGenTexture())

    @override
    @overload
    def glCompressedTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glCompressedTexImage2D(int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL20Interceptor, self).glCompressedTexImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), arg7)

    @overload
    def glGetUniformLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetUniformLocation(int,java.lang.String)"""
        return int.__wrap(super(__GL20Interceptor, self).glGetUniformLocation(__int.valueOf(arg0), arg1))

    @override
    @overload
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform1iv(int,int,java.nio.IntBuffer)"""
        super(__GL20Interceptor, self).glUniform1iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteTexture(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteTexture(int)"""
        super(__GL20Interceptor, self).glDeleteTexture(__int.valueOf(arg0))

    @override
    @overload
    def getCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getCalls()"""
        return int.__wrap(super(GLInterceptor, self).getCalls())

    @override
    @overload
    def glDeleteFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glDeleteFramebuffers(int,java.nio.IntBuffer)"""
        super(__GL20Interceptor, self).glDeleteFramebuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetBufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetBufferParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL20Interceptor, self).glGetBufferParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @overload
    def glGetProgramInfoLog(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL20Interceptor.glGetProgramInfoLog(int)"""
        return str.__wrap(super(__GL20Interceptor, self).glGetProgramInfoLog(__int.valueOf(arg0)))

    @override
    @overload
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL20Interceptor.glUniform2fv(int,int,java.nio.FloatBuffer)"""
        super(__GL20Interceptor, self).glUniform2fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2) 
 
 
# CLASS: com.badlogic.gdx.graphics.profiling.GLErrorListener
import com.badlogic.gdx.graphics.profiling.GLErrorListener as __GLErrorListener
__GLErrorListener = __GLErrorListener
from abc import abstractmethod, ABC
 
class GLErrorListener(ABC):
    """com.badlogic.gdx.graphics.profiling.GLErrorListener"""
 
    @staticmethod
    def __wrap(java_value: __GLErrorListener) -> 'GLErrorListener':
        return GLErrorListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLErrorListener):
        """
        Dynamic initializer for GLErrorListener.
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
    def onError(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.profiling.GLErrorListener.onError(int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.profiling.GLProfiler
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.profiling.GLProfiler as __GLProfiler
__GLProfiler = __GLProfiler
import com.badlogic.gdx.graphics.profiling.GLErrorListener as __GLErrorListener
__GLErrorListener = __GLErrorListener
import java.lang.Long as __long
import com.badlogic.gdx.math.FloatCounter as __FloatCounter
__FloatCounter = __FloatCounter
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
from builtins import bool
from builtins import int
 
class GLProfiler():
    """com.badlogic.gdx.graphics.profiling.GLProfiler"""
 
    @staticmethod
    def __wrap(java_value: __GLProfiler) -> 'GLProfiler':
        return GLProfiler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLProfiler):
        """
        Dynamic initializer for GLProfiler.
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
    def getCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLProfiler.getCalls()"""
        return int.__wrap(super(GLProfiler, self).getCalls())

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
    def getTextureBindings(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLProfiler.getTextureBindings()"""
        return int.__wrap(super(GLProfiler, self).getTextureBindings())

    @overload
    def getVertexCount(self) -> 'math.FloatCounter':
        """public com.badlogic.gdx.math.FloatCounter com.badlogic.gdx.graphics.profiling.GLProfiler.getVertexCount()"""
        return 'math.FloatCounter'.__wrap(super(GLProfiler, self).getVertexCount())

    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GLProfiler.isEnabled()"""
        return bool.__wrap(super(GLProfiler, self).isEnabled())

    @overload
    def setListener(self, arg0: 'GLErrorListener'):
        """public void com.badlogic.gdx.graphics.profiling.GLProfiler.setListener(com.badlogic.gdx.graphics.profiling.GLErrorListener)"""
        super(__GLProfiler, self).setListener(arg0)

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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
    def reset(self):
        """public void com.badlogic.gdx.graphics.profiling.GLProfiler.reset()"""
        super(GLProfiler, self).reset()

    @overload
    def getDrawCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLProfiler.getDrawCalls()"""
        return int.__wrap(super(GLProfiler, self).getDrawCalls())

    @overload
    def __init__(self, arg0: 'Graphics'):
        """public com.badlogic.gdx.graphics.profiling.GLProfiler(com.badlogic.gdx.Graphics)"""
        val = __GLProfiler(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getShaderSwitches(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLProfiler.getShaderSwitches()"""
        return int.__wrap(super(GLProfiler, self).getShaderSwitches())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getListener(self) -> 'GLErrorListener':
        """public com.badlogic.gdx.graphics.profiling.GLErrorListener com.badlogic.gdx.graphics.profiling.GLProfiler.getListener()"""
        return 'GLErrorListener'.__wrap(super(GLProfiler, self).getListener()) 
 
 
# CLASS: com.badlogic.gdx.graphics.profiling.GL31Interceptor
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
import com.badlogic.gdx.graphics.profiling.GL30Interceptor as __GL30Interceptor
__GL30Interceptor = __GL30Interceptor
import java.nio.IntBuffer as IntBuffer
from builtins import type
import java.nio.FloatBuffer as FloatBuffer
import com.badlogic.gdx.math.FloatCounter as __FloatCounter
__FloatCounter = __FloatCounter
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import str
import com.badlogic.gdx.graphics.profiling.GLInterceptor as __GLInterceptor
__GLInterceptor = __GLInterceptor
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
import java.nio.LongBuffer as LongBuffer
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.nio.Buffer as Buffer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.graphics.profiling.GL31Interceptor as __GL31Interceptor
__GL31Interceptor = __GL31Interceptor
import java.nio.Buffer as __Buffer
__Buffer = __Buffer
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class GL31Interceptor():
    """com.badlogic.gdx.graphics.profiling.GL31Interceptor"""
 
    @staticmethod
    def __wrap(java_value: __GL31Interceptor) -> 'GL31Interceptor':
        return GL31Interceptor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GL31Interceptor):
        """
        Dynamic initializer for GL31Interceptor.
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
    def glUniform3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3f(int,float,float,float)"""
        super(__GL30Interceptor, self).glUniform3f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def glPauseTransformFeedback(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glPauseTransformFeedback()"""
        super(GL30Interceptor, self).glPauseTransformFeedback()

    @overload
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformBlockName(int,int)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetActiveUniformBlockName(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def glGetAttribLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetAttribLocation(int,java.lang.String)"""
        return int.__wrap(super(__GL30Interceptor, self).glGetAttribLocation(__int.valueOf(arg0), arg1))

    @override
    @overload
    def glProgramUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glProgramUniformMatrix3fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glCullFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCullFace(int)"""
        super(__GL30Interceptor, self).glCullFace(__int.valueOf(arg0))

    @override
    @overload
    def glGetSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glGetSamplerParameterfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glProgramUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform3fv(int,int,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glProgramUniform3fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3iv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform3iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glBindBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindBufferRange(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glBindBufferRange(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glGenBuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenBuffer()"""
        return int.__wrap(super(GL30Interceptor, self).glGenBuffer())

    @override
    @overload
    def glGetTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetTexParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetTexParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteTexture(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTexture(int)"""
        super(__GL30Interceptor, self).glDeleteTexture(__int.valueOf(arg0))

    @override
    @overload
    def glCopyTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyTexSubImage2D(int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glCopyTexSubImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7))

    @override
    @overload
    def glVertexAttribI4ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribI4ui(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glVertexAttribI4ui(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glBindTexture(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindTexture(int,int)"""
        super(__GL30Interceptor, self).glBindTexture(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glProgramUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform3i(int,int,int,int,int)"""
        super(__GL31Interceptor, self).glProgramUniform3i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawRangeElements(int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glDrawRangeElements(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5)

    @override
    @overload
    def glGetIntegerv(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetIntegerv(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetIntegerv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glBindVertexBuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glBindVertexBuffer(int,int,long,int)"""
        super(__GL31Interceptor, self).glBindVertexBuffer(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glGetProgramPipelineiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramPipelineiv(int,int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glGetProgramPipelineiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawElements(int,int,int,int)"""
        super(__GL30Interceptor, self).glDrawElements(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def glGetStringi(self, arg0: int, arg1: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetStringi(int,int)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetStringi(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def glGenProgramPipelines(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGenProgramPipelines(int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glGenProgramPipelines(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glLinkProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glLinkProgram(int)"""
        super(__GL30Interceptor, self).glLinkProgram(__int.valueOf(arg0))

    @overload
    def glIsBuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsBuffer(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsBuffer(__int.valueOf(arg0)))

    @override
    @overload
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glTexSubImage3D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), arg10)

    @override
    @overload
    def glDrawArraysIndirect(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glDrawArraysIndirect(int,long)"""
        super(__GL31Interceptor, self).glDrawArraysIndirect(__int.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def glMemoryBarrierByRegion(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glMemoryBarrierByRegion(int)"""
        super(__GL31Interceptor, self).glMemoryBarrierByRegion(__int.valueOf(arg0))

    @override
    @overload
    def glClearBufferuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferuiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glClearBufferuiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDrawElementsIndirect(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glDrawElementsIndirect(int,int,long)"""
        super(__GL31Interceptor, self).glDrawElementsIndirect(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2))

    @override
    @overload
    def glGetQueryiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetQueryiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetQueryiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glClearDepthf(self, arg0: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearDepthf(float)"""
        super(__GL30Interceptor, self).glClearDepthf(__float.valueOf(arg0))

    @override
    @overload
    def glEndQuery(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEndQuery(int)"""
        super(__GL30Interceptor, self).glEndQuery(__int.valueOf(arg0))

    @override
    @overload
    def glCompressedTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCompressedTexImage2D(int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glCompressedTexImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), arg7)

    @override
    @overload
    def glAttachShader(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glAttachShader(int,int)"""
        super(__GL30Interceptor, self).glAttachShader(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glActiveShaderProgram(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glActiveShaderProgram(int,int)"""
        super(__GL31Interceptor, self).glActiveShaderProgram(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glDeleteProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteProgram(int)"""
        super(__GL30Interceptor, self).glDeleteProgram(__int.valueOf(arg0))

    @override
    @overload
    def glTransformFeedbackVaryings(self, arg0: int, arg1: 'String', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTransformFeedbackVaryings(int,java.lang.String[],int)"""
        super(__GL30Interceptor, self).glTransformFeedbackVaryings(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glFlushMappedBufferRange(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFlushMappedBufferRange(int,int,int)"""
        super(__GL30Interceptor, self).glFlushMappedBufferRange(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glTexParameterf(self, arg0: int, arg1: int, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameterf(int,int,float)"""
        super(__GL30Interceptor, self).glTexParameterf(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def glUniform3uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3uiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform3uiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDepthMask(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDepthMask(boolean)"""
        super(__GL30Interceptor, self).glDepthMask(__boolean.valueOf(arg0))

    @override
    @overload
    def glVertexAttrib1f(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib1f(int,float)"""
        super(__GL30Interceptor, self).glVertexAttrib1f(__int.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def glGetBooleanv(self, arg0: int, arg1: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBooleanv(int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glGetBooleanv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetBooleani_v(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetBooleani_v(int,int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glGetBooleani_v(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @overload
    def glGetActiveAttrib(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer') -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveAttrib(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetActiveAttrib(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3))

    @overload
    def glIsFramebuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsFramebuffer(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsFramebuffer(__int.valueOf(arg0)))

    @override
    @overload
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformBlockName(int,int,java.nio.Buffer,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glGetActiveUniformBlockName(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def glVertexAttribI4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribI4i(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glVertexAttribI4i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @overload
    def glGetProgramResourceLocation(self, arg0: int, arg1: int, arg2: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramResourceLocation(int,int,java.lang.String)"""
        return int.__wrap(super(__GL31Interceptor, self).glGetProgramResourceLocation(__int.valueOf(arg0), __int.valueOf(arg1), arg2))

    @override
    @overload
    def glProgramUniform4ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform4ui(int,int,int,int,int,int)"""
        super(__GL31Interceptor, self).glProgramUniform4ui(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @override
    @overload
    def glVertexAttrib1fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib1fv(int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glVertexAttrib1fv(__int.valueOf(arg0), arg1)

    @overload
    def glUnmapBuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUnmapBuffer(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glUnmapBuffer(__int.valueOf(arg0)))

    @overload
    def glIsRenderbuffer(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsRenderbuffer(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsRenderbuffer(__int.valueOf(arg0)))

    @override
    @overload
    def glGenTexture(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTexture()"""
        return int.__wrap(super(GL30Interceptor, self).glGenTexture())

    @override
    @overload
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage3D(int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glTexImage3D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), arg9)

    @overload
    def glIsProgram(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsProgram(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsProgram(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def glBindVertexArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindVertexArray(int)"""
        super(__GL30Interceptor, self).glBindVertexArray(__int.valueOf(arg0))

    @override
    @overload
    def glGetQueryObjectuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetQueryObjectuiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetQueryObjectuiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def getTextureBindings(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getTextureBindings()"""
        return int.__wrap(super(GLInterceptor, self).getTextureBindings())

    @override
    @overload
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawRangeElements(int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glDrawRangeElements(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @override
    @overload
    def getDrawCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getDrawCalls()"""
        return int.__wrap(super(GLInterceptor, self).getDrawCalls())

    @override
    @overload
    def glClearBufferfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glClearBufferfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @overload
    def glCreateShader(self, arg0: int) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCreateShader(int)"""
        return int.__wrap(super(__GL30Interceptor, self).glCreateShader(__int.valueOf(arg0)))

    @override
    @overload
    def glGetActiveUniformBlockiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformBlockiv(int,int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetActiveUniformBlockiv(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def glGetTexLevelParameterfv(self, arg0: int, arg1: int, arg2: int, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetTexLevelParameterfv(int,int,int,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glGetTexLevelParameterfv(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def glBindBuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindBuffer(int,int)"""
        super(__GL30Interceptor, self).glBindBuffer(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBufferSubData(int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glBufferSubData(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @overload
    def glGetBufferPointerv(self, arg0: int, arg1: int) -> 'Buffer':
        """public java.nio.Buffer com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBufferPointerv(int,int)"""
        return 'Buffer'.__wrap(super(__GL30Interceptor, self).glGetBufferPointerv(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def glDeleteBuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteBuffer(int)"""
        super(__GL30Interceptor, self).glDeleteBuffer(__int.valueOf(arg0))

    @override
    @overload
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTransformFeedbacks(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenTransformFeedbacks(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glClear(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClear(int)"""
        super(__GL30Interceptor, self).glClear(__int.valueOf(arg0))

    @override
    @overload
    def glStencilMask(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilMask(int)"""
        super(__GL30Interceptor, self).glStencilMask(__int.valueOf(arg0))

    @override
    @overload
    def glUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3i(int,int,int,int)"""
        super(__GL30Interceptor, self).glUniform3i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glProgramUniformMatrix2x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix2x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glProgramUniformMatrix2x4fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2fv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniform2fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix4fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glGenVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenVertexArrays(int,int[],int)"""
        super(__GL30Interceptor, self).glGenVertexArrays(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glGenQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenQueries(int,int[],int)"""
        super(__GL30Interceptor, self).glGenQueries(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @overload
    def glCreateShaderProgramv(self, arg0: int, arg1: 'String') -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL31Interceptor.glCreateShaderProgramv(int,java.lang.String[])"""
        return int.__wrap(super(__GL31Interceptor, self).glCreateShaderProgramv(__int.valueOf(arg0), arg1))

    @override
    @overload
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1fv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniform1fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def glBindBufferBase(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindBufferBase(int,int,int)"""
        super(__GL30Interceptor, self).glBindBufferBase(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glDepthFunc(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDepthFunc(int)"""
        super(__GL30Interceptor, self).glDepthFunc(__int.valueOf(arg0))

    @override
    @overload
    def glGenRenderbuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenRenderbuffer()"""
        return int.__wrap(super(GL30Interceptor, self).glGenRenderbuffer())

    @override
    @overload
    def glUniformMatrix3x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix3x2fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glBindAttribLocation(self, arg0: int, arg1: int, arg2: str):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindAttribLocation(int,int,java.lang.String)"""
        super(__GL30Interceptor, self).glBindAttribLocation(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glProgramUniform1ui(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform1ui(int,int,int)"""
        super(__GL31Interceptor, self).glProgramUniform1ui(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glGetActiveUniformsiv(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniformsiv(int,int,java.nio.IntBuffer,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetActiveUniformsiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), arg4)

    @override
    @overload
    def glClearStencil(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearStencil(int)"""
        super(__GL30Interceptor, self).glClearStencil(__int.valueOf(arg0))

    @override
    @overload
    def glGetVertexAttribPointerv(self, arg0: int, arg1: int, arg2: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribPointerv(int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glGetVertexAttribPointerv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform2i(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2i(int,int,int)"""
        super(__GL30Interceptor, self).glUniform2i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glProgramUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform4iv(int,int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glProgramUniform4iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glCompressedTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCompressedTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glCompressedTexSubImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), arg8)

    @override
    @overload
    def glStencilOpSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilOpSeparate(int,int,int,int)"""
        super(__GL30Interceptor, self).glStencilOpSeparate(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glMemoryBarrier(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glMemoryBarrier(int)"""
        super(__GL31Interceptor, self).glMemoryBarrier(__int.valueOf(arg0))

    @override
    @overload
    def glGetAttachedShaders(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetAttachedShaders(int,int,java.nio.Buffer,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetAttachedShaders(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def glReadBuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glReadBuffer(int)"""
        super(__GL30Interceptor, self).glReadBuffer(__int.valueOf(arg0))

    @overload
    def glGetProgramResourceIndex(self, arg0: int, arg1: int, arg2: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramResourceIndex(int,int,java.lang.String)"""
        return int.__wrap(super(__GL31Interceptor, self).glGetProgramResourceIndex(__int.valueOf(arg0), __int.valueOf(arg1), arg2))

    @override
    @overload
    def glGetRenderbufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetRenderbufferParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetRenderbufferParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glClearBufferiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glClearBufferiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glVertexAttribBinding(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glVertexAttribBinding(int,int)"""
        super(__GL31Interceptor, self).glVertexAttribBinding(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glVertexAttrib2fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib2fv(int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glVertexAttrib2fv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glDeleteVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteVertexArrays(int,int[],int)"""
        super(__GL30Interceptor, self).glDeleteVertexArrays(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glColorMask(self, arg0: bool, arg1: bool, arg2: bool, arg3: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glColorMask(boolean,boolean,boolean,boolean)"""
        super(__GL30Interceptor, self).glColorMask(__boolean.valueOf(arg0), __boolean.valueOf(arg1), __boolean.valueOf(arg2), __boolean.valueOf(arg3))

    @overload
    def glIsEnabled(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsEnabled(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsEnabled(__int.valueOf(arg0)))

    @override
    @overload
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glTexImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), arg8)

    @override
    @overload
    def glDrawArrays(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawArrays(int,int,int)"""
        super(__GL30Interceptor, self).glDrawArrays(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glGenTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTextures(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenTextures(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glPolygonOffset(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glPolygonOffset(float,float)"""
        super(__GL30Interceptor, self).glPolygonOffset(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def glUniformMatrix4x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix4x3fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1iv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform1iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteBuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteBuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetSamplerParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glEnableVertexAttribArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEnableVertexAttribArray(int)"""
        super(__GL30Interceptor, self).glEnableVertexAttribArray(__int.valueOf(arg0))

    @override
    @overload
    def glUniform4uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4uiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform4uiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glInvalidateSubFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: int, arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glInvalidateSubFramebuffer(int,int,java.nio.IntBuffer,int,int,int,int)"""
        super(__GL30Interceptor, self).glInvalidateSubFramebuffer(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6))

    @override
    @overload
    def glReleaseShaderCompiler(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glReleaseShaderCompiler()"""
        super(GL30Interceptor, self).glReleaseShaderCompiler()

    @override
    @overload
    def glVertexAttrib3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib3f(int,float,float,float)"""
        super(__GL30Interceptor, self).glVertexAttrib3f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def glDeleteFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteFramebuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteFramebuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetBufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBufferParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetBufferParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDisable(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDisable(int)"""
        super(__GL30Interceptor, self).glDisable(__int.valueOf(arg0))

    @overload
    def glIsTexture(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsTexture(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsTexture(__int.valueOf(arg0)))

    @override
    @overload
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glTexSubImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), arg8)

    @override
    @overload
    def glVertexAttrib4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib4f(int,float,float,float,float)"""
        super(__GL30Interceptor, self).glVertexAttrib4f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def glGetFramebufferAttachmentParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetFramebufferAttachmentParameteriv(int,int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetFramebufferAttachmentParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def glResumeTransformFeedback(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glResumeTransformFeedback()"""
        super(GL30Interceptor, self).glResumeTransformFeedback()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def glGetFloatv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetFloatv(int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glGetFloatv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetVertexAttribIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribIiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetVertexAttribIiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glGenRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenRenderbuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenRenderbuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glEndTransformFeedback(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEndTransformFeedback()"""
        super(GL30Interceptor, self).glEndTransformFeedback()

    @overload
    def glIsVertexArray(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsVertexArray(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsVertexArray(__int.valueOf(arg0)))

    @overload
    def glGetUniformBlockIndex(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformBlockIndex(int,java.lang.String)"""
        return int.__wrap(super(__GL30Interceptor, self).glGetUniformBlockIndex(__int.valueOf(arg0), arg1))

    @override
    @overload
    def glPixelStorei(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glPixelStorei(int,int)"""
        super(__GL30Interceptor, self).glPixelStorei(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glLineWidth(self, arg0: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glLineWidth(float)"""
        super(__GL30Interceptor, self).glLineWidth(__float.valueOf(arg0))

    @override
    @overload
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribPointer(int,int,int,boolean,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glVertexAttribPointer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __int.valueOf(arg4), arg5)

    @override
    @overload
    def glProgramUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform1iv(int,int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glProgramUniform1iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glBindTransformFeedback(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindTransformFeedback(int,int)"""
        super(__GL30Interceptor, self).glBindTransformFeedback(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glBlendEquation(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendEquation(int)"""
        super(__GL30Interceptor, self).glBlendEquation(__int.valueOf(arg0))

    @override
    @overload
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4fv(int,int,boolean,float[],int)"""
        super(__GL30Interceptor, self).glUniformMatrix4fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3, __int.valueOf(arg4))

    @override
    @overload
    def glProgramUniformMatrix4x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix4x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glProgramUniformMatrix4x3fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glGenerateMipmap(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenerateMipmap(int)"""
        super(__GL30Interceptor, self).glGenerateMipmap(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'GLProfiler', arg1: 'GL31'):
        """public com.badlogic.gdx.graphics.profiling.GL31Interceptor(com.badlogic.gdx.graphics.profiling.GLProfiler,com.badlogic.gdx.graphics.GL31)"""
        val = __GL31Interceptor(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def glDispatchCompute(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glDispatchCompute(int,int,int)"""
        super(__GL31Interceptor, self).glDispatchCompute(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.profiling.GLInterceptor.reset()"""
        super(GLInterceptor, self).reset()

    @override
    @overload
    def glProgramUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glProgramUniformMatrix2fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glGenBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenBuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenBuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glProgramUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform4i(int,int,int,int,int,int)"""
        super(__GL31Interceptor, self).glProgramUniform4i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @overload
    def glIsQuery(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsQuery(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsQuery(__int.valueOf(arg0)))

    @override
    @overload
    def glGetTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetTexParameterfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glGetTexParameterfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2iv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform2iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteFramebuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteFramebuffer(int)"""
        super(__GL30Interceptor, self).glDeleteFramebuffer(__int.valueOf(arg0))

    @override
    @overload
    def glSamplerParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameteri(int,int,int)"""
        super(__GL30Interceptor, self).glSamplerParameteri(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glEnable(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glEnable(int)"""
        super(__GL30Interceptor, self).glEnable(__int.valueOf(arg0))

    @overload
    def glGetShaderInfoLog(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetShaderInfoLog(int)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetShaderInfoLog(__int.valueOf(arg0)))

    @override
    @overload
    def glUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4i(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glUniform4i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glProgramUniform2f(self, arg0: int, arg1: int, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform2f(int,int,float,float)"""
        super(__GL31Interceptor, self).glProgramUniform2f(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def glStencilFunc(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilFunc(int,int,int)"""
        super(__GL30Interceptor, self).glStencilFunc(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glDeleteTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTextures(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteTextures(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2fv(int,int,boolean,float[],int)"""
        super(__GL30Interceptor, self).glUniformMatrix2fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3, __int.valueOf(arg4))

    @override
    @overload
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage2D(int,int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glTexSubImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8))

    @overload
    def glGetProgramInfoLog(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetProgramInfoLog(int)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetProgramInfoLog(__int.valueOf(arg0)))

    @override
    @overload
    def glFrontFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFrontFace(int)"""
        super(__GL30Interceptor, self).glFrontFace(__int.valueOf(arg0))

    @override
    @overload
    def glSamplerParameterf(self, arg0: int, arg1: int, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameterf(int,int,float)"""
        super(__GL30Interceptor, self).glSamplerParameterf(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def glGetUniformiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetUniformiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetBufferParameteri64v(self, arg0: int, arg1: int, arg2: 'LongBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetBufferParameteri64v(int,int,java.nio.LongBuffer)"""
        super(__GL30Interceptor, self).glGetBufferParameteri64v(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @overload
    def glGetString(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetString(int)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetString(__int.valueOf(arg0)))

    @overload
    def glGetFragDataLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetFragDataLocation(int,java.lang.String)"""
        return int.__wrap(super(__GL30Interceptor, self).glGetFragDataLocation(__int.valueOf(arg0), arg1))

    @override
    @overload
    def glProgramUniform3ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform3ui(int,int,int,int,int)"""
        super(__GL31Interceptor, self).glProgramUniform3ui(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glProgramUniform4f(self, arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform4f(int,int,float,float,float,float)"""
        super(__GL31Interceptor, self).glProgramUniform4f(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5))

    @override
    @overload
    def glTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameterfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glTexParameterfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glGenSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenSamplers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenSamplers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glClearBufferfi(self, arg0: int, arg1: int, arg2: float, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearBufferfi(int,int,float,int)"""
        super(__GL30Interceptor, self).glClearBufferfi(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glUniformMatrix2x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix2x3fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def getShaderSwitches(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getShaderSwitches()"""
        return int.__wrap(super(GLInterceptor, self).getShaderSwitches())

    @override
    @overload
    def glUseProgramStages(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glUseProgramStages(int,int,int)"""
        super(__GL31Interceptor, self).glUseProgramStages(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glGenSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenSamplers(int,int[],int)"""
        super(__GL30Interceptor, self).glGenSamplers(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glRenderbufferStorageMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glRenderbufferStorageMultisample(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glRenderbufferStorageMultisample(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glTexStorage2DMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glTexStorage2DMultisample(int,int,int,int,int,boolean)"""
        super(__GL31Interceptor, self).glTexStorage2DMultisample(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __boolean.valueOf(arg5))

    @override
    @overload
    def glSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glSamplerParameterfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def getCalls(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GLInterceptor.getCalls()"""
        return int.__wrap(super(GLInterceptor, self).getCalls())

    @override
    @overload
    def glShaderBinary(self, arg0: int, arg1: 'IntBuffer', arg2: int, arg3: 'Buffer', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glShaderBinary(int,java.nio.IntBuffer,int,java.nio.Buffer,int)"""
        super(__GL30Interceptor, self).glShaderBinary(__int.valueOf(arg0), arg1, __int.valueOf(arg2), arg3, __int.valueOf(arg4))

    @override
    @overload
    def glProgramUniform1uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform1uiv(int,int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glProgramUniform1uiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDisableVertexAttribArray(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDisableVertexAttribArray(int)"""
        super(__GL30Interceptor, self).glDisableVertexAttribArray(__int.valueOf(arg0))

    @overload
    def glIsShader(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsShader(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsShader(__int.valueOf(arg0)))

    @override
    @overload
    def glProgramUniform2ui(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform2ui(int,int,int,int)"""
        super(__GL31Interceptor, self).glProgramUniform2ui(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glDeleteVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteVertexArrays(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteVertexArrays(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glFlush(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFlush()"""
        super(GL30Interceptor, self).glFlush()

    @override
    @overload
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenTransformFeedbacks(int,int[],int)"""
        super(__GL30Interceptor, self).glGenTransformFeedbacks(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glVertexAttrib4fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib4fv(int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glVertexAttrib4fv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glBindProgramPipeline(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glBindProgramPipeline(int)"""
        super(__GL31Interceptor, self).glBindProgramPipeline(__int.valueOf(arg0))

    @override
    @overload
    def glDeleteRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteRenderbuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteRenderbuffers(__int.valueOf(arg0), arg1)

    @overload
    def glGetProgramResourceName(self, arg0: int, arg1: int, arg2: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramResourceName(int,int,int)"""
        return str.__wrap(super(__GL31Interceptor, self).glGetProgramResourceName(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def glGenVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenVertexArrays(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenVertexArrays(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glDrawArraysInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawArraysInstanced(int,int,int,int)"""
        super(__GL30Interceptor, self).glDrawArraysInstanced(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3fv(int,int,float[],int)"""
        super(__GL30Interceptor, self).glUniform3fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @overload
    def glGetUniformLocation(self, arg0: int, arg1: str) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformLocation(int,java.lang.String)"""
        return int.__wrap(super(__GL30Interceptor, self).glGetUniformLocation(__int.valueOf(arg0), arg1))

    @override
    @overload
    def glShaderSource(self, arg0: int, arg1: str):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glShaderSource(int,java.lang.String)"""
        super(__GL30Interceptor, self).glShaderSource(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glProgramUniformMatrix3x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix3x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glProgramUniformMatrix3x4fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glBindFramebuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindFramebuffer(int,int)"""
        super(__GL30Interceptor, self).glBindFramebuffer(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glGetProgramResourceiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramResourceiv(int,int,int,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glGetProgramResourceiv(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, arg4, arg5)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def glValidateProgramPipeline(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glValidateProgramPipeline(int)"""
        super(__GL31Interceptor, self).glValidateProgramPipeline(__int.valueOf(arg0))

    @override
    @overload
    def glProgramUniform3uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform3uiv(int,int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glProgramUniform3uiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glVertexAttribFormat(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glVertexAttribFormat(int,int,int,boolean,int)"""
        super(__GL31Interceptor, self).glVertexAttribFormat(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glDrawElementsInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawElementsInstanced(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glDrawElementsInstanced(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def resolveErrorNumber(arg0: int) -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.profiling.GLInterceptor.resolveErrorNumber(int)"""
        return str.__wrap(__GLInterceptor.resolveErrorNumber(__int.valueOf(arg0)))

    @override
    @overload
    def glTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glTexParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glProgramUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform2iv(int,int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glProgramUniform2iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetUniformfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glGetUniformfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform2f(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2f(int,float,float)"""
        super(__GL30Interceptor, self).glUniform2f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def glBeginQuery(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBeginQuery(int,int)"""
        super(__GL30Interceptor, self).glBeginQuery(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glProgramUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform1fv(int,int,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glProgramUniform1fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glBlitFramebuffer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlitFramebuffer(int,int,int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glBlitFramebuffer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9))

    @override
    @overload
    def glProgramUniform1i(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform1i(int,int,int)"""
        super(__GL31Interceptor, self).glProgramUniform1i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glDeleteQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteQueries(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteQueries(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glBindImageTexture(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glBindImageTexture(int,int,int,boolean,int,int,int)"""
        super(__GL31Interceptor, self).glBindImageTexture(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def glUseProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUseProgram(int)"""
        super(__GL30Interceptor, self).glUseProgram(__int.valueOf(arg0))

    @override
    @overload
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2fv(int,int,float[],int)"""
        super(__GL30Interceptor, self).glUniform2fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glProgramUniform3f(self, arg0: int, arg1: int, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform3f(int,int,float,float,float)"""
        super(__GL31Interceptor, self).glProgramUniform3f(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix2fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1fv(int,int,float[],int)"""
        super(__GL30Interceptor, self).glUniform1fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3fv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniform3fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def getVertexCount(self) -> 'math.FloatCounter':
        """public com.badlogic.gdx.math.FloatCounter com.badlogic.gdx.graphics.profiling.GLInterceptor.getVertexCount()"""
        return 'math.FloatCounter'.__wrap(super(GLInterceptor, self).getVertexCount())

    @override
    @overload
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawElements(int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glDrawElements(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def glReadPixels(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'Buffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glReadPixels(int,int,int,int,int,int,java.nio.Buffer)"""
        super(__GL30Interceptor, self).glReadPixels(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), arg6)

    @override
    @overload
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage3D(int,int,int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glTexImage3D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9))

    @override
    @overload
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1iv(int,int,int[],int)"""
        super(__GL30Interceptor, self).glUniform1iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glDeleteRenderbuffer(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteRenderbuffer(int)"""
        super(__GL30Interceptor, self).glDeleteRenderbuffer(__int.valueOf(arg0))

    @override
    @overload
    def glCreateProgram(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCreateProgram()"""
        return int.__wrap(super(GL30Interceptor, self).glCreateProgram())

    @override
    @overload
    def glProgramUniformMatrix4x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix4x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glProgramUniformMatrix4x2fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glDeleteShader(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteShader(int)"""
        super(__GL30Interceptor, self).glDeleteShader(__int.valueOf(arg0))

    @overload
    def glIsTransformFeedback(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsTransformFeedback(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsTransformFeedback(__int.valueOf(arg0)))

    @override
    @overload
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix3fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glHint(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glHint(int,int)"""
        super(__GL30Interceptor, self).glHint(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glGetVertexAttribIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribIuiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetVertexAttribIuiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDispatchComputeIndirect(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glDispatchComputeIndirect(long)"""
        super(__GL31Interceptor, self).glDispatchComputeIndirect(__long.valueOf(arg0))

    @override
    @overload
    def glProgramParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glProgramParameteri(int,int,int)"""
        super(__GL30Interceptor, self).glProgramParameteri(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glCompileShader(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCompileShader(int)"""
        super(__GL30Interceptor, self).glCompileShader(__int.valueOf(arg0))

    @override
    @overload
    def glBindSampler(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindSampler(int,int)"""
        super(__GL30Interceptor, self).glBindSampler(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glFinish(self):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFinish()"""
        super(GL30Interceptor, self).glFinish()

    @overload
    def glCheckFramebufferStatus(self, arg0: int) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCheckFramebufferStatus(int)"""
        return int.__wrap(super(__GL30Interceptor, self).glCheckFramebufferStatus(__int.valueOf(arg0)))

    @override
    @overload
    def glUniformMatrix2x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix2x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix2x4fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glSampleMaski(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glSampleMaski(int,int)"""
        super(__GL31Interceptor, self).glSampleMaski(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def glGetProgramPipelineInfoLog(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramPipelineInfoLog(int)"""
        return str.__wrap(super(__GL31Interceptor, self).glGetProgramPipelineInfoLog(__int.valueOf(arg0)))

    @override
    @overload
    def glGenFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenFramebuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenFramebuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniform4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4f(int,float,float,float,float)"""
        super(__GL30Interceptor, self).glUniform4f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4fv(int,int,float[],int)"""
        super(__GL30Interceptor, self).glUniform4fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glGetVertexAttribfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribfv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glGetVertexAttribfv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribPointer(int,int,int,boolean,int,int)"""
        super(__GL30Interceptor, self).glVertexAttribPointer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @override
    @overload
    def glRenderbufferStorage(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glRenderbufferStorage(int,int,int,int)"""
        super(__GL30Interceptor, self).glRenderbufferStorage(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glStencilMaskSeparate(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilMaskSeparate(int,int)"""
        super(__GL30Interceptor, self).glStencilMaskSeparate(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glGetInteger64v(self, arg0: int, arg1: 'LongBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetInteger64v(int,java.nio.LongBuffer)"""
        super(__GL30Interceptor, self).glGetInteger64v(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glUniformMatrix4x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix4x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix4x2fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glFramebufferParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glFramebufferParameteri(int,int,int)"""
        super(__GL31Interceptor, self).glFramebufferParameteri(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glDepthRangef(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDepthRangef(float,float)"""
        super(__GL30Interceptor, self).glDepthRangef(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def glGetTexLevelParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetTexLevelParameteriv(int,int,int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glGetTexLevelParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def glDeleteSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteSamplers(int,int[],int)"""
        super(__GL30Interceptor, self).glDeleteSamplers(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glCopyTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyTexImage2D(int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glCopyTexImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7))

    @override
    @overload
    def glValidateProgram(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glValidateProgram(int)"""
        super(__GL30Interceptor, self).glValidateProgram(__int.valueOf(arg0))

    @override
    @overload
    def glProgramUniform4uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform4uiv(int,int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glProgramUniform4uiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glBlendFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendFuncSeparate(int,int,int,int)"""
        super(__GL30Interceptor, self).glBlendFuncSeparate(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3fv(int,int,boolean,float[],int)"""
        super(__GL30Interceptor, self).glUniformMatrix3fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3, __int.valueOf(arg4))

    @override
    @overload
    def glCopyBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyBufferSubData(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glCopyBufferSubData(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glClearColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glClearColor(float,float,float,float)"""
        super(__GL30Interceptor, self).glClearColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def glVertexAttribDivisor(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribDivisor(int,int)"""
        super(__GL30Interceptor, self).glVertexAttribDivisor(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glGetUniformuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformuiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetUniformuiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniformMatrix3x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformMatrix3x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniformMatrix3x4fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glGetProgramInterfaceiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetProgramInterfaceiv(int,int,int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glGetProgramInterfaceiv(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def glGenFramebuffer(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenFramebuffer()"""
        return int.__wrap(super(GL30Interceptor, self).glGenFramebuffer())

    @override
    @overload
    def glVertexBindingDivisor(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glVertexBindingDivisor(int,int)"""
        super(__GL31Interceptor, self).glVertexBindingDivisor(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glDrawBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDrawBuffers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDrawBuffers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glDeleteProgramPipelines(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glDeleteProgramPipelines(int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glDeleteProgramPipelines(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glViewport(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glViewport(int,int,int,int)"""
        super(__GL30Interceptor, self).glViewport(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glBeginTransformFeedback(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBeginTransformFeedback(int)"""
        super(__GL30Interceptor, self).glBeginTransformFeedback(__int.valueOf(arg0))

    @override
    @overload
    def glGenQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGenQueries(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGenQueries(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetMultisamplefv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetMultisamplefv(int,int,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glGetMultisamplefv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glActiveTexture(self, arg0: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glActiveTexture(int)"""
        super(__GL30Interceptor, self).glActiveTexture(__int.valueOf(arg0))

    @override
    @overload
    def glDetachShader(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDetachShader(int,int)"""
        super(__GL30Interceptor, self).glDetachShader(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glSamplerParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTransformFeedbacks(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteTransformFeedbacks(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glProgramUniform2i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform2i(int,int,int,int)"""
        super(__GL31Interceptor, self).glProgramUniform2i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glBlendColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendColor(float,float,float,float)"""
        super(__GL30Interceptor, self).glBlendColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def glUniform1i(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1i(int,int)"""
        super(__GL30Interceptor, self).glUniform1i(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexImage2D(int,int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glTexImage2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8))

    @override
    @overload
    def glBlendEquationSeparate(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendEquationSeparate(int,int)"""
        super(__GL30Interceptor, self).glBlendEquationSeparate(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def glGetActiveUniform(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer') -> str:
        """public java.lang.String com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetActiveUniform(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return str.__wrap(super(__GL30Interceptor, self).glGetActiveUniform(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3))

    @override
    @overload
    def glProgramUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform2fv(int,int,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glProgramUniform2fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4iv(int,int,int[],int)"""
        super(__GL30Interceptor, self).glUniform4iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glBindRenderbuffer(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBindRenderbuffer(int,int)"""
        super(__GL30Interceptor, self).glBindRenderbuffer(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glUniform1f(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1f(int,float)"""
        super(__GL30Interceptor, self).glUniform1f(__int.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def glCopyTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glCopyTexSubImage3D(int,int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glCopyTexSubImage3D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8))

    @override
    @overload
    def glVertexAttribIFormat(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glVertexAttribIFormat(int,int,int,int)"""
        super(__GL31Interceptor, self).glVertexAttribIFormat(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glScissor(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glScissor(int,int,int,int)"""
        super(__GL30Interceptor, self).glScissor(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glStencilFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilFuncSeparate(int,int,int,int)"""
        super(__GL30Interceptor, self).glStencilFuncSeparate(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glProgramUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform3iv(int,int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glProgramUniform3iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glVertexAttrib3fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib3fv(int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glVertexAttrib3fv(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glVertexAttrib2f(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttrib2f(int,float,float)"""
        super(__GL30Interceptor, self).glVertexAttrib2f(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,int)"""
        super(__GL30Interceptor, self).glTexSubImage3D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10))

    @override
    @overload
    def glProgramUniformMatrix2x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix2x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glProgramUniformMatrix2x3fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @overload
    def glMapBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Buffer':
        """public java.nio.Buffer com.badlogic.gdx.graphics.profiling.GL30Interceptor.glMapBufferRange(int,int,int,int)"""
        return 'Buffer'.__wrap(super(__GL30Interceptor, self).glMapBufferRange(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def glGetError(self) -> int:
        """public int com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetError()"""
        return int.__wrap(super(GL30Interceptor, self).glGetError())

    @override
    @overload
    def glGetShaderPrecisionFormat(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetShaderPrecisionFormat(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetShaderPrecisionFormat(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform3iv(int,int,int[],int)"""
        super(__GL30Interceptor, self).glUniform3iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glBlendFunc(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBlendFunc(int,int)"""
        super(__GL30Interceptor, self).glBlendFunc(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def glFramebufferRenderbuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFramebufferRenderbuffer(int,int,int,int)"""
        super(__GL30Interceptor, self).glFramebufferRenderbuffer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def glGetUniformIndices(self, arg0: int, arg1: 'String', arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetUniformIndices(int,java.lang.String[],java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetUniformIndices(__int.valueOf(arg0), arg1, arg2)

    @override
    @overload
    def glGetProgramiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetProgramiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetProgramiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4fv(int,int,java.nio.FloatBuffer)"""
        super(__GL30Interceptor, self).glUniform4fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glGetFramebufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glGetFramebufferParameteriv(int,int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glGetFramebufferParameteriv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glFramebufferTextureLayer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFramebufferTextureLayer(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glFramebufferTextureLayer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glProgramUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glProgramUniformMatrix4fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glProgramUniformMatrix3x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniformMatrix3x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glProgramUniformMatrix3x2fv(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3)

    @override
    @overload
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform4iv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform4iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform2iv(int,int,int[],int)"""
        super(__GL30Interceptor, self).glUniform2iv(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glProgramUniform2uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform2uiv(int,int,java.nio.IntBuffer)"""
        super(__GL31Interceptor, self).glProgramUniform2uiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glDeleteQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteQueries(int,int[],int)"""
        super(__GL30Interceptor, self).glDeleteQueries(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def glTexParameteri(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glTexParameteri(int,int,int)"""
        super(__GL30Interceptor, self).glTexParameteri(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glUniformBlockBinding(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniformBlockBinding(int,int,int)"""
        super(__GL30Interceptor, self).glUniformBlockBinding(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glGetVertexAttribiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetVertexAttribiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetVertexAttribiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glInvalidateFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glInvalidateFramebuffer(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glInvalidateFramebuffer(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @overload
    def glIsProgramPipeline(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL31Interceptor.glIsProgramPipeline(int)"""
        return bool.__wrap(super(__GL31Interceptor, self).glIsProgramPipeline(__int.valueOf(arg0)))

    @override
    @overload
    def glVertexAttribIPointer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glVertexAttribIPointer(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glVertexAttribIPointer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glStencilOp(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glStencilOp(int,int,int)"""
        super(__GL30Interceptor, self).glStencilOp(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def glBufferData(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glBufferData(int,int,java.nio.Buffer,int)"""
        super(__GL30Interceptor, self).glBufferData(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @override
    @overload
    def glProgramUniform1f(self, arg0: int, arg1: int, arg2: float):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform1f(int,int,float)"""
        super(__GL31Interceptor, self).glProgramUniform1f(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def glUniform1uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glUniform1uiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glUniform1uiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glSampleCoverage(self, arg0: float, arg1: bool):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glSampleCoverage(float,boolean)"""
        super(__GL30Interceptor, self).glSampleCoverage(__float.valueOf(arg0), __boolean.valueOf(arg1))

    @override
    @overload
    def glFramebufferTexture2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glFramebufferTexture2D(int,int,int,int,int)"""
        super(__GL30Interceptor, self).glFramebufferTexture2D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def glDeleteSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteSamplers(int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glDeleteSamplers(__int.valueOf(arg0), arg1)

    @override
    @overload
    def glGetShaderiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glGetShaderiv(int,int,java.nio.IntBuffer)"""
        super(__GL30Interceptor, self).glGetShaderiv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def glProgramUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public void com.badlogic.gdx.graphics.profiling.GL31Interceptor.glProgramUniform4fv(int,int,java.nio.FloatBuffer)"""
        super(__GL31Interceptor, self).glProgramUniform4fv(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @overload
    def glIsSampler(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.graphics.profiling.GL30Interceptor.glIsSampler(int)"""
        return bool.__wrap(super(__GL30Interceptor, self).glIsSampler(__int.valueOf(arg0)))

    @override
    @overload
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public void com.badlogic.gdx.graphics.profiling.GL30Interceptor.glDeleteTransformFeedbacks(int,int[],int)"""
        super(__GL30Interceptor, self).glDeleteTransformFeedbacks(__int.valueOf(arg0), arg1, __int.valueOf(arg2))