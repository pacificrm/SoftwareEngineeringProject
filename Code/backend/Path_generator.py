import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.text import Text
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

def path_generator(course_data, image_filename):
    plt.switch_backend('agg')  # Use non-interactive backend

    fig, ax = plt.subplots()
    canvas = FigureCanvas(fig)

    rect_width = 1.5
    rect_height = 1.0
    gap = 0.5
    spacing = rect_height + gap
    center_x = 0.5 * rect_width
    num_terms = len(course_data)

    for i, (term, courses) in enumerate(reversed(list(course_data.items()))):
        ax.text(center_x - 0.6, (i + 0.5) * spacing, term, ha='left', va='center', fontweight='bold', fontsize=10, color='purple')
        
        rect = patches.Rectangle((center_x, i * spacing), rect_width, rect_height, edgecolor='blue', linewidth=2, facecolor='lightblue')
        ax.add_patch(rect)
        
        courses_text = "\n".join(" | ".join(courses[j:j + 2]) for j in range(0, len(courses), 2))
        courses_text_obj = Text(center_x + 0.5 * rect_width, (i + 0.5) * spacing, f'{courses_text}', 
                                ha='center', va='top', color='black', fontsize=8, fontweight='bold', multialignment='center')
        ax.add_artist(courses_text_obj)

    for i in range(1, num_terms):
        arrow = patches.FancyArrowPatch((1.5, i * spacing), (1.5, (i - 1) * spacing + rect_height), 
                                        color='red', mutation_scale=15, arrowstyle='-|>', linewidth=2)
        ax.add_patch(arrow)

    # Manually adjust the y-limits
    ax.set_ylim(-gap, len(course_data) * spacing)

    ax.set_xlim(0, 2 * rect_width)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.title('Learning Path', fontweight='bold', color='red')

    folder_path = os.path.join(os.getcwd(), "learning_path")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    image_path = os.path.join(folder_path, image_filename)
    plt.savefig(image_path)
    
    # Close the figure to release resources
    plt.close(fig)

    print(f"Image saved at: {image_path}")
