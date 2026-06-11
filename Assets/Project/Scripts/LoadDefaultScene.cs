using UnityEditor;
using UnityEditor.SceneManagement;

public class MultiSceneSetup
{
    [MenuItem("Tools/Load Base Configuration")]
    public static void LoadSimulationScenes()
    {
        // Close any open scenes first to start fresh
        EditorSceneManager.NewScene(NewSceneSetup.EmptyScene);

        // Load your scenes (replace paths with your actual asset paths)
        EditorSceneManager.OpenScene("Assets/Project/Scenes/moon_base.unity", OpenSceneMode.Single);
    }
}