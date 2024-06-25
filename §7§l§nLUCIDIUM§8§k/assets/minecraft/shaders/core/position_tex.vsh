#version 150

in vec3 Position;
in vec2 UV0;

uniform mat4 ModelViewMat;
uniform mat4 ProjMat;
uniform sampler2D Sampler0;

out vec2 texCoord0;

void main() {
    
    ivec2 samplepos = ivec2(UV0 * textureSize(Sampler0, 0));
    if (gl_VertexID % 4 == 1) {
        samplepos -= ivec2(0, 256);
    } else if (gl_VertexID % 4 == 2) {
        samplepos -= ivec2(208, 256);
    } else if (gl_VertexID % 4 == 3) {
        samplepos -= ivec2(208, 0);
    }
    
    if (ivec4(texelFetch(Sampler0, samplepos, 0) * 255.0) == ivec4(255, 0, 0, 0)) {
        gl_Position = ProjMat * ModelViewMat * vec4(Position + vec3(0,0,300), 1.0);
    } else {
        gl_Position = ProjMat * ModelViewMat * vec4(Position, 1.0);
    }

    texCoord0 = UV0;
}
