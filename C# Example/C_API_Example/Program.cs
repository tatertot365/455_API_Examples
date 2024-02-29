using System.Text.Json;
using Microsoft.ML.OnnxRuntime.Tensors;
using Microsoft.ML.OnnxRuntime;
using Newtonsoft.Json;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddCors(p => p.AddPolicy("corsapp", builder =>
{
    builder.WithOrigins("*").AllowAnyMethod().AllowAnyHeader();
}));

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();

}

app.UseCors("corsapp");

app.MapPost("/charges_api", async (HttpRequest request) =>
{
    var body = await request.ReadFromJsonAsync<JsonDocument>();

    string age = body.RootElement.GetProperty("age").GetString();
    string bmi = body.RootElement.GetProperty("bmi").GetString();
    string children = body.RootElement.GetProperty("children").GetString();

    var data = new InputData() { Age = float.Parse(age), Bmi = float.Parse(bmi), Children = float.Parse(children) };

    NamedOnnxValue.CreateFromTensor("float_input", data.AsTensor());

    InferenceSession session = new InferenceSession("/Users/tategillespie/Desktop/455 TA/Flask Example/C# Example/C_API_Example/sample_model.onnx");

    var result = session.Run(new List<NamedOnnxValue>
    {
        NamedOnnxValue.CreateFromTensor("float_input", data.AsTensor())
    });

    Tensor<float> score = result.First().AsTensor<float>();
    var prediction = new OnnxOutput { prediction = score.First() };

    result.Dispose();

    Console.WriteLine($"Predicted Charges: {prediction.prediction}");


    return Results.Text( JsonConvert.SerializeObject(prediction), contentType: "application/json");
});

app.Run();

public class InputData
{
    public float Age { get; set; }
    public float Bmi { get; set; }
    public float Children { get; set; }

    public Tensor<float> AsTensor()
    {
        float[] data = new float[]
        {
            Age, Bmi, Children
        };
        int[] dimensions = new int[] { 1, 3 };
        return new DenseTensor<float>(data, dimensions);
    }
}

public class OnnxOutput
{
    public float prediction { get; set; }
}
